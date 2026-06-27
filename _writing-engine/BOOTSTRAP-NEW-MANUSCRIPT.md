---
type: writing-engine
role: cartridge-bootstrapping-prompt
scope: subject-agnostic
updated: 2026-06-02
lfw_load:
  tier: core
  genres: [all]
  activities: [SESSION-START]
  phase: on-demand
---

# BOOTSTRAP A NEW MANUSCRIPT

> **You are an AI assistant (Claude, Gemini, ChatGPT, or other capable model). The writer has asked you to set up a new manuscript cartridge in LFW. This document is your complete execution plan. Follow it end-to-end. Ask clarifying questions one at a time before building.**

## What you're producing

A complete cartridge inside the `Long-Form-Writing/` folder for the new manuscript. A successful cartridge includes:

1. `_manuscript-manifest.md` — what this manuscript is, genre, premise, audience
2. `_state.md` — initial lifecycle stage and today's focus
3. `_outline.md` — initial structural outline (can be very rough at first)
4. `_voice-samples.md` — if the writer opts into voice-samples mode
5. Empty-but-ready `Items/` subfolders for the genre's Types
6. `Sessions/` and `Revision-Passes/` folders ready for use
7. A bootstrap session log (Session 000) documenting setup

## Before you start

Read these files in order:

1. `00-START-HERE.md`
2. `01-WHAT-IS-LFW.md`
3. `02-GENRE-AND-SCHEMA.md`
4. `03-CADENCE-AND-SESSIONS.md`
5. `04-ITEMS-AND-STRUCTURE.md`
6. `05-VOICE-AND-CRAFT.md`
7. `06-RESEARCH-INTEGRATION.md` (if non-fiction or dissertation)
8. All files in `_templates/`
9. The shipped worked example (`Example-Project-The-Persistence-Question/`) as a reference

## Clarifying questions you must ask the writer

Before creating any files, ask these. **One question at a time, conversationally.** Wait for each answer, probe if thin, then ask the next.

This is non-negotiable. A multi-bullet questionnaire is a documented failure mode (`_meta/FAILURE-MODES.md` F1).

### CQ1 — What's the project?

State it in one sentence. The shape matters: "a novel" is too broad; "a 75,000-word literary novel about three sisters who inherit a winery during a wildfire season" is the kind of specificity that produces a working schema.

### CQ2 — Genre?

Which of fiction / non-fiction / screenplay / play / dissertation, or hybrid? If hybrid (memoir, narrative non-fiction, autofiction), pick the closest match and we'll override Types as needed.

### CQ3 — Target length?

Word count range, page count range, runtime if applicable. This shapes pacing and milestone tracking.

### CQ4 — Audience?

Who is this for? Be specific — "general readers" is too vague; "educated general readers who read Mary Beard and Yuval Harari" is calibratable.

### CQ5 — What's the premise / thesis / logline?

One sentence (fiction: logline; non-fiction: thesis statement; dissertation: research question; screenplay: logline). The thing the manuscript exists to argue, dramatize, or prove.

### CQ6 — Why this, why now?

What's driving the writer? Career? Personal need? Long-held idea? Commission?

### CQ7 — Current state?

Has the writer started? Have they outlined? Drafted anything? Have prior abandoned attempts? What exists today vs. what we're starting from scratch?

### CQ8 — Voice mode?

The default is `writer-maintains` (the AI doesn't try to match voice). Does the writer want this default, or opt into voice-samples / voice-check-on-demand? If samples, do they have material ready to provide?

### CQ9 — Cadence?

How often will they work on this? How long is a typical session? This shapes the session protocol's defaults for `>3 days = SESSION-START`, etc.

### CQ10 — Citation style? (Non-fiction / dissertation only)

Chicago / MLA / APA / Harvard / custom?

### CQ11 — Reader modeling (non-fiction emphasis)

Who's the manuscript actually for? Get specific — name two or three reader archetypes the writer wants to satisfy. For non-fiction, the standard set is The Skeptic, The Impatient Generalist, The Domain Expert; the writer can adopt these, modify them, or define their own. These will become Reader Items in the cartridge (see chapter 10-READER) and the AI will use them in READER-SIMULATION activities.

For fiction / screenplay / play, Reader Items are optional but useful. For dissertation, Readers are usually the committee + future researchers in the field.

### CQ12 — Argument articulation (non-fiction / dissertation only)

What's the manuscript's thesis as a falsifiable claim? Not "this book is about X" — the actual sentence the writer is willing to defend, with the falsification condition. The writer's first articulation is fine even if it changes later; the point is to have an `_argument.md` to pressure-test.

For fiction without thematic argument, skip. For memoir / narrative non-fiction, ask (most have an implicit argument worth articulating).

### CQ13 — Scaffolding mode

The default is `full` — AI proposes structure, argument, beats. The writer accepts or overrides. Standard LFW posture.

Alternative: `gradual-fade`. Scaffolding intensity decreases across the lifetime of the cartridge on session-count thresholds (see chapter 09). Recommended for writers who want to develop independent structural intuition over the project's life.

Alternative: `socratic`. From session one, the AI withholds proposals and only critiques what the writer generates. Recommended for experienced writers who want pressure-testing rather than scaffolding.

Confirm or modify.

### CQ14 — Craft-profile awareness

Does the writer already have a `_craft-profile.md` at the OV root (from prior cartridges)? If yes, the AI reads it and the new cartridge benefits from accumulated craft observations. If no, propose creating one after the first few sessions in this cartridge (~session 5–8). No pressure; opt-in.

### CQ15 — Fiction-specific: spine, motifs, promises, continuity (fiction / screenplay / play only)

**For fiction cartridges only. Skip if non-fiction/dissertation.**

- **Spine** (`_spine.md`) — required for fiction. The writer's first articulation of the dramatic question (a yes/no or which question the manuscript answers at the climax) and the premise as a causal claim. First articulation is provisional; ARGUMENT-AUDIT's fiction equivalent (SCENE-AUDIT walked across the spine) will pressure-test.
- **Motifs** — what 2–4 recurring sub-surface elements does the writer want to track deliberately (image systems, recurring objects, thematic patterns)? These become Motif Items.
- **Promises** (`_promises.md`) — required for plot-driven fiction. Initially populated as the writer outlines; setups planted in early chapters are recorded so SETUP-PAYOFF-AUDIT can track them.
- **Continuity** (`_continuity.md`) — required for genre fiction with worldbuilding and any plot with secrets. The writer's initial world-rules, timeline, and information-state ledger.
- **Scaffolding mode reminder** — fiction cartridges should typically default to `gradual-fade` or `socratic` (CQ13), not `full`. Invention is the central fiction skill the OV must not crowd out.

### CQ16 — Anything else load-bearing the AI should know?

Communication preferences, particular sensitivities, prior bad experiences with AI writing assistance, anything that should shape the engagement from the start.

Once you have answers, proceed.

## Step-by-step execution

### Step 1 — Create the cartridge folder

Use a human-readable name matching the manuscript. Examples:

- `The-Winery-Sisters-Novel/`
- `Family-Memoir-Working-Title/`
- `Antarctic-Treaty-Book/`
- `Three-Act-Heist-Screenplay/`
- `Dissertation-On-Variety-Engineering/`

Avoid spaces; use hyphens. Avoid the word "Example" unless you're literally building a worked example for documentation.

### Step 2 — Populate the manifest

Use `_templates/TEMPLATE-manuscript-manifest.md`. Fill in from CQ1–CQ11.

### Step 3 — Create the Item folders

Based on genre (see `02-GENRE-AND-SCHEMA.md`):

```
<Cartridge>/Items/
├── Beats/
├── Scenes/         (fiction / screenplay / play)
├── Sections/       (non-fiction / dissertation)
├── Chapters/
├── Characters/     (fiction / screenplay / play)
├── Threads/        (non-fiction / dissertation)
├── Sources/        (non-fiction / dissertation, optional for fiction)
└── Notes/
```

Include only the folders relevant to the declared genre.

### Step 4 — Initialize state

Use `_templates/TEMPLATE-state.md`. Set:

- `lfw_lifecycle_stage: outlining` (default for new cartridges)
- `lfw_genre`: from CQ2
- Today's focus: "Initial book-level outline"
- Open Thread: "Session 001 — work the book-level outline with the writer"

### Step 5 — Seed an initial outline

Use `_templates/TEMPLATE-outline.md`. Create a minimal book-level outline based on the premise (CQ5). Don't fabricate chapter content — leave most of it as `*To be developed in OUTLINE sessions*`. The point is to have the structure to write into.

### Step 6 — Voice samples (if applicable)

If the writer opted for voice-samples mode in CQ8:

- Create `_voice-samples.md` from template
- Ask the writer to provide 3–5 substantial passages (300+ words each) of their representative writing
- Save these in the file with brief context for each

If the writer opted for writer-maintains mode (default), skip this file. Don't create an empty one.

### Step 7 — Empty subfolders

Add `.gitkeep` to `Sessions/`, `Revision-Passes/`, and any empty Item folders so they survive transport.

### Step 8 — Write the bootstrap session log

Use `_templates/TEMPLATE-Session.md`. Create `Sessions/YYYY-MM-DD_000_BOOTSTRAP.md` documenting what you created and what's queued for Session 001 (typically the first real OUTLINE session at book level).

### Step 9 — Show the writer what you built

Summarize:

- Manuscript name and genre
- Outline shape (book-level)
- Item folders created
- Voice mode active
- What Session 001 will be (typically OUTLINE on the book-level structure)

Then stop. The writer reviews. When they're ready for Session 001, they tell you.

## Quality gates

Before considering cartridging complete:

- [ ] CQ1–CQ11 asked and answered (conversationally)
- [ ] Cartridge folder created
- [ ] `_manuscript-manifest.md` populated
- [ ] `_state.md` initialized
- [ ] `_outline.md` exists (even if mostly placeholder)
- [ ] Voice samples file present if voice mode requires it
- [ ] All required Item folders created
- [ ] `Sessions/` and `Revision-Passes/` exist
- [ ] Bootstrap session log written
- [ ] Summary shown to writer

## Common failure modes to avoid

1. **Multi-bullet questionnaire** — F1 in failure modes. Conversation, not assignment.
2. **Drafting prose during bootstrap** — Bootstrap is setup, not drafting. No prose generated at this stage.
3. **Fabricating premise content** — Use the writer's words. Don't generate plot points, thesis points, or arguments they didn't give you.
4. **Over-elaborate initial outline** — Keep the initial outline rough. The writer fills it in across OUTLINE sessions.
5. **Skipping voice-mode question** — Default matters. Make the writer aware of the choice.
6. **Inferring genre from premise** — Always ask. A "story about my family" could be memoir, novel, screenplay, or play.

## A note on the writer

The writer is an adult doing serious work. They're not a beginner. They expect competent help, not encouragement. The bootstrap conversation should feel like talking with a sharp editor at the start of a long project — interested, focused, asking the questions that matter.
