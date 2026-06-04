---
Item_Prototype: LFW_Session
Item_ID: "<manuscript-slug>-session-<NNN>"
Title: "<Manuscript Title> — Session <NNN> — <Activity>"
Date_Added:
Date_Modified:
Needs_Processing: false
lfw_manuscript: "<manuscript-slug>"
lfw_session_number:
lfw_activity: ""    # one of the 25 activities defined in chapter 03 (consult _ROUTER.md for the canonical set); META / BOOTSTRAP / etc. are tolerated but skip session-read-coverage
lfw_duration_minutes:
lfw_atoms_touched: []
lfw_words_written: 0
lfw_words_revised: 0
lfw_quality_gates_passed: false
lfw_chapters_loaded: []    # v1.5: engine chapter paths loaded for this session. Required for cadence-activity sessions; the validator's session-read-coverage check (#15) verifies coverage against the router. Skip for META/BOOTSTRAP sessions.
---

# Session <NNN> — <Date> — <Activity>

## Opening State Summary

*What the AI found when it read `_state.md`. Two or three sentences. Where the manuscript stood at session start.*

## Activity Proposal & Rationale

*Which conditions from `03-CADENCE-AND-SESSIONS.md` fired. The proposal made. Whether the writer accepted or overrode.*

## What Happened

*Narrative of the session. What was outlined, drafted, revised, integrated, diagnosed.*

## Atoms Touched

| Atom | Type | Status before | Status after | Words before | Words after |
|------|------|---------------|--------------|--------------|-------------|
|      |      |               |              |              |             |

## Decisions Made

*Structural decisions, character choices, argument moves, voice choices — anything the writer locked during the session.*

## Open Threads for Next Session

- [ ]
- [ ]

## Stuck flags

*Anything the writer flagged as blocked during the session.*

## Quality Gates Checklist

- [ ] Session log written (this file)
- [ ] `_state.md` updated
- [ ] Atom files touched have been saved
- [ ] Tomorrow's focus is seeded in `_state.md`
- [ ] Revision-pass log updated (if a revision pass was active)
- [ ] Sources properly referenced (if a Section was drafted with source backing)
