---
Item_Prototype: Fleeting
Item_ID: prototype-lfw-craft-log
Title: "LFW_Craft_Log Prototype"
Date_Added: 2026-06-06
Date_Modified: 2026-06-06
Needs_Processing: false
---

# `LFW_Craft_Log` — Prototype Definition

> **What this file is.** The canonical definition of the `LFW_Craft_Log` Prototype for the Long-Form-Writing Operating Volume. Items in any cartridge that declare `Item_Prototype: LFW_Craft_Log` conform to the contract described below.

## Purpose

The Craft Log is the per-cartridge notebook of prose patterns the AI has observed in this manuscript. It is the local-to-the-cartridge counterpart to the OV-root `_craft-profile.md` (`LFW_Craft_Profile`). Patterns observed across sessions are recorded here; recurring patterns may be graduated to the cross-cartridge profile during CRAFT-REVIEW. **Operator-private by default.** Excluded from git tracking. Created at the writer's request, typically a few sessions into the cartridge, when patterns begin to surface that warrant tracking. Per chapter 09 (Writer Development). One file per cartridge.

## Required frontmatter

| Field | Type | Required? | Notes |
|-------|------|-----------|-------|
| `Item_Prototype` | string | yes | Must equal `LFW_Craft_Log` |
| `Item_ID` | string | yes | Format: `<manuscript-slug>-craft-log` |
| `Title` | string | yes | Format: `"<Manuscript Title> — Craft Log"` |
| `Date_Added` | date | yes | When the log was created |
| `Date_Modified` | date | yes | When last changed |
| `lfw_manuscript` | string | yes | Manuscript slug |

## Body structure

```markdown
# <Manuscript Title> — Craft Log

## Patterns observed this cartridge
*Dated entries. Concrete pattern names, cited instances, proposed fixes.*

### <YYYY-MM-DD> — <pattern-name>
**Pattern:**
**Instances in this cartridge:**
**Proposed fix or drill:**
**Status:** active / faded / resolved / graduated-to-profile

## Open questions for the writer
*Things the AI has noticed but isn't sure how to name yet.*

## Practice focus for this manuscript
*What the writer is deliberately working on. Single focus preferred.*

**Currently:**
**Previous foci (this cartridge):**

## Graduations
*Patterns that have crossed into the cross-cartridge profile.*

### <YYYY-MM-DD> — <pattern-name> graduated

## How to use this file
```

## Naming

- **Filename:** `_craft-log.md` (fixed; one per cartridge)
- **Location:** cartridge root
- **Wikilink target:** `_craft-log`

## Example Item

```markdown
---
Item_Prototype: LFW_Craft_Log
Item_ID: the-late-frost-craft-log
Title: "The Late Frost — Craft Log"
Date_Added: 2026-04-30
Date_Modified: 2026-06-04
lfw_manuscript: the-late-frost
---

# The Late Frost — Craft Log

## Patterns observed this cartridge

### 2026-05-02 — Closing-line lift
**Pattern:** End-of-scene paragraphs reach for a metaphorical lift that the scene's grounded prose hasn't earned.
**Instances in this cartridge:**
- 01-01 final paragraph: "the orchard breathing"
- 01-03 final paragraph: "the empty rooms holding their breath"
**Proposed fix or drill:** Try ending three scenes with a flat literal beat instead of an image. Compare which works.
**Status:** active

### 2026-05-19 — Brand-name anchoring works
**Pattern:** When Maya names a specific product or place, the prose tightens and the interiority compounds well.
**Instances in this cartridge:**
- 01-02 "the Hofstra label"
- 01-04 "the green Mason jars"
**Proposed fix or drill:** Lean into this — it's a strength worth keeping.
**Status:** active

## Open questions for the writer
- Maya's sister Sarah's voice hasn't differentiated yet — is the issue dialogue or interiority?

## Practice focus for this manuscript
**Currently:** Closing-line discipline — earn the metaphor or skip it.

## Graduations

### 2026-06-01 — Brand-name anchoring graduated
Observed in this cartridge, in Persistence-Question (earlier non-fiction), and in two previously-shipped short pieces. Cross-cartridge pattern — moved to `_craft-profile.md`.
```

## Relationships

- `LFW_Craft_Profile` — The per-cartridge counterpart that may graduate to the cross-cartridge profile. Both files coexist; the log is per-project, the profile is per-writer.
- `LFW_Session` — Patterns are observed during sessions; entries are added during those sessions, reviewed during CRAFT-REVIEW.
- `LFW_Manuscript_Manifest` — Every Craft Log declares its parent manuscript.

## Notes

- **Operator-private by default.** Sessions and craft work shouldn't leak into public release artifacts. The `.gitignore` excludes `_craft-log.md` by default; `git add -f` if intentionally tracking.
- **Single focus.** The "Practice focus" section deliberately constrains to one item at a time; deliberate practice improves faster on a singular focus than diffuse attention.
- **Diagnostic, not score.** No numeric ratings. Concrete patterns, cited instances, proposed fixes — same standard as the cross-cartridge profile.
- **Graduations require recurrence.** A pattern graduates to `_craft-profile.md` only when observed across multiple cartridges. The AI proposes graduations during CRAFT-REVIEW; the writer confirms.
