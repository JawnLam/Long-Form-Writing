---
type: Fleeting
timestamp: "2026-06-06T00:00:00Z"
Item_ID: prototype-lfw-state
title: "LFW_State Prototype"
Date_Added: 2026-06-06
Date_Modified: 2026-06-06
Needs_Processing: false
---

# `LFW_State` — Prototype Definition

> **What this file is.** The canonical definition of the `LFW_State` Prototype for the Long-Form-Writing Operating Volume. Items in any cartridge that declare `type: LFW_State` conform to the contract described below.

## Purpose

The State file is the **single source of truth for where the manuscript stands**. The AI reads it at session start; the AI writes to it at session end. It captures the cartridge's current lifecycle stage, today's focus, word-count progress, Item status snapshot, open threads, stuck flags, current revision pass, and recent-sessions log. **Required backbone in every cartridge.** Single per-cartridge file at `_state.md`. The Manifest is who the cartridge *is*; the State is where the cartridge *is now*. State is overwritten at each session-end (per chapter 06's state-persistence contract — overwrite-style); session-history accumulates in the `Sessions/` folder, not in this file.

## Required frontmatter

| Field | Type | Required? | Notes |
|-------|------|-----------|-------|
| `type` | string | yes | Must equal `LFW_State` |
| `Item_ID` | string | yes | Format: `<manuscript-slug>-state` |
| `Title` | string | yes | Format: `"<Manuscript Title> — State"` |
| `Date_Added` | date | yes | When the State was first created |
| `Date_Modified` | date | yes | When last changed (typically every session) |
| `Needs_Processing` | boolean | yes | Default `false` |
| `lfw_manuscript` | string | yes | Manuscript slug |
| `lfw_lifecycle_stage` | enum | yes | `outlining` \| `drafting` \| `revising` \| `fact-checking` \| `polishing` \| `with-beta-readers` \| `final-revision` \| `final` \| `shipped` \| `abandoned` |
| `lfw_genre` | string | yes | Mirrors Manifest's genre |
| `lfw_sessions_completed` | integer | yes | Cumulative session count |
| `lfw_total_writing_hours` | number | yes | Cumulative hours |
| `lfw_last_session_date` | date | optional | Null until first session |
| `lfw_next_session_default_activity` | string | yes | Activity name; OUTLINE / DRAFT / REVISE / SCENE-AUDIT / etc. |
| `lfw_current_revision_pass` | enum | optional | Null \| `structural` \| `voice` \| `accuracy` \| `prose-line` \| `custom` |
| `lfw_current_revision_round` | integer | yes | 0 if no pass active |
| `lfw_word_count_total` | integer | yes | Current total word count |
| `lfw_word_count_target` | integer | yes | Target total from Manifest |

## Body structure

```markdown
# <Manuscript Title> — State

## Current Lifecycle Stage
- **Stage:**
- **Stage entry date:**
- **Sessions completed in this stage:**

## Today's Focus
*What today's session is/was about. Or what last session left as tomorrow's seed.*

## Word Count Progress
| Scope | Current | Target |
|-------|---------|--------|

## Item Status Snapshot

### Chapters
| Chapter | Status | Word count | Last touched |
|---------|--------|------------|--------------|

### Sections / Scenes
| Item | Type | Status | Word count | Last touched |
|------|------|--------|------------|--------------|

### Characters / Threads / Sources

## Open Threads (to address next session)
- [ ]

## Stuck Flags
*Anywhere the writer flagged "I'm stuck here."*

## Revision Pass Progress
- **Current pass:**
- **Current round:**
- **Items remaining in current pass:**

## Recent Sessions
*Most recent first.*

## Quality gates for this stage
- [ ]
```

## Naming

- **Filename:** `_state.md` (fixed; one per cartridge)
- **Location:** cartridge root
- **Wikilink target:** `_state`

## Example Item

```markdown
---
type: LFW_State
timestamp: "2026-06-04T00:00:00Z"
Item_ID: the-late-frost-state
title: "The Late Frost — State"
Date_Added: 2026-04-15
Date_Modified: 2026-06-04
Needs_Processing: false
lfw_manuscript: the-late-frost
lfw_lifecycle_stage: drafting
lfw_genre: fiction
lfw_sessions_completed: 23
lfw_total_writing_hours: 31.5
lfw_last_session_date: 2026-06-04
lfw_next_session_default_activity: DRAFT
lfw_current_revision_pass: null
lfw_current_revision_round: 0
lfw_word_count_total: 32400
lfw_word_count_target: 85000
---

# The Late Frost — State

## Current Lifecycle Stage
- **Stage:** drafting
- **Stage entry date:** 2026-04-26
- **Sessions completed in this stage:** 18

## Today's Focus
Last session ended at the close of [[02-02-The-Garage-Argument]]. Next session: open [[02-03-Hector-Intervenes]]; the want is to draft Hector's arrival and the de-escalation of the argument; quality gate is that Hector reads as a real third party with his own purpose, not a function.

## Word Count Progress
| Scope | Current | Target |
|-------|---------|--------|
| Total | 32,400 | 85,000 |
| Chapter 1 | 12,800 | ~14,000 |
| Chapter 2 | 11,600 | ~14,000 |
| Chapter 3 | 8,000 | ~14,000 |

## Item Status Snapshot

### Chapters
| Chapter | Status | Word count | Last touched |
|---------|--------|------------|--------------|
| [[Chapter-01-Maya-Arrives]] | drafted | 12,800 | 2026-05-15 |
| [[Chapter-02-Sarah-Knows]] | drafting | 11,600 | 2026-06-04 |
| [[Chapter-03-The-Third-Party]] | drafting | 8,000 | 2026-06-04 |

### Scenes
| Item | Type | Status | Word count | Last touched |
|------|------|--------|------------|--------------|
| [[01-01-The-Approach]] | scene | drafted | 2,400 | 2026-05-15 |
| [[02-02-The-Garage-Argument]] | scene | drafting | 3,100 | 2026-06-04 |
| [[02-03-Hector-Intervenes]] | scene | planned | 0 | — |

### Characters / Threads / Sources
- Characters: Maya (established), Sarah (developing), Hector (developing), Mother (established as off-page presence)
- Threads: n/a (fiction)
- Sources: n/a (fiction)

## Open Threads (to address next session)
- [ ] Hector's voice register hasn't been calibrated; first draft will surface it
- [ ] Sarah's interiority is still glimpsed only through dialogue; consider whether one scene needs Sarah-POV
- [ ] [[02-02-The-Garage-Argument]] feels rushed at present; flagged for REVISE after Chapter 2 closes

## Stuck Flags
*(none active)*

## Revision Pass Progress
- **Current pass:** none
- **Current round:** 0
- **Items remaining in current pass:** —

## Recent Sessions
- 2026-06-04 — DRAFT — [[02-02-The-Garage-Argument]] continued; 1,400 words; argument's escalation arc drafted but de-escalation not yet reached
- 2026-06-02 — SCENE-AUDIT — [[02-01-Sarah-Finds-The-Letter]] checked against spine; passes; sequel-typed
- 2026-05-31 — DRAFT — [[02-01-Sarah-Finds-The-Letter]] drafted; 2,200 words
- 2026-05-29 — OUTLINE — Chapter 3 macro-shape settled

## Quality gates for this stage
- [ ] Reach 50% word-count target before MIDDLE-AUDIT (chapter 16 §3 — currently at 38%)
- [x] Both POVs (Maya alone, in this manuscript) have voice-register established
- [x] Spine v3 stable; no v4 in sight
- [ ] Active overlay (Story Circle) checked at Midpoint
```

## Relationships

- `LFW_Manuscript_Manifest` — Manifest is who; State is where-now. The two are the cartridge identity-and-status pair.
- `LFW_Session` — Each Session log appends to `Sessions/`; the State's `Recent Sessions` is a derived view of the last few.
- `LFW_Revision_Pass` — If a revision pass is active, State's `lfw_current_revision_pass` and the revision-pass-progress section reference the active `LFW_Revision_Pass` Item.
- `LFW_Outline` — State tracks Item status; the Outline tracks the planned/drafted distinction at the chapter level. The two stay in sync.
- All Item Prototypes — State's Item Status Snapshot lists everything in the cartridge with current status and last-touched. Per chapter 06's state-persistence contract.

## Notes

- **One per cartridge, required.** Validator fails any cartridge missing `_state.md`.
- **Overwrite-style persistence.** State is rewritten at each session-end. Don't append session-history to State — that's what `Sessions/` is for. Per `_writing-engine/06-STATE-PERSISTENCE.md` equivalent (LFW's chapter 03 on cadence and sessions documents this).
- **Today's Focus is the bootstrapping pointer.** A fresh AI session reads State, sees Today's Focus, and knows what to propose. If Today's Focus is empty, the session begins with INTERVIEW to establish focus.
- **`lfw_next_session_default_activity` is the soft proposal.** The AI proposes this activity at session start; the writer may override.
- **Lifecycle stages are not linear.** A cartridge can go drafting → revising → drafting (when revision surfaces gaps that need new drafting). The stage transitions are documented in Session logs.
- **Stuck flags are load-bearing.** When the writer flags "I'm stuck here," it persists in State across sessions until unstuck. STUCK-DIAGNOSTIC activities work against this list.
- **Quality gates are stage-specific.** Each lifecycle stage has its own quality gates; State maintains the current stage's checklist.
