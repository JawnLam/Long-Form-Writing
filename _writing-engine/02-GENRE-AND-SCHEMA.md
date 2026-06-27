---
type: writing-engine
role: schema-branching
scope: subject-agnostic
updated: 2026-06-02
lfw_load:
  tier: core
  genres: [all]
  activities: [SESSION-START]
  phase: on-demand
---

# 02 — GENRE AND SCHEMA

> **How the schema adapts per cartridge based on declared genre. One engine, five genre branches.**

## The genre field

Every cartridge declares its genre in `_manuscript-manifest.md`:

```yaml
lfw_genre: fiction | non-fiction | screenplay | play | dissertation
```

This is the load-bearing setting. It determines:

- Which Types are first-class in the cartridge
- Which optional Items apply
- What `_outline.md` looks like
- Which session activities apply (e.g., WORLDBUILDING is fiction-only)
- What "done" looks like

Genre is locked at cartridge bootstrap. Changing genre mid-cartridge is a major refactor, not a flag flip. If a project genuinely transitions (you started a research project that became a memoir), archive the cartridge and start fresh.

## Genre branch — Fiction

**Items emphasized:**

- **Scene** (primary) — the unit of dramatic action; prose lives here
- **Character** (primary) — recurring participants; first-class Items with their own files
- **Character-Bible** *(v1.3.1, opt-in)* — extended companion to Character for POV-bearing, antagonist, and major-supporting characters
- **Motif** *(v1.2)* — image-cluster / recurring-object / thematic carrier
- **Theme** *(v1.3.1)* — abstract idea the manuscript is about, carried not declared
- **Chapter** (medium) — composes Scenes; sometimes absent (some novels are chapter-less)
- **Beat** (medium) — within Scenes, the dramatic moves; optional Subtext body section in v1.3.1
- **Reader** (medium, fiction-reframed in chapter 12 §6) — modeled audience members
- **Source** (light) — for research-informed fiction; otherwise rare
- **Note** (medium) — story ideas, alternate paths

**Outline structure:** Book → Part (optional) → Chapter → Scene → Beat. May include an act structure (three-act, five-act) at the Part level.

**Lifecycle stages:** outlining → drafting → revising → polishing → shipped

**Genre-specific activities:** WORLDBUILDING (setting, magic systems, alternate-history rules), SCENE-AUDIT, CHARACTER-CONSISTENCY, CONTINUITY-CHECK, SETUP-PAYOFF-AUDIT *(v1.2)*, DIALOGUE-AUDIT, POV-VOICE-DRIFT, THEME-CHECK *(v1.3.1)*

**"Done" looks like:** A complete manuscript that the writer is ready to send to beta readers / an agent / a developmental editor. Voice consistent. Plot tight. Characters consistent.

### Fiction sub-genre *(v1.3.1)*

Fiction cartridges optionally declare a sub-genre:

```yaml
lfw_genre: fiction
lfw_fiction_subgenre: literary | thriller | mystery | romance | sff | speculative | historical | horror | ya
```

Sub-genre tunes the activity-decision algorithm's defaults (chapter 03 §6b'): cadence thresholds shift, certain activities promote, the reader-simulation lens calibrates to the sub-genre's reader expectations. The sub-genre is *advisory* — it does not change required schema. See chapter 14 §5 for the per-sub-genre cues.

## Genre branch — Non-fiction

**Items emphasized:**

- **Section** (primary) — the unit of argument or narrative; prose lives here
- **Thread** (primary) — recurring topics, arguments, framing devices that span sections
- **Source** (primary) — books, papers, interviews, data; central to non-fiction
- **Chapter** (high) — composes Sections; usually present and meaningful
- **Beat** (medium) — within Sections, the rhetorical moves
- **Note** (medium) — unplaced ideas, possible inclusions
- **Character** (light, optional) — for biographical / journalistic non-fiction with named individuals

**Outline structure:** Book → Part (optional) → Chapter → Section → Beat. The argumentative or narrative spine is usually at the Chapter level.

**Lifecycle stages:** research → outlining → drafting → revising → fact-checking → polishing → shipped

**Genre-specific notes:** RESEARCH-INTEGRATION is a heavily-used activity. Source Items carry the citation discipline (chapter 06).

**"Done" looks like:** A complete manuscript with verified citations, fact-checked claims, and a clear argumentative or narrative arc that a serious reader can follow.

## Genre branch — Screenplay

**Items emphasized:**

- **Scene** (primary) — the screenplay unit; prose follows screenwriting conventions (slug lines, action lines, dialogue)
- **Character** (primary) — speaking roles + named non-speaking; first-class Items
- **Beat** (high) — within Scenes, the dramatic moves; screenwriting traditionally tracks beats explicitly
- **Act** (high, replaces Chapter) — composes Scenes; usually three or five acts
- **Note** (medium) — alt versions, deleted scenes, dialogue fragments
- **Source** (light) — for research-driven screenplays (historical, biographical)

**Outline structure:** Screenplay → Act → Scene → Beat. Many screenwriters use a beat sheet (Save the Cat, Field paradigm, etc.) as the master outline.

**Lifecycle stages:** treatment → outlining → drafting → revising → polishing → shipped

**Genre-specific conventions:** Page-count discipline matters (1 page ≈ 1 minute of screen time). Format conventions (Final Draft, Fountain) are external to LFW but the Items accommodate them.

**"Done" looks like:** A complete screenplay ready to send to a producer, manager, agent, or contest.

## Genre branch — Play

**Items emphasized:**

- **Scene** (primary)
- **Character** (primary) — speaking roles; first-class
- **Act** (high) — composes Scenes
- **Beat** (high) — dramatic moves within Scenes
- **Setting** (custom Item for plays) — locations and stage requirements; may be a custom Type per the cartridge
- **Note** (medium) — alt versions, dramaturgical notes

**Outline structure:** Play → Act → Scene → Beat.

**Lifecycle stages:** treatment → outlining → drafting → revising → workshop-revising → polishing → shipped

**Genre-specific conventions:** Stage directions live with the prose (in Scene Items). Production considerations (cast size, set complexity) live in the manuscript manifest.

**"Done" looks like:** A complete play script ready for submission to theaters, workshops, contests, or self-production.

## Genre branch — Dissertation / academic

**Items emphasized:**

- **Section** (primary)
- **Thread** (primary) — arguments, sub-arguments, methodological threads
- **Source** (primary) — central; with rigorous citation
- **Chapter** (primary) — the major divisions; usually with formal abstracts
- **Beat** (medium) — within Sections, the analytical moves
- **Note** (medium) — research questions, methodological worries, advisor feedback

**Outline structure:** Dissertation → Chapter → Section → Beat. Usually follows discipline conventions (intro / literature review / methodology / findings / discussion / conclusion is one common shape).

**Lifecycle stages:** proposal → research → outlining → drafting → revising → defense-prep → defense → revision → final → shipped

**Genre-specific notes:** Citation rigor is the dominant constraint. RESEARCH-INTEGRATION protocol applies aggressively. Anti-fabrication is non-negotiable.

**"Done" looks like:** A defended dissertation deposited in institutional repository, plus any conventional next-step versions (book proposal, journal articles).

## How the AI uses this chapter

When loading a cartridge, the AI reads `_manuscript-manifest.md` for the `lfw_genre` field, then comes back to this chapter to know:

- Which Types to expect and create
- Which lifecycle stage labels are valid
- Which session activities to consider in the activity-decision algorithm
- What "done" looks like for THIS manuscript

When in doubt, the AI proposes the genre-default approach but accepts writer overrides (e.g., a literary novel that uses non-fiction-style Sections instead of Scenes).

## Edge cases

**Hybrid genres** (memoir, narrative non-fiction, autofiction): pick the genre whose schema is the closest fit and override specific Items. E.g., a memoir typically uses `genre: non-fiction` but adds Character Items for named individuals.

**Multi-book series:** each book is its own cartridge. A shared `series-bible.md` at the LFW root can carry cross-book reference material if needed (out of scope for the engine; a writer convention).

**Anthology / short-story collection:** each story is a cartridge; the collection is a parent folder. The "Chapter" Item in each cartridge maps to the story. Not a strong fit; consider whether LFW is the right form (a smaller artifact might serve better).

**Translation work:** out of scope for v1.0. A future v1.x extension could add a `translation` genre with Source Items for the original text and special handling for matched prose.

**Poetry collections:** out of scope for v1.0. Per-poem Item shape doesn't fit cleanly. Possible v1.x extension.

## When to extend the schema

If a writer working in a covered genre finds the Item set insufficient (e.g., a screenwriter wants a separate `Beat-Sheet` Item for the master beat sheet), add it per-cartridge in the manifest:

```yaml
lfw_custom_items:
  - beat-sheet
```

For genres beyond the five listed, this is an in-scope minor-version contribution. See `CONTRIBUTING.md` §6.
