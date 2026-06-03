# Changelog

All notable changes to Long-Form-Writing are documented in this file. Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versioning follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.1] — 2026-06-02

### Fixed — structural integrity of the worked example + engine consistency

Four classes of structural defects identified in v1.0 and fixed in this patch:

- **Wiki-link namespace normalized.** v1.0 shipped the worked example with three competing naming conventions for the same atom files (order-only `[[01-Hoshi-Opening]]`, chapter-prefixed file `03-01-Hoshi-Opening.md`, plus variant short/long Source names). All links now use the canonical chapter-prefixed filename form. `_writing-engine/04-ATOMS-AND-STRUCTURE.md` updated with explicit naming conventions per atom type and an explicit "Item_ID is a separate namespace from filenames" section.
- **Stub atoms shipped** for every atom referenced in `_state.md`, `_outline.md`, Thread atoms, and Chapter compositions but not previously present (33 stubs total: 6 Chapters, 11 Sections, 13 Sources, 3 session logs). The example cartridge's link graph is now closed: every wiki-link resolves to a real file.
- **Status enum unified.** v1.0 had three different `lfw_status` enums across templates (Beat: `planned|drafted|revised|final`; Chapter: `outlined|drafting|drafted|revising|revised|final`; Section: `planned|drafted|revised|fact-checked|final`). Section in the worked example was set to `drafting`, which was illegal under its own template. Now all prose-bearing atoms (Beat / Scene / Section / Chapter / Act) share one canonical enum: `planned | drafting | drafted | revising | revised | final`. Non-fiction Section adds `fact-checked` between `revised` and `final`. `outlined` deprecated.
- **Act and Setting templates shipped.** v1.0 advertised screenplay and play genre support but didn't ship `TEMPLATE-Act.md` or `TEMPLATE-Setting.md`, violating the engine's own "extending atom set requires a template" rule. Both templates added; `04-ATOMS-AND-STRUCTURE.md` documents them.

### Added — validator

- **`_writing-engine/_scripts/validate.py`** — stdlib-only Python validator that walks one or more cartridges and reports structural issues across eight checks (wiki-link resolution, _state reference existence, status enum legality, atom-type known, template existence, filename conformance, required frontmatter, Item_ID uniqueness). Exit code 0 on clean, 1 on issues. Optional tooling; not part of session flow. See `_writing-engine/_scripts/README.md` for usage.

### Notes

The defects fixed in v1.0.1 were structural only — they would have surfaced as broken links, illegal status values, and missing templates when an AI actually tried to use the v1.0 OV in the real world. Topical and conceptual issues (which the validator deliberately does not check) remain to be addressed in subsequent patches.

The validator turns the audit checklist in `_meta/SCHEMA-OF-SCHEMAS.md` from prose into something executable, closing the v1.0 enforcement gap that allowed all four structural defects to ship undetected.

---

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
