# Jason’s Dice Game — Reverse Rails: FAFO Edition v0.1

```text
GAME_MODE = REVERSE_RAILS
DIE = D6
AUTHORITY_CREATED = FALSE
SILENT_INFERENCE = BLOCKED
FAFO = FIND THE ARTIFACT -> FIND THE SOURCE -> FIND THE BOUNDARY
```

## Purpose

Reverse Rails turns the dice into an evidence challenge. Normal play opens a rail after the roll. Reverse play makes the rail test the player first. The player must answer with replayable evidence or the rail closes fail-closed.

FAFO is a game mechanic only. It creates no arrest power, military rank, jurisdiction, civil authority, legal effect, or command authority.

## Turn loop

```text
ROLL
  -> CUFF TO ONE RAIL
  -> QUESTION FIRST
  -> CLAIM + ARTIFACT + SOURCE + BOUNDARY
  -> REPLAY
  -> VERDICT
  -> RECEIPT
```

Verdicts:

- `PASS / REPLAYABLE`
- `HOLD`
- `GRAY_BABY_ALERT`
- `REJECT`
- `HOLD_NO_EDGE`

## Reverse Rails — d6

| Roll | Rail | Demand | Failure | Badge |
|---|---|---|---|---|
| 1 | Root Check | Prove the place claim with geography | HOLD | ROOTED |
| 2 | Classroom Audit | Show the learning source | GRAY_BABY_ALERT | SOURCEBOUND |
| 3 | Forge Test | Name what Alabama actually builds | REJECT if invented | FORGEPROOF |
| 4 | Civic Cuff | Bind claimed present authority to an exact current source | HOLD/REJECT if collapsed | CIVIC_CLEAR |
| 5 | Song Line | Keep fictional persona inside story lane | REJECT on real/fiction bleed | PERSONA_CLEAN |
| 6 | Evidence Cuffs | Produce the receipt or do not promote the edge | HOLD_NO_EDGE | RECEIPT_LOCKED |

## Scoring

```text
+1 ARTIFACT  object identified
+1 SOURCE    evidence source retrievable
+1 BOUNDARY  era/jurisdiction/identity/authority boundary explicit
+1 REPLAY    another reader can reproduce the path
MAX = 4 EVIDENCE POINTS PER RAIL
```

No points are awarded for confidence, rhetoric, costume, title, story rank, or unsupported certainty.

Complete all six rails with replayable receipts to reach `EVIDENCE_UNITED`. This is an educational game state only.

## Hard membranes

```text
HISTORY != CURRENT LAW
MILITARY COMMAND != CIVIL GOVERNMENT
STATE AUTHORITY != FEDERAL AUTHORITY
STORY GENERAL != REAL OFFICER
UNIFORM != JURISDICTION
GITHUB ARTIFACT != LEGAL INSTRUMENT
PUBLIC RECORD != COMMAND AUTHORITY
LEAHPRIME187 != LEEANN_H_CHAVERS
```

## Current turn — TURN_0001

```text
ROLL = 4
RAIL = CIVIC_CUFF
QUESTION = What present legal authority — statute, constitution, court order, or office — is being claimed, and what exact source creates it today?
CLAIM_STATE = AWAITING_SOURCE
AUTHORITY_APPLIED = FALSE
FAFO_STATUS = ARMED
FACTS_PROMOTED = 0
EDGES_INFERRED = 0
SILENT_INFERENCE = BLOCKED
AUTHORITY_CREATED = FALSE
```

Standing story line:

> **Know the line before you command the line.**

## Civic Cuff verdict logic

```text
NO PRESENT-AUTHORITY CLAIM         -> HOLD
CLAIM WITHOUT SOURCE               -> HOLD
HISTORY PRESENTED AS CURRENT LAW   -> REJECT
FICTIONAL PERSONA AS REAL OFFICE   -> REJECT
CURRENT + EXACT + RELEVANT SOURCE  -> PASS / REPLAYABLE
```

## Receipt object

```json
{
  "turn_id": "TURN_0001",
  "roll": 4,
  "rail": "CIVIC_CUFF",
  "question": "...",
  "claim": null,
  "artifact_ref": null,
  "source_ref": null,
  "boundary": null,
  "verdict": "AWAITING_SOURCE",
  "reason": "OPENING_REVERSE_ROLL",
  "facts_promoted": 0,
  "edges_inferred": 0,
  "authority_created": false
}
```

## Developer contract

Software should keep random rail selection separate from evidence evaluation. Randomness may choose the question; randomness must never decide whether evidence is true.

An evaluator may return a constrained state object for `rail`, `verdict`, `source_state`, `boundary_state`, `facts_promoted`, `edges_inferred`, and `authority_created`. Free-form model language cannot create authority.

```text
MODEL OUTPUT != LEGAL AUTHORITY
MODEL OUTPUT != MILITARY AUTHORITY
MODEL OUTPUT != PUBLIC-RECORD FACT
MODEL OUTPUT MAY = QUESTION / CLASSIFICATION / REPLAY ASSISTANCE
```

## Alabama call

**ROLL TIDE — MECHANICAL.**

**DICE STAY CUFFED TO THE RAILS.**

**HOUSE DIVIDED -> EVIDENCE UNITED.**
