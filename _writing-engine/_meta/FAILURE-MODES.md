---
type: writing-engine
role: failure-catalog
scope: subject-agnostic
updated: 2026-06-03
schema_version: 1.3.2
---

# Failure Modes — Canonical Catalog

> **Documented failure modes that LFW sessions are known to produce. Each entry: name, trigger pattern, why it matters, fix, prevention. The AI guards against every entry actively.**

## F1 — Multi-bullet questionnaire

**Trigger:** During cartridging (BOOTSTRAP-NEW-MANUSCRIPT) or stuck-diagnostic, the AI dumps a numbered list of 5–10 questions in one message.

**Why it matters:** Bulk questions get bulk answers. The writer fills them in like a form; the AI loses the nuance from probing one answer at a time. The resulting cartridge or diagnostic is generic.

**Fix:** Stop. *"Ask one question at a time, conversationally."*

**Prevention:** `BOOTSTRAP-NEW-MANUSCRIPT.md` and `03-CADENCE-AND-SESSIONS.md` both state "one question at a time." Triple-redundant by design.

## F2 — Fabrication of sources, quotes, facts

**Trigger:** Non-fiction or dissertation cartridge. The AI cites a source you can't verify, or invents a quote, or names a historical fact that's wrong.

**Why it matters:** Trust-cost is enormous. A fabricated citation in a non-fiction manuscript can end a career if it makes it to publication. Even discovered during drafting, the trust loss reshapes the whole engagement.

**Fix:** Stop. Correct. *"From now on, if you're not sure something exists or is true, say so. Don't invent."*

**Prevention:** Chapter 06 (Research Integration) codifies the four cardinal rules: never invent a citation, never fabricate a quote, cited sources must actually support the claim, source ingestion comes before source citation.

## F3 — Identity inference from indirect signals

**Trigger:** The AI calls the writer by a name parsed from a username, file path, or git config.

**Why it matters:** This is the documented recurrence pattern from OVE's failure catalog (F3 there too). It's especially bad in LFW because the manuscript may include author bio / acknowledgments where a wrong name lands in shippable artifacts.

**Fix:** Use a placeholder until the writer provides their name explicitly.

**Prevention:** Treated as a load-bearing rule in `00-START-HERE.md`.

## F-VOICE — AI homogenization of voice

**Trigger:** Voice mode is `voice-samples` or the writer asked for drafted prose. The AI produces generic AI prose that sounds nothing like the writer's voice.

**Why it matters:** This is the single most damaging failure in writing OVs. Generic AI prose is recognizable. A manuscript that's drifted into AI-voice doesn't sound like its author anymore — and most writers don't realize it's happening until much later.

**Fix:** Stop. If in `voice-samples` mode, check the samples: are they substantial (300+ words each), varied, recent, the writer's unaided work? If samples are thin, the AI can't calibrate. Switch to `writer-maintains` mode or improve the samples.

**Prevention:** Default voice mode is `writer-maintains` — AI does not attempt voice match. Writer opts in explicitly to other modes. See chapter 05.

## F8 — Drafting before outlining

**Trigger:** Writer asks the AI to draft a section that has no beats. AI starts generating prose.

**Why it matters:** Prose for a section without beats is structureless. Either it forces the writer into a structure the AI invented (homogenization), or it gets discarded and revision time is wasted.

**Fix:** Stop. *"This section doesn't have beats. OUTLINE first."* The DRAFT activity preconditions list this explicitly.

**Prevention:** `03-CADENCE-AND-SESSIONS.md` orders activities: OUTLINE before DRAFT. The decision algorithm enforces this — if today's focus has no beats, the proposal is OUTLINE, not DRAFT.

## F9 — Abandoned revision pass

**Trigger:** Writer starts a revision pass (structural, voice, accuracy, or prose-line) but never marks it `completed`. Months later, multiple passes are simultaneously in `in-progress` state.

**Why it matters:** Revision passes that lose discipline produce confused, partly-revised manuscripts. The writer can't tell what's been revised and what hasn't.

**Fix:** Open the revision-pass log. For each `in-progress` pass: either resume and complete, or mark as `aborted` with a note. Don't leave them dangling.

**Prevention:** Chapter 07 makes pass scope and completion explicit. The session protocol checks for in-progress passes at session start.

## F10 — Endless revision

**Trigger:** Same chapter has 4+ revision passes and still isn't marked `final`. The writer keeps revising and the manuscript isn't getting measurably better.

**Why it matters:** Some manuscripts never ship because their writer can't stop revising. The honest definition of done (chapter 08) gets ignored.

**Fix:** The AI surfaces the pattern. The writer answers honestly: more revision needed, or time to ship? Connected to STUCK-DIAGNOSTIC.

**Prevention:** Chapter 07 (revision discipline) + chapter 08 (finishing) + STUCK-DIAGNOSTIC activity.

## F11 — Research as procrastination

**Trigger:** Non-fiction / dissertation cartridge. Writer spends 5+ consecutive sessions in RESEARCH-INTEGRATION with no DRAFT activity. Source library grows; manuscript doesn't.

**Why it matters:** Research is a real activity. It's also a real way to avoid the harder work of drafting. The OV's job is to make the choice visible.

**Fix:** AI surfaces the pattern: *"You've been integrating sources for several sessions without drafting. Is this the right activity, or are you avoiding the drafting?"* Writer answers honestly.

**Prevention:** Chapter 06 documents this anti-pattern explicitly.

## F12 — Engine drift into manuscript specifics

**Trigger:** Writing an engine chapter, the AI inserts a manuscript-specific example as if it were canonical. *"For your novel about three sisters…"*

**Why it matters:** Engine files must be subject-agnostic. Domain bleed pollutes the engine and makes the OV harder to reuse.

**Fix:** Refactor. Move manuscript-specific guidance to the cartridge.

**Prevention:** Engine examples come from the shipped worked example (which is clearly hypothetical) or are explicitly framed as "*for example*" rather than canonical.

## F13 — Sandbox mode misuse

**Trigger:** In a sandbox environment (no file writes), the AI keeps acting as if state is being saved.

**Why it matters:** State is lost at session end. Writer thinks work is saved; it isn't. Sessions of writing evaporate.

**Fix:** At Phase 0 pre-flight, detect read-only mode. Declare sandbox mode explicitly. Tell the writer their drafts won't persist; suggest copying out at session end.

**Prevention:** Phase 0 environment checks in `AI-BOOTSTRAP.md`.

## F14 — Writer's name in cartridge before opt-in

**Trigger:** The cartridge's manifest or manuscript references the writer by name before the writer has provided it.

**Why it matters:** Connected to F3. If the manuscript header says "by John Doe" because the AI inferred, that's bad. The author's actual name belongs only after operator confirmation.

**Fix:** Replace with placeholder. Wait for the writer to provide.

**Prevention:** `00-START-HERE.md` codifies the rule; `BOOTSTRAP-NEW-MANUSCRIPT.md` asks for the name explicitly in CQ11 if it hasn't come up.

## F15 — Voice mode flipped silently

**Trigger:** Cartridge starts in `writer-maintains` voice mode; mid-cartridge the AI starts offering drafted prose as if voice-samples mode were enabled.

**Why it matters:** The writer's expectations don't match the AI's behavior. Subtle homogenization can happen before either party notices.

**Fix:** Re-read the manifest's voice mode every session start. Honor it strictly. If the writer wants to change voice modes, they update the manifest explicitly.

**Prevention:** Voice mode is read in the mandatory read order at session start.

## F16 — Beta-prep submitted before honest-thinness audit

**Trigger:** Writer asks the AI to send to beta readers without running an honest-thinness audit first.

**Why it matters:** Beta readers see thin spots the writer hasn't yet addressed. The feedback is less useful (lots of "this section needs work" that the writer already knew). The writer's beta capital is finite.

**Fix:** Propose the audit before BETA-PREP. *"Before sending, let's run the honest-thinness audit so the brief can flag what's intentional vs. what's still in progress."*

**Prevention:** Chapter 08 sequences the audit before BETA-PREP.

## F17 — Multi-cartridge confusion

**Trigger:** Writer has multiple cartridges open. Session starts on the wrong one because the AI didn't ask which.

**Why it matters:** Wrong session log written to wrong cartridge. State updates land on the wrong manuscript. Real work goes into the wrong file.

**Fix:** Phase 0 pre-flight lists all cartridges and asks the writer to confirm which one is active.

**Prevention:** `AI-BOOTSTRAP.md` Phase 0.3 requires identifying the active cartridge.

## F18 — Craft work as procrastination

**Trigger:** Development activities (ARGUMENT-AUDIT, CRAFT-REVIEW, STEELMAN, READER-SIMULATION, etc.) dominate 5+ consecutive sessions with no DRAFT or REVISE-on-existing-prose. Structurally identical to F11 (research as procrastination).

**Why it matters:** The blank page is the actual work. Craft-development is real but it's also an extremely comfortable place to hide. A writer can spend three months auditing their argument and reading source material without producing any prose, and the OV will dutifully record those sessions as productive.

**Fix:** AI surfaces the pattern: *"You've been doing development work for several sessions without producing or revising prose. Is this the right rhythm right now, or is this craft-as-avoidance? Either answer is fine; I want it to be the answer you'd give if asked."* Writer answers honestly.

**Prevention:** Chapter 09 documents this anti-pattern explicitly and tasks the AI with watching for it. Connected to F11 (research as procrastination) — same root pattern, different surface.

## F19 — Scaffolding never fades

**Trigger:** Cartridge declares `lfw_scaffolding_mode: gradual-fade` but the AI keeps proposing structure / claims / counterarguments past the session-count thresholds documented in chapter 09. The writer never develops independent structural intuition.

**Why it matters:** The scaffolding fade is the mechanism by which the OV makes itself less needed over time. If the AI silently ignores the mode, the writer remains dependent indefinitely and the development goal fails.

**Fix:** AI checks `lfw_scaffolding_mode` at session start (it's in the mandatory read order via `_manuscript-manifest.md`) and the current session count. If past the relevant threshold, AI asks the writer to draft structure/claim/diagnosis first, then critiques rather than proposes.

**Prevention:** Chapter 09 spells out the fade schedule; chapter 03 documents the scaffolding-mode-awareness step in the decision algorithm.

## F20 — Skill scoring attempted

**Trigger:** AI tries to assign numeric ratings to the writer's craft ("Voice: 7/10"; "Argument: B+"). Or `_craft-profile.md` starts accumulating skill-tree-style level numbers.

**Why it matters:** Writing skill does not quantify cleanly. A number is either wrong (no one knows what the units are) or corrosive (the writer games it or feels graded). The craft-profile's value is observational specificity — concrete patterns, cited instances — not measurement.

**Fix:** Stop. Re-read chapter 09's first caution. Replace any scores with pattern descriptions + concrete examples.

**Prevention:** Chapter 09's "skill model is observational, not scored" caution. The craft-profile template has no numeric fields.

## F21 — Reader atoms used to flatter the writer

**Trigger:** Writer creates Reader atoms whose "what they reward" sections are tightly aligned with the writer's existing voice and the "what they punish" sections are empty or perfunctory. READER-SIMULATION sessions then produce only positive reports.

**Why it matters:** The Reader's value is that they're *not* the writer. A Reader who agrees with everything the writer wrote is a mirror, not a reader. The Skeptic exists precisely to resist; if she resists nothing, she's malfunctioning.

**Fix:** During Reader-atom creation (cartridging or whenever a new Reader is added), the AI tests the Reader against the writer's existing drafted prose: does this Reader actually push back somewhere? If no, the Reader is incompletely modeled. Revise the Reader's "where they resist" section.

**Prevention:** READER-SIMULATION reports must surface at least one resistance point or one curse-of-knowledge instance, or the AI flags that the Reader may be misconfigured.

## F22 — Scene doesn't turn *(v1.2 — fiction)*

**Trigger:** A Scene atom is at `drafted` status. Its `lfw_value_shift_from` and `lfw_value_shift_to` fields are identical (or both empty). The scene has setting, stakes, and stated purpose but nothing changes — the character ends where they began.

**Why it matters:** No-turn scenes are the single most common structural flaw in fiction drafts. A novel where most scenes don't turn reads as sequence rather than story, regardless of how interesting each scene is in isolation.

**Fix:** Run SCENE-AUDIT (chapter 11 §2). State the start-state and end-state. If genuinely identical, the scene needs revising, cutting, merging, or repurposing. Sometimes a no-turn scene works (mood pieces, quiet beats); usually it doesn't.

**Prevention:** SCENE-AUDIT triggers automatically after 3+ scenes drafted without an audit. The Scene template's required `## Value-shift` body section forces the writer to declare the turn before marking `drafted`.

## F23 — Promise unfired or unearned *(v1.2 — fiction)*

**Trigger:** Two halves of the same failure. (a) A setup planted in chapter 2 (recorded as a `prefigures` relation) has no corresponding payoff visible — the unfired Chekhov's gun. (b) A reveal or payoff in chapter 18 has no setup in earlier chapters — the unearned payoff.

**Why it matters:** Reader satisfaction in fiction depends significantly on promises being kept. An unfired promise reads as the author having lost track of their own setup; an unearned payoff reads as arbitrary plot mechanics.

**Fix:** Run SETUP-PAYOFF-AUDIT (chapter 11 §4). The audit categorizes promises as unfired-long-outstanding, unearned-recently-fired, unsetup-recently-delivered, or healthy.

**Prevention:** `_promises.md` ledger; `prefigures` relation used as discipline; SETUP-PAYOFF-AUDIT triggered every ~10 scenes drafted and before READ-THROUGH.

## F24 — Character bible disconnected from the prose *(v1.2 — fiction)*

**Trigger:** A Character atom has a developed arc, voice, and relationships. The drafted scenes featuring the character don't deliver the stated want, drift away from the stated voice, or claim arc changes the prose doesn't dramatize.

**Why it matters:** A novel can have gorgeous Character atoms and flat characters in the actual chapters. The writer reads the atom, feels the character is well-developed, then writes scenes that don't bear that development out. The reader experiences flatness.

**Fix:** Run CHARACTER-CONSISTENCY (chapter 12 §1). Either the Character atom needs updating or the prose needs revising. The AI surfaces; the writer judges which side is right.

**Prevention:** CHARACTER-CONSISTENCY triggers when a Character is `established` and has appeared in 3+ Scenes since the last check.

## F25 — Arc asserted, not earned *(v1.2 — fiction)*

**Trigger:** Prose claims a character change ("she finally understood," "he stopped fighting it") without dramatizing the steps that produce the change.

**Why it matters:** The single most common character-level fiction failure after no-turn scenes. The writer feels the change (they know the character's internal arc) but the reader doesn't see the steps. The reader experiences the change as told, not earned.

**Fix:** Surface during CHARACTER-CONSISTENCY. Writer either dramatizes the missing steps or recognizes the change isn't warranted.

**Prevention:** CHARACTER-CONSISTENCY watches for asserted-change language patterns.

## F26 — Antagonist weak, unflagged *(v1.2 — fiction)*

**Trigger:** The antagonist's want is flimsier than the protagonist's; opposition is plot-mechanical rather than character-driven; the antagonist's atom has weak content (or doesn't exist).

**Why it matters:** Weak opposition is the most reliable cause of weak fiction. A protagonist whose obstacles aren't legitimate-from-the-antagonist's-frame produces a story without genuine tension.

**Fix:** Run CHARACTER-CONSISTENCY with antagonist-steelman sub-mode (chapter 12 §1). The AI builds the strongest version of the antagonist's position; if a sophisticated reader wouldn't find the want legitimate within the character's own frame, the antagonist needs more development.

**Prevention:** CHARACTER-CONSISTENCY automatically runs antagonist-steelman for any Character with `lfw_role: antagonist`.

## F27 — Motif stated, not woven *(v1.2 — fiction)*

**Trigger:** A Motif atom exists with developed body sections; its `## Where it appears` lists only 1–2 scenes across a 60,000+ word manuscript. The motif is declared but not built.

**Why it matters:** Theme that's stated is a lecture; theme that's woven is craft. A motif that appears twice in a novel is a recurring detail, not a motif.

**Fix:** Surface during CRAFT-REVIEW or READ-THROUGH. Writer either weaves the motif into more scenes or retires it.

**Prevention:** Motif atoms with `lfw_status: woven` but fewer than ~4 scene appearances get flagged. The writer's `## Risk of over-use` self-awareness is the other guardrail.

## F28 — Continuity drift *(v1.2 — fiction)*

**Trigger:** A drafted Scene contradicts a world-rule established earlier, breaks the timeline, or has a character act on information they shouldn't have yet (or fail to act on information they should have).

**Why it matters:** Continuity errors break the reader's immersion immediately. Information-state errors specifically destroy plot mechanics — the reader can't follow a mystery whose clues drift in inconsistent direction.

**Fix:** Run CONTINUITY-CHECK (chapter 12 §4). Writer decides whether to revise the scene, revise the rule, or recognize the apparent inconsistency as intentional.

**Prevention:** `_continuity.md` ledger; CONTINUITY-CHECK every ~10 scenes drafted; required after WORLDBUILDING when new rules are added.

## F29 — POV pane of glass *(v1.2 — fiction; opt-in)*

**Trigger:** A scene's prose is dense with filter words (*she saw, he felt, she noticed*) that put a pane of glass between the reader and the experience. Or POV switches mid-scene unintentionally.

**Why it matters:** Filter words distance the reader from immersion in ways the writer rarely notices. They're voice-load-bearing in some cases (when the act of noticing IS the point) and craft tells in most others.

**Fix:** Run the `pov-and-psychic-distance` craft module (chapter 12 §7). The module flags candidates; the writer decides which are intentional.

**Prevention:** Opt-in only — never silently enforced.

## F30 — Head-hop within scene *(v1.2 — fiction)*

**Trigger:** Within a single scene, the POV character switches without deliberate cause. Mid-scene drift from the `lfw_pov` field's declared POV.

**Why it matters:** Head-hopping inside a scene disorients the reader and is almost always unintentional. Omniscient narration handles this deliberately; close-third and first-person scenes shouldn't.

**Fix:** Surface via the `pov-and-psychic-distance` craft module or during a dedicated REVISE pass.

**Prevention:** The Scene's `lfw_pov` field declares the intended POV; mid-scene drift from that POV is the flag.

## F31 — Dialogue as information dump *(v1.3.1 — fiction)*

**Trigger:** A stretch of dialogue lines that score only on the Plot axis (chapter 13 §1's four-axis check). Lines deliver information or advance state; none reveal character, carry subtext, or vary rhythm.

**Why it matters:** Reader experiences as exposition in conversational clothing. Common in genre fiction's "as you know, Bob" passages and in expository scenes where the writer is solving plot rather than dramatizing it.

**Fix:** DIALOGUE-AUDIT surfaces specific lines. Revise toward 2+ axis coverage: make the information-delivery reveal character; add the subtext gap; vary the rhythm.

**Prevention:** DIALOGUE-AUDIT activity (chapter 13 §3) on any drafted scene with ≥10 dialogue lines.

## F32 — Interchangeable dialogue *(v1.3.1 — fiction)*

**Trigger:** Lines that score zero on the Character axis — any character could say them. The Character atom's dialogue tells (chapter 13 §1) are not internalized in the prose.

**Why it matters:** Reader cannot identify who is speaking without the dialogue tags; characters reduce to plot-functions; the novel feels populated by interchangeable mouthpieces.

**Fix:** Re-read the Character atom's dialogue-tells section before revising. Rewrite the lines in question with the speaker's specific tells.

**Prevention:** DIALOGUE-AUDIT cross-references each line against the speaking Character's dialogue tells. Character atoms with thin dialogue-tells sections are themselves a flag.

## F33 — On-the-nose subtext *(v1.3.1 — fiction)*

**Trigger:** Characters explain their feelings; the gap between surface and meaning collapses; declared subtext (in Beat atom) is spelled out in the prose.

**Why it matters:** Reader has nothing to do. The pleasure of dialogue-craft is registering the gap between line and meaning; collapsing the gap removes that pleasure and the work that subtext does to characterize.

**Fix:** Identify the line carrying the on-the-nose moment. Rewrite so the meaning is implied by what the character *doesn't* say, or by an action-beat, or by a non-sequitur.

**Prevention:** Beat atoms with a Subtext body section (chapter 13 §1) make the gap auditable. DIALOGUE-AUDIT flags surface dialogue that doesn't carry declared subtext.

## F34 — POV-voice bleed *(v1.3.1 — fiction)*

**Trigger:** In multi-POV fiction, one POV's chapter sounds like another POV's chapter. Reader cannot identify whose POV they are inside by the second sentence.

**Why it matters:** The whole point of alternating POV is the perceptual experience of being inside different consciousnesses. Register-bleed flattens this into single-voice narration with POV-labels.

**Fix:** POV-VOICE-DRIFT activity (chapter 13 §2) surfaces specific drift instances. Per-POV revision with the Character atom's `lfw_pov_voice_register` open as a reference.

**Prevention:** `lfw_pov_voice_register` populated for every POV-bearing Character atom; POV-VOICE-DRIFT every ~8 sessions for multi-POV cartridges; optional per-POV voice samples.

## F35 — Show-everything pathology *(v1.3.1 — fiction)*

**Trigger:** The opposite of F22 (asserted-not-shown). Writer dramatizes everything, including routine transitions; never tells; the prose runs at uniform high-intensity; pacing collapses.

**Why it matters:** Show-don't-tell weaponized as a rule produces exhausting prose. The reader needs respite; the form requires summary at non-load-bearing moments.

**Fix:** Identify the routine transitions; rewrite as summary. Reserve dramatization for moments that are actually load-bearing for character, plot, or emotional weight.

**Prevention:** The `show-dont-tell` craft module (chapter 13 §4) flags over-dramatized routine transitions when active.

## F36 — Style-sheet drift in dialogue formatting *(v1.3.1 — fiction)*

**Trigger:** Said-vs-action-beat, em-dash-vs-ellipsis, italics-vs-no-marker for inner dialogue — inconsistent across chapters. Reads as inattention.

**Why it matters:** Dialogue formatting is a small problem that signals a large failure of attention. Editors and agents notice; readers feel it before they can name it.

**Fix:** State the choices once in the manifest (or in `_style-sheet.md` v1.3.2 when shipped). Honor them. Audit during BETA-PREP.

**Prevention:** v1.3.2 will ship `_style-sheet.md`; for v1.3.1, state choices in manifest voice notes and check during BETA-PREP READ-THROUGH.

## F37 — AI homogenizes POV voices *(v1.3.1 — fiction)*

**Trigger:** AI offers revision suggestions that smooth both POVs toward a single register. AI's "improvement" reduces register-difference.

**Why it matters:** The AI's job in multi-POV work is to *preserve* difference, not to harmonize. F34's flip side: the writer maintained difference; the AI ironed it out.

**Fix:** Stop accepting AI's smoothing revisions. Re-affirm `writer-maintains` voice mode. If AI must surface revisions, they must respect each POV's `lfw_pov_voice_register`.

**Prevention:** Voice mode `writer-maintains` (default); POV-VOICE-DRIFT activity rejects AI revisions that reduce register-distance.

## F38 — Missing sequels in literary fiction *(v1.3.1 — fiction)*

**Trigger:** Every scene is a value-shifting scene; no reactive beats; reader has no room to feel the turns. The novel reads as relentless.

**Why it matters:** Literary fiction often does its most powerful work in the sequel-beats — the silent walk home, the conversation that doesn't happen, the moment alone afterwards. Omitting them collapses the form's emotional weight.

**Fix:** Identify chapters that read as relentless. Tag specific scenes as `lfw_scene_type: sequel` and develop their reaction-dilemma-decision structure. Often the writer has been writing sequels implicitly and just hasn't named them.

**Prevention:** SCENE-AUDIT now considers scene-type (chapter 14 §1); literary-subgenre cartridges' decision algorithm surfaces sequel-density as a check.

## F39 — Over-sequel'd thriller *(v1.3.1 — fiction)*

**Trigger:** Every action scene is followed by extended interiority; pacing collapses; the form's grammar (escalation, momentum, dramatic compression) is violated.

**Why it matters:** Thriller readers register slow pacing as form-violation. The interior beats that work in literary fiction kill thriller momentum.

**Fix:** Compress sequel-beats to a paragraph or skip them entirely between high-tension scenes. Sub-genre tuning (chapter 03 §6b'') should already have flagged this.

**Prevention:** Sub-genre field (thriller / mystery / horror) tunes the SCENE-AUDIT defaults to expect compressed sequels.

## F40 — Sequel without decision *(v1.3.1 — fiction)*

**Trigger:** A `lfw_scene_type: sequel` atom that processes the prior scene's outcome but produces no decision (no new want for the next scene). The chain breaks.

**Why it matters:** The sequel's job is to produce the next scene's want. Sequels that only react and dwell leave the reader without forward motion.

**Fix:** Identify the decision the sequel must produce. Often the writer wrote the reaction and the dilemma but skipped the decision because it felt premature; the answer is to commit the character to a specific next-step want even if the next step is small.

**Prevention:** The Sequel body section's Decision sub-section is required for sequel-typed scenes at SCENE-AUDIT.

## F41 — Overlay as formula *(v1.3.1 — fiction)*

**Trigger:** Beat-sheet overlay (Save the Cat / Hero's Journey / Story Circle / Freytag) treated as a writing prescription rather than a diagnostic lens. Story contorts to hit beats at their expected percentages.

**Why it matters:** Overlay-as-formula produces predictable, hollow fiction. The most-weaponized version is Save the Cat for screenplays/commercial fiction; the failure mode is genre-agnostic.

**Fix:** Walk away from the overlay. Treat it as one possible reading lens, not the writing prescription. Beats that don't fit are not necessarily defects.

**Prevention:** Overlay templates explicitly state the risk and the divergence-notes section (chapter 14 §2).

## F42 — On-the-nose theme *(v1.3.1 — fiction)*

**Trigger:** Theme stated by a character or by narration as the novel's thesis. The reader is left no work.

**Why it matters:** Theme is what's carried, not what's declared. A novel that names its theme reduces to allegory or sermon — both inferior to the novel that lets the theme emerge.

**Fix:** Identify the on-the-nose statement(s). Rewrite to carry the theme by mechanism (character choice, motif recurrence, dramatic question) rather than by declaration.

**Prevention:** THEME-CHECK activity (chapter 14 §4); Theme atom's "What it must NOT do" section.

## F43 — Character-bible as procrastination *(v1.3.1 — fiction)*

**Trigger:** Writer expands the Character-Bible indefinitely as avoidance of drafting. Same anti-pattern as research-as-procrastination (F11) and craft-work-as-procrastination (F18).

**Why it matters:** Bibles serve drafting. Bibles that grow indefinitely without prose advancing are the bible-equivalent of perpetual outlining.

**Fix:** Suspend bible work; draft for several sessions; return to the bible only to update for things prose revealed.

**Prevention:** Same diagnostic posture as F18; the AI asks the avoidance-vs-need question when bible sessions dominate.

## F44 — Sub-genre miscalibration *(v1.3.1 — fiction)*

**Trigger:** Cartridge declares a sub-genre whose conventions don't match what's actually being written; activity defaults misfire (e.g., thriller-tuned SETUP-PAYOFF-AUDIT triggers too aggressively for a literary novel mis-tagged as thriller).

**Why it matters:** The activity-decision algorithm assumes the sub-genre tag is accurate. Misfiring activities waste sessions and surface false flags.

**Fix:** Update the manifest. Re-tag the sub-genre. Reset cadence thresholds.

**Prevention:** BOOTSTRAP asks for the sub-genre with examples; the writer revisits the field at the first CRAFT-REVIEW.

## F45 — Worldbuilding as procrastination *(v1.3.2 — fiction)*

**Trigger:** SFF / fantasy / speculative cartridge. The writer expands `_worldbuilding.md` indefinitely as avoidance of drafting. The world grows; the manuscript doesn't.

**Why it matters:** Worlds serve stories. A perfectly built world without a written novel is the same anti-pattern as research-as-procrastination (F11), craft-work-as-procrastination (F18), and character-bible-as-procrastination (F43).

**Fix:** Suspend worldbuilding sessions; draft for several sessions; return to worldbuilding only to fill gaps the prose surfaces.

**Prevention:** Same diagnostic posture as F11 / F18 / F43. The AI asks the avoidance-vs-need question when worldbuilding sessions dominate.

## F46 — Timeline layers conflated *(v1.3.2 — fiction)*

**Trigger:** Story-time, world-history, and character-specific events tracked in a single timeline document; layers contaminate; events drift to wrong layer; reconciliation becomes impossible.

**Why it matters:** The whole point of multi-layer Timeline atoms is layer-isolation so each layer can be the source-of-truth for its scope. Conflation collapses the structural advantage.

**Fix:** Split the conflated timeline into per-layer Timeline atoms. Reconcile in `_continuity.md`.

**Prevention:** Validator check 12 requires `lfw_timeline_layer` to be declared; chapter 15 §2 documents the layer discipline.

## F47 — Storyboard stale *(v1.3.2 — fiction)*

**Trigger:** Storyboard not updated after scene revisions; produces false picture; worse than no storyboard.

**Why it matters:** A stale storyboard misleads the writer about the manuscript's shape. Decisions made on stale data are decisions made on lies.

**Fix:** Update the storyboard from current Scene atoms. Mark stale state explicitly (date the file).

**Prevention:** Update the storyboard at session-end whenever a Scene atom was created or substantially revised. Do not let staleness exceed two sessions.

## F48 — Style-sheet drift *(v1.3.2 — fiction)*

**Trigger:** Spelling, capitalization, italics, punctuation conventions drift across chapters. The style sheet declares one convention; the prose uses another.

**Why it matters:** Drift reads as inattention. Editors and agents notice within the first chapter. Readers feel it before they can name it.

**Fix:** Pick a convention. State it once in `_style-sheet.md`. Honor it. Catch drift during line-edit REVISE pass and BETA-PREP.

**Prevention:** `_style-sheet.md` consulted at BETA-PREP and at line-edit REVISE; documented choices once eliminate re-derivation drift.

## F49 — Inspiration becomes citation *(v1.3.2 — fiction)*

**Trigger:** Writer treats Inspiration atoms with Source-discipline rigor (full citations, quote-tracking, fold-in protocol); OR treats Source atoms with Inspiration-compost looseness (no citation, no fact-check).

**Why it matters:** Each discipline is wrong-shaped for the other artifact. Source's discipline guards against non-fiction fabrication (F2); Inspiration's looseness allows fiction's research to remain compost. Confusing them either bloats the fiction process with non-fiction overhead or strips the non-fiction process of its anti-fabrication discipline.

**Fix:** Re-classify atoms per their actual function — to-be-cited (Source) vs to-be-absorbed (Inspiration).

**Prevention:** Chapter 15 §5's Source-vs-Inspiration distinction; BOOTSTRAP guidance on which to use.

## F50 — Relationship map disconnected from prose *(v1.3.2 — fiction)*

**Trigger:** `_relationships.md` is updated diligently with relationship arcs and subtext patterns; the drafted prose doesn't reflect them.

**Why it matters:** A relationship map that doesn't track the prose is the relational equivalent of a bible disconnected from the prose (F24). The map becomes aspirational fiction *about* the manuscript.

**Fix:** CHARACTER-CONSISTENCY activity surfaces the disconnect. Either update the map to match what the prose is actually doing, or revise prose to honor the map.

**Prevention:** Update `_relationships.md` after each CHARACTER-CONSISTENCY session that touches relationships.

## F51 — Flat stakes *(v1.3.2 — fiction)*

**Trigger:** Stakes operate at the same level across the manuscript; nothing escalates. The Stakes-ladder section in `_spine.md` (v1.3.2) makes this visible at a glance.

**Why it matters:** A novel without escalating stakes reads as static even if individual scenes turn. The reader registers the absence of momentum even when prose is competent.

**Fix:** Identify chapters where stakes are not escalating. Decide what new level needs to be engaged (relational → societal? Personal → existential?). Revise to land the escalation.

**Prevention:** SCENE-AUDIT and READ-THROUGH now consult the Stakes-ladder. Inverted-pyramid risk (existential too early) is also surfaced by the ladder.

## Adding new entries

When a new failure mode surfaces in real use, add it here with the same fields. The catalog grows; the engine references it; the failure recurs less.
