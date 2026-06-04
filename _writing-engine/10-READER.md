---
type: writing-engine
role: reader-audience-modeling
scope: subject-agnostic
updated: 2026-06-03
lfw_load:
  tier: core
  genres: [all]
  activities: [READER-SIMULATION, CRAFT-REVIEW]
  phase: on-demand
---

# 10 — READER (Audience Modeling)

> **Audience modeling serves every genre — fiction needs reader-experience modeling as much as non-fiction needs reader-resistance modeling. This chapter introduces the Reader as a first-class concern and defines the two activities (READER-SIMULATION, CRAFT-REVIEW) that depend on modeled audiences. The argument-as-backbone material lives in `10-ARGUMENT.md` (non-fiction pack).**

## Why this chapter exists

One of the most common failure modes across genres is upstream of structure and style:

**The reader evaporates.** The manuscript manifest asks "who is this for" once at bootstrap, and then the audience model disappears. The writer drifts; the prose drifts; what felt clear at the breakfast-table-conversation level becomes opaque to anyone who isn't already in the writer's head. Curse of knowledge is one specific form; there are others.

Chapter 04 (Atoms and Structure) gave us containers. This chapter gives us *the reader as an entity the AI can model.*

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

## Part two — Activities that consume Reader atoms

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

**Fiction reframe:** chapter 12 §6 extends READER-SIMULATION with fiction-specific protocol (dramatic-question, page-turn-impulse, emotional-flatline detection). Fiction cartridges load both this chapter and chapter 12 for READER-SIMULATION.

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

## How this chapter interacts with the rest of the engine

- **Chapter 03 (Cadence and Sessions)** — READER-SIMULATION and CRAFT-REVIEW are entries in the universal activity table
- **Chapter 04 (Atoms and Structure)** — Reader is added as a first-class atom
- **Chapter 09 (Writer Development)** — defines the craft-profile and craft-log artifacts that CRAFT-REVIEW uses; this chapter is when, that chapter is what
- **Chapter 10 (Argument)** — the companion non-fiction-pack chapter; READER-SIMULATION often runs alongside argument-pressure activities for non-fiction cartridges
- **Chapter 12 (Fiction Character and Continuity)** — §6 extends READER-SIMULATION with fiction-specific protocol
- **`_meta/FAILURE-MODES.md`** — adds craft-as-procrastination (also addresses reader-simulation-as-procrastination — a variant of the same anti-pattern)

## When Reader activities don't apply

- **Fiction without identifiable audience target** — Reader atoms may be lightly used; READER-SIMULATION still applies (a beta reader of literary fiction is doing READER-SIMULATION informally) but the set may be smaller
- **Screenplay / play** — READER-SIMULATION applies (audiences vary; a play for repertory theater has different readers than one for Broadway); the Reader atoms may model audience archetypes rather than individual reader-archetypes

The activity table in chapter 03 is the source of truth for which activities are universal vs. genre-conditional.
