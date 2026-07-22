---
type: Fleeting
Item_ID: "ACE6DFD9-952B-444D-A127-1553A3546366"
title: "FPEDs — Full Prose Exploratory Drafts (workspace)"
Date_Added: 2026-07-21
Date_Modified: 2026-07-21
Needs_Processing: false
---

# _fpeds/ — Full Prose Exploratory Drafts

**Workspace, not canon.** This underscore-prefixed folder sits outside the `Items/` atom system and is excluded-by-convention (like other `_`-prefixed dirs). Nothing here is a canonical LFW atom until it is *promoted*.

## What an FPED is

A **F**ull **P**rose **E**xploratory **D**raft: a passage written OUT in prose to feel out tone, voice, shape, or an argumentative move — *without* committing to the canonical Section atom system. "Full Prose" is load-bearing: an FPED is always written-out prose (crude to nearly-final), **never** a shorthand fragment. A fragment belongs in `_notes/` or, once kept and typed, an `Items/Notes/` atom. (In non-fiction an FPED is often a paragraph or passage testing how an argument *sounds* before it's committed to a Section.)

## File convention

`_fpeds/YYYY-MM-DD_short-descriptive-name.md` — instantiate from `_writing-engine/_templates/TEMPLATE-fped.md`. Each carries `type: fped` and a `status` of `working | parked | promoted | abandoned`.

## Lifecycle (the `status` field)

| status | meaning |
|---|---|
| `working` | active candidate, still iterating |
| `parked` | set aside, might revisit |
| `promoted` | graduated into a canonical Section atom; `promoted_to` links the destination; the FPED stays for provenance |
| `abandoned` | dead — but **kept indefinitely**. Never delete an FPED; a discarded draft may matter later. |

## Relationship to canon

FPEDs **reference** canonical atoms (threads, sources, argument, readers) via their `references:` frontmatter, but canonical atoms do **not** reference FPEDs until the FPED is promoted. On promotion the prose graduates into an `Items/Sections/` atom and `promoted_to` records the link.

## Triage flow

`_notes/` (dump anything; first triage) → `_fpeds/` (draft it out in prose to test it) → canonical Section atom (on promotion). See `_notes/README.md` and `_writing-engine/04-ITEMS-AND-STRUCTURE.md`.
