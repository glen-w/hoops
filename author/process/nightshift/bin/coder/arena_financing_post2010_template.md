# Arena Financing Data — Template (2010–2026)

CSV structure awaiting Grokbot parquet retrieval and SEC 10-K extraction.

Columns:
- year: fiscal year
- arena_name: facility name
- operator: owner/operator entity
- capex_millions: capital expenditure (blank if unknown)
- debt_millions: long-term debt (blank if unknown)
- source_key: cite-key (e.g., sec-10k-{company}-{year} or grokbot-{id})
- confidence: HIGH|MEDIUM|LOW (or blank if not-found)
- notes: source/methodology

Status: 30 NBA arenas, years 2010–2026 scaffolded. Awaiting capex/debt population from Grokbot and SEC filings.

Blocking issues:
1. Grokbot parquet unlock (2000–2026 coverage needed)
2. SEC 10-K capex/debt extraction by operator/REIT (no automated pipeline yet)
3. Municipal bond data (MSRB EMMA or operator prospectus) for public-financed arenas