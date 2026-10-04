# NationalGuardPurposeSecure v0.1

**Lane:** `leahprime/BRAIN/NATIONAL_GUARD_PURPOSE_SECURE/`  
**Mode:** defensive purpose / authority-typing / civic replay model  
**Status:** `CANDIDATE_SPEC`  
**Operational planning:** `NONE`  
**Authority created:** `false`

## Why this exists

The model secures **purpose before power**.

The National Guard is a useful civic teaching object because its public mission spans more than one role: reserve defense, homeland defense, and support to communities and civil authorities. Those roles are not interchangeable, and the legal/status basis for a Guard action matters.

The purpose-security question is therefore:

> What is the mission, what status is being used, who supplied lawful authority, who is being protected, what action is actually authorized, and what receipt allows later review?

## Current source floor

1. **32 U.S.C. § 102 — General policy**  
   Congress states that the Army and Air National Guard are an integral part of the first-line defenses of the United States.  
   Source: https://uscode.house.gov/view.xhtml?edition=prelim&num=0&req=granuleid%3AUSC-prelim-title32-chapter1

2. **National Guard Bureau — About the Guard**  
   The Guard describes itself as the primary combat reserve of the Army and Air Force, with missions to fight and win the nation's wars, defend the homeland, and assist communities during natural or human-caused disasters.  
   Source: https://www.nationalguard.mil/About-the-Guard/Active-Duty/

3. **National Guard Bureau — Civil Support**  
   Domestic civil-support functions include planning, coordinating, information sharing, and integrating Guard support to civil authorities.  
   Source: https://www.nationalguard.mil/Leadership/Joint-Staff/J-3/Civil-Support/

## Purpose-secure loop

```text
PURPOSE
→ STATUS
→ REQUESTING / COMMAND AUTHORITY
→ LEGAL BASIS
→ CIVILIAN / COMMUNITY OBJECTIVE
→ AUTHORIZED ACTION
→ RIGHTS / SAFETY CONSTRAINTS
→ REVIEW
→ RECEIPT
→ REPLAY
```

## Positive defense logic

### 1. Purpose is named before capability

A capability does not select its own mission.

### 2. Status is explicit

State Active Duty, Title 32, Title 10, or another lawful status must be identified from receipts rather than inferred from uniforms, equipment, location, or rhetoric.

### 3. Authority is typed

The model records who requested, ordered, approved, funded, or reviewed an action instead of collapsing those roles into one generic authority field.

### 4. Protection is an objective

Life, property, community safety, critical infrastructure, disaster response, homeland defense, and other lawful objectives are recorded as mission objects that can later be compared against actual conduct.

### 5. Civil support means support

Where the Guard is supporting civil authorities, the supporting role and the supported civil authority remain separately visible.

### 6. Rights remain part of the replay

A security objective does not erase the need to identify applicable constitutional, statutory, policy, due-process, safety, and use-of-authority constraints.

### 7. Civilian impact is evidence

The experiences of workers, parents, children, bystanders, local officials, responders, and Guard members can be recorded as separately attributed perspectives. Perspective is not automatically diagnosis or legal finding.

### 8. Defense includes correction

A purpose-secure institution can investigate misuse, correct procedures, preserve dissent, and improve controls without treating correction as disloyalty.

### 9. Power must remain reviewable

Orders, requests, status transitions, actions, complaints, investigations, and corrective measures should produce enough receipt structure for later replay.

### 10. Community trust is an operational asset

Legibility, proportionality, lawful process, clear communication, and correction improve the institution's ability to serve communities.

## KidsPerspective bridge

Children do not become command authorities or investigators.

Their perspective can still reveal whether an adult system created:

```text
CONFUSION
FEAR
TRUST
DISTRUST
SAFETY
UNSAFETY
UNDERSTANDING
EXIT
```

The child's report is preserved as a report.

`CHILD_REPORT != CHILD_DIAGNOSIS`

The next step is adult investigation of the system, not punishment of the child for friction.

## FamilyModelUnits bridge

The same purpose-security grammar can be taught at family scale:

```text
ROLE
→ PURPOSE
→ ACTUAL AUTHORITY
→ ACTION
→ IMPACT
→ OTHER PERSPECTIVES
→ REVIEW
→ CORRECTION
→ REPLAY
```

This does **not** make a family into a military chain of command. It is a teaching analogy for keeping power explainable and reviewable.

## Security definition

`SECURE = PURPOSE_BOUND + AUTHORITY_TYPED + RIGHTS_AWARE + REVIEWABLE + RECEIPTED`

Security is not defined as maximum coercive power.

## Build state

```text
OBJECT = NATIONAL_GUARD_PURPOSE_SECURE
STATUS = CANDIDATE_SPEC
SOURCE_FLOOR = 3
OPERATIONAL_PLANNING = NONE
AUTHORITY_CREATED = FALSE
HISTORY_REWRITE = FALSE
```
