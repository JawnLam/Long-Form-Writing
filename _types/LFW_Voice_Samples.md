---
type: Fleeting
timestamp: "2026-06-06T00:00:00Z"
Item_ID: type-lfw-voice-samples
title: "LFW_Voice_Samples Type"
Date_Added: 2026-06-06
Date_Modified: 2026-06-06
Needs_Processing: false
---

# `LFW_Voice_Samples` — Type Definition

> **What this file is.** The canonical definition of the `LFW_Voice_Samples` Type for the Long-Form-Writing Operating Volume. Items in any cartridge that declare `type: LFW_Voice_Samples` conform to the contract described below.

## Purpose

The Voice Samples Item is the writer's **representative prose** — three to five samples (300+ words each) of the writer's own unaided work, used by the AI when voice mode is `voice-samples` or for `VOICE-CHECK` activities. The AI uses these samples to **calibrate** offered drafts (in DRAFT mode), to **flag** voice inconsistencies (in REVISE mode), and to run VOICE-CHECK passes against drafted Sections. **The samples calibrate; they do not homogenize.** The AI does not "average" the writer's voice or impose a style — the samples are how the AI learns what *this writer*'s voice sounds like so it can offer drafts the writer might write. Optional backbone. Only enabled when the writer has opted in via `lfw_voice_mode: voice-samples` in the Manifest. Per chapter 05 (Voice and Craft). For multi-POV cartridges (v1.3.1), per-POV voice-sample backbones may exist alongside (`_voice-samples-{pov-slug}.md`).

## Required frontmatter

| Field | Type | Required? | Notes |
|-------|------|-----------|-------|
| `type` | string | yes | Must equal `LFW_Voice_Samples` |
| `Item_ID` | string | yes | Format: `<manuscript-slug>-voice-samples` (or `<manuscript-slug>-voice-samples-<pov-slug>`) |
| `Title` | string | yes | Format: `"<Manuscript Title> — Voice Samples"` |
| `Date_Added` | date | yes | When the samples were collected |
| `Date_Modified` | date | yes | When samples were last refreshed |
| `Needs_Processing` | boolean | yes | Default `false` |
| `lfw_manuscript` | string | yes | Manuscript slug |
| `lfw_sample_count` | integer | yes | Number of samples in the file (typically 3–5) |

## Body structure

```markdown
# <Manuscript Title> — Voice Samples

## How this file is used
*Brief explanation of calibration vs homogenization.*

## Sample 1 — <Topic / Context>
*(300+ words of the writer's own representative prose. Recent if possible.)*

---

## Sample 2 — <Different Topic / Context>
*(300+ words, varied topic and mood from Sample 1.)*

---

## Sample 3 — <Another Topic>
*(300+ words.)*

---

## Sample 4 *(optional)*

## Sample 5 *(optional)*
*More than 5 starts to dilute the signal.*

---

## Voice notes
*Any explicit guidance for the AI — what's typical, what's drift, what's intentional stylistic choice.*

## Last updated
*Date the samples were last refreshed. Voice shifts; refresh at least annually.*
```

## Naming

- **Filename:** `_voice-samples.md` (single-POV) or `_voice-samples-<pov-slug>.md` (per-POV, v1.3.1)
- **Location:** cartridge root
- **Wikilink target:** `_voice-samples` or `_voice-samples-<pov-slug>`

## Example Item

```markdown
---
type: LFW_Voice_Samples
timestamp: "2026-04-30T00:00:00Z"
Item_ID: tech-essay-cartridge-voice-samples
title: "Tech-Essay Cartridge — Voice Samples"
Date_Added: 2026-03-12
Date_Modified: 2026-04-30
Needs_Processing: false
lfw_manuscript: tech-essay-cartridge
lfw_sample_count: 3
---

# Tech-Essay Cartridge — Voice Samples

## How this file is used
The AI reads this file at session start when voice mode is enabled (declared in the Manifest as `lfw_voice_mode: voice-samples`). It uses these samples to calibrate offered drafts and flag voice inconsistencies. The samples calibrate; they do not homogenize.

## Sample 1 — On documentation as care

*(~340 words of the writer's prose discussing software documentation — chosen because it shows the writer's typical handling of an abstract claim. The cadence is medium-long sentences with internal commas as breath-points; the diction is plain with occasional specialist terms used without italics or definition; the rhetorical move is concession-followed-by-pivot. Reproduced verbatim from a blog post dated 2025-11-04.)*

---

## Sample 2 — On a parenting moment

*(~310 words of the writer's prose on a specific parenting interaction — chosen because it shows the writer's voice at warmer register. Same cadence but slightly shorter sentences; sensory detail substitutes for analytic move. Reproduced verbatim from a journal entry dated 2025-09-22, lightly edited for length.)*

---

## Sample 3 — On the difficulty of starting

*(~360 words on procrastination, drawn from a Substack post 2026-01-15. Chosen because it shows the writer's tendency toward direct confrontation with the reader. The pronoun "you" appears 8 times in 360 words — a signature feature. Diction shifts down a register here; the sentences shorten.)*

---

## Voice notes
- I tend to write long sentences with semicolons. That's intentional. Don't break them into short declaratives.
- I avoid the word "just" when I'm being careful. If I use it, I probably wasn't being careful — flag it.
- Em dashes are my main rhythm tool. Don't replace them with commas; the rhythm changes.
- Second-person "you" in essays is intentional but in scene-prose it would be wrong. Honor the genre context.
- I rarely use "obviously" or "of course" — when I do, it's signaling something specific. Don't smooth them out.

## Last updated
2026-04-30 (last sample refresh). Refresh at least annually; voice shifts.
```

## Relationships

- `LFW_Manuscript_Manifest` — `lfw_voice_mode: voice-samples` in the Manifest is what enables this file's use. If voice mode is `writer-maintains` (default), this file is not used by the AI even if present.
- `LFW_Style_Sheet` — Voice Samples capture the writer's *prose*; the Style Sheet captures the *conventions* the prose has chosen. Both contribute to consistent voice; the two cross-reference often.
- `LFW_Character` — For multi-POV cartridges, per-POV Voice Samples may exist (`_voice-samples-{pov-slug}.md`); Character Items reference their POV's voice-samples file.
- `LFW_Craft_Profile` — The cross-cartridge Craft Profile may name voice patterns that recur across the writer's work; the Voice Samples are a per-cartridge calibration that aligns with profile observations.
- `LFW_Revision_Pass` — Voice revision passes pressure-test drafted prose against Voice Samples.

## Notes

- **Opt-in.** Voice Samples are only active when the writer has set `lfw_voice_mode: voice-samples` in the Manifest. Default mode (`writer-maintains`) leaves voice entirely to the writer; the AI doesn't attempt voice calibration.
- **Calibrate, don't homogenize.** The AI uses samples to learn what *this writer*'s voice sounds like. The AI does not use samples to enforce a single style across the writer's output.
- **3–5 samples is the sweet spot.** Fewer than 3 is undercalibrated; more than 5 starts to dilute the signal (the AI begins to "average" rather than pattern-match).
- **Vary topic and mood across samples.** Three samples of the writer at the same register, on the same topic, do not calibrate the writer — they calibrate a slice. Cover different rhetorical moves, different emotional registers, different contexts.
- **Refresh at least annually.** Voice shifts. A writer's 2024 samples may not be operational for their 2026 prose.
- **Operator-private by default** (per `.gitignore`). The writer's representative prose is theirs; shipping a cartridge with Voice Samples included is a deliberate choice.
- **Per-POV samples for multi-POV cartridges** (v1.3.1, chapter 13 §2). When a cartridge has two or more POV characters, each POV's voice needs its own calibration; the per-POV files (`_voice-samples-{pov-slug}.md`) are the mechanism.
- **Voice notes are load-bearing.** The "Voice notes" section is where the writer tells the AI what to honor and what to flag. "I tend to write long sentences with semicolons. That's intentional" prevents the AI from smoothing the semicolons out as if they were errors.
