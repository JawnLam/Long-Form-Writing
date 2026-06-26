---
type: LFW_Continuity
Item_ID: "<manuscript-slug>-continuity"
title: "<Manuscript Title> — Continuity Ledger"
Date_Added:
Date_Modified:
lfw_manuscript: "<manuscript-slug>"
lfw_continuity_version: 1
---

# <Manuscript Title> — Continuity Ledger

> **Verification ledger for fiction continuity. Three sections: world rules (for genre fiction with worldbuilding), timeline (for any non-trivial fiction), and the information-state ledger (who-knows-what, load-bearing for any plot with secrets). CONTINUITY-CHECK sessions verify drafted prose against this ledger (chapter 12 §4).**

## World rules

*Enumerated rules about how the world works. Each rule cites the scene where it's established. Updated when a new rule is introduced; checked when scenes reference relevant mechanics.*

### Rule 1 — <short name>

**Established in:** [[Scene-filename]]
**Rule:** *(precise statement; the kind of statement that can be violated)*
**Implications:** *(what this rule constrains in later scenes)*

### Rule 2 — <short name>

*(repeat per rule)*

## Timeline

*Explicit chronology of in-story events. Dated or sequenced. Critical for novels covering long spans or using non-chronological narration.*

| When | What | Where in the manuscript | Notes |
|------|------|-------------------------|-------|
| <date or sequence-N> | <event> | [[Scene-filename]] |  |

## Information-state ledger

*For each load-bearing piece of information (secret, hidden identity, plot-relevant fact), track who knows it as of each scene. The reader can be tracked as a "character" too — the dramatic-irony moments depend on this.*

### Info-item 1 — <short label>

**The information:** *(precise; what is or isn't known)*
**First introduced in:** [[Scene-filename]] *(who in-world knows it from this point)*

| Scene | Maya | Sarah | Mother | Reader |
|-------|------|-------|--------|--------|
| [[Scene-A]] | knows | doesn't know | knows | doesn't know |
| [[Scene-B]] | knows | knows (just told) | knows | knows |

### Info-item 2 — <short label>

*(repeat per load-bearing information item)*

## Continuity check log

*Append-only record of CONTINUITY-CHECK sessions: what was checked, what issues were found, what was resolved.*

### <YYYY-MM-DD> — CONTINUITY-CHECK session N

**Scope:** *(scenes checked)*
**Issues found:** *(list)*
**Resolved:** *(list — by scene revision, rule revision, or recognized-as-intentional)*

---

## How to use this file

For the AI:

- Read at session start when activity is CONTINUITY-CHECK, WORLDBUILDING, or any session drafting a fiction scene that references continuity items
- Test drafted prose against this ledger during CONTINUITY-CHECK (chapter 12 §4)
- Propose updates to the ledger when WORLDBUILDING introduces new rules
- Never silently revise prose to fix continuity — surface; the writer judges

For the writer:

- Update when new world rules are established
- Update when characters learn or transmit information
- Treat as living document; bump `lfw_continuity_version` on substantial restructuring
