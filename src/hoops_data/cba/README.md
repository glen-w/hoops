# hoops_data.cba — CBA Structure Extraction Package

Productized NBA CBA structure extraction toolkit with golden hash validation and TOC regression testing.

## Overview

This package provides deterministic extraction of structural metadata from NBA Collective Bargaining Agreement PDFs:

- **`hashing.py`** — Canonical SHA-256 hashing with `sha256:` prefix
- **`extract.py`** — PDF text extraction using `pdftotext` with page tracking
- **`build_structure.py`** — Structure parser (articles, sections, exhibits)
- **`validate.py`** — Schema validation, TOC regression, golden hash checks

## Architecture

### Extraction Pipeline

```
PDF → pdftotext → ExtractedText → CBAParser → CBAStructure → JSON
                      ↓                           ↓
                  page_map                  validation
```

### Key Features

1. **Golden Hash Validation**: 2023 edition locked to spike-validated PDF hash
2. **TOC Regression**: Expected counts (42 art / 279 sec / 17 exh)
3. **Canonical Clause IDs**: `cba:2023:art-VII:sec-6` format
4. **Spike Hazard Fix**: `splitlines()` before stripping form-feed

## Usage

### Basic Extraction

```python
from pathlib import Path
from hoops_data.cba import extract, build_structure, hashing

# Extract text
pdf_path = Path("data/raw/cba/2023/cba.pdf")
extracted = extract.extract_text_with_layout(pdf_path)

# Compute PDF hash
pdf_hash = hashing.compute_file_hash(pdf_path)

# Build structure
structure = build_structure.build_structure(
    edition="2023",
    extracted_text=extracted,
    source_sha256=pdf_hash,
    source_url="https://nbpa.com/cba",
)

# Access units
for unit in structure.units:
    print(f"{unit.id}: {unit.title} (p. {unit.page_start})")
```

### Validation

```python
from hoops_data.cba import validate

# Validate structure
result = validate.validate_all(structure.to_dict())

if result.passed:
    print("✓ All validations passed")
else:
    print(result.summary())
```

### Hashing

```python
from hoops_data.cba import hashing

# File hash (binary)
pdf_hash = hashing.compute_file_hash("cba.pdf")
# Returns: "sha256:cf59d43..."

# Text hash (canonical UTF-8 + LF + trailing newline)
text_hash = hashing.compute_text_hash(text)
# Returns: "sha256:abc123..."

# Strip prefix if needed
raw = hashing.strip_prefix(pdf_hash)
# Returns: "cf59d43..."
```

## Clause ID Format

Canonical clause IDs follow the pattern:

- **Article**: `cba:{edition}:art-{roman}`
  - Example: `cba:2023:art-VII`
- **Section**: `cba:{edition}:art-{roman}:sec-{num}`
  - Example: `cba:2023:art-VII:sec-6`
- **Exhibit**: `cba:{edition}:exh-{id}`
  - Example: `cba:2023:exh-A`

## Golden Hash

2023 edition locked to spike-validated source:

```
sha256:cf59d43fe46f63d7ba07364563046d766c487c26032fcc88432310d47effd9d9
```

Ensures deterministic extraction from NBA Official 2023 Final PDF.

## TOC Regression

For 2023 edition, validation enforces spike-proven counts:

| Type | Count |
|------|-------|
| Articles | 42 |
| Sections | 279 |
| Exhibits | 17 |

## Spike Hazard Fix

**Critical**: The spike revealed that stripping form-feed (`\f`) characters before splitting lines can merge text from different pages. 

**Solution**: Always call `splitlines()` before processing form-feeds.

```python
# ✓ CORRECT
lines = raw_text.splitlines()
lines = [line.replace("\f", "") for line in lines]

# ✗ INCORRECT (can merge pages)
text = raw_text.replace("\f", "")
lines = text.splitlines()
```

## Dependencies

- **pdftotext** (from poppler-utils) — PDF text extraction
  - Ubuntu/Debian: `sudo apt-get install poppler-utils`
  - macOS: `brew install poppler`
- **jsonschema** — Structure validation

## CLI Tools

See `scripts/cba/` for command-line tools:

- `extract_cba.py` — Extract structure from PDF
- `validate_cba_structure.py` — Validate structure files
- `cba_lookup.py` — Query committed structure metadata

## See Also

- [scripts/cba/README.md](../../../scripts/cba/README.md) — CLI tools documentation
- [docs/cba-structure-pipeline.md](../../../docs/cba-structure-pipeline.md) — Full pipeline docs
- [schemas/cba_structure.schema.json](../../../schemas/cba_structure.schema.json) — JSON schema
