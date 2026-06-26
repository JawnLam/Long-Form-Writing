---
type: Fleeting
timestamp: "2026-06-06T00:00:00Z"
Item_ID: prototype-lfw-timeline
title: "LFW_Timeline Prototype"
Date_Added: 2026-06-06
Date_Modified: 2026-06-06
Needs_Processing: false
---

# `LFW_Timeline` — Prototype Definition

> **What this file is.** The canonical definition of the `LFW_Timeline` Prototype for the Long-Form-Writing Operating Volume. Items in any cartridge that declare `type: LFW_Timeline` conform to the contract described below.

## Purpose

A Timeline is a **multi-layer chronology** of in-story events. Each Timeline Item operates at exactly one layer: story-time (the manuscript's narrative chronology), world-history (the deeper history of the world the story is set in), real-world (actual historical events that anchor the manuscript), or character-specific (one character's biographical chronology). Distinct from `_continuity.md`'s embedded story-time timeline — Timeline Items provide per-layer source-of-truth where `_continuity.md` becomes the cross-layer reconciliation point. Multiple Timeline Items per cartridge are typical (one per layer; for SFF/historical, often several per layer). Introduced in v1.3.2 (chapter 15 §2).

## Required frontmatter

| Field | Type | Required? | Notes |
|-------|------|-----------|-------|
| `type` | string | yes | Must equal `LFW_Timeline` |
| `Item_ID` | string | yes | Lowercase kebab slug |
| `Title` | string | yes | Timeline name |
| `Date_Added` | date | yes | When the Timeline was created |
| `Date_Modified` | date | yes | When last changed |
| `Needs_Processing` | boolean | yes | Default `false` |
| `lfw_manuscript` | string | yes | Manuscript slug |
| `lfw_item_type` | enum | yes | Must equal `timeline` |
| `lfw_status` | enum | yes | `drafting` \| `established` \| `revised` \| `final` |
| `lfw_timeline_layer` | enum | yes | `story-time` \| `world-history` \| `real-world` \| `character-specific` |
| `lfw_character` | wikilink | required-for-character-specific | Pointer to Character Item; only for `character-specific` layer |
| `lfw_scope` | string | yes | e.g., `"1968-2026"`, `"Day 1-Day 22"`, `"1800 BCE - 1500 BCE"` |

## Body structure

```markdown
# <Timeline name>

## What this timeline tracks
*Brief description of the layer and scope. Whose timeline, what period.*

## Chronological events
| Date | Event | Related Item |
|------|-------|--------------|

## Sub-periods *(optional)*
*For very long timelines, group by era / generation / phase.*

### <Era / period name>

## Cross-references
- **Other Timeline Items in this manuscript:**
- **`_continuity.md` cross-layer reconciliation:** *(events needing explicit reconciliation in continuity)*

## Open questions
*Timeline gaps, decision-deferred events.*

## Notes
```

## Naming

- **Filename pattern:** `<Timeline-Name-Slug>.md` (e.g., `Family-History-1968-2026.md`, `Story-Time-Three-Weeks.md`, `Maya-Life-1984-2026.md`)
- **Location:** `<Cartridge>/Items/Timelines/`
- **Wikilink target:** the filename

## Example Item

```markdown
---
type: LFW_Timeline
timestamp: "2026-06-04T00:00:00Z"
Item_ID: family-history-1968-2026
title: "Family History — 1968-2026"
lfw_manuscript: the-late-frost
lfw_item_type: timeline
lfw_status: established
lfw_timeline_layer: real-world
lfw_scope: "1968-2026"
Date_Added: 2026-04-22
Date_Modified: 2026-06-04
Needs_Processing: false
---

# Family History — 1968-2026

## What this timeline tracks
The factual chronology of the Hollis family from the original 1968 purchase of the vineyard through the present moment of the manuscript (March 2026). Real-world layer: all dates are anchored to actual historical periods (Long Island viticulture history, regional weather patterns, etc.). The timeline is *backstory*; events on this timeline are referenced in interiority and dialogue, never dramatized in scene.

## Chronological events

| Date | Event | Related Item |
|------|-------|--------------|
| 1968 | Hofstra family establishes the original vineyard (precursor to the Hollis property) | (referenced in [[01-02-Frost-Damage-Neighbor]]) |
| 1985 | Hollis family acquires the property from the Hofstras after their bankruptcy | (referenced in [[01-04-Empty-House-Walkthrough]]) |
| 1988 | Maya born | (background) |
| 1990 | Sarah born | (background) |
| 2006 | Maya leaves at 18; the rift | (referenced in [[01-04-Empty-House-Walkthrough]] interiority) |
| 2018 | Father dies; Maya visits for funeral; brief sister-contact | (referenced in [[01-04-Empty-House-Walkthrough]] interiority) |
| 2024 | Mother begins documenting her wishes; writes the letter to Maya | (referenced in [[01-05-The-Letter]]) |
| 2025 | Mother dies | (story-opening backstory) |
| 2026 (March) | Maya returns; story opens | [[01-01-The-Approach]] |

## Cross-references
- **Other Timeline Items:** [[Story-Time-Three-Weeks]] (the story-time layer; March 2026 only)
- **`_continuity.md` cross-layer reconciliation:** Information-state ledger Item-1 (Mother's letter) references the 2024 letter-writing event from this timeline.

## Open questions
- The exact year of the 2006 rift event is fixed; the *month* is not yet decided. Late summer (peak season for vineyard work) vs. winter (when the absence is more felt) — TBD before drafting any backstory-heavy scenes.

## Notes
This timeline is real-world layer because the manuscript is contemporary realism; no world-history layer is needed. Two character-specific timelines exist as separate Items: [[Maya-Life-1984-2026]] and (planned) [[Sarah-Life-1986-2026]].
```

## Relationships

- `LFW_Continuity` — Timeline Items are the per-layer source-of-truth; `_continuity.md` is the cross-layer reconciliation point. The Continuity ledger's Timeline section references Timeline Items rather than duplicating them.
- `LFW_Scene` — Timeline events reference the Scene Items where they're invoked (in interiority, dialogue, or scene-dramatization).
- `LFW_Character` — `character-specific` layer Timelines point to a specific Character via `lfw_character`. Character Items can cross-reference their biographical Timeline.
- `LFW_Worldbuilding` — `world-history` layer Timelines may align with `_worldbuilding.md`'s History (deep) section; the Timeline provides the structured chronology, the Worldbuilding the narrative gloss.
- `LFW_Manuscript_Manifest` — Optional Items.

## Notes

- **One layer per Item.** Don't mix story-time and world-history in a single Timeline; the layers serve different purposes and the cross-layer reconciliation is `_continuity.md`'s job.
- **Layer semantics:**
  - `story-time` — events that occur on-page or are dramatized in scene; the manuscript's narrative chronology
  - `world-history` — the deeper backstory of the world the story is set in (most useful for SFF/fantasy/historical fiction)
  - `real-world` — actual historical events that anchor or are referenced by the manuscript (historical fiction, contemporary fiction with real-world anchors)
  - `character-specific` — one character's biographical chronology; required `lfw_character` pointer
- **Validator check 12** (per v1.3.2) verifies timeline-layer compliance (each Item operates at one layer; required pointer for character-specific).
- **Timelines complement `_continuity.md`'s Timeline section** rather than replace it. Continuity's Timeline is operational (the dates the AI checks during CONTINUITY-CHECK); per-Item Timelines are detailed source-of-truth.
- **Multiple per cartridge.** SFF cartridges typically have at least: story-time, world-history (deep), one per major character. Historical fiction typically has: story-time, real-world (anchoring events), one per major character.
- **Status taxonomy** matches Item-status patterns elsewhere — `drafting`/`established`/`revised`/`final`. `final` means the Timeline is locked for the manuscript's remaining drafts.
