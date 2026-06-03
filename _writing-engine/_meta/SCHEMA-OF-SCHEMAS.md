---
type: writing-engine
role: meta-ontology
scope: subject-agnostic
updated: 2026-06-03
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
- Conditional backbone files: `_voice-samples.md`, `_argument.md`, `_craft-log.md`, `_spine.md`, `_continuity.md`, `_promises.md`
- Atom-storage subfolders: `Atoms/Beats/`, `Atoms/Chapters/`, `Atoms/Readers/`, `Atoms/Motifs/`, `Atoms/Themes/`, `Atoms/Character-Bibles/`, `Atoms/Notes/`, etc.
- `Sessions/` folder with append-only logs
- `Revision-Passes/` folder with append-only logs
- Session lifecycle (READ → DIAGNOSE → PROPOSE → WAIT → EXECUTE → CAPTURE → WRITE → UPDATE)
- The twenty-three universal activities (10 production + 6 development non-fiction-weighted + 4 development fiction-weighted v1.2 + 3 development fiction-craft v1.3.1)
- The four standard revision passes
- Optional opt-in overlay files: `_overlay-{name}.md` (chapter 14 §2)
- Source-of-truth: `_state.md` for current state; session logs for history

### Layer 2 — Per-genre branch

Documented in `02-GENRE-AND-SCHEMA.md`. Each genre emphasizes different atoms:

- **Fiction** — Scenes + Characters + Beats + **Motifs** + Readers (fiction-mode) + `_spine.md` + `_promises.md` + (`_continuity.md` if plot has secrets)
- **Non-fiction** — Sections + Threads + Sources + Readers + `_argument.md`
- **Screenplay** — Scenes + Characters + Acts + Beats + Motifs + `_spine.md` + `_continuity.md` + `_promises.md`
- **Play** — Scenes + Characters + Acts + Settings + Motifs + `_spine.md` + (`_continuity.md` if scope warrants) + `_promises.md`
- **Dissertation** — Sections + Threads + Sources (heavy) + Readers + `_argument.md`

The branch is declared in `_manuscript-manifest.md` (`lfw_genre`). 

- Non-fiction and dissertation add `_argument.md` as required backbone and Reader atoms as primary atom type.
- Fiction, screenplay, and play add `_spine.md` and `_promises.md` as required backbones, plus Motif atoms as the recurring-element atom (the fiction analog to non-fiction's Thread).
- Fiction with worldbuilding or plot secrets adds `_continuity.md` as required backbone.

### Layer 3 — Per-cartridge instance

Each cartridge's specific atoms, outline, state, voice samples. The cartridge is the unit of work; the atoms are its content.

## Cross-layer rules

1. **Layer 1 never names a specific manuscript.** The engine is subject-agnostic.
2. **Layer 2 never redefines Layer 1 universals.** Genre branches *emphasize* atoms; they don't change what an atom is.
3. **Layer 3 must conform to Layer 2's emphasis.** A fiction cartridge using Section atoms instead of Scene atoms is non-conforming — refactor before continuing.

## Auditing a cartridge

A well-formed cartridge satisfies:

- [ ] Has all required Layer 1 files (`_manuscript-manifest.md`, `_state.md`, `_outline.md`)
- [ ] Has all required-by-genre Layer 2 files (`_argument.md` for non-fiction/dissertation; `_spine.md` for fiction/screenplay/play; `_promises.md` for plot-driven; `_continuity.md` for genre-fiction with worldbuilding or plot secrets; `_voice-samples.md` if voice mode is `voice-samples`)
- [ ] Genre is declared and matches Layer 2 expectations
- [ ] Every atom note has valid frontmatter per its template
- [ ] Every Reader atom has all required body sections (chapter 04)
- [ ] Every Motif atom (fiction) has all required body sections (chapter 04)
- [ ] Every Scene atom (fiction) has `lfw_value_shift_from` and `lfw_value_shift_to` populated once drafted; if identical, the SCENE-AUDIT flag should be active
- [ ] No dangling wiki-links to non-existent atoms
- [ ] `_state.md` references atoms that actually exist
- [ ] If `_voice-samples.md` is present, voice mode in `_manuscript-manifest.md` matches
- [ ] If `lfw_scaffolding_mode` is `gradual-fade` or `socratic`, session-count thresholds are documented (chapter 09)
- [ ] Sessions folder has logs for all sessions claimed in `_state.md`

The validator at `_writing-engine/_scripts/validate.py` enforces a subset of these checks automatically.

## Versioning

The Layer 1 universals are stable. Schema additions (new optional atom types, new optional backbone files, new activities) are minor releases (v1.x). Breaking changes (removed fields, renamed atom types, changed required-field shape) require a major release (v2.0). See `CONTRIBUTING.md`.

v1.1 additions:
- Layer 0 introduced (OV-root files: `_craft-profile.md`)
- New atom type: **Reader** (Layer 1 universal; primary for non-fiction)
- New backbone files: `_argument.md` (required for non-fiction/dissertation), `_craft-log.md` (optional, recommended)
- Activity set expanded from 10 → 16 (six new development activities defined in chapter 10)
- Scaffolding-mode setting (`lfw_scaffolding_mode`) added to `_manuscript-manifest.md` frontmatter
- Opt-in craft modules introduced as a coaching framework (chapter 09)

v1.2 additions:
- New atom type: **Motif** (Layer 1 universal; primary for fiction). The fiction analog to non-fiction's Thread.
- New backbone files: `_spine.md` (required for fiction/screenplay/play — causal backbone), `_continuity.md` (required for genre-fiction-with-worldbuilding and plot-with-secrets — verification ledger), `_promises.md` (required for plot-driven fiction — setup/payoff ledger)
- Activity set expanded from 16 → 20 (four new fiction-weighted development activities defined in chapters 11 + 12: SCENE-AUDIT, CHARACTER-CONSISTENCY, CONTINUITY-CHECK, SETUP-PAYOFF-AUDIT)
- READER-SIMULATION extended (not duplicated) with fiction sub-protocol (chapter 12 §6)
- WORLDBUILDING extended (not duplicated) to propose CONTINUITY-CHECK at session end (chapter 12 §5)
- Scene atom template gains `lfw_value_shift_from` and `lfw_value_shift_to` frontmatter fields and a required `## Value-shift` body section
- New opt-in craft module: `pov-and-psychic-distance` (chapter 12 §7)
- The `prefigures` relation (which existed but was unused in v1.0–v1.1) becomes the canonical mechanism for declaring promises in `_promises.md`

v1.3.1 additions (this version):
- New atom types: **Character-Bible** (Layer 1 universal; opt-in extended companion to Character; chapter 14 §3), **Theme** (Layer 1 universal; primary for fiction; carried-not-declared; distinct from Motif and from `_argument.md`; chapter 14 §4)
- Scene atom gains `lfw_scene_type` field (scene | sequel | scene-sequel; chapter 14 §1 scene-and-sequel rhythm); sequel-typed Scenes are exempt from value-shift requirements (they carry decisions instead)
- Character atom gains `lfw_pov_voice_register` field (required for POV-bearing characters), dialogue-tells sub-section, optional subtext-patterns section; `lfw_character_bible` soft pointer
- Beat atom gains optional Subtext body section (for beats where dialogue carries weight)
- Manuscript-manifest gains `lfw_fiction_subgenre` (literary | thriller | mystery | romance | sff | speculative | historical | horror | ya), `lfw_active_overlays`, `lfw_active_craft_modules`, `lfw_show_dont_tell_calibration`
- Activity set expanded from 20 → 23: **DIALOGUE-AUDIT** (chapter 13 §3), **POV-VOICE-DRIFT** (chapter 13 §2), **THEME-CHECK** (chapter 14 §4)
- New opt-in craft modules: `show-dont-tell` (chapter 13 §4), `dialogue-and-subtext` (chapter 13 §1)
- Beat-sheet overlays as opt-in templates (Layer 2.5 between genre and instance): Story Circle, Save the Cat, Hero's Journey, Freytag (chapter 14 §2)
- Fiction sub-genre tunings of cadence thresholds (chapter 03 §6b''; chapter 14 §5)
- Optional per-POV voice-sample backbones (`_voice-samples-{pov-slug}.md`; chapter 13 §2)
- Validator extended: check 9 exempts sequel-typed Scenes; new check 10 (scene-type-legal); new advisory check 11 (pov-voice-register on established protagonists/antagonists)

## Connection to OVE's meta-ontology

LFW's three-layer ontology is itself an instance of the pattern documented in [Operating-Volume-Engineering](https://github.com/JawnLam/Operating-Volume-Engineering)'s `_design-engine/_meta/SCHEMA-OF-SCHEMAS.md`. LFW = Layer 1 (engine universals) + Layer 2 (genre branches) + Layer 3 (cartridge instances). OVE = Layer 1 (OVE universals) + Layer 2 (per-OV schemas) + Layer 3 (per-cartridge instances).

LFW is one valid OV-shape; OVE's protocol could be used to redesign LFW. (Self-similarity test, P9 in OVE's design principles, holds.)
