#!/usr/bin/env python3
"""Alabama Colonel Test v0.2 — byte-by-byte USAF Knowledge Management.

Public educational test only.

v0.1 exposed an environmental assumption: official Air Force pages returned HTTP 403
from GitHub-hosted runners. v0.2 preserves that failure as evidence and separates:

1. deterministic byte mechanics on a frozen public-source packet; and
2. live transport/source observations.

A transport denial is HOLD, not a false-claim verdict.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_MANIFEST = ROOT / "fixtures/leeann/ALABAMA_COLONEL_KM_TEST_MANIFEST_V0_2.json"
DEFAULT_OUT = ROOT / "build/receipts/ALABAMA_COLONEL_KM_TEST_V0_2.json"
USER_AGENT = "Mozilla/5.0 jsonwisdom-leeann-public-km-test-v0.2"


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def one_byte_mutation(data: bytes) -> tuple[bytes, int]:
    if not data:
        raise ValueError("empty packet")
    idx = len(data) // 2
    changed = bytearray(data)
    changed[idx] ^= 0x01
    return bytes(changed), idx


def byte_diff_count(a: bytes, b: bytes) -> int:
    common = min(len(a), len(b))
    return sum(1 for i in range(common) if a[i] != b[i]) + abs(len(a) - len(b))


def fetch(url: str, timeout: int = 30) -> tuple[int, bytes, str]:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "text/html,application/xhtml+xml,*/*;q=0.8",
        },
    )
    with urllib.request.urlopen(req, timeout=timeout) as response:
        return int(getattr(response, "status", response.getcode())), response.read(), response.geturl()


def controlled_edge(packet_bytes: bytes) -> dict[str, Any]:
    mutated, idx = one_byte_mutation(packet_bytes)
    s0 = sha256(packet_bytes)
    s1 = sha256(mutated)
    diff = byte_diff_count(packet_bytes, mutated)
    replay = bytearray(packet_bytes)
    replay[idx] ^= 0x01
    replay_bytes = bytes(replay)
    return {
        "S0_sha256": s0,
        "interaction": "XOR_SINGLE_BYTE_WITH_0x01",
        "interaction_index": idx,
        "S1_sha256": s1,
        "measured_byte_differences": diff,
        "digest_changed": s0 != s1,
        "replay_sha256": sha256(replay_bytes),
        "replay_matches_S1": replay_bytes == mutated,
        "derivation_edge_supported": True,
        "causal_edge_supported_for_test_transition": True,
        "reason": "The interaction is controlled, declared, measured, and independently replayed within the test.",
    }


def probe_live(source: dict[str, Any], hold_statuses: set[int], fail_statuses: set[int]) -> dict[str, Any]:
    result: dict[str, Any] = {
        "id": source["id"],
        "url": source["url"],
        "authority_created": False,
    }
    try:
        status, body, final_url = fetch(source["url"])
    except urllib.error.HTTPError as exc:
        status = int(exc.code)
        result["http_status"] = status
        result["transport_error"] = f"HTTPError: {exc}"
        if status in hold_statuses:
            result["state"] = "ACCESS_RESTRICTED_HOLD"
        elif status in fail_statuses:
            result["state"] = "SOURCE_ENDPOINT_FAIL"
        else:
            result["state"] = "UNCLASSIFIED_TRANSPORT_HOLD"
        return result
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        result.update({
            "transport_error": f"{type(exc).__name__}: {exc}",
            "state": "TRANSPORT_ENVIRONMENT_HOLD",
        })
        return result

    text = body.decode("utf-8", errors="replace")
    markers = {m: m.lower() in text.lower() for m in source.get("required_markers", [])}
    result.update({
        "http_status": status,
        "final_url": final_url,
        "bytes": len(body),
        "sha256": sha256(body),
        "markers": markers,
        "state": "LIVE_SOURCE_OBSERVED" if status == 200 and all(markers.values()) else "LIVE_SOURCE_CONTENT_HOLD",
    })
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", default=str(DEFAULT_MANIFEST))
    parser.add_argument("--out", default=str(DEFAULT_OUT))
    args = parser.parse_args()

    manifest_path = Path(args.manifest)
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    packet_path = ROOT / manifest["frozen_packet"]
    packet_bytes = packet_path.read_bytes()
    packet_json = json.loads(packet_bytes.decode("utf-8"))

    packet_hash = sha256(packet_bytes)
    packet_roundtrip = json.loads(packet_bytes.decode("utf-8")) == packet_json
    ids_unique = len({i["id"] for i in packet_json["items"]}) == len(packet_json["items"])
    source_classes_present = all(i.get("source_class") for i in packet_json["items"])
    temporal_classes_present = all(i.get("temporal_class") for i in packet_json["items"])

    edge = controlled_edge(packet_bytes)
    deterministic_pass = all([
        packet_roundtrip,
        ids_unique,
        source_classes_present,
        temporal_classes_present,
        edge["measured_byte_differences"] == 1,
        edge["digest_changed"],
        edge["replay_matches_S1"],
    ])

    required = manifest["required_invariants"]
    expected_invariants = {
        "byte_change_must_be_detectable": True,
        "controlled_transform_can_support_causal_edge": True,
        "http_200_equals_truth": False,
        "http_403_equals_false_claim": False,
        "official_source_equals_current_forever": False,
        "historical_article_equals_current_policy": False,
        "hash_match_equals_story_truth": False,
        "authority_created": False,
    }
    invariant_checks = [
        {
            "check": k,
            "expected": v,
            "actual": required.get(k),
            "pass": required.get(k) == v,
        }
        for k, v in expected_invariants.items()
    ]
    invariant_pass = all(x["pass"] for x in invariant_checks)

    hold_statuses = set(manifest["transport_policy"]["hold_statuses"])
    fail_statuses = set(manifest["transport_policy"]["fail_statuses"])
    live = [probe_live(s, hold_statuses, fail_statuses) for s in manifest["live_sources"]]

    hard_live_fail = any(x["state"] == "SOURCE_ENDPOINT_FAIL" for x in live)
    live_hold = any("HOLD" in x["state"] for x in live)
    live_observed = sum(1 for x in live if x["state"] == "LIVE_SOURCE_OBSERVED")

    if not deterministic_pass or not invariant_pass or hard_live_fail:
        status = "FAIL"
    elif live_hold:
        status = "PASS_WITH_HOLDS"
    else:
        status = "PASS"

    receipt = {
        "receipt_type": "ALABAMA_COLONEL_KM_TEST_RECEIPT",
        "version": "0.2.0",
        "test_name": "The Alabama Colonel Test of Byte-by-Byte USAF Knowledge Management",
        "classification": "PUBLIC_EDUCATIONAL_TEST",
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "repository": os.environ.get("GITHUB_REPOSITORY", "jsonwisdom/LEEANN"),
        "commit_sha": os.environ.get("GITHUB_SHA", "LOCAL_OR_UNKNOWN"),
        "status": status,
        "prior_failure_learning": {
            "v0_1_observation": "Official Air Force pages returned HTTP 403 to the GitHub-hosted runner.",
            "correction": "Transport denial is typed as ENVIRONMENTAL_HOLD rather than claim falsity.",
        },
        "frozen_packet": {
            "path": str(packet_path.relative_to(ROOT)),
            "bytes": len(packet_bytes),
            "sha256": packet_hash,
            "json_roundtrip": packet_roundtrip,
            "ids_unique": ids_unique,
            "source_classes_present": source_classes_present,
            "temporal_classes_present": temporal_classes_present,
        },
        "girl_physics_transition": edge,
        "invariant_checks": invariant_checks,
        "live_environment_probe": live,
        "summary": {
            "deterministic_byte_mechanics": "PASS" if deterministic_pass else "FAIL",
            "invariants": "PASS" if invariant_pass else "FAIL",
            "live_source_count": len(live),
            "live_sources_observed": live_observed,
            "environmental_holds": sum(1 for x in live if "HOLD" in x["state"]),
            "source_endpoint_failures": sum(1 for x in live if x["state"] == "SOURCE_ENDPOINT_FAIL"),
            "facts_promoted": 0,
            "authority_created": False,
        },
        "laws": [
            "STATE_TRANSITION_REQUIRES_MEASUREMENT",
            "FORCE_OBSERVED_NE_FORCE_CAUSED_RESULT",
            "HTTP_ACCESS_NE_TRUTH",
            "TRANSPORT_DENIAL_NE_FALSE_CLAIM",
            "OFFICIAL_NE_CURRENT_FOREVER",
            "HASH_MATCH_NE_STORY_TRUTH",
            "FAILURE_IS_EVIDENCE"
        ],
        "promotion": False,
        "military_authority": False,
        "institutional_endorsement": False,
        "authority_created": False,
    }

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(receipt, indent=2))
    return 1 if status == "FAIL" else 0


if __name__ == "__main__":
    sys.exit(main())
