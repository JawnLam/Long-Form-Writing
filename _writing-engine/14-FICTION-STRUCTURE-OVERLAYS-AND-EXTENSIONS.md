---
type: writing-engine
role: fiction-structure-overlays-and-extensions
scope: fiction
updated: 2026-06-03
---

# 14 — FICTION: STRUCTURE OVERLAYS AND EXTENSIONS

> **Scene-and-sequel rhythm, beat-sheet overlays, Theme as first-class atom, Character-Bible as extended atom, fiction sub-genre branching cues. The structural-overlay layer that sits between v1.2's foundational spine/motif/continuity and the writer's specific shaping of a manuscript.**

## What this chapter adds

- **Scene-and-sequel rhythm** — Swain's reactive-beat structure that lives between value-shifting scenes; the new `lfw_scene_type` field
- **Beat-sheet overlays** — opt-in plot-structure templates (Story Circle, Save the Cat, Hero's Journey, Freytag) that overlay onto `_spine.md` without replacing it
- **Theme atom** — first-class atom for thematic argument, distinct from Motif (image) and from `_argument.md` (which is non-fiction's logical backbone)
- **Character-Bible atom** — the deep companion to the Character atom for novels where character work is load-bearing; includes full backstory, family tree, contradictions, secrets
- **Fiction sub-genre branching** — `lfw_fiction_subgenre` field with sub-genre-specific cues for literary / thriller / mystery / romance / SFF / speculative
- **One new activity** — THEME-CHECK
- **No new universal activities** — beat-sheet overlays piggyback on existing SCENE-AUDIT and READ-THROUGH

## §1 — Scene-and-sequel rhythm

Dwight Swain's *Techniques of the Selling Writer* named the structural unit that fiction needs and that v1.2's value-shift discipline only half-captured: every dramatized turn (a *scene*) needs a corresponding reactive beat (a *sequel*) where the POV character processes the turn before the next want crystallizes.

### The pattern

A scene is: *want → conflict → outcome (value-shift).* The protagonist wants something, encounters opposition, and ends in a different value-state than they started.

A sequel is: *reaction → dilemma → decision.* The protagonist reacts to what just happened (emotionally, physically), faces a new dilemma created by the new value-state, and decides on a new course of action — which becomes the *want* of the next scene.

The full novel reads as: *scene → sequel → scene → sequel → scene...* with sequel-density varying by genre (literary fiction sits inside sequels more; thrillers compress them; romance and mystery use them to develop relationship and clue-processing respectively).

### The new field

The Scene atom gains an optional frontmatter field:

```yaml
lfw_scene_type: ""    # v1.3.1 — "scene" (value-shifting, default) | "sequel" (reactive-processing) | "scene-sequel" (compound)
```

Most atoms remain `scene` (or unset, equivalent to scene). Atoms explicitly tagged `sequel` are *not* required to declare a value-shift in the v1.2 sense; their job is processing a prior turn, not turning. The validator (chapter 13's check 9) skips value-shift requirements on `sequel`-typed atoms.

A `scene-sequel` compound atom is a Scene that contains both a turn *and* its reactive processing within the same unit — common in literary fiction where the writer compresses for prose-economy.

### The new body sections

When `lfw_scene_type: sequel`, the atom uses the **Sequel body** instead of the **Value-shift body**:

```markdown
## Sequel *(v1.3.1 — for lfw_scene_type: sequel)*

- **Whose reaction this sequel carries:** *(POV character)*
- **Reaction (emotional, physical, immediate):** *(the first response to the prior scene's outcome)*
- **Dilemma (the new situation):** *(what new choice the prior outcome forces)*
- **Decision (the new want):** *(what the character decides to pursue next — sets up the next scene's want)*
- **Carry-forward connector to next scene:** *(the decision IS the next scene's want — explicit linkage)*
```

For `scene-sequel` compound atoms, both the Value-shift body and the Sequel body appear in the atom.

### Spine ledger update

The `_spine.md` scene-by-scene ledger gains an optional column:

| # | Scene | Type | POV | From → To (if scene) / Decision (if sequel) | But/Therefore |

The validator accepts both forms; the SCENE-AUDIT activity reads the type to choose between value-shift checking (for scenes) and decision-carry-forward checking (for sequels).

### When to use sequels explicitly

Literary fiction often makes the sequel-beat the most powerful prose in the chapter (the silent walk home; the conversation that doesn't happen; the moment alone afterwards). Tagging it `sequel` lets the writer hold that prose to the *decision-emerging* discipline rather than misapplying value-shift to it.

Thrillers and commercial fiction often compress sequels into a paragraph or skip them entirely between high-tension scenes. Tagging compresses the auditing — a chapter of 5 scenes and 0 sequels is structurally correct for a thriller, structurally suspect for a literary novel.

### Failure modes

- **F38 — Missing sequels in literary fiction.** Every scene is a turn; no reactive beats; reader has no room to feel the turns. Reads as relentless.
- **F39 — Over-sequel'd thriller.** Every action scene is followed by extended interiority; pacing collapses; the form's grammar is violated.
- **F40 — Sequel without decision.** Sequel atom that processes the prior scene but doesn't produce a new want for the next scene; the chain breaks.

## §2 — Beat-sheet overlays

Beat-sheets are pre-existing structural templates (Story Circle, Save the Cat, Hero's Journey, Freytag's pyramid) that prescribe a specific shape for a narrative. v1.3.1 ships four as **opt-in overlays** that the writer maps onto their `_spine.md` without replacing it.

### The four shipped overlays

| Overlay | Origin | Fits | Beat count |
|---------|--------|------|------------|
| **Story Circle** | Dan Harmon (after Joseph Campbell) | Most fiction; literary-friendly | 8 beats |
| **Save the Cat** | Blake Snyder | Commercial fiction; screenplay-adjacent | 15 beats |
| **Hero's Journey** | Joseph Campbell / Christopher Vogler | Mythic / fantasy / quest structures | 12 beats |
| **Freytag's Pyramid** | Gustav Freytag | Classical / tragic / dramatic structures | 5 beats |

Each ships as a template (`_writing-engine/_templates/TEMPLATE-overlay-{name}.md`). The writer copies the template into the cartridge as a backbone-like file (`<Cartridge>/_overlay-{name}.md`) and fills in which Scene atoms occupy each beat-position.

### How overlays interact with `_spine.md`

The overlay does **not** replace the spine. The spine remains the causal-claim backbone (premise as causal claim, dramatic question, scene-by-scene value-shift). The overlay is a *parallel* artifact that asks: *given the spine I have, does it match the shape I'm aiming for?*

A literary novel may decline any overlay; the spine alone is sufficient. A thriller may use Save the Cat as the auditing scaffold. A fantasy may use Hero's Journey explicitly. The overlay is diagnostic, not generative — it doesn't tell the writer what to write; it tells the writer whether what they've written hits the beats the chosen shape expects.

### Frontmatter

Cartridges using an overlay declare it in `_manuscript-manifest.md`:

```yaml
lfw_active_overlays: ["story-circle"]    # v1.3.1; may be empty
```

The validator does not require an overlay file to exist even when declared; the declaration signals intent. When `_overlay-{name}.md` does exist, READ-THROUGH and SCENE-AUDIT activities consult it for shape-fit checks.

### Anti-pattern: overlay-as-formula

The overlay is a *reading lens*, not a *writing prescription*. The most common failure mode (F41) is treating Save the Cat as a fifteen-beat checklist and contorting the story to hit beats. The OV's posture: surface the overlay's expectations, surface where the spine diverges, *let the writer decide* whether the divergence is a defect or a deliberate choice.

Literary fiction frequently diverges from any named overlay deliberately. The opt-in nature of overlays protects the writer from formula-creep.

## §3 — Character-Bible atom (new)

The Character atom (v1.0, expanded v1.2 + v1.3.1) captures function, want/need/wound, voice, dialogue tells, behavioral consistency. For most characters this is sufficient. For protagonists, antagonists, and primary supporting characters in a long novel, the writer often needs more — a deep companion document where backstory, family history, contradictions, secrets, evolving arc, sensory specifics, and the connective tissue of a life all live.

### When to create a bible

- The character is POV-bearing
- The character is the antagonist (steelman discipline + extended backstory)
- The character is a primary supporting role with substantial arc
- The writer is consistently re-deriving backstory across sessions and would benefit from a single source of truth

Bibles are **opt-in.** Most secondary characters never get one. A novel with two POVs and one steelmanned antagonist typically has 3 bibles total.

### Structure

The Character-Bible atom is a separate file linked from the Character atom (via `lfw_character_bible:` field added in chapter 13). Lives in `<Cartridge>/Atoms/Character-Bibles/<Slug>.md`.

Frontmatter:

```yaml
---
Item_Prototype: LFW_Character_Bible
Item_ID: ""
Title: ""
lfw_manuscript: ""
lfw_atom_type: character-bible
lfw_status: drafting       # drafting | established | revised | final
lfw_character: ""          # wiki-link back to the Character atom
Date_Added:
Date_Modified:
Needs_Processing: false
---
```

Body sections (all optional; populate as the manuscript demands):

```markdown
# <Character Name> — Bible

## At-a-glance

*Single-paragraph summary. The character in 60 words.*

## Physical

- Appearance, posture, signature gestures
- Wardrobe / personal style
- The way they occupy a room

## Backstory (chronological)

*Birth-to-present, in dated bullets. The full timeline of a life.*

## Family / lineage / ancestry

*The branches that matter. Family tree if non-trivial.*

## Worldview

- Beliefs (load-bearing and held-lightly)
- Politics (only if relevant)
- Religious / spiritual orientation
- What they think the world is fundamentally like

## Habits and routines

*Daily rhythms. What they do without thinking. The texture of their life.*

## Skills, knowledge, and competence

- What they know expertly
- What they're competent at
- What they're publicly thought to be good at vs what they're actually good at

## Wounds (deep)

*The injuries that shape them. Often multiple; the want/need/wound triad in the Character atom names one; the bible names all.*

## Secrets

*What they're hiding, from whom, for how long, at what cost.*

## Contradictions

*The character's internal contradictions — what they value vs what they do; what they say vs what they want; what they've decided about themselves that the evidence doesn't support.*

## Arc across this manuscript

*Where they start, what changes, where they end. Beat-by-beat if useful.*

## Relationships (per-relationship)

For each significant other character: 
- *History* — how they became who they are to each other
- *Current state* — what their relationship is at the manuscript's opening
- *Evolution* — how the manuscript changes it
- *Subtext* — what's unspoken between them

## Voice (extended)

*Building on the Character atom's voice-and-prose-register section: pet phrases that ONLY appear in this bible (not in scenes — yet); the verbal register at different ages; the way their voice shifts under stress, intoxication, grief.*

## Sensory signatures

*The character's smell, the sound of their walk, the specific way light hits them. Bookkeeping for the prose to draw on consistently.*

## Notes / not-yet-decided

*Open questions about the character. Decision-deferred items. Things the writer wants to discover in drafting.*
```

### Status enum

| Status | Meaning |
|--------|---------|
| `drafting` | First-pass bible; gaps acceptable |
| `established` | Sufficient detail to support drafting; consistent with scenes drafted so far |
| `revised` | Bible has been updated after CHARACTER-CONSISTENCY surfaced drift; aligned with current draft |
| `final` | Manuscript drafted; bible reconciled; suitable for series-bible or estate-archive use |

### Read-order placement

When present, Character-Bible atoms are read **on demand**, not at session-start. They are too long to load by default. CHARACTER-CONSISTENCY activity reads them in full. POV-VOICE-DRIFT may read the voice section. Other activities read the at-a-glance summary.

### Operator-private by default

Character bibles are operator-private (gitignored in the writer's own copies; included in shipped worked examples via the `!Example-Project-*` override). Many writers prefer to keep deep character work private even when sharing the manuscript or OV.

## §4 — Theme atom (new)

Theme is the abstract idea the manuscript is *about* — distinct from premise (the situation) and from motif (the recurrent image). *Inheritance, honesty under cost, the way grief reorganizes a relationship, the limits of knowing another person* — these are themes. They are what the novel *means*, when meaning is asked.

v1.2's `_spine.md` carried thematic implication but didn't name it. v1.3.1 adds the Theme atom so the manuscript's themes are first-class, queryable, and auditable for treatment-without-on-the-noseness.

### Frontmatter

```yaml
---
Item_Prototype: LFW_Theme
Item_ID: ""
Title: ""
lfw_manuscript: ""
lfw_atom_type: theme
lfw_status: candidate    # candidate | developing | threaded | resolved
lfw_priority: ""         # "central" / "secondary" / "incidental"
lfw_appears_in_scenes: []
lfw_related_motifs: []   # wiki-links to Motif atoms that carry this theme
lfw_related_characters: []  # wiki-links to Characters who embody or test this theme
Date_Added:
Date_Modified:
Needs_Processing: false
---
```

### Body sections

```markdown
# Theme — <Name>

## What this theme is

*One paragraph. The abstract idea, in plain words.*

## Why this theme matters in this manuscript

*Not "themes are important"; specifically why THIS theme is load-bearing for THIS book.*

## How it's carried (not declared)

*The theme is not stated in the prose. It is carried by character choices, motif recurrence, plot-shape, and the dramatic question. List the mechanisms.*

## Tension within the theme

*A theme treated as a single position is preachment. A theme treated as a tension between positions is literature. What's the tension here?*

## Where it surfaces (scene-by-scene)

*Light at first; grows as scenes are drafted. Each entry: scene, what the theme does in that scene.*

## What it must NOT do

- *Be stated by any character in a way that reads as the novel's thesis*
- *Resolve neatly*
- *Become the motif's stated meaning (the motif must remain physical; the theme must remain implied)*

## Audit notes

*Track each scene's treatment as the manuscript drafts. THEME-CHECK activity will read this section.*
```

### Status enum

| Status | Meaning |
|--------|---------|
| `candidate` | Considered as a theme; not yet committed to threading through the manuscript |
| `developing` | Threading has begun; appears in some drafted scenes |
| `threaded` | Recurs across the manuscript with consistent treatment |
| `resolved` | The theme's central tension has been honored to the manuscript's conclusion |

### THEME-CHECK activity (new in v1.3.1)

Audits Theme atoms against drafted prose.

Triggering conditions:

- ≥1 Theme atom exists at `developing` or `threaded` status
- ≥5 scenes have been drafted since the theme atom was created or last checked
- ≥10 sessions since last THEME-CHECK
- Before READ-THROUGH

Procedure:

1. Read all Theme atoms
2. Cross-reference with each scene drafted since last check
3. Surface scenes where the theme appears (per `appears_in_scenes`) — is it carried by mechanism, not statement?
4. Surface scenes where the theme *should* appear but doesn't — gaps in the threading
5. Surface any prose where the theme is declared rather than carried (on-the-nose treatment — F42)
6. Cross-reference with related motifs — are the motifs doing the theme's work without the prose announcing it?

Output: theme-treatment report; flags on individual scenes; updates to `appears_in_scenes`.

### Distinction from non-fiction `_argument.md`

`_argument.md` (v1.1, non-fiction) is the logical structure of the book's claim — sub-claims, evidence, defeaters. A non-fiction book's argument is *declared* and *defended*; the reader knows what the argument is by chapter 2 at the latest.

A novel's theme is *carried* and *implied*. The reader may not articulate the theme until after finishing; the theme may even be debated among readers. Theme is to a novel what argument is to non-fiction — same structural slot in the manuscript's intentionality — but the treatment is opposite. `_argument.md` and `LFW_Theme` are not interchangeable.

## §5 — Fiction sub-genre branching

v1.2 treated "fiction" as monolithic. In practice, fiction sub-genres have meaningfully different structural disciplines. v1.3.1 adds a sub-genre field and a small set of sub-genre-specific cues without forking the schema.

### The field

In `_manuscript-manifest.md`:

```yaml
lfw_genre: fiction
lfw_fiction_subgenre: ""    # v1.3.1 — "literary" / "thriller" / "mystery" / "romance" / "sff" / "speculative" / "historical" / "horror" / "ya" / "" (unset)
```

The field is optional; cartridges without it default to "literary-or-unspecified" behavior. Multi-genre works (literary thriller, romantic mystery) declare the dominant sub-genre and note the secondary in voice notes.

### Sub-genre-specific cues

Each sub-genre comes with a small note in this chapter (below) describing the structural elements the OV should be alert to. These cues are *advisory* — they tune the activity-decision algorithm's defaults; they do not change required schema.

#### Literary

- Sequel-beats often the prose's emotional center; tag explicitly
- Theme work is high-priority (Theme atoms expected)
- READER-SIMULATION leans on prose-experience and emotional weight, less on plot-tension
- Beat-sheet overlays optional and often declined
- Motif weave often central

#### Thriller

- Sequel-beats compressed or skipped
- Stakes-ladder escalation across chapters (every chapter must raise stakes)
- Save the Cat overlay often relevant
- Setup-payoff discipline (`_promises.md`) load-bearing — unfired promises are catastrophic
- Theme treatment usually more declared, often through villain's mirrored worldview

#### Mystery

- Clue-tracking layer: every clue should be plant-ed (in plain sight) and pay-off-ed
- `_promises.md` is also the clue-ledger
- Fair-play discipline: the reader must have the same evidence the detective does
- Information-state ledger (`_continuity.md`) is the mystery's central engine
- Often uses Save the Cat or its mystery-adapted variants

#### Romance

- Romance arc beats (meet → conflict → grand-gesture → resolution) overlay onto spine
- Both protagonists' POV often used; POV-VOICE-DRIFT high-priority
- Subtext load-bearing in dialogue (chapter 13)
- Theme of vulnerability-vs-self-protection common
- Sequel-beats often the relationship's reality-checks

#### SFF (Science Fiction / Fantasy)

- `_worldbuilding.md` backbone load-bearing (v1.3.2)
- Setting atom usage expanded — multiple settings, multiple cultures
- Magic / technology rules tracked rigorously in `_continuity.md` world-rules
- Hero's Journey overlay often relevant
- WORLDBUILDING activity high-priority and frequent

#### Speculative

- Single premise-displacement from contemporary reality; everything else holds
- Continuity discipline focused on the displacement's *consequences*, not its mechanism
- Less worldbuilding overhead than SFF; more rigor on consequence-tracking
- Often literary in prose, speculative in premise

#### Historical

- Real-world timeline becomes a Continuity layer (v1.3.2's multi-layer timeline)
- Source atoms repurposed for historical research (non-fic Source atom valid for fiction's research)
- Anachronism risk monitored
- Character bibles often span longer backstories

#### Horror

- Promises and payoffs run on dread-accumulation arcs
- Subtext discipline applies (the unspoken thing in the room)
- Setting atoms often carry atmospheric weight
- Theme often interrogates safety, knowledge, and what is endurable

#### YA

- POV-voice-register often tighter (single dominant register the reader is asked to inhabit)
- Stakes-ladder slightly different (emotional / identity / belonging often dominant)
- Pacing expectations more constrained
- Theme often more direct; on-the-nose tolerance higher than literary

### How the OV uses sub-genre

The activity-decision algorithm in chapter 03 §6 considers `lfw_fiction_subgenre` when proposing defaults. Specifically:

- **Sub-genre with high setup-payoff load (thriller, mystery, horror):** SETUP-PAYOFF-AUDIT triggers earlier (≥6 scenes vs default ≥10)
- **Sub-genre with high POV-voice-register load (romance, multi-POV literary):** POV-VOICE-DRIFT triggers earlier (≥6 sessions vs default ≥8)
- **Sub-genre with high worldbuilding load (SFF, historical):** WORLDBUILDING surfaces as a frequent default; CONTINUITY-CHECK runs more often
- **Sub-genre with high theme load (literary, speculative):** THEME-CHECK runs earlier and more frequently

The sub-genre field is also surfaced to READER-SIMULATION so the simulated reader's expectations match the sub-genre's conventions.

## §6 — Failure modes added in v1.3.1 (continued from chapter 13)

- **F41 — Overlay-as-formula.** Beat-sheet overlay treated as a writing prescription rather than a diagnostic lens; story contorts to hit beats.
- **F42 — On-the-nose theme.** Theme stated by a character or by narration as the novel's thesis. The reader is left no work.
- **F43 — Character-bible becomes worldbuilding-as-procrastination.** Writer expands the bible indefinitely as avoidance of drafting. Same anti-pattern as research-as-procrastination (F-RESEARCH) and craft-work-as-procrastination (F18 from v1.1).
- **F44 — Sub-genre miscalibration.** Cartridge declares a sub-genre whose conventions don't match what's actually being written, and activity defaults misfire. Usually a manifest-update fix.

## §7 — Activity decision-rule additions

Add to chapter 03 §6b':

- **If** ≥1 Theme atom is `developing` or `threaded` AND ≥5 scenes drafted since last check AND ≥10 sessions since last THEME-CHECK → propose **THEME-CHECK**
- **If** `lfw_active_overlays` declares an overlay AND ≥10 scenes drafted AND no overlay-shape-fit assessment in recent sessions → suggest READ-THROUGH with overlay-shape-fit sub-mode
- **If** sub-genre tunings apply (per §5 above) → adjust cadence thresholds for relevant activities

## §8 — Read-order placement

Required reading before THEME-CHECK or when working with Character-Bible atoms. Recommended at BOOTSTRAP for any fiction cartridge — the sub-genre field is best populated at the start, and the theme work is best framed early even if the Theme atom is `candidate` initially.

The beat-sheet overlay templates are read on-demand when the writer chooses to import one.
