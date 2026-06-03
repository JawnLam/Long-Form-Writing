---
lfw_version: "1.3.1"
schema_version: "1.3"
schema_status: "STABLE"
release_date: 2026-06-03
release_phase: "Patch release — writer-side fiction craft (dialogue, POV-voice, scene-and-sequel, show-don't-tell, Character-Bible, Theme, sub-genre branching, beat-sheet overlays)"
---

# Long-Form-Writing — Version

This is Long-Form-Writing **v1.3.1** — first of a two-pass patch series extending v1.2's fiction foundation with the line-level craft and structural-overlay artifacts a fiction writer most often needs. v1.3.2 (next) will add the structural-artifact layer (`_worldbuilding.md`, multi-layer timeline, storyboard, style sheet, names list, research-as-inspiration, relationship map, stakes ladder). All v1.3.1 additions are backward-compatible with v1.0 / v1.1 / v1.2 cartridges.

## Version identifiers

| Identifier              | Value         | Notes                                                                  |
|-------------------------|---------------|------------------------------------------------------------------------|
| **Artifact category**   | Operating volume | See [Operating-Volume-Engineering](https://github.com/JawnLam/Operating-Volume-Engineering) for the category definition |
| **Software**            | v1.3.1        | Patch release — writer-side fiction-craft pass                         |
| **Schema**              | v1.3          | STABLE — adds Character-Bible + Theme atoms, scene-type field, POV-voice-register field, dialogue-tells sub-section, Beat subtext field (all additive; backward-compatible) |
| **Writing engine**      | v1.3.1        | 14 chapters now (00–08 unchanged; 09–10 from v1.1; 11–12 from v1.2; 13–14 added v1.3.1) |
| **Templates**           | v1.3.1        | Shipped in `_writing-engine/_templates/` (6 new templates; Scene + Character + Beat + manifest + spine templates updated) |
| **Worked examples**     | v1.3.1        | Two cartridges: Persistence-Question (non-fiction); Late-Frost (fiction; updated with v1.3.1 features in session 004) |
| **Release date**        | 2026-06-03    |                                                                        |

## Schema policy

The atom prototypes are stable at v1.3:

- v1.0 stable: `LFW_Manuscript_Manifest`, `LFW_State`, `LFW_Beat`, `LFW_Scene`, `LFW_Section`, `LFW_Chapter`, `LFW_Character`, `LFW_Thread`, `LFW_Source`, `LFW_Note`, `LFW_Session`, `LFW_Revision_Pass`, `LFW_Voice_Sample`
- v1.1 added: `LFW_Reader`, `LFW_Argument`, `LFW_Craft_Log`, `LFW_Craft_Profile`
- v1.2 added: `LFW_Motif`, `LFW_Spine`, `LFW_Continuity`, `LFW_Promises`
- v1.3.1 added: `LFW_Character_Bible`, `LFW_Theme`, four beat-sheet overlay prototypes (`LFW_Overlay_Story_Circle`, `LFW_Overlay_Save_The_Cat`, `LFW_Overlay_Heros_Journey`, `LFW_Overlay_Freytag`)

Any change that adds a required field, renames a field, removes a field, or changes a field's type requires a major version bump (v2.0). Additive changes (new optional fields, new atom subtypes, new templates, new opt-in modules) are minor or patch version bumps. v1.3.1's additions are all optional and backward-compatible.

## What is in this version

- **Writing engine** in `_writing-engine/`:
  - Fourteen core operating files (`00–08` production; `09–10` development v1.1; `11–12` fiction-craft foundation v1.2; `13–14` fiction-craft writer-side v1.3.1) plus `BOOTSTRAP-NEW-MANUSCRIPT.md`
  - Twenty-two atom-type, cartridge-backbone, and overlay templates in `_templates/` (16 from v1.2 + 6 v1.3.1 additions: Character-Bible, Theme, four overlay templates; Scene + Character + Beat + manifest + spine templates updated)
  - Schema-of-schemas + failure-modes catalog in `_meta/` (extended for v1.3.1 with character-bible, theme, scene-type, sub-genre; F31–F44 fiction failure modes)
  - Validator extended with check 10 (scene-type-legal) and check 11 (pov-voice-register advisory); check 9 now exempts sequel-typed Scenes
- **Root docs**: `README`, `AI-BOOTSTRAP`, `INSTALL`, `OPERATOR-GUIDE`, `CONTRIBUTING`, `LICENSE` (CC-BY 4.0), `VERSION`, `CHANGELOG`
- **Optional user profile template**: `_USER.md.template`
- **Two worked-example cartridges**:
  - `Example-Project-The-Persistence-Question/` — non-fiction; demonstrates v1.1 development layer
  - `Example-Project-The-Late-Frost/` — fiction; literary novel at session 4; demonstrates all v1.2 and v1.3.1 features (POV-voice-register, dialogue tells, Character-Bible, Theme atom, Story Circle overlay, sub-genre tuning)
- **`.gitignore`** that keeps writer's working artifacts operator-private (extended for v1.3.1 to include Character-Bibles, Themes, overlays, per-POV voice samples)

## Genre coverage in v1.3.1

The schema covers five long-form genres explicitly:

- **Fiction** — novels, novellas, short-story collections; Scene + Character + Motif + Theme emphasis; spine + continuity + promises backbones; full activity set including v1.3.1's DIALOGUE-AUDIT, POV-VOICE-DRIFT, THEME-CHECK; sub-genre tuning across literary / thriller / mystery / romance / SFF / speculative / historical / horror / YA **(writer-side craft materially expanded in v1.3.1)**
- **Non-fiction** — Section + Thread + Source + Reader emphasis; argument backbone; v1.1 development activities
- **Screenplay** — Scene + Character + Beat + Act emphasis; Save the Cat overlay often appropriate
- **Play** — Scene + Character + dialogue-heavy emphasis
- **Dissertation / academic** — Section + Source + Thread emphasis

## Compatibility

- **AI:** any capable assistant (Claude Sonnet/Opus class, GPT-4 class and above, Gemini 2.x and above)
- **OS:** Mac, Windows, Linux
- **Editor:** Obsidian recommended for fiction
- **Python / network / runtime dependencies:** none

## License

See `LICENSE.md`. Released under CC-BY 4.0. Original work by Jawn Lam.
