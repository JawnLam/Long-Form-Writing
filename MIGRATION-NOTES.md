# Migration Notes — Core/Pack + Generated-Router Progressive Disclosure

**Branch:** `feat/core-pack-progressive-disclosure`
**Baseline:** v1.4.0 (commit `8a9caaf`); validator clean on both example cartridges
**Scope:** structural and tooling change only; zero new capability

## Architectural intent

- **Bootstrap-phase** = the minimal always-read set. Only chapters needed to consult the router itself: `00-START-HERE`, `03-CADENCE-AND-SESSIONS`, and `_ROUTER.md`. Plus the OV-root entry point `AI-BOOTSTRAP.md` (consulted before the engine).
- **Core / on-demand** = loaded by router dispatch when a relevant activity fires. May still be effectively-always-loaded via `activities: [all]`, but the gate is the router (correct-by-construction).
- **Pack** = loaded only when the cartridge genre matches AND an activity matches. Non-fiction cartridges never load fiction-pack chapters and vice versa.

## Chapter → pack assignment

| Chapter | tier | genres | activities | phase | Notes |
|---------|------|--------|------------|-------|-------|
| `00-START-HERE.md` | core | [all] | [all] | bootstrap | Assistant entry point |
| `01-WHAT-IS-LFW.md` | core | [all] | [SESSION-START] | on-demand | Orientation; loaded at session-start only |
| `02-GENRE-AND-SCHEMA.md` | core | [all] | [SESSION-START] | on-demand | Genre-branching reference; rare consult after bootstrap |
| `03-CADENCE-AND-SESSIONS.md` | core | [all] | [all] | bootstrap | Activity decision algorithm; required every session |
| `04-ITEMS-AND-STRUCTURE.md` | core | [all] | [OUTLINE, DRAFT, REVISE, READ-THROUGH, BETA-PREP] | on-demand | Item schema reference for prose-touching activities |
| `05-VOICE-AND-CRAFT.md` | core | [all] | [all] | on-demand | Existing 00 spec: "read on every session" — dispatched on every activity via router |
| `06-RESEARCH-INTEGRATION.md` | pack | [non-fiction, dissertation] | [RESEARCH-INTEGRATION, CLAIM-EVIDENCE-CHECK, SYNTHESIS-CHECK] | on-demand | Source citation discipline; non-fic only |
| `07-REVISION-DISCIPLINE.md` | core | [all] | [REVISE, READ-THROUGH, BETA-PREP] | on-demand | Multi-pass revision protocol |
| `08-FINISHING.md` | core | [all] | [BETA-PREP, READ-THROUGH] | on-demand | Late-stage polish + assembly |
| `09-WRITER-DEVELOPMENT.md` | core | [all] | [all] | on-demand | Existing 00 spec: "read on every session" via router dispatch |
| `10-READER.md` *(after split)* | core | [all] | [READER-SIMULATION, CRAFT-REVIEW] | on-demand | Reader Item + audience modeling; serves every genre |
| `10-ARGUMENT.md` *(after split)* | pack | [non-fiction, dissertation] | [ARGUMENT-AUDIT, CLAIM-EVIDENCE-CHECK, STEELMAN, SYNTHESIS-CHECK] | on-demand | Argument backbone + four non-fic activities |
| `11-FICTION-PLOT-SPINE.md` | pack | [fiction, screenplay, play] | [SCENE-AUDIT, SETUP-PAYOFF-AUDIT, OUTLINE, READ-THROUGH] | on-demand | Spine + promises |
| `12-FICTION-CHARACTER-AND-CONTINUITY.md` | pack | [fiction, screenplay, play] | [CHARACTER-CONSISTENCY, CONTINUITY-CHECK, WORLDBUILDING, READER-SIMULATION] | on-demand | Includes fiction READER-SIMULATION reframe (§6) |
| `13-FICTION-DIALOGUE-AND-POV-VOICE.md` | pack | [fiction, screenplay, play] | [DIALOGUE-AUDIT, POV-VOICE-DRIFT, REVISE] | on-demand | Line-level fiction craft |
| `14-FICTION-STRUCTURE-OVERLAYS-AND-EXTENSIONS.md` | pack | [fiction, screenplay, play] | [THEME-CHECK, OUTLINE, CHARACTER-CONSISTENCY, READ-THROUGH] | on-demand | Scene-sequel, themes, overlays, bibles |
| `15-FICTION-PROJECT-ARTIFACTS.md` | pack | [fiction, screenplay, play] | [WORLDBUILDING, CONTINUITY-CHECK, READ-THROUGH, BETA-PREP, REVISE] | on-demand | Worldbuilding, timeline, storyboard, style-sheet, etc. |
| `16-WRITER-WEATHER-AND-MIDDLE-AUDIT.md` | core | [all] | [all] | on-demand | Chapter 16 §6 spec: "required reading on every session" |
| `BOOTSTRAP-NEW-MANUSCRIPT.md` | core | [all] | [SESSION-START] | on-demand | Cartridging protocol; see note 1 below |

### Meta files

| File | tier | genres | activities | phase | Notes |
|------|------|--------|------------|-------|-------|
| `_meta/FAILURE-MODES.md` | core | [all] | [all] | on-demand | Existing 00 spec: "read on every session" |
| `_meta/SCHEMA-OF-SCHEMAS.md` | core | [all] | [SESSION-START] | on-demand | Meta-ontology reference |

## Item → pack assignment

| Item prototype | tier | Notes |
|----------------|------|-------|
| `LFW_Beat`, `LFW_Chapter`, `LFW_Note`, `LFW_Reader`, `LFW_Craft_Log`, `LFW_Craft_Profile`, `LFW_Manuscript_Manifest`, `LFW_State`, `LFW_Outline`, `LFW_Session`, `LFW_Revision_Pass` | core | Universal across all genres |
| `LFW_Section`, `LFW_Thread`, `LFW_Source`, `LFW_Argument` | non-fic pack | |
| `LFW_Scene`, `LFW_Character`, `LFW_Character_Bible`, `LFW_Motif`, `LFW_Theme`, `LFW_Spine`, `LFW_Promises`, `LFW_Continuity`, `LFW_Timeline`, `LFW_Storyboard`, `LFW_Style_Sheet`, `LFW_Relationships`, `LFW_Worldbuilding`, `LFW_Inspiration`, `LFW_Overlay_Story_Circle`, `LFW_Overlay_Save_The_Cat`, `LFW_Overlay_Heros_Journey`, `LFW_Overlay_Freytag` | fiction pack | |
| `LFW_Act`, `LFW_Setting` | screenplay/play pack | Small; logical grouping only — no separate physical pack folder |
| `LFW_Voice_Sample` | core | Voice samples are universal |

## Notes / flagged ambiguities

### Note 1 — BOOTSTRAP-NEW-MANUSCRIPT.md and cartridge-bootstrap workflow

The cartridge-bootstrap workflow (a writer starting a new manuscript) does not have a formal activity code in chapter 03's 25-activity set. The brief says "Use the activity codes exactly as defined in chapter 03's activity set... Do not invent codes." Using `SESSION-START` as the closest proxy (a new cartridge bootstrap is the first SESSION-START of that cartridge). This is the only ambiguity in the assignment.

**Decision:** use `activities: [SESSION-START]` for `BOOTSTRAP-NEW-MANUSCRIPT.md`. Flagging for human awareness; no decision is required to proceed.

### Note 2 — Chapter 10 split prose-coherence touches

The brief says "Preserve all prose; only divide it." Splitting `10-READER-AND-ARGUMENT.md` requires:

- The shared chapter intro mentions BOTH Reader and Argument concerns. Each split file needs an intro covering only its half. This is dividing (each sentence appears in exactly one file), not rewriting.
- The chapter's title needs to be split: `10 — READER (Audience Modeling)` and `10 — ARGUMENT (Non-Fiction Backbone)`.
- The "How chapter 10 interacts" section similarly divides along the seam.
- Part three's six activities split: READER-SIMULATION + CRAFT-REVIEW → `10-READER.md`; ARGUMENT-AUDIT, CLAIM-EVIDENCE-CHECK, STEELMAN, SYNTHESIS-CHECK → `10-ARGUMENT.md`.

This is the chapter-10 case the brief acknowledges. No further ambiguity.

### Note 3 — Historical references to "chapter 10" left intact

References to chapter 10 in historical sections (CHANGELOG entries describing what v1.1 shipped; SCHEMA-OF-SCHEMAS v1.1 additions section) are NOT updated. They describe the file as it was at v1.1 release. Forward-looking references in current-state documents ARE updated to point at `10-READER.md` or `10-ARGUMENT.md` as appropriate.

### Note 4 — Novel-internal "Chapter 10" references in Late Frost

The Late Frost cartridge contains many references to "Chapter 10" — these refer to the *novel's* tenth chapter (the fight about the father), not to the engine's chapter 10. These are NOT touched.

## Phase progression

- [x] Phase 0: branch, baseline validator, ground-truth reads, migration notes
- [x] Phase 1: lfw_load declarations + build-router.py + _ROUTER.md
- [x] Phase 2: split chapter 10
- [x] Phase 3: rewrite AI-BOOTSTRAP reading list
- [x] Phase 4: validator extensions + session read-coverage
- [x] Phase 5: teeth test + genre-isolation + CHANGELOG + VERSION

## Teeth-test record (Phase 5)

All three mutations were performed in the working copy, the validator was run, the expected failure was confirmed, and the state was restored. No mutation was committed.

### Teeth test (a) — router-fresh fails on hand-edited lfw_load without router regeneration

**Mutation:** changed chapter 11's `activities` declaration from `[SCENE-AUDIT, SETUP-PAYOFF-AUDIT, OUTLINE, READ-THROUGH]` to `[SCENE-AUDIT]` (a real change that shrinks the dispatch table), and did NOT run `build-router.py` afterwards.

**Validator output (relevant lines):**

```
[router-fresh] 1 issue(s) (FAIL):
TOTAL ISSUES: 1 (+4 warning(s))
```

**Diagnosis confirmed:** the check correctly detected that the committed `_ROUTER.md` no longer matches what `render_router(collect_sources())` produces. Stale router → build failure, as designed. (Initial attempt with a `tier: core → pack` change was a no-op because the chapter's `genres/activities` were both `[all]`, so the dispatch table was unchanged. The second mutation, on `activities`, exercised the check meaningfully.)

**Restoration:** original chapter 11 content restored; validator returns to clean state.

### Teeth test (b) — wiki-link-resolves fails on dangling reference

**Mutation:** appended `<!-- teeth-test dangling: [[Definitely-Not-A-Real-Item-99999]] -->` to `Example-Project-The-Late-Frost/_outline.md`.

**Validator output (relevant lines):**

```
[wiki-link-resolves] 1 issue(s) (FAIL):
TOTAL ISSUES: 1 (+3 warning(s))
```

**Diagnosis confirmed:** the existing v1.0.1 wiki-link-resolves check correctly catches dangling references in cartridge files. Phase 4 preserves this check unchanged. (First attempt on `00-START-HERE.md` was a no-op because the link check walks cartridge files, not engine chapters — by design; engine isn't a cartridge.)

**Restoration:** original outline restored; validator returns to clean state.

### Teeth test (c) — session-read-coverage fails on fiction OUTLINE missing required pack chapter

**Mutation:** created `Example-Project-The-Late-Frost/Sessions/2099-12-31_999_TEETH-TEST.md` declaring `lfw_session_activity: OUTLINE` but a `lfw_chapters_loaded` list that omits `_writing-engine/11-FICTION-PLOT-SPINE.md` and `_writing-engine/14-FICTION-STRUCTURE-OVERLAYS-AND-EXTENSIONS.md` (both required for fiction OUTLINE per the router).

**Validator output (relevant lines):**

```
[session-read-coverage] 1 issue(s) (FAIL):
TOTAL ISSUES: 1 (+3 warning(s))
```

**Diagnosis confirmed:** the new session-read-coverage check correctly fails when a fiction OUTLINE session omits required fiction-pack chapters from `lfw_chapters_loaded`.

**Restoration:** teeth-test session log deleted; validator returns to clean state.

### Genre-isolation positive assertion

Added as validator check 16 (`genre-isolation`). Walks the router's dispatch table and asserts:

- No fiction-pack chapter ever appears under `genre = non-fiction` or `genre = dissertation`
- No non-fiction-pack chapter (chapter 06, 10-ARGUMENT) ever appears under `genre = fiction`, `screenplay`, or `play`

Passes on the current router. Combined with `router-fresh`, isolation is correct by construction: the only way to violate isolation is to hand-edit `_ROUTER.md` after build-router writes it (which `router-fresh` then catches) or to introduce contradictory `lfw_load` frontmatter (which `load-declared` would catch only structurally — the genre/activity codes are valid even if semantically wrong; this is why the positive assertion is added as its own check).

## Final state

- New validator checks: **13** (load-declared), **14** (router-fresh), **15** (session-read-coverage, FAIL + warn), **16** (genre-isolation)
- New scripts: `_writing-engine/_scripts/build-router.py`
- New generated file: `_writing-engine/_ROUTER.md`
- Split: `10-READER-AND-ARGUMENT.md` → `10-READER.md` (core) + `10-ARGUMENT.md` (non-fic pack)
- Rewritten: `AI-BOOTSTRAP.md` reading-list section
- Updated: `TEMPLATE-Session.md` (gains `lfw_chapters_loaded`)
- Backfilled: 7 example session logs with `lfw_chapters_loaded`
- No new Items, activities, chapters, templates, or failure modes
- No files physically moved
- Stdlib-only preserved (no new runtime dependencies)
- Both example cartridges pass with the new checks active
