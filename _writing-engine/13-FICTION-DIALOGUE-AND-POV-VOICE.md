---
type: writing-engine
role: fiction-craft-deepening
scope: fiction
updated: 2026-06-03
lfw_load:
  tier: pack
  genres: [fiction, screenplay, play]
  activities: [DIALOGUE-AUDIT, POV-VOICE-DRIFT, REVISE]
  phase: on-demand
---

# 13 — FICTION: DIALOGUE AND POV-VOICE

> **The craft-level chapter. v1.0 covered Scene and Character as containers. v1.2 covered the causal spine, motifs, continuity. v1.3.1 covers the line-level skills inside the container: how characters speak, how POVs sound different from each other, and how prose dramatizes rather than asserts. Three places fiction writers most often feel under-served by structural tools.**

## What this chapter adds

- **Dialogue craft** — subtext, function, characteristic speech, scene-level dialogue purpose
- **POV-voice differentiation** — alternating-POV is increasingly common; v1.2 had no tooling to keep Maya from sounding like Sarah
- **Show-don't-tell** — the most universally important craft module fiction needed; v1.2 named it as an error vocabulary item but didn't ship the module
- **Two new activities** — DIALOGUE-AUDIT and POV-VOICE-DRIFT
- **Per-POV voice samples** — optional `<Cartridge>/_voice-samples-{pov-slug}.md` backbone files for cartridges with multi-POV register-differentiation work
- **One updated Character field** — `lfw_pov_voice_register` for POV-bearing Character atoms

## §1 — Dialogue craft

Dialogue is the densest fiction-craft surface. Almost every line of dialogue does at least three things at once: it advances or evades plot, it reveals or conceals character, and it manages the reader's relationship to the present moment. v1.0 / v1.2 had no apparatus for any of these. v1.3.1 adds the apparatus.

### Four-axis dialogue function

Every drafted line of dialogue can be checked against four axes. Not every line scores on every axis; problems emerge when *no* line in a section scores on more than one.

| Axis | Question | Failure mode if line doesn't score |
|------|----------|------------------------------------|
| **Plot** | Does this line move the scene's plot forward — change a state, force a decision, deliver information, escalate stakes? | Line is conversational filler |
| **Character** | Does this line reveal something about the speaker (or, by implication, the listener)? | Line is interchangeable — any character could say it |
| **Subtext** | Is the character saying something other than what they mean? Is there a gap between the spoken and the meant? | Line is on-the-nose; characters explain their feelings |
| **Rhythm** | Does this line carry the scene's cadence — short for tension, longer for unguarded, fragmentary for interrupted, formal for distance? | Line is rhythmically inert |

A well-crafted scene of dialogue has most lines scoring on 2+ axes. Lines that score on only Plot are *information dumps in conversational clothing.* Lines that score only on Character are *demonstration.* Lines that score only on Subtext are *meaningfulness without weight.* The four-axis check is the basis of **DIALOGUE-AUDIT** (§3 below).

### Characteristic speech: the dialogue tell

Each major character has a set of characteristic speech-markers — verbal tics, sentence-shape preferences, vocabulary range, the way they handle interruption, what they say when they don't know what to say. These are the **dialogue tells**.

Character atoms in v1.0 had a Voice and prose register section; v1.3.1 formalizes a sub-section explicitly for dialogue:

```markdown
## Voice and prose register

### Narrative voice (close-third interiority, if POV)
*Sentence shape, diction, habits of mind...*

### Dialogue tells *(v1.3.1)*
- **Sentence shape:** *(short / long / fragmentary / cadenced)*
- **Diction range:** *(plain / mixed / formal / register-shifting by company)*
- **Pet phrases:** *(specific phrases this character uses)*
- **Verbal tics:** *(unnameable habits — pauses, repetitions, the way they say someone's name)*
- **What they say when they don't know what to say:** *(the placeholder — "I see" / "okay" / silence / a non-sequitur)*
- **What they say when they're lying:** *(the tell — over-precision, deflection, asking back, going short)*
- **What they say under pressure:** *(register collapse or register escalation; word-count change)*
```

Maya's Character atom in The Late Frost has *"all right"* as a sentence-mode at moments of decision, *"I see"* as a placeholder when she doesn't yet see. Sarah's atom has *"okay"* as a one-word agreement that means *I have heard you and have not yet agreed*. Both characters' dialogue should be testable against their tells in DIALOGUE-AUDIT.

### Subtext: the gap between line and meaning

Subtext is the central craft of dialogue in literary fiction and the load-bearing technique in mystery, thriller, and romance. The character is saying X; what they mean is Y. The reader registers the gap and is held by it.

Beat atoms in v1.3.1 may include an optional Subtext field for beats where dialogue carries the load:

```markdown
## Subtext *(v1.3.1, optional)*

- **Surface:** *(what is said)*
- **Underneath:** *(what is meant)*
- **What the listener registers:** *(what the OTHER character hears in the gap, or doesn't)*
- **What the reader registers:** *(reader's awareness; may differ from listener's)*
```

The Beat atom's subtext field is the per-beat receipt for the writer's intentionality. Not every beat needs one. Beats where dialogue is doing critical work — confrontation, seduction, manipulation, evasion, half-confession — should.

### Dialogue formatting conventions (style sheet anchor)

For cartridges that ship a style sheet (v1.3.2), dialogue conventions live there. For v1.3.1: the cartridge should at least state, in `_manuscript-manifest.md` voice notes or in a craft-log entry:

- **Tags:** said-only? mixed? action-beats over tags?
- **Adverbs in tags:** allowed / disallowed
- **Em-dash / ellipsis:** interruption convention vs trail-off convention
- **Foreign-language quoted material:** italics / not-italics / Romanized
- **Inner dialogue:** italics / no marker / scare-quote
- **Dialect:** how is non-standard speech rendered; what is being avoided

State the choices once; honor them. Drift on dialogue formatting is a small problem that reads as a large failure of attention.

## §2 — POV-voice differentiation

In a multi-POV novel, the prose voice — not just the dialogue — should differ across POVs. The reader should be able to identify which POV they are inside by the second sentence of a chapter. If they cannot, the POV is doing less than its name promises.

v1.2's Character atom captured voice in narrative interiority. v1.3.1 adds a frontmatter field that makes the POV-register *queryable*:

```yaml
lfw_pov_voice_register:        # v1.3.1 — required for POV-bearing Character atoms
  sentence_length: ""          # "short" / "long" / "cadenced" / "fragmentary" / "varied"
  diction: ""                  # "plain" / "mixed" / "formal" / "register-shifting"
  interiority_mode: ""         # "observational" / "ruminating" / "kinetic" / "associative"
  tense_preference: ""         # "scene-tense default" / "tense-slippage into memory" / "strict scene-tense"
  signature_moves: []          # the 2-4 prose patterns that mark this POV
  avoid_moves: []              # patterns the OTHER POV uses that this POV must not
```

Maya in The Late Frost: `sentence_length: short-with-one-layered-passage-per-beat`; `diction: plain-observational-architectural`; `interiority_mode: observational-with-suppressed-calculation`; `signature_moves: [architectural-spatial-noticing, "all-right-as-sentence", short-self-check-then-continue]`; `avoid_moves: [Sarah's-replay-pattern, "okay" as one-word-agreement]`.

Sarah: `sentence_length: cadenced-slightly-longer`; `diction: visual-kinetic`; `interiority_mode: replays-the-same-moment`; `signature_moves: [seeing-then-re-seeing, "and"-as-trail-off, "okay" as-pending-agreement]`; `avoid_moves: [Maya's-decision-"all-right", architectural-noticing]`.

### POV-VOICE-DRIFT activity (new in v1.3.1)

**POV-VOICE-DRIFT** is the audit activity. It surfaces register-bleed: places where one POV's chapter has slipped into the other POV's prose habits.

Triggering conditions:

- Two or more POV-bearing Character atoms exist with `lfw_pov_voice_register` populated
- ≥3 chapters have been drafted in *each* POV
- ≥8 sessions have passed since the last POV-VOICE-DRIFT

Procedure:

1. Read the most recent N chapters (default: last 4) by POV
2. Score each chapter's prose against its declared `lfw_pov_voice_register` — does each signature move appear? Do any avoid moves leak in?
3. Surface specific drift instances with line numbers / quoted phrases
4. Propose targeted revision — never silently rewrite

Output: drift report in the session log; line-level flags added to affected Scene atoms' Open Notes; updated `_state.md` open thread.

### Per-POV voice samples (optional)

For voice-mode cartridges (`voice-samples` enabled), v1.3.1 supports per-POV voice-sample backbones in addition to the manuscript-wide `_voice-samples.md`:

```
<Cartridge>/
  _voice-samples.md              # author's overall voice (v1.0)
  _voice-samples-maya.md         # Maya's specific POV register (v1.3.1, optional)
  _voice-samples-sarah.md        # Sarah's specific POV register (v1.3.1, optional)
```

Where present, VOICE-CHECK and POV-VOICE-DRIFT consult the POV-specific file first, then the manuscript-wide. The per-POV files are operator-private (gitignored), same as `_voice-samples.md`.

A cartridge in `writer-maintains` mode does not need these; the writer-maintains rule still holds (AI does not draft prose; AI flags structural and register issues only). Per-POV voice samples become valuable when the writer is *worried* about POV-register drift and wants the AI to have a more specific check than "this sounds Hadley-ish where it should be closer."

## §3 — DIALOGUE-AUDIT activity (new in v1.3.1)

**DIALOGUE-AUDIT** runs the four-axis function check on drafted dialogue and surfaces lines that score on zero or one axis.

Triggering conditions:

- A Scene with ≥10 dialogue-bearing lines is `drafted`
- The writer signals "the dialogue feels flat" or "this conversation isn't earning its space"
- ≥5 dialogue-heavy scenes have been drafted without a DIALOGUE-AUDIT
- Before BETA-PREP, on any chapter with a critical dialogue scene

Procedure:

1. Identify dialogue-bearing lines in the target Scene (or specified subset)
2. For each line, score against four axes (Plot / Character / Subtext / Rhythm)
3. Surface lines scoring 0 or 1 with specific diagnostic — *which axis is missing, why*
4. Surface stretches of 4+ consecutive lines that all score on the same single axis (information-dump cluster, character-demonstration cluster)
5. Cross-check against the speaking Character's dialogue tells — does the line sound like *that* character speaking, or like a generic character?
6. Cross-check against the Scene's value-shift (§ chapter 11) — do the dialogue lines participate in the turn, or are they parked outside it?

Output: per-line flags in the Scene atom's Open Notes; revision recommendations; pattern observation logged to `_craft-log.md` if the same diagnostic recurs across multiple audits.

### Cross-referencing with subtext-bearing Beats

When a Beat atom carries the v1.3.1 Subtext field, DIALOGUE-AUDIT reads it. The audit then asks: does the surface dialogue plausibly carry the declared subtext? Could a real reader, with the available cues, register the gap between line and meaning?

If the subtext is declared but the surface dialogue doesn't carry it — the writer has *intended* meaning that hasn't *landed* — the audit flags that as a craft gap, not a planning gap. The fix is at the prose layer, not the outline layer.

## §4 — Show-don't-tell as a craft module

Show-don't-tell is the most universal fiction-craft instruction and the one most often weaponized into a rule-of-thumb that does more harm than good. v1.3.1 ships it as an opt-in craft module — `craft-module-show-dont-tell.md`, referenced from chapter 09 — with the discipline that distinguishes *generative* show-don't-tell from *prohibitive* show-don't-tell.

### The discipline

**Telling is not always wrong.** A novel that never tells is exhausting; a novel that only tells is inert. The question is *what is the work of this sentence?*

- **Tell** when summarizing across time, when the texture is unimportant, when the reader needs information that doesn't deserve a scene
- **Show** when the moment is load-bearing for character, plot, or emotional weight — when the reader needs to *feel* the moment rather than be told it happened

The asserted-not-shown error mode (F22 in `_meta/FAILURE-MODES.md`, added v1.2) is specifically about telling at moments that needed showing. The fix is not "show everything"; the fix is "identify which moments are load-bearing and show *those*."

### Module triggers (opt-in)

The writer enables the module per session: *"include show-don't-tell discipline in this REVISE pass"* or sets it as a default in `_manuscript-manifest.md`:

```yaml
lfw_active_craft_modules:
  - show-dont-tell
  - pov-and-psychic-distance
```

When active, REVISE and READ-THROUGH passes will flag:

- Emotional states asserted in interiority without sensory or behavioral ground (F22)
- Backstory delivered as paragraphs of summary at moments where the reader needs the present
- Telling sentences ("She was angry") that follow a scene where the anger should already have been shown — redundant telling
- The opposite: showing where a tell would be cleaner — over-dramatizing a routine transition

The module never silently rewrites. It surfaces flags and proposes revision direction.

### Calibration: the writer's standing position

Some writers tell deliberately as a voice choice — interiority-heavy literary fiction; nineteenth-century pastiche; a narrator who comments. The craft module should know:

```yaml
lfw_show_dont_tell_calibration:
  standing_position: ""    # "strict-show" / "balanced" / "telling-narrator-as-voice" / "off"
  load_bearing_moments_only: true   # default — only flags at load-bearing moments
```

In `telling-narrator-as-voice` mode the module flags only the most egregious asserted-not-shown moments in scene-level interiority and skips routine narrative summary. The standing position protects voice from being homogenized by a module the writer never asked for.

## §5 — Updated Character atom (v1.3.1)

Existing Character atoms remain valid. v1.3.1 adds three optional sections / fields:

```yaml
---
# existing frontmatter unchanged
lfw_pov_voice_register:           # v1.3.1 — only for POV-bearing Characters
  sentence_length: ""
  diction: ""
  interiority_mode: ""
  tense_preference: ""
  signature_moves: []
  avoid_moves: []
lfw_character_bible: ""           # v1.3.1 — wiki-link to extended Character-Bible atom if present
---

## Dialogue tells *(v1.3.1, sub-section under Voice and prose register)*

(see §1)

## Subtext patterns *(v1.3.1, optional)*

*If this character habitually says-other-than-meant — what's the pattern? When do they speak plainly? When do they speak around?*
```

The `lfw_character_bible` link is a soft pointer to the extended Character-Bible atom (chapter 14 §3); not required, populated when the bible is created.

## §6 — Updated Beat atom (v1.3.1)

Existing Beat atoms remain valid. v1.3.1 adds one optional body section:

```markdown
## Subtext *(v1.3.1, optional — for beats where dialogue carries weight)*

- **Surface:** *(what is said)*
- **Underneath:** *(what is meant)*
- **What the listener registers:** *(or doesn't)*
- **What the reader registers:** *(may differ from listener)*
```

Beats where dialogue is doing critical work should have this section. Beats that are pure action, observation, or movement do not need it.

## §7 — Failure modes added in v1.3.1

See `_meta/FAILURE-MODES.md` for full entries.

- **F31 — Dialogue-as-information-dump.** Lines that score only on Plot axis; reader experiences as exposition in conversational clothing.
- **F32 — Interchangeable dialogue.** Lines that score zero on Character axis; any character could say them. Indicates dialogue tells haven't been internalized.
- **F33 — On-the-nose subtext.** Characters explain their feelings; the gap between surface and meaning collapses. Reader has nothing to do.
- **F34 — POV-voice bleed.** Maya's chapter sounds like Sarah's chapter (or vice versa); the reader cannot identify whose POV they are in. Triggers POV-VOICE-DRIFT.
- **F35 — Show-everything pathology.** Writer never tells; routine transitions are dramatized into full scenes; pacing collapses. The opposite failure mode from F22.
- **F36 — Style-sheet drift in dialogue formatting.** Said vs action-beat, em-dash vs ellipsis, italics-or-not — inconsistent across chapters. Reads as inattention.
- **F37 — AI homogenizes POV voices.** AI offers revision suggestions that smooth both POVs toward a single register. The AI's job is to *preserve* difference, not to harmonize. Voice mode `writer-maintains` is the structural defense; the POV-VOICE-DRIFT activity reinforces it.

## §8 — Activity decision-rule additions

Add to chapter 03 §6b':

- **If** a Scene with ≥10 dialogue lines is `drafted` AND hasn't been DIALOGUE-AUDIT'd → propose **DIALOGUE-AUDIT**
- **If** two POV-bearing Character atoms exist with `lfw_pov_voice_register` populated AND ≥3 chapters drafted in each AND ≥8 sessions since last POV-VOICE-DRIFT → propose **POV-VOICE-DRIFT**
- **If** the writer signals "the dialogue is flat" or "the POVs sound alike" → propose the corresponding activity even outside cadence thresholds

## §9 — What this chapter is not

- Not a dialogue-writing tutorial. The writer knows how to write dialogue; the OV provides structural checking.
- Not a substitute for the writer's ear. DIALOGUE-AUDIT surfaces structural failures (function, character-fit, subtext); it does not adjudicate whether a line is *beautiful*. That belongs to the writer.
- Not enforcement. All v1.3.1 fields are optional; all activities are opt-in. The module respects writers who don't want this layer of structure.

## §10 — Read-order placement

Required reading before any DIALOGUE-AUDIT or POV-VOICE-DRIFT activity. For cartridges with multi-POV structure, recommended at session 1 alongside chapters 11 + 12 so the POV-voice-register fields are populated early — register-drift is much easier to prevent than to retroactively diagnose across 60,000 words.
