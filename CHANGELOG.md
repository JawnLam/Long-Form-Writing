# Changelog

All notable changes to Long-Form-Writing are documented in this file. Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versioning follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] — 2026-06-02

### Added — initial public release

- **Writing engine** (`_writing-engine/`):
  - `00-START-HERE.md` — assistant entry point + mandatory read order
  - `01-WHAT-IS-LFW.md` — definition, what an LFW cartridge is, what it isn't
  - `02-GENRE-AND-SCHEMA.md` — how the schema branches per cartridge genre (fiction / non-fiction / screenplay / play / dissertation)
  - `03-CADENCE-AND-SESSIONS.md` — daily-practice protocol; ten universal session activities (SESSION-START, OUTLINE, DRAFT, REVISE, RESEARCH-INTEGRATION, READ-THROUGH, STUCK-DIAGNOSTIC, VOICE-CHECK, WORLDBUILDING, BETA-PREP)
  - `04-ATOMS-AND-STRUCTURE.md` — atom-type definitions (Beat, Scene, Section, Chapter, Character, Thread, Source, Note); relationships; composition rules
  - `05-VOICE-AND-CRAFT.md` — configurable three-tier voice model (writer-maintains-default / voice-samples-optional / VOICE-CHECK-on-demand); craft conventions
  - `06-RESEARCH-INTEGRATION.md` — for non-fiction and dissertation: source ingestion, citation discipline, fold-in protocol, anti-fabrication rules
  - `07-REVISION-DISCIPLINE.md` — multi-pass revision (structure / voice / accuracy / prose-line); revision-pass log conventions
  - `08-FINISHING.md` — getting from drafted to shippable; beta-reader prep; assembly; honest-thinness audit
  - `BOOTSTRAP-NEW-MANUSCRIPT.md` — cartridging prompt for opening a new manuscript engagement
- **Templates** (`_writing-engine/_templates/`):
  - Atom templates: `TEMPLATE-Beat.md`, `TEMPLATE-Scene.md`, `TEMPLATE-Section.md`, `TEMPLATE-Chapter.md`, `TEMPLATE-Character.md`, `TEMPLATE-Thread.md`, `TEMPLATE-Source.md`, `TEMPLATE-Note.md`
  - Cartridge backbone: `TEMPLATE-manuscript-manifest.md`, `TEMPLATE-state.md`, `TEMPLATE-outline.md`, `TEMPLATE-voice-samples.md`
  - Process: `TEMPLATE-Session.md`, `TEMPLATE-revision-pass.md`
- **Meta** (`_writing-engine/_meta/`):
  - `SCHEMA-OF-SCHEMAS.md` — three-layer ontology applied to LFW (engine universals / per-genre branch / per-instance)
  - `FAILURE-MODES.md` — canonical catalog of LFW-specific and inherited failure modes (multi-bullet questionnaire, fabrication, identity inference, AI voice homogenization, drafting-before-outlining, scope creep, abandoned-revision-pass, etc.)
- **Root docs**: `README.md`, `AI-BOOTSTRAP.md`, `INSTALL.md`, `OPERATOR-GUIDE.md`, `CONTRIBUTING.md`, `LICENSE.md` (CC-BY 4.0), `VERSION.md`, this file, `_USER.md.template`, `.gitignore`
- **One worked-example cartridge**: `Example-Project-The-Persistence-Question/` — a hypothetical non-fiction book about *why some institutions, traditions, and ideas persist across centuries while others vanish in decades* — at outlining-to-mid-draft stage. Demonstrates: structural outline, source atoms with real citations to real (publicly known) works, thread atoms, section atoms with prose, beat atoms, voice samples, session logs, and a revision pass.

### Notes

Long-Form-Writing v1.0 is the fourth operating volume in the same author's trio-now-quartet:

- **[SOLVE-eX](https://github.com/JawnLam/SOLVE-eX)** — decision-making and problem-solving
- **[LifeLong-Learning](https://github.com/JawnLam/LifeLong-Learning)** — self-directed deep study
- **[Operating-Volume-Engineering](https://github.com/JawnLam/Operating-Volume-Engineering)** — the propagator
- **Long-Form-Writing** (this) — sustained writing across multi-month/multi-year projects

LFW takes the cartridge-as-manuscript pattern that appeared as a lighter worked-example inside OVE v1.0 and develops it fully. The daily-practice cadence and configurable voice model are the distinctive innovations.
