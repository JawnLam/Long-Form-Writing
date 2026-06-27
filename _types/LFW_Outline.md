---
type: Fleeting
timestamp: "2026-06-06T00:00:00Z"
Item_ID: type-lfw-outline
title: "LFW_Outline Type"
Date_Added: 2026-06-06
Date_Modified: 2026-06-06
Needs_Processing: false
---

# `LFW_Outline` — Type Definition

> **What this file is.** The canonical definition of the `LFW_Outline` Type for the Long-Form-Writing Operating Volume. Items in any cartridge that declare `type: LFW_Outline` conform to the contract described below.

## Purpose

The Outline is the manuscript's structural plan — Parts, Chapters/Sections, and their dramatic or argumentative composition. **Required backbone in every cartridge.** Updated through OUTLINE sessions (chapter 03 cadence). The Outline answers *what shape the work takes*; the Argument (non-fiction) or Spine (fiction) answers *what claim or causal chain it makes*. The two are distinct and should be checked against each other periodically (argument-vs-outline alignment). The Outline is versioned: substantive structural shifts increment `lfw_outline_version`.

## Required frontmatter

| Field | Type | Required? | Notes |
|-------|------|-----------|-------|
| `type` | string | yes | Must equal `LFW_Outline` |
| `Item_ID` | string | yes | Format: `<manuscript-slug>-outline` |
| `Title` | string | yes | Format: `"<Manuscript Title> — Outline"` |
| `Date_Added` | date | yes | When the outline was created |
| `Date_Modified` | date | yes | When last changed |
| `Needs_Processing` | boolean | yes | Default `false` |
| `lfw_manuscript` | string | yes | Manuscript slug |
| `lfw_outline_scope` | enum | yes | `book-level` \| `chapter-level` \| `section-level` \| `beat-level` \| `all` |
| `lfw_outline_version` | integer | yes | Bumped on substantial structural shifts |

## Body structure

```markdown
# <Manuscript Title> — Outline

## Book-level shape
*What's the macro-structure? Three-act? Five-act? Argumentative spine? Chronological? Thematic?*

## Parts
*If the book has Parts. Otherwise skip.*

### Part 1: <Part Title>
*What this part does.*

## Chapters
### Chapter 1: <Chapter Title>
- **Purpose:** *What this chapter does in the book*
- **Scope:** *What's in / what's out*
- **Sections (non-fiction) or Scenes (fiction):**
  1. *(planned)*
- **Threads engaged (non-fiction) or Characters present (fiction):**
- **Open notes:**

## Structural decisions logged
*Major structural choices and rationale, in dated entries.*

### <YYYY-MM-DD>
*The choice. The alternatives considered. The rationale.*

## Open structural questions
- [ ]
```

## Naming

- **Filename:** `_outline.md` (fixed; one per cartridge)
- **Location:** cartridge root
- **Wikilink target:** `_outline`

## Example Item

```markdown
---
type: LFW_Outline
timestamp: "2026-06-04T00:00:00Z"
Item_ID: the-late-frost-outline
title: "The Late Frost — Outline"
Date_Added: 2026-04-15
Date_Modified: 2026-06-04
Needs_Processing: false
lfw_manuscript: the-late-frost
lfw_outline_scope: chapter-level
lfw_outline_version: 4
---

# The Late Frost — Outline

## Book-level shape
Three acts. Story Circle overlay active for the Maya arc (return → adapt → confrontation → return-with-elixir). Maya's POV is the through-line; Sarah's interiority is glimpsed only through dialogue and behavior.

## Chapters

### Chapter 1: Maya Arrives
- **Purpose:** Establish Maya's voice, the world of the vineyard at story-open, the cracks in the status quo (the unspoken letter from Mother)
- **Scope:** In: Maya's arrival, walkthrough of the empty house, the letter. Out: Sarah does not appear.
- **Scenes:**
  1. [[01-01-The-Approach]] — Maya driving up Highway 12
  2. [[01-02-Frost-Damage-Neighbor]] — Neighbor explains the frost damage
  3. [[01-03-The-Driveway]] — Maya at the gate; first look at the house
  4. [[01-04-Empty-House-Walkthrough]] — Inside; furniture covered; the rift memory
  5. [[01-05-The-Letter]] — Maya finds Mother's letter
- **Characters present:** Maya, Hector (neighbor)
- **Open notes:** Voice register is set in 01-01; if it drifts in 01-04's interiority, REVISE.

### Chapter 2: Sarah Knows
- **Purpose:** Sarah arrives; the rift becomes scene-present rather than memory; the letter is discovered.
- **Scope:** In: Sarah's arrival, the garage argument, the letter's discovery. Out: resolution.

## Structural decisions logged

### 2026-04-20
**Choice:** Open with Maya in motion (driving), not arrived. Alternatives: open at the empty house, open in flashback. Rationale: arrival energy gives the chapter its first beat; the empty house is more powerful when Maya enters it after the drive establishes her.

### 2026-05-18
**Choice:** Sarah does not appear in Chapter 1. Alternatives: introduce Sarah by chapter-end via phone call. Rationale: Sarah's absence is the texture of Chapter 1; introducing her diffuses what the chapter is doing.

## Open structural questions
- [ ] Is Act 2 too short at 25,000 words? Re-evaluate after first draft of Ch 4.
```

## Relationships

- `LFW_Manuscript_Manifest` — The Outline is one of three required backbones (alongside Manifest and State). Every cartridge has one.
- `LFW_Argument` — For non-fiction/dissertation: argument-vs-outline alignment is a recurring check.
- `LFW_Spine` — For fiction: the Outline structures the *shape*; the Spine structures the *causal chain*. Both exist; they answer different questions.
- `LFW_Chapter` — Outline Chapter sections reference `LFW_Chapter` Items as they are drafted; until then, chapters are planned within the Outline.
- `LFW_Scene` / `LFW_Section` — Outline planned-scenes/sections become Item files once drafted; the Outline maintains the higher-level view.
- `LFW_State` — The State references the Outline's current scope (which chapter is in production) but doesn't duplicate the Outline.

## Notes

- **One per cartridge, required.** Validator fails any cartridge missing `_outline.md`.
- **Version with intent.** `lfw_outline_version` bumps when the macro-structure shifts (a Chapter moves between Parts, the genre's overlay re-classifies, a thematic restructure). Not every edit — only structural moves.
- **`lfw_outline_scope`** declares how deep the outline goes. A `book-level` outline lists Parts and Chapter purposes; a `chapter-level` outline adds per-chapter scenes/sections; `section-level` and `beat-level` go further. Most cartridges live at `chapter-level` for most of their life.
- **Structural decisions log is append-only.** Don't rewrite history when a structural decision is reversed; add a new dated entry that documents the reversal and the reasoning.
- **Outline ≠ Synopsis.** The Outline is operational (what's drafted, what's planned, what's open). A pitch document or query synopsis lives elsewhere (a `_synopsis.md` Note, perhaps).
