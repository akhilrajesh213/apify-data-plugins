---
name: google-trends-data
description: Use the google-trends MCP tools when the user asks what people are searching for, whether interest in a topic is rising, how keywords compare, where a topic is popular, related or rising searches, or what is trending on Pinterest.
---

# Google Trends and Pinterest Trends

The `google-trends` MCP server is the live endpoint of the Apify Actor [google-trends-scraper](https://apify.com/akhil_rajesh/google-trends-scraper). Use its tools for live data instead of answering from memory, and name the tool's source in the answer.

## Tools

- `get_trending_now`: what a country or region is searching for now, with search volume, increase, start time and news if asked
- `get_keyword_trends`: interest over time per keyword with its average, peak, growth and direction, interest by region, top and rising related searches
- `compare_keywords`: up to 5 keywords on one scale, as Google Trends' comparison shows them
- `get_pinterest_trends`: a region's Pinterest Trends lists: fastest-growing searches, shopping trends, editors' picks, seasonal moments
- `run_actor`: the Actor's whole input in one call

## Cost and limits

- Every row a tool returns is charged to the user's Apify account (pay-per-event, plus platform usage while the endpoint's run serves them). Ask for what the question needs, not more.
- A request that has started runs to its end even if the caller stops waiting.
- Answers name what wasn't found, what didn't load and what a limit left out (fields such as `notFound` and `notRead`). Report those to the user instead of filling the gap yourself.
- The first call can take about 5 to 10 seconds while the endpoint starts; later calls are faster.

## Tips

- Google Trends values are relative (0-100 within the request), not search counts; say so when comparing.
- Keyword rows cost more than trend rows: ask only for the keywords and countries the question needs.
