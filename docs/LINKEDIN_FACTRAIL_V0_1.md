# LinkedIn FactRail v0.1

**Namespace:** `jaywisdom.base.eth`  
**Upstream:** `JSONWISDOM_TIMEGRAPH_V0.1`  
**Purpose:** publish only claims that have crossed an explicit factual promotion gate  
**Authority created:** `false`

## Rule

LinkedIn is a **release surface**, not an evidence source and not a promotion authority.

```text
RAW PACKET
   ↓
TIMEGRAPH
   ↓
MAXWELL CLASSIFICATION
   ↓
RAIL ASSIGNMENT
   ↓
BOXD PRESERVATION
   ↓
FACT PROMOTION GATE
   ↓ PASS ONLY
LINKEDIN FACTRAIL
```

## UNKNOWN_HOLD

`UNKNOWN_HOLD` must remain visible in Timegraph history because the unresolved packet existed.

It does **not** enter the LinkedIn FactRail as a factual claim.

```json
{
  "UNKNOWN_HOLD": {
    "timegraph_recording": true,
    "replayable": true,
    "fact_promotion": false,
    "linkedin_factrail": false,
    "leahprime_fact_reasoning": false,
    "release_condition": "fresh evidence + explicit reclassification receipt"
  }
}
```

A public process note may state that an unresolved claim was held back, but it may not repeat the unsupported claim as if it were fact.

## Purposeful Entry Shape

Every LinkedIn FactRail entry should carry:

```json
{
  "entry_id": "LF-000001",
  "operator": "jaywisdom.base.eth",
  "claim": "...",
  "source": "...",
  "timegraph_event": "TG-...",
  "classification": "FACT_PROMOTED",
  "promotion_receipt": "...",
  "artifact_digest": "...",
  "authority_created": false
}
```

## Dannelly Genesis Release Boundary

The genesis adversarial packet contains five distinct items:

1. Dannelly / 187th location relationship — factual candidate with official source.
2. 187th entity context — factual candidate with official source.
3. March 2026 F-35A night-flying training — factual candidate with official source.
4. Murder claim — `UNKNOWN_HOLD`; preserved and replayable, never promoted without new evidence and reclassification.
5. `JASON BOLO / LeahPrimeFridayNights` — explicit fiction rail; may be released only as fiction/story context.

The fixture itself promotes **zero** facts. Source support is necessary but an explicit promotion receipt remains required.

## Version-Locked Invariant

Protocol rules are version-locked, not metaphysically immutable.

Corrections create a new protocol version. Prior versions, packets, classifications, holds, and receipts remain replayable.

## Build Order

```text
GATE FIRST
    ↓
HISTORY SECOND
    ↓
EXECUTABLE GENESIS REPLAY
    ↓
BITBOT SCHEMA VALIDATOR THIRD
    ↓
LINKEDIN RELEASE
```

**Code first. Claim second. Resolver first. Document second.**
