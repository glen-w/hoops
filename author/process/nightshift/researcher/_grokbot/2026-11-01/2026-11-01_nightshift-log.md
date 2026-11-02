# Nightshift log for 2026-11-01 (night 2026-10-31)

Grok Bot ran this on the box on 1 Nov 2026 (CET, Paris time). There were 8 requests: 3 researcher and 5 coder. requests.json was not edited (sha256 d3f9…dde3, verified). Every figure carries its source URL and the retrieval date, 2026-11-01.

| id | title | status | outputs |
|---|---|---|---|
| 2026-10-31-researcher-01 | Sports Journalism 1950–2000 | done: 13 DOI items plus 9 books (gaps: desk-size data, post-1950 Black press) | 2026-11-01_researcher-01_sports-journalism-1950-2000.md |
| 2026-10-31-researcher-02 | Regional/Local Broadcasting 1960–2000 | done: 11 DOI items plus 7 books/cases (gap: a series of local rights fees) | 2026-11-01_researcher-02_regional-local-broadcasting-1960-2000.md |
| 2026-10-31-researcher-03 | Nielsen Audience Measurement 1960–2000 | done: 9 DOI items plus 5 others (gaps: out-of-home measurement, make-goods, Madow/Harris hearings) | 2026-11-01_researcher-03_nielsen-audience-measurement-1960-2000.md |
| 2026-10-31-coder-01 | Little Caesars Arena EMMA official statement | done, 16 rows (MSF 2014A CUSIPs need EMMA) | 2026-11-01_coder-01_little-caesars-arena-bond-terms.md/.csv/.parquet |
| 2026-10-31-coder-02 | Amway Center EMMA/bond rating documents | done, 15 rows (2008 OS needs EMMA) | 2026-11-01_coder-02_amway-center-bond-terms.md/.csv/.parquet |
| 2026-10-31-coder-03 | ENR CCI annual values 2000–2026 | done, 91 rows in long format (BLS deflators; ENR 2026 monthly values are paywalled) | 2026-11-01_coder-03_enr-cci-and-public-deflators-2000-2026.md/.csv/.parquet |
| 2026-10-31-coder-04 | Post-2010 NBA arena lease reserve terms | done, 13 rows (Fiserv $60M is LOW [summary-only]) | 2026-11-01_coder-04_nba-arena-lease-reserve-terms.md/.csv/.parquet |
| 2026-10-31-coder-05 | Dedicated hotel/car-rental tax pledges | done, 10 rows | 2026-11-01_coder-05_arena-tourist-tax-pledges-post2010.md/.csv/.parquet |

## Key findings
- **R1–R3.** All 33 DOIs were verified against Crossref. The core sources:
  - **Sports journalism:** the Garrison & Salwen surveys of sports journalists (1989, 1994, 1998), Real (1975), Messner et al. (1993), Eastman & Billings (2000, 2001), Mallett on the Atlanta Daily World.
  - **Local and regional broadcasting:** Bellamy (1988), Cave & Crandall (2001), Zimbalist (2000) on the NBA lockout, and the Bulls/WGN cases (7th Cir. 1992 and 1996).
  - **Nielsen:** Meehan and Hurwitz (1984), Milavsky (1992, CONTAM peoplemeter review), Buzzard (2002, "Peoplemeter Wars"), Napoli (2005), and the NBA studies that use Nielsen ratings (Kanazawa & Funk, Hausman & Leonard).
- **C4.**
  - LCA reserve: $500k/yr, rising 4%/yr, split 50/50 (HIGH).
  - Golden 1: $1/ticket Capital Repair Fee goes into the Capital Repairs Reserve Fund. The 2015 lease-revenue bonds of $272.87M carry a $18.38M DSR (HIGH, Sacramento Treasurer 2016-00071).
  - Spectrum: City is obliged to make capital repairs, financed with a $110M COP BAN (2023).
  - State Farm: $3/ticket facility charge.
  - Phoenix: $2M City plus $1M Suns per year (MEDIUM).
  - Fiserv: ArenaCo bears all repairs; the ~$60M reserve is LOW [summary-only].
- **C5.**
  - Hotel/car-rental tax is pledged at:
    - Amway: 6th-cent TDT.
    - Fiserv: WCD 2016A pledges room, car-rental and F&B taxes.
    - Frost/AT&T: Bexar CVT 2015 bonds, $78.675M, 1.75% HOT first lien plus 5% MVRT.
    - State Farm: $110M on the **car-rental** tax. This corrects the 2026-10-28 row, which said hotel-motel.
  - Not pledged: Spectrum, Golden 1, LCA, Chase and Intuit.
  - Footprint is MEDIUM, and Project Marvel is planned.
- **C3.** ENR CCI annual averages for 2000–2025, plus BLS PPI/ECI deflators from BLS API v2. ENR monthly values for 2026 are a GAP (subscription).

## Zotero
Added via the Web API (user 11334554). Items were deduped by DOI search (qmode=everything), then by title. Every new item is tagged `nightshift-2026-11-01`. No existing items or notes were edited, nothing was deleted, and "my pubs" was not touched.

**Created (24)**
- **Other sports (RNWE7I8B) + media (LFXJI77E):** A9PRA34Z, UM8QGNUI, M4KK7CA8, WBMDGKSX (Garrison/Salwen surveys); 5ZAQSA3E (Real 1975); 8W2FJTQ6 (Gantz 1981); 3XF5GBD7 (Rada 1996); RKAHU2IC (Eastman & Billings 2000); PRICTT64 (Rowe 2007).
- **History D4A783AU:** JN643MM3 (Mallett 2023), also in RNWE7I8B and media.
- **Broadcast DDL25BEF + media:** RVTFSR5A (Messner et al. 1993).
- **Other sports + econ J3XVUX2F:**
  - W5U3SAPQ (Bellamy 1988), also in media;
  - JCDKZVRK (Atkinson et al. 1988);
  - PHN8586V (Kesenne 2000);
  - CRAF88AM (Cave & Crandall 2001).
- **Broadcast + econ:** 4EFPPKJF (Zimbalist 2000 chapter).
- **Broadcast + history + econ:** N4UIVA2C (Surdam 2012).
- **Media + Nielsen I5MN75D8:**
  - ITG8J7HP (Meehan 1984);
  - E7KKQZK9 (Hurwitz 1984);
  - NVXB9T9K (Milavsky 1992);
  - JDJGC69N (Buzzard 2002);
  - 2M4VZIWA (Napoli 2005);
  - M5UTS7C4 (Webster et al., Ratings Analysis).
- **Media + econ + Nielsen:** UW9NNN7B (Aldrich et al. 2005).

**Reused (cited only, not edited):** PFC85IHT (Andrews 1996), K5Q658GC (Eastman & Billings 2001), C53N9WXC (Vrooman 1995), CR7DT9JL (El-Hodiri & Quirk 1971), 7KDKCK67 (Mongeon & Winfree 2012), AW9D2F6S (Foster et al. 2014), 5JN7VUDR (Kunz 2017), QF6H4KE9 (Kanazawa & Funk 2001), 5ZFB9FVM (Hausman & Leonard 1997).

## Needs Glen
- C1: MSF 2014A CUSIPs and the final OS from EMMA (manual).
- C2: the Amway 2008 OS from EMMA.
- C3: ENR CCI monthly values for 2026 and Dec 2025 (subscription).
- C4/C5: the AFCRA State Farm bond OS, the final WCD 2016 OS, Phoenix bond/lease documents, a primary source for the Fiserv ~$60M reserve (Wisconsin LFB paper unreachable, 504), and the final executed Golden 1 lease.
- R1–R3: books are listed but not added to Zotero, so verify and add them if wanted. Also find sources for the Madow (1961) and Harris hearings and for Beville.
