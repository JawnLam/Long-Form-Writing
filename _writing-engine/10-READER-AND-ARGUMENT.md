---
type: writing-engine
role: reader-and-argument
scope: subject-agnostic-with-non-fiction-emphasis
updated: 2026-06-02
lfw_load:
  tier: pack
  genres: [non-fiction, dissertation]
  activities: [READER-SIMULATION, ARGUMENT-AUDIT, CLAIM-EVIDENCE-CHECK, STEELMAN, SYNTHESIS-CHECK, CRAFT-REVIEW]
  phase: on-demand
---

# 10 — READER AND ARGUMENT

> **Fiction has Characters as first-class atoms. Non-fiction's true analog isn't Thread — it's the Reader. Fiction has a story; non-fiction has an argument. This chapter introduces both as first-class concerns and defines the six development activities that pressure-test them.**

## Why this chapter exists

Two of the most common failure modes in non-fiction are not structural and not stylistic — they're upstream of both:

1. **The reader evaporates.** The manuscript manifest asks "who is this for" once at bootstrap, and then the audience model disappears. The writer drifts; the prose drifts; what felt clear at the breakfast-table-conversation level becomes opaque to anyone who isn't already in the writer's head. Curse of knowledge is one specific form; there are others.
2. **The argument and the structure quietly diverge.** The container hierarchy (book → chapter → section → beat) is one thing; the *argument* (thesis → sub-claims → evidence → defeaters) is another. A section that's interesting but advances no claim is a structural success and an argumentative failure. A thesis that isn't contestable is a writing project disguised as a book.

Chapter 04 (Atoms and Structure) gave us containers. This chapter gives us *the reader as an entity the AI can model* and *the argument as an artifact the AI can pressure-test.*

## Part one — Reader as a first-class atom

### The Reader atom

A Reader is a modeled audience member: what they bring to the page, what they're patient with, what they reward, what they punish. The AI uses Reader atoms in the **READER-SIMULATION** activity (below) to read drafted sections *as that reader* and report where the reader resists, gets lost, or hits the curse of knowledge.

### Frontmatter

```yaml
Item_Prototype: LFW_Reader
Item_ID: "<lowercase-kebab-slug>"
Title: "<Reader name — short, descriptive>"
lfw_manuscript: <manuscript-slug>
lfw_atom_type: reader
lfw_status: developing   # developing | active | retired
lfw_priority: primary   # primary | secondary | tertiary
Date_Added:
Date_Modified:
Needs_Processing: false
```

### Required body sections

1. `# <Reader name>`
2. `## Who they are` — concrete sketch; one paragraph (e.g., "Educated general reader; not in the writer's field; reads non-fiction across history, sociology, economics. Subscribes to The Atlantic. Reads Mary Beard, Yuval Harari, Walter Scheidel.")
3. `## Background they bring` — what the reader already knows when they open this book. Critical for curse-of-knowledge work.
4. `## What they reward` — moves that land well with this reader (concrete examples, dry humor, structural clarity, willingness to engage counter-evidence honestly, etc.)
5. `## What they punish` — moves that lose this reader (academic jargon, hedging stacks, sections that don't advance argument, unsupported claims, etc.)
6. `## Where they resist` — places this specific reader is predisposed to push back (e.g., the Skeptic resists every claim that lacks evidence; the Domain Expert resists every oversimplification of their field)
7. `## What they're patient with vs. impatient with` — pacing, density, formality
8. `## Notes` — anything else the writer wants the AI to know when reading-as-this-reader

### Naming and location

- **Naming:** `<Reader-Slug>.md`. E.g., `Skeptic.md`, `Impatient-Generalist.md`, `Domain-Expert.md`. Or named after a real reader-archetype: `The-Atlantic-Reader.md`.
- **Location:** `Atoms/Readers/` within the cartridge.

### Recommended reader set for non-fiction cartridges

Most non-fiction manuscripts benefit from 2–4 Reader atoms covering distinct vantages. The standard set:

- **The Skeptic** — predisposed to disbelieve. Tests every claim. Resists strong assertions without evidence. The reader who keeps the writer honest.
- **The Impatient Generalist** — predisposed to lose interest if the payoff isn't visible. Tests pacing and structural clarity. Resists slow sections, missing signposts, sections that exist for completeness rather than argument.
- **The Domain Expert** — predisposed to catch oversimplification. Tests technical accuracy. Resists where the writer's compressions cross into wrong rather than just simplified.

These three together cover the most common failure modes. Add others as the project warrants — *The Politically Suspicious Reader* for a politically-sensitive chapter, *The First-Year Graduate Student* for an academic-adjacent book, *The Practitioner* for a book about a profession.

### Reader status lifecycle

- **developing** — Reader has been sketched but not yet exercised in a READER-SIMULATION
- **active** — Reader is in use; READER-SIMULATION sessions invoke them
- **retired** — Reader was used but is no longer relevant to remaining chapters (e.g., a politically-suspicious reader for a chapter that's been cut)

## Part two — Argument as a backbone

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

## Part three — The six new development activities

These are the activities the production set (chapters 03 + 07) doesn't include. They are weighted for non-fiction. Each is a first-class entry in the universal activity set (now 16 total — the original 10 in chapter 03 plus these 6).

### READER-SIMULATION

**What it is:** The AI reads a specific atom (Section or Scene or Chapter, depending on scope) *as a specific Reader atom* and reports where that reader resists, where they get lost, where they hit curse of knowledge, where they disengage.

**Trigger conditions:**

- Section or chapter is in `drafted` status
- At least one Reader atom is in `active` status
- READER-SIMULATION hasn't been run on this atom yet (or has been run only with one Reader and the others are due)

**Protocol:**

1. AI loads the named Reader atom
2. AI loads the target atom (Section/Scene/Chapter)
3. AI loads the manifest (to know voice mode, declared audience)
4. AI reads the target *as* the Reader — internally maintaining the Reader's background, patience, knowledge gaps
5. AI produces a report:
   - **Resistance points** — specific sentences/paragraphs where this Reader pushes back
   - **Lost-thread moments** — places where the Reader can no longer follow the argument
   - **Curse of knowledge instances** — where the writer assumes knowledge this Reader doesn't have
   - **Reward moments** — places this Reader notices and appreciates (so the writer keeps the moves)
   - **What this Reader most wants to see addressed that isn't**
6. AI logs the simulation in the session log
7. Writer revises (or doesn't) based on the report; revision happens in a subsequent REVISE session, not in the same session

**Critical discipline:** the AI does NOT silently rewrite to satisfy the Reader. It reports. Writer decides.

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

### CRAFT-REVIEW

**What it is:** Periodic review that reads recent session logs, the craft-log, and the craft-profile, surfaces the writer's recurring patterns, and proposes a focus for the next stretch of work. This is what converts session logs into deliberate practice (see chapter 09 in full).

**Trigger conditions:**

- 10+ sessions since last CRAFT-REVIEW
- End of a chapter draft
- Writer flags it explicitly
- A pattern has appeared 3+ times in `_craft-log.md` and warrants graduating to `_craft-profile.md`

**Protocol:**

1. AI reads the most recent 10–15 session logs
2. AI reads `_craft-log.md` in full
3. AI reads `_craft-profile.md` if it exists
4. AI identifies:
   - Patterns recurring in this cartridge — log them or update existing entries in `_craft-log.md`
   - Patterns recurring across cartridges — graduate to `_craft-profile.md`
   - The writer's progress on their current practice focus (if one is set)
   - A proposed practice focus for the next stretch
5. AI produces a report and updates the relevant files
6. Writer reads, agrees or adjusts, sets the practice focus

**Discipline:** observational, not scored (per chapter 09's first caution). Concrete pattern names with cited instances. No skill levels. No badges.

## How chapter 10 interacts with the rest of the engine

- **Chapter 03 (Cadence and Sessions)** — the universal activity table now lists 16 activities; the six defined here are weighted for non-fiction
- **Chapter 04 (Atoms and Structure)** — Reader is added as a first-class atom; `_argument.md` and `_craft-log.md` are added as cartridge backbone files
- **Chapter 06 (Research Integration)** — CLAIM-EVIDENCE-CHECK, STEELMAN, and SYNTHESIS-CHECK extend the research discipline beyond getting sources in; chapter 06 + chapter 10 together are the full research-and-argument toolkit
- **Chapter 07 (Revision Discipline)** — claim-evidence and synthesis findings feed into revision passes
- **Chapter 09 (Writer Development)** — defines the craft-profile and craft-log artifacts that CRAFT-REVIEW uses; this chapter is when, that chapter is what
- **`_meta/FAILURE-MODES.md`** — adds craft-as-procrastination (also addresses argument-audit-as-procrastination and reader-simulation-as-procrastination — all variants of the same anti-pattern)

## When development activities don't apply

Some genres make some of these activities optional:

- **Fiction without thematic argument** — `_argument.md` is optional; ARGUMENT-AUDIT is rare. Reader atoms still apply (a beta reader of literary fiction is doing READER-SIMULATION informally).
- **Screenplay / play** — `_argument.md` is unusual; STEELMAN may apply if there's a politically-charged subject. READER-SIMULATION applies (audiences vary; a play for repertory theater has different readers than one for Broadway).
- **Dissertation** — every activity applies, often more rigorously than for trade non-fiction. CLAIM-EVIDENCE-CHECK is essential. STEELMAN is the literature-review chapter's central discipline.

The activity table in chapter 03 is the source of truth for which activities are universal vs. genre-conditional.
