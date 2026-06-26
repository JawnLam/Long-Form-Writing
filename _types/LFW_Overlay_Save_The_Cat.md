---
type: Fleeting
timestamp: "2026-06-06T00:00:00Z"
Item_ID: prototype-lfw-overlay-save-the-cat
title: "LFW_Overlay_Save_The_Cat Prototype"
Date_Added: 2026-06-06
Date_Modified: 2026-06-06
Needs_Processing: false
---

# `LFW_Overlay_Save_The_Cat` — Prototype Definition

> **What this file is.** The canonical definition of the `LFW_Overlay_Save_The_Cat` Prototype for the Long-Form-Writing Operating Volume. Items in any cartridge that declare `type: LFW_Overlay_Save_The_Cat` conform to the contract described below.

## Purpose

A Save the Cat Overlay is an opt-in **reading lens** that maps the manuscript's structure onto Blake Snyder's fifteen-beat sheet (originally for screenplays, since adapted to novels). Best fit: commercial fiction — thriller, mystery, romance, YA, SFF. Opt-in via `lfw_active_overlays: [save-the-cat]` in the Manifest. One overlay file per active overlay per cartridge. Introduced in v1.3.1 (chapter 14 §2). Like all overlays: a reading lens, not a prescription. If the spine doesn't fit, the overlay is the wrong lens. This overlay is the most weaponized of the four and the most-criticized as formula — apply it carefully.

## Required frontmatter

| Field | Type | Required? | Notes |
|-------|------|-----------|-------|
| `type` | string | yes | Must equal `LFW_Overlay_Save_The_Cat` |
| `Item_ID` | string | yes | Format: `<manuscript-slug>-overlay-save-the-cat` |
| `Title` | string | yes | Format: `"<Manuscript Title> — Save the Cat Overlay"` |
| `Date_Added` | date | yes | When the overlay was added |
| `Date_Modified` | date | yes | When last changed |
| `lfw_manuscript` | string | yes | Manuscript slug |
| `lfw_overlay_type` | enum | yes | Must equal `save-the-cat` |
| `lfw_overlay_version` | integer | yes | Bumped on substantial restructuring |

## Body structure

```markdown
# <Manuscript Title> — Save the Cat Overlay

## The fifteen beats
*For a ~80,000-word novel, beats land approximately at the percentages noted.*

| # | Beat | Approx % | Scene(s) | Notes |
|---|------|----------|----------|-------|
| 1 | Opening Image | 0–1% | | |
| 2 | Theme Stated | 5% | | |
| 3 | Set-Up | 1–10% | | |
| 4 | Catalyst | 10% | | |
| 5 | Debate | 10–20% | | |
| 6 | Break Into Act Two | 20% | | |
| 7 | B Story | 22% | | |
| 8 | Fun and Games | 20–50% | | |
| 9 | Midpoint | 50% | | |
| 10 | Bad Guys Close In | 50–75% | | |
| 11 | All Is Lost | 75% | | |
| 12 | Dark Night of the Soul | 75–80% | | |
| 13 | Break Into Act Three | 80% | | |
| 14 | Finale | 80–99% | | |
| 15 | Final Image | 99–100% | | |

## Shape-fit assessment
- **Beats with clear coverage:**
- **Beats with uncertain coverage:**
- **Beats with no coverage:**
- **% positioning:** *(audit — are beats landing at roughly the percentages?)*

## Divergence notes

## Risks

## How to use this overlay

## Cross-reference
```

## Naming

- **Filename:** `_overlay-save-the-cat.md` (fixed; one per cartridge with this overlay active)
- **Location:** cartridge root
- **Wikilink target:** `_overlay-save-the-cat`

## Example Item

```markdown
---
type: LFW_Overlay_Save_The_Cat
timestamp: "2026-06-04T00:00:00Z"
Item_ID: a-thriller-overlay-save-the-cat
title: "A Thriller — Save the Cat Overlay"
lfw_manuscript: a-thriller
lfw_overlay_type: save-the-cat
lfw_overlay_version: 1
Date_Added: 2026-05-19
Date_Modified: 2026-06-04
---

# A Thriller — Save the Cat Overlay

## The fifteen beats

| # | Beat | Approx % | Scene(s) | Notes |
|---|------|----------|----------|-------|
| 1 | Opening Image | 0–1% | [[01-01-Morning-Run]] | The protagonist at her most ordinary |
| 2 | Theme Stated | 5% | [[01-02-Coffee-Shop]] | The barista's offhand remark about trust |
| 3 | Set-Up | 1–10% | [[01-01]]–[[01-04]] | Four scenes; Act One on track |
| 4 | Catalyst | 10% | [[01-05-The-Phone-Call]] | |
| 5 | Debate | 10–20% | [[01-06]]–[[02-02]] | Protagonist refuses for three scenes |
| 6 | Break Into Act Two | 20% | [[02-03-The-Flight-To-London]] | |
| 7 | B Story | 22% | [[02-04-Meeting-James]] | The romantic subplot — carrier of theme |
| 8 | Fun and Games | 20–50% | [[02-05]]–[[03-04]] | The premise's promise — what the back-cover sold |
| 9 | Midpoint | 50% | [[03-05-The-Apartment-Search]] | False win — protagonist thinks she's solved it |
| 10 | Bad Guys Close In | 50–75% | [[03-06]]–[[04-03]] | |
| 11 | All Is Lost | 75% | [[04-04-James-Is-Missing]] | |
| 12 | Dark Night of the Soul | 75–80% | [[04-05-Alone-In-The-Apartment]] | The change-decision forms |
| 13 | Break Into Act Three | 80% | [[04-06-The-Plan]] | A-story and B-story synthesize |
| 14 | Finale | 80–99% | [[05-01]]–[[05-05]] | |
| 15 | Final Image | 99–100% | [[05-05-Morning-Run-Reprise]] | Mirrors Opening Image with the change shown |

## Shape-fit assessment
- **Beats with clear coverage:** all fifteen
- **% positioning:** Act One closes at 22% (target 20%); slight overrun but acceptable for thriller pacing
- **Notes:** Beat 2 (Theme Stated) lands without being on-the-nose — the barista's remark is the carrier, not a speech

## Divergence notes
- The B Story (romantic subplot) ends in James's death rather than romantic synthesis. This is a deliberate genre choice — the thriller's emotional shape doesn't require the romance to succeed.

## Risks
- The "Fun and Games" section (20–50%) is the place where pacing can sag. Currently OK; revisit during READ-THROUGH.
```

## Relationships

- `LFW_Spine` — Spine is causal-claim backbone; the Save the Cat lens reads it through the fifteen beats. Spine wins on conflicts.
- `LFW_Promises` — Save the Cat's setups often map onto promises that need firing in the Finale. Cross-reference `_promises.md` when applying this overlay.
- `LFW_Scene` — Beats reference Scene Items via wikilinks.
- `LFW_Outline` — The Outline's structural shape is what the overlay assesses.
- `LFW_Manuscript_Manifest` — Active overlays declared in `lfw_active_overlays`.

## Notes

- **Best fit:** commercial fiction — thriller, mystery, romance, YA, SFF. For literary fiction, prefer `LFW_Overlay_Freytag` (climax-in-the-middle) or `LFW_Overlay_Story_Circle` (relational-shape).
- **The fifteen-beat checklist trap.** Don't treat the beats as a fill-in-the-blanks form. The overlay is most useful for auditing whether the major turning points (Catalyst, Midpoint, All Is Lost, Finale) are present and earning their position. The minor beats (Theme Stated, B Story) are diagnostic, not constructive.
- **% positioning is a targeting cue.** Beats landing at roughly the percentages is healthy; beats forced to the percentages produce mechanical pacing. Use as a tell, not as a rule.
- **Theme Stated is the most common F42 (on-the-nose theme) site.** Have a character mention something related; do not state the thesis. Beat 2 is the easiest to get wrong.
- **Act One past 25% is a red flag for commercial pacing.** Save the Cat is reasonable about this — Act One is *short* in commercial fiction. If the overlay diagnoses overlong Act One, that's useful information.
