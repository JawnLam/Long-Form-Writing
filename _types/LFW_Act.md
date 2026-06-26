---
type: Fleeting
timestamp: "2026-06-06T00:00:00Z"
Item_ID: prototype-lfw-act
title: "LFW_Act Prototype"
Date_Added: 2026-06-06
Date_Modified: 2026-06-06
Needs_Processing: false
---

# `LFW_Act` — Prototype Definition

> **What this file is.** The canonical definition of the `LFW_Act` Prototype for the Long-Form-Writing Operating Volume. Items in any cartridge that declare `type: LFW_Act` conform to the contract described below.

## Purpose

An Act is a top-level structural division in a screenplay or play — the largest unit between the manuscript root and individual Scenes. Each Act has a discrete dramatic purpose (the Act 1 question, the Act 2 escalation, the Act 3 resolution, etc.) and contains an ordered list of Scenes. Created when the operator outlines a screenplay or play and needs an explicit container for the Scenes that comprise each dramatic movement. Genre scope: screenplays, plays. Optional for novels (whose top-level container is `LFW_Chapter`) and not used in non-fiction or dissertation cartridges.

## Required frontmatter

| Field | Type | Required? | Notes |
|-------|------|-----------|-------|
| `type` | string | yes | Must equal `LFW_Act` |
| `Item_ID` | string | yes | Lowercase kebab slug, unique within the cartridge |
| `Title` | string | yes | Format: `"Act <N>: <Title>"` |
| `Date_Added` | date | yes | When the Act was created |
| `Date_Modified` | date | yes | When last changed |
| `Needs_Processing` | boolean | yes | Default `false` |
| `lfw_manuscript` | string | yes | Manuscript slug this Act belongs to |
| `lfw_item_type` | enum | yes | Must equal `act` |
| `lfw_status` | enum | yes | `planned` \| `drafting` \| `drafted` \| `revising` \| `revised` \| `final` |
| `lfw_order_in_parent` | integer | yes | Sequential position within the manuscript |
| `lfw_purpose` | string | yes | One-sentence statement of what this Act does dramatically |
| `lfw_target_page_count` | integer | optional | Screenplay convention: pages ≈ minutes |
| `lfw_first_drafted` | date | optional | Null until first draft exists |

## Body structure

```markdown
# Act <N>: <Title>

## Purpose
*What this act accomplishes in the screenplay or play. One paragraph.*

## Composition
*Ordered list of Scenes that make up this act. Wikilinks.*

1. [[Scene-filename-1]]
2. [[Scene-filename-2]]

## Open Notes
*Act-level issues — pacing, scope, dramatic-arc completion within this act.*

## Revision History
| Date | Pass | Changes summary |
|------|------|-----------------|
```

## Naming

- **Filename pattern:** `Act-<N>-<short-title-slug>.md` (e.g., `Act-01-Setup.md`, `Act-02-Confrontation.md`)
- **Location:** `<Cartridge>/Items/Acts/`
- **Wikilink target:** the slug

## Example Item

```markdown
---
type: LFW_Act
timestamp: "2026-06-04T00:00:00Z"
Item_ID: act-02-the-confrontation
title: "Act 2: The Confrontation"
lfw_manuscript: the-late-frost
lfw_item_type: act
lfw_status: drafting
lfw_order_in_parent: 2
lfw_purpose: "Sarah forces Maya to reveal what she's hiding about the property sale."
lfw_target_page_count: 30
lfw_first_drafted: 2026-05-12
Date_Added: 2026-05-10
Date_Modified: 2026-06-04
Needs_Processing: false
---

# Act 2: The Confrontation

## Purpose
Sarah's discovery of the will document forces Maya into a choice she has been postponing for three weeks. By act-end, both sisters know the truth and the family conflict is now open.

## Composition
1. [[02-01-Sarah-Finds-The-Letter]]
2. [[02-02-The-Garage-Argument]]
3. [[02-03-Hector-Intervenes]]

## Open Notes
- Pacing feels rushed in 02-02; consider splitting into two scenes.
- The garage argument carries too much exposition.
```

## Relationships

- `LFW_Chapter` — Acts and Chapters are alternative top-level containers. Screenplays/plays use Acts; novels use Chapters. A manuscript declares one or the other in `_manuscript-manifest.md`.
- `LFW_Scene` — Acts *contain* Scenes via `Composition` wikilinks. Each Scene declares its parent Act via `lfw_parent` frontmatter.
- `LFW_Beat` — Beats are the atomic dramatic units within Scenes; Acts contain Scenes contain Beats.
- `LFW_Spine` — The `_spine.md` cross-references Acts as the highest structural layer when present.
- `LFW_Manuscript_Manifest` — Every Act declares its parent manuscript via `lfw_manuscript`.

## Notes

- **Genre scope.** Acts are required for screenplay and play cartridges. Optional for novels (which may use Acts as a Part-level organization above Chapters, or skip them entirely). Not used in non-fiction or dissertation cartridges (which use Sections instead).
- **Page count is screenplay-specific.** The `lfw_target_page_count` field assumes the screenplay convention of one page ≈ one minute of screen time. For plays, omit or repurpose as an approximate runtime target.
- **Per `_writing-engine/_meta/SCHEMA-OF-SCHEMAS.md` § Layer 2,** Acts are part of the per-genre branch. The screenplay and play branches add `_spine.md` as required backbone and use Acts as the top-level structural container.
