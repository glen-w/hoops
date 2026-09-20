# Sidecar scope

**Audience:** humans and agents opening PRs against `glen-w/hoops`.  
**Default:** public git shows **artifacts only**. Creative, motifs, and process live in gitignored `local/` (one repo — no private sibling).

This repo is the **public data sidecar** for *Hoops: An Uncommon Field Guide to the Game of Basketball*. Prose lives in Scrivener. Citations live in Zotero `hoops`. Public framing lives on [glenwright.earth/projects/hoops](https://glenwright.earth/projects/hoops/). Do not rewrite the book here.

## Channel paste (verdict)

**Public stays:** redistributable derived CSVs/JSON, short method notes beside them, thin catalogs (`mentions.csv`, CHAPTER-MAP spine, source maps), regenerable `scripts/` / `src/`, schemas, tests.  
**Not public:** speculative essays, creative packs, motif indexes, spike diaries, agent status writeups, hooks/voice drafts → gitignored `local/` (archived under `local/archive/` when removed from the tree).  
**Ignored:** `data/raw/**` dumps, manuscript, Zotero, proprietary tracking.  
**PR rule of thumb:** if the diff does not add or harden a cite-backed artifact (or a one-line CHAPTER-MAP / ROADMAP pointer to it), reject it.

## Architecture (locked — do not re-litigate)

| Layer | Where |
|-------|--------|
| Manuscript prose | Scrivener (`.scriv` — never commit) |
| Citations / PDFs | Zotero `hoops` (+ Paperful for missing PDFs) |
| Public framing / blurb | glenwright.earth project page |
| Sidecar (this repo) | Derived tables, builders, catalogs, short method notes |
| Author/agent scratch | `local/` (gitignored) — creative, motifs, spikes |

## In vs out

| Commit (in) | Do not commit (out) |
|-------------|---------------------|
| Redistributable derived tables + license/provenance | Speculative essays, creative packs, voice drafts |
| Regenerable scripts that emit those tables | Author exploration notebooks that emit no artifact |
| Thin catalogs that unblock writing (`mentions.csv`, CHAPTER-MAP rows, source maps) | Process writeups, spike diaries, agent scratch, “how we thought about it” |
| One short method note per derived product | Long brainstorms, alternative framings, motif essays **and motif CSVs** |
| Draft **blockers / hedges** as `data/studies/*.md` or a short status cell | Narrative appends to CHAPTER-MAP Notes |

### Method note vs “showing the working”

A method note stays in-scope when it answers, in roughly **≤ ~100 lines**: source class, schema, blank rules, confidence, how to regenerate.  
It becomes out-of-scope theatre when it narrates agent paths (`/workspace/...`), lane collisions, PR choreography, or motif/voice essays longer than the table they describe.

**Good pattern:** `data/derived/salary_cap_apron/methodology.md`.  
**Out of pattern:** spike/phase reports, creative guides, hooks, STATUS diaries (removed from the public tree).

### Creative / motifs

Field-guide voice is a **manuscript** and **site** job. Motif indexes and creative packs are **local only** (`local/archive/` or `local/creative/`). Do not re-add them to the public tree. Leakage is not sensitive; still reject creative PRs so the public clone stays artifact-shaped.

## Path allowlist / denylist

### Allow (commit)

- `data/derived/**/*.csv`, `*.json` (redistributable products)
- `data/derived/**/method.md` | `methodology.md` | `SOURCE.md` | `README.md` (short)
- `data/cba/<edition>/derived/*.json` + `metadata.json` / hashes (no agreement text)
- `data/reference/**`, `data/studies/*.md` (one short note per cited claim/paper)
- `data/mentions.csv`, `data/sloan/papers.jsonl`
- `data/raw/**/README.md`, `LICENSES.md` only
- `docs/CHAPTER-MAP.md` (table spine only)
- `docs/DATA-REPOS.md`, `NUMBERS-LANDSCAPE.md`, `open_datasets.csv`, `EVIDENCE.md`
- `docs/*-sources.md`, ownership `*_methodology.md` / `*_README.md` (not trends essays)
- `docs/CBA-LOOKUP.md`, `docs/cba-structure-pipeline.md`, `docs/cba/COMPARE-*.md`
- `scripts/`, `src/`, `schemas/`, `tests/`, `ROADMAP.md`, `README.md`, `SCOPE.md`, `CONTRIBUTING.md`
- `pyproject.toml`, lockfiles, CI config

### Deny (do not add)

- `docs/creative/**`, `data/derived/creative/**`
- Motif / vignette indexes (`*_motifs.csv`, pocket guides, sonnets, postcards)
- `docs/**/SPIKE*.md`, `PHASE*-REPORT*.md`, `PRODUCTIZATION*.md`, `*-FEASIBILITY*.md`
- `docs/**/hooks.md`, writer-journey theatre
- `**/STATUS*.md`, agent desk diaries under `data/derived/**`
- Ownership `*_trends.md` stretch essays
- Manuscript, Zotero DB/PDFs, proprietary tracking dumps, CBA PDF/fulltext

### Park locally (gitignored)

- `local/**` — creative drafts, motif CSVs, notebooks, spike diaries, process archive

## CHAPTER-MAP rules

1. Append **at most one row** per new cite-backed artifact: `topic | path | cite | status`.
2. Status cells stay short (`ready`, `wanted`, `gap`, `partial`, `quotes_need_pdf`, plus ≤ ~20-word hedge).
3. **Never** append narrative, creative blurbs, or Phase diary paragraphs to Notes.
4. Draft blockers land as `data/studies/*.md` or a `wanted`/`gap` row.
5. Do not invent binder paths. Prefer `data/mentions.csv` / ROADMAP.

## Scripts: `scripts/` vs local

| Land in `scripts/` or `src/hoops_data/` when… | Keep under `local/` when… |
|-----------------------------------------------|---------------------------|
| It regenerates a committed derived file | One-off scrape that wrote no redistributable table |
| Tests or CI will call it | Notebook / exploratory REPL |
| Schema is stable enough to name | Spike that will be thrown away |

## Enforcement posture

**Hybrid A + D + C in one repo:** policy + PR checklist; indexes public / essays local; no private sibling. History rewrite removes legacy creative/process blobs so clones and blame stay artifact-shaped.

## Non-goals

- Do not propose rewriting the book in-repo.
- Do not weaken the Scrivener / Zotero split.
- Do not vendor raw NBA / tracking data or CBA fulltext.
