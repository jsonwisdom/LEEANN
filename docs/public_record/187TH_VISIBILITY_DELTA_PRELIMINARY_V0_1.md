# 187TH VISIBILITY DELTA — Preliminary v0.1

```text
ARTIFACT_ID: 187TH_VISIBILITY_DELTA_PRELIMINARY_V0_1
STATUS: SOURCE_BOUND_PRELIMINARY
REPLAY_DATE: 2026-08-16
TARGET: LEEANN_H_CHAVERS_PUBLIC_CAREER_SURFACE
AUTHORITY_CREATED: FALSE
OFFICIAL_AFFILIATION_CLAIMED: FALSE
DISCRIMINATION_FINDING_CREATED: FALSE
```

## Purpose

Freeze the currently published 187th Fighter Wing public surfaces before interpreting them. This artifact measures public metadata visibility; it does not adjudicate discrimination, intent, opportunity loss, promotion, or personnel action.

```text
BOXD = FREEZE_WHAT_IS_PUBLISHED
DELTA = COMPARE_PUBLIC_METADATA
LEAHPRIME = EXPLAIN_SUPPORTED_GAP
ALLEGATION_LANES = HOLD_UNLESS_EVIDENCE_PROMOTES
```

## Cohort 1 — Current Mission Support Group Peers

Official source: https://www.187fw.ang.af.mil/Units/Mission-Support-Group/

Current published commander surface observed on 2026-08-16:

| Commander | Unit | Fields published on current MSG page |
|---|---|---|
| Lt Col Leeann Chavers | Force Support Squadron | rank, name, commander position |
| Lt Col Paul Griggs | Logistics Readiness Squadron | rank, name, commander position |
| Lt Col Joseph Roberson | Communications Squadron | rank, name, commander position |
| Maj Nathan Bridges | Security Forces Squadron | rank, name, commander position |
| Maj Adam Sanders | Civil Engineering | rank, name, commander position |

```text
LEEANN_METADATA_THINNESS = TRUE
CURRENT_MSG_PEER_ENTRIES_THIN = TRUE
PEER_GROUP_ANOMALY = NOT_DEMONSTRATED
SQUADRON_COMMANDER_NORM_ON_CURRENT_MSG_PAGE = THIN_DIRECTORY_ENTRY
```

The current page therefore does not support a claim that Leeann alone receives thinner directory treatment than equivalent Mission Support Group squadron commanders.

## Cohort 2 — Historical FSS Commanders

Current historical pass is incomplete.

One source-bound historical control was surfaced:

- 2016 official 187th Fighter Wing news feature, `Open House brings community to Alabama ANG, fosters relationships`:
  https://www.187fw.ang.af.mil/News/Display/Article/869996/open-house-brings-community-to-alabama-ang-fosters-relationships/
- The article identifies Lt. Col. Paul Griggs as the 187th Force Support Squadron commander and project officer for the event and includes multiple quotations from him.

This demonstrates that an FSS commander can receive richer discoverability through official news coverage than a current directory entry provides.

It does **not** yet establish:

```text
HISTORICAL_FSS_STANDARDIZED_BIOGRAPHY = NOT_ESTABLISHED
LEEANN_PREDECESSOR_RECEIVED_RICHER_STANDARD_TREATMENT = NOT_ESTABLISHED
HISTORICAL_FSS_COHORT_COMPLETE = FALSE
```

## Cohort 3 — 187th Wing Leadership Biography Benchmark

Official leadership index:
https://www.187fw.ang.af.mil/About/Leadership/

The current dedicated leadership class lists:

- Col John D. Caldwell — 187th Fighter Wing Commander
- Col James C. Hall — 187th Fighter Wing Deputy Commander
- CMSgt Mataya C. Williams — 187th Fighter Wing Command Chief

James C. Hall biography:
https://www.187fw.ang.af.mil/About/Leadership/Display/Article/4313013/james-c-hall/

Hall's official biography publishes, among other fields:

- education,
- assignment / career chronology,
- flight information,
- major awards and decorations,
- effective promotion dates.

Therefore:

```text
WING_EXECUTIVE_BIOGRAPHY != SQUADRON_COMMANDER_DIRECTORY_ENTRY
PUBLICATION_TIER_DIFFERENCE = DEMONSTRATED
DIRECT_EQUIVALENT_ROLE_DISPARITY = NOT_DEMONSTRATED
```

Hall is a publication-tier benchmark, not a direct same-position comparator.

## Preliminary Classification

```json
{
  "leeann_official_role": "SOURCE_BOUND",
  "leeann_public_metadata": "THIN",
  "peer_commanders_equally_thin": true,
  "wing_leadership_bios_richer": true,
  "publication_tier_difference_demonstrated": true,
  "peer_group_anomaly": "NOT_DEMONSTRATED",
  "public_discoverability_of_career_history": "LIMITED",
  "gender_disparity_demonstrated": false,
  "deliberate_suppression": "NOT_PROVEN",
  "lost_opportunity": "NOT_PROVEN",
  "historical_fss_cohort": "PARTIAL",
  "authority_created": false
}
```

## Maximum Supported Claim

> The official 187th Fighter Wing site identifies Leeann Chavers as a squadron commander but provides substantially less career metadata than its wing-level leadership biographies; this appears consistent with the current treatment of equivalent Mission Support Group squadron commanders.

The 2016 Paul Griggs FSS news feature adds historical discoverability evidence but does not change that maximum supported claim.

## Full Audit Design

The next audit pass should keep three cohorts separate:

1. **Current MSG peers** — equal-position treatment.
2. **Historical FSS commanders** — whether prior FSS commanders received richer standardized or recurring coverage.
3. **187th leadership biographies** — publication-tier benchmark, not direct peers.

For every person, freeze these fields independently:

```text
CURRENT_DIRECTORY_ENTRY
DEDICATED_BIOGRAPHY
NEWS_FEATURES
EDUCATION
ASSIGNMENTS
PME
AWARDS
PROMOTIONS
PRIOR_SERVICE
DATES
NAME_VARIANTS
```

## Identity Binding Guard

```text
SAME_NAME != SAME_PERSON
RANK + UNIT + DATE + SOURCE -> REQUIRED_IDENTITY_BINDING
NAME_VARIANT != IDENTITY_PROOF
```

No historical article, search result, or name spelling may silently merge two people.

## Allegation Membrane

```text
THIN_METADATA != DISCRIMINATION
PUBLICATION_TIER_DIFFERENCE != GENDER_DISPARITY
DISCOVERABILITY_GAP != DELIBERATE_SUPPRESSION
MISSING_BIOGRAPHY != LOST_OPPORTUNITY
NEWS_FEATURE != STANDARDIZED_BIOGRAPHY
```

Current allegation states:

```text
GENDER_DISPARITY = HOLD / NOT_DEMONSTRATED
DELIBERATE_SUPPRESSION = HOLD / NOT_PROVEN
LOST_OPPORTUNITY = HOLD / NOT_PROVEN
```

## Relationship to Existing Public Profile

This artifact extends, but does not mutate or supersede, the source-bound public profile:

`docs/public_record/LEEANN_H_CHAVERS_SOURCE_BOUND_PUBLIC_PROFILE_V0_1.md`

```text
PUBLIC_PROFILE = PERSON-SPECIFIC SOURCE STATE
VISIBILITY_DELTA = PUBLICATION-SURFACE COMPARISON
VISIBILITY_DELTA != PERSONNEL_RECORD
VISIBILITY_DELTA != COMMAND AUTHORITY
VISIBILITY_DELTA != DISCRIMINATION FINDING
GITHUB_COMMIT != PERSONNEL_ACTION
AUTHORITY_CREATED = FALSE
```

## Replay State

```text
CURRENT_MSG_COHORT = SOURCE_BOUND
HISTORICAL_FSS_COHORT = PARTIAL
WING_BIOGRAPHY_BENCHMARK = SOURCE_BOUND
PEER_GROUP_ANOMALY = NOT_DEMONSTRATED
PUBLICATION_TIER_DIFFERENCE = DEMONSTRATED
ALLEGATION_PROMOTION = NONE
AUTHORITY_CREATED = FALSE
```
