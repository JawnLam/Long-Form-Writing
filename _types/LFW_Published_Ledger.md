---
type: Fleeting
timestamp: "2026-07-22T00:00:00Z"
Item_ID: type-lfw-published-ledger
title: "LFW_Published_Ledger Type"
Date_Added: 2026-07-22
Date_Modified: 2026-07-22
Needs_Processing: false
---

# `LFW_Published_Ledger` — Type Definition

> **What this file is.** The canonical definition of the `LFW_Published_Ledger` Type for the Long-Form-Writing Operating Volume. Items that declare `type: LFW_Published_Ledger` conform to the contract described below. Registered in `Master_Schema.yaml` (v1.47.0) and co-owned with the LFW OV.

## Purpose

The Published Ledger is the **per-cartridge, append-only history** of pieces that graduated out of a rolling-workshop. When an `LFW_Piece` reaches `published` and moves onto the MultiVac shelf, its prose leaves the workshop — but a **row stays here** so the workshop keeps a complete record of what it produced and where each piece now lives. One ledger per rolling-workshop cartridge, at `_published-ledger.md`.

It **complements** the per-Piece `lfw_graduated_to_multivac` flag: the flag is the machine idempotency signal (so MultiVac's sweep never re-grabs a graduated piece); the ledger is the human-readable audit trail.

## Required frontmatter

| Field | Type | Required? | Notes |
|-------|------|-----------|-------|
| `type` | string | yes | Must equal `LFW_Published_Ledger` |
| `Item_ID` | string | yes | Format: `<workshop-slug>-published-ledger` |
| `title` | string | yes | Format: `"<Workshop Title> — Published Ledger"` |
| `Date_Added` | date | yes | When the ledger was created (cartridge bootstrap) |
| `Date_Modified` | date | yes | When last appended |
| `Needs_Processing` | boolean | yes | Default `false` |
| `lfw_manuscript` | string | yes | Slug of the parent rolling-workshop cartridge |
| `lfw_durability` | enum | yes | `append-only` \| `mutable`. This ledger is `append-only`. |

> **Schema-registry note.** As with all `lfw_` properties, `Master_Schema.yaml` registers the body in Title_Snake_Case (`lfw_Manuscript`, `lfw_Durability`); cartridge content and templates use the lowercase form (`lfw_manuscript`, `lfw_durability`).

## Body structure

The body is a single append-only table (one row per graduated piece):

```markdown
# <Workshop Title> — Published Ledger

> **Permanent record of pieces that graduated out.** When a piece publishes, it moves out of this OV onto the MultiVac shelf — but a row stays here so the workshop keeps a complete history of what it produced and where it lives. **Append-only.**

| Date published | Title | Canonical (resource) | Mirror (URL) | Moved to (vault path) | Notes |
|----------------|-------|----------------------|--------------|-----------------------|-------|
| *(none yet)* | | | | | |
```

## Naming

- **Filename:** `_published-ledger.md` (fixed; one per rolling-workshop cartridge)
- **Location:** cartridge root
- **Wikilink target:** `_published-ledger`

## Relationships

- `LFW_Piece` — Each row corresponds to a Piece that reached `published` and set `lfw_graduated_to_multivac: true`.
- MultiVac — The "Moved to" column records the destination path on the MultiVac shelf.

## Notes

- **Append-only.** Rows are only ever added — never edited or removed — so the workshop's output history stays intact even after pieces leave. This is declared in `lfw_durability: append-only`.
- **Complement, not duplicate.** The ledger and the per-Piece `lfw_graduated_to_multivac` flag serve different roles (audit trail vs idempotency); keeping both is intentional.
