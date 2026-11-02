# League Income Ingredients: Blank Cell Classification

**Source CSV**: data/derived/league_income_ingredients.csv
**Confidence**: Varies; blanks must be classified
**Blank classifications**:
- 'source silent': PR exists but did not state figure
- 'pending scrape': extractable from known source but not yet pulled
- 'estimate excluded': derivable but outside scope
- 'source unavailable': no known public source

**Next step**: Review CSV; classify each blank; document in notes column.