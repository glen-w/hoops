# Free-Throw Pressure Integration — GAME TIME Chapter

**Status:** READY TO CITE  
**Deadline:** None (ready now; do not wait for other batches)  
**Zotero Keys:** 48 items tagged `nightshift-2026-10-22`  

## Key Finding

Free-throw pressure effect confirmed in NBA data (n=519,640 attempts, 2015-16 to 2023-24):
- **Late-close context:** −2.5 percentage points (pp) effect on FT% (p < .01)
- **Trailing context:** −5.3 pp effect on FT% (p < .01)
- **Workload × pressure interaction:** Null across 6 models (p > .05)

## Integration Point

**Chapter location:** GAME TIME § Pressure context (or Skills § Execution under pressure)  
**Suggested framing:**

> Free throws offer a clean test of pressure's effect on fine motor control. [CITE nightshift-2026-10-22 analysis] In late-close and trailing game states, NBA players showed measurable FT% decline (−2.5 pp and −5.3 pp respectively, n≈520k attempts). The effect persists independent of workload (fatigue), suggesting pressure acts on execution mechanics rather than fatigue recovery.

## Limitations

- **Cascade hypothesis untested:** Analysis tests outcome (% made), not kinematics/release variation or reinvestment behavior. Hypothesis that pressure degrades automaticity/release consistency remains untested in this dataset.
- **Confounds:** Late-close/trailing contexts correlate with opponent quality and game importance. Effect size is real but small.
- **Generalization:** FT% is uniquely clean pressure test (undefended, repeatable). Broader impact on field-goal shooting, decision-making, or team execution not addressed here.

## Files

- **Summary:** `analysis/game_time/ft_pressure_cascade.md` (one-liner)
- **Code + data:** `sandbox/coder/analysis/_grokbot/2026-10-22-pm/` (build_ft.py, enrich.py, analyze.py, robustness_and_proxies.py; supporting CSVs: ft_models.csv, ft_pressure_workload_summary.csv)
- **Raw data:** `ft_attempts_2015-2024.csv.gz` (12.2 MB, n=519,640)

## Next Steps

1. Researcher: integrate key finding + Zotero keys to GAME TIME chapter immediately
2. Researcher: review limitations section; adjust framing if needed
3. Coder: monitor for related integration into kinematic/skill sections (future batch)
