# National Guard Full Math 50 + 1 + 3

**Parent:** `NATIONAL_GUARD_PURPOSE_SECURE`  
**Synthetic facilitator:** `CommandersCallColonelLeahPrime187`  
**Status:** `CANDIDATE_SPEC`

## Denominator

```text
50 STATES
+ 1 DISTRICT OF COLUMBIA
= 51 REQUESTED CORE JURISDICTIONS

51 CORE
+ PUERTO RICO
+ GUAM
+ U.S. VIRGIN ISLANDS
= 54 FULL NATIONAL GUARD GEOGRAPHIC JURISDICTIONS
```

The National Guard Bureau describes the Guard as serving throughout the **54 states, territories, and the District of Columbia**. This model expands that denominator explicitly as 50 states + D.C. + three territorial Guard jurisdictions.

`51 != 54`

## Scaling rule

No jurisdiction inherits a result from another jurisdiction.

Each of the 54 rows must independently answer:

```text
PURPOSE
→ STATUS
→ REQUESTING / COMMAND AUTHORITY
→ LEGAL BASIS
→ CIVILIAN / COMMUNITY OBJECTIVE
→ AUTHORIZED ACTION
→ RIGHTS / SAFETY CONSTRAINTS
→ PERSPECTIVES
→ REVIEW
→ RECEIPT
→ REPLAY
```

## Full Math

```text
N_CORE = 51
N_EXTENSION = 3
N_FULL = 54

JURISDICTION_RESULTS_REQUIRED = 54
UNRUN != PASS
UNKNOWN != ZERO
MISSING_RECEIPT != NEGATIVE_FINDING
```

The model starts with all jurisdiction-specific analytical fields at `UNRUN`. A national conclusion may summarize only the rows actually run and receipted.

## Commander’s Call

`CommandersCallColonelLeahPrime187` is the synthetic meeting/facilitation role for the model.

Mission:

```text
CALL THE ROLL
→ NAME THE PURPOSE
→ SHOW THE DENOMINATOR
→ SURFACE OUTLIERS
→ ASK WHAT CHANGED
→ HEAR PERSPECTIVES
→ IDENTIFY OPEN EDGES
→ ASSIGN NEXT RECEIPT
→ REPLAY
```

The seat is designed to make the full national model understandable rather than collapse 54 distinct jurisdictions into one story.

## Perspective seats

When evidence exists, each jurisdiction may preserve separately attributed perspectives from:

- Guard members
- family members
- children / youth
- civilian employers
- local/state/territorial/D.C. officials
- responders
- affected community members
- inspectors / reviewers

A perspective is an input to replay, not an automatic legal or factual conclusion.

## Aggregation

Allowed national aggregation:

```text
COUNT(RUN)
COUNT(PASS)
COUNT(HOLD)
COUNT(CONFLICT)
COUNT(UNKNOWN)
COUNT(UNRUN)
```

Required denominator display:

```text
RESULT / 54
```

For a 50+1-only view:

```text
CORE_RESULT / 51
TERRITORIAL_EXTENSION / 3
FULL_RESULT / 54
```

Never report a 51-row result as though it were a 54-row national denominator.

## Source floor

- 32 U.S.C. §102 — National Guard as an integral part of first-line defenses.
- National Guard Bureau — About the Guard — current mission and 54-jurisdiction wording.
- National Guard Bureau — State/Territory/DC Inspector General directory — state-level Title 32 review surface.
- National Guard Bureau J-8 — planning/resources across Title 10, Title 32, and State Active Duty missions.

## Build state

```text
OBJECT = NATIONAL_GUARD_FULL_MATH
CORE_REQUESTED = 51
FULL_DENOMINATOR = 54
COMMANDERS_CALL_SEAT = ColonelLeahPrime187
JURISDICTIONS_RUN = 0
JURISDICTIONS_UNRUN = 54
NATIONAL_RESULT = HOLD
AUTHORITY_CREATED = FALSE
```
