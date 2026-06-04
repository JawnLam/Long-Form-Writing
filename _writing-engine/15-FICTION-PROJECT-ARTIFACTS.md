---
type: writing-engine
role: fiction-structural-artifacts
scope: fiction
updated: 2026-06-03
lfw_load:
  tier: pack
  genres: [fiction, screenplay, play]
  activities: [WORLDBUILDING, CONTINUITY-CHECK, READ-THROUGH, BETA-PREP, REVISE]
  phase: on-demand
---

# 15 — FICTION: PROJECT ARTIFACTS

> **The structural-support layer that sits beside v1.2's foundational spine/motif/continuity and v1.3.1's line-level craft. Six artifacts that help organize the creative process for fiction projects beyond what the v1.0–v1.3.1 schema covered: worldbuilding, multi-layer timelines, storyboard, style sheet, research-as-inspiration, relationship map. Plus a stakes-ladder addition to `_spine.md`. All artifacts are opt-in; cartridges that don't need a given artifact don't create it.**

## What this chapter adds

- **`_worldbuilding.md`** — backbone for SFF / fantasy / speculative / alt-history / horror projects requiring deep system-building (magic, technology, cosmology, cultures, languages, political structures)
- **Timeline atom** — multi-layer (story-time / world-history / real-world / character-specific); distinct from `_continuity.md`'s single embedded timeline
- **`_storyboard.md`** — scene-card view; auto-summarized compact representation of every Scene atom
- **`_style-sheet.md`** — spellings, capitalization, italics conventions, punctuation, dialogue-formatting, anachronism flags; lexicon as sub-section
- **Inspiration atom** — research-as-compost; distinct from Source (which is non-fic folded-in citations); fiction's research-tracking that doesn't pretend to citation-discipline
- **`_relationships.md`** — symmetric multi-character relationship map; complements (does not replace) per-character Relationships sections in Character atoms
- **Stakes-ladder section** added to `_spine.md` — explicit tracking of stakes-level (personal / relational / societal / existential) across the manuscript
- **No new activities.** The artifacts feed existing activities (READ-THROUGH, CHARACTER-CONSISTENCY, CONTINUITY-CHECK, BETA-PREP, REVISE)

## §1 — `_worldbuilding.md` backbone

For projects where the world is non-default — fantasy, science fiction, alt-history, horror with non-natural elements, speculative fiction with displacement-from-reality — the world needs its own design document. v1.2's `_continuity.md` carries world-rules in a section, but for SFF the world is too large to fit; it belongs in its own backbone file.

### When to create one

- Fiction sub-genre is `sff`, `speculative`, `historical`, or `horror` (with non-natural elements)
- Worldbuilding requires multiple interlocking systems (magic + cosmology + cultures + languages + political structures)
- World-rules will be referenced by multiple Settings and many Scenes

### When not to create one

- Contemporary realism (the world IS the default; no design needed beyond setting-specific notes)
- The world fits in `_continuity.md`'s world-rules section without strain
- The project is in early premise-exploration and worldbuilding hasn't crystallized

### Structure

The template ships at `_writing-engine/_templates/TEMPLATE-worldbuilding.md`. Body sections:

```markdown
# <World Name>

## What this world is
*One paragraph. The world's central premise / displacement.*

## Cosmology
*If applicable. The metaphysical structure.*

## Physical / natural systems
*Geography, climate, ecology, calendar, astronomy. What's true about how this world works physically.*

## Technology / magic
*The rules. What's possible. What's not. What costs what.*

## Cultures
*Each major culture: history, values, social structure, language, religion. One section per culture.*

## Political structures
*Governments, factions, power structures. Current state at the manuscript's opening.*

## Economy
*If load-bearing. Currency, trade, what's scarce, what's abundant.*

## Languages
*Languages spoken. Naming conventions. Pronunciation guides if invented.*

## Religions / belief systems

## History (deep)
*The centuries / millennia of backstory. May reference Timeline atoms (§2).*

## Open questions
*Worldbuilding gaps the writer is leaving deliberately or hasn't filled yet.*
```

### Discipline

- **Worldbuilding-as-procrastination is real.** F45 (added in this chapter). The same anti-pattern as research-as-procrastination and craft-as-procrastination. If `_worldbuilding.md` sessions dominate without scene-drafting advancing, the AI flags it
- **The world must serve the story.** A perfectly built world is not the goal; a world that supports the manuscript's specific Scenes is
- **Reference rigorously from `_continuity.md`.** When a Scene draws on a world-rule, that rule lives in `_worldbuilding.md`; `_continuity.md` references it. Avoid duplicating world-rules in both files

### Operator-private

`_worldbuilding.md` is operator-private by default (gitignored in writers' own work; included in shipped worked examples via the `!Example-Project-*` override). Worldbuilding is often closer to the writer than the manuscript itself.

## §2 — Multi-layer Timeline atom

`_continuity.md` carries a single embedded timeline — the novel's story-time. For projects with deeper temporal structure, v1.3.2 adds the **Timeline atom** as a first-class atom that captures one temporal layer per file.

### Layers

- **`story-time`** — the events of the novel itself, in story-time order. Equivalent to `_continuity.md`'s embedded timeline; for simple cartridges, the embedded one is sufficient. The atom form is useful when story-time becomes complex (multiple POV chronologies, non-linear structure, frame stories)
- **`world-history`** — backstory of the world preceding the novel. For SFF this may span centuries or millennia. For literary fiction it may span a family's generations
- **`real-world`** — for historical fiction, alt-history, or fiction anchored to verifiable real-world events. Cross-references with Source atoms
- **`character-specific`** — per-character life-arc; one Timeline per major character whose life-trajectory matters to the prose. Often paired with Character-Bible's chronological backstory section

### Frontmatter

```yaml
---
Item_Prototype: LFW_Timeline
Item_ID: ""
Title: ""
lfw_manuscript: ""
lfw_atom_type: timeline
lfw_status: drafting | established | revised | final
lfw_timeline_layer: story-time | world-history | real-world | character-specific
lfw_character: ""    # only for character-specific layer; wikilink to Character atom
lfw_scope: ""        # e.g., "1968-2026", "Day 1-Day 22", "1800 BCE - 1500 BCE"
Date_Added:
Date_Modified:
Needs_Processing: false
---
```

### Body

A chronological table of events. Each event: date (or relative time), what happened, related Scene/Chapter/atom wikilinks. Optional sections for granular sub-periods.

### Cross-reference with `_continuity.md`

`_continuity.md` becomes the *cross-layer reconciliation* document. When a Scene draws on multiple timelines (e.g., a character's memory of a world-history event), `_continuity.md` is where the timing is reconciled. Timeline atoms are the *source-of-truth per layer*; `_continuity.md` is the *consistency-check across layers*.

### Status enum

| Status | Meaning |
|--------|---------|
| `drafting` | First-pass timeline; gaps acceptable |
| `established` | Sufficient detail to support drafting; consistent with prose so far |
| `revised` | Timeline has been updated after CONTINUITY-CHECK surfaced drift |
| `final` | Manuscript drafted; timeline reconciled |

### When to add Timeline atoms

- **`character-specific`** when a Character-Bible's chronological backstory grows beyond a section and needs its own file
- **`world-history`** for SFF / fantasy / historical with substantial pre-novel backstory
- **`real-world`** for historical fiction
- **`story-time` as atom** for non-linear novels (Cloud Atlas, Lincoln in the Bardo, novels with frame stories)

## §3 — `_storyboard.md` backbone

A scene-card view. The conceit (borrowed from Scrivener's corkboard and from film storyboarding): every Scene as a card with a short descriptor, status, value-shift in compact form. The reader (writer + AI) can audit the whole manuscript's shape at a glance.

### Structure

Generated semi-manually; can be updated by hand or by a session activity that auto-summarizes from Scene atoms. Per chapter, a list of scene-cards:

```markdown
## Chapter 03 — The First Cold Night

| Scene | Type | Status | POV | Value-shift / Decision | One-line |
|-------|------|--------|-----|------------------------|----------|
| [[03-01-Pre-Dawn-Forecast]] | scene | drafted | Sarah | distant → operationally-bonded | Hector's call wakes both sisters; the work begins |
| [[03-02-Wind-Machines]] | scene | drafting | Maya | cold-tense → cautiously-bonded | working the lower blocks; the labor opens a small connection |
| [[03-03-Letter-Moved]] | sequel | planned | Maya | decision: scan Sarah | morning kitchen; the letter has moved an inch |
```

### When to use

- The cartridge has ≥10 drafted Scenes and structural overview is becoming difficult
- The writer is doing macro-revision (READ-THROUGH at book-scale) and wants a single view
- A specific chapter's scene-shape needs auditing
- For shorter cartridges (< 10 scenes), the `_state.md` Scene table is sufficient and the storyboard is redundant

### Discipline

- **Storyboard goes stale fast.** F47 (added in this chapter). If a session ends with new/changed Scenes but the storyboard isn't updated, the storyboard becomes worse-than-useless within a week
- **Storyboard is derivative.** The Scene atoms are the source of truth; the storyboard summarizes. Never edit story content via the storyboard — always go through the Scene atom

### Operator-private

Operator-private by default. The storyboard is the writer's working overview; it doesn't ship with the manuscript.

## §4 — `_style-sheet.md` backbone

The cartridge's style-and-language conventions. What gets capitalized, what's in italics, how dialogue is punctuated, how invented terms are spelled, what numbers are spelled out, etc. For long manuscripts the style sheet is the single biggest defense against drift-by-attention-failure.

### Structure

The template ships at `_writing-engine/_templates/TEMPLATE-style-sheet.md`. Body sections:

```markdown
# <Manuscript Title> — Style Sheet

## Voice and register reminders
*Short summary; pointer to `_voice-samples.md` if used.*

## Spelling
*US vs UK; specific words you've made a choice about (e.g., "grey" vs "gray"); brand-name capitalization.*

## Capitalization
*Deity / titles / period-specific conventions / proper nouns.*

## Italics
*Foreign words; inner dialogue; emphasis; titles; ship/vehicle names.*

## Punctuation
*Oxford comma yes/no; em-dash vs en-dash; ellipsis (3 dots vs ...); quotation marks; serial commas.*

## Numbers
*Spelled-out vs numerals; time formats; date formats; ages.*

## Dialogue formatting *(cross-reference chapter 13 §1)*
*Said-only vs mixed-tag; action-beats; em-dash for interruption vs ellipsis for trail-off; foreign-language conventions; inner dialogue marker.*

## Lexicon *(sub-section — see below)*

## Anachronism risk catalog
*For historical / period work: words / phrases / concepts that risk anachronism. List per period / era.*

## Inconsistencies to fix
*Running log of style drift caught in revision passes; not yet resolved.*
```

### Lexicon sub-section

For projects with invented terms, proper nouns, character names with specific spellings, place names, technical terminology:

```markdown
## Lexicon

| Term | Definition / context | First appears | Pronunciation |
|------|----------------------|---------------|---------------|
| Hollis | Family surname; rhymes with "Hollis" (no special pronunciation) | [[01-01-The-Approach]] | HOL-iss |
| Glen Ellen | Specific Sonoma town; not "Glenn Ellen" | [[01-01-The-Approach]] | — |
```

For fantasy / SFF with substantial invented vocabulary, the lexicon may grow into a separate `_lexicon.md` file; v1.3.2 does not formalize this — the writer makes the call when the section becomes unwieldy.

### Discipline

- **Style sheet drift in dialogue formatting (F36 from v1.3.1) and across the manuscript broadly (F48 added here) reads as inattention.** Editors and agents notice. Readers feel it before they can name it
- **The style sheet is consulted at BETA-PREP** as part of the final polish pass
- **The style sheet is consulted at the line-edit REVISE pass** if one is used

### Operator-private (mostly)

The style sheet is operator-private by default. It may eventually be shared with copy editors and proofreaders during production; that's an export-and-send action, not a publication.

## §5 — Inspiration atom

Source atoms (v1.0) carry the citation discipline for non-fiction. They include `lfw_status: identified | ingested | folded-in | superseded` and feed RESEARCH-INTEGRATION sessions. They are designed to *be cited*.

Fiction has a different research relationship. A novelist may read 30 books about Sonoma viticulture and never cite any of them. The reading shapes the prose; the books are not sources in the non-fiction sense. They are *compost.*

The Inspiration atom is fiction's research-tracking — what the writer has absorbed without committing to cite.

### Frontmatter

```yaml
---
Item_Prototype: LFW_Inspiration
Item_ID: ""
Title: ""
lfw_manuscript: ""
lfw_atom_type: inspiration
lfw_status: noted | absorbed | folded-in | retired
lfw_kind: book | article | film | conversation | observation | image | podcast | other
lfw_for: ""    # what aspect of the manuscript this informs (setting, character, voice, theme, mood)
Date_Added:
Date_Modified:
Needs_Processing: false
---
```

### Body

```markdown
# <Inspiration title>

## What it is
*Brief description. Title, author/source if applicable.*

## What it inspires in this manuscript
*Specifically — what does this feed? Mood? A character beat? A setting detail? A line of dialogue?*

## Status notes
- `noted` — encountered; intent to absorb later
- `absorbed` — read/watched/observed; effect is now diffuse
- `folded-in` — a specific element has surfaced in drafted prose
- `retired` — turned out not to be relevant; archived

## Where it surfaces (if folded-in)
*Wiki-links to Scene atoms where the inspiration has landed.*

## Notes
```

### Distinction from Source

| Distinction | Source | Inspiration |
|-------------|--------|-------------|
| Will be cited? | Yes (non-fiction discipline) | No (fiction's compost) |
| Citation-style required? | Yes | No |
| Fold-in discipline? | Rigorous (chapter 06) | Light (just track that it surfaced) |
| Used in | Non-fiction / dissertation | Fiction primarily |
| Anti-fabrication discipline? | Strict (chapter 06 cardinal rules) | n/a — the writing IS the fabrication |

A non-fic memoir might use both: Source atoms for cited research, Inspiration atoms for unstoried influence.

### Failure mode

- **F49 — Inspiration becomes citation.** Writer treats Inspiration atoms with Source-discipline rigor; or treats Source atoms with Inspiration-compost looseness. Each discipline is wrong-shaped for the other artifact

## §6 — `_relationships.md` backbone

Character atoms have a Relationships section that captures each character's view of their relationships *one-sidedly*. For novels with five or more named characters, the asymmetric one-sided view becomes hard to audit. v1.3.2 adds `_relationships.md` as the symmetric multi-character map.

### Structure

```markdown
# <Manuscript Title> — Relationship Map

## All pairs (matrix)

|                    | Maya | Sarah | Hector | Daniel | Helen |
|--------------------|------|-------|--------|--------|-------|
| **Maya**           | —    | s1    | s2     | s3     | s4    |
| **Sarah**          | s1   | —     | s5     | s6     | s7    |
| **Hector**         | s2   | s5    | —      | s8     | —     |
| **Daniel (†)**     | s3   | s6    | s8     | —      | s9    |
| **Helen (†)**      | s4   | s7    | —      | s9     | —     |

*(s1, s2, etc. point to numbered sections below)*

## Per-pair detail

### s1 — Maya ↔ Sarah
- **Type:** sisters, three-year estrangement
- **History:** *(summary)*
- **Current state (Day 1):**
- **Evolution arc:**
- **Subtext:**

### s2 — Maya ↔ Hector
*(repeat per pair)*
```

### When to use

- Five or more named characters with named relationships
- A novel where relational tension is the central engine (most literary fiction)
- During READ-THROUGH for cross-checking that the Character atoms' one-sided views are consistent symmetrically

### Discipline

- **F50 — Relationship map disconnected from prose.** The map is updated diligently; the prose doesn't reflect the relationships the map asserts. CHARACTER-CONSISTENCY catches this; the map is the input
- **Symmetry check.** What Maya thinks of her relationship to Sarah and what Sarah thinks of her relationship to Maya may differ — but they should differ in ways the writer has decided. Drift between the two one-sided views, unintended, is a flag

### Operator-private

Operator-private by default.

## §7 — Stakes ladder (addition to `_spine.md`)

v1.2's `_spine.md` has an *Escalation curve* section that tracks rising stakes implicitly. v1.3.2 makes the stakes-level explicit by adding a Stakes-ladder section to the spine template:

```markdown
## Stakes ladder

For each chapter (or major scene), note the stakes operating at four levels. Stakes can be present at multiple levels simultaneously; rising-stakes means the level escalates across the manuscript, not that every chapter must hit every level.

| Chapter | Personal | Relational | Societal | Existential | Notes |
|---------|----------|------------|----------|-------------|-------|
| 1 | Maya's unease | the sisters' careful distance | — | — | small personal + small relational; right opening level |
| 2 | Sarah's secret-keeping | the unspoken conversation | — | — | personal interior + relational rising |
| 3 | the work; the frost | shared labor | the vineyard's economic survival | — | societal layer begins |
| ... | | | | | |
```

### Stakes-level taxonomy

- **Personal** — what the protagonist privately stands to gain or lose; emotional, internal, intimate
- **Relational** — what the protagonist's key relationships stand to gain or lose
- **Societal** — what the broader world (community, institution, society) stands to gain or lose
- **Existential** — what the protagonist's fundamental identity, soul, or being stands to gain or lose

### Discipline

- **F51 — Flat stakes.** Stakes operate at the same level across the manuscript; nothing escalates. Reads as static even if individual scenes turn. The stakes-ladder makes this visible at a glance
- **Inverted-pyramid risk.** Some manuscripts escalate to existential stakes too quickly, leaving Chapter 8 with no room left to escalate. The ladder surfaces this

### Cross-reference with the escalation curve

The escalation curve names the highest-pressure moments (mid-act crisis, climax). The stakes-ladder is the per-chapter texture of *what* is at stake. Both are needed; neither subsumes the other.

## §8 — Read-order placement and activity tunings

These artifacts are read **on demand** based on activity:

- **`_worldbuilding.md`** — required reading for any WORLDBUILDING or CONTINUITY-CHECK on SFF/speculative/historical cartridges
- **Timeline atoms** — read by CONTINUITY-CHECK; read by CHARACTER-CONSISTENCY for character-specific Timelines
- **`_storyboard.md`** — read at READ-THROUGH; usually only consulted at book-scale
- **`_style-sheet.md`** — read at BETA-PREP and at line-edit REVISE pass
- **Inspiration atoms** — read when the writer references one; otherwise not loaded
- **`_relationships.md`** — read by CHARACTER-CONSISTENCY; read at READ-THROUGH
- **Stakes-ladder (in `_spine.md`)** — read by SCENE-AUDIT, READ-THROUGH, BETA-PREP

No new activities are added in v1.3.2. The artifacts feed existing activities.

### Sub-genre defaults

Per chapter 14 §5's sub-genre tunings, v1.3.2 artifacts have sub-genre-typical relevance:

| Sub-genre | _worldbuilding | Timeline (layer) | _storyboard | _style-sheet | Inspiration | _relationships | Stakes ladder |
|-----------|----------------|------------------|-------------|--------------|-------------|----------------|---------------|
| literary | rarely | character-specific common | useful | useful | useful | useful | useful |
| thriller | rarely | story-time only | useful | useful | rarely | useful | central |
| mystery | rarely | story-time + character | useful | useful | useful | useful | useful |
| romance | rarely | character | useful | useful | useful | central | useful |
| sff | central | world-history central | useful | useful | useful | useful | useful |
| speculative | useful | world-history | useful | useful | useful | useful | useful |
| historical | useful | real-world central | useful | central (anachronism) | central (research) | useful | useful |
| horror | useful (atmospheric) | story-time | useful | useful | useful | useful | central |
| ya | rarely | character | useful | useful | useful | useful | useful |

These are defaults; cartridges deviate freely.

## §9 — Failure modes added in v1.3.2

See `_meta/FAILURE-MODES.md` for full entries.

- **F45 — Worldbuilding as procrastination.** Same anti-pattern as F11 / F18 / F43. World expands indefinitely as avoidance of drafting
- **F46 — Timeline layers conflated.** Story-time, world-history, and character-specific events tracked in a single timeline document; layers contaminate; events drift to wrong layer
- **F47 — Storyboard stale.** Storyboard not updated after scene revisions; produces false picture; worse than no storyboard
- **F48 — Style-sheet drift.** Spelling, capitalization, italics conventions drift across chapters; reads as inattention
- **F49 — Inspiration becomes citation.** Inspiration atoms treated with Source-discipline rigor (or vice versa); each discipline wrong-shaped for the other artifact
- **F50 — Relationship map disconnected from prose.** Map is diligent; prose ignores it; CHARACTER-CONSISTENCY catches the gap
- **F51 — Flat stakes.** Stakes operate at the same level across the manuscript; nothing escalates; the stakes-ladder makes this visible

## §10 — How this chapter interacts with the rest of the engine

- **Chapter 03** — no new activities, but READ-THROUGH, CONTINUITY-CHECK, CHARACTER-CONSISTENCY, and BETA-PREP all gain new artifacts to consult
- **Chapter 04** — Timeline and Inspiration atom types added; six new backbone files documented
- **Chapter 09** — F45 (worldbuilding-as-procrastination) added to the procrastination-pattern family
- **Chapter 11** — `_spine.md` template gains Stakes-ladder section
- **Chapter 12** — `_continuity.md` becomes cross-layer reconciliation when Timeline atoms exist
- **Chapter 13** — `_style-sheet.md`'s dialogue-formatting section cross-references chapter 13 §1
- **Chapter 14** — sub-genre cues in §5 reference v1.3.2 artifacts
- **`_meta/FAILURE-MODES.md`** — F45–F51 added

## §11 — Read-order placement

This chapter is **read on demand** based on the artifact being created or consulted. Recommended at BOOTSTRAP for any cartridge in `sff`, `speculative`, or `historical` sub-genres (worldbuilding and timeline are usually load-bearing). Required reading before creating any of the six new backbone files or before working with Timeline / Inspiration atoms.

## §12 — What v1.3.2 does NOT add

The two-pass series (v1.3.1 + v1.3.2) is complete. Notable choices about what was deferred or folded:

- **Beat-sheet for ensemble novels (multi-protagonist).** Save the Cat / Story Circle / Hero's Journey assume a single protagonist. Multi-protagonist structures (Cloud Atlas, Olive Kitteridge) need different overlays. Deferred; possibly v1.4
- **Visual storyboard (image / drawing).** v1.3.2's storyboard is text-only. Visual storyboarding belongs in a different tool (Scrivener, Miro, paper); v1.3.2's text storyboard is the AI-readable equivalent
- **Per-POV style sheet.** A single style sheet per cartridge is sufficient for most projects. Multi-POV with substantially different dialogue conventions per POV (e.g., epistolary novels with multiple letter-writers) may need per-POV style sheets; treated as a custom-extension if needed
- **Theme atom for non-fiction.** v1.3.1's Theme atom is fiction-primary. Non-fiction memoir / narrative non-fiction may use it; v1.3.2 does not formalize a non-fiction Theme discipline (which would partially duplicate `_argument.md`'s machinery)
