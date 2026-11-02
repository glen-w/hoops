# Econ and teams reading list for Hoops analysis

Built from hr hoops_list results only (queries: salary, CBA, franchise). Only titles and paths appear here. Nothing was read in full, so no findings are claimed. Researcher should pull each summary with hoops_summary before citing.

## Query: salary (4 hits)
- Johnson 2020, Wage discrimination in the NBA: Evidence using free agent signings (key 5Y74UZCK)
- Zhang 2024, National Basketball Association Salary Prediction: A Data-Driven Linear Regression Analysis (key 6K6XPJZ9)
- Turnbull 2024, Estimating the cost of sports injuries: A scoping review (key HGZCXBI8)
- Pradhan 2025, Violating the salary cap: exploring performance gains in the National Basketball Association (key LFCW6FBV)

## Query: CBA (3 hits)
The hits do not look CBA-specific from their titles. Researcher should check before use.
- Xiao 2025, A deep learning-based study of player styles and cross-league performance adaptation (key 9HIP8MY3)
- Chen 2023, Research on the Team Operation and Management Strategy of the Mainstream Basketball (key I8JDGUVJ), in _inbox
- Leon-Quismondo 2024, Relative Age Effect on basketball. The case of Chinese professional basketball players (key ZIFVBNSA)

## Query: franchise (1 hit)
- Kim 2024, Evaluating the operational efficiency of NBA teams on franchise value (key KPJUUC2W)

## Possible analysis hooks (to be confirmed after summaries)
- Salary: Zhang 2024 and Johnson 2020 may name the salary variables they use. Match those to the B-Ref salaries page or nbastatR (HoopsHype/RealGM) before planning any salary code.
- Cap: Pradhan 2025 may define a cap-violation measure we could reproduce. Unconfirmed.
- Franchise value: Kim 2024 may name its inputs. Unconfirmed. No team-value dataset is in the ds records yet.

## Still missing
- No dataset record for CBA text, income, or team tables. Retry hoops_list with income and team. If still absent, ask Glen.
- B-Ref season CSV still not supplied. No decade averages can be produced.
