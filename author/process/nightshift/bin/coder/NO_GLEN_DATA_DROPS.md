# Policy: no Glen data drops

Glen does **not** hand over bulk CSVs. The library is already on file.

## What to do instead

1. **`paperful_ask` first for open questions** — hoops-scoped RAG (`query` = question). Use returned source keys with `hoops_summary` / `zotero_get`.
2. **paperful-out mirror** — `hoops_list` / `hoops_summary` / nested notes (full path or bare key). Decade rows already live under:
   - `hoops/_ repo citeables/decade averages _ height/… average NBA game by decade -- JIVPJ22E`
   - Nested note embeds CSV text; record URL points at `raw.githubusercontent.com/glen-w/hoops/.../avg_game_by_decade.csv`
3. **Live Zotero (read-only)** — `zotero_search` / `zotero_get` when you only have a key.
4. **Local bib** — `hoops_bib` on `private/hoops_data/hoops_data.bib` when present.
5. **If still missing** — file `analysis/nightshift_requests.json` (`kind: paper|data|info`). Do not burn tokens web-searching for library material.
6. **Never** invent numbers. **Never** open a thread asking Glen to supply a CSV.
