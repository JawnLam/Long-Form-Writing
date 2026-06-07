---
Item_Prototype: Fleeting
Item_ID: prototype-lfw-setting
Title: "LFW_Setting Prototype"
Date_Added: 2026-06-06
Date_Modified: 2026-06-06
Needs_Processing: false
---

# `LFW_Setting` — Prototype Definition

> **What this file is.** The canonical definition of the `LFW_Setting` Prototype for the Long-Form-Writing Operating Volume. Items in any cartridge that declare `Item_Prototype: LFW_Setting` conform to the contract described below.

## Purpose

A Setting is a named place-and-period where Scenes happen. The Setting Item carries the sensory anchors that make the place feel real rather than schematic (light, sound, smell, texture, the small particulars), plus the place/period frame (where this is; when this is; how the two relate). For plays, the Setting also carries stage requirements (set pieces, sightlines, entrances/exits, lighting/sound needs). Created at the writer's discretion when a setting recurs and the sensory work is worth centralizing. Optional for fiction/screenplay (Scenes can declare their setting inline); typically required for plays where staging matters. Introduced in v1.3.2 (chapter 15 §4 — fiction project artifacts).

## Required frontmatter

| Field | Type | Required? | Notes |
|-------|------|-----------|-------|
| `Item_Prototype` | string | yes | Must equal `LFW_Setting` |
| `Item_ID` | string | yes | Lowercase kebab slug |
| `Title` | string | yes | Setting name |
| `Date_Added` | date | yes | When the Setting was created |
| `Date_Modified` | date | yes | When last changed |
| `Needs_Processing` | boolean | yes | Default `false` |
| `lfw_manuscript` | string | yes | Manuscript slug |
| `lfw_item_type` | enum | yes | Must equal `setting` |
| `lfw_status` | enum | yes | `sketched` \| `defined` \| `final` |
| `lfw_period` | string | yes | Historical or narrative period |
| `lfw_location` | string | yes | Location (literal or fictional) |
| `lfw_scenes_using` | list[wikilink] | optional | Auto-populates from Scene Items' `lfw_setting` references |

## Body structure

```markdown
# <Setting Name>

## Place and period
*Where this setting is. When. The relationship between the two — a 1940s Manhattan apartment is different from a 1990s Manhattan apartment; both are different from a 1940s Brooklyn apartment.*

## Stage requirements
*(Plays only. Optional for fiction/screenplay.)*
*Set pieces, sightlines, entrances/exits, lighting requirements, sound, anything the production needs.*

## Sensory anchors
*What the audience or reader experiences when in this setting. Light, sound, smell, texture, the small particulars that make the setting feel real rather than schematic.*

## Scenes using this setting
*Wikilinks to Scene Items set here. Often auto-populated from Scene Items' `lfw_setting` field.*

## Notes
*Alternate versions considered, mood, what the setting carries thematically.*
```

## Naming

- **Filename pattern:** `<Setting-Name-Slug>.md` (e.g., `Hollis-Family-Vineyard.md`, `The-Apartment.md`)
- **Location:** `<Cartridge>/Items/Settings/`
- **Wikilink target:** the filename

## Example Item

```markdown
---
Item_Prototype: LFW_Setting
Item_ID: hollis-family-vineyard
Title: "Hollis Family Vineyard"
lfw_manuscript: the-late-frost
lfw_item_type: setting
lfw_status: defined
lfw_period: March 2026 (story-time), with backstory layers from 1968 onward
lfw_location: Eastern Long Island, North Fork
lfw_scenes_using:
  - "[[01-01-The-Approach]]"
  - "[[01-02-Frost-Damage-Neighbor]]"
  - "[[01-03-The-Driveway]]"
  - "[[01-04-Empty-House-Walkthrough]]"
  - "[[01-05-The-Letter]]"
  - "[[02-02-The-Garage-Argument]]"
Date_Added: 2026-04-18
Date_Modified: 2026-06-04
Needs_Processing: false
---

# Hollis Family Vineyard

## Place and period
North Fork of Long Island, March 2026. Six acres of Cabernet Franc and Merlot vines, plus the original 1968 Hofstra-family acquisition that the Hollises took over in 1985. The vineyard sits below the kettle-pond level; the house is on the slight rise above the vines. Manhattan is 90 miles west — visible only as light pollution on clear cold nights.

Periodically referenced backstory: the 1968 Hofstra purchase, the 1985 Hollis takeover, Maya's departure in 2006, the father's death in 2018, the mother's death in 2025. Each layer has its own sensory register in the prose.

## Sensory anchors
- **Cold:** March light on the North Fork is *bright* and *flat*. Sun without warmth. The wind has a wet edge from the Sound.
- **Smell:** Wet vine wood. Salt. The dirt is sandy and slightly briny; not the loamy ag-soil of the Hudson Valley.
- **Sound:** Empty. No traffic; no farm machinery this early in season. Gulls. The boiler kicking on inside the house.
- **Color palette:** Grey-brown vines against the still-bare oaks. The house is white clapboard, weather-greyed. The bay across the road is slate.
- **Texture:** The drive is crushed shell and gravel; loud underfoot. The vines are wire-trellised; the sound of wire on stake in wind is constant low-grade.
- **The small particular:** The neighbor Hector's vineyard, which Maya can see from the upstairs windows, has its own different rhythm — earlier pruning, different rootstock choices. The visual asymmetry across the property line is load-bearing.

## Scenes using this setting
- [[01-01-The-Approach]] — Maya driving up
- [[01-02-Frost-Damage-Neighbor]] — at the property line with Hector
- [[01-03-The-Driveway]] — the crushed-shell drive
- [[01-04-Empty-House-Walkthrough]] — interior
- [[01-05-The-Letter]] — Mother's office on the second floor
- [[02-02-The-Garage-Argument]] — in the equipment garage

## Notes
- An alternate setting version considered: 2018 (the father's funeral). Decided against — keeping backstory as interiority, not flashback scenes.
- The neighbor's vineyard asymmetry is the visual carrier for the manuscript's underlying argument about how two people can do the same thing for thirty years and produce different worlds.
```

## Relationships

- `LFW_Scene` — Scenes declare their Setting via `lfw_setting`. The Setting's `lfw_scenes_using` auto-populates from Scene references (bidirectional per chapter 04).
- `LFW_Worldbuilding` — When `_worldbuilding.md` is present (v1.3.2), Settings inherit world rules and may cross-reference deeper worldbuilding material.
- `LFW_Storyboard` — When `_storyboard.md` is present, Settings provide the visual texture the storyboard renders.
- `LFW_Style_Sheet` — Settings often supply lexicon entries (specific terminology like "kettle-pond," "rootstock," "trellised") that the Style Sheet may centralize.
- `LFW_Manuscript_Manifest` — Every Setting declares its parent manuscript via `lfw_manuscript`.

## Notes

- **Place AND period.** A 1940s Manhattan apartment and a 1990s Manhattan apartment are different settings. A 1940s Manhattan apartment and a 1940s Brooklyn apartment are different settings. The intersection is what `lfw_period` × `lfw_location` captures.
- **Sensory anchors > description.** The most-useful Setting Items are not exhaustive descriptions; they are short lists of operative sensory anchors that the prose can reach for as needed. A Setting that says "a New York apartment" is not yet a Setting; one that says "the boiler kicks on every twenty minutes; the radiator in the bedroom is louder than the one in the living room" is.
- **Stage requirements are play-specific.** For plays, the staging discipline is load-bearing — entrances/exits, set pieces, lighting cues. For fiction/screenplay, this section is omittable.
- **Auto-populated reverse references.** `lfw_scenes_using` is maintained automatically as Scene Items add `lfw_setting` references. Per the bidirectional-reference convention; the Setting Item doesn't need manual editing for new Scenes.
- **Optional Prototype.** Many cartridges (especially short-scope or single-setting) don't need Setting Items — the Scene itself can carry the sensory anchors inline. Use Setting when a place recurs and the work of writing it consistently is worth centralizing.
