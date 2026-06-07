---
Item_Prototype: Fleeting
Item_ID: prototype-lfw-craft-profile
Title: "LFW_Craft_Profile Prototype"
Date_Added: 2026-06-06
Date_Modified: 2026-06-06
Needs_Processing: false
---

# `LFW_Craft_Profile` — Prototype Definition

> **What this file is.** The canonical definition of the `LFW_Craft_Profile` Prototype for the Long-Form-Writing Operating Volume. Items in any cartridge that declare `Item_Prototype: LFW_Craft_Profile` conform to the contract described below.

## Purpose

The Craft Profile is the OV-root cross-cartridge memory of who the writer is on the page. It persists across every cartridge in the OV. **Layer 0 in LFW's three-layer ontology** (per `_writing-engine/_meta/SCHEMA-OF-SCHEMAS.md` § Layer 0). The AI reads this at the start of every session, in every cartridge — without it, every cartridge would be amnesiac about the writer's growth, strengths, working edges, and current practice focus. **Opt-in.** Created by the writer when ready, typically after 5–8 sessions in the first serious cartridge; not auto-created. **Operator-private by default.** Never shipped or shared without the writer's explicit consent.

## Required frontmatter

| Field | Type | Required? | Notes |
|-------|------|-----------|-------|
| `Item_Prototype` | string | yes | Must equal `LFW_Craft_Profile` |
| `Item_ID` | string | yes | Format: `<writer-slug>-craft-profile` |
| `Title` | string | yes | Format: `"<Writer name> — Craft Profile"` |
| `Date_Added` | date | yes | When the profile was created |
| `Date_Modified` | date | yes | When last changed |
| `lfw_writer` | string | yes | Writer name |
| `lfw_cartridges_observed_in` | list[string] | yes | Cartridge slugs this profile has accumulated from |
| `lfw_profile_version` | integer | yes | Bumped on substantial restructuring |

## Body structure

```markdown
# <Writer name> — Craft Profile

## Observed strengths
*Patterns that recur across cartridges and work well. Concrete and named.*

## Observed weaknesses
*Patterns that recur and don't work. Same standard — concrete names, cited instances.*

## Current practice focus
*What the writer is deliberately working on right now. Singular preferred.*

**Currently:**
**Previous foci:** *(append-only history)*

## Pattern log
*Dated entries naming patterns, citing instances, proposing fixes or drills.*

### <YYYY-MM-DD> — <pattern-name>
**Pattern:**
**Instances:** *(specific cartridge + section + sentence)*
**Proposed fix or drill:**
**Status:** active / faded / resolved

## Trajectory
*Coarse summary of how the writer has changed across cartridges. Written sparingly.*

### <YYYY-MM-DD> — <cartridge name> close-out

## How to use this file
```

## Naming

- **Filename:** `_craft-profile.md` (fixed; one per OV-root)
- **Location:** LFW OV root (Layer 0; not inside any cartridge)
- **Wikilink target:** `_craft-profile`

## Example Item

```markdown
---
Item_Prototype: LFW_Craft_Profile
Item_ID: jane-doe-craft-profile
Title: "Jane Doe — Craft Profile"
Date_Added: 2026-04-12
Date_Modified: 2026-06-04
lfw_writer: "Jane Doe"
lfw_cartridges_observed_in:
  - persistence-question
  - the-late-frost
lfw_profile_version: 3
---

# Jane Doe — Craft Profile

## Observed strengths

- **Concrete-naming compounds well.** When the writer names a specific brand, place, or object, the prose tightens and the subsequent interiority lands harder. Observed in *Persistence-Question* Chapter 4 ("the Hofstra archive"), *The Late Frost* 01-02 ("the Mason jars"), and the earlier short *Returnings* ("the 23 bus"). Three cartridges, consistent pattern.
- **Argumentation steelmans early.** Sub-claim defeaters are populated within the first ARGUMENT-AUDIT rather than postponed. Observed across non-fiction cartridges.

## Observed weaknesses

- **Closing-line lift unearned.** Scene-end or chapter-end paragraphs reach for metaphorical heft the grounded prose hasn't paid for. Three instances in *The Late Frost* (01-01, 01-03, 02-02). One in *Persistence-Question* (Chapter 7 close).

## Current practice focus
**Currently:** Closing-line discipline — earn the metaphor or skip it. Carried over from *The Late Frost* §practice-focus.

**Previous foci:**
- 2026-04-12 → 2026-05-18 — Argument-vs-outline alignment in non-fiction (resolved; the writer now runs the alignment check unprompted).

## Pattern log

### 2026-06-01 — Brand-name anchoring (graduated from The Late Frost)
**Pattern:** Naming specific products/places tightens the prose and lifts subsequent interiority.
**Instances:**
- The Late Frost 01-02 — "the Hofstra label"
- Persistence-Question Ch 4 — "the Hofstra archive"
- Returnings (2025 short) — "the 23 bus"
**Status:** active (deliberate continuation)

## Trajectory

### 2026-06-01 — The Late Frost close-out
The writer has consolidated the brand-name anchoring move and identified closing-line lift as the next working edge. Two cartridges of evidence; high confidence on both.
```

## Relationships

- `LFW_Craft_Log` — Per-cartridge patterns are first observed in the cartridge-local Craft Log, then graduated here when they recur across cartridges. The Craft Profile is the cross-cartridge accumulation.
- `LFW_Session` — Read at the start of every session, in every cartridge. Updated during CRAFT-REVIEW sessions (chapter 10-READER).

## Notes

- **Layer 0, not Layer 1.** The Craft Profile lives at the OV root, not inside any cartridge. Per the three-layer ontology in `_writing-engine/_meta/SCHEMA-OF-SCHEMAS.md`, Layer 0 is what makes LFW more than a per-project tool.
- **Opt-in.** Don't auto-create. Create when the writer signals readiness — typically after 5–8 sessions of pattern observation in the first cartridge.
- **Operator-private.** `.gitignore` excludes `_craft-profile.md` by default. `git add -f` to track intentionally.
- **Observational, not scored.** No numeric ratings. No skill levels. The writer recognizes themselves in the profile; that's the test. Per chapter 09.
- **Singular practice focus.** Deliberate practice on one focus at a time produces faster improvement than diffuse attention across three.
- **Graduations need recurrence.** A pattern graduates from `_craft-log.md` to this file only when observed across three or more cartridges. The AI proposes; the writer confirms.
