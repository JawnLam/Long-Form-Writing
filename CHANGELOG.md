# Changelog

All notable changes to Long-Form-Writing are documented in this file. Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versioning follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.3.1] — 2026-06-03

### Added — writer-side fiction craft pass

First of a two-pass patch series. v1.3.1 covers the line-level craft and structural-overlay artifacts: dialogue, POV-voice differentiation, scene-and-sequel rhythm, show-don't-tell craft module, Character-Bible atom, Theme atom, fiction sub-genre branching, beat-sheet overlays. v1.3.2 (next) will add the structural-artifact layer (`_worldbuilding.md`, multi-layer timeline, storyboard, style sheet, names list, research-as-inspiration, relationship map, stakes ladder).

**New engine chapters:**

- **`13-FICTION-DIALOGUE-AND-POV-VOICE.md`** — four-axis dialogue function check (Plot / Character / Subtext / Rhythm); the dialogue-tells sub-section; the DIALOGUE-AUDIT activity; POV-voice-register frontmatter and the POV-VOICE-DRIFT activity; per-POV voice samples (optional); show-don't-tell craft module with calibration field; updated Beat atom Subtext body section
- **`14-FICTION-STRUCTURE-OVERLAYS-AND-EXTENSIONS.md`** — scene-and-sequel rhythm with the `lfw_scene_type` field; four beat-sheet overlays (Story Circle, Save the Cat, Hero's Journey, Freytag); the Theme atom with THEME-CHECK activity; the Character-Bible atom; fiction sub-genre branching with per-sub-genre cadence-tunings

**New atom types:**

- **Character-Bible** (`LFW_Character_Bible`) — opt-in extended companion to Character; for POV-bearing, antagonist, and major-supporting characters. Status enum: `drafting | established | revised | final`. Lives in `Atoms/Character-Bibles/`. Operator-private by default
- **Theme** (`LFW_Theme`) — first-class atom for the abstract idea the manuscript is about; carried-not-declared; distinct from Motif (image) and `_argument.md` (logical structure). Status enum: `candidate | developing | threaded | resolved`. Lives in `Atoms/Themes/`

**Scene atom additions (backward-compatible):**

- `lfw_scene_type: scene | sequel | scene-sequel` — defaults to `scene`; sequel-typed atoms carry a decision (next scene's want) instead of a value-shift. Validator check 9 exempts sequel-typed Scenes from value-shift requirements. New `## Sequel` body section for sequel-typed atoms

**Character atom additions (backward-compatible):**

- `lfw_pov_voice_register` — structured POV-voice fields (sentence_length, diction, interiority_mode, tense_preference, signature_moves, avoid_moves). Required for POV-bearing Characters per chapter 13; optional otherwise. Validator check 11 issues advisory warnings when an established protagonist/antagonist omits the field
- `lfw_character_bible` — soft pointer to extended Character-Bible atom
- `### Dialogue tells` sub-section under Voice and prose register — sentence shape, diction range, pet phrases, verbal tics, what they say when they don't know what to say, what they say when lying, what they say under pressure
- Optional `## Subtext patterns` body section

**Beat atom addition (backward-compatible):**

- Optional `## Subtext` body section — for beats where dialogue carries weight (surface, underneath, listener-registers, reader-registers)

**Manuscript-manifest additions (backward-compatible):**

- `lfw_fiction_subgenre: literary | thriller | mystery | romance | sff | speculative | historical | horror | ya` — advisory; tunes activity cadence per chapter 03 §6b''
- `lfw_active_overlays: []` — declares which beat-sheet overlays are active
- `lfw_active_craft_modules: []` — declares which opt-in craft modules are active
- `lfw_show_dont_tell_calibration` — standing position (strict-show / balanced / telling-narrator-as-voice / off) and load-bearing-only flag

**Activity set expanded 20 → 23:**

- **DIALOGUE-AUDIT** — four-axis function check on drafted dialogue; surface zero/one-axis lines
- **POV-VOICE-DRIFT** — audit prose voice across alternating-POV chapters against each POV's lfw_pov_voice_register; surface register-bleed
- **THEME-CHECK** — audit Theme atoms against drafted prose; surface gaps in threading, on-the-nose treatment, motif/theme cross-references

**Sub-genre tunings (chapter 03 §6b''):**

Cadence thresholds shift per sub-genre:

- thriller / mystery / horror: SETUP-PAYOFF-AUDIT triggers at ≥6 scenes (default ≥10)
- romance / multi-POV literary: POV-VOICE-DRIFT triggers at ≥6 sessions (default ≥8)
- SFF / historical: WORLDBUILDING more frequent; CONTINUITY-CHECK at ≥6 scenes
- literary / speculative: THEME-CHECK at ≥6 sessions (default ≥10)

**Beat-sheet overlays (opt-in):**

Four shipped overlay templates that read against `_spine.md` as a diagnostic lens (not a writing prescription):

- Story Circle (Dan Harmon, 8 beats) — most fiction; literary-friendly
- Save the Cat (Blake Snyder, 15 beats) — commercial; screenplay-adjacent
- Hero's Journey (Campbell / Vogler, 12 stages) — mythic / fantasy / quest
- Freytag's Pyramid (1863, 5 beats) — classical / dramatic / literary

Cartridges declare active overlays in the manifest; the overlay file lives at `<Cartridge>/_overlay-{name}.md`.

**New opt-in craft modules:**

- `show-dont-tell` (chapter 13 §4) — calibrated to the writer's standing position; surfaces asserted-not-shown moments and over-dramatized routine transitions
- `dialogue-and-subtext` (chapter 13 §1) — scene-running quick check during revision (lighter than the full DIALOGUE-AUDIT activity)

**New templates:**

- `TEMPLATE-Character-Bible.md`
- `TEMPLATE-Theme.md`
- `TEMPLATE-overlay-story-circle.md`
- `TEMPLATE-overlay-save-the-cat.md`
- `TEMPLATE-overlay-heros-journey.md`
- `TEMPLATE-overlay-freytag.md`
- Updated: `TEMPLATE-Scene.md` (lfw_scene_type field; Sequel body section)
- Updated: `TEMPLATE-Character.md` (lfw_pov_voice_register, lfw_character_bible, dialogue-tells sub-section, subtext-patterns section)
- Updated: `TEMPLATE-Beat.md` (Subtext body section)
- Updated: `TEMPLATE-manuscript-manifest.md` (sub-genre, active-overlays, active-craft-modules, show-don't-tell calibration)
- Updated: `TEMPLATE-spine.md` (scene-vs-sequel column in ledger)

**Meta updates:**

- `_meta/SCHEMA-OF-SCHEMAS.md` — Layer 1 universals updated for v1.3.1 atoms and fields; activity count 20 → 23; v1.3.1 additions section added
- `_meta/FAILURE-MODES.md` — added F31 (dialogue-as-info-dump), F32 (interchangeable-dialogue), F33 (on-the-nose-subtext), F34 (POV-voice-bleed), F35 (show-everything-pathology), F36 (style-sheet-drift), F37 (AI-homogenizes-POV-voices), F38 (missing-sequels), F39 (over-sequel'd-thriller), F40 (sequel-without-decision), F41 (overlay-as-formula), F42 (on-the-nose-theme), F43 (character-bible-as-procrastination), F44 (sub-genre-miscalibration)

**Validator:**

- Extended `STATUS_ENUM` with `character-bible` and `theme`
- Updated check 9 (scene-value-shift) to exempt sequel-typed Scenes
- New check 10 (scene-type-legal) — lfw_scene_type, when set, must be scene / sequel / scene-sequel
- New check 11 (pov-voice-register-advisory) — established protagonists/antagonists should declare lfw_pov_voice_register
- Beat filename pattern broadened further to accept both v1.1 and v1.2 forms (no change from v1.2; documented for completeness)

**Worked example updated:**

- `Example-Project-The-Late-Frost/` migrated to v1.3.1 in session 004 (META session):
  - Sub-genre declared (`literary`); three craft modules activated; show-don't-tell calibrated to `balanced`
  - Maya and Sarah Character atoms gained POV-voice-register (with mirror-discipline avoid-moves), dialogue tells sub-sections, subtext patterns sections
  - Maya gained extended Character-Bible (`Maya-Hollis-Bible`) — 15 sections including chronological backstory 1984–2026
  - Theme atom created: `Honesty-Under-Cost` — central; cross-referenced with both motifs and both Characters; treatment-risks section names four specific risks for this manuscript
  - Story Circle overlay populated; beat 8 (Change) deliberately divergent; divergence documented as enactment of theme
  - Scene 01-01 declared `lfw_scene_type: scene`

**`.gitignore` updates:**

- `Atoms/Character-Bibles/*` excluded by default (operator-private bibles)
- `**/_overlay-*.md` excluded by default
- `**/_voice-samples-*.md` excluded by default (per-POV voice samples)
- Theme atoms remain tracked by default (themes are often discussed in pitches and proposals)
- Worked-example overrides preserve shipped reference content

### Notes

v1.3.1 closes three of the highest-leverage line-level craft gaps in fiction. The POV-voice-register's mirror-discipline (each POV's avoid_moves are the other POV's signature_moves) is the structural defense against POV-voice-bleed; the four-axis dialogue function check makes line-level dialogue auditable; the Character-Bible gives long-novel character work the depth-of-record it needs without bloating the Character atom.

The scene-and-sequel discipline matters most for literary fiction (where sequel-beats often do the prose's emotional work) and least for thriller (where the form compresses or skips sequels). The sub-genre tuning ensures the activity-decision algorithm respects this.

The beat-sheet overlays are deliberately opt-in and explicitly framed as reading lenses rather than writing prescriptions. The most-common failure mode (F41 — overlay-as-formula) is named in every overlay template's Risks section.

The Theme atom is distinct from Motif (image-cluster) and from `_argument.md` (non-fiction's declared logical structure). Theme is what's *carried* through the manuscript by mechanism; the validator does not enforce theme treatment, but the THEME-CHECK activity surfaces on-the-nose moments and threading gaps.

This release is backward-compatible with all v1.0 / v1.1 / v1.2 cartridges. Existing fiction cartridges without v1.3.1 fields remain valid; the AI surfaces the v1.3.1 additions during CRAFT-REVIEW and the next BOOTSTRAP-NEW-MANUSCRIPT session.

---

## [1.2.0] — 2026-06-02

### Added — fiction conceptual pass

The shift this release makes is two-sided. First, the v1.1 production-and-growth reframe that the development layer brought to non-fiction is now extended to fiction (Reader atoms, scaffolding fade, CRAFT-REVIEW, and craft-profile/log already work for fiction; v1.2 adds fiction-weighted activities, error vocabulary, and a craft module that fiction needed). Second, and specific to fiction: the v1.0/v1.1 schema was *under-serving* fiction structurally. The plot's causal backbone, scene-by-scene value-shifts, the setup-payoff relationship between scenes, motif tracking, world-rule continuity, and the information-state ledger between POV characters were all left to ad-hoc notes. v1.2 makes them first-class.

**New engine chapters:**

- **`11-FICTION-PLOT-SPINE.md`** — the **`_spine.md` backbone** as premise-as-causal-claim, dramatic question, scene-by-scene value-shift ledger, but/therefore audit, escalation curve, mid-act crisis and climax markers, honest open; the **value-shift discipline** as load-bearing scene-craft (every drafted Scene must turn — `from` and `to` value-states must differ); the **but/therefore vs. and-then test** for causal-chain soundness; the **`_promises.md` setup-payoff ledger** as the fiction equivalent of the argument-evidence ledger, with promises planted / fired / outstanding / retired; the **SCENE-AUDIT** and **SETUP-PAYOFF-AUDIT** activities defined formally
- **`12-FICTION-CHARACTER-AND-CONTINUITY.md`** — the **Motif atom** as first-class atom for image-clusters, recurrent objects, and thematic carriers (Status enum: `latent | emerging | woven | resolved`); the **CHARACTER-CONSISTENCY** activity with the antagonist-steelman discipline (the antagonist's reasoning must be sound from inside the antagonist's frame, not merely "what the antagonist would think"); the **`_continuity.md` ledger** as the cybernetic memory for world-rules, timeline, and the information-state ledger (who knows what, when); the **CONTINUITY-CHECK** activity; the **`pov-and-psychic-distance`** opt-in craft module; the **fiction READER-SIMULATION reframe** (the reader is reading for emotional weight, tonal register, and character-cues — not for arguments)

**New atom type:**

- **Motif** (`LFW_Motif`) — first-class atom representing recurrent image, object, or thematic carrier. Status enum: `latent | emerging | woven | resolved`. Tracks intended appearances across the manuscript with avoid-lists for vocabulary discipline. Used in MOTIF-CHECK and READ-THROUGH activities.

**New backbone files (fiction-weighted):**

- **`_spine.md`** — per-cartridge causal-spine backbone (premise-as-causal-claim, dramatic question, scene-by-scene value-shift ledger, escalation curve, mid-act and climax markers, and-then check). Required for plot-driven fiction; recommended for any narrative work
- **`_continuity.md`** — per-cartridge continuity ledger (world-rules, timeline, information-state ledger, cross-reference index). Required for any fiction with non-trivial worldbuilding or multi-POV information asymmetry
- **`_promises.md`** — per-cartridge setup-payoff ledger (promises planted / fired / outstanding / retired). Required for plot-driven fiction

**Scene schema update:**

- Two new optional Scene frontmatter fields: `lfw_value_shift_from`, `lfw_value_shift_to`. Optional at status `planned | drafting`; **required and must differ** at status `drafted | revising | revised | final`. The validator enforces this (check 9, scene-value-shift). New `## Value-shift` body section in the Scene template captures whose want, the conflict, the start-state, the end-state, the turn, and the but/therefore connector to the next scene.

**Activity set expanded 16 → 20:**

The original ten production activities (v1.0) and six development activities (v1.1) are unchanged. Four new fiction-weighted development activities:

- **SCENE-AUDIT** — works against `_spine.md`; checks that each Scene's value-shift is declared, that `from ≠ to`, that the but/therefore connector to the next scene is not "and then"
- **CHARACTER-CONSISTENCY** — works against Character atoms; surfaces voice / behavior / want drift; for antagonist Characters specifically checks the steelman is still loadbearing
- **CONTINUITY-CHECK** — works against `_continuity.md`; surfaces world-rule violations, timeline inconsistencies, information-state violations (a character "knowing" something they shouldn't yet)
- **SETUP-PAYOFF-AUDIT** — works against `_promises.md`; surfaces unfired promises, payoffs without setups, and faded promises (outstanding for many chapters with no recent foreshadowing)

**Craft profile and log additions:**

- **`pov-and-psychic-distance`** opt-in craft module added to the v1.1 module set (`concrete-to-abstract`, `signposting`, `given-new`, `curse-of-knowledge`) — on-demand coverage of close-third / omniscient / first-person consistency and psychic-distance modulation
- **Fiction-specific error vocabulary** added to chapter 09 (the writer-development chapter): asserted-not-shown value-shifts, antagonist-not-steelmanned, motif-overstated, motif-orphaned, scene-doesn't-turn, and-then-spine, information-state violation, voice-bleeds-between-POVs, planted-promise-not-fired, payoff-not-planted, on-the-nose-symbolism. These become the diagnostic vocabulary for CRAFT-REVIEW on fiction cartridges.

**New templates:**

- `TEMPLATE-Motif.md`
- `TEMPLATE-spine.md`
- `TEMPLATE-continuity.md`
- `TEMPLATE-promises.md`
- Updated: `TEMPLATE-Scene.md` (adds `lfw_value_shift_from` and `lfw_value_shift_to` to frontmatter; adds `## Value-shift` body section)

**Meta updates:**

- `_meta/SCHEMA-OF-SCHEMAS.md` — Layer 1 universals updated for v1.2 fiction backbones and Motif atom; Layer 2 per-genre branch expanded with fiction-specific elements; audit checklist expanded; v1.2 additions section added
- `_meta/FAILURE-MODES.md` — added F22 (asserted-not-shown value-shift), F23 (antagonist-not-steelmanned), F24 (motif-overstated-by-AI), F25 (and-then-spine-allowed-to-ship), F26 (continuity-violations-treated-as-prose-issues), F27 (information-state-violation), F28 (POV-distance-collapses-during-revision), F29 (scaffolding-fails-to-fade-in-fiction), F30 (planted-promises-go-unfired)

**Validator:**

- Extended `STATUS_ENUM` to include `motif: {latent, emerging, woven, resolved}`
- Extended `BACKBONE_FILES` to include `_spine`, `_continuity`, `_promises`
- New check 9 (`scene-value-shift`): enforces value-shift discipline on drafted Scenes — both fields set and must differ
- Beat filename pattern broadened to accept both v1.1 chapter-prefixed and v1.2 cartridge-side `Beat-NN-NN-NN-<slug>` forms

**Worked example added:**

- **`Example-Project-The-Late-Frost/`** — fiction cartridge (literary novel, two estranged sisters + Sonoma vineyard + late-frost season + family-debt secret) at session 3 / early-drafting stage. Demonstrates: all four v1.2 backbones populated (`_spine.md`, `_continuity.md`, `_promises.md`, `_craft-log.md`); 1 Chapter + 1 Scene with full value-shift section; 5 Beats with one (Beat-04) carrying a worked SCENE-AUDIT flag (asserted-not-shown value-shift); 2 Characters (Maya the protagonist + Sarah the antagonist with explicit four-reason steelman); 2 Readers (literary-fiction reader + vineyard expert); 2 Motifs (the late frost + the empty chair) at different status levels (`emerging` and `latent`); 1 bootstrap session log capturing the steelman-discipline moment.

**`.gitignore` updates:**

- `**/_spine.md`, `**/_continuity.md`, `**/_promises.md` now excluded by default (operator-private working artifacts; same logic as `_argument.md` and `_craft-log.md` in v1.1). Worked-example overrides preserve the shipped reference content.

### Notes

v1.2 is the conceptual completion of the four-corners design. Non-fiction has its argument-and-evidence backbone (v1.1); fiction now has its causal-spine, motif, continuity, and setup-payoff backbone (v1.2). The development layer (writer-skill model, scaffolding fade, opt-in craft modules, CRAFT-REVIEW) now applies cleanly across both, with fiction-weighted activities and a fiction-specific error vocabulary that v1.1 deliberately deferred.

The value-shift discipline is the single most load-bearing fiction-craft enforcement v1.2 adds. Validator check 9 makes the SCENE-AUDIT rule executable, not merely aspirational. The steelmanned-antagonist discipline is the second — character atoms for antagonists must now include a from-inside-the-frame steelman, and the CHARACTER-CONSISTENCY activity audits whether the steelman is still loadbearing as the manuscript evolves.

The fiction READER-SIMULATION reframe matters: v1.1's READER-SIMULATION was implicitly argumentative (the Reader is reading for argument quality). For fiction, the Reader is reading for emotional weight, tonal register, character-specific cues, and the moment-to-moment perceptual experience. The Vineyard-Expert reader atom in the worked example shows the domain-expert reader specialized for fiction (catching technical errors in the setting without flattening the literary read).

The scaffolding-fade discipline matters more in fiction than in non-fiction, because invention is the central skill the OV must not crowd out. The Late Frost cartridge ships in `gradual-fade` mode, with the explicit chapter-12 note about why fiction's fade thresholds are tighter than non-fiction's.

This release is backward-compatible with all v1.0 and v1.1 cartridges. Existing fiction cartridges without `_spine.md`, `_continuity.md`, `_promises.md`, or Motif atoms remain valid; the AI surfaces the v1.2 additions during BOOTSTRAP and CRAFT-REVIEW sessions but does not retroactively require them.

---

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
