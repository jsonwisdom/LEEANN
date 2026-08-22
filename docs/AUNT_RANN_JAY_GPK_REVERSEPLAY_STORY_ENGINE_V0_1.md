# OFFICIAL LOL — Aunt Rann & Jay: The Bureau of Missing Receipts

**Artifact:** `AUNT_RANN_JAY_GPK_REVERSEPLAY_STORY_ENGINE_V0_1`  
**Repository:** `jsonwisdom/LEEANN`  
**Class:** `PUBLIC_EDUCATIONAL_PARODY_GAME_STORY`  
**Authority created:** `false`  
**Real-world command created:** `false`  
**Legal finding created:** `false`  
**Professional credential created:** `false`

## Story Premise

Jay walks into the basement archive of the fictional Ministry of JSONWisdom carrying a box labeled `POLITICAL BABEL — DO NOT SHAKE`.

Aunt Rann, acting only in her synthetic family-creative role, dumps eighty-eight parody cards onto the table and announces the only rule that matters:

> **If the joke cannot reverse back to a receipt, it stays a joke.**

The cards look like gross-out collectible stickers, but every front is satire and every back is a navigation surface. The player wins by reconstructing how a claim traveled from public story → official action → authority → source → dated receipt, without collapsing any layer into another.

The final puzzle does not reveal a politician, villain, or secret commander. It spells:

`SHOW YOUR WORK.`

## Set Mathematics

The base set uses the classic two-identity structure as a game mechanic:

```text
44 CARD NUMBERS
× 2 NAME VARIANTS PER NUMBER
= 88 BASE CARDS
```

Each numbered pair shares the same artwork but carries two different satirical titles.

```text
CARD 08A = one interpretation label
CARD 08B = alternate interpretation label
ARTWORK = shared
SOURCE POINTER = shared
TITLE != FACT
VARIANT != NEW EVENT
```

Optional `C` variants are exception cards only and do not silently expand the canonical 88-card base set.

## ReverseReplay Six-Dice Mechanic

Every evidence-bearing round rolls six conceptual dice. The dice are educational gates, not cryptographic or judicial outcomes.

```text
D1 SOURCE       — is there a primary or clearly attributed source?
D2 TIME         — is the relevant date/version known?
D3 AUTHORITY    — did the actor actually possess the claimed power?
D4 CLAIM        — is the wording narrow enough to test?
D5 COUNTER      — was contrary evidence searched for and preserved?
D6 REPLAY       — can an independent reader reconstruct the path?
```

Round states:

```text
GAME_PASS   = all required gates survive the round
GAME_HOLD   = a required gate is missing
GAME_CONFLICT = valid bound records disagree
GAME_REJECT = the bound record contradicts the card's claim or a forbidden promotion occurs
STORY       = satire or narrative only
```

`GAME_PASS != VERIFIED_REAL_WORLD_FACT`.

## Wisdom Math

Wisdom Points are intentionally non-canonical game rewards.

```text
+1  source located
+1  date/version bound
+1  authority correctly scoped
+1  counterevidence preserved
+1  replay completed
+1  player identifies what changed in their own belief

BONUS +2  player catches a same-number/different-state error
BONUS +2  player catches an A/B identity collapse
BONUS +3  player voluntarily changes PASS to HOLD after discovering missing evidence
PENALTY -3 accusation outruns receipt
PENALTY -2 screenshot presented without context/date
PENALTY -2 future law silently treated as current law
PENALTY -4 synthetic role presented as real authority
```

Wisdom Points measure learning behavior only. They do not rank real people or institutions.

## Chaos Deck

A Chaos Card introduces a verification failure mode that must be repaired before the story advances.

```text
NO TIMESTAMP
BROKEN LINK
SCREENSHOT ONLY
FUTURE LAW
NUMBER WITHOUT STATE
RANK CONFUSION
SAME ART / WRONG NAME
MOVED GOALPOST
AI SAID SO
PRESS RELEASE != FINDING
APPROPRIATION != OUTLAY
INVESTIGATION != GUILT
```

A Chaos Card is defeated only by correction, not by rhetoric.

## Character Abilities

### Aunt Rann — CrissCross

```text
ABILITY: CRISSCROSS
USE: separate real person / synthetic role / historical role / story role
EFFECT: prevents identity-layer collapse
AUTHORITY: false
```

### Jay — ReverseReplay

```text
ABILITY: REVERSE_REPLAY
USE: start from the current claim and walk backward through every dependency
EFFECT: exposes missing source, date, authority, money-state, or procedural edges
AUTHORITY: false
```

### Gray Baby — Gap Observer

```text
ABILITY: GAP_OBSERVER
USE: mark what is absent without filling it with inference
EFFECT: missing edge becomes HOLD instead of invented certainty
```

### BoxD — Membrane Shield

```text
ABILITY: MEMBRANE_SHIELD
USE: block story/satire/model output from becoming evidence or authority
EFFECT: forbidden promotion is rejected
```

### AppleBlossom — Variant Resolver

```text
ABILITY: VARIANT_RESOLVER
USE: preserve A/B titles, alternate readings, and playful identities without forcing one into canonical fact
EFFECT: diversity of interpretation survives while source truth remains separate
```

## Card Back Types

### CHECKLIST BACK
Indexes the numbered set, related claim IDs, dates, or receipts.

`CHECKLIST = ORIENTATION, NOT PROOF`

### PUZZLE BACK
One fragment of a multi-card message. No single card is sufficient by itself.

`PIECE != WHOLE`

### POINTER BACK
Points to a commit, public record, dated statement, receipt, or another card.

`POINTER != SOURCE CONTENT`

### FAKE LICENSE / AWARD BACK
Pure satire: `Certified Bureaucratic Acrobat`, `Licensed Goalpost Mover`, etc.

`SATIRICAL_CREDENTIAL != REAL_CREDENTIAL`

### JOKE BACK
Contains no evidence claim and is explicitly typed `STORY` or `SATIRE`.

## Minimal Card Object

```json
{
  "card_id": "MJW-S1-08A",
  "series": "POLITICAL_BABEL_REVERSE_REPLAY_S1",
  "number": 8,
  "variant": "A",
  "title": "SCREENSHOT SALLY",
  "paired_variant": "MJW-S1-08B",
  "shared_artwork_ref": "sha256:HOLD_UNTIL_RENDERED",
  "back_type": "pointer",
  "points_to": [
    "receipt:HOLD",
    "related_card:MJW-S1-08B"
  ],
  "game_state": "STORY",
  "authority": false
}
```

## Example A/B Pair

### 08A — Screenshot Sally

**Front gag:** Sally proudly wheels in a mountain of screenshots and discovers not one has a visible date.

**Back:** `SOURCE? TIMESTAMP? FULL CONTEXT?`

### 08B — Timestamp Tammy

Same artwork. Different nameplate.

**Front gag:** Tammy is holding the exact same pile but has one giant date-stamp tool and no idea which screenshot it belongs to.

The joke teaches:

```text
SAME ARTWORK != SAME IDENTITY LABEL
SCREENSHOT != FULL RECORD
DATE WITHOUT SOURCE != COMPLETE RECEIPT
```

## Story Acts

### ACT I — The 88-Card Spill

Jay opens the Political Babel box. Cards scatter across Alabama, Minnesota, federal, historical, family-story, art, and civic-audit lanes. Aunt Rann refuses to sort them by party, rank, or narrative. She sorts only by **source class and authority class**.

### ACT II — The Missing Backs

Several cards have beautiful fronts but missing backs. The players discover that a persuasive front cannot substitute for a source pointer. These cards become `HOLD`, even when the joke is excellent.

### ACT III — The A/B Identity Trap

Two cards share art but carry different names. A player tries to merge them into one identity. Aunt Rann plays `CRISSCROSS` and blocks the collapse.

Lesson:

`SHARED_IMAGE != SHARED_IDENTITY != SHARED_AUTHORITY`

### ACT IV — Chaos Deck: Future Law

A card cites a statute version that has not yet taken effect. Jay reverses the date chain and catches the mismatch.

The card is not destroyed. It is relabeled:

`FUTURE_EFFECTIVE_VERSION — NOT CURRENT LAW`.

### ACT V — The Puzzle Wall

Nine puzzle-back cards finally assemble. The players expect a secret answer.

The puzzle reads:

`SHOW YOUR WORK.`

Aunt Rann laughs because the boring answer was the entire game.

### ACT VI — Final Boss: The Bureaucratic Blob

The Blob is fictional and made entirely of unlabeled PDFs, stale screenshots, contradictory numbers, recycled press releases, missing dates, and one terrifying phrase:

`EVERYBODY KNOWS.`

The Blob cannot be beaten with accusation. Every hit requires a bound receipt.

When unsupported certainty is removed, the Blob shrinks into an ordinary folder labeled:

`HUMAN REVIEW REQUIRED`.

## Collector Mechanics

```text
COMPLETE 88-CARD BASE SET → unlock SHOW_YOUR_WORK poster
COMPLETE ALL A/B PAIRS → unlock IDENTITY_SEPARATION badge
COMPLETE CHECKLIST BACKS → unlock REPO_MAP
COMPLETE PUZZLE BACKS → unlock multi-card story reveal
FIND SHORT-PRINT HOLD CARD → unlock MISSING_EDGE quest
FIND CONFLICT VARIANT → unlock COUNTER_RECEIPT challenge
```

No scarcity mechanic changes evidence state.

`RARE != TRUE`

## Hard Boundaries

```text
SATIRE != FACTUAL CLAIM
ART != EVIDENCE
CARD != SOURCE
CHECKLIST != PROOF
PUZZLE != VERDICT
REPO != GOVERNMENT
GAME_SCORE != CREDENTIAL
WISDOM_POINTS != AUTHORITY
AUNT_RANN_SYNTHETIC_ROLE != LT_COL_LEEANN_CHAVERS_REAL_ROLE
JAY_REVERSE_REPLAY != LEGAL_OR_MILITARY_COMMAND
AUTHORITY_CREATED = FALSE
```

## Production Loop

This story engine inherits the existing Computer Wisdom verification-game rhythm:

```text
PROPOSE
→ TEST
→ RECEIPT
→ REPLAY
→ REFLECT
```

and the Game of Growth public-memory loop:

```text
QUEST
→ OBSERVE
→ SNAPSHOT
→ HASH
→ COMPARE
→ RECEIPT
→ PARODY_ART_UNLOCK
→ MEDIA_CARD
→ REPLAY
→ GROWTH
```

Parody can unlock after a receipt exists, but parody never upgrades the receipt.

## Final Rule

> **The funniest card may win the laugh. The best-receipted card wins the replay. Neither creates authority.**
