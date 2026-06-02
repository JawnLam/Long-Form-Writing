---
type: writing-engine
role: meta-ontology
scope: subject-agnostic
updated: 2026-06-02
---

# Schema of Schemas — LFW Meta-Ontology

> **The three-layer ontology that makes LFW work across genres. Per OVE's pattern.**

## Three layers

### Layer 1 — LFW universals

These hold across every cartridge regardless of genre:

- Cartridge backbone files: `_manuscript-manifest.md`, `_state.md`, `_outline.md`
- Atom-storage subfolders: `Atoms/Beats/`, `Atoms/Chapters/`, `Atoms/Notes/`, etc.
- `Sessions/` folder with append-only logs
- `Revision-Passes/` folder with append-only logs
- Session lifecycle (READ → DIAGNOSE → PROPOSE → WAIT → EXECUTE → CAPTURE → WRITE → UPDATE)
- The ten universal activities
- The four standard revision passes
- Source-of-truth: `_state.md` for current state; session logs for history

### Layer 2 — Per-genre branch

Documented in `02-GENRE-AND-SCHEMA.md`. Each genre emphasizes different atoms:

- **Fiction** — Scenes + Characters + Beats
- **Non-fiction** — Sections + Threads + Sources
- **Screenplay** — Scenes + Characters + Acts + Beats
- **Play** — Scenes + Characters + Acts
- **Dissertation** — Sections + Threads + Sources (heavy)

The branch is declared in `_manuscript-manifest.md` (`lfw_genre`).

### Layer 3 — Per-cartridge instance

Each cartridge's specific atoms, outline, state, voice samples. The cartridge is the unit of work; the atoms are its content.

## Cross-layer rules

1. **Layer 1 never names a specific manuscript.** The engine is subject-agnostic.
2. **Layer 2 never redefines Layer 1 universals.** Genre branches *emphasize* atoms; they don't change what an atom is.
3. **Layer 3 must conform to Layer 2's emphasis.** A fiction cartridge using Section atoms instead of Scene atoms is non-conforming — refactor before continuing.

## Auditing a cartridge

A well-formed cartridge satisfies:

- [ ] Has all required Layer 1 files (`_manuscript-manifest.md`, `_state.md`, `_outline.md`)
- [ ] Genre is declared and matches Layer 2 expectations
- [ ] Every atom note has valid frontmatter per its template
- [ ] No dangling wiki-links to non-existent atoms
- [ ] `_state.md` references atoms that actually exist
- [ ] If `_voice-samples.md` is present, voice mode in `_manuscript-manifest.md` matches
- [ ] Sessions folder has logs for all sessions claimed in `_state.md`

## Versioning

The Layer 1 universals are frozen at v1.0. Schema changes require version bumps per `CONTRIBUTING.md`.

## Connection to OVE's meta-ontology

LFW's three-layer ontology is itself an instance of the pattern documented in [Operating-Volume-Engineering](https://github.com/JawnLam/Operating-Volume-Engineering)'s `_design-engine/_meta/SCHEMA-OF-SCHEMAS.md`. LFW = Layer 1 (engine universals) + Layer 2 (genre branches) + Layer 3 (cartridge instances). OVE = Layer 1 (OVE universals) + Layer 2 (per-OV schemas) + Layer 3 (per-cartridge instances).

LFW is one valid OV-shape; OVE's protocol could be used to redesign LFW. (Self-similarity test, P9 in OVE's design principles, holds.)
