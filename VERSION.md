---
lfw_version: "1.9.0"
schema_version: "1.7"
schema_status: "STABLE"
release_date: 2026-07-21
release_phase: "Minor release — adds the two-folder capture-&-exploration workspace (_notes/ raw ingestion tank + _fpeds/ Full Prose Exploratory Drafts) to every cartridge; registers the fped workspace type; fixes validator check 7 (accept OKF-conformant lowercase title). See CHANGELOG.md."
---

# Long-Form-Writing — Version

This is Long-Form-Writing **v1.9.0** — a minor release adding a standard two-folder **capture & exploration workspace** to every cartridge: `_notes/` (the raw ingestion tank — a zero-friction, pre-canonical brain-dump inbox and first triage point for any idea) and `_fpeds/` (Full Prose Exploratory Drafts — prose written out to feel out tone / voice / shape before committing to the canonical Scene/Section atom system). It registers the workspace `fped` type and its four-value `status` lifecycle, seeds both workspaces in `BOOTSTRAP-NEW-MANUSCRIPT.md` and in both example cartridges (the fiction example gains a sample FPED), and fixes a pre-existing validator bug — check 7 now accepts OKF-conformant lowercase `title` (it had hard-required capital `Title`, which every atom failed). No Item, backbone, or activity changed; the workspaces are deliberately non-canonical.

> **`CHANGELOG.md` is the authoritative release history.** The detailed prose below this section documents the **v1.4.0** release and has NOT been refreshed for the v1.5–v1.8.1 releases (a pre-existing gap); treat `CHANGELOG.md` as canonical for anything after v1.4.0.

## Version identifiers

| Identifier              | Value         | Notes                                                                  |
|-------------------------|---------------|------------------------------------------------------------------------|
| **Artifact category**   | Operating volume | See [Operating-Volume-Engineering](https://github.com/JawnLam/Operating-Volume-Engineering) for the category definition |
| **Software**            | v1.9.0        | Minor release — `_notes/` + `_fpeds/` capture-&-exploration workspaces; `fped` type; validator check-7 fix |
| **Schema**              | v1.7          | STABLE — adds the non-canonical `_notes/` + `_fpeds/` workspace convention and the `fped` type; no Item / backbone / activity change |
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
