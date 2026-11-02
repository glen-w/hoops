# Tick 289 final

Status: no new numbers.

hoops_list ran for Karamousalidis, Foteinakis and Wang. All three returned n=0 and no items. The long title queries did not match, so no exact paths were recovered. The earlier path error in hoops_summary is still unresolved.

## Next pass
- Use hoops_record with the keys: Karamousalidis 8VEP8FE8, Foteinakis E7QXTIF7, Wang NCQ6GJND.
- If that fails, use short hoops_list queries such as the first author surname alone, or the key alone.
- If a path comes back, run hoops_summary with that exact path.
- Use hoops_bib (local private/hoops_data/hoops_data.bib) as a fallback to confirm the keys exist.

## Open checks
- Foteinakis: resolve nine vs ten seasons from the full text.
- Wang 163-177: compares per-team vs combined metrics, and attempts vs makes. Check before use.
- Karamousalidis: pull Euroleague vs NCAA DI metrics only after a summary is returned.
- br_league_fetch.py: run where fetching is permitted. Log URL and access date. Build rows.csv only from fetched values.
- Keep Table A and Table B separate.

Sources: ds Basketball-Reference (WNKIH56T).