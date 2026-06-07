---
Item_Prototype: Fleeting
Item_ID: prototype-lfw-overlay-freytag
Title: "LFW_Overlay_Freytag Prototype"
Date_Added: 2026-06-06
Date_Modified: 2026-06-06
Needs_Processing: false
---

# `LFW_Overlay_Freytag` — Prototype Definition

> **What this file is.** The canonical definition of the `LFW_Overlay_Freytag` Prototype for the Long-Form-Writing Operating Volume. Items in any cartridge that declare `Item_Prototype: LFW_Overlay_Freytag` conform to the contract described below.

## Purpose

A Freytag Overlay is an opt-in **reading lens** that maps the manuscript's structure onto Gustav Freytag's five-act dramatic pyramid (1863): Exposition → Rising Action → Climax → Falling Action → Catastrophe/Dénouement. Best fit: classical tragedy, dramatic structure, literary fiction whose shape is broadly classical with a substantial post-climax movement. Opt-in via `lfw_active_overlays: [freytag]` in the Manifest. One overlay file per active overlay per cartridge. Introduced in v1.3.1 (chapter 14 §2 — beat-sheet overlays). Per the engine: overlays are "Layer 2.5" — they sit between genre-branch (Layer 2) and per-cartridge instance (Layer 3), and they are reading lenses, not prescriptions. If the spine doesn't fit, the overlay is the wrong lens for this manuscript.

## Required frontmatter

| Field | Type | Required? | Notes |
|-------|------|-----------|-------|
| `Item_Prototype` | string | yes | Must equal `LFW_Overlay_Freytag` |
| `Item_ID` | string | yes | Format: `<manuscript-slug>-overlay-freytag` |
| `Title` | string | yes | Format: `"<Manuscript Title> — Freytag's Pyramid Overlay"` |
| `Date_Added` | date | yes | When the overlay was added to the cartridge |
| `Date_Modified` | date | yes | When last changed |
| `lfw_manuscript` | string | yes | Manuscript slug |
| `lfw_overlay_type` | enum | yes | Must equal `freytag` |
| `lfw_overlay_version` | integer | yes | Bumped on substantial restructuring of the overlay's findings |

## Body structure

```markdown
# <Manuscript Title> — Freytag's Pyramid Overlay

## The five beats
| # | Beat | Question | Scene(s) | Notes |
|---|------|----------|----------|-------|
| 1 | Exposition | What is the world? | | |
| 2 | Rising Action | What complications escalate? | | |
| 3 | Climax | What's the turning point? | | |
| 4 | Falling Action | What unfolds from the commitment? | | |
| 5 | Catastrophe / Dénouement | Final state? | | |

## Shape-fit assessment
- **Beats with clear coverage:**
- **Beats with uncertain coverage:**
- **Beats with no coverage:**

## Divergence notes
*Where the manuscript deliberately departs from the pyramid.*

## Risks
*Common failure modes when applying this overlay.*

## How to use this overlay
*When to consult during OUTLINE / READ-THROUGH / REVISE.*

## Cross-reference
- Engine chapter 14 §2
- `_spine.md`
- Alternative overlays
```

## Naming

- **Filename:** `_overlay-freytag.md` (fixed; one per cartridge with this overlay active)
- **Location:** cartridge root
- **Wikilink target:** `_overlay-freytag`

## Example Item

See `Example-Project-The-Late-Frost/_overlay-freytag.md` (if present in the shipping example cartridges). The template at `_writing-engine/_templates/TEMPLATE-overlay-freytag.md` shows the full structure populated with prose.

```markdown
---
Item_Prototype: LFW_Overlay_Freytag
Item_ID: the-late-frost-overlay-freytag
Title: "The Late Frost — Freytag's Pyramid Overlay"
lfw_manuscript: the-late-frost
lfw_overlay_type: freytag
lfw_overlay_version: 1
Date_Added: 2026-05-22
Date_Modified: 2026-06-04
---

# The Late Frost — Freytag's Pyramid Overlay

## The five beats
| # | Beat | Question | Scene(s) | Notes |
|---|------|----------|----------|-------|
| 1 | Exposition | What is the world? | [[01-01-The-Approach]], [[01-04-Empty-House-Walkthrough]] | Strong; the vineyard's character is established |
| 2 | Rising Action | What complications escalate? | [[01-05-The-Letter]] through [[02-03-Hector-Intervenes]] | Six scenes; well-paced |
| 3 | Climax | What's the turning point? | [[02-02-The-Garage-Argument]] | Approximately 45% — Freytag-classical positioning |
| 4 | Falling Action | What unfolds from the commitment? | Chapters 3–5 (planned) | Underdeveloped in current outline; **needs more weight** |
| 5 | Dénouement | Final state? | Chapter 6 (planned) | One scene planned; may be too short |

## Shape-fit assessment
- **Beats with clear coverage:** 1, 2, 3
- **Beats with uncertain coverage:** 4 (Falling Action underweight)
- **Beats with no coverage:** none

## Divergence notes
This is literary not tragic; the "Catastrophe" beat is rendered as quiet acceptance, not catastrophic loss. That's the modern softening from Catastrophe to Dénouement — appropriate for the manuscript's mode.

## Risks
- Falling Action is the failure mode for this manuscript. The garage argument (Climax) commits the sisters to a direction; the subsequent chapters need to earn the dénouement by doing actual work — not just sliding to the ending.
```

## Relationships

- `LFW_Spine` — The Spine is the causal-claim backbone; the Freytag overlay reads the Spine's shape through the pyramid lens. If they conflict, the Spine wins (the overlay is a reading lens, not a structural authority).
- `LFW_Scene` — Overlay beats reference Scene Items via wikilinks; the assessment is grounded in actual drafted material.
- `LFW_Outline` — The Outline's structural shape is what the overlay assesses.
- `LFW_Manuscript_Manifest` — Active overlays are declared in `lfw_active_overlays`. Adding the overlay is opt-in.
- `LFW_Overlay_Save_The_Cat`, `LFW_Overlay_Heros_Journey`, `LFW_Overlay_Story_Circle` — Sibling overlays. A cartridge may have multiple active overlays simultaneously if each is doing different diagnostic work.

## Notes

- **Reading lens, not prescription.** Overlays diagnose; they don't dictate. If the manuscript's spine doesn't fit Freytag, the overlay is the wrong lens — not the spine that needs fixing. Per chapter 14 §2.
- **Best fit:** classical tragedy, dramatic literary fiction with a substantial post-climax movement. Modern fiction often places climax at 75% (Save the Cat's "All Is Lost") rather than 50% (Freytag's apex); for those, prefer `LFW_Overlay_Save_The_Cat`.
- **Climax-in-the-middle is the distinguishing mark.** If the manuscript's climax is near the end, Freytag is the wrong overlay; the falling action / dénouement that Freytag expects won't be there.
- **The most under-used beat is Falling Action.** Modern fiction tends to truncate it; literary fiction that uses Freytag is choosing to dwell in the aftermath of the commitment. Honor that choice when applying the overlay.
- **Catastrophe vs Dénouement.** Freytag's original term was "Catastrophe" — the tragic outcome. Modern usage softens to "Dénouement" for non-tragic outcomes. Both are valid; the *shape* is what Freytag captures.
