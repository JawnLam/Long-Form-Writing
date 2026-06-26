---
type: LFW_Argument
Item_ID: "<manuscript-slug>-argument"
title: "<Manuscript Title> — Argument Backbone"
Date_Added:
Date_Modified:
lfw_manuscript: "<manuscript-slug>"
lfw_argument_version: 1
---

# <Manuscript Title> — Argument Backbone

> **The book's logical structure as distinct from its container structure (which lives in `_outline.md`). Required for non-fiction and dissertation cartridges. The artifact ARGUMENT-AUDIT sessions pressure-test.**

## Thesis

*The book's central claim, stated as a single falsifiable sentence. Not "this book is about X" — the actual claim the writer is willing to defend.*

**Thesis:**

**Falsification condition** *(what evidence or argument would force the writer to retract):*

## Sub-claims

*The 3–7 claims the thesis decomposes into. Each is a sentence the writer is willing to defend. Each should be testable: a reader could agree with the thesis but disagree with a specific sub-claim.*

### Sub-claim 1

*One-sentence claim.*

### Sub-claim 2

*One-sentence claim.*

### Sub-claim 3

*One-sentence claim.*

*(Add more as needed; aim for 3–7 total.)*

## Evidence map

*For each sub-claim, the Sources, cases, and reasoning that support it. Cross-references to Source Items.*

### Sub-claim 1 — evidence

- [[Source-slug]] — what specifically this source contributes
- *(reasoning or case-based support)*

### Sub-claim 2 — evidence

- [[Source-slug]] — ...

*(Continue for each sub-claim.)*

## Independence check

*Are the sub-claims genuinely independent, or do some collapse into others? Where the answer is "they collapse," the writer either consolidates or makes the distinction sharper. This section is updated during ARGUMENT-AUDIT.*

- *(empty at start; populated during first ARGUMENT-AUDIT)*

## Defeaters

*For each sub-claim, what would change the writer's mind. The strongest version of the counterargument. This is where STEELMAN findings live.*

### Sub-claim 1 — defeaters

**Strongest counterargument:**

**Sources that support the counterargument:**

- [[Source-slug]] — if any

**Writer's current response to this counterargument:**

### Sub-claim 2 — defeaters

*(Continue for each sub-claim.)*

## The honest unknown

*What the writer doesn't know. What the framework can't predict. What's still genuinely contested in the field. The book's epistemic humility, made explicit.*

- *(empty at start)*

## Argument-vs-outline alignment

*Optional but useful. Periodically check: does the outline (in `_outline.md`) include sections that the argument doesn't need? Does the argument include sub-claims the outline doesn't address? Where the answer is yes, the writer either revises the outline to align or revises the argument to expand.*

- *(empty at start; populated during ARGUMENT-AUDIT)*

## How to use this file

For the AI:

- Read at session start when activity is ARGUMENT-AUDIT, STEELMAN, CLAIM-EVIDENCE-CHECK, SYNTHESIS-CHECK, or any session in a non-fiction/dissertation cartridge that touches argument
- Pressure-test during ARGUMENT-AUDIT (chapter 10-ARGUMENT)
- Never silently rewrite; surface issues and let the writer revise

For the writer:

- Update when the argument shifts (which it will, often, especially early)
- Bump `lfw_argument_version` when a significant revision lands
- Treat this file as the canonical statement of what the book is arguing — the outline is the shape, this is the logic
