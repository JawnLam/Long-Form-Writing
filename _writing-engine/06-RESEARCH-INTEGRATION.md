---
type: writing-engine
role: research-integration
scope: non-fiction-and-dissertation
updated: 2026-06-02
lfw_load:
  tier: pack
  genres: [non-fiction, dissertation]
  activities: [RESEARCH-INTEGRATION, CLAIM-EVIDENCE-CHECK, SYNTHESIS-CHECK]
  phase: on-demand
---

# 06 — RESEARCH INTEGRATION

> **For non-fiction and dissertation cartridges. The protocol for taking external sources and folding them into the manuscript without (a) plagiarizing, (b) homogenizing voice with quoted material, (c) citing sources that don't actually support the claim, or (d) inventing citations.**

## When this chapter applies

This chapter is read on demand when:

- Cartridge genre is `non-fiction` or `dissertation`
- The current activity is RESEARCH-INTEGRATION
- A Section atom needs source backing
- The writer asks "how should I handle this source?"

For fiction or screenplay cartridges that incidentally use research (historical, biographical), the principles apply but the volume is much lighter.

## The four cardinal rules

### Rule 1: Never invent a citation

If the AI is not 100% certain a source exists in the form described — exact title, exact author, exact year, exact publication — it does not name it. Possible responses:

- *"I'm not sure that book exists. Can you verify?"*
- *"There's a book by X on this topic but I don't know the exact title; want me to ask you to provide it?"*
- *"I'd recommend looking for a source on this claim. I can't name a specific one I'm certain of."*

Fabricated citations are the highest-trust-cost failure in non-fiction work. See `_meta/FAILURE-MODES.md` F2.

### Rule 2: Never fabricate a quote

If the AI is not certain a quote is verbatim, it does not present it as one. Acceptable alternatives:

- Paraphrase with attribution: *"As Beard argues in SPQR, the founding date of 753 BC is precise to a fault…"*
- Flag for verification: *"You'll want to verify the exact wording — Beard makes a similar argument somewhere in chapter 1."*
- Ask the writer: *"Do you have the verbatim quote? I can flag a passage but I shouldn't reproduce it from memory."*

### Rule 3: Cited sources must actually support the claim

A common failure: the AI cites a source whose general topic is right but whose actual content doesn't support the specific claim being made. The AI must be honest:

- *"The source you have on this topic doesn't actually argue what your sentence claims. Want me to flag this for verification, or rewrite the sentence to match what the source does say?"*

If the AI is uncertain whether a source supports a claim, it says so rather than committing.

### Rule 4: Source ingestion comes before source citation

Before a source can be cited in prose, it must exist as a Source atom in the cartridge with at least these fields populated:

- Full citation
- Why it matters here (relevance to the manuscript)
- Key claims / passages (what to cite)
- How to integrate (which sections this informs)

If the writer wants to cite a source that isn't yet an atom, the AI proposes RESEARCH-INTEGRATION first: create the atom, then come back to drafting.

## The source ingestion protocol

When the writer adds a new source to a non-fiction or dissertation cartridge:

### Step 1: Create the Source atom

Use `TEMPLATE-Source.md`. Populate the frontmatter (author, year, publication, etc.) and the body sections.

For book-length sources, the writer typically reads (or has read) the source and provides the key passages, page numbers, and relevance notes. The AI helps structure but does not invent content.

For paper-length sources, the writer may want the AI to help summarize. The AI can do this from the source text provided by the writer. The AI cannot do this from the title alone — that's fabrication.

### Step 2: Set `lfw_status: ingested`

The source exists in the cartridge with enough context to be cited safely.

### Step 3: Identify which Sections it informs

Update the Source atom's "How to integrate" section: list the Sections (with wiki-links) where this source will be cited.

Cross-reference: in the relevant Section atoms, add the Source to `lfw_sources_cited` and to the body's "Sources Used" section.

### Step 4: Fold in

In a subsequent DRAFT or REVISE session on the target Section, the source is now available to cite. The fold-in protocol:

1. **Identify the specific claim or passage** the source supports
2. **Choose the citation form** — quote, paraphrase, summarize, allusion
3. **Maintain the writer's voice** — the cited source informs the claim; it doesn't take over the prose
4. **Add the citation** in the manuscript's declared style (`lfw_citation_style`)
5. **Set `lfw_status: folded-in`** on the Source atom

### Step 5: Cross-check after drafting

Periodically (typically at the end of a revision pass or before BETA-PREP), run an accuracy pass that:

- Verifies every citation in the manuscript matches a Source atom
- Verifies every claim attributed to a source actually appears in that source
- Flags sources cited only once that might be over-relied-on
- Flags sources with `lfw_status: superseded` (the writer should update or remove them)

## Citation styles

LFW v1.0 supports the major styles:

- **Chicago Notes-Bibliography** (humanities, history) — footnotes + bibliography
- **Chicago Author-Date** (sciences, social sciences) — (Author Year, page) + reference list
- **MLA** (literary criticism, humanities) — (Author page) + Works Cited
- **APA** (psychology, education, sciences) — (Author, Year, p. X) + References
- **Harvard** (UK academic, sciences) — (Author, Year) + reference list
- **Custom** — declare your conventions in `_manuscript-manifest.md`

The AI applies the declared style consistently. It does not silently switch styles.

## When sources contradict the writer's argument

A subtle ethical question. The AI's position:

- **Surface counter-evidence honestly.** If the writer's Thread says "X" and a Source says "not X," the AI flags this in the relevant Thread atom's "Sources that complicate or contradict it" section.
- **Don't bury counter-evidence to make the argument cleaner.** The honest manuscript engages counter-evidence.
- **Don't pretend the writer's argument is unassailable.** Even in advocacy non-fiction, the strongest version of the argument addresses the strongest version of the counter-argument.

This is the writer's call ultimately. The engine surfaces; the writer decides.

## Quote density

Quoted material from sources is acceptable but should be:

- **Brief** — generally one or two sentences per quote, occasionally a paragraph for high-leverage passages
- **Cited** — every quote has an attribution
- **Functional** — the quote does work in the manuscript (it can't be paraphrased without loss)
- **Voice-aware** — the writer's prose around the quote frames it; the writer's voice surrounds the quoted voice

A non-fiction manuscript that's 30% quoted material is not your book; it's an annotated bibliography. The engine flags this if it sees it.

## Plagiarism boundary

The line between "informed by a source" and "lifted from a source" is:

- **Paraphrase without attribution = plagiarism.** Always attribute when you take an idea from a source.
- **Closely-tracked structure without attribution = plagiarism.** If you follow a source's argument in the same order with the same examples, attribute it.
- **Common knowledge does not need attribution.** "Rome was founded in 753 BC traditionally" is common knowledge; cite if you discuss the historiographical debate about that date.
- **When uncertain, cite.** Over-attribution is a minor flaw; under-attribution is a career-ending one.

## Working with primary sources

For history, religious studies, classics, literary criticism, etc., primary sources (texts being analyzed rather than just cited) get special treatment:

- Create dedicated Source atoms with `lfw_source_kind: primary-document`
- Quote more liberally than for secondary sources (primary-source analysis often requires extended quotation)
- Note translation provenance if the original is in another language
- Track edition/translation choices in the Source atom

## Dissertation-specific notes

For dissertations:

- Citation rigor is the dominant constraint. Every claim that isn't your own original analysis needs a citation.
- Source diversity matters. A dissertation that cites 12 sources for 80,000 words is under-researched.
- The literature review chapter is typically Source-heavy by design.
- Methodology sections cite methodological sources (works on the method itself).
- Defense prep means knowing every citation cold. The AI can help you study your own bibliography before defense.

## Anti-pattern: research as procrastination

A common failure: a writer in `outlining` or `drafting` stage spends every session in RESEARCH-INTEGRATION, accumulating sources without ever drafting. Six months later, hundreds of source atoms, no manuscript.

The AI watches for this:

- If RESEARCH-INTEGRATION dominates 5+ consecutive sessions with no DRAFT activity, the AI flags it
- The flag is not a judgment; it's a question: *"You've been integrating sources for several sessions without drafting. Is this the right activity, or are you avoiding the drafting?"*
- The writer answers honestly. Sometimes more research is genuinely needed. Sometimes it's avoidance.

Connected to STUCK-DIAGNOSTIC. See chapter 03.
