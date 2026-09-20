# NBA CBA Source Files

This directory contains **user-supplied** NBA Collective Bargaining Agreement PDFs.

## ⚠️ Not in Git

CBA PDFs are **gitignored** and must be provided locally. The league and NBPA retain copyright over CBA text. This repository commits structural metadata (article/section/exhibit indexes, page ranges, content hashes) to [`data/cba/`](../../cba/README.md). `data/derived/cba/` is an older fixture with a different JSON shape. Do not treat the two trees as copies.

## Source

**Official source:** [NBPA CBA page](https://nbpa.com/cba)

**Editions supported:**
- **2023** (primary) — 2023–2030 CBA
- **2017** — 2017–2024 CBA (historical reference)

## How to Use

1. **Download the CBA PDF** from the official NBPA source
2. **Place it locally:**
   - `data/raw/cba/2023/cba.pdf` (for 2023 edition)
   - `data/raw/cba/2017/cba.pdf` (for 2017 edition)
3. **The committed indexes are already in** `data/cba/<edition>/derived/`. Lookup reads that tree first.
4. **If you regenerate,** `scripts/cba/extract_cba.py` writes `data/cba/<edition>/derived/structure.json` by default. The deprecated `build_cba_structure.py` writes the older fixture shape under `data/derived/cba/`. Do not overwrite one tree with the other's output.

## File Provenance

When you download a CBA PDF, record:

| Edition | Source URL | Fetch Date | SHA-256 |
|---------|-----------|------------|---------|
| 2023    | https://nbpa.com/cba | YYYY-MM-DD | `<computed by script>` |
| 2017    | https://nbpa.com/cba | YYYY-MM-DD | `<computed by script>` |

The build script computes and stores the SHA-256 hash in `structure.json` automatically.

## Regenerating

`scripts/cba/ci_validate.sh` still diffs a regeneration against `data/derived/cba/`, the fixture tree. It does not check the indexes in `data/cba/`. If the PDF is absent, that script skips extraction.

## Integration with CHAPTER-MAP

Chapters referencing CBA articles (e.g., salary cap, defined terms) can use `scripts/cba_lookup.py` for clause IDs and page ranges. Status `needs_local_pdf` until PDF is regenerated locally. *(Infra owns actual CHAPTER-MAP rows.)*

## License Note

The CBA text is proprietary. Structural metadata (table of contents, section IDs, page ranges) falls under fair use for research and documentation purposes. This repository does **not** redistribute CBA body text.
