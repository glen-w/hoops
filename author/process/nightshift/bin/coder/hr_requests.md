# HR requests

## Done
- Prior tick: hoops_list for CBA, income, teams, Foteinakis, Wang returned nothing.
- This tick: hoops_list with an empty query returned n=40 but only 11 items (keys 243D2GH9 to 2BNAQFDH). See hr_inventory.md. No CBA, income or teams items among them.

## Next pass
1. Find out how to page past the first 11. Try hoops_list with q set to a key prefix (e.g. 2C, 2D, ...) or ask the harness for an offset/limit field.
2. Broad queries: salary, collective bargaining, franchise, decade, league.
3. hoops_summary on 2BNAQFDH (Sofyan) for decade-trend context, and on 25NDF7BW and 2BJ6DNWS if a metric is needed.
4. If the 29 unseen items also lack CBA, income and teams, ask Glen where they sit in Zotero. They may be in an uncatalogued folder or not yet imported.

## Blocked
- Season CSV from Glen (B-Ref). Check it against decade_csv_spec.md, then run decade_avg.py.
- Researcher must pick mean_of_means or games_weighted. The script prints both.
