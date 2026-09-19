# CBA Structure Extraction Scripts

Productized tools for extracting and validating NBA Collective Bargaining Agreement (CBA) structural metadata.

Built on the `hoops_data.cba` package for deterministic parsing with golden hash validation and TOC regression tests.

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements-cba.txt
```

**Note:** Also requires `pdftotext` (from poppler-utils):
- Ubuntu/Debian: `sudo apt-get install poppler-utils`
- macOS: `brew install poppler`
- Windows: [Download poppler](https://blog.alivate.com.au/poppler-windows/)

### 2. Download CBA PDF

Download from [NBPA](https://nbpa.com/cba) and place at:
- `data/raw/cba/2023/cba.pdf` (for 2023 edition)
- `data/raw/cba/2017/cba.pdf` (for 2017 edition)

### 3. Extract Structure

```bash
python scripts/cba/extract_cba.py \
    --edition 2023 \
    --pdf data/raw/cba/2023/cba.pdf
```

### 4. Validate

```bash
python scripts/cba/validate_cba_structure.py \
    data/derived/cba/2023/structure.json
```

## Scripts

### `extract_cba.py` ⭐ **Primary Tool**

Extract structural metadata from CBA PDF with validation.

**Usage:**
```bash
python scripts/cba/extract_cba.py \
    --edition {2017|2023} \
    --pdf PATH_TO_PDF \
    [--output OUTPUT_PATH] \
    [--source-url URL] \
    [--validate-hash] \
    [--skip-validation]
```

**Arguments:**
- `--edition`: CBA edition year (2017 or 2023)
- `--pdf`: Path to CBA PDF file
- `--output`: Output path (default: `data/derived/cba/{edition}/structure.json`)
- `--source-url`: Official source URL (default: https://nbpa.com/cba)
- `--validate-hash`: Strict golden hash validation (2023 only)
- `--skip-validation`: Skip validation after extraction

**Features:**
- Uses `pdftotext` for extraction (spike-validated toolchain)
- Generates clause IDs: `cba:2023:art-VII:sec-6`
- Golden hash validation for 2023 edition
- TOC regression tests (42 articles, 279 sections, 17 exhibits)

**Example:**
```bash
python scripts/cba/extract_cba.py \
    --edition 2023 \
    --pdf data/raw/cba/2023/cba.pdf \
    --validate-hash
```

### `validate_cba_structure.py`

Comprehensive validation with TOC regression and golden hash checks.

**Usage:**
```bash
python scripts/cba/validate_cba_structure.py \
    FILE [FILE ...] \
    [--strict] \
    [--skip-golden-hash] \
    [--verbose]
```

**Arguments:**
- `FILE`: Path(s) to structure.json file(s)
- `--strict`: Treat warnings as errors
- `--skip-golden-hash`: Skip golden hash validation
- `--verbose`: Show detailed validation output

**Validation Checks:**
- JSON schema compliance
- TOC regression (2023: 42 art / 279 sec / 17 exh)
- Golden hash match (2023)
- Structure integrity (parent refs, page ranges, hash formats)

**Example:**
```bash
python scripts/cba/validate_cba_structure.py \
    data/derived/cba/2023/structure.json \
    --strict
```

### `build_cba_structure.py` ⚠️ **Deprecated**

Legacy extraction script using PyMuPDF. Use `extract_cba.py` instead.
Maintained for backward compatibility only.

### `ci_validate.sh`

CI validation script for automated checks.

**Usage:**
```bash
bash scripts/cba/ci_validate.sh
```

**Behavior:**
- If PDF present: regenerate and diff against committed structure
- If PDF absent: validate fixture and committed structure only
- Runs TOC regression and golden hash validation

## Lookup Tool

### `cba_lookup.py` (at `scripts/`)

Query committed CBA structure metadata (lookup desk for Scrivener mid-draft).

**Usage:**
```bash
python scripts/cba_lookup.py "Article VII"
python scripts/cba_lookup.py --id cba:2023:art-VII:sec-6
python scripts/cba_lookup.py --term "Salary Cap"
python scripts/cba_lookup.py --list-articles
```

**Features:**
- Look up articles, sections, exhibits by name or ID
- Print edition, clause ID, title, page range
- No fulltext output (queries metadata only)
- Works with fixture (status `needs_local_pdf`) or full structure
- Supports both new clause IDs (`cba:2023:art-VII:sec-6`) and legacy IDs

**See:** [docs/CBA-LOOKUP.md](../../docs/CBA-LOOKUP.md) for detailed usage and Scrivener workflow.

## Package API

For programmatic use, import from `hoops_data.cba`:

```python
from hoops_data.cba import extract, build_structure, validate, hashing

# Extract text
extracted = extract.extract_text_with_layout(pdf_path)

# Build structure
structure = build_structure.build_structure(
    edition="2023",
    extracted_text=extracted,
    source_sha256=hashing.compute_file_hash(pdf_path),
)

# Validate
result = validate.validate_all(structure.to_dict())
if result.passed:
    print("✓ Valid")
```

## Clause ID Format

Structure uses canonical clause IDs:
- Articles: `cba:2023:art-VII`
- Sections: `cba:2023:art-VII:sec-6`
- Exhibits: `cba:2023:exh-A`

## Golden Hash

The 2023 edition is locked to the spike-validated golden hash:
```
sha256:cf59d43fe46f63d7ba07364563046d766c487c26032fcc88432310d47effd9d9
```

This ensures all extractions use the same canonical source (NBA Official 2023 Final PDF).

## TOC Regression Gates

For 2023 edition, expected counts from spike:
- **42 articles**
- **279 sections**
- **17 exhibits**

Validation fails if counts don't match spike results.

## Status Model: Lookup vs. Quotes

**Once `structure.json` is committed**, CBA operations split into two status levels:

| Operation | Status | Requires PDF? |
|-----------|--------|---------------|
| **Lookup** (clause ID, page range, structure) | ✅ **ready** | No — uses committed structure.json |
| **Quotes** (verbatim text extraction) | ⚠️ **quotes_need_pdf** | Yes — needs PDF bytes |

**UX Rule**: Don't block the writer desk on fulltext. Lookup queries return metadata (clause IDs, page ranges, structure) from committed JSON—no PDF needed. Only quote extraction requires PDF bytes.

## See Also

- Full documentation: [`docs/cba-structure-pipeline.md`](../../docs/cba-structure-pipeline.md)
- Lookup UX: [`docs/CBA-LOOKUP.md`](../../docs/CBA-LOOKUP.md)
- Schema: [`schemas/cba_structure.schema.json`](../../schemas/cba_structure.schema.json)
- Source README: [`data/raw/cba/README.md`](../../data/raw/cba/README.md)
- Derived README: [`data/derived/cba/README.md`](../../data/derived/cba/README.md)
- Lookup tool: [`scripts/cba_lookup.py`](../cba_lookup.py)
