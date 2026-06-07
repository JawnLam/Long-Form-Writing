---
Item_Prototype: Fleeting
Item_ID: prototype-lfw-overlay-story-circle
Title: "LFW_Overlay_Story_Circle Prototype"
Date_Added: 2026-06-06
Date_Modified: 2026-06-06
Needs_Processing: false
---

# `LFW_Overlay_Story_Circle` — Prototype Definition

> **What this file is.** The canonical definition of the `LFW_Overlay_Story_Circle` Prototype for the Long-Form-Writing Operating Volume. Items in any cartridge that declare `Item_Prototype: LFW_Overlay_Story_Circle` conform to the contract described below.

## Purpose

A Story Circle Overlay is an opt-in **reading lens** that maps the manuscript's structure onto Dan Harmon's eight-beat distillation of Joseph Campbell — a tighter rendering of the Hero's Journey emphasizing the relational shape: You → Need → Go → Search → Find → Take → Return → Change. Best fit: literary fiction, character-driven stories, contemporary realism — any work where the *transformation* of the character is the story's spine and the journey is metaphorical more often than literal. Opt-in via `lfw_active_overlays: [story-circle]` in the Manifest. One overlay file per active overlay per cartridge. Introduced in v1.3.1 (chapter 14 §2). Like all overlays: a reading lens, not a prescription. If the spine doesn't fit, the overlay is the wrong lens.

## Required frontmatter

| Field | Type | Required? | Notes |
|-------|------|-----------|-------|
| `Item_Prototype` | string | yes | Must equal `LFW_Overlay_Story_Circle` |
| `Item_ID` | string | yes | Format: `<manuscript-slug>-overlay-story-circle` |
| `Title` | string | yes | Format: `"<Manuscript Title> — Story Circle Overlay"` |
| `Date_Added` | date | yes | When the overlay was added |
| `Date_Modified` | date | yes | When last changed |
| `lfw_manuscript` | string | yes | Manuscript slug |
| `lfw_overlay_type` | enum | yes | Must equal `story-circle` |
| `lfw_overlay_version` | integer | yes | Bumped on substantial restructuring |

## Body structure

```markdown
# <Manuscript Title> — Story Circle Overlay

## The eight beats
*The Story Circle goes around: a character is in a zone of comfort, wants something, enters an unfamiliar situation, adapts, gets what they wanted, pays a price, returns to the familiar, and is changed.*

| # | Beat | Question | Maps to scene(s) |
|---|------|----------|------------------|
| 1 | You — character in their zone of comfort | Who are they, before? | |
| 2 | Need — they want something | What activates them? | |
| 3 | Go — they cross a threshold | What's the unfamiliar situation? | |
| 4 | Search — they adapt | What do they try / face? | |
| 5 | Find — they get what they wanted | What do they obtain? | |
| 6 | Take — they pay the price | What's the cost? | |
| 7 | Return — they come back to where they started | What's the homecoming? | |
| 8 | Change — they have changed | What's different about them now? | |

## Shape-fit assessment
- **Beats with clear coverage:**
- **Beats with uncertain coverage:**
- **Beats with no coverage:**

## Divergence notes

## How to use this overlay

## Risks

## Cross-reference
```

## Naming

- **Filename:** `_overlay-story-circle.md` (fixed; one per cartridge with this overlay active)
- **Location:** cartridge root
- **Wikilink target:** `_overlay-story-circle`

## Example Item

```markdown
---
Item_Prototype: LFW_Overlay_Story_Circle
Item_ID: the-late-frost-overlay-story-circle
Title: "The Late Frost — Story Circle Overlay"
lfw_manuscript: the-late-frost
lfw_overlay_type: story-circle
lfw_overlay_version: 2
Date_Added: 2026-05-04
Date_Modified: 2026-06-04
---

# The Late Frost — Story Circle Overlay

## The eight beats

| # | Beat | Question | Maps to scene(s) |
|---|------|----------|------------------|
| 1 | You — character in zone of comfort | Who is Maya, before? | [[01-01-The-Approach]] — Maya in Boston-life mode, driving away from it |
| 2 | Need — wants something | What activates her? | [[01-04-Empty-House-Walkthrough]] — needs to settle the estate; secretly needs to settle with Sarah |
| 3 | Go — crosses a threshold | Unfamiliar situation? | [[01-05-The-Letter]] — Mother's letter changes the terms |
| 4 | Search — adapts | What does Maya try / face? | Chapters 2–3 — repeated attempts to talk to Sarah |
| 5 | Find — gets what she wanted | What does she obtain? | (planned: Ch 4 midpoint) — apparent reconciliation |
| 6 | Take — pays the price | What's the cost? | (planned: Ch 5) — the reconciliation collapses under the letter's revelation |
| 7 | Return — comes back | What's the homecoming? | (planned: Ch 6) — Maya at the vineyard but changed |
| 8 | Change — is changed | What's different? | (planned: Ch 6 ending) — Maya claims the right to decide |

## Shape-fit assessment
- **Beats with clear coverage:** 1, 2, 3
- **Beats with uncertain coverage:** 4 (Search is planned but may need more scenes)
- **Beats with no coverage:** 5–8 (still in outline)

## Divergence notes
- Beat 8 (Change) refuses tidy transformation. Maya is changed by the experience but does not bring back an articulable "elixir." This is a deliberate literary refusal of the change-as-revelation cliché.

## How to use this overlay
The Late Frost is character-driven literary fiction; the Story Circle's relational-shape emphasis is the right diagnostic. Cross-reference with `_spine.md` during OUTLINE; revisit at the 50% Midpoint to check Find/Take handoff.

## Risks
- The Story Circle is most useful when the journey is metaphorical (relational, internal). A literal-quest reading would push toward Hero's Journey instead.
- Beat 5 (Find) is the easy place for false-win flatness. The "what was wanted" should match Beat 2's surface need *and* expose the deeper need that wasn't articulable in Beat 2.
```

## Relationships

- `LFW_Spine` — Spine is the causal-claim backbone; the Story Circle lens reads it through the eight beats. Spine wins on conflicts.
- `LFW_Scene` — Beats reference Scene Items via wikilinks.
- `LFW_Manuscript_Manifest` — Active overlays declared in `lfw_active_overlays`.
- `LFW_Overlay_Heros_Journey` — Sibling: Story Circle is a tighter eight-step rendering of the same arc. A cartridge generally picks one or the other.

## Notes

- **Best fit:** literary fiction, character-driven stories, contemporary realism. The Story Circle is more forgiving than Save the Cat (less prescriptive) and more accessible than the full Hero's Journey twelve stages. It is the right starting overlay when the question is "what arc is this story making?" rather than "what beats does it need?"
- **The transformation is the spine.** The Story Circle reads stories where character change matters more than external action. Plot-heavy stories may fit better against Save the Cat.
- **Beat 8 (Change) is the place for refusal.** Literary fiction often refuses tidy transformation; the character is changed but not in articulable ways. Document this as deliberate divergence — it's information, not error.
- **Reading lens, not prescription.** Per chapter 14 §2: if the spine doesn't fit the circle, the spine is right and the circle is wrong for this story. Walk away from the overlay if it doesn't serve.
