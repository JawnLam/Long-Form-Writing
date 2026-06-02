---
type: writing-engine
role: failure-catalog
scope: subject-agnostic
updated: 2026-06-02
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

## Adding new entries

When a new failure mode surfaces in real use, add it here with the same fields. The catalog grows; the engine references it; the failure recurs less.
