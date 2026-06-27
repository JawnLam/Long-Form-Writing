# Changelog

All notable changes to Long-Form-Writing are documented in this file. Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versioning follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.8.1] — 2026-06-27

Patch — **terminology retirement: "Prototype" → "Type".** The OVE engine concept formerly called a *Prototype* (the type-definition unit) is now uniformly called a **Type**, completing the OKF `type` vocabulary adopted in 1.8.0. Infrastructure surfaces only — `_writing-engine/` docs, `SCHEMA-OF-SCHEMAS.md`, `_scripts/validate.py`, the 27 `_types/LFW_*.md` definitions, templates, and front-door docs. Manuscript/craft prose, historical CHANGELOG entries below, and Hugo are unchanged. No behavioral or content change.

## [1.8.0] — 2026-06-26

Google OKF v0.1 conformance (coordinated with vault Master_Schema v1.23.0 + OVE v2.4.0). Universal Core renamed to OKF field names (Item_Prototype→type, Title→title, Tags→tags; added timestamp from Date_Modified, optional description/resource). Convention-6 folder _Prototypes/ → _types/. Date_Modified kept, time-synced with timestamp. Hugo excluded.

## [1.7.2] — 2026-06-07

Patch release adding `UPDATE-PROMPT.md` at the LFW root — the fourth required artifact under OVE Convention 7 (added in OVE v1.2.1).

### Added — `UPDATE-PROMPT.md`

Copy-pasteable AI prompt that asks any AI assistant (Claude, ChatGPT, Gemini, Cursor, Claude Code) to walk the operator through updating LFW to the latest release. The prompt instructs the AI to:

1. Read `INSTALL.md § "Updating"` and `OPERATOR-GUIDE.md § "Updates and troubleshooting"` so it knows LFW's update protocol.
2. Run `git fetch origin` and report incoming commits + the new CHANGELOG entry.
3. Check `git status` and propose a stash strategy if local engine modifications exist.
4. Walk through `git pull --ff-only origin main` step by step, stopping to confirm before running.
5. Surface migration recipes, major.minor folder renames, breaking-change notes from the new CHANGELOG entry.
6. Verify the operator's manuscript cartridges (Operator-Extension Zone) and operator-private files (`_USER.md`, `_craft-profile.md`, per-cartridge state/sessions/revision-passes, voice samples, character bibles, timelines, inspirations) are intact and untouched after the pull.

The prompt enforces discipline:

- Do not modify Operator-Extension or Operator-Private Zone content.
- Do not run destructive commands without explicit operator confirmation.
- Stop and ask if anything is unclear or unexpected.

### Why two update paths

OVE Convention 7 supports both a **manual path** (operator reads `INSTALL.md § Updating` and `OPERATOR-GUIDE.md § Updates`, runs git commands themselves) and an **AI-assisted path** (operator opens `UPDATE-PROMPT.md`, copies the prompt, pastes to an AI, approves each step). Manual path is recommended for major-version transitions and any release with a non-trivial migration recipe; AI-assisted path is recommended for routine releases (patches and small minors).

### Notes

Patch release — purely additive. No engine prose modified; no schema change; no Prototype content moved; no `.gitignore` change.

Coordinated multi-OV release with OVE v1.2.1 (codifies the artifact + adds validator C10), LLL v1.3.1, SOLVE-eX v2.1.3.

## [1.7.1] — 2026-06-06

Patch release adopting OVE Conventions 7 (install-and-update pattern) and 8 (engine vs operator-content boundary). Also fixes a bug in v1.7.0: the `.gitignore` patterns still referenced the old `Atoms/` folder name (renamed to `Items/` in v1.6.0).

### Fixed — `.gitignore` patterns now match the post-v1.6.0 folder structure

v1.6.0 renamed `Atoms/` to `Items/` across the repo, but `.gitignore` was missed. As a result, operator-private artifacts that should have been excluded from tracking — character bibles, timelines, inspirations — were tracked by default since v1.6.0.

- `**/Atoms/Character-Bibles/*.md` → `**/Items/Character-Bibles/*.md`
- `**/Atoms/Timelines/*.md` → `**/Items/Timelines/*.md`
- `**/Atoms/Inspirations/*.md` → `**/Items/Inspirations/*.md`

Inline comments added to flag the rename history. Operators of v1.6.0 or v1.7.0 with private character bibles in their working copies should check whether those files got tracked by accident; if so, untrack with `git rm --cached <file>` then re-commit.

### Added — OVE Convention 7 (install-and-update pattern)

`INSTALL.md` rewritten with:

- **§ 1** — canonical git-clone-with-push-disabled install snippet. Concrete URL: `https://github.com/JawnLam/Long-Form-Writing.git`. Folder convention: `Long-Form-Writing-v<major>.<minor>`.
- **§ 1a** — alternative no-git install (download ZIP, manual copy).
- **§ 8 — Updating** — `git fetch` + `git log --oneline HEAD..origin/main` + `git pull --ff-only`, with stash-pop fallback for when local engine edits would conflict.
- Major.minor folder transition snippet (`mv Long-Form-Writing-v1.7 Long-Form-Writing-v1.8`).

`OPERATOR-GUIDE.md` gains:

- **§ 9 — Updates and troubleshooting** — clean fast-forward, stash-pop conflict resolution (`git checkout --theirs`), recovery for lost files, major.minor folder transitions, contributing back upstream (re-enable push to your fork; never to upstream).

### Added — OVE Convention 8 (engine vs operator-content boundary)

`CONTRIBUTING.md` gains:

- **§ 7 — Content zones** — declares the four zones with concrete path patterns:
  - **Engine Zone** — front-door docs, `_writing-engine/`, `_types/`, `_USER.md.template`, `.gitignore`
  - **Operator-Private Zone** — `_USER.md`, `_craft-profile.md`, per-cartridge state/sessions/revision-passes, voice samples, craft logs, argument/spine/continuity/promises backbones, overlays, worldbuilding/storyboard/style-sheet/relationships, operator-private Items (character-bibles, timelines, inspirations)
  - **Operator-Extension Zone** — operator's own manuscript cartridges parallel to `Example-Project-*`
  - **Shipped Examples Zone** — `Example-Project-The-Late-Frost/`, `Example-Project-The-Persistence-Question/`

`OPERATOR-GUIDE.md` gains:

- **§ 8 — Engine vs your work** — plain-English explanation of the four-zone boundary, with concrete file/folder examples per zone.

### Notes

This is a patch release: no engine prose changed beyond the documentation additions; no schema change; no Prototype changes; no `_types/` content moved.

The `.gitignore` fix is the only behavioral change. Operators on v1.7.0 with private character-bible / timeline / inspiration content should audit whether those files got tracked since v1.6.0 (likely yes if they did `git add .` since then) and untrack as needed.

This release is part of an OVE-coordinated multi-OV cycle: OVE v1.2.0 codifies Conventions 7 and 8; LFW v1.7.1 retrofits them here; LLL v1.3.0 and SOLVE-eX v2.1.2 retrofit them in parallel.

## [1.7.0] — 2026-06-06

Adopts Operating-Volume-Engineering Convention 6 (every OV ships its own `_types/` folder for portability). Completes the lowercase-form of v1.6.0's atom → Item rename in templates and Item files. No new engine capability; the contribution is **portability** — anyone cloning this repo without the operator's vault Infrastructure now gets the full Prototype definitions out of the box.

### Added — `_types/` folder with 36 LFW Prototype definitions

A new top-level folder, `_types/`, contains one Markdown file per LFW Prototype in the namespace. Each file is structured per OVE's `TEMPLATE-Prototype.md` (Purpose, Required frontmatter, Body structure, Naming, Example Item, Relationships, Notes). The 36 files:

- **Already in vault** (9, from v1.16.0; verbatim mirrors of `~/Obsidian/.../_Infrastructure For All Vaults/_types/LFW_*.md`): `LFW_Beat`, `LFW_Chapter`, `LFW_Character_Bible`, `LFW_Motif`, `LFW_Note`, `LFW_Reader`, `LFW_Scene`, `LFW_Session`, `LFW_Source`.
- **Authored new** (27 — declared in shipping templates but never previously written as standalone Prototype definitions anywhere): `LFW_Act`, `LFW_Argument`, `LFW_Character`, `LFW_Continuity`, `LFW_Craft_Log`, `LFW_Craft_Profile`, `LFW_Inspiration`, `LFW_Manuscript_Manifest`, `LFW_Outline`, `LFW_Overlay_Freytag`, `LFW_Overlay_Heros_Journey`, `LFW_Overlay_Save_The_Cat`, `LFW_Overlay_Story_Circle`, `LFW_Promises`, `LFW_Relationships`, `LFW_Revision_Pass`, `LFW_Section`, `LFW_Setting`, `LFW_Spine`, `LFW_State`, `LFW_Storyboard`, `LFW_Style_Sheet`, `LFW_Theme`, `LFW_Thread`, `LFW_Timeline`, `LFW_Voice_Samples`, `LFW_Worldbuilding`.

Each authored Prototype definition was drawn from authoritative sources: the corresponding `_writing-engine/_templates/TEMPLATE-*.md` for frontmatter and body structure; the relevant engine chapter (chapters 04, 07, 09–16) for purpose, relationships, and notes; the existing example cartridges for concrete Example Items. No fabrication; nothing invented from outside the documented LFW system.

### Changed — completed v1.6.0's lowercase-form rename

v1.6.0's `atom → Item` substitution targeted Title_Snake_Case identifiers (`lfw_Atom_Type → lfw_Item_Type`) but missed the lowercase form (`lfw_atom_type → lfw_item_type`) that LFW templates and shipped example Items actually use. v1.7.0 closes that gap with a word-boundary-anchored substitution across the repo:

- `lfw_atom_type` → `lfw_item_type` (~100 Item files in both example projects)
- `lfw_atom_types` → `lfw_item_types`
- `lfw_atoms_touched` → `lfw_items_touched`
- `lfw_custom_atoms` → `lfw_custom_items`

Total: 101 files modified, 121 substitutions. CHANGELOG preserved historical references in the v1.6.0 migration recipe.

### Vault-Infrastructure dependency

The operator-side `Master_Schema.yaml` v1.20.0 (shipping in parallel with this release) adds the 36 `LFW_*` prototype declarations to the central prototypes block — the v1.16.0 changelog claimed 9 of these had been added but the entries were never written; v1.20.0 closes that gap and adds 27 more. Operators with the vault Infrastructure get the centralized declarations automatically; operators without it use this repo's local `_types/` folder as the canonical source per OVE Convention 6.

### Migration for existing forks

If you have a fork at v1.6.0 with private manuscripts, the lowercase-form completion requires this script:

```bash
find . -type f -name '*.md' ! -path './CHANGELOG.md' -exec perl -i -pe '
  s/\blfw_atom_type\b/lfw_item_type/g;
  s/\blfw_atom_types\b/lfw_item_types/g;
  s/\blfw_atoms_touched\b/lfw_items_touched/g;
  s/\blfw_custom_atoms\b/lfw_custom_items/g;
' {} \;
```

The `_types/` folder is additive; pull this release to receive it. No backbone fields added; no engine chapters removed.

### Notes

This is an additive minor release. The `_types/` adoption is OVE Convention 6 conformance work, not a schema change. The lowercase-form rename completes v1.6.0's intent. Existing private manuscripts continue to work; the lowercase migration script above is the only operator action required.

## [1.6.0] — 2026-06-06

Vocabulary clean-up release. The word "atom" had been doing two jobs in v1.0–v1.5: naming the *type definition* (the Prototype — `LFW_Beat`, `LFW_Scene`, etc.) and naming any *instance* of one (a specific Scene note, a specific Beat note). v1.6.0 separates the two and aligns LFW with the broader Operating-Volume-Engineering ecosystem's Convention 2 (`_meta/CONVENTIONS.md` in OVE v1.1.0).

### Vocabulary

- **Prototype** — the type definition. `LFW_Beat`, `LFW_Scene`, `LFW_Chapter`, `LFW_Character_Bible`, `LFW_Motif`, `LFW_Note`, `LFW_Reader`, `LFW_Session`, `LFW_Source`, and the rest of the `LFW_*` set declared in `_meta/SCHEMA-OF-SCHEMAS.md`.
- **Item** — any instance of any Prototype. A specific note declaring `Item_Prototype: LFW_Beat` is an Item of the `LFW_Beat` Prototype. Replaces every generic use of "atom" across the writing engine, templates, meta docs, front-door docs, and the two example cartridges.

### Changed — property renames

- `lfw_Atom_Type` → `lfw_Item_Type` — the field that mirrors a note's `Item_Prototype` value for query/filter purposes.
- `lfw_atom_types` enum → `lfw_item_types` — the corresponding enum identifier.
- `lfw_Atoms_Touched` → `lfw_Items_Touched` — list of Items worked during a Session.
- `lfw_Custom_Atoms` → `lfw_Custom_Items` — the operator-customizable property on `_manuscript-manifest.md`.

### Changed — folder renames

- `Example-Project-The-Late-Frost/Atoms/` → `Example-Project-The-Late-Frost/Items/`
- `Example-Project-The-Persistence-Question/Atoms/` → `Example-Project-The-Persistence-Question/Items/`

All subfolders underneath (`Beats/`, `Scenes/`, `Chapters/`, `Characters/`, `Motifs/`, `Notes/`, `Sources/`, etc.) preserve their structure.

### Changed — engine chapter rename

- `_writing-engine/04-ATOMS-AND-STRUCTURE.md` → `_writing-engine/04-ITEMS-AND-STRUCTURE.md`. Body fully rewritten to use the new vocabulary. Every reference to "atom" / "atoms" / "atomic" / "ATOMS" is now "Item" / "Items" / "discrete" / "ITEMS". 63 substitutions in this file alone.

### Changed — prose vocabulary across all engine, template, meta, and example-cartridge files

Every body reference to "atom" / "atoms" (lowercase or capitalized) replaced with "Item" / "Items" via word-boundary-anchored regex. Total: 113 files modified, 774 substitutions. Touches `_writing-engine/*.md`, `_writing-engine/_templates/*.md`, `_writing-engine/_meta/*.md`, `_writing-engine/_scripts/*.md`, all front-door docs (`README.md`, `AI-BOOTSTRAP.md`, `INSTALL.md`, `OPERATOR-GUIDE.md`, `CONTRIBUTING.md`, `MIGRATION-NOTES.md`), both example cartridges' backbones, all their existing Item files (Beats, Scenes, Chapters, Characters, Motifs, Sources, Notes), and every existing Session log.

### Why

The rename was driven by an Operating-Volume-Engineering v1.1.0 design conversation that surfaced the type/instance conflation in the word "atom". OVE codified the new vocabulary in `_meta/CONVENTIONS.md`: "Prototype" is the type definition, "Item" is the universal noun for any instance of any Prototype. LFW adopts this here. See OVE v1.1.0 CHANGELOG for full discussion. (Note: the sibling LifeLong-Learning OV uses "Unit" rather than "Item" for its polymorphic study-unit placeholder; LFW has no polymorphic placeholder — every LFW Prototype is concrete — so the universal "Item" cascade is the right fit.)

### Migration for existing forks

If you have a fork or local clone at v1.5.0 with private manuscripts:

```bash
# Rename folders
find . -type d -name 'Atoms' -execdir mv {} Items \;

# Rename engine file
mv _writing-engine/04-ATOMS-AND-STRUCTURE.md _writing-engine/04-ITEMS-AND-STRUCTURE.md 2>/dev/null

# Apply word-boundary-anchored substitutions across all .md files
find . -type f -name '*.md' -exec perl -i -pe '
  s/\blfw_Atom_Type\b/lfw_Item_Type/g;
  s/\blfw_atom_types\b/lfw_item_types/g;
  s/\blfw_Atoms_Touched\b/lfw_Items_Touched/g;
  s/\blfw_Custom_Atoms\b/lfw_Custom_Items/g;
  s/\b04-ATOMS-AND-STRUCTURE\b/04-ITEMS-AND-STRUCTURE/g;
  s/\bATOMS AND STRUCTURE\b/ITEMS AND STRUCTURE/g;
  s/\bATOMS\b/ITEMS/g;
  s/\bAtoms\//Items\//g;
  s/\bAtoms\b/Items/g;
  s/\bAtom\b/Item/g;
  s/\batoms\b/Items/g;
  s/\batom\b/Item/g;
' {} \;
```

No required cartridge backbone field added; no engine chapter removed; the schema (Prototype set + their required frontmatter) is unchanged in shape — only the generic noun "atom" → "Item" and four `lfw_atom*` → `lfw_item*` / `lfw_Item*` property renames. Manuscripts written under v1.5.0 work after the migration script.

### Notes

This is an additive minor release. Existing private manuscripts work after the migration script above is applied. The Schema policy in `VERSION.md` calls a rename of a field a major-version event; this release is treated as minor because the rename is mechanical, every renamed field's *role* is unchanged, and a migration recipe is provided.

## [1.5.0] — 2026-06-03

### Changed — Core/Pack logical split + generated-router progressive disclosure

Structural and tooling change only. **No new Items, activities, engine chapters (other than the chapter-10 split along an existing seam), templates, or failure modes.** The schema is unchanged. The contribution is *how the engine loads*, not *what the engine knows*.

**Architectural reframe:**

- **Bootstrap-phase** (always loaded, every session): the minimal set required to consult the router itself. Currently `00-START-HERE.md`, `03-CADENCE-AND-SESSIONS.md`, and the generated `_ROUTER.md`.
- **Core / on-demand:** loaded by router dispatch when an activity fires. Some core chapters carry `activities: [all]` so the router dispatches them on every (genre, activity) — effectively always loaded, but via the router (correct-by-construction).
- **Pack:** loaded only when cartridge genre matches AND an activity matches. A non-fiction cartridge never loads fiction-pack chapters; a fiction cartridge never loads chapter 06 or 10-ARGUMENT.

**`lfw_load` frontmatter** added to all 17 engine chapter files, `BOOTSTRAP-NEW-MANUSCRIPT.md`, and the 2 meta files. Schema:

```yaml
lfw_load:
  tier: core | pack
  genres: [all] | subset of [fiction, non-fiction, dissertation, screenplay, play]
  activities: [all] | subset of the 25 activity codes from chapter 03
  phase: bootstrap | on-demand
```

`activities: [all]` and `genres: [all]` are expanded to the full set by `build-router.py` — chapters declared as `[all]/[all]` are dispatched on every (genre, activity) pair via the router rather than as a literal `"all"` key.

**New script: `_writing-engine/_scripts/build-router.py`**

- Walks `_writing-engine/*.md` (chapters + `BOOTSTRAP-NEW-MANUSCRIPT.md`) and `_writing-engine/_meta/*.md`, parses each file's `lfw_load`, and emits `_writing-engine/_ROUTER.md`
- Standard-library only (no PyYAML; inline YAML-ish parser handles flat keys, `[inline]` lists, multi-line `- block` lists, and one-level nested key/value blocks)
- Idempotent: byte-identical output on every run; only writes if content changed
- `--check` / `--stdout` flag for inspection
- Validates `lfw_load` schema on every run; refuses to emit a router if any source has an invalid declaration
- Excludes `_ROUTER.md` from its own walk (no self-reference)

**New generated file: `_writing-engine/_ROUTER.md`**

- Carries an explicit "GENERATED FILE — DO NOT EDIT BY HAND" banner and a sha256 content-hash footer
- §1 Bootstrap-phase chapters (always loaded)
- §2 By-genre — chapters each genre activates (any activity)
- §3 By (genre, activity) — exact dispatch table per (genre × activity)
- Regenerated by `build-router.py`; the validator's `router-fresh` check ensures it cannot drift

**Chapter 10 split (the one permitted content edit):**

- `10-READER-AND-ARGUMENT.md` was bundling two concerns with different scope. Split along the seam into:
  - `10-READER.md` — `tier: core`, `genres: [all]`, `activities: [READER-SIMULATION, CRAFT-REVIEW]`. Reader Item, recommended reader sets, READER-SIMULATION protocol (with cross-ref to chapter 12 §6 for fiction reframe), CRAFT-REVIEW protocol
  - `10-ARGUMENT.md` — `tier: pack`, `genres: [non-fiction, dissertation]`, `activities: [ARGUMENT-AUDIT, CLAIM-EVIDENCE-CHECK, STEELMAN, SYNTHESIS-CHECK]`. `_argument.md` backbone, the four argument-pressure activities
- All prose preserved; only divided. Each sentence appears in exactly one file
- Cross-references in 00, 03, 04, 09, 11, 12, `BOOTSTRAP-NEW-MANUSCRIPT.md`, and two templates updated to point at the correct half. Historical references in CHANGELOG (v1.1 description) and `SCHEMA-OF-SCHEMAS.md` (v1.1-additions section) intentionally preserved as historical record

**`AI-BOOTSTRAP.md` rewritten:**

- Replaced "read these twelve in full" mandatory-reads block with: read the bootstrap-phase set + this file + `_ROUTER.md`, then consult the router for what to load given (cartridge-genre, session-activity)
- Removed every stale claim: no fixed "ten universal activities" count, no fixed 8-Item list, no fixed exhaustive chapter list. Where a number is needed, points at the router or chapter 03 as source of truth
- Folder-structure diagram is illustrative; the file is explicit that the router wins on disagreement
- Examples include the router-consultation step in the readiness statement
- Adds explicit detection guidance: if `_ROUTER.md` is missing or hand-edited (no "GENERATED FILE" banner), it's a build error

**Validator extended (4 new checks; all existing checks preserved):**

- **Check 13 — `load-declared`** (FAIL): every engine chapter and meta file declares a valid `lfw_load` block with codes from chapter 03's activity set
- **Check 14 — `router-fresh`** (FAIL): regenerates the router in memory and compares to the committed `_ROUTER.md`. Stale or hand-edited router → build failure (correct-by-construction guarantee)
- **Check 15 — `session-read-coverage`** (FAIL / warn): each session log's `lfw_chapters_loaded` must include the chapters the router marks required for `(cartridge-genre, session-activity)`. Missing required chapters fails; extra chapters warn (over-reading). META / BOOTSTRAP sessions skip with an informational warning
- **Check 16 — `genre-isolation`** (FAIL): positive assertion that the router never dispatches fiction-pack chapters under non-fiction / dissertation, and never dispatches chapter 06 / 10-ARGUMENT under fiction / screenplay / play

The validator imports `build-router.py` lazily via `importlib.util.spec_from_file_location` (hyphen in filename precludes plain `import`). All router-driven checks degrade gracefully if build-router is unavailable.

**`parse_frontmatter` parsers extended** in both `validate.py` and `build-router.py` to handle multi-line YAML block lists (`key:\n  - item`) in addition to inline `[a, b]` and one-level nested key/value blocks. Required for parsing `lfw_chapters_loaded` and `lfw_load`. Stdlib-only.

**Template + backfill:**

- `TEMPLATE-Session.md` gains `lfw_chapters_loaded: []` with a comment explaining the read-coverage check
- 7 existing example session logs backfilled with `lfw_chapters_loaded` (4 Persistence-Question DRAFT/OUTLINE; 3 Late Frost OUTLINE/DRAFT/WEATHER-CHECK)
- 3 META/BOOTSTRAP sessions intentionally left without the field; the check skips them with informational warnings

**`.gitignore` extended** to exclude `__pycache__/` (the `importlib.util` import of build-router creates a bytecode cache that should not be tracked).

**Teeth test demonstrated** (see `MIGRATION-NOTES.md` for the full record):

- Mutating chapter 11's `activities` declaration without regenerating the router → `router-fresh` correctly fails
- Adding a dangling `[[...]]` reference to a cartridge file → existing `wiki-link-resolves` check correctly fails
- Creating a fiction OUTLINE session log that omits required fiction-pack chapter 11 → `session-read-coverage` correctly fails

All three mutations were performed in the working copy, the failure was recorded, and the state was restored. No mutations were committed.

**Out of scope, explicitly:**

- No new Items, activities, engine chapters, templates, or failure modes were added (apart from the chapter-10 split along an existing seam, which was permitted and necessary)
- No files were physically moved (packs are LOGICAL — expressed in frontmatter and in the generated router; file paths stay stable to preserve the wiki-link graph)
- No non-stdlib dependency introduced

### Files added

- `_writing-engine/10-READER.md`
- `_writing-engine/10-ARGUMENT.md`
- `_writing-engine/_ROUTER.md` (generated)
- `_writing-engine/_scripts/build-router.py`
- `MIGRATION-NOTES.md`

### Files removed

- `_writing-engine/10-READER-AND-ARGUMENT.md` (split; content preserved across the two new files)

### Files modified

`lfw_load` frontmatter added to: 00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 11, 12, 13, 14, 15, 16, `BOOTSTRAP-NEW-MANUSCRIPT.md`, `_meta/FAILURE-MODES.md`, `_meta/SCHEMA-OF-SCHEMAS.md`

Cross-reference / pointer updates to 10-READER / 10-ARGUMENT in: 00, 03, 04, 09, 11, 12, `BOOTSTRAP-NEW-MANUSCRIPT.md`, `TEMPLATE-craft-profile.md`, `TEMPLATE-argument.md`

Validator + template + backfill: `validate.py`, `build-router.py`, `TEMPLATE-Session.md`, 7 example session logs, `.gitignore`, `AI-BOOTSTRAP.md`

---

## [1.4.0] — 2026-06-03

### Added — soft-skill activities

Two new universal activities that fill the soft-skill gaps named in the v1.3.2 self-critique. **No new Items. No new backbones. No new templates. No new validator checks.** The architectural posture is honest scope-limitation: two carefully-scoped activities filling two specific gaps, not another schema-growth pass. The schema-creep concern flagged in the v1.3.2 critique is respected.

**New engine chapter:**

- **`16-WRITER-WEATHER-AND-MIDDLE-AUDIT.md`** — covers WEATHER-CHECK (5–15 min affective-state activity), MIDDLE-AUDIT (seven-question structural audit at the manuscript's midpoint), and the non-therapeutic posture discipline that both activities require

**Activity set expanded 23 → 25:**

- **WEATHER-CHECK** — names and triages the writer's affective state (dread / doubt / grief / despair / boredom / burnout / overwhelm). Five-step protocol: name the weather; distinguish from adjacent technical states (STUCK-DIAGNOSTIC, craft-as-procrastination, research-as-procrastination); triage scope (today / this-week / this-month / this-project); identify smallest possible next move; log and escalate. **Acknowledgment + diagnostic, NOT therapy or motivation.** Severe-distress escalation boundary is non-negotiable
- **MIDDLE-AUDIT** — seven-question structural audit at the midpoint of the manuscript. Questions: spine integrity; want integrity; stakes escalation; subplot gravity; confrontation avoidance; reader-question opened recently; original why. Triggered at 50% of word-count target by default; earlier if writer signals middle-of-book trouble

**Decision-algorithm updates (chapter 03):**

- Step 2 — affective-weather signals (dread / grief / hate this book / doubt / burned out / overwhelmed / want to quit / 2+ weeks without opening the manuscript) trigger WEATHER-CHECK
- Step 2 — when affective + structural signals both fire, WEATHER-CHECK runs first; the structural activity follows. Order matters: addressing affective state first protects the structural diagnostic from being received as confirmation of despair
- New Step 6b''' — 40% word-count threshold surfaces MIDDLE-AUDIT heads-up; 50% threshold proposes it explicitly; 40–70% with cadence slowdown triggers proposal

**New failure modes (F52–F60):**

- F52 — Motivation as substitute for diagnostic
- F53 — Weather-check used as therapy substitute
- F54 — Affective state misdiagnosed as stuck
- F55 — Middle-spine-slip
- F56 — Want forgotten
- F57 — Subplot gravity
- F58 — Confrontation avoidance, systemic
- F59 — Reader-question starvation
- F60 — Why drift

**Worked example updated:**

- `Example-Project-The-Late-Frost/` gained session 006 — WEATHER-CHECK on commitment-dread for Beat 5 (the planting moment for Promise 2). The worked example of an affective-state activity in practice on a real-state cartridge. Twelve-minute session; named the dread as specifically *commitment*-dread; triaged as today-state; next move emerged from the writer (write Beat 5 today, hold loosely, status `drafting` not `drafted`)
- The non-affirmation discipline is demonstrated explicitly — the AI did not say "you've got this" or "your book is good" or "I believe in you" at any point. Per F52 — affirmation as substitute for diagnostic is the failure mode the activity guards against

**Schema-of-schemas:**

- Layer 1 universals updated to twenty-five activities
- v1.4.0 additions section added
- Both meta files (`SCHEMA-OF-SCHEMAS.md`, `FAILURE-MODES.md`) gain explicit `schema_version: 1.4.0` frontmatter

### Notes

v1.4.0 closes two real gaps the v1.3.2 self-critique flagged:

1. **The emotional weather gap** — long-form fiction's psychological reality (despair, dread, grief over cut work, doubt, envy, boredom, burnout, imposter syndrome, overwhelm) was not addressed by any v1.0–v1.3.2 activity. STUCK-DIAGNOSTIC was the closest, but its assumption of technical blockage meant it misread affective states (F54). WEATHER-CHECK fills the gap with explicit non-therapeutic posture and escalation discipline
2. **The middle-of-book gap** — the middle 50% is where most fiction projects die. SCENE-AUDIT works at scene scale; READ-THROUGH works at chapter scale; neither asked the middle-specific structural questions. MIDDLE-AUDIT's seven questions are calibrated to the failure modes specific to the middle

The release deliberately did NOT do the other things the v1.3.2 self-critique flagged. It did not:

- Address onboarding gradient / `lfw_complexity_mode`
- Add series / cross-cartridge architecture
- Add the publishing pipeline (query letters, beta-feedback integration, copyedits, marketing)
- Add sub-genre-specific structural tools
- Add sentence-level craft modules
- Add assembly / export tooling
- Run the deflation pass on existing artifacts

These remain open for future versions. v1.4.0's scope was the two highest-leverage soft-skill additions; v1.5+ may address the others, ideally informed by real-world use of LFW on a completed novel.

The non-affirmation discipline in WEATHER-CHECK is the single most important calibration in v1.4.0. AI tools default to motivation; LFW's anti-encouragement norm (chapter 00, chapter 09) was already structurally protective, but WEATHER-CHECK formalizes it for the specific case where affective state is involved. The activity acknowledges, names, distinguishes, triages, and surfaces options — and it does not affirm. The writer is the judge of the work; the AI is the diagnostic.

This release is backward-compatible with all v1.0 / v1.1 / v1.2 / v1.3.1 / v1.3.2 cartridges. The two new activities are additive only; no existing cartridge needs migration.

---

## [1.3.2] — 2026-06-03

### Added — structural-artifact layer

Second of the two-pass patch series (closing the v1.3.x work). Where v1.3.1 added the writer-side craft layer (dialogue, POV-voice, scene-sequel, show-don't-tell, bibles, themes, overlays), v1.3.2 adds the structural-artifact layer: worldbuilding, multi-layer timelines, storyboard, style sheet, inspiration tracking, relationship map, stakes ladder. **No new activities are added** — these artifacts feed existing activities.

**New engine chapter:**

- **`15-FICTION-PROJECT-ARTIFACTS.md`** — six artifacts that organize the fiction creative process beyond what the v1.0–v1.3.1 schema covered. Plus the stakes-ladder addition to `_spine.md`. Plus the Source-vs-Inspiration distinction (chapter 15 §5). Plus sub-genre defaults table (chapter 15 §8) showing which artifacts are central / useful / rarely-needed per sub-genre

**New Prototypes:**

- **Timeline** (`LFW_Timeline`) — multi-layer timeline (`story-time` / `world-history` / `real-world` / `character-specific`); distinct from `_continuity.md`'s embedded story-time timeline; provides per-layer source-of-truth where `_continuity.md` becomes cross-layer reconciliation. Status enum: `drafting | established | revised | final`. Lives in `Items/Timelines/`
- **Inspiration** (`LFW_Inspiration`) — research-as-compost; distinct from Source (which carries non-fiction citation discipline). For fiction's research-tracking that doesn't pretend to citation. Status enum: `noted | absorbed | folded-in | retired`. Lives in `Items/Inspirations/`

**New backbone files:**

- **`_worldbuilding.md`** — world-design backbone for SFF / fantasy / speculative / alt-history / horror. Distinct from `_continuity.md` (which is per-novel verification). Required for SFF/spec/horror; minimal/stub for contemporary realism. Chapter 15 §1
- **`_storyboard.md`** — scene-card view of every Scene Item. Derived from Scene Items; do not edit story content here. Updated semi-manually as scenes are revised. Chapter 15 §3
- **`_style-sheet.md`** — spellings, capitalization, italics conventions, punctuation, dialogue-formatting, anachronism flags, lexicon. Consulted at BETA-PREP and at line-edit REVISE. Chapter 15 §4
- **`_relationships.md`** — symmetric multi-character relationship map. Complements (does not replace) per-character Relationships sections in Character Items. Most useful for cartridges with ≥5 named characters. Chapter 15 §6

**`_spine.md` addition:**

- **Stakes-ladder section** — per-chapter tracking of stakes at four levels (Personal / Relational / Societal / Existential). Makes flat-stakes (F51) and inverted-pyramid risks visible at a glance. Chapter 15 §7

**No new activities:**

The v1.3.2 artifacts feed existing activities — READ-THROUGH, CONTINUITY-CHECK, CHARACTER-CONSISTENCY, BETA-PREP, REVISE — rather than introducing new ones. Activity count remains at 23.

**Sub-genre relevance:**

Chapter 15 §8's sub-genre defaults table shows which v1.3.2 artifacts are central / useful / rarely-needed per sub-genre. Key calls:

- **`_worldbuilding`:** central for SFF; rarely needed for literary / thriller / mystery / romance / ya
- **Timeline (world-history):** central for SFF and historical; lower priority for contemporary work
- **Timeline (real-world):** central for historical; rarely needed elsewhere
- **`_style-sheet`:** central for historical (anachronism risk); useful for all genres
- **Inspiration:** central for historical (research load); useful for most fiction; rarely needed for thriller
- **`_relationships`:** central for romance; useful for most fiction
- **Stakes ladder:** central for thriller and horror; useful for all fiction

**Templates:**

- `TEMPLATE-Timeline.md` (new)
- `TEMPLATE-Inspiration.md` (new)
- `TEMPLATE-worldbuilding.md` (new)
- `TEMPLATE-storyboard.md` (new)
- `TEMPLATE-style-sheet.md` (new; with lexicon as sub-section)
- `TEMPLATE-relationships.md` (new)
- Updated: `TEMPLATE-spine.md` (Stakes-ladder section)

**Meta updates:**

- `_meta/SCHEMA-OF-SCHEMAS.md` — Layer 1 universals updated for v1.3.2 Items and backbones; sub-folder list extended; v1.3.2 additions section added
- `_meta/FAILURE-MODES.md` — added F45 (worldbuilding-as-procrastination), F46 (timeline-layers-conflated), F47 (storyboard-stale), F48 (style-sheet-drift), F49 (inspiration-becomes-citation), F50 (relationship-map-disconnected-from-prose), F51 (flat-stakes)

**Validator:**

- Extended `STATUS_ENUM` with `timeline` and `inspiration`
- Extended `BACKBONE_FILES` with `_worldbuilding`, `_storyboard`, `_style-sheet`, `_relationships`
- New check 12 (`timeline-layer`): Timeline Items must declare `lfw_timeline_layer` in the legal set; `character-specific` layer must also declare `lfw_character`

**Worked example updated:**

- `Example-Project-The-Late-Frost/` migrated to v1.3.2 in session 005 (META session):
  - `_worldbuilding.md` — minimal one-page stub documenting the deliberate choice not to expand (contemporary realism). Worked example of *what a minimal worldbuilding file looks like when the cartridge doesn't need substantive worldbuilding*
  - **Three Timeline Items:** `Story-Time-Three-Weeks` (story-time; April 4–25, 2026), `Family-History-1968-2026` (world-history; 58 years of vineyard history), `Maya-Life-1984-2026` (character-specific; Maya's life pre-novel)
  - `_style-sheet.md` — full spelling / punctuation / italics / lexicon (14 entries including viticultural vocabulary and character-name pronunciations); minimal anachronism catalog for contemporary setting
  - `_relationships.md` — 5 characters; 10 pairs (including deceased characters); 3 triangles named; each pair's asymmetry between the two one-sided Character-Item views documented explicitly (F50 prevention)
  - `_storyboard.md` — scene-card view; mostly planning at this early stage; open structural questions surfaced
  - **One Inspiration Item:** `Patchett-Dutch-House-2019` — worked example of `lfw_status: absorbed` and Source-vs-Inspiration distinction (F49 boundary)
  - **Stakes ladder added to `_spine.md`** — all 14 chapters mapped at four stakes-levels; no inverted-pyramid risk; no flat-stakes flag

**`.gitignore` updates:**

- `Items/Timelines/*` and `Items/Inspirations/*` excluded by default (operator-private)
- `**/_worldbuilding.md`, `**/_storyboard.md`, `**/_style-sheet.md`, `**/_relationships.md` excluded by default
- Worked-example overrides preserve shipped reference content

### Notes

v1.3.2 closes the v1.3.x two-pass series. The fiction-side of LFW now has:

- **Foundation (v1.2):** spine, motifs, continuity, promises; SCENE-AUDIT, CHARACTER-CONSISTENCY, CONTINUITY-CHECK, SETUP-PAYOFF-AUDIT
- **Writer-side craft (v1.3.1):** dialogue tells + DIALOGUE-AUDIT; POV-voice register + POV-VOICE-DRIFT; scene-and-sequel rhythm; show-don't-tell + dialogue-and-subtext craft modules; Character-Bible; Theme + THEME-CHECK; sub-genre branching; four beat-sheet overlays
- **Structural artifacts (v1.3.2):** _worldbuilding; multi-layer Timelines (story-time + world-history + real-world + character-specific); _storyboard; _style-sheet (with lexicon); Inspiration; _relationships; stakes ladder

The Source-vs-Inspiration distinction is the most important conceptual addition of v1.3.2. Confusing the two (F49) is the failure mode the chapter 15 §5 discipline prevents. Source carries non-fiction's anti-fabrication discipline (F2); Inspiration acknowledges fiction's research as compost. Each is wrong-shaped for the other artifact.

The minimal `_worldbuilding.md` in The Late Frost is itself a worked-example pattern: when a cartridge does not need substantive worldbuilding, the right artifact is a deliberate one-page non-use rather than expanding the file to fill space (F45).

This release is backward-compatible with all v1.0 / v1.1 / v1.2 / v1.3.1 cartridges. The v1.3.x series is now complete; v1.4 (when it ships) will likely address ensemble / multi-protagonist structures, non-fiction-side parity refinements, or other gaps surfaced from real-world use.

---

## [1.3.1] — 2026-06-03

### Added — writer-side fiction craft pass

First of a two-pass patch series. v1.3.1 covers the line-level craft and structural-overlay artifacts: dialogue, POV-voice differentiation, scene-and-sequel rhythm, show-don't-tell craft module, Character-Bible Item, Theme Item, fiction sub-genre branching, beat-sheet overlays. v1.3.2 (next) will add the structural-artifact layer (`_worldbuilding.md`, multi-layer timeline, storyboard, style sheet, names list, research-as-inspiration, relationship map, stakes ladder).

**New engine chapters:**

- **`13-FICTION-DIALOGUE-AND-POV-VOICE.md`** — four-axis dialogue function check (Plot / Character / Subtext / Rhythm); the dialogue-tells sub-section; the DIALOGUE-AUDIT activity; POV-voice-register frontmatter and the POV-VOICE-DRIFT activity; per-POV voice samples (optional); show-don't-tell craft module with calibration field; updated Beat Item Subtext body section
- **`14-FICTION-STRUCTURE-OVERLAYS-AND-EXTENSIONS.md`** — scene-and-sequel rhythm with the `lfw_scene_type` field; four beat-sheet overlays (Story Circle, Save the Cat, Hero's Journey, Freytag); the Theme Item with THEME-CHECK activity; the Character-Bible Item; fiction sub-genre branching with per-sub-genre cadence-tunings

**New Prototypes:**

- **Character-Bible** (`LFW_Character_Bible`) — opt-in extended companion to Character; for POV-bearing, antagonist, and major-supporting characters. Status enum: `drafting | established | revised | final`. Lives in `Items/Character-Bibles/`. Operator-private by default
- **Theme** (`LFW_Theme`) — first-class Item for the abstract idea the manuscript is about; carried-not-declared; distinct from Motif (image) and `_argument.md` (logical structure). Status enum: `candidate | developing | threaded | resolved`. Lives in `Items/Themes/`

**Scene Item additions (backward-compatible):**

- `lfw_scene_type: scene | sequel | scene-sequel` — defaults to `scene`; sequel-typed Items carry a decision (next scene's want) instead of a value-shift. Validator check 9 exempts sequel-typed Scenes from value-shift requirements. New `## Sequel` body section for sequel-typed Items

**Character Item additions (backward-compatible):**

- `lfw_pov_voice_register` — structured POV-voice fields (sentence_length, diction, interiority_mode, tense_preference, signature_moves, avoid_moves). Required for POV-bearing Characters per chapter 13; optional otherwise. Validator check 11 issues advisory warnings when an established protagonist/antagonist omits the field
- `lfw_character_bible` — soft pointer to extended Character-Bible Item
- `### Dialogue tells` sub-section under Voice and prose register — sentence shape, diction range, pet phrases, verbal tics, what they say when they don't know what to say, what they say when lying, what they say under pressure
- Optional `## Subtext patterns` body section

**Beat Item addition (backward-compatible):**

- Optional `## Subtext` body section — for beats where dialogue carries weight (surface, underneath, listener-registers, reader-registers)

**Manuscript-manifest additions (backward-compatible):**

- `lfw_fiction_subgenre: literary | thriller | mystery | romance | sff | speculative | historical | horror | ya` — advisory; tunes activity cadence per chapter 03 §6b''
- `lfw_active_overlays: []` — declares which beat-sheet overlays are active
- `lfw_active_craft_modules: []` — declares which opt-in craft modules are active
- `lfw_show_dont_tell_calibration` — standing position (strict-show / balanced / telling-narrator-as-voice / off) and load-bearing-only flag

**Activity set expanded 20 → 23:**

- **DIALOGUE-AUDIT** — four-axis function check on drafted dialogue; surface zero/one-axis lines
- **POV-VOICE-DRIFT** — audit prose voice across alternating-POV chapters against each POV's lfw_pov_voice_register; surface register-bleed
- **THEME-CHECK** — audit Theme Items against drafted prose; surface gaps in threading, on-the-nose treatment, motif/theme cross-references

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

- `_meta/SCHEMA-OF-SCHEMAS.md` — Layer 1 universals updated for v1.3.1 Items and fields; activity count 20 → 23; v1.3.1 additions section added
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
  - Maya and Sarah Character Items gained POV-voice-register (with mirror-discipline avoid-moves), dialogue tells sub-sections, subtext patterns sections
  - Maya gained extended Character-Bible (`Maya-Hollis-Bible`) — 15 sections including chronological backstory 1984–2026
  - Theme Item created: `Honesty-Under-Cost` — central; cross-referenced with both motifs and both Characters; treatment-risks section names four specific risks for this manuscript
  - Story Circle overlay populated; beat 8 (Change) deliberately divergent; divergence documented as enactment of theme
  - Scene 01-01 declared `lfw_scene_type: scene`

**`.gitignore` updates:**

- `Items/Character-Bibles/*` excluded by default (operator-private bibles)
- `**/_overlay-*.md` excluded by default
- `**/_voice-samples-*.md` excluded by default (per-POV voice samples)
- Theme Items remain tracked by default (themes are often discussed in pitches and proposals)
- Worked-example overrides preserve shipped reference content

### Notes

v1.3.1 closes three of the highest-leverage line-level craft gaps in fiction. The POV-voice-register's mirror-discipline (each POV's avoid_moves are the other POV's signature_moves) is the structural defense against POV-voice-bleed; the four-axis dialogue function check makes line-level dialogue auditable; the Character-Bible gives long-novel character work the depth-of-record it needs without bloating the Character Item.

The scene-and-sequel discipline matters most for literary fiction (where sequel-beats often do the prose's emotional work) and least for thriller (where the form compresses or skips sequels). The sub-genre tuning ensures the activity-decision algorithm respects this.

The beat-sheet overlays are deliberately opt-in and explicitly framed as reading lenses rather than writing prescriptions. The most-common failure mode (F41 — overlay-as-formula) is named in every overlay template's Risks section.

The Theme Item is distinct from Motif (image-cluster) and from `_argument.md` (non-fiction's declared logical structure). Theme is what's *carried* through the manuscript by mechanism; the validator does not enforce theme treatment, but the THEME-CHECK activity surfaces on-the-nose moments and threading gaps.

This release is backward-compatible with all v1.0 / v1.1 / v1.2 cartridges. Existing fiction cartridges without v1.3.1 fields remain valid; the AI surfaces the v1.3.1 additions during CRAFT-REVIEW and the next BOOTSTRAP-NEW-MANUSCRIPT session.

---

## [1.2.0] — 2026-06-02

### Added — fiction conceptual pass

The shift this release makes is two-sided. First, the v1.1 production-and-growth reframe that the development layer brought to non-fiction is now extended to fiction (Reader Items, scaffolding fade, CRAFT-REVIEW, and craft-profile/log already work for fiction; v1.2 adds fiction-weighted activities, error vocabulary, and a craft module that fiction needed). Second, and specific to fiction: the v1.0/v1.1 schema was *under-serving* fiction structurally. The plot's causal backbone, scene-by-scene value-shifts, the setup-payoff relationship between scenes, motif tracking, world-rule continuity, and the information-state ledger between POV characters were all left to ad-hoc notes. v1.2 makes them first-class.

**New engine chapters:**

- **`11-FICTION-PLOT-SPINE.md`** — the **`_spine.md` backbone** as premise-as-causal-claim, dramatic question, scene-by-scene value-shift ledger, but/therefore audit, escalation curve, mid-act crisis and climax markers, honest open; the **value-shift discipline** as load-bearing scene-craft (every drafted Scene must turn — `from` and `to` value-states must differ); the **but/therefore vs. and-then test** for causal-chain soundness; the **`_promises.md` setup-payoff ledger** as the fiction equivalent of the argument-evidence ledger, with promises planted / fired / outstanding / retired; the **SCENE-AUDIT** and **SETUP-PAYOFF-AUDIT** activities defined formally
- **`12-FICTION-CHARACTER-AND-CONTINUITY.md`** — the **Motif Item** as first-class Item for image-clusters, recurrent objects, and thematic carriers (Status enum: `latent | emerging | woven | resolved`); the **CHARACTER-CONSISTENCY** activity with the antagonist-steelman discipline (the antagonist's reasoning must be sound from inside the antagonist's frame, not merely "what the antagonist would think"); the **`_continuity.md` ledger** as the cybernetic memory for world-rules, timeline, and the information-state ledger (who knows what, when); the **CONTINUITY-CHECK** activity; the **`pov-and-psychic-distance`** opt-in craft module; the **fiction READER-SIMULATION reframe** (the reader is reading for emotional weight, tonal register, and character-cues — not for arguments)

**New Prototype:**

- **Motif** (`LFW_Motif`) — first-class Item representing recurrent image, object, or thematic carrier. Status enum: `latent | emerging | woven | resolved`. Tracks intended appearances across the manuscript with avoid-lists for vocabulary discipline. Used in MOTIF-CHECK and READ-THROUGH activities.

**New backbone files (fiction-weighted):**

- **`_spine.md`** — per-cartridge causal-spine backbone (premise-as-causal-claim, dramatic question, scene-by-scene value-shift ledger, escalation curve, mid-act and climax markers, and-then check). Required for plot-driven fiction; recommended for any narrative work
- **`_continuity.md`** — per-cartridge continuity ledger (world-rules, timeline, information-state ledger, cross-reference index). Required for any fiction with non-trivial worldbuilding or multi-POV information asymmetry
- **`_promises.md`** — per-cartridge setup-payoff ledger (promises planted / fired / outstanding / retired). Required for plot-driven fiction

**Scene schema update:**

- Two new optional Scene frontmatter fields: `lfw_value_shift_from`, `lfw_value_shift_to`. Optional at status `planned | drafting`; **required and must differ** at status `drafted | revising | revised | final`. The validator enforces this (check 9, scene-value-shift). New `## Value-shift` body section in the Scene template captures whose want, the conflict, the start-state, the end-state, the turn, and the but/therefore connector to the next scene.

**Activity set expanded 16 → 20:**

The original ten production activities (v1.0) and six development activities (v1.1) are unchanged. Four new fiction-weighted development activities:

- **SCENE-AUDIT** — works against `_spine.md`; checks that each Scene's value-shift is declared, that `from ≠ to`, that the but/therefore connector to the next scene is not "and then"
- **CHARACTER-CONSISTENCY** — works against Character Items; surfaces voice / behavior / want drift; for antagonist Characters specifically checks the steelman is still loadbearing
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

- `_meta/SCHEMA-OF-SCHEMAS.md` — Layer 1 universals updated for v1.2 fiction backbones and Motif Item; Layer 2 per-genre branch expanded with fiction-specific elements; audit checklist expanded; v1.2 additions section added
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

The value-shift discipline is the single most load-bearing fiction-craft enforcement v1.2 adds. Validator check 9 makes the SCENE-AUDIT rule executable, not merely aspirational. The steelmanned-antagonist discipline is the second — character Items for antagonists must now include a from-inside-the-frame steelman, and the CHARACTER-CONSISTENCY activity audits whether the steelman is still loadbearing as the manuscript evolves.

The fiction READER-SIMULATION reframe matters: v1.1's READER-SIMULATION was implicitly argumentative (the Reader is reading for argument quality). For fiction, the Reader is reading for emotional weight, tonal register, character-specific cues, and the moment-to-moment perceptual experience. The Vineyard-Expert reader Item in the worked example shows the domain-expert reader specialized for fiction (catching technical errors in the setting without flattening the literary read).

The scaffolding-fade discipline matters more in fiction than in non-fiction, because invention is the central skill the OV must not crowd out. The Late Frost cartridge ships in `gradual-fade` mode, with the explicit chapter-12 note about why fiction's fade thresholds are tighter than non-fiction's.

This release is backward-compatible with all v1.0 and v1.1 cartridges. Existing fiction cartridges without `_spine.md`, `_continuity.md`, `_promises.md`, or Motif Items remain valid; the AI surfaces the v1.2 additions during BOOTSTRAP and CRAFT-REVIEW sessions but does not retroactively require them.

---

## [1.1.0] — 2026-06-02

### Added — the development layer

The shift this release makes is from *production-and-continuity* to *production-and-growth*. v1.0 tracked the manuscript beautifully and tracked the writer not at all. v1.1 closes that gap with a development layer that models the writer's skill, makes the reader a first-class concern, separates argument from outline, and adds the feedback activities the production set was missing.

**New engine chapters:**

- **`09-WRITER-DEVELOPMENT.md`** — the craft-profile (OV-root, cross-cartridge) and craft-log (per-cartridge) artifacts; the diagnostic-not-instance feedback stance that turns "this transition is weak" (said ten times) into "you consistently end sections on the example without landing the closing claim — here's the targeted fix"; the **scaffolding fade** mechanism (`lfw_scaffolding_mode: full | gradual-fade | socratic`) with explicit session-count thresholds, so the OV designs in becoming-less-needed rather than hoping for it; the **opt-in craft modules** (`concrete-to-abstract`, `signposting`, `given-new`, `curse-of-knowledge`) as on-request coaching rather than silent enforcement; the two cautions (skill is observational not scored; craft-work-as-procrastination is the same anti-pattern as research-as-procrastination).
- **`10-READER-AND-ARGUMENT.md`** — the **Reader Item** as the non-fiction analog to Character; the **`_argument.md` backbone** as the argument's logical structure separate from `_outline.md`'s container hierarchy; the six new development activities defined formally (READER-SIMULATION, ARGUMENT-AUDIT, CLAIM-EVIDENCE-CHECK, STEELMAN, SYNTHESIS-CHECK, CRAFT-REVIEW).

**New Prototype:**

- **Reader** (`LFW_Reader`) — first-class Item representing a modeled audience member. Status enum: `developing | active | retired`. Standard recommended set for non-fiction: The Skeptic, The Impatient Generalist, The Domain Expert. Used in READER-SIMULATION activities.

**New backbone files:**

- **`_argument.md`** — per-cartridge argument backbone (thesis, sub-claims, evidence map, defeaters, honest unknown). Required for non-fiction and dissertation cartridges; recommended for memoir / narrative non-fiction; optional for fiction with thematic argument.
- **`_craft-log.md`** — per-cartridge writer-pattern record. Optional but recommended for any serious project.

**New OV-root file:**

- **`_craft-profile.md`** — the cross-cartridge writer-skill memory. Persists across every cartridge. Operator-private (gitignored). Opt-in (writer creates when ready). Observational, never scored.

**Activity set expanded 10 → 16:**

The original ten production activities (SESSION-START, OUTLINE, DRAFT, REVISE, RESEARCH-INTEGRATION, READ-THROUGH, STUCK-DIAGNOSTIC, VOICE-CHECK, WORLDBUILDING, BETA-PREP) are unchanged. Six new development activities:

- **READER-SIMULATION** — AI reads a drafted Item as a specific Reader; reports resistance, lost threads, curse of knowledge
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

- `_meta/SCHEMA-OF-SCHEMAS.md` — three-layer ontology expanded to four (Layer 0 = OV-root persistent files; Layer 1 = per-cartridge universals; Layer 2 = per-genre branches; Layer 3 = per-cartridge instances). New Item + backbones documented.
- `_meta/FAILURE-MODES.md` — added F18 (craft-work-as-procrastination), F19 (scaffolding-never-fades), F20 (skill-scoring-attempted), F21 (reader-Items-used-to-flatter).

**Validator:**

- Extended `STATUS_ENUM` to include `reader: {developing, active, retired}`
- Extended `BACKBONE_FILES` to include `_argument`, `_craft-log`
- Same eight checks; now covers all new artifacts

**Worked example updates:**

- Three Reader Items added: `Skeptic.md`, `Impatient-Generalist.md`, `Domain-Expert.md`
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

- **Wiki-link namespace normalized.** v1.0 shipped the worked example with three competing naming conventions for the same Item files (order-only `[[01-Hoshi-Opening]]`, chapter-prefixed file `03-01-Hoshi-Opening.md`, plus variant short/long Source names). All links now use the canonical chapter-prefixed filename form. `_writing-engine/04-ITEMS-AND-STRUCTURE.md` updated with explicit naming conventions per Prototype and an explicit "Item_ID is a separate namespace from filenames" section.
- **Stub Items shipped** for every Item referenced in `_state.md`, `_outline.md`, Thread Items, and Chapter compositions but not previously present (33 stubs total: 6 Chapters, 11 Sections, 13 Sources, 3 session logs). The example cartridge's link graph is now closed: every wiki-link resolves to a real file.
- **Status enum unified.** v1.0 had three different `lfw_status` enums across templates (Beat: `planned|drafted|revised|final`; Chapter: `outlined|drafting|drafted|revising|revised|final`; Section: `planned|drafted|revised|fact-checked|final`). Section in the worked example was set to `drafting`, which was illegal under its own template. Now all prose-bearing Items (Beat / Scene / Section / Chapter / Act) share one canonical enum: `planned | drafting | drafted | revising | revised | final`. Non-fiction Section adds `fact-checked` between `revised` and `final`. `outlined` deprecated.
- **Act and Setting templates shipped.** v1.0 advertised screenplay and play genre support but didn't ship `TEMPLATE-Act.md` or `TEMPLATE-Setting.md`, violating the engine's own "extending Item set requires a template" rule. Both templates added; `04-ITEMS-AND-STRUCTURE.md` documents them.

### Added — validator

- **`_writing-engine/_scripts/validate.py`** — stdlib-only Python validator that walks one or more cartridges and reports structural issues across eight checks (wiki-link resolution, _state reference existence, status enum legality, Item-type known, template existence, filename conformance, required frontmatter, Item_ID uniqueness). Exit code 0 on clean, 1 on issues. Optional tooling; not part of session flow. See `_writing-engine/_scripts/README.md` for usage.

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
  - `04-ITEMS-AND-STRUCTURE.md` — Item-type definitions (Beat, Scene, Section, Chapter, Character, Thread, Source, Note); relationships; composition rules
  - `05-VOICE-AND-CRAFT.md` — configurable three-tier voice model (writer-maintains-default / voice-samples-optional / VOICE-CHECK-on-demand); craft conventions
  - `06-RESEARCH-INTEGRATION.md` — for non-fiction and dissertation: source ingestion, citation discipline, fold-in protocol, anti-fabrication rules
  - `07-REVISION-DISCIPLINE.md` — multi-pass revision (structure / voice / accuracy / prose-line); revision-pass log conventions
  - `08-FINISHING.md` — getting from drafted to shippable; beta-reader prep; assembly; honest-thinness audit
  - `BOOTSTRAP-NEW-MANUSCRIPT.md` — cartridging prompt for opening a new manuscript engagement
- **Templates** (`_writing-engine/_templates/`):
  - Item templates: `TEMPLATE-Beat.md`, `TEMPLATE-Scene.md`, `TEMPLATE-Section.md`, `TEMPLATE-Chapter.md`, `TEMPLATE-Character.md`, `TEMPLATE-Thread.md`, `TEMPLATE-Source.md`, `TEMPLATE-Note.md`
  - Cartridge backbone: `TEMPLATE-manuscript-manifest.md`, `TEMPLATE-state.md`, `TEMPLATE-outline.md`, `TEMPLATE-voice-samples.md`
  - Process: `TEMPLATE-Session.md`, `TEMPLATE-revision-pass.md`
- **Meta** (`_writing-engine/_meta/`):
  - `SCHEMA-OF-SCHEMAS.md` — three-layer ontology applied to LFW (engine universals / per-genre branch / per-instance)
  - `FAILURE-MODES.md` — canonical catalog of LFW-specific and inherited failure modes (multi-bullet questionnaire, fabrication, identity inference, AI voice homogenization, drafting-before-outlining, scope creep, abandoned-revision-pass, etc.)
- **Root docs**: `README.md`, `AI-BOOTSTRAP.md`, `INSTALL.md`, `OPERATOR-GUIDE.md`, `CONTRIBUTING.md`, `LICENSE.md` (CC-BY 4.0), `VERSION.md`, this file, `_USER.md.template`, `.gitignore`
- **One worked-example cartridge**: `Example-Project-The-Persistence-Question/` — a hypothetical non-fiction book about *why some institutions, traditions, and ideas persist across centuries while others vanish in decades* — at outlining-to-mid-draft stage. Demonstrates: structural outline, source Items with real citations to real (publicly known) works, thread Items, section Items with prose, beat Items, voice samples, session logs, and a revision pass.

### Notes

Long-Form-Writing v1.0 is the fourth operating volume in the same author's trio-now-quartet:

- **[SOLVE-eX](https://github.com/JawnLam/SOLVE-eX)** — decision-making and problem-solving
- **[LifeLong-Learning](https://github.com/JawnLam/LifeLong-Learning)** — self-directed deep study
- **[Operating-Volume-Engineering](https://github.com/JawnLam/Operating-Volume-Engineering)** — the propagator
- **Long-Form-Writing** (this) — sustained writing across multi-month/multi-year projects

LFW takes the cartridge-as-manuscript pattern that appeared as a lighter worked-example inside OVE v1.0 and develops it fully. The daily-practice cadence and configurable voice model are the distinctive innovations.
