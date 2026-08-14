# Aunt Rann — Real Person / Synthetic Role Boundary v0.1

**Repository:** `jsonwisdom/LEEANN`  
**Classification:** `PUBLIC_EDUCATIONAL_SIMULATION`  
**Authority created:** `false`

## Purpose

Keep the real-world public record for Lt Col Leeann Chavers separate from the JSONWisdom `Aunt Rann` / `LeeAnnPrime` simulation roles.

This file is a boundary receipt. It does not create identity, military authority, endorsement, affiliation, or operational command.

## Panel A — Real Person Reference

```text
NAME: Lt Col Leeann Chavers
PUBLIC ROLE REFERENCE: Commander, Force Support Squadron
UNIT REFERENCE: 187th Fighter Wing, Alabama Air National Guard
LOCATION REFERENCE: Montgomery, Alabama
SOURCE CLASS: OFFICIAL_187FW_PUBLIC_ROLE_TEXT
SOURCE: https://www.187fw.ang.af.mil/Units/Mission-Support-Group/
OBSERVED: 2026-08-14
```

### Real-person boundary

```text
REAL_RANK = Lieutenant Colonel
REAL_ROLE = Commander, Force Support Squadron
REAL_UNIT_REFERENCE = 187th Fighter Wing

REAL_RANK ≠ AUNT_RANN_SIMULATION_RANK
REAL_ROLE ≠ LEEANN_GENERAL_WAR_CIVIL_ROLE
REAL_UNIT ≠ JSONWISDOM_SYSTEM_AUTHORITY
```

The current public-role reference may be updated only from a fresh official source receipt.

### Contact and portrait status

```text
OFFICIAL_PORTRAIT = HOLD / OFFICIAL_SOURCE_REQUIRED
CONTACT_DETAILS = HOLD_UNLESS_INDEPENDENTLY_VERIFIED_FROM_CURRENT_OFFICIAL_SOURCE
```

No synthetic image may be presented as an official portrait. The intentional blank real-photo panel remains valid until an official public-use image is sourced and receipted.

## Panel B — Aunt Rann / LeeAnnPrime

```text
DISPLAY_ALIAS: Aunt Rann
LANE_ID: LEEANN
ROLE: SISTER_SYNTAX_CREATIVE_COMMANDER
CREATIVE_FUNCTION: DIRECT_THE_THREE_PROPOSALS_AND_EXPLAIN_EACH_EDIT_CHOICE
FINAL_RELEASE_AUTHORITY: false
MAY_REQUEST_MOM_REVIEW: true
MAY_OVERRIDE_MOM: false
```

Existing source: `FAMILY_MOVIE_CREATOR_V0_2.json`.

### Strategic replay extension

The wider JSONWisdom Art of War RePlay may use the separate fictional role:

```text
SIMULATION_ROLE: LEEANN_GENERAL_WAR_CIVIL
DISPLAY_FUNCTION: STRATEGIC_REPLAY_CALLER
REAL_MILITARY_RANK_CLAIMED: false
REAL_WORLD_COMMAND: false
AUTHORITY_CREATED: false
```

This is a systems-education character role only. It must not be represented as Lt Col Chavers's actual military assignment, authority, endorsement, or conduct.

## CrissCross Rule

```text
REAL_PERSON
    ║
    ║ CRISSCROSS — DO NOT COLLAPSE
    ║
SYNTHETIC_ROLE
```

Allowed:
- cite verified public facts about the real person with provenance
- use Aunt Rann / LeeAnnPrime as clearly labeled synthetic educational characters
- compare system roles only when the boundary is visible
- preserve gaps as HOLD

Forbidden:
- synthetic portrait presented as official portrait
- simulation rank presented as real rank
- fictional events presented as real conduct
- JSONWisdom role presented as USAF/ANG endorsement
- real military rank used to create JSONWisdom authority

## Canonical Separation

```text
LT_COL_LEEANN_CHAVERS = REAL_PERSON_REFERENCE
AUNT_RANN = SYNTHETIC_FAMILY_CREATIVE_ROLE
LEEANNPRIME = SYNTHETIC_REPLAY_CHARACTER
LEEANN_GENERAL_WAR_CIVIL = SYNTHETIC_STRATEGIC_REPLAY_ROLE

REAL_RANK ≠ SIMULATION_ROLE
PUBLIC_FACT ≠ FAMILY_STORY
PORTRAIT_GAP ≠ PERMISSION_TO_INVENT
RECEIPT ≠ AUTHORITY
```

## Status Receipt

```json
{
  "artifact": "AUNT_RANN_REAL_SYNTHETIC_BOUNDARY",
  "version": "0.1.0",
  "repository": "jsonwisdom/LEEANN",
  "real_person_reference": {
    "name": "Lt Col Leeann Chavers",
    "rank": "Lieutenant Colonel",
    "public_role": "Commander, Force Support Squadron",
    "unit_reference": "187th Fighter Wing",
    "location_reference": "Montgomery, Alabama",
    "source_class": "OFFICIAL_187FW_PUBLIC_ROLE_TEXT",
    "observed": "2026-08-14"
  },
  "synthetic_roles": {
    "aunt_rann": "SISTER_SYNTAX_CREATIVE_COMMANDER",
    "leeannprime": "SYNTHETIC_REPLAY_CHARACTER",
    "leeann_general_war_civil": "STRATEGIC_REPLAY_CALLER"
  },
  "official_portrait": "HOLD_OFFICIAL_SOURCE_REQUIRED",
  "contact_details": "HOLD_UNLESS_CURRENT_OFFICIAL_SOURCE_VERIFIED",
  "real_military_authority_transferred": false,
  "government_endorsement_claimed": false,
  "authority_created": false,
  "status": "BOUNDARY_RECORDED"
}
```

## Final Rule

> **Honor the real record. Label the synthetic role. Never use one to manufacture authority for the other.**
