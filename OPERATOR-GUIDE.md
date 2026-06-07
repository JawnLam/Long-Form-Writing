# Long-Form-Writing — Operator Guide

This guide is for the writer running LFW day-to-day: how sessions actually work, common failure modes, how to recover, and how to keep a multi-month manuscript healthy.

If you're setting up for the first time, read [`INSTALL.md`](INSTALL.md) first.

---

## 1. How a writing session actually works

A writing session has eight phases. The AI runs through all of them; you only experience the parts where you talk and write.

1. **READ** — AI reads the writing engine, your `_USER.md` (if present), the active cartridge's `_manuscript-manifest.md`, `_state.md`, `_outline.md`, recent session logs, and any Items flagged as today's focus.
2. **DIAGNOSE** — AI inspects state for hard overrides, today's focus, overdue revision passes, stuck flags.
3. **PROPOSE** — AI proposes an activity (SESSION-START / OUTLINE / DRAFT / REVISE / RESEARCH-INTEGRATION / READ-THROUGH / STUCK-DIAGNOSTIC / VOICE-CHECK / WORLDBUILDING / BETA-PREP) with rationale.
4. **WAIT** — AI waits for your confirmation or override.
5. **EXECUTE** — the actual writing happens here.
6. **CAPTURE** — AI records Item updates, prose drafted, revision changes, decisions made.
7. **WRITE session log** — new file in `<Cartridge>/Sessions/`.
8. **UPDATE `_state.md`** — overwritten with new state; today's focus rolls forward to tomorrow's seed.

If a session ends without phases 6–8, the session is incomplete. Tell the AI to finish.

## 2. Reading the cartridge state

`<Cartridge>/_state.md` is the single source of truth. Useful sections:

- **Lifecycle stage** — outlining / drafting / revising / polishing / shipped
- **Today's focus** — what's queued for today's session
- **Item status table** — every Section / Scene with draft state (not-started / drafted / revised-pass-1 / final)
- **Revision pass progress** — current pass, what's left to revise
- **Word counts** — by chapter / section / total
- **Open Threads** — what next session is supposed to address
- **Stuck flags** — anywhere the writer marked "I'm stuck here"

## 3. Common failure modes and how to fix them

### AI tries to write your manuscript for you

**Symptom:** You ask the AI to "help me with chapter 3" and it generates prose. You wanted to write the prose; you wanted the AI to help you outline, probe, push, or revise.

**Fix:** Be explicit about the activity. *"OUTLINE this chapter — don't draft any prose."* Or *"Probe my draft for weak spots — don't rewrite it."* The activities (defined in `_writing-engine/03-CADENCE-AND-SESSIONS.md`) exist to make this unambiguous.

**Prevention:** Default voice mode is hands-off. Use `_USER.md` to set your default AI involvement level.

### AI homogenizes your voice (in voice-samples mode)

**Symptom:** You've enabled voice-samples mode and the AI's DRAFT output sounds like generic AI prose, not your voice.

**Fix:** Check your voice samples. They need to be genuinely representative — varied (different topics, different moods), substantial (multiple paragraphs each), and clearly *your* voice (not your influences). If samples are short or vague, the AI defaults to averaged prose. See `_writing-engine/05-VOICE-AND-CRAFT.md`.

**Prevention:** Curate voice samples deliberately. 3–5 substantial passages (300+ words each) work better than 20 short ones.

### AI starts drafting prose before the section is outlined

**Symptom:** Section has no beat-level plan and the AI starts generating prose anyway.

**Fix:** Stop. Tell the AI: *"This section doesn't have beats. OUTLINE first."* Documented failure mode F8 in `_writing-engine/_meta/FAILURE-MODES.md`.

**Prevention:** The session protocol algorithm orders activities. OUTLINE comes before DRAFT. If you skip OUTLINE because "you already know what the section is," you'll find later that the AI didn't.

### AI invents sources, quotes, or facts (non-fiction)

**Symptom:** AI cites a book, paper, or expert you can't verify. The citation feels plausible but doesn't quite match anything real.

**Fix:** Stop immediately and verify. If fabricated, say *"That citation is wrong. Remove it from the section. From now on, if you're not sure a source exists, say so."* This is failure mode F2.

**Prevention:** For non-fiction and dissertation work, the engine has a RESEARCH-INTEGRATION protocol (chapter 06) with explicit anti-fabrication discipline. Use it. Don't draft research-heavy prose without sources already ingested into Source Items.

### AI uses a guessed name for you

**Symptom:** The AI calls you by a name you haven't provided (often parsed from your username or file path).

**Fix:** Stop and correct. Failure mode F3 — load-bearing rule with a documented recurrence pattern.

### `_state.md` is corrupted or stale

**Symptom:** AI can't read your state, or state contradicts the session logs.

**Fix:** Open the most recent session log in `<Cartridge>/Sessions/`. Reconstruct `_state.md` from it using `_writing-engine/_templates/TEMPLATE-state.md`. If multiple sessions back are unrecoverable, walk the Item status fields directly to rebuild.

### You've revised the same section three times and it's still not right

**Symptom:** Revision pass 1, 2, 3 — each time you go back, the section feels worse. You've lost the original momentum.

**Fix:** This is the classic "abandoned revision pass" failure (F9). Stop revising. Go back to OUTLINE and ask: *is this section in the right place in the book? Does it need to exist? Is the beat structure wrong, not the prose?* Most three-times-revised sections are structurally wrong, not prose-wrong.

### You haven't written in weeks and the cartridge feels intimidating

**Symptom:** You stopped writing for two weeks. Now opening the cartridge feels like a task.

**Fix:** Run a SESSION-START activity with a low bar. The AI re-reads state, summarizes where you were, surfaces the smallest reasonable next step (often "draft three beats of Section 4.2 — fifteen minutes"). The protocol is designed for re-entry after gaps.

**Prevention:** Daily-practice cadence is the design assumption. Two-week gaps happen; the engine accommodates them but they cost momentum. Treat the cartridge as a living thing — even 15 minutes once a week is better than a two-month gap followed by a heroic push.

## 4. Cartridge health over time

A long-form manuscript can drift across months. Periodic checks:

- **Every ~10 sessions:** ask the AI to do a **state-audit** pass — does the outline still match the chapters being drafted? Any Items drifting?
- **At end of first draft:** ask the AI for an **honest-thinness audit** — where is the manuscript thin? What needs more research, more revision, more cutting?
- **Before each major revision pass:** run a **READ-THROUGH** at the appropriate scale before line-by-line work.
- **Before sending to beta readers:** run a **BETA-PREP** activity. Last chance to catch big problems.

## 5. Sharing or transporting a cartridge

A cartridge is a self-contained folder. Zip and send.

If you're sharing with a collaborator (co-author, editor), they drop the cartridge into their own LFW folder. **Note that the cartridge contains your voice samples, drafts, and notes** — share deliberately.

## 6. Multiple manuscripts in parallel

No limit. You can have several cartridges in active drafting at once. The AI loads only one cartridge per session.

Some writers find that working on two genres simultaneously (a novel and a non-fiction project) actually helps — when one is stuck, work the other. The engine accommodates this; each cartridge's state is independent.

## 7. When you abandon a cartridge

It happens. Some manuscripts don't finish. To archive a cartridge cleanly:

- Update `_state.md` lifecycle stage to `abandoned`
- Add a final session log explaining why
- Move the cartridge folder to an `_Archived/` directory at the LFW root (or wherever you want)

Don't delete. The Items, the partial draft, the research — keep them. Future-you may return.

## 8. Engine vs your work — the four content zones (OVE Convention 8)

Your installed LFW folder has four content zones. Knowing which is which prevents the operator-pulls-and-loses-work failure mode.

### Engine Zone — release-owned; updated by `git pull`

The files that LFW's release ships:

- Front-door docs: `README.md`, `AI-BOOTSTRAP.md`, `INSTALL.md`, `OPERATOR-GUIDE.md`, `CONTRIBUTING.md`, `LICENSE.md`, `VERSION.md`, `CHANGELOG.md`, `MIGRATION-NOTES.md`
- `_writing-engine/` — engine chapters, templates, meta, scripts
- `_Prototypes/` — LFW's own Prototype definitions
- `_USER.md.template` — the template, not the populated `_USER.md`
- `.gitignore` — engine-zone file

**Do not edit Engine Zone files directly.** Updates from `git pull` overwrite them. Customizations belong in Operator-Extension Zone cartridges or in per-cartridge configuration (`_manuscript-manifest.md`, `_style-sheet.md`, `_argument.md`, `_spine.md`).

### Operator-Private Zone — gitignored; never tracked

The `.gitignore` excludes:

- Your operator profile (`_USER.md`), cross-cartridge craft profile (`_craft-profile.md`)
- Per-cartridge state (`**/_state.md`), session logs (`**/Sessions/*.md`), revision passes (`**/Revision-Passes/*.md`)
- Operator-private working artifacts: voice samples, craft logs, argument backbones, spine, continuity, promises, overlays, worldbuilding, storyboard, style sheet, relationships
- Operator-private Items: character bibles, timelines, inspirations (under each cartridge's `Items/Character-Bibles/`, `Items/Timelines/`, `Items/Inspirations/`)

These never get pushed and never get touched by `git pull`. The `!Example-Project-*/**` override re-includes the worked examples (Shipped Examples Zone).

### Operator-Extension Zone — your manuscript cartridges; survives `git pull`

This is where your work lives. Every manuscript you bootstrap through LFW becomes a folder at the LFW root.

`<Cartridge>/` folders that aren't named `Example-Project-*` are not in LFW's release, so `git pull` never touches them. They're yours.

### Shipped Examples Zone — release-owned; updated by `git pull`

The two worked-example cartridges that demonstrate LFW:

- `Example-Project-The-Late-Frost/` — literary fiction
- `Example-Project-The-Persistence-Question/` — non-fiction

**Do not edit Shipped Examples directly.** If you want to riff on an example, copy it into an Extension Zone cartridge (`cp -r Example-Project-The-Late-Frost My-Novel-In-Progress`) and customize there.

## 9. Updates and troubleshooting

The canonical update workflow lives in `INSTALL.md § 8`. Common scenarios:

### Clean fast-forward (no local engine modifications)

```bash
cd ~/Operating-Volumes/Long-Form-Writing-v<your-major>.<minor>
git fetch origin
git log --oneline HEAD..origin/main          # what's incoming
git pull --ff-only origin main
```

### Fast-forward fails because you have local engine modifications

```bash
git status                                    # see what's modified
git stash push --include-untracked -m "pre-update state"
git pull --ff-only origin main
git stash pop                                 # may produce conflicts on engine files you edited
```

If `git stash pop` reports conflicts, the conflict is between *your local edit* of an engine file and *the upstream release's version*. You almost always want the upstream version (engine evolution generally improves what's there):

```bash
git checkout --theirs <conflicting-file>
git add <conflicting-file>
# OR — abandon your local edits entirely:
git checkout origin/main -- <conflicting-file>
```

If your local edit was load-bearing, copy it to a side file before checkout, then reconcile.

### Update lost a file you cared about

`git pull` only updates tracked paths. If a file disappeared, either: (a) the release explicitly removed it (the `CHANGELOG.md` will say so), or (b) it was a gitignored file you forgot was ignored. For (a), the file is recoverable via `git log --all --oneline -- <path>`. For (b), check whether the file matched a `.gitignore` pattern.

### Major.minor folder transition

When the release notes say to rename your folder:

```bash
cd ~/Operating-Volumes/
mv Long-Form-Writing-v<old> Long-Form-Writing-v<new>
cd Long-Form-Writing-v<new>
git status   # should show clean
```

The folder rename doesn't affect git; the rename is for your filesystem clarity.

### Contributing back upstream

To contribute back (open a PR against the upstream LFW), re-enable push to *your own fork* (never to upstream):

```bash
# Replace with your fork's URL
git remote set-url --push origin https://github.com/<your-username>/Long-Form-Writing.git

# Make a branch, commit, push to your fork, open a PR on GitHub
git checkout -b my-contribution
# ... your changes ...
git commit -m "..."
git push origin my-contribution
```

When you're done contributing, re-disable push to protect your private manuscript work going forward:

```bash
git remote set-url --push origin DISABLED_TO_PREVENT_ACCIDENTAL_PUSH_OF_PERSONAL_WORK
```

## Version

This operator guide ships with Long-Form-Writing v1.7.1.
