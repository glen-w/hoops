# NBA CBA parser feasibility (hoops sidecar)

**Access date:** 2026-09-19 (Europe/Paris, UTC+2)  
**Requester context:** Survey glen-w BBNJ repos → assess an analogous reader for NBA Collective Bargaining Agreements in `glen-w/hoops`.  
**Clarification applied:** `glen-w/BBNJ` is the *landscape scan*, not the agreement reader. The package to mirror is **`dacheah/bbnj-high-seas-treaty-corpus`**. `BBNJ-Navigator` is a weaker independent JSON. `glen-w/BBNJ-CHM-proto` is a Clearing-House Mechanism desk prototype — it does **not** host agreement PDF parsing.

---

## 1. What the BBNJ reader does (concrete files/APIs)

### Orientation of glen-w repos (do not confuse)

| Repo | Role | Agreement parsing? |
|------|------|--------------------|
| [`glen-w/BBNJ`](https://github.com/glen-w/BBNJ) | Open-source **landscape scan** (13 projects; reports dated 9 Sep 2026) | No — documents others |
| [`glen-w/BBNJ-CHM-proto`](https://github.com/glen-w/BBNJ-CHM-proto) | Transactional Cl-HM prototype (MGR/EIA/CBTMT rails); MIT | No — treaty text is linked, not re-parsed |
| [`dacheah/bbnj-high-seas-treaty-corpus`](https://github.com/dacheah/bbnj-high-seas-treaty-corpus) | **Authoritative legal corpus** + deterministic derived structure | **Yes — this is the mirror target** |
| [`henriquejbmarcos/BBNJ-Navigator`](https://github.com/henriquejbmarcos/BBNJ-Navigator) | Static SPA over hand-built `bbnj_agreement.json` | Independent digitisation; no SHA-256 / CI |

Landscape verdict (from `glen-w/BBNJ` `reports/01-landscape.md` and `reports/repos/01-…`): corpus is best-in-class for provenance + CI; Navigator is fine UX but weaker substrate.

### Package / module identity (corpus)

Not a pip-installable named package today — a **repo-as-toolkit**:

- **Python scripts** under `scripts/` (entry points, not a console_scripts package)
- **Schemas** under `schema/`
- **Two layers:** `authoritative/` (source PDFs + hashes) and `derived/` (structure, concepts)
- DOI badge: `10.5281/zenodo.21279773` (claimed; landscape scan marked network-unverified on 2026-09-09)
- Live site: https://dacheah.github.io/bbnj-high-seas-treaty-corpus/

### How it ingests PDF / text

| Stage | Script / tool | Behavior |
|-------|---------------|----------|
| Capture → store | `scripts/ingest.py` | Append-only packaging of captured files; writes `metadata.yaml`; refuses overwrite of an existing version |
| Extract | `scripts/extract.py` + `scripts/pipelines.py` | Re-derive `text.txt` from stored `original.pdf`; compare SHA-256 to recorded `text_sha256` |
| Extractors | **poppler** `pdftotext` (primary); **PyMuPDF** for some records (e.g. UNCLOS); OCR pipelines for zh/ar (`ocr_unverified`) | Toolchain versions attested; CI pins `ubuntu-24.04` + Poppler 24.02.0 |
| Build derived | `scripts/build_derived.py` | Deterministic unit split + citation detection + concept tags |
| Validate | `scripts/validate_corpus.py`, `scripts/repro_gate.py`, `scripts/verify_engine.py` | Schema, path identity, hash match, AKN mint check, engine manifest |
| Site | `scripts/build_site.py` | Static HTML from layers |

Deps (`scripts/requirements.txt`): `PyYAML>=6.0`, `jsonschema>=4.0`, `pymupdf==1.28.2` (pinned), system `poppler-utils`.

### Structure model

English BBNJ Agreement derived artifact (verified 2026-09-19):

`derived/un/bbnj-agreement-2023/2023-06-19/structure.json`

- `unit_type`: `"article"`
- `unit_count`: **79** = preamble/chapeau + Articles 1–76 + ANNEX I + ANNEX II
- Each unit: `{ number, label, text }`
- Root also has `citations_detected` (list of cross-ref strings; 114 entries in English structure)
- Flagged `_derived: true` + disclaimer (never presented as authoritative)

`build_derived.split_units()` heuristics (from source): prefer `Article|Section|Rule|Clause` + number headers; else numbered paragraphs; else whole-document unit. Configurable via `concepts.UNIT_HEADERS` / `CITATION_PATTERNS`.

### Derived outputs (beyond structure)

Per authoritative version under `derived/<corpus_id>/<version_id>/`:

- `structure.json`
- `concepts.json` (keyword / curated tags; often `review_status: unreviewed`)
- `derived-metadata.yaml` (traces to `source_text_sha256`)

Corpus-level:

- `derived/concept-index.json` (+ `.md`)
- `derived/crosswalk-bbnj-unclos.json` (+ `.md`) — unofficial BBNJ↔UNCLOS crosswalk

### Provenance / hashing

`scripts/hashing.py`:

- Algorithm: **SHA-256**, always prefixed `sha256:`
- `original_sha256` over raw PDF bytes
- `text_sha256` over canonical `text.txt` (UTF-8, LF, no BOM, one trailing newline)
- Authoritative `metadata.yaml` also carries `content_hash`, `source_url`, `retrieval_date`, `text_fidelity` (`extracted_verified` | `extracted_unverified` | `ocr_unverified`), `capture_history[]`, license/rights notes

Schemas: `schema/authoritative-metadata.schema.json`, `schema/derived-metadata.schema.json`, plus `schema/akn-registry.json` (Akoma Ntoso identifiers).

### Tests & CI

- **No pytest suite** (landscape note). Self-tests embedded in `watch_sources.py` / `verify_engine.py`.
- GitHub Actions:
  - `.github/workflows/validate.yml` — every push/PR: engine identity, toolchain pin assert, `validate_corpus.py`, `repro_gate.py`
  - `.github/workflows/pages.yml` — validate → build_derived → build_site → Pages
  - `watch-sources.yml`, `annual-review.md`

### Licenses

- Derived layer / scripts / docs / site: **CC BY 4.0** (`LICENSE-derived-CC-BY-4.0.txt`)
- No root `LICENSE` → GitHub API `license: null`
- Source UN texts: **not relicensed**; per-record `license` / `rights_note` (UN materials freely reproducible with attribution, no warranty)

### Contrast: BBNJ-Navigator (weaker independent JSON)

- Five-file static app; `bbnj_agreement.json` (~156 KB): metadata + preamble + 12 parts / 76 articles + 2 annexes
- Provenance = source URL in metadata only; **no content hashes, no multi-language, no CI**
- Themes hard-coded in JS (`ARTICLE_THEMES`) — editorial, not data
- Landscape recommendation: consume corpus layers; do not maintain a third digitisation

---

## 2. What transfers vs what doesn't

### Transfers well (engineering pattern)

| Pattern | Why it matters for NBA CBA |
|---------|----------------------------|
| Two-layer wall: raw official PDF vs derived JSON | Keep "what the league published" separate from "what we parsed" |
| SHA-256 of PDF + derived text; metadata with retrieval date + official URL | Detect silent PDF replacements / edition drift |
| Deterministic structure parse + schema validation | Reproducible clause IDs for Scrivener lookups |
| CI integrity gate (hash + schema) | Sidecar stays honest as editions update |
| Explicit disclaimers on derived artifacts | Writers know JSON is not the contract |
| User-supplied / gitignored raw (`data/raw/` already in hoops) | Matches hoops README data policy |

### Does **not** transfer (legal / licensing / domain)

| Treaty corpus | NBA CBA |
|---------------|---------|
| UN materials: freely reproducible with attribution | **Private labor agreement** between NBA and NBPA — **copyrighted**; not an open treaty |
| Committing byte-exact PDFs + full `text.txt` in git is normal | **Do not republish full CBA text in a public git repo** without care / rights review |
| Six authentic languages, AKN legal IDs | English primary; Article/Section/Exhibit model, not UNCLOS-style Parts |
| CC BY 4.0 on derived full-text structure | Sidecar should prefer **structure + citations + clause IDs + short excerpts / hashes**, not full verbatim republication |
| Public UN depositary URLs | Official PDFs are published for reading, but publication ≠ permission to rehost |

**Honest bottom line:** Mirror the *architecture* (provenance, layers, deterministic parse, CI). Do **not** mirror the *content policy* of committing full authoritative text to a public repo.

### Official NBA CBA sources (public PDFs; verified HTTP 200 on 2026-09-19)

Portal pages:

- NBPA CBA hub: https://nbpa.com/cba  
- NBA Official 2017 page: https://official.nba.com/2017-nba-collective-bargaining-agreement/  
- NBPA announcement (points to NBA.com/official and NBPA.com): https://nbpa.com/news/nba-collective-bargaining-agreement-signed  

Direct PDFs (prefer these as "official URL" in metadata; sizes checked 2026-09-19):

| Edition | Publisher surface | URL | Size (bytes) |
|---------|-------------------|-----|--------------|
| **2023** Final | NBA Official (ak-static) | https://ak-static.cms.nba.com/wp-content/uploads/sites/4/2024/06/2023-NBA-Collective-Bargaining-Agreement-Final.pdf | 2 903 978 |
| **2023** Final | NBPA (imgix/cosmic) | https://imgix.cosmicjs.com/25da5eb0-15eb-11ee-b5b3-fbd321202bdf-Final-2023-NBA-Collective-Bargaining-Agreement-6-28-23.pdf | 2 850 534 |
| **2017** | NBA Official (ak-static) | https://ak-static.cms.nba.com/wp-content/uploads/sites/4/2017/10/2017-NBA-Collective-Bargaining-Agreement.pdf | 2 176 412 |
| **2017** | NBPA (imgix) | https://cosmic-s3.imgix.net/3c7a0a50-8e11-11e9-875d-3d44e94ae33f-2017-NBA-NBPA-Collective-Bargaining-Agreement.pdf | 2 186 284 |
| **2011** | NBPA (imgix) | https://cosmic-s3.imgix.net/3d8ade10-8e11-11e9-875d-3d44e94ae33f-2011-NBA-NBPA-Collective-Bargaining-Agreement.pdf | UNCONFIRMED size (link present on nbpa.com/cba) |

Also linked from NBA Official related links: CBA 101 PDF (summary educational doc — not the CBA itself).

**Copyright flag (non-lawyer note for @engineer):** Publication of PDFs on NBPA/NBA sites does not make the text open-licensed. Public sidecar should store **structure, clause IDs, page/locator citations, defined-term index, and content hashes** — and optionally **user-local** full text under `data/raw/` (gitignored). Avoid committing full extracted text to `glen-w/hoops` without an explicit rights decision.

---

## 3. Proposed MVP for NBA CBA parser in hoops (or sibling)

### Placement

Prefer **in-repo module** under existing `hoops-data` (`src/hoops_data/cba/` or `src/hoops_cba/`) so Scrivener chapter maps and `data/mentions.csv` stay co-located. Spin a sibling `glen-w/nba-cba-corpus` only if the rights story and CI weight grow beyond the sidecar.

Align with hoops policy already stated in README: manuscript + Zotero stay out; `data/raw/` is gitignored; "cite, don't rehost" for proprietary systems.

### MVP scope

1. **Ingest official PDF only**  
   - User downloads from NBA/NBPA URLs above → place under `data/raw/cba/<edition>/original.pdf` (gitignored).  
   - Optional helper: `hoops_data.cba.fetch_manifest` that records URL + expected sha256 without committing bytes (or commits only hash + URL).

2. **Provenance sidecar (committed)**  
   - `data/cba/<edition>/metadata.yaml`: `edition_id`, `effective_dates`, `source_url`, `retrieval_date`, `original_sha256`, `extractor`, `text_fidelity`, `rights_note` ("not redistributed; local raw only").

3. **Deterministic parse**  
   - Extract text locally (pdftotext / pymupdf) → gitignored `text.txt`.  
   - Parse **Articles → Sections → Exhibits/Appendices** (CBA TOC is Article/Section-heavy; 2023 opens with ARTICLE I DEFINITIONS, ARTICLE II UNIFORM PLAYER CONTRACT, … plus Exhibit A UPC, etc.).  
   - Stable clause IDs, e.g. `cba:2023:art-VII:sec-10` (BRI / Audit Report style cites).

4. **Derived JSON (safe to commit if text omitted or truncated)**  
   Suggested `data/cba/<edition>/derived/structure.json` shape:
   - `articles[]`: `{ id, number, title, page_start?, sections[{ id, number, title, page_start? }] }`
   - `exhibits[]`
   - `defined_terms[]` from Article I (term → section locator; **definition body optional / local-only**)
   - `cross_refs[]` ("Article VII, Section 3", "Exhibit A")
   - `salary_cap_index[]`: headings / section IDs matching BRI, Cap, Apron, Tax, Escrow, Exceptions, Soft Cap, etc. (keyword rules, labelled unreviewed)
   - `_derived`, `_disclaimer`, `source_pdf_sha256`

5. **Writer UX (beside Scrivener)**  
   - CLI: `uv run python -m hoops_data.cba lookup "VII.3"` / `lookup "apron"` → prints locator + optional local snippet.  
   - CSV/JSON join to Scrivener binder via existing `docs/CHAPTER-MAP.md` / `data/mentions.csv` rows (`cba_clause_id`, `edition`, `note`).  
   - Optional: thin MCP or Cursor rule that resolves clause IDs without pasting full CBA into chat logs.

### What MVP deliberately skips

- Committing full PDF or full extracted text to public git  
- Multi-edition semantic diff UI (P1)  
- LLM "explain this clause" as authority (never)  
- OCR path unless a future scan-only exhibit appears (2023/2017 PDFs appear text-extractable — UNCONFIRMED full audit)

---

## 4. P0 / P1 / P2 build plan for @engineer

### P0 — Foundation (1–3 days)

- [ ] Add `src/hoops_data/cba/` with `hashing.py` (copy corpus conventions: `sha256:` prefix + text normalize)
- [ ] `metadata.schema.json` + sample `metadata.yaml` for **2023** and **2017**
- [ ] Document download → `data/raw/cba/...` in README; extend `.gitignore`
- [ ] `extract.py`: pdftotext/pymupdf → local `text.txt`; record toolchain versions
- [ ] `build_structure.py`: Article / Section / Exhibit headers → `structure.json` **without** full body text in the committed artifact (titles + IDs + page numbers if available)
- [ ] `validate.py`: metadata schema + hash file exists locally + structure schema
- [ ] One golden fixture: committed structure for 2023 built from a known PDF hash (CI skips extract if raw absent; local + optional secret CI has raw)

### P1 — Writer-facing index (3–5 days)

- [ ] Article I defined-terms extractor → `defined_terms.json` (locator-first)
- [ ] Cross-ref detector adapted to "Article X, Section Y" / "Exhibit Z"
- [ ] Salary-cap / BRI heading index (rule-based, `review_status: unreviewed`)
- [ ] CLI `lookup` + wire 5–10 rows into `data/mentions.csv` for draft chapters that cite the CBA
- [ ] Dual-edition support (2017 vs 2023) with `edition_id` on every ID
- [ ] Minimal CI: schema validate committed derived files; hash-lock expected `original_sha256` for official URLs

### P2 — Hardening & editions (later)

- [ ] Page-map / PDF outline fallback when text layer headers are fragile
- [ ] Semantic diff of structure between 2017→2023 (section renumbers — known CBA hazard)
- [ ] Optional sibling public repo that ships **only** structure + hashes (no text)
- [ ] Watch script for NBA/NBPA PDF URL changes (corpus `watch_sources.py` analogue)
- [ ] Human review pass on salary-cap index; promote `review_status`

---

## 5. Risks

| Risk | Severity | Mitigation |
|------|----------|------------|
| **Copyright / republication** of CBA full text in public git | High | Gitignore raw + full text; commit structure/IDs/hashes/citations only; rights note in metadata |
| **PDF layout fragility** across 2011/2017/2023 editions (headers, two-column TOC, Exhibit formatting) | High | Per-edition recipe files (like corpus `RECIPES`); golden hashes; don't assume one regex forever |
| **Silent upstream PDF replace** (same URL, new bytes) | Medium | Store `original_sha256`; fail closed on mismatch |
| **OCR / bad text layer** | Medium (lower if digital PDFs) | Prefer pdftotext; spot-check Article I and Cap articles; fidelity flag |
| **Clause renumbering** between CBAs | High for multi-edition cites | Never cite bare "Art. VII" across editions without `edition_id` |
| **Over-trusting keyword "salary cap" tags** | Medium | Label unreviewed; writers confirm against PDF |
| **Treating Navigator-style full-text JSON as OK for CBA** | High (policy) | Explicitly reject committing Navigator-equivalent full CBA JSON publicly |
| **CHM-proto confusion** | Low | Confirmed: no agreement parser there — do not dig for one |

### UNCONFIRMED / honesty box

- Exact Article count / Exhibit list for 2023 vs 2017 not fully enumerated in this note (would require a local parse pass on the PDFs). TOC sampling from public search snippets shows Article I Definitions, Article II UPC, … through many articles + exhibits — **structure MVP should discover from PDF, not hard-code 79**.
- Whether NBA Official and NBPA 2023 PDFs are **byte-identical** is UNCONFIRMED (sizes differ: 2 903 978 vs 2 850 534) — treat as possibly distinct files; hash whichever the user actually uses and record that URL.
- Zenodo DOI for the BBNJ corpus was network-unverified in the 2026-09-09 landscape scan.
- No clone of `dacheah/bbnj-high-seas-treaty-corpus` was required; inspection used raw.githubusercontent.com + landscape notes (2026-09-19).

---

## Sources consulted (2026-09-19)

- https://github.com/glen-w/BBNJ (+ `reports/01-landscape.md`, `reports/repos/01-bbnj-high-seas-treaty-corpus.md`, `08-BBNJ-Navigator.md`)
- https://github.com/glen-w/BBNJ-CHM-proto (README — Cl-HM desk, not parser)
- https://github.com/dacheah/bbnj-high-seas-treaty-corpus (README, scripts, schemas, workflows, sample `structure.json`, `metadata.yaml`, hashing, LICENSE-derived)
- https://github.com/glen-w/hoops (README, `pyproject.toml` → package `hoops-data`)
- https://nbpa.com/cba ; NBA Official CBA PDF URLs listed in §2

---

*End of feasibility note. Next artifact for writers/data: `/workspace/hoops-thicken-efficiency-income-2026-09-19/` (source map only).*
