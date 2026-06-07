---
Item_Prototype: Fleeting
Item_ID: prototype-lfw-spine
Title: "LFW_Spine Prototype"
Date_Added: 2026-06-06
Date_Modified: 2026-06-06
Needs_Processing: false
---

# `LFW_Spine` — Prototype Definition

> **What this file is.** The canonical definition of the `LFW_Spine` Prototype for the Long-Form-Writing Operating Volume. Items in any cartridge that declare `Item_Prototype: LFW_Spine` conform to the contract described below.

## Purpose

The Spine is fiction's **causal backbone** — the scene-by-scene value-shift map plus the but/therefore connectors that make the manuscript a *plot* rather than a *sequence*. **Required backbone for fiction, screenplay, and play cartridges.** Distinct from the Outline (which is the container hierarchy — Parts, Chapters, Sections). The Spine answers *what causes what* and *what shifts at each beat*; the Outline answers *what's the shape*. SCENE-AUDIT sessions pressure-test the Spine against drafted scenes. Introduced in v1.2 (chapter 11 — fiction plot/spine). Single per-cartridge file at `_spine.md`. The Stakes-ladder section was added in v1.3.2 (chapter 15 §7).

## Required frontmatter

| Field | Type | Required? | Notes |
|-------|------|-----------|-------|
| `Item_Prototype` | string | yes | Must equal `LFW_Spine` |
| `Item_ID` | string | yes | Format: `<manuscript-slug>-spine` |
| `Title` | string | yes | Format: `"<Manuscript Title> — Causal Spine"` |
| `Date_Added` | date | yes | When the spine was created |
| `Date_Modified` | date | yes | When last changed |
| `lfw_manuscript` | string | yes | Manuscript slug |
| `lfw_spine_version` | integer | yes | Bumped on substantial restructuring |

## Body structure

```markdown
# <Manuscript Title> — Causal Spine

## Premise as causal claim
**Premise:** *(the *because*: because [protagonist] [wants/fears], and because [obstacle], the story must unfold)*

## The dramatic question
**Dramatic question:** *(the yes/no or which question the whole manuscript answers)*

## Scene-by-scene value-shifts
| # | Scene | Type | POV | From → To (scenes) / Decision (sequels) | But/Therefore connector |
|---|-------|------|-----|------------------------------------------|-------------------------|

## Cause→effect linkage
- **But / Therefore connections:** <count>
- **And then connections:** <count>

## Escalation curve
- **Mid-act crisis:**
- **Climax:**

## Stakes ladder *(v1.3.2)*
| Chapter | Personal | Relational | Societal | Existential | Notes |
|---------|----------|------------|----------|-------------|-------|

**Stakes-level taxonomy:**
- **Personal** — what the protagonist privately stands to gain/lose
- **Relational** — what their key relationships stand to gain/lose
- **Societal** — what the broader world stands to gain/lose
- **Existential** — what their fundamental identity/being stands to gain/lose

## Escalation map *(optional)*
| Scene | Pressure | Notes |
|-------|----------|-------|

## The honest open
*What's not yet causal; scenes the writer suspects exist for reasons other than causality.*

## Revision log
### <YYYY-MM-DD> — v1
```

## Naming

- **Filename:** `_spine.md` (fixed; one per cartridge)
- **Location:** cartridge root
- **Wikilink target:** `_spine`

## Example Item

```markdown
---
Item_Prototype: LFW_Spine
Item_ID: the-late-frost-spine
Title: "The Late Frost — Causal Spine"
Date_Added: 2026-04-19
Date_Modified: 2026-06-04
lfw_manuscript: the-late-frost
lfw_spine_version: 4
---

# The Late Frost — Causal Spine

## Premise as causal claim
**Premise:** Because Maya needs to settle her mother's estate but cannot fully grieve until she settles the rift with her sister, and because the estate's trust governance forces them into a binary decision, the story must unfold toward a confrontation where each sister's version of the past is exposed and neither version is preserved intact.

## The dramatic question
**Dramatic question:** Can Maya and Sarah co-decide the vineyard's future, or will the third-trustee option that their mother left as a tiebreaker be exercised?

## Scene-by-scene value-shifts
| # | Scene | Type | POV | From → To / Decision | Connector |
|---|-------|------|-----|----------------------|-----------|
| 1 | [[01-01-The-Approach]] | scene | Maya | distant → arriving | **therefore** the empty house must be entered |
| 2 | [[01-02-Frost-Damage-Neighbor]] | scene | Maya | unaware → aware-of-fragility | **therefore** the estate's economic situation enters her mind |
| 3 | [[01-03-The-Driveway]] | scene | Maya | arriving → present | **therefore** the house's emptiness can be felt |
| 4 | [[01-04-Empty-House-Walkthrough]] | sequel | Maya | decision: open Mother's office | **therefore** the next scene's want is to read Mother's papers |
| 5 | [[01-05-The-Letter]] | scene | Maya | private → carrying-a-secret | **but** despite this secret, the rift with Sarah cannot remain a private problem |
| ... | | | | | |

## Cause→effect linkage
- **But / Therefore connections:** 18
- **And then connections:** 3 — at scenes 7, 11, 14 (review at next SCENE-AUDIT)

## Escalation curve
- **Mid-act crisis:** [[02-02-The-Garage-Argument]] — Sarah confronts Maya; the rift is now scene-present rather than memory; from confrontable to inflamed
- **Climax:** (planned: Chapter 6) — the third-trustee option is invoked; each sister must accept what she has not been willing to accept

## Stakes ladder
| Chapter | Personal | Relational | Societal | Existential | Notes |
|---------|----------|------------|----------|-------------|-------|
| 1 | Maya's grief | Sarah-distance | (none) | (none) | Personal-and-relational only — appropriate for an opening |
| 2 | Maya's culpability for the rift | Direct sister-conflict | (none) | (none) | |
| 3 | Both sisters' versions of Mother | Mother-as-third-presence | Vineyard economic viability | (none) | Societal layer enters |
| 4 | Maya's self-knowledge | Sister-bond test | Vineyard viability | (none) | |
| 5 | (planned) Maya's claim to selfhood | Sister-renegotiation | Vineyard's future | What it means to inherit | Existential enters; deliberate, not premature |
| 6 | (planned, climax) | (planned, climax) | (planned, climax) | (planned, climax) | All four layers operative |

**Inverted-pyramid check:** Existential stakes are deliberately deferred until Chapter 5; the manuscript does not front-load existential framing. This is the literary-fiction pattern of earning the existential through the personal.

## The honest open
- Scene 7's value-shift is unclear in the current draft; the scene may exist for setup-purposes that should be redistributed across 6 and 8.
- The Mid-act crisis at 02-02 is the strongest scene; subsequent scenes have not yet earned their pressure.

## Revision log
### 2026-04-19 — v1
Created. Initial spine extracted from outline; connector ratio 14 but/therefore to 4 and-then. Stakes ladder began as personal+relational only.

### 2026-05-12 — v2
After CHAR-AUDIT, the third-trustee option (Promise 1) was confirmed as the climax mechanism. Stakes ladder gained societal layer at Chapter 3.

### 2026-05-30 — v3 / 2026-06-04 — v4
Stakes-ladder existential entry at Chapter 5 confirmed as the right moment. Connector ratio improved to 18:3.
```

## Relationships

- `LFW_Scene` — Spine references every Scene Item via wikilinks; each Scene's value-shift contributes to the spine row.
- `LFW_Promises` — Spine's setups/payoffs are tracked in `_promises.md`; the two files cross-reference often.
- `LFW_Continuity` — Spine answers what-causes-what; Continuity answers what-the-world-and-information-state-are. The two are orthogonal but mutually constraining.
- `LFW_Outline` — Outline structures the shape; Spine structures the causality. Argument-vs-outline alignment in non-fiction has a fiction counterpart: spine-vs-outline alignment in fiction.
- `LFW_Overlay_*` — Active overlays read the spine through their lens. The spine is the canonical structure; overlays are diagnostic.
- `LFW_Manuscript_Manifest` — Required backbone for fiction/screenplay/play; declared via `lfw_genre`.

## Notes

- **One per cartridge, required for fiction.** Validator's spine check fails any fiction/screenplay/play cartridge missing `_spine.md`.
- **The connector word matters.** A spine dominated by "and then" is *sequence*, not *plot*. The But/Therefore vs And-Then ratio is a diagnostic; falling below ~3:1 toward but/therefore is a sign the spine has loosened.
- **Sequel-typed scenes carry decisions, not value-shifts.** Per v1.3.1 (chapter 14 §1 scene-and-sequel rhythm). Sequel-typed scenes are exempt from value-shift requirements; they instead carry the next scene's want.
- **Stakes ladder is v1.3.2 addition.** Tracks stakes at four levels per Chapter; F51 (flat stakes) is what this section surfaces. Existential stakes appearing by Chapter 3 leaves the rest of the manuscript no escalation room — flag if accidental; honor if deliberate.
- **Revision log is append-only.** Each spine revision gets a dated entry. Versions captured in `lfw_spine_version`.
- **Update as scenes draft.** The Spine is a living document; SCENE-AUDIT during drafting tests prose against the spine, and either tightens the prose or revises the spine — never silently.
