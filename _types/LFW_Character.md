---
type: Fleeting
timestamp: "2026-06-06T00:00:00Z"
Item_ID: type-lfw-character
title: "LFW_Character Type"
Date_Added: 2026-06-06
Date_Modified: 2026-06-06
Needs_Processing: false
---

# `LFW_Character` — Type Definition

> **What this file is.** The canonical definition of the `LFW_Character` Type for the Long-Form-Writing Operating Volume. Items in any cartridge that declare `type: LFW_Character` conform to the contract described below.

## Purpose

A Character is a person — fictional or non-fictional, speaking or non-speaking, major or minor — who appears in the manuscript. The Character Item is the lightweight reference: role, background, voice, arc, scenes-present, and key relationships. It is created for every speaking character and every load-bearing non-speaking character (someone whose absence would damage the scene). Created at cartridge bootstrap (protagonists, antagonists, major-supporting) or at first appearance (others). For POV-bearing or trilogy-spanning characters, an extended companion `LFW_Character_Bible` is created as opt-in supplement (chapter 14 §3). Genre scope: fiction, screenplay, play. Not used in non-fiction or dissertation (which use Threads instead).

## Required frontmatter

| Field | Type | Required? | Notes |
|-------|------|-----------|-------|
| `type` | string | yes | Must equal `LFW_Character` |
| `Item_ID` | string | yes | Lowercase kebab slug |
| `Title` | string | yes | Character's full name |
| `Date_Added` | date | yes | When the Character was first noted |
| `Date_Modified` | date | yes | When last changed |
| `Needs_Processing` | boolean | yes | Default `false` |
| `lfw_manuscript` | string | yes | Manuscript slug |
| `lfw_item_type` | enum | yes | Must equal `character` |
| `lfw_role` | enum | yes | `protagonist` \| `antagonist` \| `major-supporting` \| `minor` \| `speaking` \| `non-speaking` |
| `lfw_first_appearance` | wikilink | optional | Scene where character first appears |
| `lfw_scenes_present` | list[wikilink] | optional | Scenes the character appears in; auto-populates from Scene Items |
| `lfw_status` | enum | yes | `developing` \| `established` \| `revised` \| `final` |
| `lfw_pov_voice_register` | object | required-for-POV | Sub-fields: `sentence_length`, `diction`, `interiority_mode`, `tense_preference`, `signature_moves` (list), `avoid_moves` (list). Required when this character is a POV; optional otherwise. (v1.3.1) |
| `lfw_character_bible` | wikilink | optional | Soft pointer to the `LFW_Character_Bible` companion if one exists (v1.3.1) |

## Body structure

```markdown
# <Character Full Name>

## Role
*Function in the story.*

## Background
*Relevant history before the story begins.*

## Voice and Manner
*Speech patterns. Defining gestures. What they sound like.*

### Dialogue tells *(v1.3.1)*
- **Sentence shape:**
- **Diction range:**
- **Pet phrases:**
- **Verbal tics:**
- **What they say when they don't know what to say:**
- **What they say when they're lying:**
- **What they say under pressure:**

## Subtext patterns *(v1.3.1, optional)*

## Arc
*How this character changes (or doesn't) across the book.*

## Relationships
*Wikilinks to other characters with relationship type and trajectory.*

## Scenes Present
*Wikilinks to scenes they appear in. Auto-populates from Scene Items.*

## Open Questions
*Things about the character not yet decided.*
```

## Naming

- **Filename pattern:** `<Character-Name>.md` (Title-Case, hyphenated; e.g., `Maya-Hollis.md`, `Greg-Faber.md`)
- **Location:** `<Cartridge>/Items/Characters/`
- **Wikilink target:** the filename (e.g., `[[Maya-Hollis]]`)

## Example Item

```markdown
---
type: LFW_Character
Item_ID: maya-hollis
title: "Maya Hollis"
lfw_manuscript: the-late-frost
lfw_item_type: character
lfw_role: protagonist
lfw_first_appearance: "[[01-01-The-Approach]]"
lfw_scenes_present:
  - "[[01-01-The-Approach]]"
  - "[[01-02-The-Driveway]]"
  - "[[01-03-Empty-House-Walkthrough]]"
lfw_status: established
lfw_pov_voice_register:
  sentence_length: cadenced
  diction: plain-with-precise-nouns
  interiority_mode: observational
  tense_preference: scene-tense
  signature_moves:
    - "naming the room before naming the feeling"
    - "specific brand or model names as anchor for memory"
  avoid_moves:
    - "abstract emotional adjectives"
    - "italicized internal monologue"
lfw_character_bible: "[[Maya-Hollis-Bible]]"
Date_Added: 2026-04-15
Date_Modified: 2026-06-04
Needs_Processing: false
---

# Maya Hollis

## Role
First-person POV protagonist. Returns to the family vineyard after twenty years away to settle her mother's estate.

## Background
Departed at 18 after the rift with her sister Sarah. Now 38, working as a literary editor in Boston. Last visit was eight years ago for her father's funeral.

## Voice and Manner
Precise, observational, slightly dry. Names things accurately before naming what she feels about them.

### Dialogue tells
- **Sentence shape:** cadenced, with internal pauses on commas
- **Diction range:** plain with occasional botanical or oenological precision
- **Pet phrases:** "right" (as acknowledgment), "I suppose"
- **What they say when they don't know what to say:** asks back a clarifying question
- **What they say when they're lying:** over-precise dates

## Arc
External: settles the estate. Internal: rebuilds the relationship with Sarah. By Act 3, claims agency over what the property becomes — she does NOT want to inherit a museum.
```

## Relationships

- `LFW_Character_Bible` — Opt-in extended companion for POV-bearing, antagonist, and major-supporting characters. Linked via `lfw_character_bible`.
- `LFW_Scene` — Characters are referenced in Scene Items' `lfw_characters_present` lists; reciprocally tracked in this Character's `lfw_scenes_present`.
- `LFW_Beat` — Beats may carry character-specific subtext (v1.3.1 Beat extension).
- `LFW_Relationships` — When present (v1.3.2), `_relationships.md` provides a symmetric multi-character map.
- `LFW_Manuscript_Manifest` — Every Character declares its parent manuscript via `lfw_manuscript`.

## Notes

- **POV characters need the voice-register block.** Per v1.3.1, characters with `lfw_role: protagonist` (POV-bearing) or any POV-bearing role MUST populate `lfw_pov_voice_register`. The validator's check 11 flags missing voice-register on established protagonists/antagonists as advisory.
- **`Character` vs `Character_Bible`.** Character is the lightweight always-present reference. Character_Bible is the opt-in extended companion (chapter 14 §3) for POV-bearing, antagonist, and major-supporting characters where the additional depth pays off. Soft pointer (`lfw_character_bible`) links the two; either can exist alone.
- **`lfw_scenes_present` auto-populates.** Edit Scene Items' `lfw_characters_present`; the Character's `lfw_scenes_present` is derived. Per chapter 04's bidirectional-reference convention.
