---
type: Fleeting
timestamp: "2026-06-06T00:00:00Z"
Item_ID: type-lfw-overlay-heros-journey
title: "LFW_Overlay_Heros_Journey Type"
Date_Added: 2026-06-06
Date_Modified: 2026-06-06
Needs_Processing: false
---

# `LFW_Overlay_Heros_Journey` — Type Definition

> **What this file is.** The canonical definition of the `LFW_Overlay_Heros_Journey` Type for the Long-Form-Writing Operating Volume. Items in any cartridge that declare `type: LFW_Overlay_Heros_Journey` conform to the contract described below.

## Purpose

A Hero's Journey Overlay is an opt-in **reading lens** that maps the manuscript's structure onto Joseph Campbell's monomyth as distilled by Christopher Vogler — twelve stages from Ordinary World to Return with the Elixir. Best fit: mythic, fantasy, quest, science fiction, coming-of-age structures. Opt-in via `lfw_active_overlays: [heros-journey]` in the Manifest. One overlay file per active overlay per cartridge. Introduced in v1.3.1 (chapter 14 §2). Like all overlays: a reading lens, not a prescription. If the spine doesn't fit, the overlay is the wrong lens.

## Required frontmatter

| Field | Type | Required? | Notes |
|-------|------|-----------|-------|
| `type` | string | yes | Must equal `LFW_Overlay_Heros_Journey` |
| `Item_ID` | string | yes | Format: `<manuscript-slug>-overlay-heros-journey` |
| `Title` | string | yes | Format: `"<Manuscript Title> — Hero's Journey Overlay"` |
| `Date_Added` | date | yes | When the overlay was added |
| `Date_Modified` | date | yes | When last changed |
| `lfw_manuscript` | string | yes | Manuscript slug |
| `lfw_overlay_type` | enum | yes | Must equal `heros-journey` |
| `lfw_overlay_version` | integer | yes | Bumped on substantial restructuring |

## Body structure

```markdown
# <Manuscript Title> — Hero's Journey Overlay

## The twelve stages
| # | Stage | Question | Scene(s) | Notes |
|---|-------|----------|----------|-------|
| 1 | Ordinary World | Life before the call? | | |
| 2 | Call to Adventure | What disrupts? | | |
| 3 | Refusal of the Call | Why resist? | | |
| 4 | Meeting the Mentor | Who aids? | | Mentor may be human, object, knowledge |
| 5 | Crossing the Threshold | What commits the hero? | | |
| 6 | Tests, Allies, Enemies | How is the hero formed? | | |
| 7 | Approach to the Inmost Cave | What precedes the ordeal? | | |
| 8 | Ordeal | Near-death (literal or symbolic)? | | |
| 9 | Reward | What is gained? | | |
| 10 | The Road Back | What pulls toward home? | | |
| 11 | Resurrection | Final confrontation? | | |
| 12 | Return with the Elixir | What is brought back? | | |

## Shape-fit assessment
- **Stages with clear coverage:**
- **Stages with uncertain coverage:**
- **Stages with no coverage:**

## Divergence notes

## Risks

## How to use this overlay

## Cross-reference
```

## Naming

- **Filename:** `_overlay-heros-journey.md` (fixed; one per cartridge with this overlay active)
- **Location:** cartridge root
- **Wikilink target:** `_overlay-heros-journey`

## Example Item

```markdown
---
type: LFW_Overlay_Heros_Journey
timestamp: "2026-06-04T00:00:00Z"
Item_ID: a-quest-novel-overlay-heros-journey
title: "A Quest Novel — Hero's Journey Overlay"
lfw_manuscript: a-quest-novel
lfw_overlay_type: heros-journey
lfw_overlay_version: 2
Date_Added: 2026-05-12
Date_Modified: 2026-06-04
---

# A Quest Novel — Hero's Journey Overlay

## The twelve stages
| # | Stage | Question | Scene(s) | Notes |
|---|-------|----------|----------|-------|
| 1 | Ordinary World | Life before the call? | [[01-01-Village]] | Strong; the village's small-scale concerns are vivid |
| 2 | Call to Adventure | What disrupts? | [[01-02-The-Messenger]] | |
| 3 | Refusal | Why resist? | [[01-03-The-Argument-With-Mother]] | Refusal is felt; not just spoken |
| 4 | Mentor | Who aids? | [[02-01-The-Old-Map]] | **The mentor here is an object — the map, not a person. This is the manuscript's deliberate refusal of the mentor-figure cliché.** |
| 5 | Crossing the Threshold | What commits? | [[02-04-Departure]] | |
| ... | | | | |
| 12 | Return with the Elixir | What is brought back? | (planned: Chapter 12) | **The manuscript refuses this stage. The hero returns changed but does not bring an elixir; the question of what they "gained" is left open. This is a deliberate divergence — modern literary fantasy.** |

## Divergence notes
- Stage 4 (Mentor): the mentor is an object, not a person. The map carries the wisdom.
- Stage 12 (Return with the Elixir): refused. The hero returns; what they brought is ambiguous.

## Risks
- Stage 4 in lesser drafts could collapse into a wise-elder cliché. Hold the line.
- Stage 11 (Resurrection) is the place where a final-battle spectacle would crowd out the actual transformation. The manuscript's resurrection is a quiet conversation.
```

## Relationships

- `LFW_Spine` — Spine is the causal-claim backbone; the Hero's Journey lens reads it through the monomyth. Spine wins on conflicts.
- `LFW_Worldbuilding` — Hero's Journey often pairs with cartridges that have substantial worldbuilding (SFF, fantasy, alt-history). When `_worldbuilding.md` is present (v1.3.2), the overlay can cross-reference it.
- `LFW_Scene` — Stages reference Scene Items via wikilinks.
- `LFW_Manuscript_Manifest` — Active overlays declared in `lfw_active_overlays`.
- `LFW_Overlay_Story_Circle` — Sibling and structurally related (Story Circle is a tighter eight-step rendering of the same arc). A cartridge generally picks one or the other, not both.

## Notes

- **Best fit:** mythic, fantasy, quest, science fiction, coming-of-age. The monomyth's resonance is powerful when the manuscript is *being* mythic; it is hollow when applied as costume to a non-mythic story.
- **The most-clichéd stage is Mentor.** Modern fiction often does better with the mentor-as-fragment, mentor-as-object, mentor-as-memory than the wise-elder trope.
- **Two common failure modes:**
  - **Resurrection-as-final-battle-spectacle.** Stage 11 inflates into action that crowds out the actual transformation.
  - **Return-with-Elixir-as-tidy-ending.** Stage 12 over-resolves; modern literary fantasy often refuses this stage to honor the cost of the journey.
- **The journey may be metaphorical.** Coming-of-age cartridges with no literal travel still map onto the monomyth — Ordinary World is childhood; Call is the loss of innocence; Ordeal is the first adult test.
- **Reading lens.** If the manuscript doesn't fit, the manuscript is right and the overlay is wrong for it. Don't bend the spine to fit the lens.
