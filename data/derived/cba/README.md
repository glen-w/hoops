# NBA CBA Derived Structure

This directory contains **derived structural metadata** extracted from NBA Collective Bargaining Agreement PDFs.

## What's Committed

**Only structural metadata,** not fulltext:
- Article, section, and exhibit IDs
- Titles (truncated)
- Page ranges
- Character offsets (for local verification)
- Content hashes (SHA-256 of text slices, not the text itself)

**Source PDFs are not committed** and must be supplied locally (see `data/raw/cba/README.md`).

## Structure Format

Each edition's `structure.json` follows the schema in `schemas/cba_structure.schema.json`:

```json
{
  "edition": "2023",
  "source_sha256": "...",
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
      "text_sha256": "abc123..."
    },
    ...
  ]
}
```

### Unit Types

- `article` — Top-level CBA articles (e.g., "Article I: DEFINITIONS")
- `section` — Sections within articles (e.g., "Section 1. Definitions")
- `subsection` — Subsections (if present and parseable)
- `exhibit` — Exhibits and appendices (e.g., "Exhibit A: Uniform Player Contract")

### Hierarchy

- Articles have `parent_id: null`
- Sections reference their parent article via `parent_id`
- Exhibits are typically top-level (`parent_id: null`)

## Editions

### 2023 CBA (2023–2030)

Primary edition. Covers the current collective bargaining period.

- **Source:** NBPA official CBA page
- **Structure:** `2023/structure.json`

### 2017 CBA (2017–2024)

Historical reference for comparison and evolution analysis.

- **Source:** NBPA official CBA page (archived)
- **Structure:** `2017/structure.json`

## Validation

Validate structure files:

```bash
python scripts/cba/validate_cba_structure.py data/derived/cba/*/structure.json
```

## IP and Fair Use

This repository commits **structural metadata only.** The CBA text itself is proprietary (NBA and NBPA). Structural metadata—table of contents, section IDs, page ranges—falls under fair use for research and documentation.

**Host-of-record pattern:** The official CBA lives at NBPA. This repo is a research sidecar that points to the authoritative source and provides tooling for local structure extraction.
