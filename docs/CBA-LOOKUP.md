# CBA Lookup Desk

Quick reference CLI for querying NBA CBA structural metadata from Scrivener mid-draft.

## Purpose

When writing in Scrivener and you need to reference a CBA article, section, or defined term, use this tool to quickly look up:
- Edition (2017 or 2023)
- Clause ID (for cross-references)
- Title
- Page range / character span

**Important:** This tool queries **committed structure metadata only**. It does not access or print CBA body text (PDFs are gitignored).

## Status Model: Lookup vs. Quotes

**Once `structure.json` is committed**, CBA lookup queries are **ready** (not `needs_local_pdf`):

| Operation | Status | Requires PDF? |
|-----------|--------|---------------|
| **Lookup** (clause ID, page range, structure) | ✅ **ready** | No — uses committed structure.json |
| **Quotes** (verbatim text extraction) | ⚠️ **quotes_need_pdf** | Yes — needs PDF bytes |

**UX Rule**: Don't block the writer desk on fulltext. Once structure.json exists:
- Lookup queries → **ready** (returns clause IDs, page ranges, metadata)
- Quote extraction → **quotes_need_pdf** (requires PDF)

This split unblocks Scrivener drafting for structure-based references while clearly flagging where PDF bytes are still needed for verbatim quotes.

## Fixture vs. Full Structure

- **With committed structure.json:** Lookup queries fully ready; only quotes need PDF
- **With fixture only:** Lookup works for clause IDs and structure; page ranges may be null until regenerated

## Quick Start

### Look up Article VII (Salary Cap)

```bash
$ python scripts/cba_lookup.py "Article VII"

Edition: 2023
ID: article_7
Type: article
Title: Article VII: TEAM SALARY CAP
Pages: [fixture - needs_local_pdf]

Status: needs_local_pdf
(Fixture only - place PDF at data/raw/cba/2023/cba.pdf and regenerate)
```

**After PDF is local and regenerated:**

```bash
$ python scripts/cba_lookup.py "Article VII"

Edition: 2023
ID: article_7
Type: article
Title: Article VII: TEAM SALARY CAP
Pages: 42-58
Character span: 125432-178965 (53,533 chars)
```

### Look up by Unit ID

```bash
$ python scripts/cba_lookup.py --id article_7_section_1

Edition: 2023
ID: article_7_section_1
Type: section
Title: Section 1. Salary Cap Amount for 2023-24 Season
Parent: article_7
Pages: 42-44
Character span: 125432-132100 (6,668 chars)
```

### Search for a Defined Term

```bash
$ python scripts/cba_lookup.py --term "Salary Cap"

Edition: 2023
ID: article_1
Type: article
Title: Article I: DEFINITIONS
Pages: 5-18

Status: needs_local_pdf
```

**Note:** Term search is limited in v1 to definition-related articles. Full term indexing (`terms.json`) is a future enhancement.

### List All Articles

```bash
$ python scripts/cba_lookup.py --list-articles

Edition: 2023
ID: article_1
Type: article
Title: Article I: DEFINITIONS
Pages: [fixture - needs_local_pdf]
...

Total articles: 8
```

### Query 2017 CBA

```bash
$ python scripts/cba_lookup.py --edition 2017 "Article VII"
```

### Search Across Both Editions

```bash
$ python scripts/cba_lookup.py --all-editions "Article VII"

============================================================
Edition: 2017
============================================================
Edition: 2017
ID: article_7
Type: article
Title: Article VII: TEAM SALARY CAP
Pages: 40-55

============================================================
Edition: 2023
============================================================
Edition: 2023
ID: article_7
Type: article
Title: Article VII: TEAM SALARY CAP
Pages: 42-58
```

## Usage from Scrivener

### Scenario 1: Referencing a CBA Article in Draft

You're writing in Scrivener:

> The salary cap is governed by **Article VII** of the CBA (pages XX-XX).

**Workflow:**
1. Open terminal
2. Run: `python scripts/cba_lookup.py "Article VII"`
3. Note the page range: `42-58`
4. Update draft: "Article VII of the CBA (pages 42-58)"

### Scenario 2: Finding a Section ID for a Footnote

You want to add a precise footnote:

> See CBA Article VII, Section 1 for the salary cap calculation.

**Workflow:**
1. Run: `python scripts/cba_lookup.py --id article_7_section_1`
2. Get metadata:
   - **ID:** `article_7_section_1`
   - **Title:** "Section 1. Salary Cap Amount for 2023-24 Season"
   - **Pages:** 42-44
3. Draft footnote with precision: "CBA Art. VII §1 (pp. 42-44)"

### Scenario 3: Quick Article List

You're outlining a chapter on CBA structure and need a list of all articles:

**Workflow:**
1. Run: `python scripts/cba_lookup.py --list-articles`
2. Copy the list into Scrivener as a reference note

## CLI Reference

### Basic Usage

```bash
python scripts/cba_lookup.py [OPTIONS] [QUERY]
```

### Options

| Option | Description |
|--------|-------------|
| `QUERY` | Search query (article name, section, etc.) |
| `--edition {2017,2023}` | CBA edition to query (default: 2023) |
| `--id UNIT_ID` | Look up by exact unit ID |
| `--term TERM` | Search for defined term |
| `--list-articles` | List all top-level articles |
| `--all-editions` | Search across all available editions |

### Examples

```bash
# Article lookup
python scripts/cba_lookup.py "Article VII"

# Section lookup by ID
python scripts/cba_lookup.py --id article_7_section_1

# Term search
python scripts/cba_lookup.py --term "Salary Cap"

# List articles in 2017 CBA
python scripts/cba_lookup.py --edition 2017 --list-articles

# Compare across editions
python scripts/cba_lookup.py --all-editions "Article IV"
```

## Output Fields

| Field | Description |
|-------|-------------|
| **Edition** | CBA edition year (2017 or 2023) |
| **ID** | Unique unit identifier (for cross-references) |
| **Type** | Unit type (article, section, exhibit, etc.) |
| **Title** | Unit title (truncated to 200 chars) |
| **Parent** | Parent unit ID (if hierarchical) |
| **Pages** | Page range (e.g., "42-58") or `[fixture - needs_local_pdf]` |
| **Character span** | Character offsets in extracted fulltext (if PDF processed) |
| **Status** | `needs_local_pdf` when fixture only |

## Limitations (v1)

- ❌ **No fulltext output** — Body text is not stored in git and cannot be printed
- ❌ **No term index** — Defined term search is limited to article titles; full term indexing (`terms.json`) is a future enhancement
- ❌ **Fixture mode** — Without local PDF, only article titles and IDs are available
- ❌ **No web UI** — CLI only for v1

## Upgrading from Fixture to Full Structure

### Current State (Fixture Only)

```bash
$ python scripts/cba_lookup.py "Article VII"

Status: needs_local_pdf
(Fixture only - place PDF at data/raw/cba/2023/cba.pdf and regenerate)
```

### Steps to Upgrade

1. **Download CBA PDF** from [NBPA](https://nbpa.com/cba)
2. **Place at:** `data/raw/cba/2023/cba.pdf`
3. **Install dependencies:** `pip install -r requirements-cba.txt`
4. **Regenerate structure:**
   ```bash
   python scripts/cba/build_cba_structure.py \
       --edition 2023 \
       --pdf data/raw/cba/2023/cba.pdf
   ```
5. **Verify:**
   ```bash
   python scripts/cba_lookup.py "Article VII"
   # Should now show page ranges
   ```

### After Regeneration

```bash
$ python scripts/cba_lookup.py "Article VII"

Edition: 2023
ID: article_7
Type: article
Title: Article VII: TEAM SALARY CAP
Pages: 42-58
Character span: 125432-178965 (53,533 chars)
```

## Integration with CHAPTER-MAP

For chapters referencing CBA articles (e.g., salary cap, defined terms), the CHAPTER-MAP can link to lookup results with status `needs_local_pdf` until the PDF is locally available.

**Example CHAPTER-MAP row (Infra owns actual map):**

| Chapter | Section | Reference | Status |
|---------|---------|-----------|--------|
| Analytics | Salary Cap | CBA Art. VII §1 | `needs_local_pdf` |

*Note: Infra owns CHAPTER-MAP rows. This is a suggested integration pattern only.*

## Future Enhancements

Potential v2 features (not in this PR):

- **Terms index** — `data/derived/cba/{edition}/terms.json` with defined terms
- **Cross-reference tracking** — "as defined in Section X" lookups
- **Section hierarchy** — Navigate parent/child relationships
- **Exhibit lookup** — Query exhibits by letter/number
- **Edition diff** — Compare article structures across 2017 vs. 2023
- **Export formats** — JSON, CSV, markdown output for scripting

## See Also

- **Pipeline documentation:** [cba-structure-pipeline.md](cba-structure-pipeline.md)
- **Extraction script:** `scripts/cba/build_cba_structure.py`
- **Validation:** `scripts/cba/validate_cba_structure.py`
- **Schema:** `schemas/cba_structure.schema.json`

## Support

For issues with the lookup tool, open an issue on the `glen-w/hoops` repository.

For questions about CBA content or official text, refer to [NBPA](https://nbpa.com/cba).
