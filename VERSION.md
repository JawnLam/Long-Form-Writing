---
lfw_version: "1.3.2"
schema_version: "1.3"
schema_status: "STABLE"
release_date: 2026-06-03
release_phase: "Patch release — structural-artifact layer (worldbuilding, multi-layer timelines, storyboard, style sheet, inspiration, relationship map, stakes ladder)"
---

# Long-Form-Writing — Version

This is Long-Form-Writing **v1.3.2** — second of the two-pass patch series. Where v1.3.1 added the writer-side craft layer (dialogue, POV-voice, scene-and-sequel, show-don't-tell, Character-Bible, Theme, sub-genre branching, beat-sheet overlays), v1.3.2 adds the structural-artifact layer that organizes a fiction project beyond what the v1.0–v1.3.1 schema covered. All v1.3.2 additions are backward-compatible with v1.0 / v1.1 / v1.2 / v1.3.1 cartridges. No new activities are added — the new artifacts feed existing activities.

## Version identifiers

| Identifier              | Value         | Notes                                                                  |
|-------------------------|---------------|------------------------------------------------------------------------|
| **Artifact category**   | Operating volume | See [Operating-Volume-Engineering](https://github.com/JawnLam/Operating-Volume-Engineering) for the category definition |
| **Software**            | v1.3.2        | Patch release — structural-artifact pass                               |
| **Schema**              | v1.3          | STABLE — adds Timeline + Inspiration atoms and four backbone files (all additive; backward-compatible) |
| **Writing engine**      | v1.3.2        | 15 chapters now (00–08 unchanged; 09–10 from v1.1; 11–12 from v1.2; 13–14 from v1.3.1; 15 added v1.3.2) |
| **Templates**           | v1.3.2        | Shipped in `_writing-engine/_templates/` (6 new templates; spine template updated for stakes ladder) |
| **Worked examples**     | v1.3.2        | Two cartridges: Persistence-Question (non-fiction); Late-Frost (fiction; updated with v1.3.2 features in session 005) |
| **Release date**        | 2026-06-03    |                                                                        |

## Schema policy

The atom prototypes are stable at v1.3:

- v1.0 stable: `LFW_Manuscript_Manifest`, `LFW_State`, `LFW_Beat`, `LFW_Scene`, `LFW_Section`, `LFW_Chapter`, `LFW_Character`, `LFW_Thread`, `LFW_Source`, `LFW_Note`, `LFW_Session`, `LFW_Revision_Pass`, `LFW_Voice_Sample`
- v1.1 added: `LFW_Reader`, `LFW_Argument`, `LFW_Craft_Log`, `LFW_Craft_Profile`
- v1.2 added: `LFW_Motif`, `LFW_Spine`, `LFW_Continuity`, `LFW_Promises`
- v1.3.1 added: `LFW_Character_Bible`, `LFW_Theme`, four beat-sheet overlay prototypes
- v1.3.2 added: `LFW_Timeline`, `LFW_Inspiration`, `LFW_Worldbuilding`, `LFW_Storyboard`, `LFW_Style_Sheet`, `LFW_Relationships`

Any change that adds a required field, renames a field, removes a field, or changes a field's type requires a major version bump (v2.0). v1.3.2's additions are all optional and backward-compatible.

## What is in this version

- **Writing engine** in `_writing-engine/`:
  - Fifteen core operating files (`00–08` production; `09–10` development v1.1; `11–12` fiction-craft foundation v1.2; `13–14` fiction-craft writer-side v1.3.1; `15` fiction-structural-artifacts v1.3.2) plus `BOOTSTRAP-NEW-MANUSCRIPT.md`
  - Twenty-eight atom-type, cartridge-backbone, and overlay templates in `_templates/` (22 from v1.3.1 + 6 v1.3.2 additions: Timeline, Inspiration, worldbuilding, storyboard, style-sheet, relationships; spine template updated for stakes ladder)
  - Schema-of-schemas + failure-modes catalog in `_meta/` (extended for v1.3.2 with timeline, inspiration, four new backbones; F45–F51 structural-artifact failure modes)
  - Validator extended with check 12 (timeline-layer); STATUS_ENUM gains timeline and inspiration; BACKBONE_FILES gains four new backbones
- **Root docs**: `README`, `AI-BOOTSTRAP`, `INSTALL`, `OPERATOR-GUIDE`, `CONTRIBUTING`, `LICENSE` (CC-BY 4.0), `VERSION`, `CHANGELOG`
- **Optional user profile template**: `_USER.md.template`
- **Two worked-example cartridges**:
  - `Example-Project-The-Persistence-Question/` — non-fiction; v1.1 development layer
  - `Example-Project-The-Late-Frost/` — fiction; session 5; demonstrates v1.0–v1.3.2 features including three Timeline atoms (story-time + world-history + character-specific), all four v1.3.2 backbones, one Inspiration atom, stakes ladder in spine
- **`.gitignore`** extended for v1.3.2 operator-private artifacts (Timelines, Inspirations, worldbuilding, storyboard, style-sheet, relationships)

## Genre coverage in v1.3.2

The schema covers five long-form genres explicitly:

- **Fiction** — full atom + backbone + activity set across v1.0–v1.3.2 (the structural-artifact additions are fiction-primary; contemporary realism uses lighter slice; SFF / historical / speculative use the full set)
- **Non-fiction** — Section + Thread + Source + Reader emphasis; argument backbone; v1.1 development activities
- **Screenplay** — Scene + Character + Beat + Act emphasis; Save the Cat overlay often appropriate
- **Play** — Scene + Character + dialogue-heavy emphasis
- **Dissertation / academic** — Section + Source + Thread emphasis

## Compatibility

- **AI:** any capable assistant (Claude Sonnet/Opus class, GPT-4 class and above, Gemini 2.x and above)
- **OS:** Mac, Windows, Linux
- **Editor:** Obsidian recommended for fiction (graph view across atoms is useful)
- **Python / network / runtime dependencies:** none

## License

See `LICENSE.md`. Released under CC-BY 4.0. Original work by Jawn Lam.
