# JSONWisdom Structure — JayTree Correction Report v0.1

Status: `ACTIVE / MEASUREMENT-FIRST`  
Reference root: `jsonwisdom/LEEANN`  
Machine surface: `C:\Users\jsonw\LEEANN`  
Authority created: `FALSE`

## Objective

Apply the JayTree backward-sync grammar across the JSONWisdom repository estate without rewriting history or treating workflow differences as defects by default.

```text
TODAY
→ YESTERDAY
→ LAST_7_DAYS
→ LAST_30_DAYS
→ LAST_3_YEARS
```

The same five-rung measurement applies to every nonempty repository once that repository has a local/full-history execution context or an equivalent API receipt.

## LEEANN findings

LEEANN is now the reference implementation.

Observed pre-JayTree master state included:

```text
HEAD_BEFORE_JAYTREE = 8ff6afe282f1bfacd3b18d15e4d9014806ccabfb
YESTERDAY_BASE      = 738f74cc7194639894190f536ca29be603ca02e5
YESTERDAY_DELTA     = 16 reachable commits from base to pre-JayTree head
```

The prior daily console measured a rolling `24.hours` window. That is useful operational telemetry but it is not the same object as a calendar-day replay.

Correction:

```text
ROLLING_24H != TODAY
ROLLING_24H != YESTERDAY
```

JayTree adds explicit local calendar boundaries using `America/Chicago`.

## Workflow correction #1 — DST-safe schedule

Initial JayTree schedule used `05:37 UTC`.

Measured defect:

```text
05:37 UTC = 00:37 CDT
05:37 UTC = 23:37 CST (previous local day)
```

Therefore the original schedule could execute before local midnight during standard time and misclassify `TODAY`.

Corrected schedule:

```text
06:37 UTC
= 01:37 CDT
= 00:37 CST
```

Status: `CORRECTED`.

## Workflow correction #2 — remote receipt vs Alabama-machine delivery

A GitHub Actions artifact is not automatically present on RYZEN5.

```text
WORKFLOW_ARTIFACT != LOCAL_MACHINE_FILE
REMOTE_COMMIT != LOCAL_PULL
```

Correction: JayTree now prepares and commits `docs/jaytree-status.json`. The existing Alabama-machine use case can receive it through the already observed `git pull` path.

Status: `CORRECTED_REMOTE_SURFACE / LOCAL_PULL_STILL_REQUIRES_RECEIPT`.

## Workflow correction #3 — machine-generated commits

LEEANN's existing console workflow creates commits such as:

```text
chore: refresh Wisdom Family Console daily update
chore: refresh LeahPrime machine heartbeat
```

These are valid state transitions, but they must not be silently counted as human-authored work. Existing console logic already filters those subjects for its human activity panel.

JayTree keeps all commits in the Git history receipt but does not infer human intent from machine-generated commits.

Status: `BOUNDARY_PRESERVED`.

## Workflow correction #4 — historical pinned replay

`timegraph-genesis-replay.yml` deliberately checks out a fixed historical SHA.

That can prove replay of the pinned state, but it cannot prove the current PR head.

```text
PINNED_HISTORICAL_REPLAY = PASSABLE_OBJECT
PINNED_HISTORICAL_REPLAY != CURRENT_PR_HEAD_REPLAY
```

Status: `NOT_A_BUG_BY_ITSELF / CLAIM_CEILING_MUST_STAY_EXPLICIT`.

No mutation is made to that workflow in this pass.

## JSONWisdom estate rollout

The estate audit has two coverage modes:

```text
PUBLIC_ONLY
ACCOUNT_TOKEN_SCOPE
```

Without a deliberately supplied `JAYTREE_ESTATE_TOKEN`, the GitHub workflow uses the public user API and must report private coverage as unmeasured.

```text
PUBLIC_REPO_SCAN != PRIVATE_REPO_SCAN
PRIVATE_COVERAGE_WITHOUT_TOKEN = GAP_AUTH_SCOPE
```

This is intentional fail-closed behavior.

## Per-repository correction classifier

Every repository is classified before mutation:

```text
ACTIVE_NONEMPTY
EMPTY
ARCHIVED
PRIVATE
DEFAULT_BRANCH_NONSTANDARD
WORKFLOW_PRESENT
WORKFLOW_GAP
```

The correction engine must not impose `main` on `master`, or `master` on `main`, merely for aesthetic consistency.

```text
NONSTANDARD != WRONG
OLD != BROKEN
EMPTY != FAILED
NO_WORKFLOW != WORKFLOW_FAILURE
```

## Rollout order

```text
1. LEEANN — reference implementation / machine delivery
2. JSONWisdom estate inventory — all observable repositories
3. Active nonempty repositories — self-audit candidate set
4. Workflow-bearing repositories — inspect before correction
5. Empty / archived repositories — classify, do not manufacture activity
6. Private repositories — require explicit sufficient token scope
```

## Mutation policy

Allowed:

```text
add receipt files
add audit workflows
correct measured schedule/path/permission defects
add explicit claim ceilings
open tracking issues
```

Forbidden by this rollout:

```text
force push
rebase published history merely for cleanliness
backdate commits
rewrite source claims
silently merge draft PRs
promote GAP to PASS
```

## Current state

```text
JAYTREE_LEEANN = ACTIVE
TODAY_SERIES004_BRIDGE = PRESENT
BACKWARD_SYNC_WORKFLOW = ACTIVE
RYZEN5_DELIVERY_SURFACE = docs/jaytree-status.json
RYZEN5_LOCAL_PULL = PENDING_RECEIPT
ESTATE_INVENTORY = WORKFLOW_ACTIVE
PRIVATE_ESTATE_COVERAGE = TOKEN_DEPENDENT
HISTORY_REWRITE = FALSE
AUTHORITY_CREATED = FALSE
```
