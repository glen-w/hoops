# NBA CBA Source Files

This directory contains **user-supplied** NBA Collective Bargaining Agreement PDFs.

## ⚠️ Not in Git

CBA PDFs are **gitignored** and must be provided locally. The league and NBPA retain copyright over CBA text. This repository commits only **derived structural metadata** (article/section/exhibit IDs, titles, page ranges, content hashes) to `data/derived/cba/`.

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
3. **Run the extraction script:**
   ```bash
   python scripts/cba/build_cba_structure.py --edition 2023 --pdf data/raw/cba/2023/cba.pdf
   ```
4. **Commit only the derived structure:**
   ```bash
   git add data/derived/cba/2023/structure.json
   git commit -m "Update 2023 CBA structure"
   ```

## File Provenance

When you download a CBA PDF, record:

| Edition | Source URL | Fetch Date | SHA-256 |
|---------|-----------|------------|---------|
| 2023    | https://nbpa.com/cba | YYYY-MM-DD | `<computed by script>` |
| 2017    | https://nbpa.com/cba | YYYY-MM-DD | `<computed by script>` |

The build script computes and stores the SHA-256 hash in `structure.json` automatically.

## Regenerating

If the PDF is present, CI validation will regenerate structure and diff it against the committed version. If the PDF is absent, CI skips extraction with a clear message.

## License Note

The CBA text is proprietary. Structural metadata (table of contents, section IDs, page ranges) falls under fair use for research and documentation purposes. This repository does **not** redistribute CBA body text.
