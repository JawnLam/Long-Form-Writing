---
type: Fleeting
timestamp: "2026-06-06T00:00:00Z"
Item_ID: prototype-lfw-theme
title: "LFW_Theme Prototype"
Date_Added: 2026-06-06
Date_Modified: 2026-06-06
Needs_Processing: false
---

# `LFW_Theme` — Prototype Definition

> **What this file is.** The canonical definition of the `LFW_Theme` Prototype for the Long-Form-Writing Operating Volume. Items in any cartridge that declare `type: LFW_Theme` conform to the contract described below.

## Purpose

A Theme is the **abstract idea or tension** the manuscript is exploring — carried, not declared. Distinct from `LFW_Motif` (the *physical* recurring element) and from `LFW_Argument` (which is non-fiction's explicit thesis). A Theme is the question or tension the manuscript is asking *through* its plot, characters, and motifs. Created when the writer identifies a load-bearing thematic concern; revised throughout drafting. **Genre scope: fiction, screenplay, play.** Carried-not-declared: the discipline is to never state the theme in the prose as the novel's thesis. Introduced in v1.3.1 (chapter 14 §4). THEME-CHECK activities work against Theme Items.

## Required frontmatter

| Field | Type | Required? | Notes |
|-------|------|-----------|-------|
| `type` | string | yes | Must equal `LFW_Theme` |
| `Item_ID` | string | yes | Lowercase kebab slug |
| `Title` | string | yes | Format: `"Theme — <Name>"` |
| `Date_Added` | date | yes | When the Theme was identified |
| `Date_Modified` | date | yes | When last changed |
| `Needs_Processing` | boolean | yes | Default `false` |
| `lfw_manuscript` | string | yes | Manuscript slug |
| `lfw_item_type` | enum | yes | Must equal `theme` |
| `lfw_status` | enum | yes | `candidate` \| `developing` \| `threaded` \| `resolved` |
| `lfw_priority` | enum | yes | `central` \| `secondary` \| `incidental` |
| `lfw_appears_in_scenes` | list[wikilink] | optional | Scene Items where this theme is carried |
| `lfw_related_motifs` | list[wikilink] | optional | Motif Items that carry this theme |
| `lfw_related_characters` | list[wikilink] | optional | Characters who embody or test this theme |

## Body structure

```markdown
# Theme — <Name>

## What this theme is
*The abstract idea, in plain words. Articulate as a question or a tension, not a thesis-statement.*

## Why this theme matters in this manuscript
*Specifically why THIS theme is load-bearing for THIS book.*

## How it's carried (not declared)
- **Through character:** *(which characters embody which positions)*
- **Through motif:** *(which motifs carry the theme)*
- **Through plot-shape:** *(how the spine enacts the theme)*
- **Through dramatic question:** *(how the dramatic question is also thematic)*

## Tension within the theme
*A theme treated as a single position is preachment. A theme treated as a tension between positions is literature.*

- **Position A:**
- **Position B:**
- **What the manuscript does with the tension:**

## Where it surfaces (scene-by-scene)
| Scene | How the theme appears | Position carried |
|-------|----------------------|------------------|

## What it must NOT do
*(failure modes)*

## Treatment risks for this manuscript

## Audit notes
*THEME-CHECK findings.*
```

## Naming

- **Filename pattern:** `<Theme-Name-Slug>.md` (e.g., `Inheritance-As-Burden.md`, `Honesty-Under-Cost.md`)
- **Location:** `<Cartridge>/Items/Themes/`
- **Wikilink target:** the filename

## Example Item

```markdown
---
type: LFW_Theme
timestamp: "2026-06-04T00:00:00Z"
Item_ID: inheritance-as-burden
title: "Theme — Inheritance As Burden"
lfw_manuscript: the-late-frost
lfw_item_type: theme
lfw_status: threaded
lfw_priority: central
lfw_appears_in_scenes:
  - "[[01-04-Empty-House-Walkthrough]]"
  - "[[01-05-The-Letter]]"
  - "[[02-02-The-Garage-Argument]]"
lfw_related_motifs:
  - "[[The-Late-Frost]]"
  - "[[Mothers-Letter]]"
lfw_related_characters:
  - "[[Maya-Hollis]]"
  - "[[Sarah-Hollis]]"
Date_Added: 2026-04-26
Date_Modified: 2026-06-04
Needs_Processing: false
---

# Theme — Inheritance As Burden

## What this theme is
The tension between inheritance as gift and inheritance as obligation. When something is left to you — a vineyard, a sister, a version of yourself — what part of receiving it is choosing it?

## Why this theme matters in this manuscript
The Late Frost is not a "story about an inheritance" in the cliché sense. The inheritance is the test the sisters have to take in order to confront the rift. The thematic question — what you must accept in order to inherit, and what you can refuse — is the same question the spine asks plot-wise.

## How it's carried (not declared)
- **Through character:** Maya embodies the refusal-to-receive (she has built a life in Boston explicitly to not-inherit). Sarah embodies the obligation-to-receive (she has stayed and resented and worked). Both are wrong; both are right.
- **Through motif:** The Late Frost (the physical event that almost killed the vines) carries the theme — frost is the inheritance the vineyard didn't ask for and must adapt to. The Mother's Letter is the explicit inheritance the daughters are forced to negotiate.
- **Through plot-shape:** The spine's question (can they co-decide?) is structurally the thematic question (can they co-accept?).
- **Through dramatic question:** Same question, plot-side. The answer to the dramatic question is also the answer to the thematic question.

## Tension within the theme
- **Position A:** Inheritance is gift. Receiving it is the act of honoring what was given. Refusing is ingratitude.
- **Position B:** Inheritance is constraint. Receiving it is the obligation to live a life shaped by what was given. Refusing is sovereignty.
- **What the manuscript does with the tension:** Both positions are steelmanned; neither sister is right; both grow only when they recognize the other's position is real. The manuscript refuses to choose.

## Where it surfaces (scene-by-scene)
| Scene | How the theme appears | Position carried |
|-------|----------------------|------------------|
| [[01-04-Empty-House-Walkthrough]] | Maya inventorying what's been kept and not-kept | Position A (briefly); refused |
| [[01-05-The-Letter]] | Mother's letter as an unwanted inheritance Maya is now responsible for | Both (tension begins) |
| [[02-02-The-Garage-Argument]] | Sarah's "you don't get to walk away again" lands as Position B | B |

## What it must NOT do
- Be stated by any character as the novel's thesis ("This is about inheritance" — never)
- Resolve neatly (no clean A-wins or B-wins ending)
- Become a motif's stated meaning (the late frost stays a frost; never "the late frost is, of course, inheritance itself")
- Be the answer to the dramatic question (the dramatic question's answer is the third-trustee option's invocation; the theme is what is *illuminated* by that answer)

## Treatment risks for this manuscript
- The metaphor (frost ≈ inheritance) is heavy-handed in the title. Resist any sentence in the prose that closes the gap. The title can carry the metaphor; the prose must not.
- Sarah's POV (if added) risks tipping into Position B as the manuscript's "answer." Maintain the refusal-to-choose.

## Audit notes

### 2026-05-22 — THEME-CHECK session 1
**Surfaced:** Maya's interiority in 01-04 was reaching for Position A explicitly ("the gift of being trusted with this") — too close to thesis-statement. Cut.
**Changed:** Replaced with the inventory beat — Maya naming what's been kept, the specific objects. The theme now arrives through the objects, not through Maya's commentary.
```

## Relationships

- `LFW_Motif` — Themes are carried *through* Motifs. Each Motif Item declares which Themes it carries; each Theme lists its carrying Motifs. The asymmetric pair lets Motifs stay physical while Themes stay abstract.
- `LFW_Character` — Themes are embodied *by* Characters. Each Character's `## Arc` may engage one or more Themes; the Theme's `lfw_related_characters` tracks the reciprocal.
- `LFW_Scene` — Scenes carry Themes; the Theme Item's `lfw_appears_in_scenes` tracks the manifestation.
- `LFW_Spine` — Dramatic question often *is* the thematic question structurally. Spine and Theme cross-reference often.
- `LFW_Manuscript_Manifest` — Optional Items; not declared in Manifest by default.

## Notes

- **Carried-not-declared is load-bearing.** The discipline of *not* stating the theme is what separates literature from preachment. THEME-CHECK is the activity that holds the line.
- **Themes are tensions, not positions.** A theme treated as a single position becomes thesis. A theme treated as a tension becomes literature. Position A and Position B must both be steelmanned for the theme to do its work.
- **Status taxonomy.** `candidate` (writer suspects this theme is present), `developing` (the theme is showing up in drafts but isn't yet fully threaded), `threaded` (the theme appears in the right places to do its work), `resolved` (the manuscript's relationship to the theme is now stable; revisions won't move it).
- **Priority taxonomy.** `central` (load-bearing for the manuscript), `secondary` (present and operative but not load-bearing), `incidental` (touched once or twice; not worth Item-tracking unless promoted).
- **F42 — on-the-nose theme.** The most common failure mode. Surfaces when a character is given a speech that states the theme; resist always. (Even in Save the Cat's "Theme Stated" beat 2 — the rule is *related*, not *stated*.)
- **Subgenre fit.** Theme Items pay off best in literary fiction. Commercial fiction may treat theme more lightly; high-concept genre fiction sometimes has theme as a side dish rather than a load-bearing concern.
