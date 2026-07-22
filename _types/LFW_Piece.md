---
type: Fleeting
timestamp: "2026-07-22T00:00:00Z"
Item_ID: type-lfw-piece
title: "LFW_Piece Type"
Date_Added: 2026-07-22
Date_Modified: 2026-07-22
Needs_Processing: false
---

# `LFW_Piece` — Type Definition

> **What this file is.** The canonical definition of the `LFW_Piece` Type for the Long-Form-Writing Operating Volume. Items that declare `type: LFW_Piece` conform to the contract described below. Registered in `Master_Schema.yaml` (v1.47.0) and co-owned with the LFW OV.

## Purpose

A **Piece** is the front document (`_piece.md`) of a **piece-folder** in a Long-Form-Writing *rolling-workshop* cartridge (e.g. "Public Square One"). A piece-folder is a self-contained short-form work — an essay or commentary — that lives in its own folder alongside an Obsidian Canvas of supporting material (`_wall.canvas`). The Piece is the identity-and-status card of that folder: its `lfw_piece_status` represents the state of the **entire** project folder, not just the prose file.

This is a different granularity from `LFW_Manuscript_Manifest` (the front doc of a whole *book* cartridge) and from `LFW_Section` (a unit *inside* one manuscript). A rolling workshop produces many short pieces over time; each is its own folder with its own Piece front-doc.

## Required frontmatter

| Field | Type | Required? | Notes |
|-------|------|-----------|-------|
| `type` | string | yes | Must equal `LFW_Piece` |
| `Item_ID` | string | yes | Format: `<piece-slug>-piece` |
| `title` | string | yes | The piece's working/published title |
| `Date_Added` | date | yes | When the piece-folder was created |
| `Date_Modified` | date | yes | When last changed |
| `Needs_Processing` | boolean | yes | Default `false` |
| `lfw_manuscript` | string | yes | Slug of the parent rolling-workshop cartridge |
| `lfw_piece_status` | enum | **yes** | `germinating` \| `drafting` \| `revising` \| `ready` \| `published` \| `archived`. State of the entire folder. `published` is the signal MultiVac's intake sweep watches for; `archived` closes the folder out. |
| `lfw_graduated_to_multivac` | boolean | optional | Idempotency flag MultiVac sets `true` once it graduates the piece onto the shelf. Absent/`false` are equivalent. |
| `Publication_Date` | date | on-publication | Universal-core field. The date the piece published. (No piece-specific date property — reuse the core.) |
| `resource` | string (uri) | on-publication | Universal-core field. The **canonical** publication URL (e.g. the Substack post) — the work's canonical web home. |
| `URL` | string (url) | optional | Universal-core field. A **mirror** publication URL (e.g. the Medium cross-post), if any. |

> **Schema-registry note.** In `Master_Schema.yaml` the `lfw_` property bodies are registered in Title_Snake_Case (`lfw_Piece_Status`, `lfw_Graduated_To_MultiVac`) per the vault's Case Rule 4; LFW cartridge **content and templates** use the lowercase form (`lfw_piece_status`, `lfw_graduated_to_multivac`), exactly as every other `lfw_` property already does across the two layers. The enum identifier `lfw_piece_statuses` is lowercase in both.

## Companion: `_wall.canvas` (convention, not a type)

Each piece-folder carries an Obsidian Canvas `_wall.canvas` — the "wall" of supporting material (quotes, sources, fragments, structure). A `.canvas` file is JSON with **no YAML frontmatter**, so it is a documented folder convention, **not** a schema type. Do not create a type for it.

## Body structure

```markdown
# <Piece Title>

## What this piece is
*One or two sentences. The claim or the angle.*

## Status notes
*Where the whole folder stands; what's next.*

## The draft
*The prose, or a link to where it lives in the folder.*

## Publication
*Once published: canonical + mirror links, date. Mirrors Publication_Date / resource / URL.*
```

## Naming

- **Filename:** `_piece.md` (fixed; one per piece-folder)
- **Location:** the piece-folder root, inside the rolling-workshop cartridge
- **Wikilink target:** `_piece`

## Example Item

```markdown
---
type: LFW_Piece
timestamp: "2026-07-22T00:00:00Z"
Item_ID: the-chucky-allegory-piece
title: "The Chucky Allegory"
Date_Added: 2026-07-22
Date_Modified: 2026-07-22
Needs_Processing: false
lfw_manuscript: public-square-one
lfw_piece_status: drafting
lfw_graduated_to_multivac: false
---

# The Chucky Allegory

## What this piece is
A short commentary using the Chucky franchise as an allegory for stochastic violence in public rhetoric.

## Status notes
Draft in progress; the wall (`_wall.canvas`) holds the source quotes and the rebuttal structure.
```

## Relationships

- `LFW_Published_Ledger` — When a Piece reaches `published` and graduates to MultiVac, a row is appended to the cartridge's `_published-ledger.md`; the per-Piece `lfw_graduated_to_multivac` flag is the machine idempotency signal, the ledger is the human-readable history.
- `LFW_Manuscript_Manifest` — A rolling-workshop cartridge still carries a manifest (the workshop's identity); the Piece is a per-work front-doc *within* it, a finer granularity than a whole-book manuscript.
- MultiVac — On publication the piece graduates DT42 → MultiVac (the vault's published-source shelf); the MultiVac source note carries the same canonical URL in its `resource`.

## Notes

- **Status is folder-scoped.** `lfw_piece_status` describes the whole piece-folder, not just the prose file.
- **Publication metadata reuses the universal core.** Date → `Publication_Date`; canonical URL → `resource`; mirror URL → `URL`. There are deliberately no `lfw_published_date` / platform-specific URL properties (v1.47.0 rejected those as redundant with the core).
- **`archived` keeps the folder.** An archived piece-folder is closed-out but not deleted.
