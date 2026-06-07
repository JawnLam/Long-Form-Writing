---
Item_Prototype: Fleeting
Item_ID: prototype-lfw-argument
Title: "LFW_Argument Prototype"
Date_Added: 2026-06-06
Date_Modified: 2026-06-06
Needs_Processing: false
---

# `LFW_Argument` — Prototype Definition

> **What this file is.** The canonical definition of the `LFW_Argument` Prototype for the Long-Form-Writing Operating Volume. Items in any cartridge that declare `Item_Prototype: LFW_Argument` conform to the contract described below.

## Purpose

An Argument is the book's logical structure — as distinct from its container structure (which lives in `_outline.md`). It captures the thesis, sub-claims, evidence map, defeaters, and honest unknowns. **Required backbone for non-fiction and dissertation cartridges.** It exists as a single per-cartridge file at `_argument.md`, not as a folder of Items. The ARGUMENT-AUDIT session (chapter 10-ARGUMENT) pressure-tests the structure documented here. Created at cartridge bootstrap for non-fiction/dissertation; never created for fiction/screenplay/play (which use `_spine.md` instead for their causal-not-logical backbone).

## Required frontmatter

| Field | Type | Required? | Notes |
|-------|------|-----------|-------|
| `Item_Prototype` | string | yes | Must equal `LFW_Argument` |
| `Item_ID` | string | yes | Format: `<manuscript-slug>-argument` |
| `Title` | string | yes | Format: `"<Manuscript Title> — Argument Backbone"` |
| `Date_Added` | date | yes | When the argument file was created |
| `Date_Modified` | date | yes | When last changed |
| `lfw_manuscript` | string | yes | Manuscript slug |
| `lfw_argument_version` | integer | yes | Bumped on significant argument revisions |

## Body structure

```markdown
# <Manuscript Title> — Argument Backbone

## Thesis
*The book's central claim as a single falsifiable sentence.*

**Thesis:**
**Falsification condition:**

## Sub-claims
*3–7 testable claims the thesis decomposes into.*

### Sub-claim 1
### Sub-claim 2
### Sub-claim 3

## Evidence map
*Per sub-claim: Sources, cases, and reasoning that support it.*

### Sub-claim 1 — evidence
- [[Source-slug]] — what specifically this source contributes

## Independence check
*Are the sub-claims genuinely independent? Populated during ARGUMENT-AUDIT.*

## Defeaters
*Per sub-claim: strongest counterargument; sources supporting the counterargument; writer's current response.*

### Sub-claim 1 — defeaters
**Strongest counterargument:**
**Sources that support the counterargument:**
**Writer's current response to this counterargument:**

## The honest unknown
*What the writer doesn't know. What the framework can't predict. Epistemic humility, made explicit.*

## Argument-vs-outline alignment
*Optional check: does the outline include sections the argument doesn't need, or vice versa? Populated during ARGUMENT-AUDIT.*

## How to use this file
```

## Naming

- **Filename:** `_argument.md` (fixed; one per cartridge)
- **Location:** cartridge root (alongside `_manuscript-manifest.md`, `_state.md`, `_outline.md`)
- **Wikilink target:** `_argument`

## Example Item

```markdown
---
Item_Prototype: LFW_Argument
Item_ID: persistence-question-argument
Title: "The Persistence Question — Argument Backbone"
Date_Added: 2026-05-15
Date_Modified: 2026-06-02
lfw_manuscript: persistence-question
lfw_argument_version: 3
---

# The Persistence Question — Argument Backbone

## Thesis

**Thesis:** Civilizations persist when their adaptive capacity is selected for by hostile-but-not-lethal environmental pressure operating on inheritable, written tradition; they collapse when one of the three conditions weakens.

**Falsification condition:** A civilization that demonstrably had all three conditions present and collapsed anyway — or a long-persisting civilization that lacked one or more — would invalidate the framework.

## Sub-claims

### Sub-claim 1
Pressure must be hostile enough to select against maladaptive tradition but not so lethal it eliminates the population before adaptation can occur.

### Sub-claim 2
Adaptation must be encoded in inheritable form (written tradition or institutional structure that survives generational turnover) for selection to compound across generations.

### Sub-claim 3
Selection operates on the unit of distributed-legitimacy structures, not individual leadership decisions.

## Evidence map

### Sub-claim 1 — evidence
- [[Tainter-Collapse-1988]] — Tainter's marginal-returns argument supplies the lethality-threshold model
- Roman frontier pressure analysis (Chapter 4)
- Comparative: Easter Island lethality crossed the threshold; the population could not adapt fast enough
```

## Relationships

- `LFW_Source` — Argument evidence cites Sources via wikilinks in the `Evidence map` section.
- `LFW_Thread` — In non-fiction, Threads are the running ideas; the Argument is the meta-structure that organizes them.
- `LFW_Reader` — Reader Items inform how the Argument is pitched; the Argument doesn't change but its presentation does per Reader.
- `LFW_Outline` — Argument-vs-outline alignment is a recurring check during ARGUMENT-AUDIT.
- `LFW_Manuscript_Manifest` — Required backbone declaration: `_argument.md` MUST exist in non-fiction/dissertation cartridges.

## Notes

- **One per cartridge.** Unlike Items in `Items/`, the Argument is a single file at cartridge root. It is not a folder full of independent Items.
- **Genre-required.** Non-fiction and dissertation cartridges fail validator check `lfw_argument` if this file is missing.
- **Versioned in-file.** `lfw_argument_version` bumps when the argument substantially restructures (not on every edit). Per `_writing-engine/_meta/SCHEMA-OF-SCHEMAS.md`, Layer 1 universals like Argument are stable; the version captures within-document evolution.
- **The Argument is the logic; the outline is the shape.** Treat as the canonical statement of what the book is arguing; the outline structures HOW to deliver it.
