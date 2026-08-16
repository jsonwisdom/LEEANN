#!/usr/bin/env python3
"""Alabama Colonel Test — LeeAnn byte-by-byte USAF Knowledge Management.

Public educational test only. Uses public U.S. Air Force web surfaces.
No classified, controlled, operational, or private data is requested or processed.

The test proves mechanics, not truth:
- fetch public source bytes
- hash exact bytes
- re-fetch and compare byte-for-byte
- preserve volatility as HOLD instead of smoothing it away
- mutate exactly one byte and prove the digest changes
- preserve temporal/source classes
- emit a replay receipt
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_MANIFEST = ROOT / "fixtures/leeann/ALABAMA_COLONEL_KM_PUBLIC_SOURCE_MANIFEST_V0_1.json"
DEFAULT_RECEIPT = ROOT / "build/receipts/ALABAMA_COLONEL_KM_TEST_V0_1.json"
USER_AGENT = "jsonwisdom-leeann-public-km-test/0.1 (+https://github.com/jsonwisdom/LEEANN)"


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def fetch_bytes(url: str, timeout: int = 30) -> tuple[int, bytes, str]:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "text/html,*/*;q=0.8"})
    with urllib.request.urlopen(req, timeout=timeout) as response:
        status = int(getattr(response, "status", response.getcode()))
        body = response.read()
        final_url = response.geturl()
        return status, body, final_url


def marker_check(body: bytes, markers: list[str]) -> dict[str, bool]:
    text = body.decode("utf-8", errors="replace")
    return {marker: marker.lower() in text.lower() for marker in markers}


def one_byte_mutation(data: bytes) -> tuple[bytes, int]:
    if not data:
        raise ValueError("cannot mutate empty source bytes")
    index = len(data) // 2
    mutated = bytearray(data)
    mutated[index] ^= 0x01
    return bytes(mutated), index


def count_byte_differences(a: bytes, b: bytes) -> int:
    overlap = min(len(a), len(b))
    differences = sum(1 for i in range(overlap) if a[i] != b[i])
    return differences + abs(len(a) - len(b))


def validate_invariants(manifest: dict[str, Any]) -> list[dict[str, Any]]:
    inv = manifest["invariants"]
    expected = {
        "http_200_equals_truth": False,
        "official_domain_equals_current_forever": False,
        "historical_article_equals_current_policy": False,
        "hash_match_equals_story_truth": False,
        "byte_change_must_be_detectable": True,
        "unknown_or_volatile_state_must_be_preserved": True,
        "authority_created": False,
    }
    checks = []
    for key, value in expected.items():
        actual = inv.get(key)
        checks.append({"check": key, "expected": value, "actual": actual, "pass": actual == value})
    return checks


def run_source(source: dict[str, Any], pause_seconds: float) -> dict[str, Any]:
    result: dict[str, Any] = {
        "id": source["id"],
        "url": source["url"],
        "source_class": source["source_class"],
        "temporal_class": source["temporal_class"],
        "authority_created": False,
    }

    try:
        status1, body1, final1 = fetch_bytes(source["url"])
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, OSError) as exc:
        result.update({
            "fetch_1": "FAIL",
            "error": f"{type(exc).__name__}: {exc}",
            "state": "FAIL_FETCH",
        })
        return result

    result.update({
        "fetch_1": "PASS" if status1 == 200 else "FAIL",
        "http_status_1": status1,
        "final_url_1": final1,
        "bytes_1": len(body1),
        "sha256_1": sha256(body1),
        "markers": marker_check(body1, source.get("required_markers", [])),
    })

    mutated, mutation_index = one_byte_mutation(body1)
    result["girl_physics_edge"] = {
        "S0_bytes": len(body1),
        "S0_sha256": sha256(body1),
        "interaction": "CONTROLLED_ONE_BYTE_XOR_0x01",
        "mutation_index": mutation_index,
        "S1_bytes": len(mutated),
        "S1_sha256": sha256(mutated),
        "measured_byte_differences": count_byte_differences(body1, mutated),
        "digest_changed": sha256(body1) != sha256(mutated),
        "causal_edge_supported": True,
        "reason": "The transformation is declared, controlled, and replayable.",
    }

    time.sleep(max(0.0, pause_seconds))

    try:
        status2, body2, final2 = fetch_bytes(source["url"])
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, OSError) as exc:
        result.update({
            "fetch_2": "FAIL",
            "fetch_2_error": f"{type(exc).__name__}: {exc}",
            "byte_stability": "HOLD_SECOND_FETCH_FAILED",
            "state": "PASS_WITH_HOLD",
        })
        return result

    same_bytes = body1 == body2
    result.update({
        "fetch_2": "PASS" if status2 == 200 else "FAIL",
        "http_status_2": status2,
        "final_url_2": final2,
        "bytes_2": len(body2),
        "sha256_2": sha256(body2),
        "byte_stability": "PASS" if same_bytes else "VOLATILE_SOURCE_HOLD",
        "same_endpoint": final1 == final2,
        "same_history": same_bytes,
        "live_byte_differences": count_byte_differences(body1, body2),
    })

    markers_pass = all(result["markers"].values())
    mutation_pass = (
        result["girl_physics_edge"]["measured_byte_differences"] == 1
        and result["girl_physics_edge"]["digest_changed"] is True
    )
    http_pass = status1 == 200 and status2 == 200

    if not http_pass or not markers_pass or not mutation_pass:
        result["state"] = "FAIL"
    elif same_bytes:
        result["state"] = "PASS"
    else:
        result["state"] = "PASS_WITH_HOLD"

    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", default=str(DEFAULT_MANIFEST))
    parser.add_argument("--out", default=str(DEFAULT_RECEIPT))
    parser.add_argument("--pause-seconds", type=float, default=1.0)
    args = parser.parse_args()

    manifest_path = Path(args.manifest)
    out_path = Path(args.out)
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

    invariant_checks = validate_invariants(manifest)
    invariant_pass = all(item["pass"] for item in invariant_checks)

    source_results = [run_source(source, args.pause_seconds) for source in manifest["sources"]]
    hard_fail = any(item.get("state") in {"FAIL", "FAIL_FETCH"} for item in source_results)
    any_hold = any("HOLD" in item.get("state", "") or "HOLD" in item.get("byte_stability", "") for item in source_results)

    if hard_fail or not invariant_pass:
        status = "FAIL"
    elif any_hold:
        status = "PASS_WITH_HOLDS"
    else:
        status = "PASS"

    receipt = {
        "receipt_type": "ALABAMA_COLONEL_KM_TEST_RECEIPT",
        "version": "0.1.0",
        "test_name": "The Alabama Colonel Test of Byte-by-Byte USAF Knowledge Management",
        "classification": "PUBLIC_EDUCATIONAL_TEST",
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "repository": os.environ.get("GITHUB_REPOSITORY", "jsonwisdom/LEEANN"),
        "commit_sha": os.environ.get("GITHUB_SHA", "LOCAL_OR_UNKNOWN"),
        "status": status,
        "girl_physics_law": "FORCE_OBSERVED_NE_FORCE_CAUSED_RESULT",
        "core_question": "What state existed, what interaction occurred, what changed, and what measurement proves the transition?",
        "invariant_checks": invariant_checks,
        "sources": source_results,
        "summary": {
            "source_count": len(source_results),
            "pass": sum(1 for item in source_results if item.get("state") == "PASS"),
            "pass_with_hold": sum(1 for item in source_results if item.get("state") == "PASS_WITH_HOLD"),
            "fail": sum(1 for item in source_results if item.get("state") in {"FAIL", "FAIL_FETCH"}),
            "facts_promoted": 0,
            "authority_created": False,
        },
        "semantic_boundaries": {
            "http_200_implies_truth": False,
            "official_source_implies_current_forever": False,
            "historical_context_implies_current_policy": False,
            "same_endpoint_implies_same_history": False,
            "hash_match_implies_story_truth": False,
            "one_byte_controlled_mutation_supports_causal_edge": True,
            "unknown_hold_is_valid_state": True,
        },
        "promotion": False,
        "military_authority": False,
        "institutional_endorsement": False,
        "authority_created": False,
    }

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(receipt, indent=2))
    return 1 if status == "FAIL" else 0


if __name__ == "__main__":
    sys.exit(main())
