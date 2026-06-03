---
type: writing-engine
role: atom-definitions
scope: subject-agnostic
updated: 2026-06-02
---

# 04 — ATOMS AND STRUCTURE

> **The atom-type definitions, relationship vocabulary, and composition rules that hold across all genres. Per-genre emphasis lives in chapter 02; this chapter is the underlying schema.**

## What an atom is

An atom is the smallest reusable, referenceable unit of a manuscript. Atoms have frontmatter, structured body sections, and named relationships to other atoms. They are stored as individual markdown files in the cartridge's `Atoms/` subfolders.

The fourteen atom types in LFW v1.3.1:

| Type | Role | Genre relevance |
|------|------|-----------------|
| **Beat** | Smallest dramatic or rhetorical move; optional Subtext body section *(v1.3.1)* | All genres |
| **Scene** | Composed of beats; prose lives here (fiction, screenplay, play); value-shift *(v1.2)* + optional scene-type *(v1.3.1)* | Fiction / screenplay / play |
| **Section** | Composed of beats; prose lives here (non-fiction, dissertation) | Non-fiction / dissertation |
| **Chapter** | Composes scenes or sections | Fiction / non-fiction / dissertation |
| **Act** | Composes scenes (screenplay/play equivalent of Chapter) | Screenplay / play |
| **Setting** | Location, period, and stage-condition record | Play (primary); fiction / screenplay (optional) |
| **Character** | Recurring participant; v1.3.1 adds POV-voice-register and dialogue-tells | Fiction / screenplay / play |
| **Character-Bible** *(v1.3.1)* | Extended companion to Character for POV-bearing, antagonist, and major-supporting characters | Fiction / screenplay / play |
| **Reader** | Modeled audience member; used in READER-SIMULATION | Non-fiction (primary) / dissertation / fiction (extended in chapter 12) |
| **Motif** *(v1.2)* | Recurring sub-surface image, object, gesture, symbol, sound | Fiction (primary) / screenplay / play |
| **Theme** *(v1.3.1)* | Abstract idea the manuscript is about; carried not declared | Fiction (primary) / screenplay / play / memoir |
| **Thread** | Recurring topic / argument / framing device | Non-fiction / dissertation |
| **Source** | External material informing the work | Non-fiction / dissertation (heavy); fiction (light) |
| **Note** | Unplaced fragment, idea, future inclusion | All genres |

Plus the cartridge backbone files (`_manuscript-manifest.md`, `_state.md`, `_outline.md`, `_voice-samples.md`, `_argument.md`, `_craft-log.md`, `_spine.md`, `_continuity.md`, `_promises.md`) which are not atoms but structural files that organize them. See "Cartridge backbone files" near the end of this chapter.

## Universal status enum (load-bearing)

Every prose-bearing atom (Beat, Scene, Section, Chapter, Act) uses **one** canonical lifecycle:

```
planned → drafting → drafted → revising → revised → final
```

Non-fiction and dissertation **Section** atoms add one optional value, `fact-checked`, between `revised` and `final`:

```
planned → drafting → drafted → revising → revised → fact-checked → final
```

These are the **only** legal `lfw_status` values for prose-bearing atoms. Templates and validators enforce this. Older drafts of the engine had Chapter-specific values (`outlined`); these are deprecated. Use `planned` for "outline not yet done" and `drafting` for "outline done, prose in progress."

Other atom types use type-specific lifecycle fields, NOT `lfw_status`:

| Atom type | Lifecycle field | Legal values |
|-----------|-----------------|--------------|
| Beat / Scene / Section / Chapter / Act | `lfw_status` | `planned`, `drafting`, `drafted`, `revising`, `revised`, `final` (+ `fact-checked` for non-fiction Section) |
| Character | `lfw_status` | `developing`, `established`, `revised`, `final` |
| Character-Bible *(v1.3.1)* | `lfw_status` | `drafting`, `established`, `revised`, `final` |
| Reader | `lfw_status` | `developing`, `active`, `retired` |
| Motif | `lfw_status` | `latent`, `emerging`, `woven`, `resolved` |
| Theme *(v1.3.1)* | `lfw_status` | `candidate`, `developing`, `threaded`, `resolved` |
| Thread | `lfw_status` | `emerging`, `active`, `concluded` |
| Source | `lfw_status` | `identified`, `ingested`, `folded-in`, `superseded` |
| Setting | `lfw_status` | `sketched`, `defined`, `final` |
| Note | `lfw_status` | `unplaced`, `placed`, `discarded` |

## Naming conventions and wiki-links

Wiki-links in atom bodies (`[[Foo]]`) target the **filename without the `.md` extension**. There is no other link resolution mechanism. The validator enforces that every wiki-link resolves to an actual file.

This forces a **disciplined naming convention**, because a flat folder (`Atoms/Sections/`) collects sections from every chapter and order-only names (`01-Opening.md`) collide globally. Canonical names below.

### Filename conventions per atom type

| Atom type | Naming pattern | Example | Folder |
|-----------|---------------|---------|--------|
| Beat | `<chapter>-<section-or-scene>-Beat-<order>-<short-slug>.md` | `03-01-Beat-01-Arrival.md` | `Atoms/Beats/` |
| Scene | `<chapter>-<order>-<short-slug>.md` (chapter-prefixed) | `04-03-Library-Confrontation.md` | `Atoms/Scenes/` |
| Section | `<chapter>-<order>-<short-slug>.md` (chapter-prefixed) | `03-01-Hoshi-Opening.md` | `Atoms/Sections/` |
| Chapter | `Chapter-<NN>-<short-title>.md` | `Chapter-03-Family-Business-Persistence.md` | `Atoms/Chapters/` |
| Act | `Act-<N>-<short-title>.md` | `Act-2-The-Reversal.md` | `Atoms/Acts/` |
| Character | `<First-Last>.md` or `<Slug>.md` | `Maya-Chen.md` | `Atoms/Characters/` |
| Character-Bible *(v1.3.1)* | `<First-Last>.md` (mirrors Character filename) | `Maya-Chen.md` | `Atoms/Character-Bibles/` |
| Reader | `<Reader-Slug>.md` (Title-Case-Hyphenated) | `Skeptic.md`, `Impatient-Generalist.md` | `Atoms/Readers/` |
| Motif | `<Motif-Name>.md` (Title-Case-Hyphenated) | `Cold-as-Inheritance.md`, `The-Empty-Chair.md` | `Atoms/Motifs/` |
| Theme *(v1.3.1)* | `<Theme-Name>.md` (Title-Case-Hyphenated) | `Honesty-Under-Cost.md` | `Atoms/Themes/` |
| Thread | `<Thread-Name>.md` (Title-Case-Hyphenated) | `Distributed-Legitimacy.md` | `Atoms/Threads/` |
| Source | `<Lastname>-<Short-Title>-<Year>.md` | `Beard-SPQR-2015.md` | `Atoms/Sources/` |
| Setting | `<Setting-Name>.md` | `The-Conservatory.md` | `Atoms/Settings/` |
| Note | `<YYYY-MM-DD>-<short-slug>.md` | `2026-06-02-bell-curve-observation.md` | `Atoms/Notes/` |

**Canonicalization rules:**

- For a given Source, pick **one** canonical name (typically last-name + short title + year). All wiki-links use that name. Multiple variants (`[[Beard-SPQR-2015]]` and `[[Mary-Beard-SPQR-2015]]` for the same source) are link-graph corruption.
- Chapter-prefixing is non-negotiable for Sections, Scenes, and Beats. Order-only naming (`01-Opening`) collides across chapters in a flat folder.
- Filenames are case-sensitive in the link graph; pick a case convention per cartridge and stay consistent.

### Item_ID is a SEPARATE namespace from filenames

Every atom has both:

- A **filename** (e.g., `Beard-SPQR-2015.md`) — case-sensitive Title-Case-Hyphenated; used as the wiki-link target
- An **`Item_ID`** in frontmatter (e.g., `beard-spqr-2015`) — lowercase-kebab; used for data queries (Obsidian Bases, external scripts, citation graphs)

These two namespaces serve different purposes and should not be conflated:

- **Wiki-links** in atom bodies always use the filename form, never the Item_ID
- **Data queries** that walk frontmatter use the Item_ID
- **Renaming the file** does not automatically change the Item_ID, and vice versa — both are stable identifiers in their respective domains

Older drafts of this engine ambiguously suggested wiki-links could use Item_IDs. They cannot. Filenames are the link key. Period.

## Beat

The smallest unit. A beat is a single move — a turn in argument, a moment of action, a line of dialogue that does work, a sentence that lands.

**Frontmatter:**

```yaml
Item_Prototype: LFW_Beat
Item_ID: "<lowercase-kebab-slug>"
Title: "<short descriptive name>"
lfw_manuscript: <manuscript-slug>
lfw_atom_type: beat
lfw_status: planned   # planned | drafting | drafted | revising | revised | final
lfw_parent: "[[<chapter-prefixed-section-or-scene-filename>]]"
lfw_order_in_parent: <int>     # 1, 2, 3, ... within the parent scene/section
lfw_characters_present: []     # for fiction/screenplay/play
lfw_threads_engaged: []        # for non-fiction/dissertation
lfw_first_drafted: <YYYY-MM-DD | null>
lfw_word_count: <int>
Date_Added:
Date_Modified:
Needs_Processing: false
```

**Required sections:**

1. `# <Beat name>`
2. `## Purpose` — what this beat accomplishes in the scene/section
3. `## Content` — the actual prose (when drafted) or planned content (when in outline)
4. `## Connects` — beats this follows from / leads to
5. `## Notes` — anything the writer wants to remember about this beat

**Naming:** `<chapter>-<section-or-scene-order>-Beat-<beat-order>-<short-slug>.md`. E.g., `03-01-Beat-01-Arrival.md` for Chapter 3, Section 1, Beat 1.

**Location:** `Atoms/Beats/` (flat folder; chapter-prefixing avoids collisions).

## Scene (fiction / screenplay / play)

A scene is a dramatic unit: typically continuous in time and place, with characters present and something happening that moves the story.

**Frontmatter:**

```yaml
Item_Prototype: LFW_Scene
Item_ID: "<lowercase-kebab-slug>"
Title: "<descriptive title>"
lfw_manuscript: <manuscript-slug>
lfw_atom_type: scene
lfw_status: planned   # planned | drafting | drafted | revising | revised | final
lfw_parent: "[[<chapter-or-act-filename>]]"
lfw_order_in_parent: <int>
lfw_setting: "<location/time>"
lfw_pov: "<character or narrator>"
lfw_characters_present: []
lfw_purpose: "<one-sentence: what this scene must do in the larger work>"
lfw_value_shift_from: ""    # v1.2: starting value-state (e.g., "safe", "hopeful", "ignorant")
lfw_value_shift_to: ""      # v1.2: ending value-state (must differ from `from` for the scene to turn)
lfw_scene_type: scene       # v1.3.1: scene (value-shifting, default) | sequel (reactive-processing) | scene-sequel (compound)
lfw_first_drafted: <YYYY-MM-DD | null>
lfw_word_count: <int>
Date_Added:
Date_Modified:
Needs_Processing: false
```

**Required sections:**

1. `# <Scene title>`
2. `## Setting and Stakes` — where, when, who, what's at stake
3. `## Value-shift` *(v1.2; for lfw_scene_type: scene or scene-sequel)* — start-state → end-state; whose want drives this scene; what's the conflict; what's different at the end (the SCENE-AUDIT discipline made structural; see chapter 11 §2)
4. `## Sequel` *(v1.3.1; for lfw_scene_type: sequel or scene-sequel)* — reaction → dilemma → decision; the decision IS the next scene's want (see chapter 14 §1 for the scene-and-sequel rhythm)
5. `## Beats` — ordered list of beats (with wiki-links to beat atoms)
6. `## Prose` — the drafted scene; or `*To be drafted*` if not yet
7. `## Connections` — what this scene sets up / pays off (the `prefigures` relation captures setups; see chapter 11 §3 for the SETUP-PAYOFF-AUDIT discipline)
8. `## Open Notes` — known weaknesses, alternate versions considered

**Naming:** `<chapter>-<order>-<short-slug>.md`. E.g., `04-03-Library-Confrontation.md` for Chapter 4, Scene 3.

**Location:** `Atoms/Scenes/`.

**v1.2 value-shift discipline:** A Scene whose `lfw_value_shift_from` and `lfw_value_shift_to` fields are identical (or both empty after the scene is drafted) has not turned. The SCENE-AUDIT activity (chapter 11) flags these. The most teachable fiction craft discipline the v1.0–v1.1 engine ignored.

## Section (non-fiction / dissertation)

A section is a unit of argument or narrative within a chapter. Roughly analogous to a "scene" in structural role but the conventions differ.

**Frontmatter:**

```yaml
Item_Prototype: LFW_Section
Item_ID: "<lowercase-kebab-slug>"
Title: "<section title>"
lfw_manuscript: <manuscript-slug>
lfw_atom_type: section
lfw_status: planned   # planned | drafting | drafted | revising | revised | fact-checked | final
lfw_parent: "[[<chapter-filename>]]"
lfw_order_in_parent: <int>
lfw_purpose: "<one-sentence: what this section argues or narrates>"
lfw_threads_engaged: []
lfw_sources_cited: []
lfw_first_drafted: <YYYY-MM-DD | null>
lfw_word_count: <int>
Date_Added:
Date_Modified:
Needs_Processing: false
```

**Required sections:**

1. `# <Section title>`
2. `## Purpose` — what this section is for in the chapter's argument or narrative
3. `## Beats` — ordered list of beats
4. `## Prose` — drafted content
5. `## Sources Used` — wiki-links to Source atoms
6. `## Threads Engaged` — wiki-links to Thread atoms
7. `## Open Notes` — weaknesses, fact-checks pending, alternate approaches

**Naming:** `<chapter>-<order>-<short-slug>.md`. E.g., `03-01-Hoshi-Opening.md` for Chapter 3, Section 1.

**Location:** `Atoms/Sections/`.

**Note:** `fact-checked` is a non-fiction / dissertation-only status value between `revised` and `final`. Fiction Section atoms (rare; most fiction uses Scenes) skip it.

## Chapter

A chapter is a composition of scenes or sections, usually with a coherent arc.

**Frontmatter:**

```yaml
Item_Prototype: LFW_Chapter
Item_ID: "<lowercase-kebab-slug>"
Title: "<chapter title>"
lfw_manuscript: <manuscript-slug>
lfw_atom_type: chapter
lfw_status: planned   # planned | drafting | drafted | revising | revised | final
lfw_parent: "[[<part-filename>]]"   # optional; some books have no parts
lfw_order_in_parent: <int>
lfw_word_count: <int>
lfw_target_word_count: <int>
lfw_first_drafted: <YYYY-MM-DD | null>
lfw_revisions_completed: <int>
Date_Added:
Date_Modified:
Needs_Processing: false
```

**Required sections:**

1. `# Chapter N: <title>`
2. `## Purpose` — what this chapter accomplishes in the book
3. `## Composition` — ordered list of scenes (fiction) or sections (non-fiction) with wiki-links
4. `## Open Notes` — chapter-level issues
5. `## Revision History` — log of revision passes that touched this chapter

**Naming:** `Chapter-<NN>-<short-title>.md`. E.g., `Chapter-03-Family-Business-Persistence.md`. Two-digit chapter numbers (`01`, `02`, ..., `10`, `11`) so files sort correctly in flat folders.

**Location:** `Atoms/Chapters/`.

## Act (screenplay / play)

Screenplay and play equivalent of Chapter. Composes scenes within an act structure.

**Frontmatter:**

```yaml
Item_Prototype: LFW_Act
Item_ID: "<lowercase-kebab-slug>"
Title: "Act <N>: <title>"
lfw_manuscript: <manuscript-slug>
lfw_atom_type: act
lfw_status: planned   # planned | drafting | drafted | revising | revised | final
lfw_order_in_parent: <int>
lfw_purpose: "<one sentence: what this act does in the larger work>"
lfw_target_page_count: <int>     # screenplay convention: pages ≈ minutes
lfw_first_drafted: <YYYY-MM-DD | null>
Date_Added:
Date_Modified:
Needs_Processing: false
```

**Required sections:**

1. `# Act <N>: <title>`
2. `## Purpose` — what this act accomplishes
3. `## Composition` — ordered list of scenes (wiki-links)
4. `## Open Notes` — act-level issues
5. `## Revision History`

**Naming:** `Act-<N>-<short-title>.md`. E.g., `Act-2-The-Reversal.md`.

**Location:** `Atoms/Acts/`.

## Setting (play; optional for fiction/screenplay)

Records a location, period, and stage-condition combination that scenes can reference. Play-primary; useful in fiction and screenplay when a setting recurs across multiple scenes with distinctive features worth preserving.

**Frontmatter:**

```yaml
Item_Prototype: LFW_Setting
Item_ID: "<lowercase-kebab-slug>"
Title: "<Setting name>"
lfw_manuscript: <manuscript-slug>
lfw_atom_type: setting
lfw_status: sketched   # sketched | defined | final
lfw_period: "<historical/narrative period>"
lfw_location: "<location>"
lfw_scenes_using: []   # auto-populated from Scene atoms
Date_Added:
Date_Modified:
Needs_Processing: false
```

**Required sections:**

1. `# <Setting name>`
2. `## Place and period` — where, when
3. `## Stage requirements` (plays) — set pieces, sightlines, entrances/exits
4. `## Sensory anchors` — what the audience/reader experiences
5. `## Scenes using this setting` — wiki-links to Scene atoms

**Naming:** `<Setting-Name>.md`. E.g., `The-Conservatory.md`.

**Location:** `Atoms/Settings/`.

## Reader (non-fiction primary; optional elsewhere)

A modeled audience member: what they bring to the page, what they reward, what they punish. Used by the **READER-SIMULATION** activity (chapter 10). For non-fiction the typical recommended set is three Readers — The Skeptic, The Impatient Generalist, The Domain Expert.

**Frontmatter:**

```yaml
Item_Prototype: LFW_Reader
Item_ID: "<lowercase-kebab-slug>"
Title: "<Reader name — short, descriptive>"
lfw_manuscript: <manuscript-slug>
lfw_atom_type: reader
lfw_status: developing   # developing | active | retired
lfw_priority: primary    # primary | secondary | tertiary
Date_Added:
Date_Modified:
Needs_Processing: false
```

**Required body sections:**

1. `# <Reader name>`
2. `## Who they are` — concrete sketch; one paragraph
3. `## Background they bring` — what they already know; basis for curse-of-knowledge detection
4. `## What they reward` — moves that land with this reader
5. `## What they punish` — moves that lose this reader
6. `## Where they resist` — places this reader is predisposed to push back
7. `## What they're patient with vs. impatient with`
8. `## Notes`

**Naming:** `<Reader-Slug>.md`. E.g., `Skeptic.md`, `Impatient-Generalist.md`, `The-Atlantic-Reader.md`.

**Location:** `Atoms/Readers/`.

See chapter 10 for the READER-SIMULATION activity that uses Reader atoms. Chapter 12 §6 extends READER-SIMULATION with fiction-specific protocol (dramatic-question, page-turn-impulse, emotional-flatline detection).

## Motif (fiction primary; optional for screenplay/play) *(v1.2)*

A recurring sub-surface element — theme, image system, recurring object, gesture, symbol, sound — that surfaces across scenes and builds (or fails to build) across the manuscript. Fiction's first-class atom for thematic through-lines. Structural equivalent to non-fiction's Thread.

**Frontmatter:**

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

**Required body sections:**

1. `# <Motif name>`
2. `## What this motif is` — what the recurring element is and what it carries; one or two paragraphs
3. `## Where it appears` — wiki-links to Scene atoms with a one-line note on what the motif does in each
4. `## What it builds toward` — accumulation pattern; does it gain meaning or just repeat?
5. `## Risk of over-use` — the writer's own awareness of when the motif becomes heavy-handed
6. `## Notes`

**Naming:** `<Motif-Name>.md`. E.g., `Cold-as-Inheritance.md`, `The-Empty-Chair.md`, `Vine-and-Blood.md`.

**Location:** `Atoms/Motifs/`.

See chapter 12 §2 for the full Motif discipline and the F27 (motif-stated-not-woven) failure mode.

## Character (fiction / screenplay / play)

Recurring participant. First-class atom.

**Frontmatter:**

```yaml
Item_Prototype: LFW_Character
Item_ID: "<slug>"
Title: "<character full name>"
lfw_manuscript: <manuscript-slug>
lfw_atom_type: character
lfw_role: protagonist | antagonist | major-supporting | minor | speaking | non-speaking
lfw_first_appearance: "[[Scene-slug]]"
lfw_scenes_present: []
lfw_status: developing | established | revised | final
lfw_pov_voice_register:        # v1.3.1: required for POV-bearing characters; optional otherwise
  sentence_length: ""          # "short" | "long" | "cadenced" | "fragmentary" | "varied"
  diction: ""                  # "plain" | "mixed" | "formal" | "register-shifting"
  interiority_mode: ""         # "observational" | "ruminating" | "kinetic" | "associative"
  tense_preference: ""         # "scene-tense" | "tense-slippage-into-memory" | "strict-scene-tense"
  signature_moves: []          # 2-4 prose patterns marking this POV
  avoid_moves: []              # patterns the OTHER POV uses that this POV must not
lfw_character_bible: ""        # v1.3.1: wikilink to extended Character-Bible atom if present
Date_Added:
Date_Modified:
Needs_Processing: false
```

**Required sections:**

1. `# <Character name>`
2. `## Role` — function in the story
3. `## Background` — relevant history before the story
4. `## Voice and Manner` — speech patterns, defining gestures, what they sound like
   - `### Dialogue tells` *(v1.3.1)* — sentence shape; diction range; pet phrases; verbal tics; what they say when they don't know what to say; what they say when lying; what they say under pressure (chapter 13 §1)
5. `## Subtext patterns` *(v1.3.1, optional)* — if the character habitually says-other-than-meant, what's the pattern?
6. `## Arc` — how this character changes (or doesn't) across the book
7. `## Relationships` — wiki-links to other characters with relationship type
8. `## Scenes Present` — wiki-links to scenes they appear in
9. `## Open Questions` — things about the character not yet decided

**Naming:** `<FirstName-LastName>.md` or `<Slug>.md`. E.g., `Maya-Chen.md`.

**Location:** `Atoms/Characters/`.

See chapter 13 for POV-voice-register discipline and the POV-VOICE-DRIFT activity.

## Character-Bible (fiction / screenplay / play) *(v1.3.1)*

The extended companion atom for POV-bearing characters, antagonists, and major supporting characters in long novels. Most secondary characters never get one. The Character atom captures function and arc; the Bible captures the depth that the prose draws on.

**Frontmatter:**

```yaml
Item_Prototype: LFW_Character_Bible
Item_ID: "<character-slug>-bible"
Title: "<Character Name> — Bible"
lfw_manuscript: <manuscript-slug>
lfw_atom_type: character-bible
lfw_status: drafting | established | revised | final
lfw_character: "[[<Character-filename>]]"
Date_Added:
Date_Modified:
Needs_Processing: false
```

**Body sections** (all optional; populate as the manuscript demands):

At-a-glance / Physical / Backstory (chronological) / Family-lineage-ancestry / Worldview / Habits and routines / Skills, knowledge, and competence / Wounds (deep) / Secrets / Contradictions / Arc across this manuscript / Relationships (per-relationship) / Voice (extended) / Sensory signatures / Notes-not-yet-decided

See `_writing-engine/_templates/TEMPLATE-Character-Bible.md` for the full structure and chapter 14 §3 for usage discipline.

**Naming:** `<First-Last>.md` mirroring the Character filename. E.g., a `Maya-Chen.md` Character has `Maya-Chen.md` Bible.

**Location:** `Atoms/Character-Bibles/` (separate folder; folder makes the bible/character distinction immediate).

**Operator-private by default** — gitignored in writers' own work; shipped in worked examples via `!Example-Project-*` override.

## Theme (fiction / memoir / narrative non-fiction) *(v1.3.1)*

The abstract idea the manuscript is *about*. Carried, not declared. Distinct from premise (the situation), distinct from motif (the recurring image), distinct from `_argument.md` (which is non-fiction's logical backbone where the argument is *declared* and *defended*).

**Frontmatter:**

```yaml
Item_Prototype: LFW_Theme
Item_ID: "<theme-slug>"
Title: "Theme — <Name>"
lfw_manuscript: <manuscript-slug>
lfw_atom_type: theme
lfw_status: candidate | developing | threaded | resolved
lfw_priority: central | secondary | incidental
lfw_appears_in_scenes: []
lfw_related_motifs: []
lfw_related_characters: []
Date_Added:
Date_Modified:
Needs_Processing: false
```

**Required body sections:**

1. `# Theme — <Name>`
2. `## What this theme is` — the abstract idea in plain words
3. `## Why this theme matters in this manuscript`
4. `## How it's carried (not declared)` — mechanisms: character / motif / plot-shape / dramatic question
5. `## Tension within the theme` — positions A and B; what the manuscript does with the tension
6. `## Where it surfaces (scene-by-scene)` — table of scenes + how the theme appears + which position carried
7. `## What it must NOT do` — guard against on-the-nose treatment
8. `## Audit notes` — THEME-CHECK findings logged here

**Naming:** `<Theme-Name>.md`. E.g., `Honesty-Under-Cost.md`.

**Location:** `Atoms/Themes/`.

See chapter 14 §4 for the full discipline and the THEME-CHECK activity.

## Thread (non-fiction / dissertation)

Recurring topic, argument, framing device, or analytical lens that spans sections and chapters.

**Frontmatter:**

```yaml
Item_Prototype: LFW_Thread
Item_ID: "<slug>"
Title: "<thread name>"
lfw_manuscript: <manuscript-slug>
lfw_atom_type: thread
lfw_kind: argument | counter-argument | framing | concept | recurring-example | methodology
lfw_status: emerging | active | concluded
lfw_sections_engaged: []
Date_Added:
Date_Modified:
Needs_Processing: false
```

**Required sections:**

1. `# <Thread name>`
2. `## What this thread is` — one or two paragraphs
3. `## Where it appears` — wiki-links to Section atoms that engage it
4. `## Sources that support it` — wiki-links to Source atoms
5. `## Sources that complicate or contradict it` — counter-evidence; for honest argumentation
6. `## Arc across the book` — how this thread develops from chapter to chapter
7. `## Open Notes` — unresolved aspects

**Naming:** `<Thread-Name>.md`. E.g., `Decline-vs-Transformation-Thesis.md`.

**Location:** `Atoms/Threads/`.

## Source

External material: books, papers, interviews, datasets, primary documents, videos, lectures.

**Frontmatter:**

```yaml
Item_Prototype: LFW_Source
Item_ID: "<slug>"
Title: "<source title>"
lfw_manuscript: <manuscript-slug>
lfw_atom_type: source
lfw_source_kind: book | paper | article | interview | dataset | primary-document | video | other
lfw_authors: []
lfw_year: <year>
lfw_publication: "<publisher / journal / venue>"
lfw_url: ""
lfw_status: identified | ingested | folded-in | superseded
lfw_relevance: high | medium | low
lfw_sections_citing: []
Date_Added:
Date_Modified:
Needs_Processing: false
```

**Required sections:**

1. `# <Source title>`
2. `## Citation` — full formatted citation in your manuscript's required style (Chicago, APA, MLA, etc.)
3. `## Why it matters here` — relevance to the manuscript's argument or narrative
4. `## Key claims / passages` — what to cite, paraphrase, or engage with (with page numbers / locations)
5. `## How to integrate` — notes on which sections this informs and how
6. `## Worries` — methodological concerns, contested findings, things to verify

**Naming:** `<Author-Lastname>-<Short-Title>-<Year>.md`. E.g., `Beard-SPQR-2015.md`.

**Location:** `Atoms/Sources/`.

## Note

Unplaced fragment, idea, future inclusion, possible scene, dialogue snippet, observation.

**Frontmatter:**

```yaml
Item_Prototype: LFW_Note
Item_ID: "<slug>"
Title: "<short label>"
lfw_manuscript: <manuscript-slug>
lfw_atom_type: note
lfw_kind: idea | fragment | dialogue | observation | research-lead | structural-thought
lfw_status: unplaced | placed | discarded
lfw_placed_at: "[[Section-or-Scene]]"   # if placed
Date_Added:
Date_Modified:
Needs_Processing: false
```

**Required sections:**

1. `# <Note title>`
2. `## Content` — the actual fragment / idea / observation
3. `## Origin` — where it came from (a real conversation, a moment of thought, a reading)
4. `## Possible homes` — places in the manuscript it might fit

**Naming:** `<YYYY-MM-DD>-<short-slug>.md`. E.g., `2026-06-02-bell-curve-observation.md`.

**Location:** `Atoms/Notes/`.

## Relationship vocabulary

Used in atom frontmatter and body wiki-links:

| Relation | Used between | Captured in |
|----------|--------------|-------------|
| `composed-of` | Chapter → Scene/Section | Chapter body's `## Composition` |
| `part-of` | Scene/Section → Chapter | Scene/Section frontmatter `lfw_parent` |
| `contains-beat` | Scene/Section → Beat | Scene/Section body's `## Beats` |
| `precedes` / `follows` | Atom ↔ Atom of same type | Sequence within parent |
| `appears-in` | Character → Scene | Character body's `## Scenes Present` |
| `cites` | Section → Source | Section body's `## Sources Used` |
| `engaged-in` | Section → Thread | Section body's `## Threads Engaged` |
| `supports` / `contradicts` | Source → Thread | Thread body |
| `prefigures` | Scene → Scene | Body, narrative payoff/setup |
| `parallels` | Atom ↔ Atom | Body, structural parallels |
| `relates-to` | Atom ↔ Atom | Body, free-form connection |

## Composition rules

- **Beats are atomic.** Do not nest beats inside beats.
- **A Scene/Section composes Beats** in a defined order (`lfw_order_in_parent`).
- **A Chapter composes Scenes (fiction) or Sections (non-fiction)** in a defined order.
- **Optionally, a Part composes Chapters.** Not required; many books have no parts.
- **Characters, Readers, and Threads are not composed into other atoms.** They're referenced (appears-in, engaged-in, simulated-by) but they don't have an "order in parent."
- **Sources and Notes are floating.** They reference things and are referenced by things, but they have no parent.

## Cartridge backbone files (not atoms)

In addition to the atoms above, every cartridge has a set of **backbone files** — structural markdown files at the cartridge root that organize the atoms and capture state, outline, argument, and development context. They are not atoms (no `lfw_atom_type` field) but they have their own prototypes and are first-class engine artifacts.

| File | Purpose | Required in | Defined in |
|------|---------|-------------|------------|
| `_manuscript-manifest.md` | The cartridge's manifest — what this manuscript is, genre, voice mode, scaffolding mode | All cartridges | Template + chapter 02 |
| `_state.md` | Single source of truth for current state, today's focus, atom-status snapshot | All cartridges | Template + chapter 03 |
| `_outline.md` | Container hierarchy (book → chapter → section/scene → beat) | All cartridges | Template + chapter 04 |
| `_voice-samples.md` | Voice-mode reference passages (only when voice mode is `voice-samples` or `voice-check-on-demand`) | Conditional | Template + chapter 05 |
| `_argument.md` | Argument backbone — thesis, sub-claims, evidence map, defeaters, honest unknown | **Required for non-fiction and dissertation**; optional for memoir/narrative non-fiction; not applicable to screenplay/play | Template + chapter 10 |
| `_spine.md` *(v1.2)* | Causal backbone — premise as causal claim, scene-by-scene value-shifts, but/therefore linkage, escalation curve | **Required for fiction, screenplay, play**; recommended for memoir/narrative non-fiction; not applicable to non-fiction/dissertation | Template + chapter 11 |
| `_continuity.md` *(v1.2)* | World-rule + timeline + information-state (who-knows-what) ledger | **Required for genre fiction with worldbuilding and any plot-driven fiction with secrets**; required for screenplay; recommended for long-form fiction | Template + chapter 12 |
| `_promises.md` *(v1.2)* | Setup/payoff ledger — promises planted, fired, outstanding, unsetup payoffs, retired | **Required for plot-driven fiction** (mystery, thriller, literary novel with subplot); required for screenplay/play; optional for non-plot literary fiction | Template + chapter 11 |
| `_craft-log.md` | Per-cartridge writer-pattern observations + practice focus | Optional (recommended for any serious project) | Template + chapter 09 |

The argument and craft-log backbones were added in v1.1. The spine, continuity, and promises backbones are v1.2 additions for fiction parity with non-fiction's development layer. All five are **development-layer** artifacts that pair with the **OV-root** craft-profile (chapter 09).

### The `prefigures` relation as discipline *(v1.2)*

The relationship vocabulary (below) includes `prefigures` for scene-to-scene foreshadowing. In v1.0–v1.1 this relation existed but had no discipline; in v1.2 it is the canonical mechanism for declaring promises in `_promises.md`. When the writer marks Scene A as `prefigures` Scene B, the SETUP-PAYOFF-AUDIT activity (chapter 11) treats this as a planted promise; when the corresponding payoff lands, the relation is exercised. See chapter 11 §3 for the protocol.

## Status field lifecycle (recap)

For prose-bearing atoms (Beat / Scene / Section / Chapter / Act), the canonical lifecycle is:

- **planned** → atom exists with frontmatter; outline (beats) may or may not exist yet; no prose
- **drafting** → outline is done; prose is being written but not yet complete
- **drafted** → first-pass prose is complete
- **revising** → a revision pass is currently touching this atom
- **revised** → at least one revision pass has completed on it
- **fact-checked** (non-fiction Section only) → accuracy pass completed
- **final** → marked finished by the writer

Non-prose atoms (Character, Thread, Source, Setting, Note) use type-specific status vocabularies — see the "Universal status enum" table earlier in this chapter.

## Atom file conventions

- **Markdown only.** No HTML, no special syntax that breaks in non-Obsidian editors.
- **YAML frontmatter required.** Every atom has it.
- **Wiki-style links** (`[[Atom-Name]]`) for cross-atom references.
- **Section headers must match the template.** The AI relies on these to find content.
- **Word counts** in frontmatter for Scenes/Sections/Chapters are best-effort estimates; not authoritative until the manuscript is assembled.

## When the writer wants to extend the schema

Extending the atom set requires:

1. A real need (a recurring concept that doesn't fit any existing atom type)
2. A template in `_writing-engine/_templates/` for the new atom
3. A note in the cartridge's `_manuscript-manifest.md` under `lfw_custom_atoms`
4. Consistent application (don't have the new atom only in one cartridge if the engine should know about it)

See `CONTRIBUTING.md` §1 for the in-scope contribution pattern.
