# Tick 286 final

State: hr second pass returned only one result, `hoops_list` with n=0 and no items. No `hoops_bib` output came back, though four requests went out (three bib, one list). No 'path' error this time. Nothing was read or verified, so no numbers or claims were added.

## What this means
- The list query "shooting trends three-point decade" matched nothing. That is not evidence the papers are missing from Zotero. The query may simply be too narrow.
- The three `hoops_bib` results are missing. It is unknown whether they returned empty or were dropped. Do not assume either.

## Next tick
1. Retry `hoops_bib` once per paper with a short author-only query: `Foteinakis`, `Wang`, `Karamousalidis`.
2. Retry `hoops_list` with a broader query, e.g. `shooting`, or with no query.
3. If `hoops_bib` still returns nothing, stop retrying hr. Report to Glen that hr returns empty or no output for papers cited in `pc`.
4. Do not block on hr for the data step. `br_league_fetch.py` needs only Basketball-Reference (ds WNKIH56T).

## Open items (unchanged, need a readable source)
- Foteinakis: nine or ten seasons? Per-game or per-season metric?
- Wang pp.163-177: one team or both? What basis?
- Karamousalidis: read the excerpt after CHAID before citing trees.
- Keep Table A (mean_of_means) and Table B (games_weighted) separate.
- `br_league_fetch.py`: run it, log URL and access date, build rows.csv from fetched values only.
