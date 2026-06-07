---
Item_Prototype: Fleeting
Item_ID: prototype-lfw-worldbuilding
Title: "LFW_Worldbuilding Prototype"
Date_Added: 2026-06-06
Date_Modified: 2026-06-06
Needs_Processing: false
---

# `LFW_Worldbuilding` — Prototype Definition

> **What this file is.** The canonical definition of the `LFW_Worldbuilding` Prototype for the Long-Form-Writing Operating Volume. Items in any cartridge that declare `Item_Prototype: LFW_Worldbuilding` conform to the contract described below.

## Purpose

The Worldbuilding file is the **world-design backbone for SFF, fantasy, speculative, alt-history, and horror cartridges** requiring deep system-building. It documents cosmology, physical/natural systems (geography, climate, ecology, calendar, astronomy), technology/magic (what's possible, what's not, what costs what, edge cases), cultures, political structures, economy, languages, religions, and deep history. Distinct from `_continuity.md` — Worldbuilding holds the *rules*; Continuity tracks adherence to them. Single per-cartridge file at `_worldbuilding.md`. **Required backbone for SFF/fantasy/speculative/alt-history/horror with non-natural elements.** Cartridges in contemporary realism do not need this file. WORLDBUILDING activities extend (not duplicate) and propose CONTINUITY-CHECK at session-end (v1.2, chapter 12 §5). Introduced in v1.3.2 (chapter 15 §1). The anti-procrastination check is load-bearing: worldbuilding-as-procrastination is F45 — the world serves the story, not the reverse.

## Required frontmatter

| Field | Type | Required? | Notes |
|-------|------|-----------|-------|
| `Item_Prototype` | string | yes | Must equal `LFW_Worldbuilding` |
| `Item_ID` | string | yes | Format: `<manuscript-slug>-worldbuilding` |
| `Title` | string | yes | Format: `"<World Name> — Worldbuilding"` |
| `Date_Added` | date | yes | When the file was created |
| `Date_Modified` | date | yes | When last changed |
| `lfw_manuscript` | string | yes | Manuscript slug |
| `lfw_worldbuilding_version` | integer | yes | Bumped on substantial restructuring |

## Body structure

```markdown
# <World Name> — Worldbuilding

## What this world is
*One paragraph. The world's central premise / displacement from default reality.*

## Cosmology
*If applicable. Metaphysical structure.*

## Physical / natural systems
### Geography
### Climate
### Ecology
### Calendar
### Astronomy

## Technology / magic
### What's possible
### What's not
### What costs what
*Magic/technology that does X is not free.*
### Edge cases

## Cultures
### <Culture name>
- **History (in brief):**
- **Values (load-bearing):**
- **Social structure:**
- **Language(s) spoken:**
- **Religion / belief:**
- **Material culture:**
- **Politics:**
- **Relationship to other cultures:**

## Political structures
## Economy
## Languages
### Invented vocabulary
## Religions / belief systems
## History (deep)
*May reference `LFW_Timeline` Items with `lfw_timeline_layer: world-history`.*

## Open questions

## Anti-procrastination check
*Per chapter 15 §1: F45 (worldbuilding-as-procrastination). The world serves the story; the story does not serve the world.*
```

## Naming

- **Filename:** `_worldbuilding.md` (fixed; one per cartridge)
- **Location:** cartridge root
- **Wikilink target:** `_worldbuilding`

## Example Item

```markdown
---
Item_Prototype: LFW_Worldbuilding
Item_ID: the-iron-archive-worldbuilding
Title: "The Iron Archive — Worldbuilding"
Date_Added: 2026-03-20
Date_Modified: 2026-06-04
lfw_manuscript: the-iron-archive
lfw_worldbuilding_version: 3
---

# The Iron Archive — Worldbuilding

## What this world is
A late-Bronze-Age polity (loosely modeled on Hittite/Mycenaean) where writing is iron-stylus on annealed clay; the institution of the Archive (a guild of trained scribes) is the load-bearing political body because they alone can produce inheritable inscriptions. The displacement from real-world Bronze Age: writing has political power equivalent to a priesthood or a hereditary aristocracy.

## Physical / natural systems

### Geography
A peninsula bounded by a mountain range to the north and the sea to the south, east, and west. Three river-valleys feed the central plain. Climate is hot-arid summer, mild-wet winter. Most habitation is along the rivers.

### Calendar
Twelve months tied to agricultural and ritual cycles. Years are reckoned from the founding of the Archive (currently year 412 AF — "After Founding"). Months align with stellar risings.

### Astronomy
Two visible planets named in the language as `Selat` and `Vahrun`; their conjunction every ~18 years marks the Archive's renewal-of-vows ceremony.

## Technology / magic
This world has no magic. The displacement is sociological, not metaphysical: writing-as-political-power is the speculative element. All physical technology is consistent with c. 1300 BCE Mediterranean.

### What's possible
- Iron-stylus on clay tablets (annealed to fire-hardness for permanence)
- Cuneiform-style script with 87 base symbols
- The Archive's recording of contracts, land claims, royal acts is what makes them politically operative

### What's not
- No paper, no ink, no parchment (a deliberate constraint shaping the politics)
- No printing
- No telegraphy or rapid communication

### What costs what
- A single contract tablet takes a trained scribe ~3 hours of work
- Iron styli are the property of the Archive; scribes do not own their tools
- Clay tablets that have not yet been annealed can be erased; once annealed, they are permanent. The annealing decision is its own political act.

## Cultures

### The Archive
- **History:** Founded year 0 AF (412 years ago, story-time). Originally a scribal guild attached to the temple of the lost goddess Iras; survived the temple's destruction in year 67 AF and absorbed the temple's archival role.
- **Values:** Permanence over expediency. The annealing decision is the Archive's central ritual. Truth-as-inscribed.
- **Social structure:** Hierarchical. Apprentices (years 1–7), Inscribers (years 8–20), Annealers (~50 in the polity), Council of Annealers (12 elected).

### The Court
- **History:** The royal family of the polity, currently in its 14th generation. The current king is weak; the regent (his mother) is the operative power.
- **Values:** Dynastic continuity. Land. Lineage.
- **Relationship to the Archive:** Co-dependent. The king is legitimate because the Archive recognizes him; the Archive has political reach because the king grants its authority.

### The Merchant Houses
- **History:** Trading guilds across the three river-valleys; rose in the past century from local merchants to inter-polity traders.
- **Values:** Trade routes, treaty access, wealth as social mobility.
- **Relationship to the Archive:** Increasingly conflicted. Merchants want contracts inscribed *quickly*; Annealers refuse to be rushed. This is the manuscript's core political conflict.

## Languages
The polity has one official language, `Hattil`. Two trade-pidgins exist for cross-polity commerce.

### Invented vocabulary
*(Substantial — cross-reference [[The-Iron-Archive-Style-Sheet]] lexicon section)*

## History (deep)
Cross-reference [[Iron-Archive-World-History-Founding-to-412AF]] for the full Timeline at `world-history` layer.

## Open questions
- [ ] What exactly happened to the temple of Iras in year 67 AF? Currently vague; may need to be specific by midpoint of drafting.
- [ ] Is the regent's relationship to the Archive being kept deliberately ambiguous, or is the writer avoiding committing?

## Anti-procrastination check
**Current word-count:** worldbuilding file is 4,200 words; manuscript is 18,500 words drafted. Ratio is acceptable.

**Last sentence drafted:** [[02-04-The-Annealing-Refusal]] mid-scene (working in DRAFT).

**Anti-procrastination ruling:** The Worldbuilding is operative — every section is referenced in at least one drafted scene's continuity check. No expansion has been deferred to "later"; current rules suffice for current drafts. If the writer finds themselves opening this file without an active scene-question, that's the F45 alarm.
```

## Relationships

- `LFW_Continuity` — Continuity tracks adherence to Worldbuilding rules. The two are co-dependent: World-rules live here; Continuity verifies drafted prose against them.
- `LFW_Timeline` — Deep-history portions of Worldbuilding may delegate to `LFW_Timeline` Items at `world-history` layer.
- `LFW_Style_Sheet` — Invented vocabulary defined in Worldbuilding feeds the Style Sheet's lexicon section.
- `LFW_Setting` — Settings inherit world-rules from Worldbuilding; particular sensory anchors live in Settings, while the underlying rules live here.
- `LFW_Overlay_Heros_Journey` — Often pairs with Worldbuilding (mythic/fantasy structures benefit from both).
- `LFW_Manuscript_Manifest` — Required backbone for SFF/fantasy/speculative/alt-history/horror; conditional declaration based on `lfw_fiction_subgenre`.

## Notes

- **Genre-required.** Required for SFF, fantasy, speculative, alt-history, and horror cartridges with non-natural elements. Optional or skipped for contemporary realism (whose "worldbuilding" is the writer's everyday-world fluency).
- **F45 — Worldbuilding-as-procrastination.** The most dangerous failure mode for this Prototype. When this file grows faster than the manuscript itself, the writer is procrastinating in the guise of preparation. WORLDBUILDING activities propose CONTINUITY-CHECK at session-end as a discipline pivot — the rules just established must be checked against drafted prose, which forces return to drafting.
- **Anti-procrastination check section is mandatory in body.** The section exists to force the writer to confront the worldbuilding-vs-drafting ratio. If the ratio is acceptable, the section is a heartbeat check; if it's not, the section is the alarm.
- **World serves story, not the reverse.** Per chapter 15 §1. Rules that are not referenced in drafted prose are speculative architecture — keep, but don't expand without scene-demand.
- **Distinct from `_continuity.md`.** Worldbuilding holds rules; Continuity verifies adherence. The two files have orthogonal responsibilities; don't duplicate rules in both.
- **Deep history may delegate to Timeline Items.** For worlds with extensive backstory, the Worldbuilding's `History (deep)` section can be brief, deferring to `LFW_Timeline` Items at `world-history` layer for full chronology.
- **WORLDBUILDING activity (v1.2, chapter 12 §5)** is the in-session work that extends this file. Per v1.2: WORLDBUILDING extends, doesn't duplicate; activity proposes CONTINUITY-CHECK at session-end to maintain the world-served-by-story discipline.
