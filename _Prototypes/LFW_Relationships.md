---
Item_Prototype: Fleeting
Item_ID: prototype-lfw-relationships
Title: "LFW_Relationships Prototype"
Date_Added: 2026-06-06
Date_Modified: 2026-06-06
Needs_Processing: false
---

# `LFW_Relationships` — Prototype Definition

> **What this file is.** The canonical definition of the `LFW_Relationships` Prototype for the Long-Form-Writing Operating Volume. Items in any cartridge that declare `Item_Prototype: LFW_Relationships` conform to the contract described below.

## Purpose

The Relationships Map is the symmetric multi-character relationship artifact — a single per-cartridge file at `_relationships.md` that maps the pairwise (and triangular) dynamics between named characters. It complements the per-Character `## Relationships` body section (which is asymmetric — each character's one-sided view) by providing the symmetric, all-pairs view that surfaces asymmetry drift. Most useful for novels with five or more named characters whose interlocking dynamics matter. Optional backbone. Read during CHARACTER-CONSISTENCY and READ-THROUGH activities. Introduced in v1.3.2 (chapter 15 §6).

## Required frontmatter

| Field | Type | Required? | Notes |
|-------|------|-----------|-------|
| `Item_Prototype` | string | yes | Must equal `LFW_Relationships` |
| `Item_ID` | string | yes | Format: `<manuscript-slug>-relationships` |
| `Title` | string | yes | Format: `"<Manuscript Title> — Relationship Map"` |
| `Date_Added` | date | yes | When the map was created |
| `Date_Modified` | date | yes | When last changed |
| `lfw_manuscript` | string | yes | Manuscript slug |
| `lfw_relationships_version` | integer | yes | Bumped on substantial restructuring |

## Body structure

```markdown
# <Manuscript Title> — Relationship Map

## Cast
*Roster of named characters whose relationships are mapped here.*
- [[Character-1]]
- [[Character-2]]

## All-pairs matrix
|              | Char 1 | Char 2 | Char 3 |
|--------------|--------|--------|--------|
| **Char 1**   | —      | s1     | s2     |
| **Char 2**   | s1     | —      | s3     |
| **Char 3**   | s2     | s3     | —      |

## Per-pair detail
### s1 — [[Character-1]] ↔ [[Character-2]]
- **Type:** *(sisters / lovers / colleagues / antagonists / mentor-student / parent-child)*
- **History:**
- **Current state at manuscript opening:**
- **Evolution arc across the manuscript:**
- **Subtext:** *(what's unspoken between them)*
- **Asymmetry:** *(how do their one-sided views differ? Is asymmetry intentional or drift?)*

## Triangle dynamics *(optional)*
*Three-character relationships with load-bearing dynamics.*

## Audit notes
*CHARACTER-CONSISTENCY findings about asymmetry drift.*
```

## Naming

- **Filename:** `_relationships.md` (fixed; one per cartridge)
- **Location:** cartridge root
- **Wikilink target:** `_relationships`

## Example Item

```markdown
---
Item_Prototype: LFW_Relationships
Item_ID: the-late-frost-relationships
Title: "The Late Frost — Relationship Map"
Date_Added: 2026-05-08
Date_Modified: 2026-06-04
lfw_manuscript: the-late-frost
lfw_relationships_version: 2
---

# The Late Frost — Relationship Map

## Cast
- [[Maya-Hollis]]
- [[Sarah-Hollis]]
- [[Hector-Reyes]]
- [[Mother]] *(deceased; relationships carry into Items as memory)*

## All-pairs matrix
|              | Maya | Sarah | Hector | Mother |
|--------------|------|-------|--------|--------|
| **Maya**     | —    | s1    | s2     | s3     |
| **Sarah**    | s1   | —     | s4     | s5     |
| **Hector**   | s2   | s4    | —      | s6     |
| **Mother**   | s3   | s5    | s6     | —      |

## Per-pair detail

### s1 — [[Maya-Hollis]] ↔ [[Sarah-Hollis]]
- **Type:** Sisters; estranged
- **History:** Maya left at 18 after the rift (specifics still being decided in OUTLINE). Twenty years of intermittent contact, increasingly distant after their father's death in 2018.
- **Current state at manuscript opening:** Civil, distant. Sarah resents Maya's absence; Maya doesn't know how to apologize for what she also doesn't fully understand she did.
- **Evolution arc across the manuscript:** From distant civility → confrontation (Ch 2) → tentative repair → collapse → quiet acceptance of asymmetry (Maya's growth) or rebuilding (Sarah's growth). Final state: both/neither, deliberately ambiguous.
- **Subtext:** Each carries her own version of what happened in 2006. Neither's version is fully accurate.
- **Asymmetry:** Maya's Item characterizes Sarah as "the one who stayed and resents me." Sarah's Item (not yet drafted) will characterize Maya as "the one who left and never looked back." The asymmetry is *intentional* — the manuscript's working argument is that the rift is the asymmetry, not a single event.

### s2 — [[Maya-Hollis]] ↔ [[Hector-Reyes]]
- **Type:** Neighbor, near-stranger transitioning to ally
- **History:** Hector arrived at the next-door vineyard when Maya was already gone; he knew the parents in their later years
- **Current state at manuscript opening:** Acquaintance
- **Evolution arc:** Becomes a load-bearing minor ally in Act 2

## Triangle dynamics

### Triangle: Maya ↔ Sarah ↔ Mother
**Dynamic:** Each sister has a different version of Mother. The rift in 2006 was, in part, a fight about which Mother was the real one. Mother's letter (Promise 1) is operative here — she anticipated the asymmetry and prepared the third-trustee option as a tiebreaker the sisters cannot wield against each other.

## Audit notes

### 2026-05-22 — CHARACTER-CONSISTENCY session 1
**Finding:** Maya's Item describes Sarah as "resentful" in three scenes; Sarah's first appearance (drafted 2026-05-12) does not show that resentment textually — Sarah is *cool*, not resentful. Either Maya's interiority is unreliable (intentional — she expects resentment she doesn't actually see) or the drafted Sarah needs to land the resentment.
**Decision:** Maya's interiority is unreliable here. Leave Maya's Item as-is; add a note in Maya's `## Subtext` about her expectation-vs-reality with Sarah.
```

## Relationships

- `LFW_Character` — Relationship Items are the symmetric counterpart to each Character's asymmetric `## Relationships` body section. The two coexist; asymmetry drift between them surfaces during CHARACTER-CONSISTENCY.
- `LFW_Scene` — Drafted relational interactions populate the per-pair `Evolution arc` over time.
- `LFW_Manuscript_Manifest` — Optional backbone; not required by any genre but useful when the cast exceeds about five named characters.

## Notes

- **Symmetric view.** The all-pairs matrix is the symmetric view of the cast; the per-Character `## Relationships` is the asymmetric (per-character one-sided) view. Both are useful; this Item exists to surface asymmetry drift.
- **Asymmetry is sometimes intentional.** Unreliable POVs produce asymmetric relationship characterizations on purpose. Per-pair `Asymmetry` field documents whether asymmetry is intentional (and reveals the unreliable POV) or drift (and needs reconciliation).
- **Cast threshold.** For cartridges with three or fewer named characters, this file is overkill — the per-Character sections are sufficient. The break-even is usually five named characters.
- **Triangle dynamics are load-bearing or not at all.** Don't enumerate every triangle; only the ones whose dynamic matters structurally (love triangles, oedipal triangles, three-friend dynamics where the third presence shapes the pair).
