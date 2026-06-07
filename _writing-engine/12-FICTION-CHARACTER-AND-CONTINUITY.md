---
type: writing-engine
role: fiction-character-continuity
scope: fiction-screenplay-play
updated: 2026-06-02
lfw_load:
  tier: pack
  genres: [fiction, screenplay, play]
  activities: [CHARACTER-CONSISTENCY, CONTINUITY-CHECK, WORLDBUILDING, READER-SIMULATION]
  phase: on-demand
---

# 12 — FICTION CHARACTER AND CONTINUITY

> **Chapter 11 covered fiction's causal spine and the setup/payoff ledger. This chapter covers the three remaining fiction-specific gaps the engine had: the Character Item that never gets checked against the prose, the absence of a Thread analog for theme/motif, and the WORLDBUILDING activity that was generative but never verified itself against the draft. Plus the POV/psychic-distance craft module — the largest teachable fiction skill the engine ignored.**

## Why this chapter exists

Three persistent fiction failure modes the engine couldn't see:

1. **The Character bible doesn't reach the page.** A character has a gorgeous arc in their Item file and a flat one in the chapters. Voice on the page contradicts the voice declared in the Item. The stated want never operates as fuel in any scene. The arc is asserted ("she finally understood") rather than earned (shown to the reader through the steps that produced the change).
2. **Theme and motif live in the writer's head, accidentally on the page.** Non-fiction got Thread to track recurring arguments; fiction got nothing equivalent for image systems, recurring objects, thematic patterns. Theme that's stated is a lecture; theme that's woven is craft. You can only weave deliberately what you can see.
3. **Worldbuilding is fun and generative; continuity is hard and ignored.** WORLDBUILDING in v1.0 was a generative activity — invent a world. The actually-difficult fiction work is verifying that scene 31 doesn't contradict the magic rule established in scene 4, that timelines hold across hundreds of pages, and (load-bearing for any plot with secrets, which is most plots) that the who-knows-what state is consistent.

This chapter adds the artifacts and activities for all three. Plus the POV/psychic-distance craft module — the most teachable prose-level fiction skill the v1.0–v1.1 engine ignored.

## Part one — CHARACTER-CONSISTENCY activity

### What it is

A diagnostic that reads drafted prose for a specific Character and tests four questions:

1. **Want delivery** — does the want stated in the Character Item's `## Arc` section operate as fuel in the prose? If the Character Item says "Maya wants her sister's recognition," does that want push behavior visibly in the scenes Maya appears in?
2. **Voice consistency** — does the dialogue and POV-prose for this Character match the voice declared in `## Voice and Manner`? Or has voice drifted across chapters (often unconsciously — voice drift is the most common fiction-craft regression after head-hopping).
3. **Arc earned or asserted** — when the prose claims a character change ("she finally understood," "he stopped fighting it"), are the steps that produce the change shown in the prose, or is the change declared without dramatization?
4. **Antagonist steelman** — for antagonists specifically: is the antagonist's want as strong and as legitimate-feeling as the protagonist's? A weak antagonist (one whose want is flimsy, whose opposition is plot-mechanical rather than character-driven) is the most reliable cause of weak fiction.

### Trigger conditions

- A Character Item is at `established` status
- The Character has appeared in 3+ drafted Scenes
- CHARACTER-CONSISTENCY hasn't been run on this Character since the last batch of Scenes were drafted
- Writer flags CHARACTER-CONSISTENCY explicitly
- Antagonist sub-check: the Character has `lfw_role: antagonist` and hasn't been steelmanned

### Protocol

1. AI reads the target Character Item in full
2. AI reads every Scene Item where the Character has `lfw_characters_present` (or appears in body)
3. AI reads the surrounding Chapter context
4. AI tests:
   - Want delivery — quote evidence from the prose; note absences
   - Voice consistency — sample dialogue / interiority across multiple scenes; flag drift
   - Arc earned — for each claimed change, locate the dramatized steps in the prose; flag asserted-only changes
   - For antagonist: steelman the antagonist's position; ask whether a sophisticated reader would find the want legitimate within the character's own frame
5. AI produces a report:
   - **Want delivery** — evidenced / partial / absent, with citations
   - **Voice consistency** — consistent / drifting, with specific drift markers
   - **Arc earned** — earned / asserted / mixed, with the specific assertions flagged
   - **Antagonist steelman** (if applicable) — strong / weak, with the steelman articulated
6. Writer revises in subsequent REVISE sessions (or doesn't, with reason)

### Discipline

The AI does NOT rewrite character dialogue or interiority to "fix" inconsistencies. The Character Item may be the thing that's wrong (sometimes the writer's understanding of the character has evolved past the Item and the Item needs updating; sometimes the drafted prose is more honest than the planned Item). The AI surfaces; the writer judges which side is right.

### Failure modes this catches

**F24 — character-bible-disconnected-from-prose.** The Item and the prose drift apart silently.

**F25 — arc-asserted-not-earned.** The novel claims a change the prose hasn't dramatized.

**F26 — antagonist-weak-unflagged.** The protagonist's opposition is mechanical rather than character-driven, and the writer hasn't surfaced the problem.

### When Character-Bible Items are present *(v1.3.1)*

If the Character Item has `lfw_character_bible` populated and the Bible Item exists, CHARACTER-CONSISTENCY reads the Bible in full as part of the activity. The audit then can:

- Test the prose against the Bible's deep backstory, contradictions, and arc-across-manuscript (not just against the Character Item's surface)
- Surface drift between Bible and prose (e.g., a habit declared in the Bible that hasn't surfaced in any drafted scene, suggesting the prose is forgetting the character)
- Surface drift between Character Item and Bible (the Character Item may be ahead of the Bible, or vice versa)

The Character-Bible's structure and discipline are defined in chapter 14 §3. CHARACTER-CONSISTENCY is the primary consumer of the Bible — most other activities read only the Character Item's surface.

## Part two — Motif Item: fiction's Thread analog

### What it is

A Motif is fiction's first-class Item for tracking a recurring sub-surface element — a theme, an image system, a recurring object, a repeating gesture, an idea that surfaces across scenes and chapters. It is the structural equivalent of non-fiction's Thread Item.

Non-fiction's recurring argumentative through-lines have somewhere to live (Threads). Fiction's recurring thematic through-lines (until this release) had nowhere, so they stayed accidental. The Motif Item changes that.

### Frontmatter

```yaml
Item_Prototype: LFW_Motif
Item_ID: "<lowercase-kebab-slug>"
Title: "<Motif name>"
lfw_manuscript: <manuscript-slug>
lfw_atom_type: motif
lfw_kind: image-system | recurring-object | thematic-pattern | gesture | symbol | sound
lfw_status: latent | emerging | woven | resolved
lfw_priority: primary | secondary
lfw_scenes_present: []
Date_Added:
Date_Modified:
Needs_Processing: false
```

### Required body sections

1. `# <Motif name>`
2. `## What this motif is` — what the recurring element is and what it carries (image, idea, association). Brief — one or two paragraphs.
3. `## Where it appears` — wiki-links to Scene Items where this motif surfaces, with a one-line note on what it does in that scene
4. `## What it builds toward` — does the motif accumulate meaning across appearances, or does it just repeat? If accumulating, what's the trajectory?
5. `## Risk of over-use` — does the motif risk becoming heavy-handed if it appears too often, or in too obvious a context? The writer's own awareness of where the line is.
6. `## Notes` — anything else (sources of the motif in the writer's reading; alternate versions considered; whether it's deliberate or emerged)

### Naming and location

- **Naming:** `<Motif-Name>.md`. E.g., `Cold-as-Inheritance.md`, `Vine-and-Blood.md`, `The-Empty-Chair.md`.
- **Location:** `Items/Motifs/`.

### Status lifecycle

- **latent** — the writer has identified the motif but hasn't planted it in the draft yet
- **emerging** — the motif has appeared in 1–2 scenes; pattern is forming
- **woven** — the motif appears across multiple scenes/chapters in a clear pattern that builds
- **resolved** — the motif has reached its terminal moment (the motif's final appearance, where it pays off or recedes)

### Recommended motif count

Most novels have 2–5 motifs operating across the manuscript. Fewer is usually fine. More than 7 tends to dilute — readers can hold maybe five recurring sub-surface elements before the motif system becomes noise.

The writer can decide which patterns are deliberate motifs and which are background. The Motif Item is opt-in; an undocumented recurring image is just a recurring image, not a Motif.

### Failure mode this catches

**F27 — motif-stated-not-woven.** The writer says the motif is operating; the prose only shows the motif twice in 80,000 words; nothing builds.

## Part three — `_continuity.md`: the verification backbone

### What it is

`_continuity.md` is the fiction backbone file for tracking three kinds of continuity:

1. **World-rule continuity** — for genre fiction with worldbuilding (fantasy, science fiction, alternate history, magical realism): does scene 31 contradict the magic rule established in scene 4? Does the established cosmology hold?
2. **Timeline continuity** — across hundreds of pages, does the order of events stay consistent? Did Tuesday actually come after Monday in this chapter and last chapter? Is the character the same age at scene 17 as they should be given scene 3?
3. **Information-state continuity (who-knows-what ledger)** — load-bearing for any plot with secrets. At each scene, what does each character know? What do they not know? When does the reveal happen, and is the reveal consistent with what scene 14 implied?

The third is the most important and the most ignored. A novel with even minor information-state drift is unreadable; a novel with rigorous information-state tracking creates the dramatic-irony moments that make plot-driven fiction work.

### Required sections of `_continuity.md`

1. **World rules** — for cartridges with worldbuilding: enumerated rules about how the world works. Each rule has a citation to the scene where it's established. Updated when a new rule is introduced; checked when scenes reference relevant mechanics.
2. **Timeline** — explicit chronology of in-story events. Dated or sequenced. Critical for novels covering long spans or with non-chronological narration.
3. **Information-state ledger** — for each load-bearing piece of information (a secret, a hidden identity, a plot-relevant fact), a table tracking: who introduced it, who knows it as of each scene, who learns it when, and when (if) the reader learns it. The reader can be tracked as a "character" in this ledger.
4. **Continuity check log** — append-only record of CONTINUITY-CHECK sessions: what was checked, what issues were found, what was resolved.

### When `_continuity.md` is required

- **Genre fiction with worldbuilding** — required (fantasy, SF, alternate history, magical realism)
- **Plot-driven fiction with secrets** — required (mystery, thriller, literary fiction with reveals)
- **Long-form fiction** — recommended (any novel of >50,000 words benefits)
- **Vignette collections, short-story collections, flash** — usually not needed
- **Screenplay** — required (every screenplay has continuity demands)
- **Play** — depends; smaller-scope plays often don't need it

## Part four — CONTINUITY-CHECK activity

### What it is

A verification activity that reads drafted prose against `_continuity.md` and flags inconsistencies. The dedicated counterpart to WORLDBUILDING (which remains generative).

### Trigger conditions

- A new Scene has been drafted that references world-rules, timeline, or information-state items in the ledger
- 10+ scenes have been drafted since last CONTINUITY-CHECK
- A new world rule was added but the writer hasn't checked prior scenes for compliance
- Before any READ-THROUGH at chapter or book scale

### Protocol

1. AI reads `_continuity.md` in full
2. AI reads the target Scene(s) — usually the most recent batch of drafted scenes
3. AI tests each item in the ledger against the target scenes:
   - **World rules**: does the scene violate or strain any established rule?
   - **Timeline**: does the scene's stated time-position fit with established chronology?
   - **Information-state**: does each character behave consistently with what they know at this point? Do they act on information they shouldn't have yet, or fail to act on information they should have?
4. AI produces a report:
   - **Rule violations** — specific scene + which rule
   - **Timeline issues** — specific contradictions
   - **Information-state slips** — characters acting outside their knowledge state
   - **New continuity items the scene introduces** — propose additions to `_continuity.md`
5. Writer decides whether the scene needs revision, whether the rule needs revision, or whether the apparent inconsistency is actually intentional (e.g., a character lying about what they know is a violation of the surface ledger but consistent with deeper tracking)

### Discipline

The AI does NOT silently revise prose to fix continuity. Continuity is the writer's call. The AI surfaces; the writer judges. Sometimes the right answer is "the world rule was always wrong; revise the rule and propagate." Sometimes it's "scene 31 needs rewriting." The AI presents options, not edicts.

### Failure modes this catches

**F28 — continuity-drift.** World-rule violations, timeline contradictions, information-state slips that the writer can't see because they hold the whole novel in their head and forget where each piece was last touched.

## Part five — WORLDBUILDING activity (extended for v1.2)

WORLDBUILDING remains the engine's generative activity for fiction worldbuilding work: creating settings, magic systems, alternate-history rules, fictional cultures. It is **not duplicated** by CONTINUITY-CHECK — the two are complementary:

- **WORLDBUILDING** generates new world elements; populates Setting Items and the world-rules section of `_continuity.md`
- **CONTINUITY-CHECK** verifies drafted prose against the world elements WORLDBUILDING populated

A typical fiction cartridge will have WORLDBUILDING sessions early (when the world is being built) and CONTINUITY-CHECK sessions throughout the drafting phase (as scenes accumulate against the established world).

The engine's slight v1.2 update to WORLDBUILDING: at the end of every WORLDBUILDING session, propose updating `_continuity.md` with any new rules introduced. This closes the loop between generation and verification.

## Part six — Fiction READER-SIMULATION reframe

The READER-SIMULATION activity defined in chapter 10-READER was framed around non-fiction reader experience: resistance, lost threads, curse of knowledge. For fiction, the questions are different and arguably more important:

### Fiction reader-simulation questions

1. **Is the dramatic question alive on this page?** Does the reader still feel "I need to find out whether [X]"? Or has the page lost the question?
2. **Where does the page-turn impulse die?** Specific sentences or paragraphs where a fiction reader would set the book down.
3. **Do we still care about this character right now?** Sympathy / interest tracking — a character we cared about in chapter 3 may have lost the reader by chapter 17 through accumulated bad behavior or just by being off-page too long.
4. **Does the climax land the feeling it's reaching for?** For climactic scenes specifically — does the emotional payoff match the setup, or does it underperform? Underperformed climaxes are usually invisible to the writer (curse-of-knowledge: you feel the climax because you know what you meant) and visible to a fresh reader.

### Fiction reader-want/fear/hope tracking

For fiction READER-SIMULATION, the Reader Item takes on an additional dimension: the **reader's want/fear/hope through the manuscript**. What does the reader want to happen? What do they fear? What do they hope for? These shift across the manuscript as the story unfolds.

The AI can track the reader's want/fear/hope as a line through the manuscript and simulate where that line goes flat (emotional flatline) or where it dips (loss of stakes) or where it builds (good tension). The flatline is the killer — fiction that doesn't track the reader's emotional state cannot diagnose it.

### Fiction protocol modification

When running READER-SIMULATION on a fiction cartridge:

1. AI reads the Reader Item (as always)
2. AI reads the Reader Item's `## Want/fear/hope at this point` section (fiction-specific, added by the writer for fiction-priority Readers)
3. AI reads the target Scene/Chapter
4. AI tests the four fiction-specific questions above
5. AI produces a fiction-flavored report: dramatic-question status, page-turn-impulse map, sympathy/interest level, emotional-flatline locations
6. Writer revises in subsequent REVISE sessions

The chapter-10 protocol still applies; this is an extension, not a replacement.

## Part seven — `pov-and-psychic-distance` craft module

The opt-in craft module added in v1.2. The most teachable prose-level fiction skill the v1.0–v1.1 engine ignored.

### What it flags

When invoked on a REVISE or READ-THROUGH pass:

- **Psychic distance shifts** — the zoom from distant narration ("It was a small town") to deep interiority ("The wallpaper smelled exactly like her grandmother's house, and Maya felt the old hatred wake up"). Good fiction modulates psychic distance deliberately; bad fiction wobbles between zoom levels without intention.
- **Head-hopping within a scene** — the POV character should be consistent within any single scene (with limited, deliberate exceptions in omniscient narration). Mid-scene POV switches are usually unintentional and disorient the reader.
- **Filter words** — the words that put a pane of glass between the reader and the experience: *she saw, he felt, she noticed, he heard, she realized, he wondered, she thought.* Sometimes filter words are correct (when the act of noticing is itself the point). Usually they're a craft tell — *she saw the dog* should usually be *the dog* (in deep POV) or *the dog was there* (in distant POV). The filter word is rarely the right choice.

### How it works

Same as other craft modules (chapter 09): on-demand, invoked by the writer for a specific REVISE or READ-THROUGH pass. The AI scans the target Items and produces a list of candidates. Writer decides which to revise.

The module is opt-in because filter-word density and psychic-distance choices are voice-load-bearing. A writer whose voice depends on careful filter-word use should not have them silently flagged on every drafted section. They surface only when the writer asks.

### Failure mode this catches

**F29 — pov-pane-of-glass.** Filter-word density that distances the reader from the experience without intention.

**F30 — head-hop-within-scene.** Unintentional POV switches inside scenes.

## Part eight — Fiction error vocabulary (for the craft-log)

The v1.1 craft-log discipline tracks recurring patterns in the writer's prose. For fiction cartridges, the patterns the AI watches for are:

- **scene-doesn't-turn** (F22) — recurring no-turn scenes
- **and-then-not-but-therefore** — recurring causal-chain slack
- **arc-asserted-not-earned** (F25) — recurring undramatized character changes
- **antagonist-mechanical** (F26) — recurring weak-antagonist patterns
- **motif-stated-not-woven** (F27) — themes named but not built across the prose
- **continuity-slip** (F28) — recurring world-rule or information-state drift
- **filter-word-density** (F29) — recurring pane-of-glass patterns
- **head-hop-within-scene** (F30) — recurring POV slips
- **telling-not-showing** — the canonical fiction-craft failure

Each pattern, when observed 3+ times, becomes a craft-log entry per the chapter-09 discipline. Each pattern that appears in 3+ cartridges graduates to `_craft-profile.md`.

## When this chapter applies and when it relaxes

This chapter assumes plot-driven, character-driven fiction. Form variations:

- **Literary fiction without conventional plot** — CHARACTER-CONSISTENCY applies; CONTINUITY-CHECK applies (timeline, who-knows-what); Motif Items are likely heavily used; SETUP-PAYOFF-AUDIT may be lighter
- **Genre fiction** — every part of this chapter applies more rigorously; readers in genre fiction punish unfulfilled promises and inconsistent characters more
- **Experimental fiction** — Character may apply or not depending on the form; the writer judges
- **Short stories / flash** — usually too short for this chapter's machinery to earn its keep; the form contains its own discipline

## How this chapter interacts with the rest of the engine

- **Chapter 03 (Cadence and Sessions)** — adds CHARACTER-CONSISTENCY and CONTINUITY-CHECK to the activity table (4 new fiction activities total with chapter 11's contributions; 20 universal activities)
- **Chapter 04 (Items and Structure)** — Motif documented as a new first-class Item; `_continuity.md` added to backbone files
- **Chapter 05 (Voice and Craft)** — POV craft module cross-referenced
- **Chapter 06 (Research Integration)** — generally not applicable to fiction; some research-informed fiction uses Sources
- **Chapter 07 (Revision Discipline)** — CHARACTER-CONSISTENCY and CONTINUITY-CHECK findings feed into revision passes
- **Chapter 09 (Writer Development)** — fiction error vocabulary added to the craft-log discipline; POV module added to the craft-module list
- **Chapter 10-READER** — Readers are extended with fiction-specific want/fear/hope tracking
- **Chapter 11 (Fiction Plot and Spine)** — sister chapter; together they're the fiction-specific development layer
- **`_meta/FAILURE-MODES.md`** — adds F24–F30 (character-disconnected, arc-asserted, antagonist-weak, motif-not-woven, continuity-drift, pov-pane-of-glass, head-hop)

## Carry-over cautions (unchanged from v1.1)

- **Skill model is observational, not scored.** Fiction has even less quantifiable skill than non-fiction; no scores, no levels.
- **Craft work as procrastination.** A writer can hide from a hard chapter inside a SCENE-AUDIT or a CONTINUITY-CHECK or a CHARACTER-CONSISTENCY just as easily as inside RESEARCH-INTEGRATION or worldbuilding. The pattern is identical (F18); the surface is fiction-flavored.
- **Scaffolding fade matters MORE in fiction.** Invention is the central fiction skill. An AI that generates your plot turns and character moves doesn't make you a better novelist; it makes you a novelist who can't work without it. The v1.1 scaffolding-fade machinery applies with extra weight for fiction cartridges. Default for fiction cartridges should typically be `gradual-fade` or `socratic`; `full` indefinitely is the highest-risk mode for fiction.
