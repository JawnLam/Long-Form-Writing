---
type: LFW_Piece
Item_ID: "<piece-slug>-piece"
title: "<Piece Title>"
Date_Added: <YYYY-MM-DD>
Date_Modified: <YYYY-MM-DD>
Needs_Processing: false
lfw_manuscript: "<workshop-slug>"
lfw_piece_status: germinating   # germinating | drafting | revising | ready | published | archived
lfw_graduated_to_multivac: false
# On publication, add the universal-core fields (do NOT invent piece-specific ones):
# Publication_Date: <YYYY-MM-DD>   # the date it published
# resource: "<canonical URL>"      # canonical publication URL (e.g. Substack)
# URL: "<mirror URL>"              # optional mirror (e.g. Medium)
---

# <Piece Title>

## What this piece is

*One or two sentences. The claim or the angle.*


## Status notes

*Where the whole folder stands; what's next. The status above describes the ENTIRE piece-folder, not just this prose file.*


## The draft

*The prose, or a pointer to where it lives in the folder.*


## Publication

*Once published: canonical + mirror links and date, mirroring `Publication_Date` / `resource` / `URL` above. On graduation to MultiVac, `lfw_graduated_to_multivac` is set true and a row is appended to `_published-ledger.md`.*

<!--
Companion: each piece-folder carries an Obsidian Canvas `_wall.canvas` — the wall of
supporting material (quotes, sources, fragments, structure). A .canvas file is JSON with
no YAML frontmatter, so it is a folder convention, NOT a schema type.
-->
