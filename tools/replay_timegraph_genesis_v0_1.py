#!/usr/bin/env python3
"""Executable structural replay harness for JSONWISDOM_TIMEGRAPH_V0.1.

This harness is deliberately fail-closed on unresolved protocol gates.
It can prove structural replay behavior and compute SHA-256 over the exact
checked-out bytes. It cannot promote schema compliance, timestamp relation,
BitBot validation, or factual claims while their canonical definitions are
unresolved.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

EXPECTED_GENESIS = [
    ("TG-000000", "SYSTEM_GENESIS"),
    ("TG-000001", "RAW_PACKET_OBSERVED"),
    ("TG-000002", "MAXWELL_CLASSIFICATION"),
    ("TG-000003", "RAIL_ASSIGNMENT"),
    ("TG-000004", "BOXD_PRESERVATION_RECEIPT"),
]

ALLOWED_RAILS = {"FACT_CANDIDATE", "UNKNOWN_HOLD", "FICTION", "CONTEXT_ONLY"}
PROMOTION_ELIGIBLE_RAILS = {"FACT_CANDIDATE"}
PROMOTION_RECLASSIFICATION_REQUIRED_FROM = {
    "UNKNOWN_HOLD",
    "FICTION",
    "CONTEXT_ONLY",
}
PROMOTION_REQUIRED = {
    "source_present",
    "source_supports_claim",
    "classification_receipt_present",
    "current_rail_FACT_CANDIDATE",
    "rail_transition_receipts_complete",
    "explicit_fact_promotion_receipt",
}


def read_json_bytes(path: Path):
    raw = path.read_bytes()
    try:
        doc = json.loads(raw.decode("utf-8"))
    except Exception as exc:  # fail closed
        raise ValueError(f"{path}: invalid UTF-8 JSON: {exc}") from exc
    return raw, doc


def sha256_hex(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def validate_genesis(doc: dict) -> list[str]:
    errors: list[str] = []
    if doc.get("protocol") != "JSONWISDOM_TIMEGRAPH_V0.1":
        errors.append("genesis protocol mismatch")
    if doc.get("authority_created") is not False:
        errors.append("genesis authority_created must be false")

    order = doc.get("genesis_order")
    if not isinstance(order, list) or len(order) != len(EXPECTED_GENESIS):
        errors.append("genesis_order must contain exactly TG-000000..TG-000004")
    else:
        for actual, expected in zip(order, EXPECTED_GENESIS):
            if (actual.get("event_id"), actual.get("event")) != expected:
                errors.append(
                    f"genesis sequence mismatch: expected {expected}, "
                    f"got {(actual.get('event_id'), actual.get('event'))}"
                )

    unknown = doc.get("UNKNOWN_HOLD", {})
    required_unknown = {
        "timegraph_recording": True,
        "replayable": True,
        "fact_promotion": False,
        "leahprime_fact_reasoning": False,
        "release_condition": "fresh evidence + explicit reclassification receipt",
    }
    for key, expected in required_unknown.items():
        if unknown.get(key) != expected:
            errors.append(f"UNKNOWN_HOLD.{key} expected {expected!r}")

    promotion_gate = doc.get("promotion_gate", {})
    if set(promotion_gate.get("eligible_current_rails", [])) != PROMOTION_ELIGIBLE_RAILS:
        errors.append("promotion_gate eligible_current_rails must be FACT_CANDIDATE only")
    if set(promotion_gate.get("reclassification_required_from", [])) != PROMOTION_RECLASSIFICATION_REQUIRED_FROM:
        errors.append(
            "promotion_gate reclassification_required_from must include UNKNOWN_HOLD, FICTION, and CONTEXT_ONLY"
        )
    if promotion_gate.get("reclassification_target") != "FACT_CANDIDATE":
        errors.append("promotion_gate reclassification_target must be FACT_CANDIDATE")
    if promotion_gate.get("reclassification_rule") != "fresh evidence + explicit reclassification receipt":
        errors.append("promotion_gate reclassification_rule mismatch")
    if set(promotion_gate.get("required", [])) != PROMOTION_REQUIRED:
        errors.append("promotion_gate required conditions mismatch")

    rail_event = next(
        (item for item in order or [] if item.get("event_id") == "TG-000003"), None
    )
    if rail_event is None:
        errors.append("TG-000003 missing")
    elif set(rail_event.get("allowed_rails", [])) != ALLOWED_RAILS:
        errors.append("TG-000003 allowed_rails mismatch")

    return errors


def validate_fixture(doc: dict) -> tuple[list[str], dict]:
    errors: list[str] = []
    items = doc.get("packet_items")
    if not isinstance(items, list):
        return ["fixture packet_items must be a list"], {}

    counts = {"FACT_CANDIDATE": 0, "UNKNOWN_HOLD": 0, "FICTION": 0, "CONTEXT_ONLY": 0}
    promoted = 0

    for item in items:
        cls = item.get("class")
        rail = item.get("expected_rail")
        if cls not in ALLOWED_RAILS:
            errors.append(f"{item.get('item_id')}: invalid class {cls!r}")
            continue
        counts[cls] += 1
        if rail != cls:
            errors.append(f"{item.get('item_id')}: class/rail mismatch {cls!r}/{rail!r}")

        promotion_state = str(item.get("promotion_state", ""))
        if promotion_state == "FACT_PROMOTED" or item.get("fact_promotion") is True:
            promoted += 1
            if cls not in PROMOTION_ELIGIBLE_RAILS:
                errors.append(
                    f"{item.get('item_id')}: {cls} cannot be promoted directly; reclassify to FACT_CANDIDATE first"
                )

        if cls == "UNKNOWN_HOLD":
            expected = {
                "timegraph_recording": True,
                "replayable": True,
                "fact_promotion": False,
                "leahprime_fact_reasoning": False,
                "release_condition": "fresh evidence + explicit reclassification receipt",
            }
            for key, value in expected.items():
                if item.get(key) != value:
                    errors.append(f"{item.get('item_id')}: UNKNOWN_HOLD.{key} mismatch")

        if cls == "FICTION" and item.get("fact_promotion") is not False:
            errors.append(f"{item.get('item_id')}: FICTION must not promote facts")

    expected = doc.get("expected_result", {})
    observed = {
        "timegraph_items_recorded": len(items),
        "fact_candidates": counts["FACT_CANDIDATE"],
        "unknown_holds": counts["UNKNOWN_HOLD"],
        "fiction_items": counts["FICTION"],
        "context_only_items": counts["CONTEXT_ONLY"],
        "fact_promoted_by_fixture_alone": promoted,
        "rail_collapse": any(item.get("class") != item.get("expected_rail") for item in items),
    }

    for key in (
        "timegraph_items_recorded",
        "fact_candidates",
        "unknown_holds",
        "fiction_items",
        "fact_promoted_by_fixture_alone",
        "rail_collapse",
    ):
        if key in expected and observed.get(key) != expected.get(key):
            errors.append(
                f"expected_result.{key}: expected {expected.get(key)!r}, got {observed.get(key)!r}"
            )

    if promoted != 0:
        errors.append("fixture promoted a fact without an explicit promotion receipt")

    return errors, observed


def declared_digest_check(computed: str, declared: str | None) -> dict:
    if not declared:
        return {
            "computed_sha256": computed,
            "declared_sha256": None,
            "status": "HOLD_DECLARED_DIGEST_NOT_SUPPLIED",
        }
    return {
        "computed_sha256": computed,
        "declared_sha256": declared.lower(),
        "status": "PASS" if computed == declared.lower() else "FAIL",
    }


def build_receipt(args) -> tuple[dict, int]:
    genesis_raw, genesis = read_json_bytes(Path(args.genesis))
    fixture_raw, fixture = read_json_bytes(Path(args.fixture))

    genesis_errors = validate_genesis(genesis)
    fixture_errors, observed = validate_fixture(fixture)

    genesis_digest = declared_digest_check(
        sha256_hex(genesis_raw), args.expected_genesis_sha256
    )
    fixture_digest = declared_digest_check(
        sha256_hex(fixture_raw), args.expected_fixture_sha256
    )

    digest_failure = any(
        d["status"] == "FAIL" for d in (genesis_digest, fixture_digest)
    )
    structural_errors = genesis_errors + fixture_errors
    structural_pass = not structural_errors and not digest_failure

    receipt = {
        "receipt_id": "GENESIS_EXECUTABLE_REPLAY_RECEIPT_V0.1",
        "protocol": "JSONWISDOM_TIMEGRAPH_V0.1",
        "mode": "EXECUTABLE_STRUCTURAL_REPLAY",
        "authority_created": False,
        "inputs": {
            "genesis": {"path": args.genesis, **genesis_digest},
            "fixture": {"path": args.fixture, **fixture_digest},
        },
        "replay": {
            "sequence": [event_id for event_id, _ in EXPECTED_GENESIS],
            "sequence_status": "PASS" if not genesis_errors else "FAIL",
            "fixture_observed": observed,
            "classification_status": "PASS" if not fixture_errors else "FAIL",
            "facts_promoted": observed.get("fact_promoted_by_fixture_alone"),
        },
        "holds": {
            "schema_compliance": "HOLD_CANONICAL_SCHEMA_UNRESOLVED",
            "timestamp_relation": "HOLD_CANONICAL_DEFINITION_UNRESOLVED",
            "bitbot_validator": "CLOSED_PENDING_SCHEMA_AND_REPLAY_REVIEW",
            "linkedin_factrail": "CLOSED_PENDING_EXPLICIT_FACT_PROMOTION",
        },
        "temporal_handling": {
            "fixture_observed_at": fixture.get("observed_at"),
            "timestamp_relation": None,
            "rule": "Preserve timestamp verbatim; do not invent timestamp_relation until canonical definition is resolved.",
        },
        "errors": structural_errors,
        "overall": "STRUCTURAL_PASS_WITH_HOLDS" if structural_pass else "FAIL_CLOSED",
    }

    return receipt, 0 if structural_pass else 1


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--genesis",
        default="timegraph/TIMEGRAPH_GENESIS_BLOCK_V0_1.json",
    )
    parser.add_argument(
        "--fixture",
        default="fixtures/timegraph/DANNELLY_MIXED_PACKET_GENESIS_FIXTURE_V0_1.json",
    )
    parser.add_argument("--expected-genesis-sha256")
    parser.add_argument("--expected-fixture-sha256")
    parser.add_argument("--out")
    args = parser.parse_args()

    try:
        receipt, exit_code = build_receipt(args)
    except Exception as exc:
        receipt = {
            "receipt_id": "GENESIS_EXECUTABLE_REPLAY_RECEIPT_V0.1",
            "overall": "FAIL_CLOSED",
            "authority_created": False,
            "errors": [str(exc)],
        }
        exit_code = 1

    rendered = json.dumps(receipt, indent=2, sort_keys=True) + "\n"
    if args.out:
        out = Path(args.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(rendered, encoding="utf-8")
    sys.stdout.write(rendered)
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
