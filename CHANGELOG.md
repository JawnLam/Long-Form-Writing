# Changelog

All notable changes to Long-Form-Writing are documented in this file. Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versioning follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] — 2026-06-02

### Added — the development layer

The shift this release makes is from *production-and-continuity* to *production-and-growth*. v1.0 tracked the manuscript beautifully and tracked the writer not at all. v1.1 closes that gap with a development layer that models the writer's skill, makes the reader a first-class concern, separates argument from outline, and adds the feedback activities the production set was missing.

**New engine chapters:**

- **`09-WRITER-DEVELOPMENT.md`** — the craft-profile (OV-root, cross-cartridge) and craft-log (per-cartridge) artifacts; the diagnostic-not-instance feedback stance that turns "this transition is weak" (said ten times) into "you consistently end sections on the example without landing the closing claim — here's the targeted fix"; the **scaffolding fade** mechanism (`lfw_scaffolding_mode: full | gradual-fade | socratic`) with explicit session-count thresholds, so the OV designs in becoming-less-needed rather than hoping for it; the **opt-in craft modules** (`concrete-to-abstract`, `signposting`, `given-new`, `curse-of-knowledge`) as on-request coaching rather than silent enforcement; the two cautions (skill is observational not scored; craft-work-as-procrastination is the same anti-pattern as research-as-procrastination).
- **`10-READER-AND-ARGUMENT.md`** — the **Reader atom** as the non-fiction analog to Character; the **`_argument.md` backbone** as the argument's logical structure separate from `_outline.md`'s container hierarchy; the six new development activities defined formally (READER-SIMULATION, ARGUMENT-AUDIT, CLAIM-EVIDENCE-CHECK, STEELMAN, SYNTHESIS-CHECK, CRAFT-REVIEW).

**New atom type:**

- **Reader** (`LFW_Reader`) — first-class atom representing a modeled audience member. Status enum: `developing | active | retired`. Standard recommended set for non-fiction: The Skeptic, The Impatient Generalist, The Domain Expert. Used in READER-SIMULATION activities.

**New backbone files:**

- **`_argument.md`** — per-cartridge argument backbone (thesis, sub-claims, evidence map, defeaters, honest unknown). Required for non-fiction and dissertation cartridges; recommended for memoir / narrative non-fiction; optional for fiction with thematic argument.
- **`_craft-log.md`** — per-cartridge writer-pattern record. Optional but recommended for any serious project.

**New OV-root file:**

- **`_craft-profile.md`** — the cross-cartridge writer-skill memory. Persists across every cartridge. Operator-private (gitignored). Opt-in (writer creates when ready). Observational, never scored.

**Activity set expanded 10 → 16:**

The original ten production activities (SESSION-START, OUTLINE, DRAFT, REVISE, RESEARCH-INTEGRATION, READ-THROUGH, STUCK-DIAGNOSTIC, VOICE-CHECK, WORLDBUILDING, BETA-PREP) are unchanged. Six new development activities:

- **READER-SIMULATION** — AI reads a drafted atom as a specific Reader; reports resistance, lost threads, curse of knowledge
- **ARGUMENT-AUDIT** — pressure-tests `_argument.md` (contestability, sub-claim independence, evidence sufficiency, weakest link)
- **CLAIM-EVIDENCE-CHECK** — distinct from accuracy: does the evidence warrant a claim *this strong*?
- **STEELMAN** — strongest version of the counterargument before the writer rebuts
- **SYNTHESIS-CHECK** — flag sections that are annotated-bibliography-in-disguise
- **CRAFT-REVIEW** — periodic review of recent sessions + craft-log + craft-profile; surface patterns; propose practice focus

**Scaffolding fade:**

New per-cartridge frontmatter setting `lfw_scaffolding_mode` with three values (`full`, `gradual-fade`, `socratic`). The `gradual-fade` mode escalates AI withholding at explicit session-count thresholds (default: sessions 1–10 `full`, 11–30 partial fade, 31–60 major fade, 61+ writer-led on structure). Thresholds are customizable in `lfw_scaffolding_thresholds`. Mechanism by which the OV designs in needing-it-less over time.

**Opt-in craft modules:**

Four shipped modules, on-demand per REVISE or READ-THROUGH pass: `concrete-to-abstract`, `signposting`, `given-new`, `curse-of-knowledge`. Never silent enforcement; surface-on-request only.

**New templates:**

- `TEMPLATE-Reader.md`
- `TEMPLATE-craft-profile.md`
- `TEMPLATE-craft-log.md`
- `TEMPLATE-argument.md`

**Meta updates:**

- `_meta/SCHEMA-OF-SCHEMAS.md` — three-layer ontology expanded to four (Layer 0 = OV-root persistent files; Layer 1 = per-cartridge universals; Layer 2 = per-genre branches; Layer 3 = per-cartridge instances). New atom + backbones documented.
- `_meta/FAILURE-MODES.md` — added F18 (craft-work-as-procrastination), F19 (scaffolding-never-fades), F20 (skill-scoring-attempted), F21 (reader-atoms-used-to-flatter).

**Validator:**

- Extended `STATUS_ENUM` to include `reader: {developing, active, retired}`
- Extended `BACKBONE_FILES` to include `_argument`, `_craft-log`
- Same eight checks; now covers all new artifacts

**Worked example updates:**

- Three Reader atoms added: `Skeptic.md`, `Impatient-Generalist.md`, `Domain-Expert.md`
- `_argument.md` populated with the persistence-question's five sub-claims, evidence map, defeaters, honest-unknown, and live independence concerns from current ARGUMENT-AUDIT considerations
- `_craft-log.md` populated with two early-observed patterns (soft-close-on-example, em-dash cadence dependency) as worked-example
- `_manuscript-manifest.md` updated with `lfw_scaffolding_mode: gradual-fade` and documentation of the development-layer files
- `_state.md` updated with Readers section and four new open threads pointing at the development activities

**`.gitignore` updates:**

`_craft-profile.md`, `**/_craft-log.md`, `**/_argument.md` now excluded by default (operator-private; writers using LFW for their own work want these in their personal git but not in shared/forked OV copies). Worked-example overrides preserve the shipped reference content.

### Notes

The development layer is the cybernetic move that v1.0 was missing. A controller needs memory of past states to correct error modes; v1.0 had complete manuscript-state memory and zero writer-state memory. v1.1's craft-profile + craft-log are exactly that controller memory. Every other addition (Readers, argument backbone, six new activities, scaffolding fade) follows from the same reframe: the OV exists to make the writer better, not just to get the book finished.

This release deliberately preserves v1.0's anti-patterns guardrails (no AI silent rewrites; voice belongs to the writer; activities require explicit writer confirmation) while adding the development surfaces. The scaffolding fade and the opt-in craft modules in particular are designed so that more AI involvement does not mean more AI control — the writer's hand stays on the wheel.

The conceptual pass focuses on non-fiction. Fiction-specific equivalents (Character-driven equivalents of the development activities, plot-structure auditing, narrative-arc tracking) are the next pass.

---

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
