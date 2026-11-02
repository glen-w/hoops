# Review of `task_2_3_attendance_tv_revenue_scaffolding.md`

**Request:** 2026-10-21-coder-05 (high)
**Status:** done. Several decisions need Glen.

## Summary
- **Task 2 (league attendance) is well-aimed but mostly done now.** Tonight's work (coder-01/02/03) fills 2017-18 to 2023-24, and the drafts follow the scaffolding's long schema.
- **Task 3 as written (per-team *local* media revenue, 2016-17 to 2023-24) is out of scope** for both chapters. I recommend dropping it or shrinking it sharply.

## Misalignments found
1. **Task 3 contradicts itself.** The heading says "Per-Team **National** TV Revenue". The body and the closing note say it covers **local** media only (Sportico's local TV and radio), because "National media is already in `league_income_ingredients.csv`".
2. **That premise is false.** `league_income_ingredients.csv` is a one-sentence placeholder with no national-media data, or any data at all (coder-03).
3. **The Brayton chapter needs national deals, not local revenue.** `brayton_chapter_outline.md` argues from the **$24B → $76B national deals** and league-level attendance. Neither the outline nor the chapter stub makes any per-team claim, so per-team local media revenue serves no argument there.
4. **The Sonkeng chapter needs neither task** (coder-04).
5. **The Brayton paper itself covers the NFL and NHL, not the NBA** (researcher-02). The NBA economic timeline is the chapter's *own* extension of Brayton's frame. It should be presented as such, and backed by basketball-specific labour and injury sources (e.g. Padaki et al. 2016 on NBA concussion), not by more revenue tables.
6. **The outline's causal claim is unsourced.** "The concussion issue surfaces most visibly during periods of high league profitability" is a hypothesis. No data in Task 2/3 can test it without a concussion-coverage timeline, which nobody has scoped.
7. **The schema doesn't match the actual files.** The scaffolding defines a long format. The new CSVs are wide and use other column names. The confidence scale has no LOW, though 2020-21 needs one. Allow LOW, or keep GAP for "no official figure" and put the lower-bound value in the notes.
8. **Smaller factual issues in the doc:**
   - It describes 2019-20 as a "COVID-shortened season (72 games)". Teams played roughly 63–67 games before the suspension, plus seeding games in the bubble; verify before citing.
   - The "~$1.67B" ticket-revenue record for 2018-19 is unsourced.
   - The doc's period starts at 2018-19, but the outline's labour timeline would benefit from 2016-17 (the start of the $24B deal) and 2023-24. 2023-24 has now been added.
9. **Sportico access:** the doc asks whether a subscription is needed. That only matters if Task 3 survives. Ask Glen only then.

## Recommended rescoped plan
| Item | Keep / change | Effort |
|---|---|---|
| Task 2 attendance, league totals 2016-17 to 2023-24 | **Keep.** It's essentially done (coder-03 drafts). Add 2015-16 and 2016-17 from NBA PR 2019 (21,972,129 and 21,997,412) if the timeline starts there | ~0.5 h |
| Per-team attendance | **Drop** unless a chapter makes team-level claims | n/a |
| Task 3 local media per team | **Drop**, or park until a chapter needs it | saves ~1–2 days plus a subscription |
| National TV deals | **Replace Task 3 with this.** Two rows are already drafted (coder-03). Verify the per-partner split if the chapter cites it | ~0.5 h |
| Labour timeline (CBA 2011 lockout, 2017 CBA, 2020 bubble/BRI escrow, 2023 CBA) | **Add.** This is what the Brayton argument actually needs, with dates from NBA/NBPA releases | ~1 h |
| `league_income_ingredients.csv` | Rebuild it as the long-format file, or delete it. **Glen decides** | n/a |

## Answers to the doc's open questions (my recommendation)
- **Per-team or league total?** League total only.
- **Show 2019-20 and 2020-21 separately?** Yes. Mark 2019-20 as partial-with-crowds (not zero) and 2020-21 as a restricted, incomplete lower bound.
- **Sportico access?** Not needed if Task 3 is dropped.
