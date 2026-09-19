# Team Logos — Fair Use Policy

## Overview

This directory maintains **URL references only** to team logos, following fair-use principles. We do **not** download, host, or redistribute logo files.

## Schema: logos.csv

| Column | Type | Description |
|--------|------|-------------|
| `team_id` | string | Foreign key to teams.csv |
| `logo_type` | enum | One of: `primary`, `alternate`, `wordmark` |
| `source` | string | Source identifier (e.g., `wikimedia_commons`, `official_website`) |
| `url` | string | Direct URL to the logo resource |
| `format` | string | File format (e.g., `svg`, `png`) |
| `license` | string | License identifier (e.g., `PD`, `CC-BY-SA-4.0`, `fair-use`) |
| `as_of` | date | Date of URL verification (YYYY-MM-DD) |
| `notes` | string | Optional notes about the logo or usage restrictions |

## Priority: SVG from Wikimedia Commons

**Preferred source:** Wikimedia Commons SVG files, which are:
- Open-licensed (typically PD or CC-BY-SA)
- Vector format (scalable)
- Well-documented
- Stable URLs

**Search strategy:**
1. Check team's Wikidata item (P154: logo image property)
2. Search Wikimedia Commons for "{team name} logo"
3. Verify license compatibility
4. Record Commons file URL

## When Commons is Blocked

If a team logo is **not** available on Wikimedia Commons with an open license:

1. **Leave the row empty** in `logos.csv`
2. **Document the gap** in `LOGOS-GAPS.md`
3. **Do not** scrape official team websites
4. **Do not** upload copyrighted logos to this repository

### Fair-Use Reference Only

For copyrighted logos, we may include a `fair-use` reference URL pointing to:
- The team's official website logo page
- A reliable third-party database (e.g., sportslogos.net)

These are **reference URLs only** and do not grant redistribution rights.

## Current Status

As of **2026-09-19**, `logos.csv` is sparse:
- **EuroLeague (men)**: 0 / 20 logos populated
- **EuroLeague Women**: 0 / 22 logos populated

Logo population is deferred to a follow-up task. See `LOGOS-GAPS.md` for details.

## Future Work

To populate logos:
1. Run `scripts/teams/fetch_logos_from_commons.py` (to be created)
2. Manually verify licensing for any non-Commons sources
3. Update this README with coverage statistics

## License

This file documents logo **references** only. The logos themselves are copyrighted by their respective teams and leagues. Use of these references must comply with applicable trademark and copyright law.
