---
type: writing-engine
role: meta-ontology
scope: subject-agnostic
updated: 2026-06-02
---

# Schema of Schemas — LFW Meta-Ontology

> **The three-layer ontology that makes LFW work across genres. Per OVE's pattern.**

## Three layers

### Layer 0 — OV-root (persists across cartridges)

Files at the LFW root that persist across every cartridge:

- `_USER.md` — global writer profile (identity, communication preferences)
- `_craft-profile.md` — the cross-cartridge writer-skill memory (chapter 09)

Layer 0 is what makes LFW more than a per-project tool. The craft-profile in particular is the controller's memory of the writer; without it, every cartridge is amnesiac about the writer's growth.

### Layer 1 — LFW universals (per cartridge)

These hold inside every cartridge regardless of genre:

- Cartridge backbone files: `_manuscript-manifest.md`, `_state.md`, `_outline.md`
- Conditional backbone files: `_voice-samples.md`, `_argument.md`, `_craft-log.md`
- Atom-storage subfolders: `Atoms/Beats/`, `Atoms/Chapters/`, `Atoms/Readers/`, `Atoms/Notes/`, etc.
- `Sessions/` folder with append-only logs
- `Revision-Passes/` folder with append-only logs
- Session lifecycle (READ → DIAGNOSE → PROPOSE → WAIT → EXECUTE → CAPTURE → WRITE → UPDATE)
- The sixteen universal activities (10 production + 6 development)
- The four standard revision passes
- Source-of-truth: `_state.md` for current state; session logs for history

### Layer 2 — Per-genre branch

Documented in `02-GENRE-AND-SCHEMA.md`. Each genre emphasizes different atoms:

- **Fiction** — Scenes + Characters + Beats
- **Non-fiction** — Sections + Threads + Sources + **Readers** + `_argument.md`
- **Screenplay** — Scenes + Characters + Acts + Beats
- **Play** — Scenes + Characters + Acts + Settings
- **Dissertation** — Sections + Threads + Sources (heavy) + **Readers** + `_argument.md`

The branch is declared in `_manuscript-manifest.md` (`lfw_genre`). Non-fiction and dissertation add `_argument.md` as a required backbone file and Reader atoms as a primary atom type.

### Layer 3 — Per-cartridge instance

Each cartridge's specific atoms, outline, state, voice samples. The cartridge is the unit of work; the atoms are its content.

## Cross-layer rules

1. **Layer 1 never names a specific manuscript.** The engine is subject-agnostic.
2. **Layer 2 never redefines Layer 1 universals.** Genre branches *emphasize* atoms; they don't change what an atom is.
3. **Layer 3 must conform to Layer 2's emphasis.** A fiction cartridge using Section atoms instead of Scene atoms is non-conforming — refactor before continuing.

## Auditing a cartridge

A well-formed cartridge satisfies:

- [ ] Has all required Layer 1 files (`_manuscript-manifest.md`, `_state.md`, `_outline.md`)
- [ ] Has all required-by-genre Layer 2 files (`_argument.md` for non-fiction/dissertation; `_voice-samples.md` if voice mode is `voice-samples`)
- [ ] Genre is declared and matches Layer 2 expectations
- [ ] Every atom note has valid frontmatter per its template
- [ ] Every Reader atom has all required body sections (chapter 04)
- [ ] No dangling wiki-links to non-existent atoms
- [ ] `_state.md` references atoms that actually exist
- [ ] If `_voice-samples.md` is present, voice mode in `_manuscript-manifest.md` matches
- [ ] If `lfw_scaffolding_mode` is `gradual-fade` or `socratic`, session-count thresholds are documented (chapter 09)
- [ ] Sessions folder has logs for all sessions claimed in `_state.md`

The validator at `_writing-engine/_scripts/validate.py` enforces a subset of these checks automatically.

## Versioning

The Layer 1 universals are stable. Schema additions (new optional atom types, new optional backbone files, new activities) are minor releases (v1.x). Breaking changes (removed fields, renamed atom types, changed required-field shape) require a major release (v2.0). See `CONTRIBUTING.md`.

v1.1 additions (this version):
- Layer 0 introduced (OV-root files: `_craft-profile.md`)
- New atom type: **Reader** (Layer 1 universal; primary for non-fiction)
- New backbone files: `_argument.md` (required for non-fiction/dissertation), `_craft-log.md` (optional, recommended)
- Activity set expanded from 10 → 16 (six new development activities defined in chapter 10)
- Scaffolding-mode setting (`lfw_scaffolding_mode`) added to `_manuscript-manifest.md` frontmatter
- Opt-in craft modules introduced as a coaching framework (chapter 09)

## Connection to OVE's meta-ontology

LFW's three-layer ontology is itself an instance of the pattern documented in [Operating-Volume-Engineering](https://github.com/JawnLam/Operating-Volume-Engineering)'s `_design-engine/_meta/SCHEMA-OF-SCHEMAS.md`. LFW = Layer 1 (engine universals) + Layer 2 (genre branches) + Layer 3 (cartridge instances). OVE = Layer 1 (OVE universals) + Layer 2 (per-OV schemas) + Layer 3 (per-cartridge instances).

LFW is one valid OV-shape; OVE's protocol could be used to redesign LFW. (Self-similarity test, P9 in OVE's design principles, holds.)
