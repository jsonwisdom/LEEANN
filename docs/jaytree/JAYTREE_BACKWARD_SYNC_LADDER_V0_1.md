# JayTree Backward Sync Ladder v0.1

Status: `ACTIVE / REFERENCE IMPLEMENTATION`  
Root: `jsonwisdom/LEEANN`  
Authority created: `FALSE`

## Purpose

JayTree turns repository history into a replayable backward-sync ladder instead of a narrative recap.

```text
NOW
↓
TODAY
↓
YESTERDAY
↓
LAST_7_DAYS
↓
LAST_30_DAYS
↓
LAST_3_YEARS
↓
REPOSITORY_GENESIS / GAP
```

Every rung is measured from Git history. A later summary may describe a rung, but the receipt is the commit boundary, file delta, and generated hash.

## Constitutional rules

```text
SYNC_CLAIM != SYNC_RECEIPT
REMOTE_UPDATED != LOCAL_MACHINE_PULLED
PUBLIC_REPO_SCAN != PRIVATE_REPO_SCAN
WINDOW_SUMMARY != CAUSATION
MISSING_HISTORY != NO_HISTORY
UPSTREAM_PASS != DOWNSTREAM_PROMOTION
AUTHORITY_CREATED = FALSE
```

Series 004 Burden Rule applies:

```text
CLAIMANT_OF_STRONGER_STATE -> BURDEN_OF_PROOF
NO_RECEIPT != FALSE
NO_RECEIPT != PROVEN
CAPTURE_FAILURE != BURDEN_SHIFT
```

## Window grammar

The reference machine timezone is `America/Chicago`. Each execution resolves exact UTC boundaries and records them in the output receipt.

Required windows:

```text
TODAY
YESTERDAY
LAST_7_DAYS
LAST_30_DAYS
LAST_3_YEARS
```

Each rung records:

```text
window_id
start_local
end_local
start_utc
end_utc
base_before_window_sha
first_commit_in_window
last_commit_in_window
commit_count
changed_files
status
```

`status` is one of:

```text
PASS
EMPTY_WINDOW
GAP_HISTORY
CONFLICT
```

## LEEANN reference implementation

LEEANN is the first live root because it is also Jay's Alabama-machine console surface.

```text
GitHub / LEEANN
    ↓ git pull
C:\Users\jsonw\LEEANN
    ↓
docs/
    ↓
localhost:8000
```

A GitHub commit proves the remote state. A successful `git pull` on RYZEN5 proves the local transition. Those are separate receipts.

## Structure-wide application

JayTree applies to the JSONWisdom estate through measurement-first rollout:

```text
LEEANN reference implementation
    ↓
repo inventory
    ↓
classify each repository
    ↓
measure history windows
    ↓
report workflow gaps
    ↓
correct only receipted defects
    ↓
optional per-repo caller
```

Repository classes:

```text
ACTIVE_NONEMPTY
EMPTY
ARCHIVED
PRIVATE_SCOPE_REQUIRED
WORKFLOW_PRESENT
WORKFLOW_GAP
DEFAULT_BRANCH_NONSTANDARD
```

No repository is rewritten merely because another repository uses a different branch, language, workflow, or age.

## Correction rule

JayTree corrections are additive by default:

```text
OBSERVE
→ RECEIPT
→ GAP / CONFLICT
→ PROPOSED_CORRECTION
→ WORKFLOW TEST
→ HUMAN / REPO-SCOPED ACCEPTANCE
```

No force pushes. No synthetic backdating. No rewriting old commits to make the tree look cleaner.

## Machine sync receipt

For RYZEN5 the decisive local receipt remains:

```text
HOST = RYZEN5
REPOSITORY = jsonwisdom/LEEANN
REMOTE_HEAD = <sha>
LOCAL_HEAD_AFTER_PULL = <same sha>
PULL_RESULT = PASS
OBSERVED_AT = <timestamp>
```

`REMOTE_HEAD = X` alone does not prove `LOCAL_HEAD = X`.

## Current posture

```text
JAYTREE = ACTIVE
LEEANN = REFERENCE_ROOT
ESTATE_ROLLOUT = MEASUREMENT_FIRST
FORCE_PUSH = FORBIDDEN_BY_WORKFLOW
HISTORY_REWRITE = FALSE
AUTHORITY_CREATED = FALSE
```
