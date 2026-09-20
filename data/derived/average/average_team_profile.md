# Average NBA team — composite vignette (Phase 1)

**Access:** 2026-09-20 (Europe/Paris / PT)  
**Status:** COMPOSITE OF DISTRIBUTIONS — **not** a fake franchise.  
**Honesty locks:** no mean hex; distributions reported beside every composite.

## One-paragraph composite (with distributions)

The Phase-1 “average” NBA club is best read as a **modal / median sketch**, not a personified team. Across all **30** current franchises in `teams.csv` (desk as_of 2026-09-19):

- **Home market size band (mode):** `mid_large_2.5_5M` — **9/30** teams (30.0%). Full band mix: {'mid_large_2.5_5M': 9, 'megacity_10M+': 4, 'large_5_10M': 9, 'mid_1_2.5M': 7, 'under_1M': 1}.
- **Arena capacity (median):** **19,019** seats (mean 18,814.3; range 16,867–20,917; n=30 public capacities in teams desk).
- **Ownership structure (mode):** **`majority`** — **20/30** (66.7%). Distribution: {'majority': 20, 'public': 1, 'group': 4, 'sole': 5}.
- **Primary colour hex:** **GAP** — **0/30** `colours_primary_hex` cells filled in teams.csv. Per honesty lock we do **not** invent a mean hex; modal-among-filled applies only after P0d.
- **Conference mix:** {'Eastern': 15, 'Western': 15} (balanced Eastern/Western under current NBA alignment).
- **Division mix:** {'Atlantic': 5, 'Central': 5, 'Southeast': 5, 'Northwest': 5, 'Pacific': 5, 'Southwest': 5}.
- **Founded year (median):** 1967 (mean 1967.2; span 1923–2002).
- **Country:** {'US': 29, 'CA': 1} (29 US + 1 CA).

US metro populations: Census CBSA 2023 estimates (median US MSA among 29 US-home teams: **4,342,304**). Toronto uses StatCan 2021 GTA **6,712,341** via Wikipedia — different vintage; flagged in inputs CSV.

## What this is / is not

| Is | Is not |
|----|--------|
| Summary of empirical distributions from the teams desk + Census/StatCan | A 31st franchise with a made-up name, colour, or owner |
| Cite-backed seats / ownership mode / metro bands | Averaged hex colour or string-mean city name |

## Inputs

See `average_team_inputs.csv` (30 rows) and `average_team_profile.json`.

## Next passes (not claimed done)

- **P0d colours:** fill official primary hex → then report **modal** primary among filled (still never a channel-wise mean hex).
- Optional: CSA vs MSA sensitivity; city proper vs metro; arena *basketball* config vs max concert capacity footnotes.
