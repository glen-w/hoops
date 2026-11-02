# ENR CCI annual 2000–2026 plus public alternative deflators (coder-03)
Retrieved 2026-11-01. Data: `2026-11-01_coder-03_enr-cci-and-public-deflators-2000-2026.csv` / `.parquet` (91 rows; long format: series, year, value, unit, source_url, document, page, retrieved, confidence, notes).

## ENR Construction Cost Index (20-city, 1913=100), public reproductions
| Years | Source | Confidence |
|---|---|---|
| 2000–2020 annual averages | Hermiston, OR agenda attachment, "Construction Cost Index History – As of December 2021" (https://hermiston.novusagenda.com/agendapublic/AttachmentViewer.ashx?AttachmentID=4339&ItemID=3204). Cross-checked against the Rosenet copy, which differs by ≤1 point in a few years and has 2012 on an 11-month basis | MEDIUM |
| 2021 | 12,133.33: my own mean of 12 monthly values (the annual cell is blank in the source) | MEDIUM |
| 2022–2023 | 13,006.84 / 13,358.05, from a Town of Truckee agenda chart | MEDIUM |
| 2024 | 13,571.30 (another Truckee copy shows 13,565.74; not reconciled) | LOW |
| 2025 | 13,881.30, **Jan–Nov only** | LOW |
| 2026 | **GAP**: no public reproduction | GAP |

ENR's own free page only shows pre-1990 history. The full current table needs a subscription.

## Public alternative deflators (BLS PPI, API v2 annual averages, HIGH)
- **WPUSI012011** Construction Materials (1982=100): 2000–2025. For example, 2000 = 144.1, 2010 = 194.5, 2020 = 239.2, 2025 = 337.910.
- **PCU236222236222** New School Building Construction (Dec 2005=100): 2006–2025. It is the closest public PPI to a building-output price for large public facilities.
- **WPUIP2312301** Net inputs to other nonresidential construction, goods (Jun 2010=100): 2011–2025.
- **2026:** the rows are the mean of Jan–Sep monthly values, labelled YTD and MEDIUM (preliminary months).
- **Note:** FRED fredgraph.csv downloads failed, so the values were pulled directly from BLS. The series titles were checked against the FRED/BLS pages.

## Needs Glen
- ENR 2026 monthly values (and the Dec 2025 value) need ENR subscription access.
