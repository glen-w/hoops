# CBA Structure Extraction Scripts

Scripts for extracting and validating NBA Collective Bargaining Agreement (CBA) structural metadata.

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements-cba.txt
```

### 2. Download CBA PDF

Download from [NBPA](https://nbpa.com/cba) and place at:
- `data/raw/cba/2023/cba.pdf` (for 2023 edition)
- `data/raw/cba/2017/cba.pdf` (for 2017 edition)

### 3. Extract Structure

```bash
python scripts/cba/build_cba_structure.py \
    --edition 2023 \
    --pdf data/raw/cba/2023/cba.pdf
```

### 4. Validate

```bash
python scripts/cba/validate_cba_structure.py \
    data/derived/cba/2023/structure.json
```

## Scripts

### `build_cba_structure.py`

Extract structural metadata from CBA PDF.

**Usage:**
```bash
python scripts/cba/build_cba_structure.py \
    --edition {2017|2023} \
    --pdf PATH_TO_PDF \
    [--output OUTPUT_PATH] \
    [--source-url URL]
```

**Arguments:**
- `--edition`: CBA edition year (2017 or 2023)
- `--pdf`: Path to CBA PDF file
- `--output`: Output path for structure.json (default: `data/derived/cba/{edition}/structure.json`)
- `--source-url`: Official source URL (default: https://nbpa.com/cba)

**Output:**
- `data/derived/cba/{edition}/structure.json` — Structural metadata

**Example:**
```bash
python scripts/cba/build_cba_structure.py \
    --edition 2023 \
    --pdf data/raw/cba/2023/cba.pdf
```

### `validate_cba_structure.py`

Validate structure JSON files against schema.

**Usage:**
```bash
python scripts/cba/validate_cba_structure.py \
    FILE [FILE ...] \
    [--strict]
```

**Arguments:**
- `FILE`: Path(s) to structure.json file(s)
- `--strict`: Exit with non-zero code on any validation failure

**Example:**
```bash
python scripts/cba/validate_cba_structure.py \
    data/derived/cba/2023/structure.json \
    --strict
```

### `ci_validate.sh`

CI validation script. Regenerates and validates structures.

**Usage:**
```bash
bash scripts/cba/ci_validate.sh
```

**Behavior:**
- If PDF present: regenerate and diff against committed structure
- If PDF absent: validate fixture and committed structure only

## See Also

- Full documentation: [`docs/cba-structure-pipeline.md`](../../docs/cba-structure-pipeline.md)
- Schema: [`schemas/cba_structure.schema.json`](../../schemas/cba_structure.schema.json)
- Source README: [`data/raw/cba/README.md`](../../data/raw/cba/README.md)
- Derived README: [`data/derived/cba/README.md`](../../data/derived/cba/README.md)
