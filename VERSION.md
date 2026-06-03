---
lfw_version: "1.2.0"
schema_version: "1.2"
schema_status: "STABLE"
release_date: 2026-06-02
release_phase: "Minor release — fiction conceptual pass (production-and-growth parity for fiction, plus fiction-specific schema elements the v1.0/v1.1 schema was under-serving)"
---

# Long-Form-Writing — Version

This is Long-Form-Writing **v1.2.0** — minor release closing the fiction-side gap left by v1.1. v1.1 brought the development layer (writer-skill model, Reader atoms, argument backbone, six new activities, scaffolding fade, opt-in craft modules) but only to non-fiction. v1.2 brings fiction parity *and* adds the fiction-specific structural elements the v1.0/v1.1 schema was under-serving: causal-spine backbone, motif atoms, setup-payoff ledger, continuity ledger, scene value-shift discipline, four new fiction-weighted development activities, fiction error vocabulary in the craft-profile, and a POV-and-psychic-distance craft module. All additions are backward-compatible with v1.0 and v1.1 cartridges.

## Version identifiers

| Identifier              | Value         | Notes                                                                  |
|-------------------------|---------------|------------------------------------------------------------------------|
| **Artifact category**   | Operating volume | See [Operating-Volume-Engineering](https://github.com/JawnLam/Operating-Volume-Engineering) for the category definition |
| **Software**            | v1.2.0        | Minor release — fiction conceptual pass                                |
| **Schema**              | v1.2          | STABLE — atom prototypes locked; v1.2 adds Motif atom + three fiction backbone files (additive, backward-compatible) |
| **Writing engine**      | v1.2          | 12 chapters now (00–08 unchanged; 09 + 10 from v1.1; 11 + 12 added v1.2) |
| **Templates**           | v1.2          | Shipped in `_writing-engine/_templates/` (4 new templates; Scene template updated) |
| **Worked examples**     | v1.2          | Two cartridges now: `Example-Project-The-Persistence-Question/` (non-fiction) and `Example-Project-The-Late-Frost/` (fiction) |
| **Release date**        | 2026-06-02    |                                                                        |

## Schema policy

The atom prototypes (`LFW_Manuscript_Manifest`, `LFW_State`, `LFW_Beat`, `LFW_Scene`, `LFW_Section`, `LFW_Chapter`, `LFW_Character`, `LFW_Reader`, `LFW_Motif`, `LFW_Thread`, `LFW_Source`, `LFW_Note`, `LFW_Session`, `LFW_Revision_Pass`, `LFW_Voice_Sample`) are stable at v1.2. Any change that:

- Adds a required field
- Renames a field
- Removes a field
- Changes a field's type

requires a major version bump (v2.0). Additive changes (new optional fields, new atom subtypes for additional genres, new templates) are minor version bumps (v1.x). v1.2's two added optional Scene fields (`lfw_value_shift_from`, `lfw_value_shift_to`) are additive — Scenes without them remain legal at `planned | drafting` status; the validator enforces them only when the Scene is `drafted` or later.

## What is in this version

- **Writing engine** in `_writing-engine/`:
  - Twelve core operating files (`00–08` production layer; `09–10` development layer from v1.1; `11–12` fiction-craft additions from v1.2) plus `BOOTSTRAP-NEW-MANUSCRIPT.md`
  - Sixteen atom-type and cartridge-backbone templates in `_templates/` (12 from v1.1 + 4 v1.2 additions: Motif, spine, continuity, promises; Scene template updated for value-shift)
  - Schema-of-schemas + failure-modes catalog in `_meta/` (extended for v1.2 with motif, spine, continuity, promises, and F22–F30 fiction failure modes)
  - Validator extended with check 9 (scene-value-shift) and v1.2 schema additions
- **Root docs** at the root: `README`, `AI-BOOTSTRAP`, `INSTALL`, `OPERATOR-GUIDE`, `CONTRIBUTING`, `LICENSE` (CC-BY 4.0), `VERSION`, `CHANGELOG`
- **Optional user profile template**: `_USER.md.template`
- **Two worked-example cartridges**:
  - `Example-Project-The-Persistence-Question/` — non-fiction; outlining-to-mid-draft stage; demonstrates the v1.1 development layer
  - `Example-Project-The-Late-Frost/` — fiction; literary novel at session 3 (early-drafting stage); demonstrates the v1.2 fiction development layer (spine, motifs, promises, continuity, value-shift, steelmanned antagonist, fiction READER-SIMULATION)
- **`.gitignore`** that keeps a writer's manuscript-in-progress out of source control by default (including the v1.2 fiction backbones) while preserving the shipped examples

## Genre coverage in v1.2

The schema covers five long-form genres explicitly:

- **Fiction** — novels, novellas, short-story collections; Scene + Character + Motif atom emphasis; spine + continuity + promises backbones; SCENE-AUDIT, CHARACTER-CONSISTENCY, CONTINUITY-CHECK, SETUP-PAYOFF-AUDIT activities **(materially expanded in v1.2)**
- **Non-fiction** — book-length argument or narrative; Section + Thread + Source + Reader emphasis; argument backbone; READER-SIMULATION, ARGUMENT-AUDIT, CLAIM-EVIDENCE-CHECK, STEELMAN, SYNTHESIS-CHECK, CRAFT-REVIEW activities (v1.1)
- **Screenplay** — feature films, short scripts; Scene + Character + Beat emphasis with act structure
- **Play** — stage plays; Scene + Character + dialogue-heavy atom emphasis
- **Dissertation / academic** — citation-heavy long-form scholarship; Section + Source + Thread emphasis

Genre is declared per cartridge in `_manuscript-manifest.md`. The schema branches accordingly.

## Compatibility

- **AI:** any capable assistant (Claude Sonnet/Opus class, GPT-4 class and above, Gemini 2.x and above)
- **OS:** Mac, Windows, Linux
- **Editor:** Obsidian recommended for fiction (graph view across atoms is useful); also fine in VS Code, Cursor, Windsurf, Zed, JetBrains, or plain text editors with AI integration
- **Python / network / runtime dependencies:** none

## License

See `LICENSE.md`. Released under CC-BY 4.0. Original work by Jawn Lam.
