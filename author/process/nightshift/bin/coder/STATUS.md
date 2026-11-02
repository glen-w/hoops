# Analysis status (coder, tick 2026-10-19)

## Blocked
- `hoops_list` for `avg_game_by_decade` returned 0 items.
- `hoops_list` for `salary collective bargaining franchise` returned 0 items.
- No rows file exists, so no statistics can be computed. No numbers are given here.

## Present, not yet run
- `analysis/ds_sources.csv`: 9 sources, taken from Zotero abstracts only.
- `analysis/check_rows.py`: validates a rows CSV. Usage: `python3 -I analysis/check_rows.py rows.csv season [col ...]`.
- `analysis/decade_table.py`: from an earlier tick, not re-checked this tick.

## Next steps once rows exist
1. Run `check_rows.py` on the rows file.
2. Run `decade_table.py` on the same file.
3. Paste the output into `chapter_target.md`, citing the hr path.

## Open risk
- Check the Basketball-Reference ToS wording before redistributing any scraped content.
- The researcher should try other list keys, such as `Basketball-Reference`, `season rows` and `salaries`. The Basketball-Reference ds note names it as the source for the avg_game_by_decade rows.
