---
type: writing-engine
role: argument-backbone
scope: non-fiction-and-dissertation
updated: 2026-06-03
lfw_load:
  tier: pack
  genres: [non-fiction, dissertation]
  activities: [ARGUMENT-AUDIT, CLAIM-EVIDENCE-CHECK, STEELMAN, SYNTHESIS-CHECK]
  phase: on-demand
---

# 10 — ARGUMENT (Non-Fiction Backbone)

> **Fiction has a story; non-fiction has an argument. This chapter introduces the argument as an artifact the AI can pressure-test and defines the four argument-side activities (ARGUMENT-AUDIT, CLAIM-EVIDENCE-CHECK, STEELMAN, SYNTHESIS-CHECK). Reader/audience modeling lives in `10-READER.md` (core, all genres).**

## Why this chapter exists

A non-fiction failure mode that is not structural and not stylistic — it's upstream of both:

**The argument and the structure quietly diverge.** The container hierarchy (book → chapter → section → beat) is one thing; the *argument* (thesis → sub-claims → evidence → defeaters) is another. A section that's interesting but advances no claim is a structural success and an argumentative failure. A thesis that isn't contestable is a writing project disguised as a book.

Chapter 04 (Atoms and Structure) gave us containers. This chapter gives us *the argument as an artifact the AI can pressure-test.*

## Part one — Argument as a backbone

### `_argument.md` — the cartridge backbone

A non-fiction cartridge has, in addition to `_outline.md` (container hierarchy), an `_argument.md` (logical structure). The two are intentionally different artifacts because they encode different things:

- `_outline.md` answers *what's in the book and in what order*
- `_argument.md` answers *what the book claims, what supports each claim, and what would defeat it*

A book whose outline and argument are tightly aligned is structurally sound. A book whose outline contains sections that don't appear in the argument has structural padding; a book whose argument contains claims that don't appear in the outline has argumentative gaps.

### Required sections of `_argument.md`

1. **Thesis** — the book's central claim, stated as a falsifiable sentence. Not "this book is about X"; the actual claim. Includes the falsification condition: what evidence or argument would force the writer to retract.
2. **Sub-claims** — the 3–7 claims the thesis decomposes into. Each is a sentence the writer is willing to defend.
3. **Evidence map** — for each sub-claim, the Sources, cases, or reasoning that supports it. Cross-references to Source atoms.
4. **Independence check** — explicit assessment of whether the sub-claims are genuinely independent or whether some collapse into others. This is the place the example's own "is condition four the weakest" question lives.
5. **Defeaters** — for each sub-claim, what would change the writer's mind. The strongest version of the counterargument. Cross-references to Sources that complicate, where they exist.
6. **The honest unknown** — what the writer doesn't know, what the framework can't predict, what's still genuinely contested. The book's epistemic humility, made explicit.

### When `_argument.md` is required

- **Non-fiction** — required
- **Dissertation / academic** — required (and rigorous; this is where the literature-review chapter's structure comes from)
- **Memoir / narrative non-fiction** — recommended; argument may be more implicit but still has a shape
- **Fiction** — optional; some fiction has a thematic argument worth articulating, most doesn't
- **Screenplay / play** — typically not applicable; thematic argument lives in subtext, not in claim structure

## Part two — The four argument-pressure activities

### ARGUMENT-AUDIT

**What it is:** Pressure-test of `_argument.md`. Is the thesis contestable? Are the sub-claims genuinely independent? Where's the weakest link? What would defeat the argument that isn't currently engaged?

**Trigger conditions:**

- `_argument.md` exists and has been touched since the last ARGUMENT-AUDIT
- A new chapter has been outlined that touches new sub-claims
- The writer flags ARGUMENT-AUDIT explicitly ("I'm not sure the framework holds")
- 8+ sessions since the last ARGUMENT-AUDIT

**Protocol:**

1. AI reads `_argument.md` in full
2. AI reads any Thread atoms (cross-cartridge thread tracking)
3. AI tests, in order:
   - **Contestability** — is the thesis a claim a reasonable person could disagree with? A non-falsifiable thesis is not a thesis; it's a stance.
   - **Sub-claim independence** — do the sub-claims actually decompose into separate pieces, or do two of them collapse?
   - **Evidence sufficiency** — for each sub-claim, does the evidence map cite specific sources or is it hand-wavy?
   - **Defeater handling** — for each sub-claim, is the strongest counter named in `## Defeaters`, or is the engagement weak?
   - **Weakest link** — which sub-claim, if dropped, would most damage the overall thesis? Is that sub-claim the most thinly supported one?
4. AI produces a report covering each test. Honest, substantive, not flattering.
5. Writer decides which findings to address. Often the answer is "the argument needs revision before more drafting" — a real and good answer that the OV should make easy to act on.

**Discipline:** this activity is the place where structural padding gets exposed. A section that the outline has but the argument doesn't need is structural padding. Surfaces; doesn't silently cut.

### CLAIM-EVIDENCE-CHECK

**What it is:** Distinct from the accuracy revision pass. **Accuracy** asks *is the citation real, is the quote correct.* **Claim-evidence-check** asks *does this evidence warrant a claim this strong.* Overclaiming is non-fiction's cardinal sin.

**Trigger conditions:**

- Section is in `drafted` status
- Section cites Source atoms (or makes claims that should cite Source atoms)
- Before accuracy revision pass (it's a different question)

**Protocol:**

1. AI reads the target Section
2. AI reads every Source atom cited
3. For each load-bearing claim in the prose:
   - Identify what the claim is asserting
   - Identify what the cited source actually supports
   - Compare: does the source warrant the claim as stated, or is the claim stronger than the source supports?
4. AI produces a list of:
   - **Overclaimed** — sentences where the prose asserts more than the source supports
   - **Underclaimed** — sentences where the prose hedges more than the source warrants (sometimes the writer's own argument is stronger than they've let it be)
   - **Unsupported** — claims that have no source backing in this section
   - **Source mismatched** — sources cited that don't actually support the specific claim
5. Writer revises in a subsequent REVISE session

**Connection to chapter 06:** Research-integration handles *getting sources into the manuscript correctly*. Claim-evidence-check handles *making sure the prose's claims match what the sources actually support*. They're sequential and complementary.

### STEELMAN

**What it is:** Before the writer rebuts a counterargument in a Thread or Section, the AI builds the strongest version of the counterargument. The point is to make the rebuttal land against the actual strong opposition, not a strawman the writer is comfortable with.

**Trigger conditions:**

- Writer is preparing to rebut a counterargument
- A Thread atom's `## Sources that complicate or contradict it` section has entries that haven't been steelmanned
- Writer flags STEELMAN explicitly

**Protocol:**

1. AI loads the relevant Thread or Section
2. AI loads the counter-Source atoms
3. AI constructs the strongest version of the counterargument:
   - State the counter-claim as charitably and forcefully as possible
   - Cite the counter-evidence at its strongest
   - Anticipate what the counterargument's *best* defender would say to the writer's rebuttal
4. AI presents the steelman to the writer
5. Writer revises their rebuttal (in a subsequent REVISE session) against the steelman, not against their original strawman

**Discipline:** the AI is not allowed to soften the steelman to make the writer's rebuttal easier. The point is to make the writer earn the rebuttal. If the steelman is so strong that the writer's rebuttal doesn't hold, that's a finding — the writer either revises the rebuttal or revises the claim.

### SYNTHESIS-CHECK

**What it is:** Flag sections that are annotated-bibliography-in-disguise — sections that report sources cleanly but don't synthesize them into a claim that's the writer's. The skill that makes a better non-fiction writer is synthesizing sources into something new, not just citing them.

**Trigger conditions:**

- Section is in `drafted` status
- Section cites 3+ Source atoms
- Section hasn't been synthesis-checked

**Protocol:**

1. AI reads the target Section
2. AI examines the section's structure:
   - How many sentences are quotation, paraphrase, or source-attribution?
   - How many sentences are the writer's synthesis, integration, or original argument?
   - Is the section's main move *reporting* what sources say, or *making* an argument that uses them?
3. AI produces a report:
   - **Synthesis ratio** — rough estimate of synthesis-vs-report content
   - **Sections where the writer's voice goes missing** — long stretches where the prose is entirely source-attribution
   - **The argument this section actually makes** — restated by the AI; writer assesses whether it's the argument the section is supposed to make
   - **Suggested move** — sometimes the right answer is to shorten source content and amplify the writer's synthesis
4. Writer decides whether to restructure

**Connection to chapter 06:** Research-integration teaches the writer to *handle sources cleanly*. Synthesis-check makes sure the sources serve the writer's argument rather than substituting for it.

## How this chapter interacts with the rest of the engine

- **Chapter 03 (Cadence and Sessions)** — ARGUMENT-AUDIT, CLAIM-EVIDENCE-CHECK, STEELMAN, and SYNTHESIS-CHECK are entries in the universal activity table
- **Chapter 04 (Atoms and Structure)** — `_argument.md` and `_craft-log.md` are added as cartridge backbone files
- **Chapter 06 (Research Integration)** — CLAIM-EVIDENCE-CHECK, STEELMAN, and SYNTHESIS-CHECK extend the research discipline beyond getting sources in; chapter 06 + this chapter together are the full research-and-argument toolkit
- **Chapter 07 (Revision Discipline)** — claim-evidence and synthesis findings feed into revision passes
- **Chapter 10 (Reader)** — the companion core chapter for audience modeling; READER-SIMULATION often runs alongside these argument-pressure activities for non-fiction cartridges
- **`_meta/FAILURE-MODES.md`** — argument-audit-as-procrastination is a variant of the craft-as-procrastination anti-pattern

## When argument activities don't apply

Some genres make some of these activities optional:

- **Fiction without thematic argument** — `_argument.md` is optional; ARGUMENT-AUDIT is rare
- **Screenplay / play** — `_argument.md` is unusual; STEELMAN may apply if there's a politically-charged subject
- **Dissertation** — every activity applies, often more rigorously than for trade non-fiction. CLAIM-EVIDENCE-CHECK is essential. STEELMAN is the literature-review chapter's central discipline

The activity table in chapter 03 is the source of truth for which activities are universal vs. genre-conditional.
