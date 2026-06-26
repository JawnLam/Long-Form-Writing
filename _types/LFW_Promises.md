---
type: Fleeting
timestamp: "2026-06-06T00:00:00Z"
Item_ID: prototype-lfw-promises
title: "LFW_Promises Prototype"
Date_Added: 2026-06-06
Date_Modified: 2026-06-06
Needs_Processing: false
---

# `LFW_Promises` — Prototype Definition

> **What this file is.** The canonical definition of the `LFW_Promises` Prototype for the Long-Form-Writing Operating Volume. Items in any cartridge that declare `type: LFW_Promises` conform to the contract described below.

## Purpose

The Promises Ledger is the setup/payoff tracking artifact — every setup planted in the manuscript and whether it has been fired. **Required backbone for plot-driven fiction.** Single per-cartridge file at `_promises.md`. SETUP-PAYOFF-AUDIT sessions (chapter 11 §4) work against this file. Tracks four states: outstanding (planted, awaiting payoff), fired (paid off — earned or unearned), retired (decided not to pay off), and reverse-mapped payoffs-without-setups (the unearned-payoff defect). Each promise records its planting scene, the implied payoff shape, and the foreshadow trail. Created at cartridge bootstrap for plot-driven fiction. Introduced in v1.2 (chapter 11 — fiction plot/spine).

## Required frontmatter

| Field | Type | Required? | Notes |
|-------|------|-----------|-------|
| `type` | string | yes | Must equal `LFW_Promises` |
| `Item_ID` | string | yes | Format: `<manuscript-slug>-promises` |
| `Title` | string | yes | Format: `"<Manuscript Title> — Setup/Payoff Ledger"` |
| `Date_Added` | date | yes | When the ledger was created |
| `Date_Modified` | date | yes | When last changed |
| `lfw_manuscript` | string | yes | Manuscript slug |
| `lfw_promises_version` | integer | yes | Bumped on substantial restructuring |

## Body structure

```markdown
# <Manuscript Title> — Setup/Payoff Ledger

## Promises planted
### Promise 1 — <short name>
- **Planted in:** [[Scene-filename]]
- **Concerns:** *(character, object, situation)*
- **Implied payoff:** *(what shape will fire this promise)*
- **Status:** outstanding | fired | retired
- **Foreshadow trail:** *(scenes where the promise is reinforced)*

## Promises fired
### Payoff 1 — <short name>
- **Fired in:** [[Scene-filename]]
- **Discharges promise:** Promise N above
- **Earned?** earned | unearned | mixed
- **Notes:**

## Promises currently outstanding
*Setups planted but not yet paid off. Flag long-outstanding without foreshadowing.*

## Payoffs without setups
*Reveals or moves the reader will experience as arbitrary because they weren't planted.*

## Promises retired
### Retired promise 1 — <short name>
- **Originally planted in:** [[Scene-filename]]
- **Retired on:** <YYYY-MM-DD>
- **Reason:**
- **Action taken:** *(setup removed / left as red herring / repurposed)*

## How to use this file
```

## Naming

- **Filename:** `_promises.md` (fixed; one per cartridge)
- **Location:** cartridge root
- **Wikilink target:** `_promises`

## Example Item

```markdown
---
type: LFW_Promises
timestamp: "2026-06-04T00:00:00Z"
Item_ID: the-late-frost-promises
title: "The Late Frost — Setup/Payoff Ledger"
Date_Added: 2026-04-22
Date_Modified: 2026-06-04
lfw_manuscript: the-late-frost
lfw_promises_version: 3
---

# The Late Frost — Setup/Payoff Ledger

## Promises planted

### Promise 1 — Mother's letter (third trustee option)
- **Planted in:** [[01-05-The-Letter]]
- **Concerns:** Trust governance; Maya/Sarah's ability to settle the estate
- **Implied payoff:** The third-trustee option will become operative when Sarah and Maya cannot agree.
- **Status:** outstanding
- **Foreshadow trail:** [[02-02-The-Garage-Argument]] (Maya nearly mentions; checks herself); [[02-03-Hector-Intervenes]] (the third party is named in passing)

### Promise 2 — The frost damage was not natural
- **Planted in:** [[01-02-Frost-Damage-Neighbor]]
- **Concerns:** The vineyard's economic viability; the antagonist's hand
- **Implied payoff:** Reveal of who damaged the vines and why
- **Status:** outstanding
- **Foreshadow trail:** *none yet planted*; **fading risk** — should reinforce in Chapter 3 or retire

## Promises fired

*(none yet — first draft mid-Act 2)*

## Promises currently outstanding

- **Promise 1** ([[01-05-The-Letter]]) — outstanding for 5 scenes; foreshadow trail present; healthy
- **Promise 2** ([[01-02-Frost-Damage-Neighbor]]) — outstanding for 8 scenes; **no foreshadow trail since planting** — fading risk

## Payoffs without setups

*(none flagged in current draft)*

## Promises retired

### Retired promise 1 — The Hofstra wine-club correspondence
- **Originally planted in:** [[01-02-Frost-Damage-Neighbor]] (early draft)
- **Retired on:** 2026-05-08
- **Reason:** This setup pointed toward a subplot about Mother's wine-club friendships that doesn't survive the focused-sisters structure of the current draft.
- **Action taken:** Setup removed in second draft; the neighbor's dialogue no longer mentions the wine club.
```

## Relationships

- `LFW_Scene` — Promises wikilink the Scene Items where setup is planted and payoff is fired. The `prefigures` relation (v1.2) on Scene Items is the canonical mechanism for declaring promises.
- `LFW_Spine` — The Spine is the causal-claim backbone; Promises track the setups/payoffs that the spine's causal chain depends on.
- `LFW_Continuity` — Continuity tracks who-knows-what; Promises track what-needs-firing. The two are orthogonal but cross-reference often (information-state transitions often pay off as promises).
- `LFW_Manuscript_Manifest` — Required backbone for plot-driven fiction; declared via genre and subgenre flags.

## Notes

- **One per cartridge.** Single file at cartridge root, not a folder of Items.
- **Genre-conditional.** Required for plot-driven fiction (thrillers, mysteries, plotted literary fiction). Optional for character-driven literary fiction whose causal chain is interior. SCREENPLAY and PLAY cartridges typically need it because tight runtime forces every setup to fire.
- **The `prefigures` relation is the index.** Per v1.2 (chapter 11), every `prefigures` link in a Scene Item should appear here as a promise; every promise should have a corresponding `prefigures` on the planting scene. Drift between the two surfaces during SETUP-PAYOFF-AUDIT.
- **The four states matter.** "Outstanding" without foreshadow trail is the fading-promise defect. "Fired-unearned" is the under-set-up defect. "Payoff without setup" is the arbitrary-reveal defect. "Retired" is honest housekeeping — documenting retirement prevents re-treating retired setups as outstanding.
- **Update during drafting, not only during audit.** Add a promise entry every time a significant setup is planted; the audit is for checking, not for first-time discovery. (Per chapter 11 §4.)
