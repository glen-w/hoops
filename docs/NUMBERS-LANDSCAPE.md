# Basketball numbers: where they live

One page. Source by source is [DATA-REPOS.md](DATA-REPOS.md). The filterable list is [open_datasets.csv](open_datasets.csv).

The numbers split four ways. Historical box scores are open enough to cite: Basketball-Reference, 1946–. Modern league endpoints are usable and not republishable: NBA Stats, mostly from about 1996, and ESPN play-by-play from about 2002 via hoopR. Tracking is a vendor product, SportVU then Second Spectrum then Hawk-Eye. The tooling in front of all of that is good: `nba_api`, `hoopR`, `nbastatR`.

What this repo will not do is stated once in [DATA-REPOS.md](DATA-REPOS.md). No full mirrors. No Kaggle warehouse until credentials exist. No SportVU dumps. A package license is not a data license.

## Solved enough to write from

- Season aggregates and the advanced season stats. Basketball-Reference already feeds `avg_game_by_decade`.
- Play-by-play for a local notebook, from about 1996 (NBA Stats) or 2002 (ESPN / hoopR-data). Leave the mirror on disk.
- College team efficiency without KenPom: Barttorvik CSVs.
- A citation path for tracking: public aggregates, shot charts, and Sloan papers. Not the raw coordinates.

## Not in the repo yet

- A versioned salary snapshot. The contracts are on Basketball-Reference. Nothing is committed with a pull date.
- WNBA tables. `wehoop` can load them. We have not.
- A 30-team front-office series. [franchise_efficiency_2015_16.md](../data/derived/franchise_efficiency_2015_16.md) corrects one season's draft claims. It is not that table.

Gambling odds are not a gap to fill. The fans chapter can describe the machinery. No dataset ([ROADMAP](../ROADMAP.md) §6).

## Parked

Kaggle (`wyattowalsh/basketball`, `nathanlauga/nba-games`, and the other warehouses). KenPom, Cleaning the Glass, BigDataBall, and the NBAstuffer shop, unless someone is paying. Spotrac, except a page we cite.

## Read next

[DATA-REPOS.md](DATA-REPOS.md) for the source, the client, and the constraint. [open_datasets.csv](open_datasets.csv) to filter by priority. [ROADMAP.md](../ROADMAP.md) §5 for how this meets the analytics chapter.
