# ABI Technology Dept — Alabama Source Replay v0.1

```text
ARTIFACT_ID: ABI_TECHNOLOGY_DEPT_REPLAY_V0_1
RESEARCH_MODE: PUBLIC_SOURCE_REPLAY
TURN: TURN_0002
AUTHORITY_CREATED: FALSE
SILENT_INFERENCE: BLOCKED
```

## Question

What does the current public record support when the phrase **“ABI Technology Dept”** is replayed against Alabama's actual present-day structure?

## Finding

The exact phrase **“ABI Technology Dept”** is not established here as a current official Alabama organizational unit.

The public-source replay instead resolves four distinct lanes:

1. **ABI is a legacy agency name.** The Alabama Bureau of Investigation was among the functions consolidated into the Alabama Law Enforcement Agency under Act 2013-67.
2. **Current investigative lane = ALEA State Bureau of Investigation (SBI).** ALEA describes SBI as its investigative, non-uniform arm.
3. **Current ALEA technology-support lane = Administrative Bureau Information & Technology Unit.** ALEA says this unit operates and secures agency networks, applications, systems, devices, and electronic data; performs cybersecurity training/auditing/reporting; and supports modernization and IT services.
4. **Statewide Alabama IT-governance lane = Office of Information Technology (OIT).** OIT was separately created in 2013 by Act 2013-68 / SB117 for statewide IT governance, strategic planning, and resource utilization.

## Interesting bridge

Current Alabama Secretary of Information Technology / State CIO Daniel Urquhart previously served as CIO for ALEA. Alabama's official OIT biography says his ALEA work included helping design, build, and implement a state-of-the-art criminal justice network.

That creates a real historical/organizational bridge:

```text
LEGACY ABI FUNCTIONS
        ↓
ALEA / SBI INVESTIGATIVE LANE
        ↘
         ALEA INFORMATION & TECHNOLOGY UNIT
                  ↓
        FORMER ALEA CIO DANIEL URQUHART
                  ↓
        ALABAMA OIT / STATE CIO
```

This bridge is organizational history, not a claim that OIT, ALEA IT, SBI, and the former ABI are the same entity.

## Technology-adjacent SBI functions

Current SBI public material includes CJIS and the Alabama Fusion Center among its divisions and lists technical surveillance among investigative assistance capabilities. Historical ALEA material also records that after 2015 consolidation, the Internet Crimes Against Children unit moved from the former ABI into ALEA's Fusion Center and used forensic technology examiners.

These facts show technology-intensive investigative work. They do **not** establish a current unit formally named `ABI Technology Dept`.

## Civic Cuff boundary

```text
FORMER_ABI != CURRENT_SBI_NAME
SBI != ALEA_ADMIN_IT
ALEA_ADMIN_IT != STATE_OIT
TECHNICAL_SURVEILLANCE != GENERAL_IT_GOVERNANCE
CRIMINAL_JUSTICE_NETWORK != JURISDICTION_BY_ITSELF
HISTORICAL_ORG_NAME != CURRENT_AUTHORITY
```

## TURN_0002 protocol audit

The canonical game declares `DIE = D6` and six rails only. A 2D6 combined result of 7 therefore cannot silently create a seventh rail.

```text
INPUT_DICE          = [3,4]
COMBINED_VECTOR     = 7
CANONICAL_SELECTOR  = D6 / 1..6
ROLL_VALID_AS_RAIL  = FALSE
REQUESTED_NEW_RAIL  = TOP_BAMA_SECRET_RAIL
RAIL_CREATION       = REJECTED_PROTOCOL_DRIFT
ACTIVE_RAIL         = CIVIC_CUFF
```

The research itself is replayable even though the rail mutation is invalid.

## Source-bound promoted facts

```text
F01 = ACT_2013_67_CONSOLIDATED_ABI_FUNCTIONS_INTO_ALEA
F02 = CURRENT_SBI_IS_ALEA_INVESTIGATIVE_NON_UNIFORM_ARM
F03 = ALEA_INFORMATION_TECHNOLOGY_UNIT_IS_UNDER_ADMINISTRATIVE_BUREAU
F04 = ALABAMA_OIT_IS_SEPARATE_STATEWIDE_IT_GOVERNANCE_LANE
```

No relationship edge among these organizations is inferred beyond the public organizational/history statements above.

## Public sources

- Alabama Law Enforcement Agency — About ALEA
- Alabama Legislature — 2013 General Acts summary, Act 2013-67 and Act 2013-68
- Alabama Law Enforcement Agency — State Bureau of Investigation
- Alabama Law Enforcement Agency — Administrative Bureau / Information & Technology Unit
- Alabama Office of Information Technology — About / Primary Mandates / Daniel Urquhart biography
- Alabama Law Enforcement Agency — 2015 ICAC consolidation history

```text
FACTS_PROMOTED       = 4
EDGES_INFERRED       = 0
EVIDENCE_POINTS      = 4
SILENT_INFERENCE     = BLOCKED
AUTHORITY_CREATED    = FALSE
TURN_VERDICT         = REPLAYABLE_CORRECTION
```

**The funny part is mechanical: the evidence survives; the invented seventh rail does not.**
