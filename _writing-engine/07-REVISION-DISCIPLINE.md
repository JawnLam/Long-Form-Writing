---
type: writing-engine
role: revision-discipline
scope: subject-agnostic
updated: 2026-06-02
---

# 07 — REVISION DISCIPLINE

> **Revising is its own work, not a degraded form of drafting. Multi-pass discipline keeps revision purposeful and finite.**

## The core problem revision solves

Most first drafts are wrong in multiple ways at once:

- Structurally — wrong scenes/sections, wrong order, wrong scope
- Voice-wise — inconsistent register, drift across chapters
- Accuracy-wise (non-fiction) — claims not yet verified, citations incomplete
- Prose-line — sentences that don't quite land, word choices off

A writer trying to fix all of these in one pass fixes none of them well. They hop from "this sentence is awkward" to "wait, this scene shouldn't exist" to "I'm not sure I believe this argument" and end up demoralized.

Multi-pass discipline solves this. Each pass has a single focus. The writer (and the AI) only attend to that focus during that pass. Other issues get noted but not addressed until their pass.

## The four standard passes

LFW v1.0 specifies four standard revision passes. A cartridge may add custom passes in `_manuscript-manifest.md` if its genre demands.

### Pass 1: Structural

**Question:** Does this manuscript hang together?

**What to look for:**

- Are the right chapters/scenes here? Are any missing? Any extra?
- Is the order right? Does each chapter follow from the previous?
- Are the scopes proportionate? (A 40,000-word setup and a 5,000-word payoff is structurally broken.)
- Do the threads (non-fiction) or arcs (fiction) develop coherently across the book?
- Is the opening doing the work it needs to? The ending?

**What to ignore:**

- Prose-line awkwardness — note it but don't fix it; that's a later pass
- Voice inconsistency — note it; pass 2
- Factual claims — note them; pass 3
- Word choices — pass 4

**Output:**

- A list of structural changes to make
- Cut sections marked for removal (move to `_archive/` within the cartridge, don't delete)
- Reordered chapters
- New sections to draft (or revised outlines for existing sections)

This pass often results in significant cutting and re-drafting. That's expected.

### Pass 2: Voice

**Question:** Does this sound like the writer throughout?

**What to look for:**

- Drift across chapters (chapter 1 sounds different from chapter 9)
- Sections that sound like quoted sources (voice was lost during RESEARCH-INTEGRATION)
- Sections that sound like the AI homogenized them
- Inconsistent register (you started conversational, drifted into academic; or vice versa)

**Voice mode interaction:**

- `writer-maintains`: the AI flags inconsistencies; the writer fixes them
- `voice-samples`: the AI may offer voice-corrected drafts for the writer to revise
- `voice-check-on-demand`: this entire pass IS the VOICE-CHECK activity

**What to ignore:**

- Structure — that was pass 1
- Facts — that's pass 3
- Word choice unless it's a voice signal — pass 4

**Output:**

- Voice-inconsistency flags in `_state.md`
- Revised passages (or a list of passages to revise)
- Updated voice samples if the writer's voice has shifted intentionally

### Pass 3: Accuracy (non-fiction and dissertation)

**Question:** Are the claims, citations, and quotations correct?

**What to look for:**

- Every factual claim — is it sourced or common knowledge?
- Every citation — does it match a Source atom? Is the source actually in the bibliography?
- Every quotation — verbatim? Page number correct?
- Every name, date, place — spelled correctly? Year correct?
- Every statistic or data claim — source verified?

**Method:**

This pass typically requires going slowly with the sources at hand. The AI helps by:

- Listing every claim and matching it to the relevant Source atom
- Flagging claims with no source
- Flagging citations that don't match an existing Source atom (might be a typo or might be fabrication — verify both ways)
- Surfacing quotes the writer asked to flag for verification

**Output:**

- A claim-by-claim verification log
- Any citations that need re-checking
- Any quotes that need to be verified or paraphrased

For fiction without research dependencies, this pass is skipped. For fiction with historical or technical accuracy stakes, it's required.

### Pass 4: Prose-line

**Question:** Does the prose, sentence-by-sentence, do its work?

**What to look for:**

- Awkward sentences
- Word choices that don't land
- Rhythm flatness (long stretches of same-length sentences)
- Filler ("very," "really," "just," "rather")
- Clichés that haven't earned their place
- Repetition (the same word three times in a paragraph; the same image twice in a chapter)
- Tense slips
- Point-of-view slips (fiction)

**AI involvement:**

This pass is the writer's most. The AI may flag candidates only if explicitly invited (*"flag awkward sentences in this chapter"*). Most writers prefer to do prose-line work alone — it's where voice lives most concentratedly.

**Output:**

- A polished manuscript at the prose-line level
- Atoms updated with revised prose
- Final word counts

## The revision-pass log

Every pass produces a log entry in `<Cartridge>/Revision-Passes/`. File name:

```
YYYY-MM-DD_pass-NN_<pass-kind>.md
```

E.g., `2026-09-15_pass-01_structural.md`.

Use `TEMPLATE-revision-pass.md`. The log captures:

- **Pass kind** (structural / voice / accuracy / prose-line / custom)
- **Scope** (which chapters/sections this pass covered)
- **Started / completed** dates
- **Atoms touched** with before/after status
- **Major changes** (cuts, reorderings, new sections, etc.)
- **Decisions made** (with rationale)
- **Open threads** carried forward to the next pass

The log is append-only; revisions to the log itself are bad practice.

## Pass ordering

The standard order is **structural → voice → accuracy → prose-line**. The reasoning:

1. **Structural first** because reordering or cutting a chapter makes voice/accuracy/prose work on that chapter wasted effort
2. **Voice second** because consistent voice makes accuracy verification easier (you can hear when something doesn't fit)
3. **Accuracy third** because verifying claims requires the structural and voice work to be settled
4. **Prose-line last** because polishing sentences in a section you're about to cut is a waste

A writer may iterate (do another structural pass after the first prose pass surfaces a problem). That's fine. But within any single pass, focus is strict.

## When a pass needs to be aborted

Sometimes a writer starts a pass and realizes mid-way that the manuscript needs a different kind of work. Don't ignore the signal — abort the pass cleanly:

1. Update the revision-pass log: mark the pass as `aborted` with a note explaining why
2. Update `_state.md` lifecycle stage to whatever the new work requires (often back to `drafting` or `outlining`)
3. Start the new work in a fresh session

Aborted passes are not failures; they're the protocol working. The failure mode is continuing a pass that should be aborted, doing surface work on a manuscript that needs deeper work.

## Multiple rounds

A book typically goes through multiple revision rounds. Round 1: structural / voice / accuracy / prose-line. Beta readers. Round 2: structural / voice / accuracy / prose-line. Editor. Round 3: structural / voice / accuracy / prose-line.

Each round has its own four passes. The revision-pass log captures every pass across every round.

After a certain point (typically round 3 for most projects), additional passes have diminishing returns. The honest-thinness audit in chapter 08 helps the writer know when to stop.

## The danger of endless revision

Some manuscripts get stuck in perpetual revision. Symptoms:

- Five+ structural passes, each one moving the same sections around
- Voice drift over time (the writer's voice has changed; the early chapters now feel old)
- Increasingly small changes per pass with no improvement in confidence
- The writer's reluctance to call anything "final"

The AI watches for this:

- If a chapter has 4+ revision passes and is still not marked `final`, the AI surfaces this in the session log
- The AI proposes a "should this be done?" conversation
- The writer answers honestly — sometimes the manuscript needs another pass; sometimes the writer needs to ship

This is connected to STUCK-DIAGNOSTIC (chapter 03) and to BETA-PREP (chapter 08).
