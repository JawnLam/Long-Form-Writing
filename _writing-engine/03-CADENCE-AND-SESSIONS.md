---
type: writing-engine
role: session-protocol
scope: subject-agnostic
updated: 2026-06-02
lfw_load:
  tier: core
  genres: [all]
  activities: [all]
  phase: bootstrap
---

# 03 — CADENCE AND SESSIONS

> **Daily-practice protocol, ten universal activities, the activity-decision algorithm, quality gates.**

## The daily-practice assumption

LFW is built for writers who work on a project across many short sessions. Not a multi-week sprint of long hours. The session protocol assumes:

- Most sessions are 15–90 minutes
- A writer may work 3–7 days a week, depending on the project and the season of life
- Re-entry after gaps (a day, a week, two weeks) is the normal case, not the exception
- Momentum across sessions matters more than heroic single-session output

This shapes everything below.

## Session lifecycle

```
1. READ writing engine + cartridge state (per 00-START-HERE.md)
2. DIAGNOSE current state (lifecycle stage, today's focus, open threads)
3. PROPOSE a session activity with rationale
4. WAIT for writer confirmation or override
5. EXECUTE the activity
6. CAPTURE atom updates, prose drafted, decisions made
7. WRITE the session log
8. UPDATE _state.md with today's progress + tomorrow's seed
```

Steps 1, 6, 7, 8 are non-negotiable. Step 5 varies by activity.

## The twenty-five universal session activities

Ten **production** activities (this chapter) plus thirteen **development** activities (six non-fiction-weighted in chapters 10-READER and 10-ARGUMENT; four fiction-weighted from v1.2 in chapters 11 + 12; three fiction-weighted from v1.3.1 in chapters 13 + 14) plus two **soft-skill** activities from v1.4.0 (chapter 16: WEATHER-CHECK, MIDDLE-AUDIT). Together they are the full session-activity set the AI can propose.

### Production activities

| Code | Activity | Right default when |
|------|----------|---------------------|
| **SESSION-START** | Re-orient after a gap; set today's focus | First session of the week, or returning after >3 days; writer signals re-entry |
| **OUTLINE** | Structural design at any scale | New cartridge in outlining stage; a section/scene lacks beats; structural revision needed |
| **DRAFT** | Generate new prose | Section/scene has beats; writer has momentum; previous session ended with explicit DRAFT-this-next |
| **REVISE** | Pass over existing prose | A specific atom is in `drafted` state; revision pass is current and not abandoned |
| **RESEARCH-INTEGRATION** | Fold sources into the manuscript | Non-fiction/dissertation; unintegrated sources exist; section needs source backing |
| **READ-THROUGH** | Higher-scale assessment than line-edit | Chapter is fully drafted; before a revision pass starts; before BETA-PREP |
| **STUCK-DIAGNOSTIC** | Structured diagnosis when blocked | Writer says "I'm stuck"; same atom has been touched 3+ sessions without progress |
| **VOICE-CHECK** | Voice-consistency pass | Voice mode is enabled AND a section has been drafted AND voice samples are recent |
| **WORLDBUILDING** | Fiction-specific setting work | Fiction cartridge; writer flagged worldbuilding gap; new setting element is referenced in scenes |
| **BETA-PREP** | Final pass before sending to beta readers | Manuscript is in `polishing` stage; writer signals readiness to send |

### Development activities — non-fiction weighted (defined in chapters 10-READER and 10-ARGUMENT)

| Code | Activity | Right default when |
|------|----------|---------------------|
| **READER-SIMULATION** | Read a drafted section as a specific Reader atom; non-fiction: resistance/lost-thread/curse-of-knowledge; fiction: dramatic-question/page-turn/sympathy/emotional-flatline (see chapter 12 §6) | Section is drafted; ≥1 Reader atom is active; the section hasn't been simulated yet |
| **ARGUMENT-AUDIT** | Pressure-test `_argument.md` — contestability, sub-claim independence, evidence sufficiency, weakest link | `_argument.md` exists and has changed; new chapter touches new sub-claims; ≥8 sessions since last audit |
| **CLAIM-EVIDENCE-CHECK** | Test whether prose claims are stronger or weaker than the cited sources actually warrant | Section is drafted with cited Sources; before accuracy revision pass |
| **STEELMAN** | Build the strongest version of a counterargument before the writer rebuts it | A Thread's counter-evidence section has un-steelmanned entries; writer is preparing to rebut |
| **SYNTHESIS-CHECK** | Flag sections that are annotated-bibliography-in-disguise — sources cited but not synthesized into the writer's argument | Section is drafted with 3+ sources cited |
| **CRAFT-REVIEW** | Read recent sessions + craft-log + craft-profile; surface recurring patterns; propose next practice focus | ≥10 sessions since last CRAFT-REVIEW; end of a chapter draft; a craft-log pattern is ready to graduate |

### Development activities — fiction weighted (defined in chapters 11 + 12; v1.2)

| Code | Activity | Right default when |
|------|----------|---------------------|
| **SCENE-AUDIT** | Value-shift diagnostic: whose want drives this scene, what's the conflict, what's different at the end vs. beginning (the load-bearing fiction craft test) | Scene is drafted; value-shift fields unpopulated or identical; 3+ scenes drafted without a SCENE-AUDIT |
| **CHARACTER-CONSISTENCY** | Does the prose deliver the Character atom's stated want, voice, and arc? + antagonist-steelman for antagonist atoms; reads Character-Bible if present *(v1.3.1)* | Character is `established` and has appeared in 3+ Scenes since last check; antagonist hasn't been steelmanned |
| **CONTINUITY-CHECK** | Verify drafted prose against `_continuity.md`: world-rules, timeline, information-state (who-knows-what) | New scene references continuity items; 10+ scenes since last check; before READ-THROUGH |
| **SETUP-PAYOFF-AUDIT** | Audit `_promises.md` against drafted manuscript: outstanding/unfired promises, unearned/unsetup payoffs | 10+ scenes drafted since last audit; before READ-THROUGH; before BETA-PREP |

### Development activities — fiction craft (defined in chapters 13 + 14; v1.3.1)

| Code | Activity | Right default when |
|------|----------|---------------------|
| **DIALOGUE-AUDIT** | Four-axis function check on drafted dialogue (plot / character / subtext / rhythm); surface zero- or one-axis lines | Scene with ≥10 dialogue lines is `drafted`; ≥5 dialogue-heavy scenes drafted without a DIALOGUE-AUDIT; writer signals "dialogue feels flat"; before BETA-PREP on a critical dialogue scene |
| **POV-VOICE-DRIFT** | Audit prose voice across alternating-POV chapters against each POV's `lfw_pov_voice_register`; surface register-bleed | 2+ POV-bearing Character atoms with `lfw_pov_voice_register` populated; ≥3 chapters drafted in each; ≥8 sessions since last drift check |
| **THEME-CHECK** | Audit Theme atoms against drafted prose; surface gaps in threading, on-the-nose treatment, motif/theme cross-references | ≥1 Theme atom is `developing` or `threaded`; ≥5 scenes drafted since last check; ≥10 sessions since last THEME-CHECK; before READ-THROUGH |

### Soft-skill activities (defined in chapter 16; v1.4.0)

| Code | Activity | Right default when |
|------|----------|---------------------|
| **WEATHER-CHECK** | Name and triage the writer's affective state (dread / doubt / grief / despair / boredom / burnout / overwhelm). Acknowledgment + diagnostic, NOT therapy or motivation. Distinct from STUCK-DIAGNOSTIC (technical) and from craft-as-procrastination (avoidance pattern). 5–15 minute activity. | Writer signals affective weather directly ("I dread / hate / am grieving / am doubting"); 2+ weeks without opening the manuscript; recurring affective comments across 3+ session logs the writer hasn't named; after a milestone (act break, midpoint, draft completion, beta feedback, rejection); after a ≥1,000-word cut; writer requests |
| **MIDDLE-AUDIT** | Seven-question structural audit at the midpoint of the manuscript; surface the failure modes specific to the middle (spine slip, want forgotten, subplot gravity, confrontation avoidance, reader-question starvation, why-drift, flat stakes) | Word count crosses 50% of target; writer reports middle dragging; ≥5 consecutive sessions of slow forward momentum during the middle; cadence has slowed ≥50% during the middle; writer requests |

## Decision algorithm

Evaluate in order. First condition that fires determines the default proposal.

### Step 1 — Hard overrides

- **If** the writer explicitly named the activity for this session → execute that
- **If** the writer named a specific atom or section → propose the appropriate activity for that atom's state (DRAFT if no prose; REVISE if drafted; OUTLINE if no beats)

### Step 2 — Stuck signal AND affective-weather signal

- **If** the writer says "stuck" or "blocked" → propose **STUCK-DIAGNOSTIC**
- **If** the most recent atoms in `_state.md` show repeated revisions with no advancement → propose **STUCK-DIAGNOSTIC**
- **If** the writer says "dread" / "grieving" / "hate this book" / "doubt" / "burned out" / "overwhelmed" / "don't know why I'm doing this" / "want to quit" → propose **WEATHER-CHECK** (v1.4.0; chapter 16)
- **If** the writer has not opened the manuscript in ≥2 weeks without an explicit pre-stated hiatus → propose **WEATHER-CHECK**
- **If** a structural signal *and* an affective signal both fire → propose **WEATHER-CHECK first** (5–15 min), then the structural activity (chapter 16 §3 — order matters; addressing affective state first protects the structural diagnostic from being received as confirmation of despair)
- **Critical:** affective weather and technical stuck are NOT the same; misdiagnosing one as the other is F54 (chapter 16). The disambiguation is the writer's call after WEATHER-CHECK Step 1's question

### Step 3 — Re-entry signal

- **If** >3 days since last session → propose **SESSION-START** (short re-orientation; sets up the real session's focus)
- **If** the writer's first message includes "where was I" or "remind me where I left off" → propose **SESSION-START**

### Step 4 — Lifecycle stage default

- **If** lifecycle stage = `outlining` → propose **OUTLINE** at the appropriate scale
- **If** lifecycle stage = `drafting` AND today's focus has beats → propose **DRAFT** on today's focus
- **If** lifecycle stage = `drafting` AND today's focus lacks beats → propose **OUTLINE** on today's focus
- **If** lifecycle stage = `revising` AND current revision pass has unfinished atoms → propose **REVISE**
- **If** lifecycle stage = `polishing` → propose **READ-THROUGH** if not done recently, else **BETA-PREP** if checklist complete
- **If** lifecycle stage = `fact-checking` (non-fiction) → propose accuracy pass (REVISE in accuracy mode)

### Step 5 — Cadence rhythms

- **If** ≥ 5 sessions of DRAFT with no READ-THROUGH → propose **READ-THROUGH**
- **If** voice mode is enabled AND a chapter has been drafted with no VOICE-CHECK → propose **VOICE-CHECK**
- **If** non-fiction with multiple Sources ingested but not folded → propose **RESEARCH-INTEGRATION**

### Step 6 — Genre-specific defaults

- **Fiction:** if worldbuilding has gaps flagged in `_state.md` → propose **WORLDBUILDING**
- **Dissertation:** if a citation in a Section atom is incomplete → propose RESEARCH-INTEGRATION (citation completion mode)

### Step 6b — Development activities (non-fiction emphasis)

For non-fiction and dissertation cartridges, evaluate these in addition to the production defaults above. They take priority *only when explicitly triggered* (the writer asks, or a hard threshold is met) — never as the silent default over a normal DRAFT session, because the production work has to land.

- **If** the writer signals stuck on the argument (not the prose) → propose **ARGUMENT-AUDIT**
- **If** `_argument.md` has changed since the last ARGUMENT-AUDIT AND ≥8 sessions have passed → propose **ARGUMENT-AUDIT**
- **If** Section is `drafted` AND active Reader atoms haven't simulated it → propose **READER-SIMULATION** (after the writer's drafting momentum is acknowledged)
- **If** Section is `drafted` AND has cited Sources AND hasn't been claim-evidence-checked → propose **CLAIM-EVIDENCE-CHECK** before accuracy pass
- **If** a Thread has un-steelmanned counter-evidence AND the writer is about to draft the rebuttal → propose **STEELMAN** first
- **If** Section has 3+ cited Sources AND high source-to-prose ratio → propose **SYNTHESIS-CHECK**
- **If** ≥10 sessions since last CRAFT-REVIEW OR chapter draft just completed → propose **CRAFT-REVIEW**

### Step 6b' — Development activities (fiction emphasis)

For fiction, screenplay, and play cartridges, evaluate these. Same triggering posture as non-fiction development activities: not silent defaults; explicit triggers only.

- **If** Scene is `drafted` AND value-shift fields are unpopulated OR identical (no turn declared) → propose **SCENE-AUDIT**
- **If** 3+ scenes have been drafted without any SCENE-AUDIT → propose **SCENE-AUDIT** on the most recent
- **If** a Character is `established` AND has appeared in 3+ drafted Scenes since last check → propose **CHARACTER-CONSISTENCY** for that Character
- **If** a Character has `lfw_role: antagonist` AND hasn't been steelmanned → propose **CHARACTER-CONSISTENCY** with antagonist-steelman sub-mode
- **If** `_continuity.md` exists AND new Scenes reference continuity items AND 10+ scenes since last check → propose **CONTINUITY-CHECK**
- **If** ≥10 scenes drafted since last SETUP-PAYOFF-AUDIT → propose **SETUP-PAYOFF-AUDIT**
- **If** the writer signals "the plot feels slack" or "I don't know why this chapter happens" → propose checking the spine; if the spine reads mostly *and then*, propose **SCENE-AUDIT** across the affected chapter
- **If** a fiction worldbuilding gap is flagged → propose **WORLDBUILDING** (generative); after the session, propose **CONTINUITY-CHECK** to verify drafted scenes against new rules
- **If** a Scene with ≥10 dialogue lines is `drafted` AND hasn't been DIALOGUE-AUDIT'd → propose **DIALOGUE-AUDIT** *(v1.3.1)*
- **If** ≥2 POV-bearing Character atoms exist with `lfw_pov_voice_register` populated AND ≥3 chapters drafted in each AND ≥8 sessions since last POV-VOICE-DRIFT → propose **POV-VOICE-DRIFT** *(v1.3.1)*
- **If** the writer signals "the dialogue is flat" or "the POVs sound alike" → propose the corresponding craft activity (DIALOGUE-AUDIT or POV-VOICE-DRIFT) even outside cadence thresholds *(v1.3.1)*
- **If** ≥1 Theme atom is `developing` or `threaded` AND ≥5 scenes drafted since last check AND ≥10 sessions since last THEME-CHECK → propose **THEME-CHECK** *(v1.3.1)*

### Step 6b''' — Middle-of-manuscript heads-up and MIDDLE-AUDIT *(v1.4.0)*

For any cartridge with `_state.md` word-count progress:

- **If** word count crosses **40% of target** for the first time → surface heads-up: *"You're approaching the middle. Consider running MIDDLE-AUDIT in the next 2–3 sessions per chapter 16 §3."* Do not impose
- **If** word count crosses **50% of target** for the first time → propose **MIDDLE-AUDIT** (writer can defer)
- **If** word count is between 40%–70% AND ≥5 consecutive sessions have shown slow forward momentum OR cadence has slowed ≥50% from normal → propose **MIDDLE-AUDIT** (the structural diagnostic; pair with WEATHER-CHECK if affective signals also present)
- **If** writer signals "the middle is dragging" / "I don't know why I'm writing this chapter" / "I've lost the thread" → propose **MIDDLE-AUDIT**

For very-long-form cartridges (200,000+ word target), MIDDLE-AUDIT may run more than once — at ~30%, ~50%, ~70%. Default is once at ~50%.

### Step 6b'' — Sub-genre-tuned defaults *(v1.3.1)*

If `lfw_fiction_subgenre` is declared in `_manuscript-manifest.md`, the cadence thresholds above shift per chapter 14 §5:

- **thriller / mystery / horror:** SETUP-PAYOFF-AUDIT triggers at ≥6 scenes (default ≥10); promises drift faster in plot-heavy work
- **romance / multi-POV literary:** POV-VOICE-DRIFT triggers at ≥6 sessions (default ≥8); register-difference is load-bearing
- **SFF / historical:** WORLDBUILDING surfaces as frequent default; CONTINUITY-CHECK runs at ≥6 scenes (default ≥10)
- **literary / speculative:** THEME-CHECK triggers at ≥6 sessions (default ≥10); theme work is high-priority

These are tunings, not new activities. The sub-genre cues live in chapter 14 §5.

### Step 6c — Scaffolding-mode awareness

If the cartridge declares `lfw_scaffolding_mode: gradual-fade` or `socratic`, the AI's proposal style changes for OUTLINE, ARGUMENT-AUDIT, STUCK-DIAGNOSTIC, SCENE-AUDIT (for fiction), and the fiction worldbuilding/continuity activities per chapter 09. Specifically:

- In `gradual-fade` mode past the relevant session threshold, the AI asks the writer to draft the structure / claim / value-shift / plot-turn / character-arc / diagnosis first, then critiques rather than proposes
- In `socratic` mode from session one, the AI never proposes a beat list, a claim, a value-shift, a character arc, a plot turn, or a counterargument — only critiques what the writer proposes

Scaffolding fade matters **more** in fiction than in non-fiction (chapter 12 §carry-over). Invention is the central fiction skill; an AI that generates the writer's plot turns and character moves doesn't make them a better novelist. Fiction cartridges should typically default to `gradual-fade` or `socratic`; `full` indefinitely is the highest-risk mode for fiction.

See chapter 09 for the full fade schedule and the rationale.

### Step 7 — Post-proposal

Present the proposal:

```
Proposed activity: <CODE> — <plain-English description>
Focus: <specific atom or scope>
Rationale: <which conditions fired>
Alternative: <next-priority activity>
Your call.
```

Wait. Do not begin until confirmation or override.

## Activity details

### SESSION-START

A short re-orientation. Aim: 5–15 minutes. The AI:

1. Re-reads cartridge state (already done in pre-flight, but explicit here)
2. Summarizes where the writer left off in 2–3 sentences
3. Surfaces today's focus from `_state.md` or proposes one based on outline + open threads
4. Asks the writer to confirm or adjust the focus
5. Hands off to the real session activity

This is the activity to default to after gaps. Writers underestimate how much re-orientation matters; this protects momentum.

### OUTLINE

Structural design. Scales:

- **Book-level:** the overall structure; usually done once at bootstrap, occasionally revisited
- **Chapter-level:** what does this chapter do? What's its scope and shape?
- **Section/Scene-level:** what beats are in this section? In what order?
- **Beat-level:** what specifically happens or is argued in this beat?

The AI's job in OUTLINE: ask questions, surface options, identify gaps, propose structures the writer can accept or reject. NOT to generate prose. Prose is for DRAFT.

### DRAFT

Generate new prose for a specific atom (usually a Section or Scene). Preconditions:

- The atom has beats (the writer has done OUTLINE on it)
- The writer has chosen DRAFT explicitly or it's the appropriate default

Voice-mode handling:

- **writer-maintains:** the AI does NOT write the prose. It probes ("what's the next beat?"), structures ("here's where I see Beat 3 fitting"), pushes back ("Beat 5 doesn't follow from Beat 4"). The writer writes the words.
- **voice-samples:** the AI may offer drafted prose for the writer to revise, modeled on the voice samples. The writer always has final word.
- **VOICE-CHECK-on-demand:** like writer-maintains during DRAFT; voice checking is a separate activity.

The AI writes the session log capturing what beats were drafted, what prose landed.

### REVISE

Pass over existing prose. The pass kind matters — see chapter 07 for the multi-pass discipline.

In a structural revision pass: the AI may suggest cutting a scene, reordering chapters, merging sections. Never silently rewrite.

In a voice pass: the AI may flag inconsistencies (only if voice mode is enabled).

In an accuracy pass (non-fiction): the AI may flag claims needing verification.

In a prose-line pass: the AI may suggest line-level changes (only if explicitly invited — most writers prefer to do line edits themselves).

### RESEARCH-INTEGRATION

Non-fiction and dissertation cartridges. See chapter 06 for the full protocol.

Short version: take a Source atom that's been ingested and fold its content into the relevant Section atoms. The fold-in protocol prevents:

- Source quotes appearing verbatim without attribution (plagiarism)
- The writer's voice being lost in long quoted passages
- Sources cited without actual relevance to the section's argument
- Fabricated citations or quotes

### READ-THROUGH

The writer reads (or has the AI read) a chapter or part at a higher scale than line-editing. The AI's job: identify structural problems, voice drift, places where the argument or plot thins, places where the writer has lost the thread.

Output: a READ-THROUGH summary in the session log. Open threads added to `_state.md` for the next revision pass.

### STUCK-DIAGNOSTIC

When the writer is blocked. The AI runs a structured diagnostic:

1. **What's the unit of stuck?** A specific section? A character? A chapter? The whole book?
2. **What did you try?** Recent attempts; what failed and why
3. **What's the avoidance?** What are you avoiding by being stuck (a hard scene? a confrontation you don't want to write? a section that requires research you haven't done?)
4. **What's the smallest possible next move?** Often 15 minutes on the smallest reasonable thing breaks the block

The AI does not provide motivational support. It does diagnostic structure.

### VOICE-CHECK

Only runs if voice mode is enabled (`writer-maintains` mode skips this activity entirely).

Reads voice samples + recently drafted prose + flags inconsistencies. Output: voice-consistency notes in the session log. Never silently changes prose.

### WORLDBUILDING

Fiction/speculative cartridges. Setting, magic systems, alternate-history rules, fictional cultures. The AI's job: ask the questions the worldbuilding doesn't yet answer; capture answers in dedicated atoms; flag contradictions across atoms.

### BETA-PREP

Last activity before sending to beta readers. The AI:

1. Runs a final READ-THROUGH at book scale
2. Identifies remaining open threads, thinness, structural worries
3. Helps the writer prepare a beta-reader brief (what to look for, what to ignore, what's intentional)
4. Updates `_state.md` lifecycle stage to `with-beta-readers`

After beta returns, the writer opens a new revision pass.

## Writing the session log

At the end of every session, create a new file in `<Cartridge>/Sessions/` named:

```
YYYY-MM-DD_NNN_<activity-code>.md
```

`NNN` is zero-padded sequential. Use `_writing-engine/_templates/TEMPLATE-Session.md`.

## Updating `_state.md`

After every session, overwrite `_state.md` with:

- Lifecycle stage (if it changed)
- Today's focus → moved to "Last completed" + tomorrow's focus seeded
- Atom status table updated for atoms touched
- Word counts updated (per chapter / section / total)
- Open Threads (close any addressed, add new)
- Stuck flags (set or cleared)

## Quality gates

Before ending any session, confirm:

- [ ] Session log written
- [ ] `_state.md` updated
- [ ] Atom files touched have been saved
- [ ] Tomorrow's focus is seeded
- [ ] If a revision pass was active, the revision-pass log has been updated
- [ ] If sources were folded in, the relevant Section atoms reference them properly

If any is no, the session is not complete.
