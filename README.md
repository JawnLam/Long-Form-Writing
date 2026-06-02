# Long-Form-Writing

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Version](https://img.shields.io/badge/version-v1.0.0-blue.svg)](VERSION.md)

Long-Form-Writing is an **[operating volume](https://github.com/JawnLam/Operating-Volume-Engineering)** for AI-orchestrated sustained writing — book-length non-fiction, novels, screenplays, dissertations, plays, and other multi-month-to-multi-year projects. Pick a manuscript you've always wanted to finish. Point any capable AI at this folder, tell it to read `AI-BOOTSTRAP.md`, and it will help you carry the project across hundreds of daily writing sessions — keeping outline, atoms, drafts, and revision state in plain markdown files so you own your work.

> **What's an operating volume?** A self-contained markdown corpus an AI loads to orchestrate a particular kind of long-running, stateful work — the slot in the AI lexicon between a Custom GPT / Project and an AI harness. Substrate-agnostic (Claude, GPT, Gemini, etc.), stateful (files on disk are the memory), forkable. See **[Operating-Volume-Engineering](https://github.com/JawnLam/Operating-Volume-Engineering)** for the discipline. Long-Form-Writing is one of four operating volumes by the same author, alongside **[SOLVE-eX](https://github.com/JawnLam/SOLVE-eX)** (decision-making), **[LifeLong-Learning](https://github.com/JawnLam/LifeLong-Learning)** (self-directed study), and **Operating-Volume-Engineering** itself (the propagator).

---

## What this is

Long-Form-Writing is a writing engine plus a per-manuscript "cartridge" system. The writing engine is the AI's operating manual: how to start a new manuscript, how to structure a daily session, how to handle structural decisions, how to draft, revise, integrate research, diagnose a stuck moment, and prepare for beta readers. Cartridges are manuscript folders — one per project you're working on — that the engine plugs into.

You don't need to learn the system. The AI does. You point it at the folder, name your project, and the next two hundred sessions have a continuous memory.

The default tone is peer-level, direct, substantive critique. The system treats you as an adult writer doing serious work, not a beginner needing encouragement.

## What it can help with

- **Non-fiction books** — argument-driven, narrative-driven, or research-driven; multi-month arcs from premise to finished manuscript
- **Novels** — character-driven and plot-driven fiction; scene-by-scene work; character bibles; voice consistency
- **Screenplays and stage plays** — act structure, scene work, dialogue, beat sheets
- **Dissertations and long academic projects** — citation-heavy chapter work, source integration, defense prep
- **Memoirs and narrative non-fiction** — the hybrid space; the engine accommodates the edges
- **Other multi-month writing projects** — long-form essays, novellas, RFPs, business books, religious / spiritual texts, anything that needs to be carried across time

## What this is not

- Not a fiction generator. The AI doesn't write your book for you; it helps you write it.
- Not a publishing tool. The OV gets you to a shippable manuscript. Publishing happens outside.
- Not a substitute for an editor. When the work is ready, you still need a human editor — the OV makes you ready faster.
- Not opinionated about what you should write. You define the project; the engine adapts.

## The five things this OV is built around

1. **Genre-branching cartridges.** Every manuscript declares a genre — fiction, non-fiction, screenplay, dissertation, play. The schema adapts: a fiction cartridge gets Character atoms; a non-fiction cartridge gets Thread atoms; a dissertation gets Source-heavy atoms. One engine, six adapted shapes.

2. **Daily-practice cadence.** Sessions are designed to fit a writer's actual rhythm: 15 minutes on a stuck scene, 90 minutes of drafting, an hour-long revision pass. The session protocol accommodates short-and-frequent over long-and-rare. Momentum is structural, not heroic.

3. **Configurable voice model.** The default is *the writer maintains their own voice; the engine helps with structure, research, and revision logistics*. Optional: drop voice samples into the cartridge so the AI can match your style during DRAFT/REVISE. Optional: run a dedicated VOICE-CHECK activity. You decide how much help you want.

4. **Atoms as building blocks.** Manuscripts are composed of Beats (smallest), Scenes/Sections (the prose lives here), Chapters (compositions), Characters/Threads (recurring), Sources (research), Notes (unplaced fragments). The atom shape comes from your genre.

5. **Multi-pass revision discipline.** Revising is its own work, not a degraded form of drafting. The OV has explicit passes — structural, voice, accuracy, prose-line — and a revision-pass log that captures what each pass changed and why.

## Quick start

### 1. Open the folder in your AI environment

Plain markdown. Any environment where your AI can read local files works — Claude Code, Claude Desktop, Claude.ai Projects, ChatGPT Projects, Gemini, Cursor, Windsurf, Obsidian + Copilot, or plain text editors with AI integration.

### 2. Tell the AI to bootstrap

In your first message, say:

> **"Read `AI-BOOTSTRAP.md` and help me set up a new manuscript."**

Or, if you already have one in progress:

> **"Read `AI-BOOTSTRAP.md` and let's continue [project name]."**

### 3. Have the conversation

The AI asks one question at a time about the manuscript. Don't expect a bulk questionnaire — that's a documented failure mode this OV specifically guards against. Expect Socratic clarification, a structural conversation, and the start of a long working relationship with your project.

For setup details, see [`INSTALL.md`](INSTALL.md). For day-to-day operation and troubleshooting, see [`OPERATOR-GUIDE.md`](OPERATOR-GUIDE.md). To extend or contribute, see [`CONTRIBUTING.md`](CONTRIBUTING.md).

## System requirements

- **AI assistant** — any model capable of reading markdown and parsing YAML frontmatter (Claude Sonnet/Opus class, GPT-4 class and above, Gemini 2.x and above)
- **OS** — Mac, Windows, or Linux
- **Editor** — Obsidian works very well for this OV (the graph view across atoms is useful for fiction); also fine in VS Code, Cursor, Windsurf, Zed, plain text editors with AI integration
- **Python / network / runtime dependencies** — none

## Folder structure

| Folder / file                              | Contents                                                                |
|--------------------------------------------|-------------------------------------------------------------------------|
| `AI-BOOTSTRAP.md`                          | AI entry point — first file the AI reads                                |
| `README.md`                                | This file                                                               |
| `INSTALL.md`                               | Setup instructions                                                      |
| `OPERATOR-GUIDE.md`                        | Day-to-day operation and troubleshooting                                |
| `CONTRIBUTING.md`                          | How to extend the engine or share improvements back                     |
| `VERSION.md` / `CHANGELOG.md`              | Release metadata and history                                            |
| `LICENSE.md`                               | CC-BY 4.0                                                               |
| `_USER.md.template`                        | Optional user-profile template                                          |
| `_writing-engine/`                         | The subject-agnostic writing operating manual                           |
| `_writing-engine/_templates/`              | Templates for every atom type + cartridge backbone files                |
| `_writing-engine/_meta/`                   | Schema-of-schemas + the failure-modes catalog                           |
| `Example-Project-The-Persistence-Question/` | Worked example: a hypothetical non-fiction book at outlining-to-mid-draft stage |

Each cartridge contains: `_manuscript-manifest.md`, `_state.md`, `_outline.md`, optional `_voice-samples.md`, `Atoms/` (Beats / Sections-or-Scenes / Chapters / Threads-or-Characters / Sources / Notes), `Sessions/`, `Revision-Passes/`.

## License

Long-Form-Writing is released under the **Creative Commons Attribution 4.0 International License (CC-BY 4.0)**. You are free to share, adapt, and build upon this material for any purpose — including commercially — provided you give appropriate attribution.

See [`LICENSE.md`](LICENSE.md) for the full license text. Attribution format:

> Built on **Long-Form-Writing v1.0** by Jawn Lam — https://github.com/JawnLam/Long-Form-Writing
> Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

## Version

See [`VERSION.md`](VERSION.md). This is the **v1.0.0 initial public release**.
