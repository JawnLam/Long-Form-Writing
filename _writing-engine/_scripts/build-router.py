#!/usr/bin/env python3
"""
LFW router generator.

Walks engine chapter files and meta files, parses their `lfw_load` frontmatter,
and emits `_writing-engine/_ROUTER.md` — a generated dispatch manifest that
maps (genre, activity) → chapters to load.

Standard-library only. No external dependencies.

Usage:
    python3 build-router.py            # writes _ROUTER.md
    python3 build-router.py --check    # prints generated content to stdout; does not write
    python3 build-router.py --stdout   # synonym for --check

The generator is IDEMPOTENT: running it twice produces a byte-identical file.
The validator's `router-fresh` check regenerates in memory and compares to
the committed `_ROUTER.md`; a stale router becomes a build failure.

Source files walked:
  - _writing-engine/*.md (all chapter files at the engine root, including
    BOOTSTRAP-NEW-MANUSCRIPT.md)
  - _writing-engine/_meta/*.md (FAILURE-MODES, SCHEMA-OF-SCHEMAS)

The router itself (`_writing-engine/_ROUTER.md`) is excluded from the walk
to prevent self-reference.
"""

import hashlib
import pathlib
import re
import sys
from collections import defaultdict


# Project root resolution: script lives at <ROOT>/_writing-engine/_scripts/build-router.py
ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
ENGINE = ROOT / "_writing-engine"
ROUTER_OUT = ENGINE / "_ROUTER.md"

VALID_TIERS = {"core", "pack"}
VALID_PHASES = {"bootstrap", "on-demand"}
VALID_GENRES = {"all", "fiction", "non-fiction", "dissertation", "screenplay", "play"}

# Activity codes per chapter 03 — the 25 activities. Plus "all" as a wildcard.
VALID_ACTIVITIES = {
    "all",
    # Production (10)
    "SESSION-START", "OUTLINE", "DRAFT", "REVISE", "RESEARCH-INTEGRATION",
    "READ-THROUGH", "STUCK-DIAGNOSTIC", "VOICE-CHECK", "WORLDBUILDING", "BETA-PREP",
    # Development non-fiction (6)
    "READER-SIMULATION", "ARGUMENT-AUDIT", "CLAIM-EVIDENCE-CHECK", "STEELMAN",
    "SYNTHESIS-CHECK", "CRAFT-REVIEW",
    # Development fiction v1.2 (4)
    "SCENE-AUDIT", "CHARACTER-CONSISTENCY", "CONTINUITY-CHECK", "SETUP-PAYOFF-AUDIT",
    # Fiction craft v1.3.1 (3)
    "DIALOGUE-AUDIT", "POV-VOICE-DRIFT", "THEME-CHECK",
    # Soft-skill v1.4.0 (2)
    "WEATHER-CHECK", "MIDDLE-AUDIT",
}


def parse_frontmatter(text):
    """Minimal YAML-ish parser. Stdlib-only — no PyYAML.
    Handles flat keys, scalar values, [list] inline, multi-line block lists
    (`key:\\n  - item`), and one-level nested key/value blocks
    (`key:\\n  child: val`). Returns a dict."""
    out = {}
    if not text.startswith("---\n"):
        return out
    end = text.find("\n---\n", 4)
    if end == -1:
        return out
    fm_text = text[4:end]
    lines = fm_text.splitlines()

    def _strip_scalar(v):
        if isinstance(v, str):
            if v.startswith('"') and v.endswith('"'):
                v = v[1:-1]
            elif v.startswith("'") and v.endswith("'"):
                v = v[1:-1]
            v = re.sub(r"\s+#.*$", "", v).strip()
        return v

    def _parse_inline_value(val):
        val = val.strip()
        if val.startswith("[") and val.endswith("]"):
            inner = val[1:-1].strip()
            if not inner:
                return []
            return [_strip_scalar(x.strip()) for x in inner.split(",")]
        return _strip_scalar(val)

    i = 0
    while i < len(lines):
        line = lines[i]
        if not line or line.lstrip().startswith("#"):
            i += 1
            continue
        if line.startswith(" ") or line.startswith("\t"):
            i += 1
            continue
        if ":" not in line:
            i += 1
            continue
        key, _, val = line.partition(":")
        key = key.strip()
        val = val.strip()
        if val:
            out[key] = _parse_inline_value(val)
            i += 1
            continue
        # Empty value → nested block (list or dict) follows
        i += 1
        nested_items = []
        nested_dict = {}
        is_list = None
        while i < len(lines):
            child = lines[i]
            if not child.strip():
                i += 1
                continue
            if not (child.startswith(" ") or child.startswith("\t")):
                break
            stripped = child.strip()
            if stripped.startswith("- "):
                if is_list is False:
                    break
                is_list = True
                nested_items.append(_strip_scalar(stripped[2:].strip()))
                i += 1
                continue
            if stripped == "-":
                if is_list is False:
                    break
                is_list = True
                nested_items.append("")
                i += 1
                continue
            if ":" in stripped:
                if is_list is True:
                    break
                is_list = False
                ckey, _, cval = stripped.partition(":")
                nested_dict[ckey.strip()] = _parse_inline_value(cval)
                i += 1
                continue
            i += 1
        if is_list:
            out[key] = nested_items
        else:
            out[key] = nested_dict

    return out


def collect_sources():
    """Return list of (relative-path, lfw_load-dict, full-path) for every
    source file. Sorted by relative path for deterministic output."""
    paths = []
    # Engine root .md files (chapters + BOOTSTRAP)
    for p in sorted(ENGINE.glob("*.md")):
        if p.name == "_ROUTER.md":
            continue
        paths.append(p)
    # Meta files
    for p in sorted((ENGINE / "_meta").glob("*.md")):
        paths.append(p)
    out = []
    for p in paths:
        text = p.read_text()
        fm = parse_frontmatter(text)
        lfw_load = fm.get("lfw_load")
        if not isinstance(lfw_load, dict):
            continue  # silently skip files without lfw_load (the validator catches this separately)
        rel = p.relative_to(ROOT).as_posix()
        out.append((rel, lfw_load, p))
    return out


def validate_lfw_load(rel_path, ll):
    """Return list of (path, error-string) tuples; empty if valid."""
    errors = []
    tier = ll.get("tier", "").strip() if isinstance(ll.get("tier"), str) else ""
    if tier not in VALID_TIERS:
        errors.append((rel_path, f"tier='{tier}' not in {sorted(VALID_TIERS)}"))
    phase = ll.get("phase", "").strip() if isinstance(ll.get("phase"), str) else ""
    if phase not in VALID_PHASES:
        errors.append((rel_path, f"phase='{phase}' not in {sorted(VALID_PHASES)}"))
    genres = ll.get("genres", [])
    if not isinstance(genres, list) or not genres:
        errors.append((rel_path, "genres must be a non-empty list"))
    else:
        for g in genres:
            if g not in VALID_GENRES:
                errors.append((rel_path, f"genre '{g}' not in {sorted(VALID_GENRES)}"))
    activities = ll.get("activities", [])
    if not isinstance(activities, list) or not activities:
        errors.append((rel_path, "activities must be a non-empty list"))
    else:
        for a in activities:
            if a not in VALID_ACTIVITIES:
                errors.append((rel_path, f"activity '{a}' not in known activity set"))
    return errors


def build_dispatch_tables(sources):
    """Returns (bootstrap_set, by_genre, by_genre_activity) tuples for emission.
    "all" in `genres` or `activities` is expanded to the full set. Chapters declared
    with activities=[all] are dispatched on EVERY known activity for their declared
    genres — they become effectively-always-loaded via the router."""
    bootstrap = []
    # by_genre: { genre: [paths] } — chapters this genre may activate (any activity)
    by_genre = defaultdict(list)
    # by_genre_activity: { (genre, activity): [paths] } — for specific dispatch
    by_genre_activity = defaultdict(list)

    # Full sets used to expand "all"
    ALL_GENRES = ["fiction", "non-fiction", "dissertation", "screenplay", "play"]
    ALL_ACTIVITIES = sorted(a for a in VALID_ACTIVITIES if a != "all")

    for rel, ll, _ in sources:
        phase = ll["phase"]
        genres = ll["genres"]
        activities = ll["activities"]

        if phase == "bootstrap":
            bootstrap.append(rel)
            continue

        # Expand "all" in genres
        expanded_genres = list(ALL_GENRES) if "all" in genres else list(genres)
        # Expand "all" in activities
        expanded_activities = list(ALL_ACTIVITIES) if "all" in activities else list(activities)

        for g in expanded_genres:
            if rel not in by_genre[g]:
                by_genre[g].append(rel)

        for g in expanded_genres:
            for a in expanded_activities:
                if rel not in by_genre_activity[(g, a)]:
                    by_genre_activity[(g, a)].append(rel)

    return bootstrap, by_genre, by_genre_activity


def render_router(sources):
    """Render the _ROUTER.md content. Deterministic and idempotent.
    Returns the full string."""
    # Validate first; collect errors
    all_errors = []
    for rel, ll, _ in sources:
        all_errors.extend(validate_lfw_load(rel, ll))
    if all_errors:
        msg = "build-router.py: invalid lfw_load frontmatter:\n"
        for rel, err in all_errors:
            msg += f"  - {rel}: {err}\n"
        raise SystemExit(msg)

    bootstrap, by_genre, by_genre_activity = build_dispatch_tables(sources)

    lines = []
    lines.append("# _ROUTER.md — LFW Engine Dispatch Manifest")
    lines.append("")
    lines.append("> **GENERATED FILE — DO NOT EDIT BY HAND.**")
    lines.append(">")
    lines.append("> Regenerate with `python3 _writing-engine/_scripts/build-router.py`.")
    lines.append(">")
    lines.append("> The validator's `router-fresh` check regenerates this file in memory")
    lines.append("> on every run and fails if the committed copy differs from the regenerated")
    lines.append("> content. A stale router becomes a build failure — correct by construction.")
    lines.append("")
    lines.append("Source-of-truth for which engine chapters an AI loads on a given session,")
    lines.append("computed from each chapter's `lfw_load` frontmatter declaration. AI clients")
    lines.append("consult this file after reading the bootstrap-phase chapters and use the")
    lines.append("(genre, activity) tables to determine which on-demand chapters to load.")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Bootstrap section
    lines.append("## 1. Bootstrap-phase (always loaded, every session)")
    lines.append("")
    lines.append("These chapters are loaded before the router is consulted. The minimal")
    lines.append("always-read set required to dispatch the rest of the engine.")
    lines.append("")
    for rel in sorted(bootstrap):
        lines.append(f"- `{rel}`")
    lines.append(f"- `_writing-engine/_ROUTER.md` (this file)")
    lines.append("")
    lines.append("AI clients should also read `AI-BOOTSTRAP.md` at the OV root before any")
    lines.append("engine chapter, then load the bootstrap-phase chapters above plus this")
    lines.append("router, then dispatch via the tables below.")
    lines.append("")

    # By-genre section: which chapters a cartridge of this genre ever activates
    lines.append("## 2. By genre — chapters this genre activates (on-demand)")
    lines.append("")
    lines.append("For a cartridge of a given genre, these are the chapters the router may")
    lines.append("dispatch (depending on session activity — see §3). Chapters NOT listed for")
    lines.append("a genre are never loaded for that genre, no matter what activity is run.")
    lines.append("")
    for g in sorted(by_genre.keys()):
        lines.append(f"### {g}")
        lines.append("")
        for rel in sorted(by_genre[g]):
            lines.append(f"- `{rel}`")
        lines.append("")

    # By (genre, activity) section
    lines.append("## 3. By (genre, activity) — exact dispatch table")
    lines.append("")
    lines.append("On any given session, the AI determines the cartridge genre (from")
    lines.append("`_manuscript-manifest.md`) and the proposed activity (per `03-CADENCE-AND-SESSIONS.md`)")
    lines.append("and loads the chapters listed for that pair. Always also load the bootstrap-phase")
    lines.append("chapters (§1).")
    lines.append("")
    # Sort by genre, then activity
    sorted_pairs = sorted(by_genre_activity.keys())
    current_genre = None
    for (g, a) in sorted_pairs:
        if g != current_genre:
            lines.append(f"### {g}")
            lines.append("")
            current_genre = g
        chapters = sorted(by_genre_activity[(g, a)])
        chapter_list = ", ".join(f"`{c}`" for c in chapters)
        lines.append(f"- **{a}** → {chapter_list}")
    lines.append("")

    # Hash footer
    content_so_far = "\n".join(lines)
    content_hash = hashlib.sha256(content_so_far.encode("utf-8")).hexdigest()[:16]
    lines.append("---")
    lines.append("")
    lines.append(f"_Content hash (sha256, first 16 chars): `{content_hash}`_")
    lines.append("")

    return "\n".join(lines)


def main():
    args = sys.argv[1:]
    check_only = any(a in ("--check", "--stdout") for a in args)

    sources = collect_sources()
    if not sources:
        raise SystemExit("build-router.py: no source files with lfw_load found")

    content = render_router(sources)

    if check_only:
        sys.stdout.write(content)
        return

    # Idempotent write — only update mtime if content changed
    if ROUTER_OUT.exists():
        existing = ROUTER_OUT.read_text()
        if existing == content:
            print(f"build-router.py: _ROUTER.md is already up to date ({len(sources)} sources)")
            return
    ROUTER_OUT.write_text(content)
    print(f"build-router.py: wrote {ROUTER_OUT.relative_to(ROOT)} from {len(sources)} sources")


if __name__ == "__main__":
    main()
