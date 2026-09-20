# CBA Defined-Terms Pocket Guide: Method

## Selection Criteria

From 83 Article I defined terms in each edition (2017, 2023), selected 20 standout terms for the pocket guide based on:

1. **Writer utility**: Terms that illuminate how the league's financial and roster machinery actually works
2. **Conceptual distinctiveness**: Each term represents a different mechanism or rule domain
3. **Cross-edition stability**: Preferred terms present in both CBAs (with locator evolution noted)
4. **Narrative potential**: Terms that support vivid, accurate vignettes without requiring legal-treatise prose

## Dual-Edition Coverage

All 20 terms appear in both the 2017 and 2023 CBAs. Locator strings changed between editions as Article I was reorganized (e.g., "Designated Veteran Player" moved from subsection (q) in 2017 to (p) in 2023), but the underlying concepts remained stable. Where substantive rule changes occurred (e.g., expansion of Two-Way Contract slots, tightening of Designated Veteran Player criteria), the vignette notes the evolution.

## IP Constraint

**No CBA full text reproduced.**  

Each vignette:
- Summarizes the term's function in plain English (2–4 sentences)
- Cites the formal locator from `defined_terms.json` (article/section keys, not page numbers)
- Cross-references related terms within the guide
- Does NOT paste definition language from the PDF

Where the JSON `definition_preview` field contained long verbatim excerpts, the guide distills the concept in the author's own words. Short labels like "Basketball Related Income" and "BRI" are term names, not protected prose; article references (e.g., `cba:2023:art-I:sec-1:(h)`) are factual locators, not copyrighted content.

## Motif Tags

Controlled vocabulary for clustering terms by domain:

- **cap**: Salary cap accounting and thresholds
- **trade**: Transaction mechanics (free agency, trades)
- **player**: Individual player rights, compensation, status
- **roster**: Active/inactive lists, G League shuttles
- **draft**: Rookie selection and scale contracts
- **governance**: League-wide rules (revenue sharing, floors, calendars)
- **revenue**: BRI and financial flows
- **injury**: (not used in this set; available for future expansion)
- **media**: (not used in this set; available for future expansion)

Tags are pipe-separated in `motif_tags.csv` to support multi-label filtering.

## Source Data

- **2023 CBA**: `data/cba/2023/derived/defined_terms.json` (83 terms, edition_id `2023`, source PDF SHA-256 `cf59d43fe46f63d7ba07364563046d766c487c26032fcc88432310d47effd9d9`)
- **2017 CBA**: `data/cba/2017/derived/defined_terms.json` (83 terms, edition_id `2017`, source PDF SHA-256 `66d620ebf682e2ffc55698394fb4635d738bf0e0250aad34f9cc137a25bf051a`)

Both JSON files extracted by the repo's CBA parser pipeline (see `docs/cba/SPIKE-REPORT.md`, `docs/CBA-LOOKUP.md`). The parser truncates full definition bodies in the JSON to prevent accidental verbatim republishing; the guide relies on those truncated previews + article pointers, never the full PDF text.

## Structure Metadata

Where useful for article/section context, consulted:
- `data/cba/2023/derived/structure.json` (42 articles, 279 sections)
- `data/cba/2017/derived/structure.json` (42 articles, 272 sections)
- `data/cba/2023/derived/headings_index.json` (nested heading map)
- `data/cba/2017/derived/headings_index.json` (nested heading map)

These files provide the article/section hierarchy used in locator strings; they contain no prose quotations, only structural keys.

## Guide Slug Format

Each term's `guide_slug` in `motif_tags.csv` matches the markdown anchor ID used in `pocket_guide.md`, enabling programmatic cross-referencing. Slugs are lowercase, hyphen-separated, and unique within the guide.

Example:
- Term: "Basketball Related Income"
- Slug: `basketball-related-income-bri`
- Markdown anchor: `#basketball-related-income-bri`

## Version

- **Guide version**: 1.0  
- **Created**: 2026-09-19  
- **Branch**: `cursor/cba-pocket-guide-0598`  
- **Author**: Glen W. (via Cursor Cloud Agent)

## Maintenance

To extend this guide:
1. Read `data/cba/{edition}/derived/defined_terms.json` for candidate terms
2. Draft vignettes in your own words; cite locators from the JSON
3. Add rows to `motif_tags.csv` with appropriate motif tags
4. Append guide slugs to `pocket_guide.md` with cross-references
5. Do NOT copy-paste definition language from the CBA PDF
6. Update this method doc if selection criteria or tag vocabulary evolves
