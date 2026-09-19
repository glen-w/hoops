# FIBA BAT statistics — source note

**As of:** 2026-09-19  
**Draft-linked URL (requested):** [https://www.fiba.basketball/bat-statistics-2022.pdf](https://www.fiba.basketball/bat-statistics-2022.pdf) — **HTTP 404** on 2026-09-19 (retired path).  
**Current official PDF used:** [https://assets.fiba.basketball/image/upload/documents-corporate-bat-bat-statistics.pdf](https://assets.fiba.basketball/image/upload/documents-corporate-bat-bat-statistics.pdf)  
**Index page:** [https://about.fiba.basketball/en/services/basketball-arbitral-tribunal/bat-process](https://about.fiba.basketball/en/services/basketball-arbitral-tribunal/bat-process) (“BAT Statistics - 2007-2025”)  
**Label:** OFFICIAL (FIBA / BAT).  
**Confidence:** **HIGH** for numbers transcribed from the PDF text layer.

## What happened to the 2022 PDF?

The ROADMAP cite `https://www.fiba.basketball/bat-statistics-2022.pdf` is dead. Secondary literature (e.g. Elite Law) still points at that URL and quotes **1,904 requests 2007–2022**, which matches the sum of annual rows through 2022 in the current PDF. FIBA now hosts a rolling **2007–2025** statistics sheet at the assets URL above (PDF metadata CreationDate **2026-02-05 CET**, title “Statistics programmiert 2025”).

## Files

| File | Rows | Contents |
|------|------|----------|
| `fiba_bat_arbitration_by_year.csv` | 21 | Annual 2007–2025 + PDF total + derived 2007–2022 cumulative |
| `fiba_bat_2022_key_metrics.csv` | 8 | Chapter-ready 2022 metrics + cumulative requests |
| `fiba_bat_pdf_footnotes.csv` | 3 | PDF footnotes *, **, *** |
| `bat-statistics.pdf` | — | Downloaded official PDF snapshot |
| `bat-statistics.txt` | — | `pdftotext -layout` extract for audit |

## Gaps

- PDF page 1 is **BAT Arbitration Proceedings** only. A header for **Payment Order Proceedings (POP)** appears but **no POP numeric table** was present in the extracted page (1 page PDF). Marked GAP — do not invent POP counts.
- 2025 row has `cases_pending=74`; treat as incomplete year at PDF cut-off.
- Wayback fetch of the retired 2022 URL failed (TLS/429) this pass; reliance is on current official PDF + cross-check of 1904 cumulative.

## Citation

Basketball Arbitral Tribunal / FIBA. *BAT Statistics 2007–2025.* https://assets.fiba.basketball/image/upload/documents-corporate-bat-bat-statistics.pdf (accessed 2026-09-19). Supersedes retired https://www.fiba.basketball/bat-statistics-2022.pdf.
