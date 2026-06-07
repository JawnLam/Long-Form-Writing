# Long-Form-Writing — Install Guide

Once you have this folder on disk, the only things you need to use it are an AI assistant and your willingness to actually write the thing.

## 1. Install (recommended: git clone with push disabled)

This is the **canonical install pattern per OVE Convention 7** — git-tracked so you can `git pull` future releases; push disabled so you can't accidentally upload your manuscript work.

```bash
# Choose a parent folder. Anything works — Dropbox-synced, iCloud-synced, Obsidian vault, etc.
mkdir -p ~/Operating-Volumes
cd ~/Operating-Volumes

# Clone into a folder named with the current major.minor.
# (Check VERSION.md or the GitHub releases page for the current version.)
git clone https://github.com/JawnLam/Long-Form-Writing.git \
  Long-Form-Writing-v1.7

# Disable push remote — protects your manuscript work against accidental upload.
cd Long-Form-Writing-v1.7
git remote set-url --push origin DISABLED_TO_PREVENT_ACCIDENTAL_PUSH_OF_PERSONAL_WORK

# Verify
git remote -v
# Expect: origin fetch URL real; origin push URL = DISABLED_TO_PREVENT_ACCIDENTAL_PUSH_OF_PERSONAL_WORK
```

**Why the folder name has a version suffix.** The convention is `Long-Form-Writing-v<major>.<minor>`. When a new major.minor ships (e.g., v1.8), `OPERATOR-GUIDE.md § Updates` walks you through renaming the folder so old and new can briefly coexist during the transition.

**Why push is disabled.** Almost everything you do in this folder beyond reading the engine is private manuscript work — character bibles, drafts, session histories, motif catalogs. The push-disabled default prevents the worst-case operator-error: `git push` accidentally uploading your in-progress manuscript to the public LFW repo. You can re-enable push to your own fork if you want to contribute back upstream (see `OPERATOR-GUIDE.md § Contributing back`).

## 1a. Alternative install (no git tracking)

If you don't want git tracking — you'd rather treat this as a snapshot reference, no updates — you can also just download the folder:

- **Plain copy:** Download a release ZIP from the GitHub releases page; unzip anywhere your AI assistant can read.
- **Cloud-synced folder** (Dropbox, iCloud, OneDrive, Google Drive) — convenient for cross-device writing.
- **Obsidian vault** — recommended for fiction (graph view across characters, scenes, motifs).
- **Plain local folder** — works for any AI environment that supports file attachments.

The folder is fully self-contained. No network fetch happens at runtime; no paths are hard-coded. The trade-off versus the git-tracked install: you don't get `git pull` updates — you have to re-download each release.

## 2. (Optional) Configure your user profile

If you want consistent personalization across every manuscript:

```
cp _USER.md.template _USER.md
```

Fill in your name (the spelling matters — see `_writing-engine/_meta/FAILURE-MODES.md`), communication preferences, and any default writing preferences (preferred genre, default cadence, voice-mode preferences).

## 3. (Optional) Initialize git

If you want version control on your manuscripts (recommended for any serious writing project):

```
cd "Long-Form-Writing"
git init
git add .
git commit -m "Initial install"
```

The shipped `.gitignore` excludes drafts and session logs by default so the folder can be shared without leaking unfinished work. **For your own manuscripts you almost certainly want the opposite** — every revision tracked. Edit `.gitignore` to remove the cartridge-content exclusions before your first commit on your own work.

## 4. First session walkthrough

1. **Open the folder in your AI environment.**

2. **Send the AI a single message.** Choose the one that matches:

   For a new manuscript:
   > Read `AI-BOOTSTRAP.md` and help me set up a new manuscript.

   For an existing cartridge:
   > Read `AI-BOOTSTRAP.md` and let's continue [project name].

   For a stuck moment:
   > Read `AI-BOOTSTRAP.md` — I'm stuck on chapter 4 of [project]. Help me diagnose.

   For conceptual questions about the system:
   > Read `AI-BOOTSTRAP.md` — what is this OV for?

3. **Wait for the readiness statement.** The AI's first response should be a short paragraph confirming it has read the writing engine, plus either a clarifying question (new manuscript), a session-activity proposal (existing cartridge), or a direct answer (orientation).

   If the AI responds with a long explanation or generic greeting instead, it skipped Phase 0. Tell it: *"Read `AI-BOOTSTRAP.md` in full before responding."*

4. **Have the conversation.** Expect one question at a time. The AI guards against multi-bullet questionnaires.

## 5. The daily rhythm

Once a cartridge is set up, the typical writing day looks like:

1. **Open the folder; tell the AI to continue your manuscript.** AI re-reads state.
2. **AI proposes today's activity** based on `_state.md` (what's flagged as today's focus, what's been promised, what's overdue).
3. **You confirm or override.** "I want to draft Section 3.2 today" overrides anything the AI proposed.
4. **Work the session.** 15 minutes, 90 minutes, whatever fits today.
5. **Close out.** The AI writes a session log, updates `_state.md`, captures any new Items.

Some days you write. Some days you outline. Some days you revise. Some days you're stuck and run a STUCK-DIAGNOSTIC. The protocol accommodates all of these.

## 6. What "done" looks like

A complete cartridge produces, by the time you're done:

- A finished manuscript (assembled from Section/Scene Items)
- A complete structural outline (`_outline.md` final form)
- A library of Items — beats, scenes/sections, chapters, characters/threads, sources, notes
- Session logs covering the full arc of the project
- Revision pass logs (what each pass changed and why)
- An honest assessment of what's still thin (the AI's job is to surface this before you ship)

Then you take the manuscript to a human editor, agent, advisor, or publication channel — depending on what the project is for.

## 7. Troubleshooting

| Symptom                                                | Likely cause / resolution                                                                                                                          |
|--------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| AI tries to write your manuscript for you              | Voice-mode misconfigured, or you asked for prose without an outline first. Say *"Don't draft until we've outlined the section."*                    |
| AI homogenizes your voice                              | You're in voice-samples mode but samples aren't representative. Switch to writer-maintains mode, or update samples. See `_writing-engine/05-VOICE-AND-CRAFT.md`. |
| AI dumps a multi-bullet questionnaire during cartridging | Stop. Say *"Ask one question at a time, conversationally."* Documented failure mode F1.                                                              |
| AI invents sources or quotes for non-fiction           | Stop and correct. From now on it should say *"I can't verify that"* rather than invent. F2 in failure modes.                                         |
| AI uses a guessed name for you                         | Correct with placeholder. F3 in failure modes.                                                                                                       |
| AI starts drafting prose before the section is outlined | Stop. The protocol explicitly forbids this (F8). Return to OUTLINE first.                                                                            |
| Session ends without writing to `_state.md`            | Re-prompt: *"Close the session properly — write the session log and update `_state.md`."*                                                            |

For deeper guidance, see `OPERATOR-GUIDE.md`.

## 8. Updating (when a new release ships)

When LFW ships a new release on GitHub (announced in `CHANGELOG.md`):

```bash
cd ~/Operating-Volumes/Long-Form-Writing-v<your-current-major>.<minor>

git fetch origin
git log --oneline HEAD..origin/main           # preview what's incoming

# If you have no local engine modifications: clean fast-forward
git pull --ff-only origin main

# If you have local engine modifications: stash → pull → pop
git stash push --include-untracked -m "pre-update state"
git pull --ff-only origin main
git stash pop                                  # resolve any conflicts
```

**When major.minor changes (e.g., v1.7 → v1.8 ships):**

```bash
cd ~/Operating-Volumes/
mv Long-Form-Writing-v1.7 Long-Form-Writing-v1.8
```

The CHANGELOG entry for the new major.minor will tell you whether folder rename is recommended or required. For pure-patch releases (e.g., v1.7.0 → v1.7.1), no folder rename is needed.

For troubleshooting common update issues (fast-forward conflicts, stash-pop merge conflicts, dirty working tree blocking pull), see `OPERATOR-GUIDE.md § Updates and troubleshooting`.

## Version

This install guide ships with Long-Form-Writing v1.7.1. See `VERSION.md`.
