---
type: Fleeting
timestamp: "2026-06-06T00:00:00Z"
Item_ID: prototype-lfw-storyboard
title: "LFW_Storyboard Prototype"
Date_Added: 2026-06-06
Date_Modified: 2026-06-06
Needs_Processing: false
---

# `LFW_Storyboard` — Prototype Definition

> **What this file is.** The canonical definition of the `LFW_Storyboard` Prototype for the Long-Form-Writing Operating Volume. Items in any cartridge that declare `type: LFW_Storyboard` conform to the contract described below.

## Purpose

The Storyboard is a **scene-card view of the manuscript** — every Scene Item rendered as a single-row card showing type, status, POV, value-shift (or decision for sequels), and a one-line descriptor. The whole manuscript's shape at a glance. Optional backbone. Useful for book-scale revision (READ-THROUGH, BETA-PREP) and for explaining the manuscript's shape to a critique partner or agent. **Derived from Scene Items** — never edit story content here; always go through the Scene Item. The Storyboard is a *view*, not a *source*. Stale storyboards are worse than no storyboard (F47); the staleness rule is that storyboards should not exceed two sessions of drift behind drafted Items. Introduced in v1.3.2 (chapter 15 §3).

## Required frontmatter

| Field | Type | Required? | Notes |
|-------|------|-----------|-------|
| `type` | string | yes | Must equal `LFW_Storyboard` |
| `Item_ID` | string | yes | Format: `<manuscript-slug>-storyboard` |
| `Title` | string | yes | Format: `"<Manuscript Title> — Storyboard"` |
| `Date_Added` | date | yes | When the Storyboard was created |
| `Date_Modified` | date | yes | When last regenerated |
| `lfw_manuscript` | string | yes | Manuscript slug |
| `lfw_storyboard_version` | integer | yes | Bumped on substantial restructuring |

## Body structure

```markdown
# <Manuscript Title> — Storyboard

## Last updated
*(Date — keep current; flag stale state explicitly)*

## Manuscript shape at a glance
- **Chapters drafted:** X of Y planned
- **Total scenes:** N (M drafted, P revising, Q planned)
- **Word count:** N of target

## Scene cards (chapter by chapter)

### Chapter 01 — <Chapter title>
| Scene | Type | Status | POV | Value-shift / Decision | One-line |
|-------|------|--------|-----|------------------------|----------|

### Chapter 02 — <Chapter title>

## Open structural questions

## Audit notes from last READ-THROUGH

## How to use this storyboard
```

## Naming

- **Filename:** `_storyboard.md` (fixed; one per cartridge)
- **Location:** cartridge root
- **Wikilink target:** `_storyboard`

## Example Item

```markdown
---
type: LFW_Storyboard
timestamp: "2026-06-04T00:00:00Z"
Item_ID: the-late-frost-storyboard
title: "The Late Frost — Storyboard"
Date_Added: 2026-05-20
Date_Modified: 2026-06-04
lfw_manuscript: the-late-frost
lfw_storyboard_version: 3
---

# The Late Frost — Storyboard

## Last updated
2026-06-04 (current; refreshed at session-end yesterday)

## Manuscript shape at a glance
- **Chapters drafted:** 2 of 6 planned
- **Total scenes:** 28 (15 drafted, 1 drafting, 12 planned)
- **Word count:** 32,400 of 85,000 target (38%)

## Scene cards

### Chapter 01 — Maya Arrives
| Scene | Type | Status | POV | Value-shift / Decision | One-line |
|-------|------|--------|-----|------------------------|----------|
| [[01-01-The-Approach]] | scene | drafted | Maya | distant → arriving | Maya driving up Highway 12 |
| [[01-02-Frost-Damage-Neighbor]] | scene | drafted | Maya | unaware → aware-of-fragility | Hector explains the frost damage at the property line |
| [[01-03-The-Driveway]] | scene | drafted | Maya | arriving → present | Maya at the gate; first look at the house |
| [[01-04-Empty-House-Walkthrough]] | sequel | drafted | Maya | decision: open Mother's office | Inside; furniture covered; the rift memory |
| [[01-05-The-Letter]] | scene | drafted | Maya | private → carrying-a-secret | Maya finds Mother's letter |

### Chapter 02 — Sarah Knows
| Scene | Type | Status | POV | Value-shift / Decision | One-line |
|-------|------|--------|-----|------------------------|----------|
| [[02-01-Sarah-Finds-The-Letter]] | scene | drafted | Maya | hidden → exposed | Sarah finds the letter in Maya's bag |
| [[02-02-The-Garage-Argument]] | scene | drafting | Maya | civil → inflamed | Sisters argue in the equipment garage |
| [[02-03-Hector-Intervenes]] | scene | planned | Maya | inflamed → forced-pause | Hector arrives unexpectedly |

### Chapter 03 — The Third Party (planned)
| Scene | Type | Status | POV | Value-shift / Decision | One-line |
|-------|------|--------|-----|------------------------|----------|
| [[03-01-After-The-Argument]] | sequel | planned | Maya | decision: tell Sarah the letter's full contents | Quiet sequel; the next scene's want forms |
| [[03-02-The-Disclosure]] | scene | planned | Maya | secret → shared (with cost) | Maya tells Sarah everything |

## Open structural questions
- Chapter 3 may need a fourth scene; the disclosure may need its own breathing room. Revisit after Chapter 2 closes.
- The current Chapter 4 outline has [[Sarah-POV-Garden-Scene]] as the manuscript's only Sarah-POV scene. Open question: does the manuscript need exactly one Sarah-POV scene, or none? Decide before drafting Chapter 4.

## Audit notes from last READ-THROUGH
Last READ-THROUGH was at the close of Chapter 1 (2026-05-16). Findings:
- Scene-level work is strong; chapter-level transitions need attention
- 01-04 → 01-05 transition is the weakest junction; consider revising 01-04's closing or 01-05's opening to bridge

## How to use this storyboard
- Read at READ-THROUGH activities to see the manuscript at glance
- Read at BETA-PREP for the final structural audit
- Cross-reference with [[_spine]] for causal chain, [[_promises]] for setup/payoff distribution
- Update at session-end whenever a Scene Item's status, value-shift, or one-line changes
```

## Relationships

- `LFW_Scene` — Storyboard is **derived** from Scene Items. Every Scene's status, value-shift, POV, and one-line descriptor appears here. Never edit story content in the Storyboard — go through the Scene Item.
- `LFW_Chapter` — Scene cards are grouped by Chapter.
- `LFW_Spine` — Storyboard renders the structural what; Spine renders the causal why. The two cross-reference often during READ-THROUGH.
- `LFW_Promises` — Setup/payoff distribution across the storyboard is a visual check the Storyboard makes easy.
- `LFW_Outline` — Outline is the planned shape; Storyboard is the current actual shape (planned + drafted + revising).
- `LFW_Manuscript_Manifest` — Optional backbone.

## Notes

- **Optional backbone.** Most useful for book-scale revision and for explaining the book's shape to outside readers. Cartridges in heavy drafting mode may skip it; cartridges in revision benefit substantially.
- **Derived view, not authoritative.** The Storyboard restates what the Scene Items already say. If the Storyboard and a Scene disagree, the Scene wins; the Storyboard needs regeneration.
- **Staleness rule.** Per chapter 15 §3: don't let the Storyboard drift more than two sessions behind drafted Items. F47 (stale storyboard worse than no storyboard) names the failure mode.
- **The one-line descriptor is the discipline.** One-line means one line. If a scene's one-line is hard to write, the scene may be doing too much.
- **`Value-shift / Decision` column unifies scenes and sequels.** Scenes carry value-shifts (from-state → to-state); sequels carry decisions (the next scene's want).
