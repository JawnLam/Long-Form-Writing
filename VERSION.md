---
lfw_version: "1.0.0"
schema_version: "1.0"
schema_status: "STABLE"
release_date: 2026-06-02
release_phase: "Initial public release"
---

# Long-Form-Writing — Version

This is Long-Form-Writing **v1.0.0** — initial public release.

## Version identifiers

| Identifier              | Value         | Notes                                                                  |
|-------------------------|---------------|------------------------------------------------------------------------|
| **Artifact category**   | Operating volume | See [Operating-Volume-Engineering](https://github.com/JawnLam/Operating-Volume-Engineering) for the category definition |
| **Software**            | v1.0.0        | Initial public release                                                 |
| **Schema**              | v1.0          | STABLE — atom prototypes and cartridge backbone locked                 |
| **Writing engine**      | v1.0          | Subject-agnostic writing operating manual                              |
| **Templates**           | v1.0          | Shipped in `_writing-engine/_templates/`                               |
| **Worked example**      | v1.0          | `Example-Project-The-Persistence-Question/`                            |
| **Release date**        | 2026-06-02    |                                                                        |

## Schema policy

The atom prototypes (`LFW_Manuscript_Manifest`, `LFW_State`, `LFW_Beat`, `LFW_Scene`, `LFW_Section`, `LFW_Chapter`, `LFW_Character`, `LFW_Thread`, `LFW_Source`, `LFW_Note`, `LFW_Session`, `LFW_Revision_Pass`, `LFW_Voice_Sample`) are stable at v1.0. Any change that:

- Adds a required field
- Renames a field
- Removes a field
- Changes a field's type

requires a major version bump (v2.0). Additive changes (new optional fields, new atom subtypes for additional genres, new templates) are minor version bumps (v1.x).

## What is in this version

- **Writing engine** in `_writing-engine/`:
  - Nine core operating files (`00–08`) plus `BOOTSTRAP-NEW-MANUSCRIPT.md`
  - Twelve atom-type and cartridge-backbone templates in `_templates/`
  - Schema-of-schemas + failure-modes catalog in `_meta/`
- **Root docs** at the root: `README`, `AI-BOOTSTRAP`, `INSTALL`, `OPERATOR-GUIDE`, `CONTRIBUTING`, `LICENSE` (CC-BY 4.0), `VERSION`, `CHANGELOG`
- **Optional user profile template**: `_USER.md.template`
- **One worked-example cartridge**: `Example-Project-The-Persistence-Question/` — a hypothetical non-fiction book project at outlining-to-mid-draft stage
- **`.gitignore`** that keeps a writer's manuscript-in-progress out of source control by default while preserving the shipped example

## Genre coverage in v1.0

The schema covers five long-form genres explicitly:

- **Fiction** — novels, novellas, short-story collections; Scene + Character atom emphasis
- **Non-fiction** — book-length argument or narrative; Section + Thread + Source emphasis
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
