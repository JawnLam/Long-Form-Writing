---
type: Fleeting
Item_ID: "EE22E80C-D0AF-4F45-B2BD-0251ACC1B60C"
title: "_notes — Raw Ingestion Tank (workspace)"
Date_Added: 2026-07-21
Date_Modified: 2026-07-21
Needs_Processing: false
---

# _notes/ — Raw Ingestion Tank

**Workspace, not canon.** This underscore-prefixed folder sits outside the `Items/` atom system and is excluded-by-convention (like other `_`-prefixed dirs). It is pre-canonical and pre-typed.

## What this is

A zero-friction brain-dump inbox — the **first-ever triage point for ANY idea**. Dump anything here: full prose, scraps, clippings, links, half-sentences. This is where things go **before you know what they are**.

- Running capture file: `_inbox.md` (append freely).
- Anything that grows its own life: a freeform `_notes/<name>.md`.
- Workspace docs use `type: Fleeting` (a non-`LFW_` type) so they are **not** subjected to canonical-atom validation.

## What this is NOT

- **Not** `Items/Notes/` — those are the typed, *kept* `LFW_Note` atoms that ideas graduate INTO once they've earned a place.
- **Not** `_fpeds/` — that workspace is specifically *full prose* exploratory drafts. A half-sentence or a link is a `_notes/` item, not an FPED.

## Triage flow

```
_notes/            (dump anything; first triage)
  -> Items/Notes/  (typed, kept LFW_Note atom)          and/or
  -> _fpeds/       (draft it out in prose to test it)
  -> canonical Section atom   (on promotion)
```

Nothing in `_notes/` is obligated to graduate — it's a tank; most of it evaporates. See `_writing-engine/04-ITEMS-AND-STRUCTURE.md`.
