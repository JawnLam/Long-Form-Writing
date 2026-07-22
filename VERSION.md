---
lfw_version: "1.10.0"
schema_version: "1.8"
schema_status: "STABLE"
release_date: 2026-07-22
release_phase: "Minor release — adds the rolling-workshop short-form pattern: two Layer-1 Types (LFW_Piece front-doc of a piece-folder + LFW_Published_Ledger append-only graduation history) with new templates, validator check 18 (piece-status), and coordinated registration in the vault Master_Schema (v1.47.0). Publication metadata reuses the universal core (Publication_Date / resource / URL). See CHANGELOG.md."
---

# Long-Form-Writing — Version

This is Long-Form-Writing **v1.10.0** — a minor release adding the **rolling-workshop short-form pattern**. A rolling-workshop cartridge produces many self-contained short pieces (essays / commentary) over time rather than one long manuscript. Two Layer-1 Types support it: **`LFW_Piece`** — the front document (`_piece.md`) of a piece-folder whose `lfw_piece_status` (germinating → drafting → revising → ready → published → archived) represents the state of the entire folder, alongside a companion Obsidian Canvas `_wall.canvas` — and **`LFW_Published_Ledger`** — the per-cartridge append-only history of pieces that graduated out to MultiVac. `published` is the signal MultiVac's intake sweep watches for. New templates `TEMPLATE-piece.md` and `TEMPLATE-published-ledger.md`; validator check 18 (piece-status). Publication metadata deliberately reuses the universal core (`Publication_Date` / `resource` / `URL`) rather than piece-specific properties. Registered in the vault `Master_Schema.yaml` at **v1.47.0**. No existing Item, backbone, or activity changed.

> **`CHANGELOG.md` is the authoritative release history.** The detailed prose below this section documents the **v1.4.0** release and has NOT been refreshed for the v1.5–v1.8.1 releases (a pre-existing gap); treat `CHANGELOG.md` as canonical for anything after v1.4.0.

## Version identifiers

| Identifier              | Value         | Notes                                                                  |
|-------------------------|---------------|------------------------------------------------------------------------|
| **Artifact category**   | Operating volume | See [Operating-Volume-Engineering](https://github.com/JawnLam/Operating-Volume-Engineering) for the category definition |
| **Software**            | v1.10.0       | Minor release — rolling-workshop pattern: `LFW_Piece` + `LFW_Published_Ledger` types, 2 templates, validator check 18 (piece-status) |
| **Schema**              | v1.8          | STABLE — adds Layer-1 `LFW_Piece` + `LFW_Published_Ledger`; publication metadata reuses universal core; registered in vault Master_Schema v1.47.0; no existing Item / backbone / activity change |
| **Writing engine**      | v1.4.0        | 16 chapters now (00–08 unchanged; 09–10 from v1.1; 11–12 from v1.2; 13–14 from v1.3.1; 15 from v1.3.2; 16 added v1.4.0) |
| **Templates**           | v1.4.0        | Unchanged from v1.3.2 (28 templates)                                   |
| **Worked examples**     | v1.4.0        | Two cartridges: Persistence-Question (non-fiction); Late-Frost (fiction; gained session 006 demonstrating WEATHER-CHECK in action) |
| **Release date**        | 2026-06-03    |                                                                        |

## Schema policy

The Item types are stable at v1.3 (no changes in v1.4.0):

- v1.0 stable: `LFW_Manuscript_Manifest`, `LFW_State`, `LFW_Beat`, `LFW_Scene`, `LFW_Section`, `LFW_Chapter`, `LFW_Character`, `LFW_Thread`, `LFW_Source`, `LFW_Note`, `LFW_Session`, `LFW_Revision_Pass`, `LFW_Voice_Sample`
- v1.1 added: `LFW_Reader`, `LFW_Argument`, `LFW_Craft_Log`, `LFW_Craft_Profile`
- v1.2 added: `LFW_Motif`, `LFW_Spine`, `LFW_Continuity`, `LFW_Promises`
- v1.3.1 added: `LFW_Character_Bible`, `LFW_Theme`, four beat-sheet overlay types
- v1.3.2 added: `LFW_Timeline`, `LFW_Inspiration`, `LFW_Worldbuilding`, `LFW_Storyboard`, `LFW_Style_Sheet`, `LFW_Relationships`
- v1.4.0 added: **nothing**

v1.4.0's contribution is at the activity layer only.

## What is in this version

- **Writing engine** in `_writing-engine/`:
  - Sixteen core operating files (`00–08` production; `09–10` development v1.1; `11–12` fiction-craft foundation v1.2; `13–14` fiction-craft writer-side v1.3.1; `15` fiction-structural-artifacts v1.3.2; `16` soft-skill activities v1.4.0) plus `BOOTSTRAP-NEW-MANUSCRIPT.md`
  - Twenty-eight Item-type, cartridge-backbone, and overlay templates (unchanged from v1.3.2)
  - Schema-of-schemas + failure-modes catalog in `_meta/` (extended for v1.4.0 with F52–F60 covering the soft-skill failure modes; schema_version field added to both meta files)
  - Validator unchanged
- **Root docs**: `README`, `AI-BOOTSTRAP`, `INSTALL`, `OPERATOR-GUIDE`, `CONTRIBUTING`, `LICENSE` (CC-BY 4.0), `VERSION`, `CHANGELOG`
- **Optional user profile template**: `_USER.md.template`
- **Two worked-example cartridges**:
  - `Example-Project-The-Persistence-Question/` — non-fiction; v1.1 development layer
  - `Example-Project-The-Late-Frost/` — fiction; gained session 006 demonstrating WEATHER-CHECK on commitment-dread for Beat 5; the worked example of an affective-state activity in practice
- **`.gitignore`** unchanged from v1.3.2

## The new activities at a glance

### WEATHER-CHECK (chapter 16 §2)

A 5–15 minute activity that names and triages the writer's affective state. Five-step protocol:

1. **Name the weather** — one neutral question; specificity matters
2. **Distinguish from adjacent technical states** — STUCK-DIAGNOSTIC, craft-as-procrastination, research-as-procrastination, or genuine affective weather
3. **Triage scope** — today-state / this-week / this-month / this-project
4. **Identify smallest possible next move** — may be: nothing
5. **Log and escalate** — log the weather; escalate to external support when distress signals are past what the OV is appropriate for

**Not a substitute for therapy or for mental health support.** Chapter 16 §1's escalation discipline is non-negotiable.

### MIDDLE-AUDIT (chapter 16 §3)

A seven-question structural audit run at the midpoint of the manuscript. Surfaces the failure modes specific to the middle 50%:

1. **Spine integrity** (F55)
2. **Want integrity** (F56)
3. **Stakes escalation** (cross-references F51)
4. **Subplot gravity** (F57)
5. **Confrontation avoidance** (F58)
6. **Reader-question opened recently?** (F59)
7. **Original why** (F60)

Triggered at 50% of word-count target by default; earlier if writer signals middle-of-book trouble.

## New failure modes (chapter 16 §4)

- **F52** — Motivation as substitute for diagnostic
- **F53** — Weather-check used as therapy substitute
- **F54** — Affective state misdiagnosed as stuck
- **F55** — Middle-spine-slip
- **F56** — Want forgotten
- **F57** — Subplot gravity
- **F58** — Confrontation avoidance, systemic
- **F59** — Reader-question starvation
- **F60** — Why drift

## Compatibility

- **AI:** any capable assistant (Claude Sonnet/Opus class, GPT-4 class and above, Gemini 2.x and above)
- **OS:** Mac, Windows, Linux
- **Editor:** Obsidian recommended for fiction
- **Python / network / runtime dependencies:** none

## License

See `LICENSE.md`. Released under CC-BY 4.0. Original work by Jawn Lam.
