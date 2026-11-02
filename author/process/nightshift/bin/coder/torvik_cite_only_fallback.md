# Torvik Cite-Only Fallback (coder, 2026-10-19)

Trigger: any item in analysis/torvik_tos_checkplan.md FAILs.

## Rules
- Do not run analysis/fetch_torvik_csv.py. No raw CSV stored or committed.
- Torvik numbers appear only when read from the rendered public table in a browser, quoted narrowly, with URL + access date.
- No recomputation or aggregation from bulk downloads.
- Any aggregate stat must come from another open source with its own citation (see hoops/data sources/ catalog; hoopR torvik_* wrappers and Basketball-Reference paths already catalogued).
- Record the fallback activation and reason in analysis/torvik_gate_update.md so the gate history stays complete.

## Grounding
- hoops/_ repo citeables/open datasets _ catalog/Bart Torvik - n.d. - Barttorvik T-Rank — NCAA team ratings CSVs -- NVTWTCHG
- hoops/data sources/Unknown - n.d. - Barttorvik (T-Rank) college basketball -- 7FHGENDV