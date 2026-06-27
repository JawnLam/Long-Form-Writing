---
type: Fleeting
timestamp: "2026-06-06T00:00:00Z"
Item_ID: type-lfw-section
title: "LFW_Section Type"
Date_Added: 2026-06-06
Date_Modified: 2026-06-06
Needs_Processing: false
---

# `LFW_Section` — Type Definition

> **What this file is.** The canonical definition of the `LFW_Section` Type for the Long-Form-Writing Operating Volume. Items in any cartridge that declare `type: LFW_Section` conform to the contract described below.

## Purpose

A Section is the non-fiction analog to fiction's Scene — a sub-chapter unit of prose that argues or narrates one bounded thing. Sections compose Chapters; Beats may compose Sections (for tightly-structured non-fiction). Each Section has a declared purpose, the Threads it engages, the Sources it cites, and a single dramatic/argumentative role in the chapter. Genre scope: non-fiction and dissertation cartridges. (Fiction/screenplay/play cartridges use Scenes instead.) Created when an Outline's planned section is ready to be drafted.

## Required frontmatter

| Field | Type | Required? | Notes |
|-------|------|-----------|-------|
| `type` | string | yes | Must equal `LFW_Section` |
| `Item_ID` | string | yes | Lowercase kebab slug |
| `Title` | string | yes | Section title |
| `Date_Added` | date | yes | When the Section was created |
| `Date_Modified` | date | yes | When last changed |
| `Needs_Processing` | boolean | yes | Default `false` |
| `lfw_manuscript` | string | yes | Manuscript slug |
| `lfw_item_type` | enum | yes | Must equal `section` |
| `lfw_status` | enum | yes | `planned` \| `drafting` \| `drafted` \| `revising` \| `revised` \| `fact-checked` \| `final` |
| `lfw_parent` | wikilink | yes | Parent Chapter |
| `lfw_order_in_parent` | integer | yes | Sequential position within the Chapter |
| `lfw_purpose` | string | yes | One sentence: what this section argues or narrates |
| `lfw_threads_engaged` | list[wikilink] | optional | Thread Items addressed in this Section |
| `lfw_sources_cited` | list[wikilink] | optional | Source Items cited in this Section |
| `lfw_first_drafted` | date | optional | Null until drafted |
| `lfw_word_count` | integer | yes | Current word count |

## Body structure

```markdown
# <Section title>

## Purpose
*What this section is for in the chapter's argument or narrative. One or two sentences.*

## Beats
*Ordered list of beats in this section. Wikilinks to Beat Items.*

1. [[Beat-slug-1]]
2. [[Beat-slug-2]]

## Prose
*Drafted content. Or `*To be drafted*` if not yet.*

## Sources Used
*Wikilinks to Source Items cited in this section.*
- [[Source-slug]]

## Threads Engaged
*Wikilinks to Thread Items.*
- [[Thread-slug]]

## Open Notes
*Weaknesses, fact-checks pending, alternate approaches, things to verify.*
```

## Naming

- **Filename pattern:** `<Chapter-N>-<Section-MM>-<short-title-slug>.md` (e.g., `03-01-Tainter-Setup.md`)
- **Location:** `<Cartridge>/Items/Sections/`
- **Wikilink target:** the filename

## Example Item

```markdown
---
type: LFW_Section
timestamp: "2026-06-02T00:00:00Z"
Item_ID: 03-01-tainter-setup
title: "Tainter Setup: marginal returns as collapse mechanism"
lfw_manuscript: persistence-question
lfw_item_type: section
lfw_status: drafted
lfw_parent: "[[Chapter-03-Family-Business-Persistence]]"
lfw_order_in_parent: 1
lfw_purpose: "Introduce Tainter's marginal-returns model as the framework Chapter 3 will pressure-test against family-business persistence data."
lfw_threads_engaged:
  - "[[Selection-Pressure-Hostile-But-Not-Lethal]]"
  - "[[Adaptive-Ritual]]"
lfw_sources_cited:
  - "[[Tainter-Collapse-1988]]"
  - "[[Schein-Organizational-Culture-and-Leadership-2010]]"
lfw_first_drafted: 2026-05-29
lfw_word_count: 2840
Date_Added: 2026-05-15
Date_Modified: 2026-06-02
Needs_Processing: false
---

# Tainter Setup: marginal returns as collapse mechanism

## Purpose
This section establishes Joseph Tainter's marginal-returns model of civilizational collapse and previews Chapter 3's argument that the model survives transposition from civilizations to family businesses with one modification: the lethality threshold.

## Beats
1. [[03-01-Beat-01-Tainters-Argument-Summary]]
2. [[03-01-Beat-02-The-Lethality-Threshold-Question]]
3. [[03-01-Beat-03-Why-Family-Businesses-Are-A-Test-Case]]

## Prose
The argument from *The Collapse of Complex Societies* (Tainter, 1988) is widely misread as economic — costs exceed benefits, complexity unsustainable, collapse follows. The economic frame is real but secondary. What Tainter actually argues is selective…

*(prose continues)*

## Sources Used
- [[Tainter-Collapse-1988]] — primary framework source
- [[Schein-Organizational-Culture-and-Leadership-2010]] — used for the institutional-culture analog in Beat 03

## Threads Engaged
- [[Selection-Pressure-Hostile-But-Not-Lethal]] — Beat 02 advances this thread by establishing the lethality threshold as a load-bearing variable
- [[Adaptive-Ritual]] — touched in Beat 03's family-business transposition

## Open Notes
- Beat 02's lethality-threshold argument needs one more empirical example beyond Easter Island; currently feels Easter-Island-dependent
- Fact-check: Tainter's exact phrasing of "complexity as a problem-solving response" — make sure the citation is precise
```

## Relationships

- `LFW_Chapter` — Sections compose Chapters via `lfw_parent` and the Chapter's `Composition` body section.
- `LFW_Beat` — Beats compose Sections (when present); the Section's Beats are referenced in its body and each Beat declares `lfw_parent` pointing here.
- `LFW_Source` — Sections cite Sources via `lfw_sources_cited`. Sources may reciprocally track Sections that cite them via `lfw_sections_citing`.
- `LFW_Thread` — Sections engage Threads via `lfw_threads_engaged`; Threads track their carrying Sections.
- `LFW_Argument` — The Section's purpose maps onto one or more sub-claims in the Argument backbone.
- `LFW_Manuscript_Manifest` — Every Section declares its parent manuscript via `lfw_manuscript`.

## Notes

- **Section ≠ Scene.** Sections are non-fiction's per-chapter unit; Scenes are fiction's. The two are deliberately separate Types so per-genre activities and audits can target the right Item type.
- **`lfw_status` includes `fact-checked`.** Non-fiction Items have an extra revision stage beyond fiction's revision cycle: factual accuracy is a separate concern from prose-line revision. Per chapter 07 (Revision Discipline).
- **Beats are optional.** A Section may compose directly of prose (one block) or may decompose into Beat Items. The choice depends on how tightly structured the chapter is; argumentative chapters typically benefit from Beat-level decomposition.
- **`lfw_sources_cited` and `lfw_threads_engaged` are bidirectional.** Per chapter 04's bidirectional-reference convention, the Source/Thread Items reciprocally list Sections that cite/engage them. The validator's check 5 flags asymmetries.
