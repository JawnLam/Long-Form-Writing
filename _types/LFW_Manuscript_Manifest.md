---
type: Fleeting
timestamp: "2026-06-06T00:00:00Z"
Item_ID: type-lfw-manuscript-manifest
title: "LFW_Manuscript_Manifest Type"
Date_Added: 2026-06-06
Date_Modified: 2026-06-06
Needs_Processing: false
---

# `LFW_Manuscript_Manifest` — Type Definition

> **What this file is.** The canonical definition of the `LFW_Manuscript_Manifest` Type for the Long-Form-Writing Operating Volume. Items in any cartridge that declare `type: LFW_Manuscript_Manifest` conform to the contract described below.

## Purpose

The Manuscript Manifest is the **identity card of a cartridge** — the single per-cartridge file at `_manuscript-manifest.md` that declares what the manuscript is, who it is for, what genre, what voice mode, what active overlays and craft modules apply. It is the first file every AI session reads in any cartridge; without it a fresh session cannot know the genre branch, the writer's communication preferences, the bootstrap context, or which conditional backbones are expected. **Required backbone file in every cartridge.** Created at cartridge bootstrap; updated when the manuscript's identity shifts (genre re-classified, voice mode changed, overlay added). Per `_writing-engine/_meta/SCHEMA-OF-SCHEMAS.md` § Layer 1.

## Required frontmatter

| Field | Type | Required? | Notes |
|-------|------|-----------|-------|
| `type` | string | yes | Must equal `LFW_Manuscript_Manifest` |
| `Item_ID` | string | yes | Format: `<manuscript-slug>-manifest` |
| `Title` | string | yes | Format: `"<Manuscript Title> — Manuscript Manifest"` |
| `Date_Added` | date | yes | When the cartridge was bootstrapped |
| `Date_Modified` | date | yes | When last changed |
| `Needs_Processing` | boolean | yes | Default `false` |
| `lfw_manuscript_title` | string | yes | Working title |
| `lfw_manuscript_slug` | string | yes | Cartridge slug |
| `lfw_genre` | enum | yes | `fiction` \| `non-fiction` \| `screenplay` \| `play` \| `dissertation` |
| `lfw_fiction_subgenre` | enum | optional-fiction | `literary` \| `thriller` \| `mystery` \| `romance` \| `sff` \| `speculative` \| `historical` \| `horror` \| `ya` (v1.3.1; fiction only) |
| `lfw_target_length` | string | yes | e.g., `"75,000 words"` or `"110 pages"` |
| `lfw_voice_mode` | enum | yes | `writer-maintains` \| `voice-samples` \| `voice-check-on-demand` |
| `lfw_citation_style` | string | optional | `chicago-notes-bibliography` \| `chicago-author-date` \| `mla` \| `apa` \| `harvard` \| `custom` \| blank for fiction |
| `lfw_writer_name` | string | yes | Operator-confirmed; never inferred (see P7 / F3) |
| `lfw_bootstrapped` | date | yes | Cartridge bootstrap date |
| `lfw_custom_items` | list[string] | optional | Operator-defined custom Type names beyond the universal Layer 1 set |
| `lfw_active_overlays` | list[enum] | optional | Subset of: `story-circle`, `save-the-cat`, `heros-journey`, `freytag` (v1.3.1) |
| `lfw_active_craft_modules` | list[enum] | optional | Subset of: `show-dont-tell`, `dialogue-and-subtext`, `pov-and-psychic-distance`, `concrete-to-abstract`, `signposting`, `given-new`, `curse-of-knowledge` (v1.3.1) |
| `lfw_show_dont_tell_calibration` | object | optional | Sub-fields: `standing_position` (enum), `load_bearing_moments_only` (boolean). Only if show-dont-tell module is active (v1.3.1) |

## Body structure

```markdown
# <Manuscript Title> — Manuscript Manifest

## What this manuscript is
*One or two paragraphs. The shape of the project.*

## Premise / Thesis / Logline
*One sentence.*

## Why this manuscript, why now
*The motivating need.*

## Intended audience
*Specific.*

## Comparable works
*Two or three works that share genre, audience, or shape.*

## Current state at bootstrap
*Has the writer started? Outlined? Drafted? Prior abandoned attempts?*

## Voice notes
*If voice mode is writer-maintains: probably nothing here.*
*If voice-samples or voice-check-on-demand: any per-cartridge voice guidance.*

## Cadence
*Expected working pattern.*

## Scope boundaries
*Anything explicitly out of scope.*

## Sensitivities or red lines
*Anything the AI should know to handle carefully.*

## Communication preferences
Defaults (override if needed):
- **Register:** peer
- **Critique style:** substantive
- **Hedging:** minimal
- **Filler tolerance:** none

## Genre-specific notes
*Per-genre considerations.*

## Notes for any AI session
*Anything else a fresh AI session should know.*
```

## Naming

- **Filename:** `_manuscript-manifest.md` (fixed; one per cartridge)
- **Location:** cartridge root
- **Wikilink target:** `_manuscript-manifest`

## Example Item

```markdown
---
type: LFW_Manuscript_Manifest
timestamp: "2026-06-04T00:00:00Z"
Item_ID: the-late-frost-manifest
title: "The Late Frost — Manuscript Manifest"
Date_Added: 2026-04-15
Date_Modified: 2026-06-04
Needs_Processing: false
lfw_manuscript_title: "The Late Frost"
lfw_manuscript_slug: the-late-frost
lfw_genre: fiction
lfw_fiction_subgenre: literary
lfw_target_length: "85,000 words"
lfw_voice_mode: writer-maintains
lfw_citation_style: ""
lfw_writer_name: "[OPERATOR-CONFIRMED]"
lfw_bootstrapped: 2026-04-15
lfw_custom_items: []
lfw_active_overlays:
  - story-circle
lfw_active_craft_modules:
  - dialogue-and-subtext
  - pov-and-psychic-distance
lfw_show_dont_tell_calibration:
  standing_position: balanced
  load_bearing_moments_only: true
---

# The Late Frost — Manuscript Manifest

## What this manuscript is
A literary novel about two estranged sisters returning to settle their mother's vineyard estate. First-person, present-tense, ~85k words.

## Premise / Logline
Maya returns to the family vineyard after twenty years to settle their mother's estate; the rift with her sister Sarah is the actual problem and the estate is the surface.

## Why this manuscript, why now
The writer has been carrying this story for three years; the mother-character is now stable enough to be one-step-removed (the writer's own mother passed in 2024).

## Intended audience
Readers who read Patchett, Strout, Robinson. Literary fiction that respects readers.

## Comparable works
- Ann Patchett, *The Dutch House* (2019)
- Marilynne Robinson, *Gilead* (2004)

## Current state at bootstrap
~5,000 words of opening exists from an attempt in 2024. Outline is partial.

## Voice notes
Voice mode is `writer-maintains`. No voice-samples needed.

## Cadence
3 sessions/week. 60–90 minutes each. Target: first draft by Sept 2026.

## Scope boundaries
The mother is dead at story-open and never appears alive in scenes. Past is interiority only.

## Sensitivities or red lines
The grief texture must not become sentimental. If a scene-end is reaching, flag it.

## Communication preferences
Defaults.

## Genre-specific notes
- POV: first-person from Maya, single
- Tense: present
- Narrative distance: close

## Notes for any AI session
- Story Circle overlay is active; reference for OUTLINE check-ins.
- Show-don't-tell calibration is `balanced`, load-bearing only — do not flag every telling moment.
```

## Relationships

- `LFW_State` — Together with `_state.md`, the Manifest forms the cartridge backbone identity. The Manifest is who the cartridge *is*; the State is where the cartridge *is now*.
- `LFW_Outline` — The Manifest declares premise; the Outline structures it.
- `LFW_Argument` — Required backbone for non-fiction/dissertation; declared by `lfw_genre`.
- `LFW_Spine` — Required backbone for fiction/screenplay/play; declared by `lfw_genre`.
- `LFW_Reader` — Reader Items are calibrated against the Manifest's `Intended audience`.
- `LFW_Overlay_*` — Active overlays are declared in `lfw_active_overlays`; each active overlay has a corresponding `_overlay-<name>.md` Item.

## Notes

- **One per cartridge, required.** Validator fails any cartridge missing `_manuscript-manifest.md`.
- **`lfw_writer_name` must be operator-confirmed.** Per LFW's identity-from-indirect-signals rule (F3 in `_meta/FAILURE-MODES.md`), the writer name is never inferred from git config, username, or path. Use `[OPERATOR-CONFIRMED]` placeholder until the writer provides their name. (The vault-wide CLAUDE.md feedback memory `feedback_no_identity_fabrication` reinforces this.)
- **Genre determines conditional backbone.** Non-fiction/dissertation triggers required `_argument.md`. Fiction/screenplay/play triggers required `_spine.md` and `_promises.md`. Fiction with worldbuilding or plot secrets triggers required `_continuity.md`. The validator enforces these based on the declared genre.
- **`lfw_custom_items`** (formerly `lfw_custom_items`) lets a cartridge declare extra OV-specific Type names beyond the universal set. Use sparingly; the universals are usually sufficient.
- **The Manifest is read first at every session.** Treat it as the cartridge's bootstrap pointer; update it when the manuscript's identity (not its content) shifts.
