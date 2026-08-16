#!/usr/bin/env python3
"""Inventory the JSONWisdom GitHub estate for JayTree rollout.

Without an explicit account-scoped token this script uses the public user API and
marks coverage PUBLIC_ONLY. With JAYTREE_ESTATE_TOKEN it uses /user/repos and can
include repositories visible to that token.

This tool reports; it does not modify repositories.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path


def request_json(url: str, token: str | None):
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "JayTree-Inventory-v0.1",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def paginate(base_url: str, token: str | None) -> list[dict]:
    page = 1
    items: list[dict] = []
    while True:
        sep = "&" if "?" in base_url else "?"
        data = request_json(f"{base_url}{sep}per_page=100&page={page}", token)
        if not data:
            break
        items.extend(data)
        if len(data) < 100:
            break
        page += 1
    return items


def classify(repo: dict) -> list[str]:
    labels = []
    if repo.get("archived"):
        labels.append("ARCHIVED")
    if int(repo.get("size", 0) or 0) == 0:
        labels.append("EMPTY")
    else:
        labels.append("ACTIVE_NONEMPTY" if not repo.get("archived") else "NONEMPTY")
    if repo.get("private"):
        labels.append("PRIVATE")
    if repo.get("default_branch") not in {"main", "master"}:
        labels.append("DEFAULT_BRANCH_NONSTANDARD")
    return labels


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--owner", default="jsonwisdom")
    ap.add_argument("--out", default="build/jaytree/JSONWISDOM_ESTATE_INVENTORY.json")
    args = ap.parse_args()

    token = os.environ.get("JAYTREE_ESTATE_TOKEN") or None
    if token:
        coverage = "ACCOUNT_TOKEN_SCOPE"
        base = "https://api.github.com/user/repos?affiliation=owner"
    else:
        coverage = "PUBLIC_ONLY"
        owner = urllib.parse.quote(args.owner)
        base = f"https://api.github.com/users/{owner}/repos?type=owner"

    repos = paginate(base, token)
    rows = []
    for r in sorted(repos, key=lambda x: x.get("full_name", "").lower()):
        rows.append({
            "full_name": r.get("full_name"),
            "visibility": r.get("visibility", "private" if r.get("private") else "public"),
            "private": bool(r.get("private")),
            "default_branch": r.get("default_branch"),
            "created_at": r.get("created_at"),
            "updated_at": r.get("updated_at"),
            "pushed_at": r.get("pushed_at"),
            "size_kb": r.get("size"),
            "archived": bool(r.get("archived")),
            "classification": classify(r),
        })

    payload = {
        "schema": "JAYTREE_JSONWISDOM_ESTATE_INVENTORY_V0_1",
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z"),
        "owner": args.owner,
        "coverage": coverage,
        "repo_count_observed": len(rows),
        "private_coverage_claim": "TOKEN_SCOPED" if token else "NOT_MEASURED",
        "repos": rows,
        "invariants": [
            "PUBLIC_REPO_SCAN != PRIVATE_REPO_SCAN",
            "REPO_PRESENT != REPO_HEALTHY",
            "WORKFLOW_PRESENT != WORKFLOW_PASS",
            "EMPTY_REPO != FAILED_REPO",
            "AUTHORITY_CREATED = FALSE",
        ],
        "authority_created": False,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["receipt_sha256"] = hashlib.sha256(canonical).hexdigest()

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
