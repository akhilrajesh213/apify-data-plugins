# Google Trends and Pinterest Trends (Claude Code plugin)

Google Trends' Trending Now in 125 countries, keyword interest over time with rising and top related searches, keyword comparisons, and Pinterest Trends lists, through an Apify MCP server.

The plugin connects Claude Code to the live MCP endpoint of the Apify Actor [google-trends-scraper](https://apify.com/akhil_rajesh/google-trends-scraper) (`https://akhil-rajesh--google-trends-scraper.apify.actor/mcp`) and adds a skill that tells Claude when to use it.

## Install

```bash
claude plugin marketplace add akhilrajesh213/apify-data-plugins
claude plugin install google-trends-mcp@akhil-rajesh-data
```

Claude Code asks for your **Apify API token** when the plugin is enabled and keeps it in your system's credential store. Create a free account at [apify.com](https://apify.com) and copy the token from Apify Console > Settings > API & Integrations.

## Tools

- `get_trending_now`: what a country or region is searching for now, with search volume, increase, start time and news if asked
- `get_keyword_trends`: interest over time per keyword with its average, peak, growth and direction, interest by region, top and rising related searches
- `compare_keywords`: up to 5 keywords on one scale, as Google Trends' comparison shows them
- `get_pinterest_trends`: a region's Pinterest Trends lists: fastest-growing searches, shopping trends, editors' picks, seasonal moments
- `run_actor`: the Actor's whole input in one call

## Ask in plain words

- *"What's trending in the US right now?"*
- *"Is interest in 'protein coffee' rising or falling over the last 12 months?"*
- *"Compare 'chatgpt', 'claude' and 'gemini' over the past 90 days."*
- *"What are the fastest-growing Pinterest searches in Canada?"*

## Cost

Calls run on your Apify account at the Actor's pay-per-event prices, shown on its [Apify page](https://apify.com/akhil_rajesh/google-trends-scraper), plus platform usage while the endpoint's run serves you. Apify's free plan includes monthly credits.

> This is an independent tool, not affiliated with or endorsed by the owners of the data source. All product and company names are the property of their respective owners.
