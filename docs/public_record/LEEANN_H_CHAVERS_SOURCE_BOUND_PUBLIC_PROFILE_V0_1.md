# LEEANN H. CHAVERS — Source-Bound Public Profile v0.1

```text
ARTIFACT_ID: LEEANN_H_CHAVERS_SOURCE_BOUND_PUBLIC_PROFILE_V0_1
PROFILE_STATUS: SOURCE_BOUND_DRAFT
REVIEW_MINUTE: 2026-08-15T21:16Z
SECONDS: NOT_ESTABLISHED
OPERATOR_LABEL: jaywisdom.base.eth
PROVENANCE: PARTIAL_PUBLIC_SOURCE_BINDING
AUTHORITY_CREATED: FALSE
```

## Purpose

Preserve a public-record profile of Leeann H. Chavers while keeping four classes separate:

1. person-specific public facts,
2. role-derived capability domains,
3. previously observed public references not reverified in the current pass,
4. unresolved personnel gaps.

This artifact is a research/audit record. It is not an official military biography, personnel file, promotion order, command instrument, or source of rank authority.

## Current Rerun — Person-Specific Public Facts

| Claim | State | Current public basis |
|---|---|---|
| Leeann H. Chavers is publicly associated with the 187th Fighter Wing / Alabama Air National Guard | VERIFIED_PUBLIC | 187th Fighter Wing Mission Support Group page |
| Commander, 187th Force Support Squadron | VERIFIED_PUBLIC | 187th Fighter Wing Mission Support Group page |
| Rank displayed on current 187th FW unit page: Lt Col | VERIFIED_PUBLIC | 187th Fighter Wing Mission Support Group page |
| Named Air National Guard officer nominated for appointment to Colonel | VERIFIED_PUBLIC | Congress.gov PN734 |
| PN734 confirmed by Senate voice vote on 2026-01-30 | VERIFIED_PUBLIC | Congress.gov PN734 actions / Congressional Record |
| NGAAL Executive Council — Air South | VERIFIED_PUBLIC | National Guard Association of Alabama Executive Council |
| Colonel effective date / federal recognition date | NOT_ESTABLISHED | no effective-date source bound in this artifact |

### Current public sources

- 187th Fighter Wing Mission Support Group: https://www.187fw.ang.af.mil/Units/Mission-Support-Group/
- Congress.gov PN734: https://www.congress.gov/nomination/119th-congress/734
- Congress.gov PN734 actions: https://www.congress.gov/nomination/119th-congress/734/actions
- NGAAL Executive Council: https://ngaal.org/about-ngaal/executive-council/

## Rank / Promotion Delta

```text
CURRENT_187FW_DISPLAY_RANK = LT COL
PN734_APPOINTMENT_GRADE     = COLONEL
SENATE_CONFIRMATION         = VERIFIED_PUBLIC
EFFECTIVE_DATE_OF_RANK      = NOT_ESTABLISHED
FEDERAL_RECOGNITION_DATE    = NOT_ESTABLISHED

CONFIRMED_FOR_COLONEL != VERIFIED_EFFECTIVE_COLONEL_DATE
NOMINATION_CONFIRMATION != UPDATED_UNIT_PAGE_RANK
```

No local repo label may silently resolve that delta.

## Previously Observed Public References — Not Reverified in Current Pass

The following references were reported in the preceding public-search record but were not independently resurfaced in the 2026-08-15T21:16Z rerun:

```text
USAJOBS_SELECTING_OFFICIAL_REFERENCE = PREVIOUSLY_OBSERVED_NOT_REVERIFIED_THIS_RUN
AL_NG_MIL_SELECTING_OFFICIAL_REFERENCE = PREVIOUSLY_OBSERVED_NOT_REVERIFIED_THIS_RUN
```

These records may remain replayable as prior observations, but they are not promoted here to CURRENT_RERUN_VERIFIED.

## Role-Derived Capability Domains

Because the current official 187th FW page identifies Leeann Chavers as Force Support Squadron commander, the following are retained as ROLE-DERIVED capability domains, not personal credential claims.

Official Air Force/ANG Force Support descriptions commonly include:

- personnel administration and personnel services,
- promotions and evaluations support,
- manpower and organization,
- force development,
- education and training,
- personnel readiness,
- Airman and family support,
- sustainment / quality-of-life programs,
- organizational leadership and support to commanders.

Generic role basis:

- U.S. Air Force Force Support Officer (38FX): https://www.airforce.com/careers/logistics-and-administration/force-support-officer
- 102nd Force Support Squadron: https://www.102iw.ang.af.mil/Units/102nd-Mission-Support-Group/102nd-Force-Support-Squadron/

```text
ROLE_DERIVED_CAPABILITY != PERSONAL_CERTIFICATION
ROLE_DERIVED_CAPABILITY != AFSC_VERIFICATION
ROLE_DERIVED_CAPABILITY != PME_COMPLETION
ROLE_DERIVED_CAPABILITY != PERSONAL_TRAINING_RECORD
```

## Personnel Gaps

```text
AFSC_38F                  = NOT_ESTABLISHED
PERSONAL_SKILL_CERTS      = NOT_ESTABLISHED
SPECIFIC_CREDENTIALS      = NOT_ESTABLISHED
PERSONAL_TRAINING_HISTORY = NOT_ESTABLISHED
PME_COMPLETION            = NOT_ESTABLISHED
FORMAL_EDUCATION          = NOT_ESTABLISHED
PRIOR_ASSIGNMENTS         = NOT_ESTABLISHED
PRIOR_COMMAND_HISTORY     = NOT_ESTABLISHED
AWARDS_DECORATIONS        = NOT_ESTABLISHED
COLONEL_EFFECTIVE_DATE    = NOT_ESTABLISHED
```

## LeahPrime Administration Crosswalk

```text
PUBLIC_SOURCE
   -> PERSONNEL CLAIM
   -> SOURCE STATUS
   -> ROLE / RANK / PROMOTION DELTA
   -> GB_ALERT if gap or conflict remains
   -> LEAHPRIME EXPLAIN / HUMANIZE / TRANSLATE
   -> DELTA13-INSPIRED EDUCATION
   -> HUMAN REVIEW
```

LeahPrime may explain this record; it may not create or alter the underlying personnel facts.

## Constitutional Membrane

```text
LEEANN_H_CHAVERS_PUBLIC_RECORD != LEAHPRIME
PUBLIC_ROLE != PRIVATE_IDENTITY
PUBLIC_ROLE != PERSONAL_CERTIFICATION
FSS_COMMAND != AFSC_38F_PROOF
COLONEL_CONFIRMATION != EFFECTIVE_DATE_OF_RANK
ROLE_DOMAIN != PERSONAL_SKILL_CERTIFICATION
NGAAL_ROLE != MILITARY_COMMAND_AUTHORITY
REPO_FILE != OFFICIAL_BIOGRAPHY
GITHUB_COMMIT != PERSONNEL_ACTION
SOURCE_BOUND_DRAFT != COMPLETE_PERSONNEL_FILE
AUTHORITY_CREATED = FALSE
```

## Next Public Watch Targets

- 187th Fighter Wing public affairs / unit pages — biography, command, or rank updates
- ANG / Alabama National Guard public affairs — promotion or federal recognition notices
- DVIDS — official captions, features, command events
- Congress.gov / Congressional Record — nomination and confirmation lineage
- NGAAL — council updates / public biographical material
- USAJOBS / Alabama National Guard vacancy announcements — selecting-official context

## Verdict

```text
PROFILE_STATUS        = SOURCE_BOUND_DRAFT
CURRENT_PUBLIC_CORE   = VERIFIED
PERSONAL_SKILL_MATRIX = PARTIAL_ROLE_DERIVED_ONLY
BIOGRAPHY              = NOT_FOUND_IN_CURRENT_RERUN
IDENTITY_COLLAPSE      = BLOCKED
AUTHORITY_CREATED      = FALSE
```
