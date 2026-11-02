# Nightshift log: 2026-10-21

Processed 13 requests from `requests.json`. Finished around 09:15 Paris time (CEST, UTC+2).

**Constraints honoured:**
- Nothing was sent or posted.
- Zotero was read only, with no writes and no access to "my pubs".
- Sandbox source files were not modified.
- The API key was never printed.

**Verification:** every related-work DOI in the briefs resolved via Crossref or OpenAlex. Unverifiable candidates were dropped.

| id | title | status | output file | note |
|---|---|---|---|---|
| 2026-10-21-researcher-01 | Sofyan: Bibliometric review | done | 2026-10-21_researcher-01_sofyan-bibliometric.md | 584 of 12,865 Scopus hits; the chapter-10 stub claims themes the paper doesn't report |
| 2026-10-21-researcher-02 | Brayton: Concussion crisis and labour politics | done, **needs Glen** | 2026-10-21_researcher-02_brayton-concussion-labor.md | Paper is NFL/NHL, not NBA; sandbox note title wrong; added Padaki 2016 NBA concussion bridge |
| 2026-10-21-researcher-03 | Sonkeng: Healing touch of pickup | done, **needs Glen** | 2026-10-21_researcher-03_sonkeng-pickup-selfcare.md | Zotero lacks DOI and vol/pages (12(4):465–480); the "two hours prescription" in the draft is unsupported |
| 2026-10-21-researcher-04 | Vázquez-Estévez: Clutch offence | done | 2026-10-21_researcher-04_vazquez-clutch-offense.md | EuroLeague, last minute and OT (sandbox title wrong); "first 17 s" wording caveat |
| 2026-10-21-researcher-05 | Lasco: Heightism and height premium | done | 2026-10-21_researcher-05_lasco-heightism.md | Conceptual review; basketball only in passing |
| 2026-10-21-researcher-06 | Sansone: Mental fatigue and injury | done | 2026-10-21_researcher-06_sansone-mental-fatigue.md | Null result, n=14 and 11 injuries; not a concussion paper |
| 2026-10-21-researcher-07 | Galvanovskis: Sound and free throws | done | 2026-10-21_researcher-07_galvanovskis-sound-ft.md | Weak evidence; treats NBA 2019-20 as a no-crowd season, which it wasn't |
| 2026-10-21-researcher-08 | Hore: ML sustainability model | done | 2026-10-21_researcher-08_hore-ml-sustainability.md | Box-score only (no biomechanics); kappa 0.35; McNemar misread in the AI note |
| 2026-10-21-coder-01 | 2021-22 attendance official total | done | 2026-10-21_coder-01_attendance-2021-22.md | 20,910,813 (SBJ, NBA paid), MEDIUM-HIGH; no NBA press release found |
| 2026-10-21-coder-02 | Verify 2020-21 (671k) | done | 2026-10-21_coder-02_attendance-2020-21.md | 671k rejected; no official total; ~1.49M lower bound, LOW-MEDIUM |
| 2026-10-21-coder-03 | Reconcile analysis/ CSVs | done, **needs Glen** | 2026-10-21_coder-03_csv-reconcile.md (+ 3 CSV drafts) | Old CSVs are empty stubs; merge into corrected drafts; league_income_ingredients.csv is a placeholder sentence |
| 2026-10-21-coder-04 | Sonkeng chapter data needs | done | 2026-10-21_coder-04_sonkeng-data-needs.md | No pro-league stats needed; one intro sentence at most |
| 2026-10-21-coder-05 | Review Task 2/3 scaffolding | done, **needs Glen** | 2026-10-21_coder-05_scaffolding-review.md | Task 3 (local per-team media) is out of scope; replace with national deals and a labour timeline |

**CSV drafts written to out/:**
- 2026-10-21_coder-03_attendance_2017_24_merged.csv
- 2026-10-21_coder-03_league_attendance_long_draft.csv
- 2026-10-21_coder-03_national_tv_revenue_2016_36_merged.csv

## Needs Glen
1. **Brayton chapter framing.** The paper covers the NFL and NHL. Decide whether the chapter argues by analogy for basketball (recommended, with Padaki 2016) or broadens to professional sport.
2. **Zotero fixes** (I can't make them on a read-only job):
   - Sonkeng 24ECN7VH: add DOI 10.1080/2159676X.2019.1634128 and 12(4):465–480.
   - Volume/issue missing for Vázquez 277L4R4G (15(4) 1928) and Sansone 27HTLIPC (14(4) 148).
   - Galvanovskis and Hore are typed journalArticle with consensus.app URLs.
3. **Sandbox note titles are wrong** for Brayton ("in the NBA") and Vázquez-Estévez ("last two minutes").
4. **`league_income_ingredients.csv`** is a one-line placeholder claiming completed work. Rebuild it or delete it.
5. **CSV choices:**
   - adopt the merged drafts;
   - wide or long schema;
   - whether to allow LOW confidence;
   - whether to archive the empty stubs.
6. **Task 3 scope:**
   - drop per-team local media in favour of national deals plus a labour timeline;
   - the Sportico subscription question becomes moot if it's dropped.
7. **Chapter overclaims to reword:**
   - ch08 "measurably affect" (Galvanovskis);
   - ch09 "biomechanical, workload" (Hore);
   - ch11 MF→injury (Sansone);
   - the Sonkeng "two hours" prescription;
   - Brayton outline: 2019-20 "zero attendance", the 671k figure, and the unsourced profitability→concussion-visibility claim.
