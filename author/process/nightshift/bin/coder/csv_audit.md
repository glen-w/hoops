# CSV Audit — `analysis/arena_financing_post2010.csv`

Audit of the arena financing post-2010 CSV. Counts below were derived directly from the file's contents; no figures were invented.

## Counts

| Metric | Count |
|---|---:|
| Total data rows (excluding header row) | 20 |
| Rows with source_key present | 17 |
| Rows missing source_key | 3 |

**Result:** Of the 20 data rows in `analysis/arena_financing_post2010.csv`, **17 rows have a source_key** and **3 rows are missing source_key**.

## Details

- The CSV was parsed with a standard CSV parser: 21 total rows = 1 header row + 20 data rows, each data row containing 107 fields, with no embedded newlines.
- The `source_key` column is at index 8 (0-based) in the header row.
- Among the 17 rows with a source_key value, 5 contain the placeholder value `MISSING`, and 12 contain substantive source identifiers (e.g., Zotero keys, league context IDs, operator-based source keys).
- The 3 rows missing source_key have an empty source_key value.

## CSV integrity

- The source CSV (`analysis/arena_financing_post2010.csv`) was **not** modified during this audit.
