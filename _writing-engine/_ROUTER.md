# _ROUTER.md — LFW Engine Dispatch Manifest

> **GENERATED FILE — DO NOT EDIT BY HAND.**
>
> Regenerate with `python3 _writing-engine/_scripts/build-router.py`.
>
> The validator's `router-fresh` check regenerates this file in memory
> on every run and fails if the committed copy differs from the regenerated
> content. A stale router becomes a build failure — correct by construction.

Source-of-truth for which engine chapters an AI loads on a given session,
computed from each chapter's `lfw_load` frontmatter declaration. AI clients
consult this file after reading the bootstrap-phase chapters and use the
(genre, activity) tables to determine which on-demand chapters to load.

---

## 1. Bootstrap-phase (always loaded, every session)

These chapters are loaded before the router is consulted. The minimal
always-read set required to dispatch the rest of the engine.

- `_writing-engine/00-START-HERE.md`
- `_writing-engine/03-CADENCE-AND-SESSIONS.md`
- `_writing-engine/_ROUTER.md` (this file)

AI clients should also read `AI-BOOTSTRAP.md` at the OV root before any
engine chapter, then load the bootstrap-phase chapters above plus this
router, then dispatch via the tables below.

## 2. By genre — chapters this genre activates (on-demand)

For a cartridge of a given genre, these are the chapters the router may
dispatch (depending on session activity — see §3). Chapters NOT listed for
a genre are never loaded for that genre, no matter what activity is run.

### dissertation

- `_writing-engine/01-WHAT-IS-LFW.md`
- `_writing-engine/02-GENRE-AND-SCHEMA.md`
- `_writing-engine/04-ATOMS-AND-STRUCTURE.md`
- `_writing-engine/05-VOICE-AND-CRAFT.md`
- `_writing-engine/06-RESEARCH-INTEGRATION.md`
- `_writing-engine/07-REVISION-DISCIPLINE.md`
- `_writing-engine/08-FINISHING.md`
- `_writing-engine/09-WRITER-DEVELOPMENT.md`
- `_writing-engine/10-ARGUMENT.md`
- `_writing-engine/10-READER.md`
- `_writing-engine/16-WRITER-WEATHER-AND-MIDDLE-AUDIT.md`
- `_writing-engine/BOOTSTRAP-NEW-MANUSCRIPT.md`
- `_writing-engine/_meta/FAILURE-MODES.md`
- `_writing-engine/_meta/SCHEMA-OF-SCHEMAS.md`

### fiction

- `_writing-engine/01-WHAT-IS-LFW.md`
- `_writing-engine/02-GENRE-AND-SCHEMA.md`
- `_writing-engine/04-ATOMS-AND-STRUCTURE.md`
- `_writing-engine/05-VOICE-AND-CRAFT.md`
- `_writing-engine/07-REVISION-DISCIPLINE.md`
- `_writing-engine/08-FINISHING.md`
- `_writing-engine/09-WRITER-DEVELOPMENT.md`
- `_writing-engine/10-READER.md`
- `_writing-engine/11-FICTION-PLOT-SPINE.md`
- `_writing-engine/12-FICTION-CHARACTER-AND-CONTINUITY.md`
- `_writing-engine/13-FICTION-DIALOGUE-AND-POV-VOICE.md`
- `_writing-engine/14-FICTION-STRUCTURE-OVERLAYS-AND-EXTENSIONS.md`
- `_writing-engine/15-FICTION-PROJECT-ARTIFACTS.md`
- `_writing-engine/16-WRITER-WEATHER-AND-MIDDLE-AUDIT.md`
- `_writing-engine/BOOTSTRAP-NEW-MANUSCRIPT.md`
- `_writing-engine/_meta/FAILURE-MODES.md`
- `_writing-engine/_meta/SCHEMA-OF-SCHEMAS.md`

### non-fiction

- `_writing-engine/01-WHAT-IS-LFW.md`
- `_writing-engine/02-GENRE-AND-SCHEMA.md`
- `_writing-engine/04-ATOMS-AND-STRUCTURE.md`
- `_writing-engine/05-VOICE-AND-CRAFT.md`
- `_writing-engine/06-RESEARCH-INTEGRATION.md`
- `_writing-engine/07-REVISION-DISCIPLINE.md`
- `_writing-engine/08-FINISHING.md`
- `_writing-engine/09-WRITER-DEVELOPMENT.md`
- `_writing-engine/10-ARGUMENT.md`
- `_writing-engine/10-READER.md`
- `_writing-engine/16-WRITER-WEATHER-AND-MIDDLE-AUDIT.md`
- `_writing-engine/BOOTSTRAP-NEW-MANUSCRIPT.md`
- `_writing-engine/_meta/FAILURE-MODES.md`
- `_writing-engine/_meta/SCHEMA-OF-SCHEMAS.md`

### play

- `_writing-engine/01-WHAT-IS-LFW.md`
- `_writing-engine/02-GENRE-AND-SCHEMA.md`
- `_writing-engine/04-ATOMS-AND-STRUCTURE.md`
- `_writing-engine/05-VOICE-AND-CRAFT.md`
- `_writing-engine/07-REVISION-DISCIPLINE.md`
- `_writing-engine/08-FINISHING.md`
- `_writing-engine/09-WRITER-DEVELOPMENT.md`
- `_writing-engine/10-READER.md`
- `_writing-engine/11-FICTION-PLOT-SPINE.md`
- `_writing-engine/12-FICTION-CHARACTER-AND-CONTINUITY.md`
- `_writing-engine/13-FICTION-DIALOGUE-AND-POV-VOICE.md`
- `_writing-engine/14-FICTION-STRUCTURE-OVERLAYS-AND-EXTENSIONS.md`
- `_writing-engine/15-FICTION-PROJECT-ARTIFACTS.md`
- `_writing-engine/16-WRITER-WEATHER-AND-MIDDLE-AUDIT.md`
- `_writing-engine/BOOTSTRAP-NEW-MANUSCRIPT.md`
- `_writing-engine/_meta/FAILURE-MODES.md`
- `_writing-engine/_meta/SCHEMA-OF-SCHEMAS.md`

### screenplay

- `_writing-engine/01-WHAT-IS-LFW.md`
- `_writing-engine/02-GENRE-AND-SCHEMA.md`
- `_writing-engine/04-ATOMS-AND-STRUCTURE.md`
- `_writing-engine/05-VOICE-AND-CRAFT.md`
- `_writing-engine/07-REVISION-DISCIPLINE.md`
- `_writing-engine/08-FINISHING.md`
- `_writing-engine/09-WRITER-DEVELOPMENT.md`
- `_writing-engine/10-READER.md`
- `_writing-engine/11-FICTION-PLOT-SPINE.md`
- `_writing-engine/12-FICTION-CHARACTER-AND-CONTINUITY.md`
- `_writing-engine/13-FICTION-DIALOGUE-AND-POV-VOICE.md`
- `_writing-engine/14-FICTION-STRUCTURE-OVERLAYS-AND-EXTENSIONS.md`
- `_writing-engine/15-FICTION-PROJECT-ARTIFACTS.md`
- `_writing-engine/16-WRITER-WEATHER-AND-MIDDLE-AUDIT.md`
- `_writing-engine/BOOTSTRAP-NEW-MANUSCRIPT.md`
- `_writing-engine/_meta/FAILURE-MODES.md`
- `_writing-engine/_meta/SCHEMA-OF-SCHEMAS.md`

## 3. By (genre, activity) — exact dispatch table

On any given session, the AI determines the cartridge genre (from
`_manuscript-manifest.md`) and the proposed activity (per `03-CADENCE-AND-SESSIONS.md`)
and loads the chapters listed for that pair. Always also load the bootstrap-phase
chapters (§1).

### dissertation

- **ARGUMENT-AUDIT** → `_writing-engine/10-ARGUMENT.md`
- **BETA-PREP** → `_writing-engine/04-ATOMS-AND-STRUCTURE.md`, `_writing-engine/07-REVISION-DISCIPLINE.md`, `_writing-engine/08-FINISHING.md`
- **CLAIM-EVIDENCE-CHECK** → `_writing-engine/06-RESEARCH-INTEGRATION.md`, `_writing-engine/10-ARGUMENT.md`
- **CRAFT-REVIEW** → `_writing-engine/10-READER.md`
- **DRAFT** → `_writing-engine/04-ATOMS-AND-STRUCTURE.md`
- **OUTLINE** → `_writing-engine/04-ATOMS-AND-STRUCTURE.md`
- **READ-THROUGH** → `_writing-engine/04-ATOMS-AND-STRUCTURE.md`, `_writing-engine/07-REVISION-DISCIPLINE.md`, `_writing-engine/08-FINISHING.md`
- **READER-SIMULATION** → `_writing-engine/10-READER.md`
- **RESEARCH-INTEGRATION** → `_writing-engine/06-RESEARCH-INTEGRATION.md`
- **REVISE** → `_writing-engine/04-ATOMS-AND-STRUCTURE.md`, `_writing-engine/07-REVISION-DISCIPLINE.md`
- **SESSION-START** → `_writing-engine/01-WHAT-IS-LFW.md`, `_writing-engine/02-GENRE-AND-SCHEMA.md`, `_writing-engine/BOOTSTRAP-NEW-MANUSCRIPT.md`, `_writing-engine/_meta/SCHEMA-OF-SCHEMAS.md`
- **STEELMAN** → `_writing-engine/10-ARGUMENT.md`
- **SYNTHESIS-CHECK** → `_writing-engine/06-RESEARCH-INTEGRATION.md`, `_writing-engine/10-ARGUMENT.md`
- **all** → `_writing-engine/05-VOICE-AND-CRAFT.md`, `_writing-engine/09-WRITER-DEVELOPMENT.md`, `_writing-engine/16-WRITER-WEATHER-AND-MIDDLE-AUDIT.md`, `_writing-engine/_meta/FAILURE-MODES.md`
### fiction

- **BETA-PREP** → `_writing-engine/04-ATOMS-AND-STRUCTURE.md`, `_writing-engine/07-REVISION-DISCIPLINE.md`, `_writing-engine/08-FINISHING.md`, `_writing-engine/15-FICTION-PROJECT-ARTIFACTS.md`
- **CHARACTER-CONSISTENCY** → `_writing-engine/12-FICTION-CHARACTER-AND-CONTINUITY.md`, `_writing-engine/14-FICTION-STRUCTURE-OVERLAYS-AND-EXTENSIONS.md`
- **CONTINUITY-CHECK** → `_writing-engine/12-FICTION-CHARACTER-AND-CONTINUITY.md`, `_writing-engine/15-FICTION-PROJECT-ARTIFACTS.md`
- **CRAFT-REVIEW** → `_writing-engine/10-READER.md`
- **DIALOGUE-AUDIT** → `_writing-engine/13-FICTION-DIALOGUE-AND-POV-VOICE.md`
- **DRAFT** → `_writing-engine/04-ATOMS-AND-STRUCTURE.md`
- **OUTLINE** → `_writing-engine/04-ATOMS-AND-STRUCTURE.md`, `_writing-engine/11-FICTION-PLOT-SPINE.md`, `_writing-engine/14-FICTION-STRUCTURE-OVERLAYS-AND-EXTENSIONS.md`
- **POV-VOICE-DRIFT** → `_writing-engine/13-FICTION-DIALOGUE-AND-POV-VOICE.md`
- **READ-THROUGH** → `_writing-engine/04-ATOMS-AND-STRUCTURE.md`, `_writing-engine/07-REVISION-DISCIPLINE.md`, `_writing-engine/08-FINISHING.md`, `_writing-engine/11-FICTION-PLOT-SPINE.md`, `_writing-engine/14-FICTION-STRUCTURE-OVERLAYS-AND-EXTENSIONS.md`, `_writing-engine/15-FICTION-PROJECT-ARTIFACTS.md`
- **READER-SIMULATION** → `_writing-engine/10-READER.md`, `_writing-engine/12-FICTION-CHARACTER-AND-CONTINUITY.md`
- **REVISE** → `_writing-engine/04-ATOMS-AND-STRUCTURE.md`, `_writing-engine/07-REVISION-DISCIPLINE.md`, `_writing-engine/13-FICTION-DIALOGUE-AND-POV-VOICE.md`, `_writing-engine/15-FICTION-PROJECT-ARTIFACTS.md`
- **SCENE-AUDIT** → `_writing-engine/11-FICTION-PLOT-SPINE.md`
- **SESSION-START** → `_writing-engine/01-WHAT-IS-LFW.md`, `_writing-engine/02-GENRE-AND-SCHEMA.md`, `_writing-engine/BOOTSTRAP-NEW-MANUSCRIPT.md`, `_writing-engine/_meta/SCHEMA-OF-SCHEMAS.md`
- **SETUP-PAYOFF-AUDIT** → `_writing-engine/11-FICTION-PLOT-SPINE.md`
- **THEME-CHECK** → `_writing-engine/14-FICTION-STRUCTURE-OVERLAYS-AND-EXTENSIONS.md`
- **WORLDBUILDING** → `_writing-engine/12-FICTION-CHARACTER-AND-CONTINUITY.md`, `_writing-engine/15-FICTION-PROJECT-ARTIFACTS.md`
- **all** → `_writing-engine/05-VOICE-AND-CRAFT.md`, `_writing-engine/09-WRITER-DEVELOPMENT.md`, `_writing-engine/16-WRITER-WEATHER-AND-MIDDLE-AUDIT.md`, `_writing-engine/_meta/FAILURE-MODES.md`
### non-fiction

- **ARGUMENT-AUDIT** → `_writing-engine/10-ARGUMENT.md`
- **BETA-PREP** → `_writing-engine/04-ATOMS-AND-STRUCTURE.md`, `_writing-engine/07-REVISION-DISCIPLINE.md`, `_writing-engine/08-FINISHING.md`
- **CLAIM-EVIDENCE-CHECK** → `_writing-engine/06-RESEARCH-INTEGRATION.md`, `_writing-engine/10-ARGUMENT.md`
- **CRAFT-REVIEW** → `_writing-engine/10-READER.md`
- **DRAFT** → `_writing-engine/04-ATOMS-AND-STRUCTURE.md`
- **OUTLINE** → `_writing-engine/04-ATOMS-AND-STRUCTURE.md`
- **READ-THROUGH** → `_writing-engine/04-ATOMS-AND-STRUCTURE.md`, `_writing-engine/07-REVISION-DISCIPLINE.md`, `_writing-engine/08-FINISHING.md`
- **READER-SIMULATION** → `_writing-engine/10-READER.md`
- **RESEARCH-INTEGRATION** → `_writing-engine/06-RESEARCH-INTEGRATION.md`
- **REVISE** → `_writing-engine/04-ATOMS-AND-STRUCTURE.md`, `_writing-engine/07-REVISION-DISCIPLINE.md`
- **SESSION-START** → `_writing-engine/01-WHAT-IS-LFW.md`, `_writing-engine/02-GENRE-AND-SCHEMA.md`, `_writing-engine/BOOTSTRAP-NEW-MANUSCRIPT.md`, `_writing-engine/_meta/SCHEMA-OF-SCHEMAS.md`
- **STEELMAN** → `_writing-engine/10-ARGUMENT.md`
- **SYNTHESIS-CHECK** → `_writing-engine/06-RESEARCH-INTEGRATION.md`, `_writing-engine/10-ARGUMENT.md`
- **all** → `_writing-engine/05-VOICE-AND-CRAFT.md`, `_writing-engine/09-WRITER-DEVELOPMENT.md`, `_writing-engine/16-WRITER-WEATHER-AND-MIDDLE-AUDIT.md`, `_writing-engine/_meta/FAILURE-MODES.md`
### play

- **BETA-PREP** → `_writing-engine/04-ATOMS-AND-STRUCTURE.md`, `_writing-engine/07-REVISION-DISCIPLINE.md`, `_writing-engine/08-FINISHING.md`, `_writing-engine/15-FICTION-PROJECT-ARTIFACTS.md`
- **CHARACTER-CONSISTENCY** → `_writing-engine/12-FICTION-CHARACTER-AND-CONTINUITY.md`, `_writing-engine/14-FICTION-STRUCTURE-OVERLAYS-AND-EXTENSIONS.md`
- **CONTINUITY-CHECK** → `_writing-engine/12-FICTION-CHARACTER-AND-CONTINUITY.md`, `_writing-engine/15-FICTION-PROJECT-ARTIFACTS.md`
- **CRAFT-REVIEW** → `_writing-engine/10-READER.md`
- **DIALOGUE-AUDIT** → `_writing-engine/13-FICTION-DIALOGUE-AND-POV-VOICE.md`
- **DRAFT** → `_writing-engine/04-ATOMS-AND-STRUCTURE.md`
- **OUTLINE** → `_writing-engine/04-ATOMS-AND-STRUCTURE.md`, `_writing-engine/11-FICTION-PLOT-SPINE.md`, `_writing-engine/14-FICTION-STRUCTURE-OVERLAYS-AND-EXTENSIONS.md`
- **POV-VOICE-DRIFT** → `_writing-engine/13-FICTION-DIALOGUE-AND-POV-VOICE.md`
- **READ-THROUGH** → `_writing-engine/04-ATOMS-AND-STRUCTURE.md`, `_writing-engine/07-REVISION-DISCIPLINE.md`, `_writing-engine/08-FINISHING.md`, `_writing-engine/11-FICTION-PLOT-SPINE.md`, `_writing-engine/14-FICTION-STRUCTURE-OVERLAYS-AND-EXTENSIONS.md`, `_writing-engine/15-FICTION-PROJECT-ARTIFACTS.md`
- **READER-SIMULATION** → `_writing-engine/10-READER.md`, `_writing-engine/12-FICTION-CHARACTER-AND-CONTINUITY.md`
- **REVISE** → `_writing-engine/04-ATOMS-AND-STRUCTURE.md`, `_writing-engine/07-REVISION-DISCIPLINE.md`, `_writing-engine/13-FICTION-DIALOGUE-AND-POV-VOICE.md`, `_writing-engine/15-FICTION-PROJECT-ARTIFACTS.md`
- **SCENE-AUDIT** → `_writing-engine/11-FICTION-PLOT-SPINE.md`
- **SESSION-START** → `_writing-engine/01-WHAT-IS-LFW.md`, `_writing-engine/02-GENRE-AND-SCHEMA.md`, `_writing-engine/BOOTSTRAP-NEW-MANUSCRIPT.md`, `_writing-engine/_meta/SCHEMA-OF-SCHEMAS.md`
- **SETUP-PAYOFF-AUDIT** → `_writing-engine/11-FICTION-PLOT-SPINE.md`
- **THEME-CHECK** → `_writing-engine/14-FICTION-STRUCTURE-OVERLAYS-AND-EXTENSIONS.md`
- **WORLDBUILDING** → `_writing-engine/12-FICTION-CHARACTER-AND-CONTINUITY.md`, `_writing-engine/15-FICTION-PROJECT-ARTIFACTS.md`
- **all** → `_writing-engine/05-VOICE-AND-CRAFT.md`, `_writing-engine/09-WRITER-DEVELOPMENT.md`, `_writing-engine/16-WRITER-WEATHER-AND-MIDDLE-AUDIT.md`, `_writing-engine/_meta/FAILURE-MODES.md`
### screenplay

- **BETA-PREP** → `_writing-engine/04-ATOMS-AND-STRUCTURE.md`, `_writing-engine/07-REVISION-DISCIPLINE.md`, `_writing-engine/08-FINISHING.md`, `_writing-engine/15-FICTION-PROJECT-ARTIFACTS.md`
- **CHARACTER-CONSISTENCY** → `_writing-engine/12-FICTION-CHARACTER-AND-CONTINUITY.md`, `_writing-engine/14-FICTION-STRUCTURE-OVERLAYS-AND-EXTENSIONS.md`
- **CONTINUITY-CHECK** → `_writing-engine/12-FICTION-CHARACTER-AND-CONTINUITY.md`, `_writing-engine/15-FICTION-PROJECT-ARTIFACTS.md`
- **CRAFT-REVIEW** → `_writing-engine/10-READER.md`
- **DIALOGUE-AUDIT** → `_writing-engine/13-FICTION-DIALOGUE-AND-POV-VOICE.md`
- **DRAFT** → `_writing-engine/04-ATOMS-AND-STRUCTURE.md`
- **OUTLINE** → `_writing-engine/04-ATOMS-AND-STRUCTURE.md`, `_writing-engine/11-FICTION-PLOT-SPINE.md`, `_writing-engine/14-FICTION-STRUCTURE-OVERLAYS-AND-EXTENSIONS.md`
- **POV-VOICE-DRIFT** → `_writing-engine/13-FICTION-DIALOGUE-AND-POV-VOICE.md`
- **READ-THROUGH** → `_writing-engine/04-ATOMS-AND-STRUCTURE.md`, `_writing-engine/07-REVISION-DISCIPLINE.md`, `_writing-engine/08-FINISHING.md`, `_writing-engine/11-FICTION-PLOT-SPINE.md`, `_writing-engine/14-FICTION-STRUCTURE-OVERLAYS-AND-EXTENSIONS.md`, `_writing-engine/15-FICTION-PROJECT-ARTIFACTS.md`
- **READER-SIMULATION** → `_writing-engine/10-READER.md`, `_writing-engine/12-FICTION-CHARACTER-AND-CONTINUITY.md`
- **REVISE** → `_writing-engine/04-ATOMS-AND-STRUCTURE.md`, `_writing-engine/07-REVISION-DISCIPLINE.md`, `_writing-engine/13-FICTION-DIALOGUE-AND-POV-VOICE.md`, `_writing-engine/15-FICTION-PROJECT-ARTIFACTS.md`
- **SCENE-AUDIT** → `_writing-engine/11-FICTION-PLOT-SPINE.md`
- **SESSION-START** → `_writing-engine/01-WHAT-IS-LFW.md`, `_writing-engine/02-GENRE-AND-SCHEMA.md`, `_writing-engine/BOOTSTRAP-NEW-MANUSCRIPT.md`, `_writing-engine/_meta/SCHEMA-OF-SCHEMAS.md`
- **SETUP-PAYOFF-AUDIT** → `_writing-engine/11-FICTION-PLOT-SPINE.md`
- **THEME-CHECK** → `_writing-engine/14-FICTION-STRUCTURE-OVERLAYS-AND-EXTENSIONS.md`
- **WORLDBUILDING** → `_writing-engine/12-FICTION-CHARACTER-AND-CONTINUITY.md`, `_writing-engine/15-FICTION-PROJECT-ARTIFACTS.md`
- **all** → `_writing-engine/05-VOICE-AND-CRAFT.md`, `_writing-engine/09-WRITER-DEVELOPMENT.md`, `_writing-engine/16-WRITER-WEATHER-AND-MIDDLE-AUDIT.md`, `_writing-engine/_meta/FAILURE-MODES.md`

---

_Content hash (sha256, first 16 chars): `d1dad77a2b15a988`_
