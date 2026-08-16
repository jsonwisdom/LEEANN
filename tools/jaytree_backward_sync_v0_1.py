#!/usr/bin/env python3
"""JayTree backward-sync audit v0.1.

Produces a replay receipt from Git history for five fixed windows:
TODAY, YESTERDAY, LAST_7_DAYS, LAST_30_DAYS, LAST_3_YEARS.

The script is measurement-only. It does not mutate Git history.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from datetime import datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

LOCAL_TZ = ZoneInfo("America/Chicago")


def git(*args: str, allow_empty: bool = False) -> str:
    p = subprocess.run(["git", *args], text=True, capture_output=True)
    if p.returncode != 0:
        if allow_empty:
            return ""
        raise RuntimeError(p.stderr.strip() or f"git {' '.join(args)} failed")
    return p.stdout.strip()


def iso(dt: datetime) -> str:
    return dt.isoformat(timespec="seconds")


def utc_iso(dt: datetime) -> str:
    return dt.astimezone(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def commit_list(start: datetime, end: datetime) -> list[str]:
    raw = git(
        "log",
        f"--since={utc_iso(start)}",
        f"--until={utc_iso(end)}",
        "--pretty=format:%H",
        allow_empty=True,
    )
    return [x for x in raw.splitlines() if x]


def one_before(moment: datetime) -> str | None:
    out = git("rev-list", "-1", f"--before={utc_iso(moment)}", "HEAD", allow_empty=True)
    return out or None


def changed_files(base: str | None, head: str | None, commits_desc: list[str]) -> list[str]:
    if not head:
        return []
    if base:
        out = git("diff", "--name-only", base, head, allow_empty=True)
        return sorted({x for x in out.splitlines() if x})

    # No commit exists before this window in the reachable history. In that case
    # there is no valid diff base. Aggregate the file names touched by every
    # commit in the window instead of pretending the last commit represents the
    # whole window.
    names: set[str] = set()
    for sha in commits_desc:
        out = git("show", "--pretty=format:", "--name-only", sha, allow_empty=True)
        names.update(x for x in out.splitlines() if x)
    return sorted(names)


def make_window(window_id: str, start: datetime, end: datetime) -> dict:
    commits_desc = commit_list(start, end)
    commits_asc = list(reversed(commits_desc))
    first = commits_asc[0] if commits_asc else None
    last = commits_desc[0] if commits_desc else None
    base = one_before(start)

    if commits_desc:
        status = "PASS"
    elif base:
        status = "EMPTY_WINDOW"
    else:
        status = "GAP_HISTORY"

    return {
        "window_id": window_id,
        "start_local": iso(start),
        "end_local": iso(end),
        "start_utc": utc_iso(start),
        "end_utc": utc_iso(end),
        "base_before_window_sha": base,
        "first_commit_in_window": first,
        "last_commit_in_window": last,
        "commit_count": len(commits_desc),
        "changed_files": changed_files(base, last, commits_desc),
        "status": status,
    }


def resolve_windows(now_local: datetime) -> list[tuple[str, datetime, datetime]]:
    today_start = now_local.replace(hour=0, minute=0, second=0, microsecond=0)
    yesterday_start = today_start - timedelta(days=1)
    yesterday_end = today_start - timedelta(seconds=1)
    seven_start = today_start - timedelta(days=7)
    thirty_start = today_start - timedelta(days=30)
    three_year_start = today_start.replace(year=today_start.year - 3)

    return [
        ("TODAY", today_start, now_local),
        ("YESTERDAY", yesterday_start, yesterday_end),
        ("LAST_7_DAYS", seven_start, yesterday_end),
        ("LAST_30_DAYS", thirty_start, yesterday_end),
        ("LAST_3_YEARS", three_year_start, yesterday_end),
    ]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="build/jaytree/JAYTREE_RECEIPT.json")
    ap.add_argument("--now", help="optional ISO timestamp for deterministic replay")
    args = ap.parse_args()

    now_local = datetime.fromisoformat(args.now).astimezone(LOCAL_TZ) if args.now else datetime.now(LOCAL_TZ)
    head = git("rev-parse", "HEAD")
    remote = git("config", "--get", "remote.origin.url", allow_empty=True) or "UNKNOWN_HOLD"
    branch = git("rev-parse", "--abbrev-ref", "HEAD", allow_empty=True) or "UNKNOWN_HOLD"

    windows = [make_window(wid, start, end) for wid, start, end in resolve_windows(now_local)]

    payload = {
        "schema": "JAYTREE_BACKWARD_SYNC_RECEIPT_V0_1",
        "generated_at": utc_iso(now_local),
        "timezone": "America/Chicago",
        "repository": remote,
        "branch": branch,
        "head_sha": head,
        "windows": windows,
        "invariants": [
            "SYNC_CLAIM != SYNC_RECEIPT",
            "REMOTE_UPDATED != LOCAL_MACHINE_PULLED",
            "PUBLIC_REPO_SCAN != PRIVATE_REPO_SCAN",
            "WINDOW_SUMMARY != CAUSATION",
            "MISSING_HISTORY != NO_HISTORY",
            "AUTHORITY_CREATED = FALSE",
        ],
        "authority_created": False,
    }

    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    payload["receipt_sha256"] = hashlib.sha256(canonical).hexdigest()

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
