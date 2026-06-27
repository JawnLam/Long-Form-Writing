---
type: Fleeting
timestamp: "2026-06-06T00:00:00Z"
Item_ID: type-lfw-inspiration
title: "LFW_Inspiration Type"
Date_Added: 2026-06-06
Date_Modified: 2026-06-06
Needs_Processing: false
---

# `LFW_Inspiration` — Type Definition

> **What this file is.** The canonical definition of the `LFW_Inspiration` Type for the Long-Form-Writing Operating Volume. Items in any cartridge that declare `type: LFW_Inspiration` conform to the contract described below.

## Purpose

An Inspiration is research-as-compost — a book, film, conversation, observation, image, or other input that feeds the manuscript without becoming a citation. Distinct from `LFW_Source` (which carries non-fiction citation discipline). Inspirations are how fiction absorbs influence without pretending to scholarship: the writer notes what struck them, what aspect of the manuscript it informs, and (eventually) where it has surfaced in drafted prose. Created at any time during a cartridge's life. Per chapter 15 §5 (v1.3.2). Genre scope: any cartridge — fiction especially, but non-fiction also benefits from a non-citational lane for influence.

## Required frontmatter

| Field | Type | Required? | Notes |
|-------|------|-----------|-------|
| `type` | string | yes | Must equal `LFW_Inspiration` |
| `Item_ID` | string | yes | Lowercase kebab slug |
| `Title` | string | yes | Inspiration title (book name, film, etc.) |
| `Date_Added` | date | yes | When the Inspiration was noted |
| `Date_Modified` | date | yes | When last changed |
| `Needs_Processing` | boolean | yes | Default `false` |
| `lfw_manuscript` | string | yes | Manuscript slug |
| `lfw_item_type` | enum | yes | Must equal `inspiration` |
| `lfw_status` | enum | yes | `noted` \| `absorbed` \| `folded-in` \| `retired` |
| `lfw_kind` | enum | yes | `book` \| `article` \| `film` \| `conversation` \| `observation` \| `image` \| `podcast` \| `other` |
| `lfw_for` | string | yes | What aspect this informs (setting / character / voice / theme / mood / rhythm / scene-change / sensory texture) |

## Body structure

```markdown
# <Inspiration title>

## What it is
*Brief description. Title, author/source if applicable. Link if online.*

## What it inspires in this manuscript
*Specifically. Mood for a setting? A character beat? A line of dialogue rhythm? Sensory texture?*

## How it's working in the prose (if folded-in)
*If status is `folded-in`, name the specific scenes where the inspiration has surfaced.*

## Where it surfaces
- Scene: [[Scene-filename]] — *what aspect of the inspiration is operative here*

## Status notes
- `noted` — encountered; intent to absorb later
- `absorbed` — read/watched/observed; effect is now diffuse
- `folded-in` — a specific element has surfaced in drafted prose
- `retired` — turned out not to be relevant; archived

## Notes
*Anything else. Quotes or excerpts (informally — these are not citations).*
```

## Naming

- **Filename pattern:** `<Author-Title-Year>.md` for books/articles; `<Title-Year>.md` for films; `<Short-Label>.md` for observations/conversations
- **Location:** `<Cartridge>/Items/Inspirations/`
- **Wikilink target:** the filename

## Example Item

```markdown
---
type: LFW_Inspiration
timestamp: "2026-06-04T00:00:00Z"
Item_ID: patchett-dutch-house-2019
title: "Patchett — The Dutch House (2019)"
lfw_manuscript: the-late-frost
lfw_item_type: inspiration
lfw_status: folded-in
lfw_kind: book
lfw_for: sibling-dynamics over decades; first-person retrospective texture
Date_Added: 2026-04-29
Date_Modified: 2026-06-04
Needs_Processing: false
---

# Patchett — The Dutch House (2019)

## What it is
Ann Patchett's novel about siblings (Maeve and Danny) revisiting the house they were raised in and the parental absence that shaped them. First-person from Danny.

## What it inspires in this manuscript
The cadence of looking-back interiority while also being present in the scene. Patchett's narrator narrates from a much-later vantage point but inhabits each scene. *The Late Frost* needs the same trick: Maya's first-person is in-the-moment but her interiority has a 38-year-old's perspective.

## How it's working in the prose (if folded-in)
The way Maya names the vineyard's specific botanical details before naming her feelings — that's a Patchett move, absorbed and reapplied to a different sensory register.

## Where it surfaces
- Scene: [[01-01-The-Approach]] — opening paragraph's looking-back-from-later cadence
- Scene: [[01-02-The-Driveway]] — the way the house is named before it's felt

## Notes
Re-read the first 30 pages before starting Act 2. The rhythm there is teaching me something I haven't yet absorbed.
```

## Relationships

- `LFW_Source` — Distinct concept. Sources carry citation discipline (especially for non-fiction); Inspirations are non-citational influence. A book can be both (cited as a Source for facts; absorbed as an Inspiration for prose rhythm) — separate Items.
- `LFW_Scene` — Once status is `folded-in`, Inspirations wikilink the Scenes where they've surfaced.
- `LFW_Style_Sheet` — When an Inspiration informs voice or lexicon, the Style Sheet may capture the operating result; the Inspiration itself stays the diffuse origin.
- `LFW_Manuscript_Manifest` — Every Inspiration declares its parent manuscript.

## Notes

- **Compost, not citation.** Inspirations don't appear in bibliographies. The fold-in is implicit. Fiction's debts to other fiction are infinite and unenumerable; this Type lets the writer track what they're deliberately drawing on without overclaiming.
- **`lfw_status` is load-bearing.** A `noted` inspiration is a future-self note. An `absorbed` inspiration has become part of the writer's diffuse register. A `folded-in` inspiration has a traceable scene-level effect. A `retired` inspiration is archive-only — keep it, don't delete; the journey from interesting to not-relevant is data.
- **Excluded from `.gitignore` by default** (in v1.3.2 default `.gitignore`) as operator-private. The writer may opt in to tracking if shipping the cartridge.
- **Cross-genre.** Non-fiction can benefit from Inspirations too — for prose rhythm, for argumentative posture, for tonal register that doesn't belong in the bibliography but matters to the writing.
