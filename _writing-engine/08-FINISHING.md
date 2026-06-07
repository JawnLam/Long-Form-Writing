---
type: writing-engine
role: finishing
scope: subject-agnostic
updated: 2026-06-02
lfw_load:
  tier: core
  genres: [all]
  activities: [BETA-PREP, READ-THROUGH]
  phase: on-demand
---

# 08 — FINISHING

> **Getting from drafted to shippable. Beta readers, assembly, the honest-thinness audit, and what "done" means.**

## The lifecycle stages near the end

```
drafting → revising → fact-checking (non-fic) → polishing → with-beta-readers → final-revision → final → shipped
```

Each transition has a checklist. Don't transition prematurely.

## Polishing stage

Polishing is the final-revision-pass stage. The writer has:

- Completed at least one structural revision pass
- Completed at least one voice pass
- Completed accuracy passes (non-fiction)
- Completed at least one prose-line pass

The manuscript is "drafted" in every section, "revised" in most, with the remaining items in the writer's known-thin list.

Polishing tightens the last 10%. Activities:

- Final prose-line work on remaining Items
- Front-matter and back-matter (acknowledgments, bibliography, dedication, etc.)
- Page-count / word-count discipline (cutting filler if over; adding texture if under)
- Final consistency checks (character details, spelling of names, formatting)

When polishing is done, the lifecycle stage moves to `ready-for-beta` if you have beta readers; otherwise directly to `final` if the writer is shipping without beta.

## The honest-thinness audit

Before sending to beta readers (or before shipping if no beta), the writer runs an honest-thinness audit with the AI. The AI's job: surface what's still thin.

The audit reads:

- The full outline
- Every chapter at high level
- Every Thread / Character Item
- The revision-pass logs

The audit produces:

- **Structural thinness:** chapters or sections that still feel undercooked despite the revision passes
- **Voice thinness:** places where voice still feels inconsistent
- **Argument thinness (non-fiction):** claims that still need stronger support; counter-arguments still unaddressed
- **Character thinness (fiction):** characters who never quite came alive; arcs that don't pay off
- **Pacing thinness:** chapters that drag; chapters that compress what should be longer
- **Honest assessment of strongest and weakest chapters**

The AI presents this candidly. The writer makes the call: ship anyway, fix the thin spots, or open another revision round.

This is the activity to use when the writer is asking themselves *"is this done?"* The audit gives them a structured answer.

## BETA-PREP activity

When the writer is ready to send to beta readers, the AI runs a BETA-PREP activity that produces:

### A beta-reader brief

A short document the writer can send along with the manuscript. Contents:

- **What kind of book this is** — genre, intended audience, comparable titles
- **What the writer is asking for** — overall reactions, specific concerns, particular chapters
- **What to ignore** — things the writer knows about and is already addressing
- **What's intentional** — stylistic choices that might look like mistakes but aren't
- **Logistics** — by-when, what format, how to send feedback

A good beta brief saves the writer from the unhelpful "I liked it" responses and gets them targeted feedback they can use.

### An assembly check

Pull the prose from all Section/Scene Items into a single read-through document for the beta reader. Verify:

- All Items in their final order
- No placeholder text or `*To be drafted*` markers slipped through
- All citations resolve to Source Items
- Front-matter and back-matter present

### A bug-report channel for the writer

The AI suggests that the writer keep a `Beta-Feedback/` folder in the cartridge to collect responses. Each beta reader's feedback becomes its own file. Patterns across readers get surfaced when the writer opens the next revision pass.

## During the beta period

Lifecycle stage: `with-beta-readers`.

The writer can:

- Start a new manuscript (open a new cartridge)
- Work on revisions to OTHER chapters they know need work regardless of beta feedback
- Read more sources for a future project
- Rest

The writer should NOT:

- Make pre-emptive changes based on imagined beta feedback
- Open the manuscript every day to second-guess decisions

The AI declines to do speculative revision on the manuscript while it's `with-beta-readers`. The discipline is: wait for the actual feedback.

## After beta feedback

When beta responses come in:

1. Read them all before responding to any
2. Categorize feedback:
   - **Universal hits** (3+ readers said the same thing): take seriously
   - **Specific reader bias** (one reader hated a chapter another loved): assess case by case
   - **Direct contradictions** (reader A wants more X; reader B wants less): writer judgment
   - **Things the writer disagrees with**: defensible to ignore but note why
3. Open a new revision round to address the universal hits
4. Update Thread/Character Items with any beta-surfaced gaps
5. Run another honest-thinness audit before final

## The "final" stage

When the writer decides the manuscript is done:

- Lifecycle stage: `final`
- All Items have `lfw_status: final`
- The manuscript can be assembled for distribution

Assembly is straightforward: walk the outline order, pull prose from each Section/Scene in order, concatenate.

## Output formats

LFW v1.0 doesn't ship export tooling. The manuscript lives as markdown Items; assembly produces a single markdown file. Conversion to other formats (PDF, EPUB, DOCX, screenplay format like Fountain or FDX, dissertation LaTeX) happens outside the OV.

Recommended tools (out of scope, just pointers):

- **Pandoc** for Markdown → PDF / EPUB / DOCX
- **Vellum** (Mac) for clean EPUB and print PDF
- **Fountain** for screenplay-to-Final-Draft conversion
- **LaTeX with biblatex** for dissertations

## Shipped stage

`lfw_status: shipped` on the manuscript indicates the project is out in the world (published, deposited, submitted, sold, distributed — whatever "out" means for your project).

After shipping, the cartridge becomes a record. The writer:

- Can revisit it for retrospective reasons
- Can mine it for material for the next project
- Can use it as a worked example for their own future LFW cartridges

The cartridge folder can be moved to an `_Archived/` directory or kept in place. The Items have value as a record of what the writer learned about their own process.

## When a manuscript doesn't finish

Some projects don't ship. The writer:

- Updates `_state.md` lifecycle stage to `abandoned`
- Writes a final session log explaining why (not for guilt; for future-self's reference)
- Moves the cartridge to `_Archived/`
- Does NOT delete

Abandoned cartridges have real value: they capture what the writer was working on, what shape the project took, what blocked it. Future projects often reuse Items (Characters, Threads, Sources) from abandoned cartridges.

The OV does not judge abandonment. Most serious writers have multiple abandoned projects. They're part of the work.

## The honest definition of "done"

The most useful definition of "done" for a manuscript:

> *Done is when the next pass would not measurably improve the manuscript over what shipping now would accomplish.*

This is not "done is when it's perfect." Perfect doesn't exist in long-form writing. The choice is between (a) shipping a manuscript that has flaws but does work in the world, and (b) refining a manuscript indefinitely so it does no work at all.

The honest-thinness audit + the writer's judgment + (for non-final projects) an external editor are how this gets decided.

The OV's job here is to make the choice visible, not to make it for the writer.
