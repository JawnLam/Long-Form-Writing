---
lfw_version: "1.7.1"
schema_version: "1.6"
schema_status: "STABLE"
release_date: 2026-06-06
release_phase: "Patch release — fixes stale .gitignore Atoms→Items patterns missed in v1.7.0; adopts OVE Conventions 7 (install-and-update pattern) and 8 (engine vs operator boundary)"
---

# Long-Form-Writing — Version

This is Long-Form-Writing **v1.4.0** — minor release adding two soft-skill activities that fill the gaps the production / development / structural-artifact layers of v1.0–v1.3.2 did not touch. **WEATHER-CHECK** names and triages the writer's affective state (dread, doubt, grief, despair, boredom, burnout, overwhelm) — acknowledgment + diagnostic, NOT therapy or motivation. **MIDDLE-AUDIT** is a specific seven-question structural audit run at the midpoint of the manuscript, the place where most fiction projects die.

**v1.4.0 deliberately adds zero new Items, zero new backbones, zero new templates, and zero new validator checks.** It is the first release in the v1.x series whose architectural posture is honest scope-limitation: two carefully-scoped activities filling two specific gaps, not another schema-growth pass. The schema-creep concern noted in the v1.3.2 self-critique is respected.

## Version identifiers

| Identifier              | Value         | Notes                                                                  |
|-------------------------|---------------|------------------------------------------------------------------------|
| **Artifact category**   | Operating volume | See [Operating-Volume-Engineering](https://github.com/JawnLam/Operating-Volume-Engineering) for the category definition |
| **Software**            | v1.4.0        | Minor release — soft-skill activity pass; zero schema growth           |
| **Schema**              | v1.4          | STABLE — no Item or backbone additions; activity set expands 23 → 25  |
| **Writing engine**      | v1.4.0        | 16 chapters now (00–08 unchanged; 09–10 from v1.1; 11–12 from v1.2; 13–14 from v1.3.1; 15 from v1.3.2; 16 added v1.4.0) |
| **Templates**           | v1.4.0        | Unchanged from v1.3.2 (28 templates)                                   |
| **Worked examples**     | v1.4.0        | Two cartridges: Persistence-Question (non-fiction); Late-Frost (fiction; gained session 006 demonstrating WEATHER-CHECK in action) |
| **Release date**        | 2026-06-03    |                                                                        |

## Schema policy

The Item prototypes are stable at v1.3 (no changes in v1.4.0):

- v1.0 stable: `LFW_Manuscript_Manifest`, `LFW_State`, `LFW_Beat`, `LFW_Scene`, `LFW_Section`, `LFW_Chapter`, `LFW_Character`, `LFW_Thread`, `LFW_Source`, `LFW_Note`, `LFW_Session`, `LFW_Revision_Pass`, `LFW_Voice_Sample`
- v1.1 added: `LFW_Reader`, `LFW_Argument`, `LFW_Craft_Log`, `LFW_Craft_Profile`
- v1.2 added: `LFW_Motif`, `LFW_Spine`, `LFW_Continuity`, `LFW_Promises`
- v1.3.1 added: `LFW_Character_Bible`, `LFW_Theme`, four beat-sheet overlay prototypes
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
