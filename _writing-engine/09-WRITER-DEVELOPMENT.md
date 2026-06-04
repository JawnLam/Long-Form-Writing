---
type: writing-engine
role: writer-development
scope: subject-agnostic
updated: 2026-06-02
lfw_load:
  tier: core
  genres: [all]
  activities: [all]
  phase: on-demand
---

# 09 — WRITER DEVELOPMENT

> **The OV's production-and-continuity machinery (chapters 03–08) tracks the manuscript's state. This chapter is about something else: the writer's growth. The controller's memory of strengths, weaknesses, recurring patterns, and current practice focus that turns instance-level critique into deliberate practice. The single highest-leverage addition the engine makes.**

## Why this chapter exists

A production engine without a development layer makes books and not better writers. The session protocol, the revision discipline, the research integration — these track the manuscript. They don't track the writer.

A good non-fiction editor carries a notebook in their head: *this writer buries the lede, overuses the em-dash past the point it lands, writes strong cases and weak syntheses, hedges when the claim is actually strong.* That notebook is what turns "this transition is weak" (said ten times across a year) into "you consistently end sections on the example and never land the claim — that's a transition habit; here's the targeted drill."

This chapter introduces the artifacts and protocol that give the AI that notebook. Without it, every critique is amnesiac and the writer relearns the same lesson on every project.

## The two artifacts

### `_craft-profile.md` — at the OV root

A single file at the LFW root that persists across every cartridge. The AI reads it at the start of every session, in every cartridge. It is the cross-project memory of who this writer is on the page.

Sections (per `TEMPLATE-craft-profile.md`):

- **Observed strengths** — patterns of the writer's prose, structural sense, voice that work and recur
- **Observed weaknesses** — patterns of failure that recur across cartridges
- **Current practice focus** — what the writer is deliberately working on now
- **Pattern log** — dated entries naming a pattern, citing concrete instances, proposing the targeted fix
- **Trajectory** — coarse summary of how the writer has changed across cartridges

The file is opt-in. The writer creates it from the template when ready. The AI doesn't auto-generate one; it would feel surveillance-adjacent and the writer should be the one to decide that the OV is keeping this kind of record.

The file is operator-private. `.gitignore` excludes it. Never shipped with the OV.

### `_craft-log.md` — per cartridge

A per-cartridge file that captures patterns specific to the current manuscript. The AI updates it when a pattern is observed in the manuscript's prose; the writer reads it during CRAFT-REVIEW sessions; entries that turn out to be cross-project graduate up to `_craft-profile.md`.

Sections (per `TEMPLATE-craft-log.md`):

- **Patterns observed this cartridge** — dated entries with examples
- **Open questions for the writer** — things the AI has noticed but isn't sure how to name yet
- **Practice focus for this manuscript** — what the writer is deliberately working on while writing this book
- **Graduations** — patterns that have been observed enough times here that they belong in `_craft-profile.md`

Per-cartridge. Excluded from `.gitignore` by default (operator-private). Lives inside each cartridge folder.

## Diagnostic feedback, not instance feedback

The craft-profile and craft-log enable a tonal shift that's the actual point of this chapter.

**Instance feedback** (what the engine does by default without these artifacts):

> *"This transition is weak. The section ends on the example without landing the claim."*

True. Useful for this section. Doesn't compound across sessions; the writer forgets; the same fix gets proposed again next week.

**Diagnostic feedback** (what the engine does when the craft-log/profile are in play):

> *"This is the same transition pattern flagged in Sections 02-03 and 02-04 — you end on the example without the closing claim that ties it to the chapter argument. Logged in `_craft-log.md` as 'soft-close-on-example.' Pattern fix: write the closing claim sentence first, then place the example before it. Want me to add 'closing-claim-first' to your current practice focus?"*

Same observation. Different work. The first is editing. The second is coaching.

The shift requires both files to exist and to be updated honestly. The AI's job during CRAFT-REVIEW (defined in chapter 10-READER) and during any session where a pattern recurs:

1. Notice the recurrence
2. Name the pattern (kept short and concrete, never clinical)
3. Cite the specific instances
4. Propose the targeted fix or drill
5. Log it in `_craft-log.md`
6. If it has appeared in 3+ cartridges, graduate it to `_craft-profile.md`

The naming matters. "You bury the lede" is a name; "your transitions are sometimes weak" is not. Names are concrete enough to point at; they're also short enough to remember.

## Scaffolding fade

The default LFW posture is *the AI proposes, the writer disposes*. This is the right starting posture. Done indefinitely, it produces a dependent writer: a year in, they can't outline a chapter without the tool.

The voice-default protects the writer's prose from AI homogenization. There is no equivalent default that protects the writer's *thinking* from AI scaffolding. This chapter adds it.

### The three scaffolding modes

Set in `_manuscript-manifest.md`:

```yaml
lfw_scaffolding_mode: full   # full | gradual-fade | socratic
```

**`full` (default)** — the AI proposes structure, argument moves, beats, transitions. The writer accepts or overrides. Standard LFW posture from v1.0.

**`gradual-fade`** — scaffolding intensity decreases across the lifetime of the cartridge, on explicit triggers (see below). Early sessions look like `full`; mid-project sessions ask the writer to generate the outline first, then the AI critiques; late sessions are mostly writer-led with AI as reader, not as architect.

**`socratic`** — from session one, the AI withholds structural and argumentative proposals. It asks Socratic questions, surfaces problems, and pushes back. The writer generates structure, claims, counterarguments. The AI never proposes a beat list or a thesis — only critiques what the writer proposes.

The mode is chosen at cartridging (BOOTSTRAP-NEW-MANUSCRIPT asks). Can be changed mid-cartridge but should be deliberate, not drift.

### Gradual-fade trigger schedule

When `lfw_scaffolding_mode: gradual-fade` is set, the AI's behavior shifts at session-count thresholds:

| Sessions 1–10 | Behavior identical to `full`. AI proposes everything; writer learns the OV's affordances. |
| Sessions 11–30 | At OUTLINE and ARGUMENT-AUDIT activities, the AI asks the writer to draft the structure or claim first, then critiques. At DRAFT and other activities, behavior is still `full`. |
| Sessions 31–60 | OUTLINE and ARGUMENT-AUDIT are writer-led; the AI critiques. STUCK-DIAGNOSTIC adds a "what's your best diagnosis?" prompt before the AI offers its own. |
| Sessions 61+ | Writer-led on all structure, argument, and diagnostic activities. AI's role is reader, pressure-tester, pattern-flagger, craft-coach. AI never proposes a beat list, a claim, or a counterargument without the writer's first attempt on the table. |

These thresholds are defaults. A writer can adjust them in `_manuscript-manifest.md`:

```yaml
lfw_scaffolding_thresholds:
  full_through_session: 10
  partial_fade_through_session: 30
  major_fade_through_session: 60
```

The thresholds are intentionally session-count-based, not time-based. A writer who works 7 days a week reaches session 30 in a month; a writer who works once a week reaches it in seven months. Both have the same accumulated practice. The fade tracks practice, not calendar.

### Why this matters

A writing OV that's done its job leaves the writer needing it less. That's the goal — not user retention. The scaffolding fade designs this in rather than hoping for it.

The writer who completes a `gradual-fade` cartridge should, by the end, have internalized the structural intuitions the AI was scaffolding at the start. The next cartridge they open, they make more proposals; the AI critiques more and structures less. Over multiple cartridges, the AI becomes a reader-and-coach rather than a co-author.

A writer who never fades is not failing — different writers want different tools. But the default for `gradual-fade` is the developmental case; that's what the mode is for.

## Opt-in craft modules

The engine's anti-style-policing stance is correct (chapter 05): the AI doesn't enforce sentence length or cut clichés silently. Voice belongs to the writer.

But there are specific craft disciplines that, when explicitly invoked by the writer for a specific pass, are useful coaching material. These are **modules** — toggled on by the writer for a specific REVISE or READ-THROUGH pass, never silent, never default.

The shipped modules:

### `concrete-to-abstract`

Surfaces sections that lead with abstract argument before grounding it in a concrete example. Reverses the recommended sequence for trade non-fiction (example first, then the principle).

The module reads each section's first three beats and flags those where the abstract claim lands before the concrete grounding. Writer decides whether the inversion is intentional (sometimes it is — academic prose sometimes demands abstract-first) or whether to restructure.

### `signposting`

For long chapters (8,000+ words), flags places where the reader has likely lost the argument's thread. Looks for:

- Sections that don't open with a clear statement of what the section is doing
- Argumentative pivots without explicit transitions
- Recurring threads that go unmentioned for thousands of words and then reappear without re-introduction
- The end of long arguments without a "where we just were and where we're going" landing

Surfaces candidates; writer decides which need signposts and which don't.

### `given-new`

The information-flow contract: each sentence's *given* (the thing the reader already knows) should come first; the *new* should come at the end. Long stretches of new-first prose feel disorienting even when the writer can't say why.

The module flags candidates. It does NOT silently restructure; it surfaces patterns and the writer chooses.

### `curse-of-knowledge`

Reads sections looking for places where the writer has assumed knowledge the target reader (per Reader atoms — see chapter 10-READER) doesn't have. Cross-references the Reader atoms' "background" sections to surface mismatches.

The module's output is a list of specific assumptions the writer should examine. Never silent rewrites.

### `show-dont-tell` *(v1.3.1 — fiction)*

Specified in chapter 13 §4. Surfaces:

- Emotional states asserted in interiority without sensory or behavioral ground (F22 from v1.2)
- Backstory summary at moments where the reader needs the present
- Redundant telling that restates what an earlier scene already showed
- Over-dramatization of routine transitions (F35 — show-everything pathology)

The module is calibrated to the writer's standing position (`strict-show` / `balanced` / `telling-narrator-as-voice` / `off`). Voice-load-bearing telling is protected; weaponized show-don't-tell is the failure mode the calibration prevents.

### `dialogue-and-subtext` *(v1.3.1 — fiction)*

Specified in chapter 13 §1. Surfaces in REVISE and READ-THROUGH passes:

- Lines that score on only one of the four dialogue function axes (plot / character / subtext / rhythm)
- Stretches of 4+ consecutive lines scoring on the same single axis (information-dump cluster; character-demonstration cluster)
- Dialogue that doesn't sound like the speaking character per their dialogue-tells
- Declared subtext (on the Beat atom) that the surface dialogue doesn't carry

Different from the DIALOGUE-AUDIT activity (which is a full-scene audit); the module is a scene-running quick check during revision.

### `pov-and-psychic-distance` *(v1.2 — fiction)*

The fiction equivalent of the non-fiction modules above. Flags three patterns the writer can choose to address:

- **Psychic distance shifts** — the zoom from distant narration ("It was a small town") to deep interiority ("The wallpaper smelled exactly like her grandmother's house, and Maya felt the old hatred wake up"). Good fiction modulates psychic distance deliberately; bad fiction wobbles between zoom levels without intention.
- **Head-hopping within a scene** — the POV character should be consistent within any single scene (with limited, deliberate exceptions in omniscient narration). Mid-scene POV switches are usually unintentional and disorient the reader.
- **Filter words** — *she saw, he felt, she noticed, he heard, she realized, he wondered, she thought.* The words that put a pane of glass between the reader and the experience. Sometimes filter words are correct (when the act of noticing is itself the point). Usually they're a craft tell.

The module is opt-in because filter-word density and psychic-distance choices are voice-load-bearing. A writer whose voice depends on careful filter-word use should not have them silently flagged on every drafted section. They surface only when the writer asks.

See chapter 12 §7 for the full module specification.

### How modules are invoked

In a REVISE or READ-THROUGH session:

> *"Run REVISE on Section 03-04 with the `concrete-to-abstract` and `signposting` modules active."*

The AI loads the modules' diagnostics, applies them to the named atoms, and produces a focused report. Standard REVISE machinery (revision-pass log, etc.) still applies.

### Extending modules

A writer who finds a recurring craft issue not covered by the shipped modules can add their own. Module specification:

- A name (kebab-case)
- A one-sentence description of what it flags
- A diagnostic protocol: what to look for, how to identify candidates, what the report format is
- A recommended use case (which kinds of cartridges, which kinds of revision passes)

Custom modules live in `_writing-engine/_craft-modules/` if added. Out of scope for v1.x core; pattern documented here for future extensibility.

## Fiction-specific error vocabulary (v1.2)

The craft-log discipline (above) names patterns observed in the writer's prose. For non-fiction the patterns tend to be: buries-the-lede, hedging-stack, soft-close-on-example, paragraph-rhythm-monotone, etc. For fiction cartridges the patterns are different:

- **scene-doesn't-turn** — recurring no-turn scenes (the load-bearing fiction craft regression; see chapter 11 F22)
- **and-then-not-but-therefore** — recurring causal-chain slack between scenes
- **arc-asserted-not-earned** — the prose claims a character change it doesn't dramatize
- **antagonist-mechanical** — recurring weak-antagonist patterns
- **motif-stated-not-woven** — themes named in atom files; only one or two appearances in 80,000 words
- **continuity-slip** — world-rule or information-state drift
- **filter-word-density** — recurring pane-of-glass patterns
- **head-hop-within-scene** — unintentional POV switches inside scenes
- **telling-not-showing** — the canonical fiction-craft failure
- **dialogue-as-info-dump** *(v1.3.1)* — recurring lines that score only on Plot axis
- **interchangeable-dialogue** *(v1.3.1)* — recurring lines that score zero on Character axis
- **on-the-nose-subtext** *(v1.3.1)* — characters explaining their feelings; the gap between surface and meaning collapses
- **pov-voice-bleed** *(v1.3.1)* — recurring register-bleed between POVs in alternating-POV work
- **show-everything-pathology** *(v1.3.1)* — routine transitions over-dramatized; pacing collapses
- **on-the-nose-theme** *(v1.3.1)* — theme stated by character or narration as thesis
- **missing-sequels** *(v1.3.1)* — literary fiction where every scene turns and no reactive beats appear
- **over-sequel'd** *(v1.3.1)* — thriller/commercial where action scenes routinely produce extended interiority that violates the form
- **overlay-as-formula** *(v1.3.1)* — beat-sheet overlay treated as writing prescription rather than diagnostic lens
- **character-bible-as-procrastination** *(v1.3.1)* — bible expands indefinitely as avoidance of drafting

These get logged in `_craft-log.md` per the standard chapter-09 discipline. Patterns that appear in 3+ cartridges graduate to `_craft-profile.md`. See chapters 11 and 12 for the activities that produce these observations (SCENE-AUDIT, CHARACTER-CONSISTENCY, CONTINUITY-CHECK, SETUP-PAYOFF-AUDIT, READER-SIMULATION in fiction mode).

## Two cautions

### Caution 1 — Skill model is observational, not scored

Writing skill does not quantify cleanly. A "Level 7 writer" number would be both wrong (no one knows what the units are) and corrosive (the writer either games it or feels graded by it).

`_craft-profile.md` therefore contains **descriptions and examples**, never scores. No "Voice: 7/10" lines. No badge unlocks. No skill trees. Patterns are named in plain language with concrete instances cited. The writer reads their own profile and recognizes themselves; that's the test.

If the AI is ever tempted to add a numeric skill metric, this is the chapter that forbids it.

### Caution 2 — Craft work as procrastination

The same anti-pattern flagged for research integration (chapter 06) applies to craft development. A writer can hide from the blank page inside an ARGUMENT-AUDIT or a CRAFT-REVIEW just as easily as inside a long string of RESEARCH-INTEGRATION sessions.

The AI watches for it. Specifically:

- If `CRAFT-REVIEW` + `ARGUMENT-AUDIT` + `STEELMAN` + `READER-SIMULATION` + similar non-prose activities dominate 5+ consecutive sessions with no DRAFT or REVISE-on-existing-prose, the AI flags it
- The flag is not a judgment. It's a question: *"You've been doing development work for several sessions without producing or revising prose. Is this the right rhythm right now, or is this craft-as-avoidance? Either answer is fine; I want it to be the answer you'd give if asked."*
- The writer answers honestly. Sometimes the development work is genuinely needed (a thesis that doesn't hold needs ARGUMENT-AUDIT before any more drafting). Sometimes it's avoidance.

This caution is structurally identical to the research-as-procrastination caution and lives in the same FAILURE-MODES catalog.

## How this chapter interacts with the rest of the engine

- **Chapter 03 (Cadence and Sessions)** — adds `CRAFT-REVIEW` to the activity table; updates the decision algorithm to consider craft-log entries
- **Chapter 05 (Voice and Craft)** — cross-references this chapter for the craft modules
- **Chapter 06 (Research Integration)** — the research-as-procrastination pattern; this chapter's craft-as-procrastination is structurally identical
- **Chapter 07 (Revision Discipline)** — REVISE passes can invoke craft modules from this chapter
- **Chapter 10 (Reader, Argument)** — the development activities defined in 10-READER (READER-SIMULATION, CRAFT-REVIEW) and 10-ARGUMENT (ARGUMENT-AUDIT, CLAIM-EVIDENCE-CHECK, STEELMAN, SYNTHESIS-CHECK) include CRAFT-REVIEW; this chapter is the *what*, 10-READER is the *when*
- **`_meta/FAILURE-MODES.md`** — adds craft-work-as-procrastination, scaffolding-not-fading, skill-scoring-attempted

## When the writer should engage this chapter

- **Bootstrap** — BOOTSTRAP-NEW-MANUSCRIPT now asks about scaffolding mode and whether to create `_craft-log.md` for this cartridge
- **After ~5 sessions in a cartridge** — first natural moment to propose creating `_craft-profile.md` if it doesn't exist
- **Every ~10 sessions** — natural cadence for CRAFT-REVIEW (defined in chapter 10-READER)
- **End of a cartridge** — final CRAFT-REVIEW; graduate patterns from `_craft-log.md` to `_craft-profile.md`
- **Start of the next cartridge** — the AI reads `_craft-profile.md` and the writer's accumulated patterns inform the new engagement from session one
