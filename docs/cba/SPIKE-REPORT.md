# Spike report: corpus-style NBA CBA parse (glen-w/hoops)

**Access / run date:** 2026-09-19 (Europe/Paris, UTC+2)  
**Brief:** `/workspace/hoops-cba-parser-feasibility-2026-09-19.md`  
**Spike root:** `/workspace/hoops-cba-spike/` (box scratch only)

---

## 1. What we did

| Step | Result |
|------|--------|
| Download official 2023 Final PDF | **HTTP 200** from NBA ak-static |
| Size | **2 903 978** bytes (matches feasibility table) |
| SHA-256 | `sha256:cf59d43fe46f63d7ba07364563046d766c487c26032fcc88432310d47effd9d9` |
| Extract | **pdftotext 25.03.0** (poppler-utils); layout + no-layout variants |
| Structure split | Articles → Sections → Exhibits → `derived/structure.json` |
| Indexes | `derived/defined_terms.json`, `derived/headings_index.json` (incl. salary-cap / MLE) |

**Source URL used:**  
`https://ak-static.cms.nba.com/wp-content/uploads/sites/4/2024/06/2023-NBA-Collective-Bargaining-Agreement-Final.pdf`

**Not used this spike:** NBPA imgix twin (different byte size in feasibility note — treat as possibly distinct file; hash whichever edition you ingest).

---

## 2. Layout of spike artifacts

```
hoops-cba-spike/
  SPIKE-REPORT.md          ← this file (safe summary)
  .gitignore               ← ignores raw PDF + full text extracts
  scripts/parse_cba_spike.py
  raw/                     ← LOCAL ONLY — do not commit to public git
    2023-NBA-CBA-Final.pdf
    text.txt               ← pdftotext -layout (~1.52 MB)
    text-nolayout.txt      ← pdftotext default (~1.35 MB) ← parser input
    metadata.json          ← URL, hashes, retrieval_date, rights_note
    original.sha256
  derived/                 ← structure metadata + ≤500-char previews only
    structure.json
    defined_terms.json
    headings_index.json
```

---

## 3. What worked

### Fetch / extract

- Official PDF fetches cleanly (200, `application/pdf`).
- Digital text layer is strong: **686 pages**, Acrobat PDFMaker/Word origin; no OCR needed for body articles.
- `pdftotext` without `-layout` yields the cleanest `ARTICLE N` / `Section N.` headers for regex splitting.
- `-layout` preserves TOC alignment but is noisier for body headers (prefer no-layout for structure, keep layout optional for page-ish reads).

### Deterministic structure (sample-validated)

| Unit | Count | Notes |
|------|------:|-------|
| Articles | **42** (I–XLII) | Matches TOC enumeration |
| Exhibits | **17** (A–H, I-1…I-7, J-1, J-2) | Body exhibits after Art XLII |
| Sections (parsed) | **279** | Across all articles |

**TOC spot-check (expected vs parsed) — all OK:**

| Article | Expected §§ | Parsed |
|---------|------------:|-------:|
| I | 1 | 1 |
| II | 15 | 15 |
| VII | 12 | 12 |
| X | 10 | 10 |
| XI | 5 | 5 |

Stable clause ID shape (as proposed in feasibility): `cba:2023:art-VII:sec-6`.

**Article VII** title and sections land correctly, including:

- §2 Salary Cap / Tax Level / Apron  
- §6 Exceptions to the Salary Cap  
- §12 Designated Share Arrangement  

### Defined terms / cap index

- Article I yielded **83** term entries (lettered + fallback quote/`means` scan); locator-first with truncated definition previews.
- Art VII §6 exception subsection scan found **11** exception heads, including all three Mid-Level variants:
  - Non-Taxpayer Mid-Level Salary Exception `(e)`
  - Taxpayer Mid-Level Salary Exception `(f)`
  - Mid-Level Salary Exception for Room Teams `(g)`
- `salary_cap_index` (31 hits) tags salary cap / BRI / luxury tax / apron / MLE units — labelled `review_status: unreviewed`.

### Provenance pattern (transfers from BBNJ corpus)

- PDF SHA-256 + text SHA-256 recorded in `raw/metadata.json` and mirrored on derived roots.
- `_derived` + `_disclaimer` + `rights_note` on derived JSON.
- Two-layer wall: full bytes/text in `raw/`; commit-shaped material in `derived/` (previews ≤500 chars).

---

## 4. Failure modes / hazards (engineer must plan for)

1. **Copyright / republication (policy, not parse)**  
   CBA is a private NBA/NBPA labor agreement. Publication on NBA/NBPA sites ≠ permission to rehost. **Do not commit PDF or full `text*.txt` to public `glen-w/hoops`.** Prefer gitignored `data/raw/cba/` + committed metadata/structure/hashes/previews.

2. **Form-feed / `splitlines()` footgun**  
   Python `str.splitlines()` treats `\x0c` as a line break. Doing `text.replace("\x0c","").splitlines()` **merges** page-boundary lines and shifts article bounds (false “Art I bleeds into Art II”). **Always `splitlines()` first, then strip `\x0c` per line.**

3. **Section header ambiguity**  
   Body uses both `Section N.` alone and `Section N. Title` on one line. Mid-sentence cross-refs often appear as a lone `Section N.` after a comma wrap (`… Article VII,\nSection 7.`). Mitigation used: context check + **monotonic section-number filter**. Still fragile for P0→P1 without TOC golden counts per article.

4. **Articles without sections**  
   XVI, XVII, XXXIV, XXXV are prose-only (section_count 0). Title collector must stop on prose (ALL-CAPS bias); otherwise titles swallow body.

5. **Running headers / page numbers**  
   `Article VII` + bare page integers intercalate; must ignore when collecting titles/sections.

6. **Defined-term wraps**  
   Common pattern: `(a)\n"Term" means`. Requires join before regex. Mixed curly/straight quotes. Alphabet restarts / multi-pass definitions → letter in locator is ambiguous without deeper parsing. Fallback unlettered locators dilute precision (83 terms, only ~25 with `(letter)` locators).

7. **MLE / Tax / Apron live in Art VII, not Art I**  
   Art I has generic `"Exception"` and BRI pointer; operational Mid-Level / Tax Level / Apron math is under **Article VII**. Keyword index on titles alone under-tags; subsection scan of §6 is required for MLE.

8. **Nested exception letters**  
   Under Traded Player Exception, nested `(i)` / `(ii)` (Standard vs Aggregate) can collide with top-level `(i)` Minimum Player Salary Exception if the scanner is naive. Spike kept both; IDs need hierarchy for production (`sec-6:(j):(i)`).

9. **Keyword false positives**  
   `salary_cap` tag fires on any section preview mentioning “Salary Cap” (e.g. Art II max salary). Keep `review_status: unreviewed`; do not treat as authority.

10. **Edition twin PDFs**  
    NBA Official vs NBPA 2023 files differ in size (feasibility). Hash the bytes you actually use; do not assume identical.

11. **pymupdf**  
    Not installed on this box; spike used poppler only (aligned with BBNJ corpus primary). Optional second extractor for cross-check / outline bookmarks remains P1.

12. **Multi-edition renumbering**  
    Unexercised here; citing bare “Art. VII” across 2017→2023 without `edition_id` remains a known writer hazard.

---

## 5. Recommended P0 for @engineer (hoops)

Ship the **architecture**, not a full-text corpus:

1. **`src/hoops_data/cba/`**  
   - `hashing.py` (`sha256:` prefix; canonical text: UTF-8, LF, trailing newline)  
   - `extract.py` (pdftotext primary; record toolchain version)  
   - `build_structure.py` (Article / Section / Exhibit; **no full body in committed JSON**)  
   - `validate.py` (schema + local hash presence)

2. **Paths**  
   - Raw: `data/raw/cba/2023/original.pdf` + `text.txt` (**gitignore**)  
   - Committed: `data/cba/2023/metadata.yaml` + `derived/structure.json` (IDs, titles, page/line locators, short previews or none)

3. **Golden fixture**  
   - Lock `original_sha256` = `sha256:cf59d43fe46f63d7ba07364563046d766c487c26032fcc88432310d47effd9d9` for the NBA Official 2023 Final URL above.  
   - CI: validate committed structure when raw absent; full extract job only when raw present (local / private).

4. **TOC-driven validation**  
   - Per-edition expected section counts (at least I, II, VII, X, XI as in this spike) as a regression gate.

5. **README / rights**  
   - Explicit: cite & local raw only; never publish full CBA text. Mirror hoops “cite, don’t rehost” policy.

**Defer to P1:** defined-terms completeness, cross-ref detector, salary-cap index review, CLI `lookup`, 2017 dual-edition, pymupdf outline fallback.

---

## 6. Copyright reminder (non-lawyer)

- The 2023 NBA/NBPA Collective Bargaining Agreement is **copyrighted**.
- Official PDFs are published for reading; that is **not** an open license to republish the full text or PDF in a public git repo.
- This spike keeps full PDF + full extracts under `/workspace/hoops-cba-spike/raw/` (box scratch + `.gitignore`).
- Derived JSON here uses **structure metadata + ≤500-character previews only**.
- For `glen-w/hoops`: commit hashes, URLs, clause IDs, titles, and optional tiny previews — **not** `original.pdf` / full `text.txt`.

---

## 7. Quick numbers (2026-09-19)

| Metric | Value |
|--------|------:|
| HTTP | 200 |
| PDF bytes | 2 903 978 |
| PDF pages | 686 |
| PDF SHA-256 | `cf59d43fe46f63d7ba07364563046d766c487c26032fcc88432310d47effd9d9` |
| Articles | 42 |
| Exhibits | 17 |
| Sections parsed | 279 |
| Defined terms (spike) | 83 |
| Salary-cap index hits | 31 |
| MLE subsection hits | 3 |
| Extractor | pdftotext 25.03.0 |
| pymupdf | not installed |

---

*End of spike report. Feasibility parent: `hoops-cba-parser-feasibility-2026-09-19.md`.*
