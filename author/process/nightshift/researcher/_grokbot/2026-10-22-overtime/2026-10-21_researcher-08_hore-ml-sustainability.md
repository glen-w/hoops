# Hore & Bhattacharya 2018: An ML "sustainability model" for NBA players

**Request:** 2026-10-21-researcher-08 (low)
**Status:** done
**Sources used:** Zotero `2BJ6DNWS` (metadata, note, full text), OpenAlex W2894199709 and Crossref.

## Citation
Hore, S., & Bhattacharya, T. (2018). A machine learning based approach towards building a sustainability model for NBA players. In *2018 Second International Conference on Inventive Communication and Computational Technologies (ICICCT)* (pp. 1690–1694). IEEE. https://doi.org/10.1109/ICICCT.2018.8473102

**Zotero metadata gaps:** The item is typed journalArticle (it is a conference paper), and the URL is a consensus.app link.

## Core argument
Player performance statistics can predict whether an NBA player will "sustain" a career of **more than 5 years**, which could help teams make investment decisions.

## Methods
- **Data:** about 1,300 player records from a public data.world dataset of per-player box-score statistics (GP, PTS, FG% and so on), with a binary target of career length over 5 years. The paper doesn't say whether these are rookie-season stats.
- **Feature selection:** Boruta kept 11 of 20 features.
- **Models compared:** Naïve Bayes, SVM, multilayer perceptron and random forest, using an 80/20 split and 10-fold cross-validation in R (caret).

## Key findings
- SVM did best: mean accuracy **0.703** (maximum 0.868), mean kappa 0.349, ROC 0.842, sensitivity 0.744 and specificity 0.829.
- The other models were in a similar range.

## Critical read
- A kappa of about 0.35 means **modest** predictive value, little better than base-rate guessing.
- The reported "max accuracy 0.868" is a best fold and should not be quoted as the model's accuracy.
- The Zotero AI note reads McNemar's p = 0.6831 as evidence for SVM. In caret's confusionMatrix, McNemar tests the **symmetry of errors**, not model superiority. Don't repeat that reading.
- "Sustainability" here means career length, not environmental or health sustainability.
- A short conference paper with about 6 citations (OpenAlex).

## Fit with the chapter (`chapters/09_ml_sustainability.md`)
- The stub claims models "trained on biomechanical, workload, and performance data". **The paper uses box-score statistics only.** It has no biomechanics or workload data, so reword the stub.
- Better used as an example of early, simple career-length prediction, set against the economics literature on career length and draft effects.

## Related works (DOIs verified via Crossref)
1. Staw, B. M., & Hoang, H. (1995). Sunk costs in the NBA: Why draft order affects playing time and survival in professional basketball. *Administrative Science Quarterly*, 40(3), 474–494. https://doi.org/10.2307/2393794
2. Groothuis, P. A., & Hill, J. R. (2004). Exit discrimination in the NBA: A duration analysis of career length. *Economic Inquiry*, 42(2), 341–349. https://doi.org/10.1093/ei/cbh065
3. Teramoto, M., & Cross, C. L. (2010). Relative importance of performance factors in winning NBA games in regular season versus playoffs. *Journal of Quantitative Analysis in Sports*, 6(3). https://doi.org/10.2202/1559-0410.1260
4. Kursa, M. B., & Rudnicki, W. R. (2010). Feature selection with the Boruta package. *Journal of Statistical Software*, 36(11). https://doi.org/10.18637/jss.v036.i11. The method source.
