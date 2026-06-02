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

The eight atom types in LFW v1.0:

| Type | Role | Genre relevance |
|------|------|-----------------|
| **Beat** | Smallest dramatic or rhetorical move | All genres |
| **Scene** | Composed of beats; prose lives here (fiction, screenplay, play) | Fiction / screenplay / play |
| **Section** | Composed of beats; prose lives here (non-fiction, dissertation) | Non-fiction / dissertation |
| **Chapter** | Composes scenes or sections | All genres (sometimes absent) |
| **Character** | Recurring participant in fiction/screenplay/play | Fiction / screenplay / play |
| **Thread** | Recurring topic / argument / framing device | Non-fiction / dissertation |
| **Source** | External material informing the work | Non-fiction / dissertation (heavy); fiction (light) |
| **Note** | Unplaced fragment, idea, future inclusion | All genres |

Plus the cartridge backbone files (`_manuscript-manifest.md`, `_state.md`, `_outline.md`, `_voice-samples.md`) which are not atoms but structural files that organize them.

## Beat

The smallest unit. A beat is a single move — a turn in argument, a moment of action, a line of dialogue that does work, a sentence that lands.

**Frontmatter:**

```yaml
Item_Prototype: LFW_Beat
Item_ID: "<slug>"
Title: "<short descriptive name>"
lfw_manuscript: <manuscript-slug>
lfw_atom_type: beat
lfw_status: planned | drafted | revised | final
lfw_parent: "[[Section-or-Scene-slug]]"
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

**Naming:** `<order>-<short-slug>.md` within the parent. E.g., `01-Hook-Open.md`, `02-State-Premise.md`.

**Location:** `Atoms/Beats/` or nested under the parent — the cartridge's convention.

## Scene (fiction / screenplay / play)

A scene is a dramatic unit: typically continuous in time and place, with characters present and something happening that moves the story.

**Frontmatter:**

```yaml
Item_Prototype: LFW_Scene
Item_ID: "<slug>"
Title: "<descriptive title>"
lfw_manuscript: <manuscript-slug>
lfw_atom_type: scene
lfw_status: planned | drafted | revised | final
lfw_parent: "[[Chapter-or-Act-slug]]"
lfw_order_in_parent: <int>
lfw_setting: "<location/time>"
lfw_pov: "<character or narrator>"
lfw_characters_present: []
lfw_purpose: "<one-sentence: what this scene must do in the larger work>"
lfw_first_drafted: <YYYY-MM-DD | null>
lfw_word_count: <int>
Date_Added:
Date_Modified:
Needs_Processing: false
```

**Required sections:**

1. `# <Scene title>`
2. `## Setting and Stakes` — where, when, who, what's at stake
3. `## Beats` — ordered list of beats (with wiki-links to beat atoms)
4. `## Prose` — the drafted scene; or `*To be drafted*` if not yet
5. `## Connections` — what this scene sets up / pays off
6. `## Open Notes` — known weaknesses, alternate versions considered

**Naming:** `<order>-<short-slug>.md`. E.g., `03-Arrival-at-the-Door.md`.

**Location:** `Atoms/Scenes/`.

## Section (non-fiction / dissertation)

A section is a unit of argument or narrative within a chapter. Roughly analogous to a "scene" in structural role but the conventions differ.

**Frontmatter:**

```yaml
Item_Prototype: LFW_Section
Item_ID: "<slug>"
Title: "<section title>"
lfw_manuscript: <manuscript-slug>
lfw_atom_type: section
lfw_status: planned | drafted | revised | final | fact-checked
lfw_parent: "[[Chapter-slug]]"
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

**Naming:** `<order>-<short-slug>.md`. E.g., `02-The-Argument-Against-Decline.md`.

**Location:** `Atoms/Sections/`.

## Chapter

A chapter is a composition of scenes or sections, usually with a coherent arc.

**Frontmatter:**

```yaml
Item_Prototype: LFW_Chapter
Item_ID: "<slug>"
Title: "<chapter title>"
lfw_manuscript: <manuscript-slug>
lfw_atom_type: chapter
lfw_status: outlined | drafting | drafted | revising | revised | final
lfw_parent: "[[Part-slug]]"   # optional; some books have no parts
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

**Naming:** `Chapter-N-<short-title>.md`. E.g., `Chapter-03-The-Antarctic-Treaty-Case.md`.

**Location:** `Atoms/Chapters/`.

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
Date_Added:
Date_Modified:
Needs_Processing: false
```

**Required sections:**

1. `# <Character name>`
2. `## Role` — function in the story
3. `## Background` — relevant history before the story
4. `## Voice and Manner` — speech patterns, defining gestures, what they sound like
5. `## Arc` — how this character changes (or doesn't) across the book
6. `## Relationships` — wiki-links to other characters with relationship type
7. `## Scenes Present` — wiki-links to scenes they appear in
8. `## Open Questions` — things about the character not yet decided

**Naming:** `<FirstName-LastName>.md` or `<Slug>.md`. E.g., `Maya-Chen.md`.

**Location:** `Atoms/Characters/`.

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
- **Characters and Threads are not composed into other atoms.** They're referenced (appears-in, engaged-in) but they don't have an "order in parent."
- **Sources and Notes are floating.** They reference things and are referenced by things, but they have no parent.

## Status field lifecycle

The `lfw_status` field on each atom progresses:

- **planned** → atom exists with frontmatter and outline but no prose
- **drafted** → prose has been written
- **revised** → at least one revision pass has touched it
- **final** → marked finished by the writer

For Sections in non-fiction, an additional `fact-checked` status indicates accuracy pass completion.

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
