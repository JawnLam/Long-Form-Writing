---
Item_Prototype: Fleeting
Item_ID: prototype-lfw-continuity
Title: "LFW_Continuity Prototype"
Date_Added: 2026-06-06
Date_Modified: 2026-06-06
Needs_Processing: false
---

# `LFW_Continuity` — Prototype Definition

> **What this file is.** The canonical definition of the `LFW_Continuity` Prototype for the Long-Form-Writing Operating Volume. Items in any cartridge that declare `Item_Prototype: LFW_Continuity` conform to the contract described below.

## Purpose

The Continuity Ledger is the verification artifact for fiction continuity — what world rules have been established, when in-story events occur, and who knows what as of each scene. It exists as a single per-cartridge file at `_continuity.md`. **Required backbone for fiction with worldbuilding (SFF, fantasy, speculative, alt-history, horror) and any plot with secrets.** CONTINUITY-CHECK sessions (chapter 12 §4) verify drafted prose against this ledger. Created at cartridge bootstrap for relevant genres; populated as world rules and information-state evolve. The information-state ledger is load-bearing for dramatic-irony management — the reader is tracked as a "character" alongside the in-world cast.

## Required frontmatter

| Field | Type | Required? | Notes |
|-------|------|-----------|-------|
| `Item_Prototype` | string | yes | Must equal `LFW_Continuity` |
| `Item_ID` | string | yes | Format: `<manuscript-slug>-continuity` |
| `Title` | string | yes | Format: `"<Manuscript Title> — Continuity Ledger"` |
| `Date_Added` | date | yes | When the ledger was created |
| `Date_Modified` | date | yes | When last changed |
| `lfw_manuscript` | string | yes | Manuscript slug |
| `lfw_continuity_version` | integer | yes | Bumped on substantial restructuring |

## Body structure

```markdown
# <Manuscript Title> — Continuity Ledger

## World rules
*Enumerated rules about how the world works. Each rule cites the scene where established.*

### Rule 1 — <short name>
**Established in:** [[Scene-filename]]
**Rule:** *(precise statement; the kind that can be violated)*
**Implications:** *(what this constrains in later scenes)*

## Timeline
*Explicit chronology of in-story events.*

| When | What | Where in the manuscript | Notes |
|------|------|-------------------------|-------|

## Information-state ledger
*For each load-bearing piece of information, track who knows it as of each scene.*

### Info-item 1 — <short label>
**The information:**
**First introduced in:** [[Scene-filename]]

| Scene | Char-A | Char-B | Char-C | Reader |
|-------|--------|--------|--------|--------|

## Continuity check log
*Append-only record of CONTINUITY-CHECK sessions.*

### <YYYY-MM-DD> — CONTINUITY-CHECK session N
**Scope:** *(scenes checked)*
**Issues found:**
**Resolved:**

## How to use this file
```

## Naming

- **Filename:** `_continuity.md` (fixed; one per cartridge)
- **Location:** cartridge root
- **Wikilink target:** `_continuity`

## Example Item

```markdown
---
Item_Prototype: LFW_Continuity
Item_ID: the-late-frost-continuity
Title: "The Late Frost — Continuity Ledger"
Date_Added: 2026-04-22
Date_Modified: 2026-06-04
lfw_manuscript: the-late-frost
lfw_continuity_version: 2
---

# The Late Frost — Continuity Ledger

## World rules

### Rule 1 — Vineyard ownership transfers via the family trust, not direct will
**Established in:** [[01-01-The-Approach]]
**Rule:** Maya and Sarah are co-trustees of the Hollis Family Trust; the property cannot be sold without unanimous trustee approval.
**Implications:** Sarah cannot force the sale alone; Maya cannot block it forever. Plot pressure arises from this constraint.

## Timeline

| When | What | Where in the manuscript | Notes |
|------|------|-------------------------|-------|
| 1968 | Mother arrives at vineyard | (backstory, not on-page) | |
| 2006 | Sisters' rift | [[01-04-Empty-House-Walkthrough]] | Recalled in interiority |
| March 2026 | Maya returns | [[01-01-The-Approach]] | Opening scene |

## Information-state ledger

### Info-item 1 — The letter from Mother to Maya (last will alternative)
**The information:** Mother left a handwritten letter for Maya only, naming a third trustee option Sarah doesn't know about.
**First introduced in:** [[01-05-The-Letter]]

| Scene | Maya | Sarah | Hector | Reader |
|-------|------|-------|--------|--------|
| [[01-01-The-Approach]] | doesn't know | doesn't know | doesn't know | doesn't know |
| [[01-05-The-Letter]] | knows | doesn't know | doesn't know | knows |
| [[02-02-The-Garage-Argument]] | knows | doesn't know | doesn't know | knows |
| [[02-01-Sarah-Finds-The-Letter]] | knows | knows (just found) | doesn't know | knows |

## Continuity check log

### 2026-05-15 — CONTINUITY-CHECK session 1
**Scope:** Chapters 1–2 (drafted to date)
**Issues found:** In 01-03, Maya references the trust structure before establishing it in 01-01. Timing problem.
**Resolved:** Added two-line establishment in 01-01 §2.
```

## Relationships

- `LFW_Scene` — All world-rule establishments, timeline entries, and information-state transitions cite Scene Items via wikilinks. CONTINUITY-CHECK verifies drafted Scenes against this ledger.
- `LFW_Character` — Information-state ledger columns track per-character knowledge.
- `LFW_Worldbuilding` — When `_worldbuilding.md` is present (v1.3.2), world rules in Continuity reference the deeper worldbuilding material in Worldbuilding; the two stay synchronized.
- `LFW_Manuscript_Manifest` — Required backbone for fiction with worldbuilding or plot-with-secrets; declared via genre + flags.
- `LFW_Promises` — Promises (setup/payoff) often interact with information-state; the two ledgers cross-reference.

## Notes

- **One per cartridge.** Single file at cartridge root, not a folder of Items.
- **Genre-conditional.** Required for fiction with worldbuilding (any non-natural elements) or plot with secrets. Validator's continuity check is conditional on cartridge declaration in `_manuscript-manifest.md`.
- **Reader as character.** The information-state ledger treats the reader as a tracked entity. Dramatic-irony moments (reader knows what character doesn't, or vice versa) become explicit and audit-able.
- **CONTINUITY-CHECK is the activity.** Don't silently revise prose to fix continuity; surface and let the writer judge. Per chapter 12 §4.
