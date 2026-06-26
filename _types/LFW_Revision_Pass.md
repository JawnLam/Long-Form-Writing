---
type: Fleeting
timestamp: "2026-06-06T00:00:00Z"
Item_ID: prototype-lfw-revision-pass
title: "LFW_Revision_Pass Prototype"
Date_Added: 2026-06-06
Date_Modified: 2026-06-06
Needs_Processing: false
---

# `LFW_Revision_Pass` — Prototype Definition

> **What this file is.** The canonical definition of the `LFW_Revision_Pass` Prototype for the Long-Form-Writing Operating Volume. Items in any cartridge that declare `type: LFW_Revision_Pass` conform to the contract described below.

## Purpose

A Revision Pass is a single bounded revision sweep across the manuscript (or a defined sub-scope) with a single declared kind: structural, voice, accuracy, prose-line, or custom. Each pass produces one Revision_Pass Item that records the focus, scope, method, Items touched, major changes, decisions made, and open threads carried forward. Per chapter 07 (Revision Discipline): the four standard revision kinds are deliberately bounded — a pass that drifts becomes two passes, not one undisciplined sweep. Created at the start of every revision pass; status moves through `in-progress` → `completed` (or `aborted`). Multiple passes per cartridge; multiple rounds per pass (round 1, round 2, etc.) for iterative work. Pass logs are append-only history; never rewritten.

## Required frontmatter

| Field | Type | Required? | Notes |
|-------|------|-----------|-------|
| `type` | string | yes | Must equal `LFW_Revision_Pass` |
| `Item_ID` | string | yes | Format: `<manuscript-slug>-pass-<NN>` |
| `Title` | string | yes | Format: `"<Manuscript Title> — Revision Pass <NN> — <Kind>"` |
| `Date_Added` | date | yes | When the pass was started |
| `Date_Modified` | date | yes | When last changed |
| `Needs_Processing` | boolean | yes | Default `false` |
| `lfw_manuscript` | string | yes | Manuscript slug |
| `lfw_pass_number` | integer | yes | Cumulative pass number across the cartridge's life |
| `lfw_pass_round` | integer | yes | Round number within this pass-kind for this cartridge |
| `lfw_pass_kind` | enum | yes | `structural` \| `voice` \| `accuracy` \| `prose-line` \| `custom` |
| `lfw_scope` | string | yes | `whole-book` \| `chapter-N` \| `sections-X-Y` \| free-text |
| `lfw_status` | enum | yes | `in-progress` \| `completed` \| `aborted` |
| `lfw_started` | date | yes | Pass start date |
| `lfw_completed` | date | optional | Null until pass completes |

## Body structure

```markdown
# Pass <NN> (Round <R>) — <Kind>

## Pass focus
*One paragraph. What this pass is about. What it will and won't attend to.*

## Scope
*Which Items, chapters, sections this pass covers.*

## Method
*How the pass is being conducted — read order, what's being checked Item-by-Item.*

## Items Touched
| Item | Status before | Status after | Changes summary |
|------|---------------|--------------|-----------------|

## Major Changes
### <Date> — Change N
**What changed:**
**Why:**
**Items affected:**

## Decisions Made

## Open Threads Carried Forward
- [ ]

## Pass-completion summary
*Written when the pass is marked `completed` or `aborted`.*
**Final scope completed:**
**Word-count delta:**
**Items moved from `drafted` → `revised`:**
**Items still requiring attention before final:**
```

## Naming

- **Filename pattern:** `Pass-<NN>-<kind>.md` (e.g., `Pass-01-structural.md`, `Pass-02-voice.md`)
- **Location:** `<Cartridge>/Revision-Passes/`
- **Wikilink target:** the filename

## Example Item

```markdown
---
type: LFW_Revision_Pass
timestamp: "2026-09-02T00:00:00Z"
Item_ID: the-late-frost-pass-02
title: "The Late Frost — Revision Pass 02 — Voice"
Date_Added: 2026-08-15
Date_Modified: 2026-09-02
Needs_Processing: false
lfw_manuscript: the-late-frost
lfw_pass_number: 2
lfw_pass_round: 1
lfw_pass_kind: voice
lfw_scope: whole-book
lfw_status: completed
lfw_started: 2026-08-15
lfw_completed: 2026-09-02
---

# Pass 02 (Round 1) — Voice

## Pass focus
Single-pass voice check across the whole book. Verify Maya's first-person register stays consistent — cadenced sentences, observational interiority, specific botanical/oenological nouns as anchors. Catch drift toward conventional "literary voice" (italicized internal monologue, abstract emotional adjectives, periodic-sentence inflation).

## Scope
Whole book. Chapters 1–6 (drafted to date).

## Method
Read every scene aloud. Mark drift in margin (the LFW validator's voice-drift check won't catch register-level drift; this is operator-only work). After each chapter, summarize the kind of drift seen — pattern-naming aids the next pass.

## Items Touched
| Item | Status before | Status after | Changes summary |
|------|---------------|--------------|-----------------|
| [[01-01-The-Approach]] | drafted | revised | Trimmed two italicized interior lines |
| [[01-04-Empty-House-Walkthrough]] | drafted | revised | Replaced three abstract-feeling adjectives with sensory anchors |
| [[02-02-The-Garage-Argument]] | drafted | revised | Reduced periodic-sentence inflation in opening paragraph |
| ... | ... | ... | ... |

## Major Changes

### 2026-08-20 — Closing-line discipline applied
**What changed:** Six chapter-end paragraphs lost their metaphorical lift. Replaced with flat literal beats per Craft Profile pattern.
**Why:** Per craft profile observation that closing-line lift recurs across cartridges and doesn't earn its weight. Aligns with current practice focus.
**Items affected:** 01-01, 01-03, 02-02, 03-01, 04-04, 05-02

## Decisions Made
- The italicized interior-monologue technique is OUT for this manuscript. The interiority will be carried by sentence cadence and sensory specificity, not by typography. Lock decision for any future drafts.

## Open Threads Carried Forward
- [ ] Sarah's dialogue register is not yet differentiated from Maya's narration. Pass 3 (or focused dialogue work) needed.
- [ ] Three scenes (04-01, 04-05, 05-01) still feel voice-drifty; couldn't pinpoint why. Re-read after Pass 3.

## Pass-completion summary
**Final scope completed:** All drafted chapters (1–6, 28 scenes total)
**Word-count delta:** −2,847 words
**Items moved from `drafted` → `revised`:** 24 Scene Items
**Items still requiring attention before final:** 04-01, 04-05, 05-01 (voice-drift uncertainty); Sarah's dialogue across all scenes
```

## Relationships

- `LFW_Scene` / `LFW_Chapter` / `LFW_Section` / `LFW_Beat` — Items touched during a pass move from `drafted` → `revised` (or `revised` → `revised` for additional passes). The Revision Pass log records which Items were touched.
- `LFW_State` — `_state.md` references the current active Revision Pass. Once a pass completes, the State's "current activity" updates.
- `LFW_Craft_Log` / `LFW_Craft_Profile` — Patterns observed during revision feed into craft-pattern tracking; the Craft Log may graduate cross-cartridge patterns to the Craft Profile.
- `LFW_Session` — Each pass typically spans many sessions; Session logs record per-session work; the Revision Pass Item is the cross-session summary.

## Notes

- **The four standard revision kinds.** Per chapter 07: `structural` (shape — what stays, what cuts, what reorders), `voice` (register and prose-line consistency), `accuracy` (fact-checking for non-fiction; continuity verification for fiction), `prose-line` (final pass at sentence-level). `custom` is the escape hatch for a focused operator-defined revision lane.
- **Single-kind discipline.** A pass declares one kind and holds it. A "voice + structural" pass drifts; two passes is the disciplined alternative. Per chapter 07 §1.
- **Multiple rounds within a kind.** `lfw_pass_round` allows iteration: Pass 02 round 1 (initial voice pass), Pass 02 round 2 (revisit after structural changes), etc. Each round is its own Item — append-only history.
- **Append-only.** Pass logs are not rewritten. If a pass is aborted, mark `aborted` and add a closing note explaining why; don't delete.
- **`Revision-Passes/` is a top-level cartridge subfolder**, parallel to `Items/` and `Sessions/`. Per cartridge structure documented in `_meta/SCHEMA-OF-SCHEMAS.md`.
