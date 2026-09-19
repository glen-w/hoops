# NBA CBA Structure Extraction Pipeline

This document describes the deterministic pipeline for extracting structural metadata from NBA Collective Bargaining Agreement (CBA) PDFs.

## Overview

The CBA structure pipeline converts official NBA CBA PDFs into machine-readable structural metadata suitable for analysis and cross-referencing. The pipeline commits **only derived artifacts** (structural metadata), never the fulltext of the CBA itself.

### Pipeline Flow

```
User-supplied PDF (local, gitignored)
    ↓
Extract text with page tracking
    ↓
Parse structural markers (articles, sections, exhibits)
    ↓
Emit structure.json with metadata (no body text)
    ↓
Validate against JSON schema
    ↓
Commit to data/derived/cba/{edition}/structure.json
```

## Intellectual Property Constraints

**Critical:** The CBA text is proprietary and copyrighted by the NBA and NBPA. This repository:

- ✅ **Commits:** Structural metadata (IDs, titles, page ranges, content hashes)
- ❌ **Never commits:** PDF files, extracted fulltext, or substantial quoted body text
- 📍 **Source of truth:** [NBPA CBA page](https://nbpa.com/cba)

This is a **host-of-record pattern**: the authoritative text lives at NBPA; this repo provides tooling and derived metadata for research purposes under fair use.

## Supported Editions

| Edition | Years | Status |
|---------|-------|--------|
| **2023** | 2023–2030 | Primary (P0) |
| **2017** | 2017–2024 | Historical reference |

## Directory Structure

```
hoops/
├── data/
│   ├── raw/
│   │   └── cba/              # ← gitignored
│   │       ├── 2023/
│   │       │   └── cba.pdf   # User-supplied, not committed
│   │       └── 2017/
│   │           └── cba.pdf
│   └── derived/
│       └── cba/              # ← committed
│           ├── 2023/
│           │   ├── structure.json         # Generated metadata
│           │   └── structure.fixture.json # CI fixture
│           └── 2017/
│               └── structure.json
├── scripts/
│   └── cba/
│       ├── build_cba_structure.py    # Extraction script
│       ├── validate_cba_structure.py # Validation
│       └── ci_validate.sh            # CI entry point
└── schemas/
    └── cba_structure.schema.json     # JSON Schema
```

## Usage

### Step 1: Download CBA PDF

Download the official CBA PDF from [NBPA](https://nbpa.com/cba) and place it locally:

```bash
# For 2023 edition
mkdir -p data/raw/cba/2023
# (download manually and place at data/raw/cba/2023/cba.pdf)

# For 2017 edition
mkdir -p data/raw/cba/2017
# (download manually and place at data/raw/cba/2017/cba.pdf)
```

### Step 2: Install Dependencies

```bash
pip install -r requirements-cba.txt
```

Dependencies:
- `pymupdf` — PDF text extraction
- `jsonschema` — Schema validation

### Step 3: Extract Structure

```bash
python scripts/cba/build_cba_structure.py \
    --edition 2023 \
    --pdf data/raw/cba/2023/cba.pdf
```

This generates `data/derived/cba/2023/structure.json`.

### Step 4: Validate

```bash
python scripts/cba/validate_cba_structure.py \
    data/derived/cba/2023/structure.json
```

### Step 5: Commit (Derived Only)

```bash
git add data/derived/cba/2023/structure.json
git commit -m "Update 2023 CBA structure"
git push
```

**Never commit** the PDF or extracted fulltext.

## Structure Format

### JSON Schema

Defined in `schemas/cba_structure.schema.json`.

### Example Structure

```json
{
  "edition": "2023",
  "source_sha256": "abc123...",
  "source_url": "https://nbpa.com/cba",
  "generated_at": "2026-09-19T13:00:00Z",
  "units": [
    {
      "id": "article_1",
      "type": "article",
      "title": "Article I: DEFINITIONS",
      "parent_id": null,
      "page_start": 5,
      "page_end": 12,
      "char_offset_start": 1234,
      "char_offset_end": 5678,
      "text_sha256": "def456..."
    },
    {
      "id": "article_1_section_1",
      "type": "section",
      "title": "Section 1. Definitions",
      "parent_id": "article_1",
      "page_start": 5,
      "page_end": 7,
      "char_offset_start": 1234,
      "char_offset_end": 3456,
      "text_sha256": "ghi789..."
    }
  ]
}
```

### Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| `edition` | string | CBA edition year ("2017", "2023") |
| `source_sha256` | string | SHA-256 hash of source PDF (for provenance) |
| `source_url` | string | Official source URL |
| `generated_at` | string | ISO 8601 timestamp of extraction |
| `units` | array | Structural units (articles, sections, exhibits) |

#### Unit Fields

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Unique identifier (e.g., "article_1", "article_1_section_1") |
| `type` | enum | "article", "section", "subsection", "exhibit", "appendix" |
| `title` | string | Unit title (truncated to 200 chars) |
| `parent_id` | string\|null | Parent unit ID (null for top-level) |
| `page_start` | int\|null | Starting page number (1-indexed) |
| `page_end` | int\|null | Ending page number (inclusive) |
| `char_offset_start` | int\|null | Character offset in extracted fulltext |
| `char_offset_end` | int\|null | Character offset end in extracted fulltext |
| `text_sha256` | string\|null | SHA-256 hash of unit's fulltext (not stored) |

**Important:** `text_sha256` is a hash **of the text content**, not the text itself. The fulltext is never committed.

## Parsing Logic

### Regex Patterns

The parser uses regex patterns to identify structural markers:

1. **Articles:** `ARTICLE [IVXLCDM]+` (Roman numerals)
   - Example: "ARTICLE I DEFINITIONS", "ARTICLE VII TEAM SALARY CAP"

2. **Sections:** `Section \d+`
   - Example: "Section 1. Player Contracts", "Section 12. Trade Restrictions"

3. **Exhibits:** `EXHIBIT [A-Z0-9]+`
   - Example: "EXHIBIT A", "EXHIBIT 1A"

### Hierarchy Construction

- **Articles** are top-level (`parent_id: null`)
- **Sections** are children of the most recent article
- **Exhibits** are typically top-level

The parser tracks character offsets and maps them to page numbers for accurate positioning.

### Limitations and Known Issues

- **Multi-column layouts:** May require manual adjustment if section detection fails
- **Nested subsections:** Currently limited; extend parser if needed
- **Exhibit structure:** Some exhibits may have internal subsections not yet parsed
- **TOC vs. body:** Parser extracts from body text, not table of contents

**Hypothesis (from requirements):** Heading regex on "ARTICLE [IVXLC]+" / "Section N." will capture most of the 2023 CBA structure. Exhibits may require a second pass.

## CI Validation

### Behavior

The `scripts/cba/ci_validate.sh` script:

1. **If PDF is present:**
   - Regenerate structure
   - Diff against committed version
   - Fail if mismatch (structure drift)

2. **If PDF is absent:**
   - Validate fixture (if present)
   - Validate committed structure (if present)
   - Skip extraction with clear message

### Running CI Locally

```bash
bash scripts/cba/ci_validate.sh
```

### GitHub Actions Integration (Future)

```yaml
# .github/workflows/cba-validation.yml
name: CBA Structure Validation
on: [push, pull_request]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - run: pip install -r requirements-cba.txt
      - run: bash scripts/cba/ci_validate.sh
```

## Fixtures for Testing

### Purpose

The `structure.fixture.json` files provide minimal valid structures for CI validation when PDFs are unavailable. They contain:

- Public TOC-level article titles (from NBPA website)
- Null values for page/offset/hash fields
- Placeholder SHA-256 (all zeros)

### Using Fixtures

Fixtures validate schema compliance without requiring the PDF. To test with a fixture:

```bash
python scripts/cba/validate_cba_structure.py \
    data/derived/cba/2023/structure.fixture.json
```

## Regenerating After Source Updates

If NBPA publishes an updated CBA:

1. Download the new PDF
2. Place it at `data/raw/cba/{edition}/cba.pdf`
3. Run extraction: `python scripts/cba/build_cba_structure.py --edition {edition} --pdf data/raw/cba/{edition}/cba.pdf`
4. Review the diff: `git diff data/derived/cba/{edition}/structure.json`
5. Commit if changes are valid

## Future Enhancements

Potential extensions (not required for initial scaffold):

1. **Terms index:** `data/derived/cba/{edition}/terms.json` with defined terms and their locations
2. **Cross-references:** Track internal references ("as defined in Section X")
3. **Change detection:** Diff structures between editions (2017 vs. 2023)
4. **Subsection parsing:** Extend parser to capture subsections (e.g., "Section 1(a)")
5. **Exhibit internals:** Parse exhibit subsections if structured
6. **NLP enhancement:** Use NLP to improve section boundary detection

## Related Work

This scaffold is modeled on the **shape** of [`dacheah/bbnj-high-seas-treaty-corpus`](https://github.com/dacheah/bbnj-high-seas-treaty-corpus), which extracts structural metadata from UN High Seas Treaty text. The pattern:

- Commit only structure, not fulltext
- Document source provenance
- Provide deterministic regeneration pipeline
- Validate with JSON schema

This is **not** a fork of `glen-w/BBNJ` (landscape scan), but inspired by the BBNJ corpus extraction pattern.

## License and Fair Use

**CBA text:** Proprietary (NBA and NBPA). Not redistributed in this repository.

**Structural metadata:** Fair use for research and documentation. This repository commits:
- Table of contents structure
- Section IDs and titles
- Page ranges
- Content hashes (not content)

Quoting short titles (e.g., "Article I: DEFINITIONS") falls under fair use. The repository does not reproduce substantial body text.

## Questions and Support

For issues with the extraction pipeline, open an issue on the `glen-w/hoops` repository.

For questions about CBA content or official text, refer to the [NBPA](https://nbpa.com/cba).
