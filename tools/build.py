"""Writes the marketplace: .claude-plugin/marketplace.json and one plugin folder per Actor.

    python tools/build.py

Each plugin connects Claude Code to one Actor's Apify Standby MCP endpoint, authenticated with the
user's own Apify API token (a sensitive userConfig option, kept in the OS credential store).
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OWNER = {"name": "Akhil Rajesh", "url": "https://apify.com/akhil_rajesh"}
REPO = "https://github.com/akhilrajesh213/apify-data-plugins"
TOKEN_OPTION = {
    "apify_token": {
        "type": "string",
        "title": "Apify API token",
        "description": "Your Apify API token (Apify Console > Settings > API & Integrations). "
                       "Runs are billed to your Apify account at the Actor's pay-per-event prices plus platform usage.",
        "required": True,
        "sensitive": True,
    }
}

PLUGINS = [
    {
        "name": "yahoo-finance-mcp",
        "displayName": "Yahoo Finance data",
        "server": "yahoo-finance",
        "actor": "yahoo-finance-scraper",
        "store": "https://apify.com/akhil_rajesh/yahoo-finance-scraper",
        "category": "finance",
        "keywords": ["yahoo finance", "stocks", "stock market", "options", "financial statements", "market data", "mcp"],
        "description": "Stock quotes, price history, options chains with Greeks, financial statements, analyst ratings, "
                       "ownership, news, SEC filings and market movers from Yahoo Finance, through an Apify MCP server.",
        "tools": [
            ("get_quotes", "live quotes with fundamentals: price, change, market cap, P/E, dividend yield, sector, analysts' target"),
            ("get_price_history", "historical prices for any period and interval, one row per ticker"),
            ("get_options_chain", "US options with Greeks, filtered by type, strike range, volume or open interest"),
            ("get_financial_statements", "income statement, balance sheet and cash flow, annual or quarterly"),
            ("get_analyst_data", "rating changes with price targets, earnings against estimates, EPS and revenue estimates"),
            ("get_ownership", "largest institutional and fund holders, insiders and their transactions"),
            ("get_news", "latest headlines per ticker"),
            ("get_sec_filings", "newest SEC filings of US listings and ADRs"),
            ("get_market_movers", "day gainers, losers and most actives (US and 20 other markets), trending tickers, ETFs, crypto"),
            ("search_symbols", "tickers matching a company name or word"),
            ("run_actor", "the Actor's whole input in one call, for reads the other tools can't express"),
        ],
        "when": "the user asks about stocks, ETFs, indices, crypto or currencies: prices, history, fundamentals, "
                "options, earnings, analysts, holders, filings, news or the day's movers",
        "examples": [
            "Compare NVDA, AMD and INTC on P/E, margins and analysts' targets.",
            "Show me AAPL's quarterly revenue and net income for the last two years.",
            "What are today's biggest gainers in India?",
            "Find SPY puts expiring next month with open interest above 10,000.",
        ],
        "tips": [
            "Indian stocks can be typed as NSE symbols (`RELIANCE`) or with Yahoo's suffix (`RELIANCE.NS`); other markets need Yahoo's suffix (`SHEL.L`, `7203.T`).",
            "Ask `search_symbols` first when the user gives a company name rather than a ticker.",
            "Ask for the period and interval the question needs: a year of daily bars, not all history.",
        ],
    },
    {
        "name": "youtube-channels-mcp",
        "displayName": "YouTube channel data",
        "server": "youtube-channels",
        "actor": "youtube-channel-scraper",
        "store": "https://apify.com/akhil_rajesh/youtube-channel-scraper",
        "category": "marketing",
        "keywords": ["youtube", "youtube channel", "competitor analysis", "creators", "influencers", "video stats", "mcp"],
        "description": "YouTube channel stats (subscribers, exact total views, video count), recent videos and Shorts with views, "
                       "channel comparisons, channels by topic, playlists and hashtags, through an Apify MCP server. No YouTube API key needed.",
        "tools": [
            ("get_channel_info", "subscribers, exact total views and video count, joined date, country, description, links"),
            ("get_channel_videos", "a channel's videos, Shorts, streams and popular videos, with filters"),
            ("compare_channels", "one row per channel, biggest first, with median views, upload pace and days since the last upload"),
            ("find_channels", "channels for a topic, from its hashtag page, with their stats"),
            ("get_playlist_videos", "a public playlist and its first 100 videos"),
            ("get_hashtag_videos", "a hashtag's counts and the videos on its page, with exact views"),
            ("run_actor", "the Actor's whole input in one call"),
        ],
        "when": "the user asks about YouTube channels, creators or competitors: subscribers, views, upload pace, "
                "recent or popular videos, Shorts, playlists, hashtags, or finding channels on a topic",
        "examples": [
            "Compare MrBeast, Mark Rober and Veritasium on median views and upload pace.",
            "What were @mkbhd's 10 most popular videos this year?",
            "Find small cooking channels that post Shorts.",
        ],
        "tips": [
            "Channels can be given as `@handle`, a channel link or a channel id.",
            "Video transcripts and comments aren't available; say so rather than guessing.",
            "Each tool call reads up to 5 channels and 200 rows; split bigger asks into several calls.",
        ],
    },
    {
        "name": "google-trends-mcp",
        "displayName": "Google Trends and Pinterest Trends",
        "server": "google-trends",
        "actor": "google-trends-scraper",
        "store": "https://apify.com/akhil_rajesh/google-trends-scraper",
        "category": "marketing",
        "keywords": ["google trends", "trending searches", "keyword research", "seo", "pinterest trends", "mcp"],
        "description": "Google Trends' Trending Now in 125 countries, keyword interest over time with rising and top related searches, "
                       "keyword comparisons, and Pinterest Trends lists, through an Apify MCP server.",
        "tools": [
            ("get_trending_now", "what a country or region is searching for now, with search volume, increase, start time and news if asked"),
            ("get_keyword_trends", "interest over time per keyword with its average, peak, growth and direction, interest by region, top and rising related searches"),
            ("compare_keywords", "up to 5 keywords on one scale, as Google Trends' comparison shows them"),
            ("get_pinterest_trends", "a region's Pinterest Trends lists: fastest-growing searches, shopping trends, editors' picks, seasonal moments"),
            ("run_actor", "the Actor's whole input in one call"),
        ],
        "when": "the user asks what people are searching for, whether interest in a topic is rising, how keywords compare, "
                "where a topic is popular, related or rising searches, or what is trending on Pinterest",
        "examples": [
            "What's trending in the US right now?",
            "Is interest in 'protein coffee' rising or falling over the last 12 months?",
            "Compare 'chatgpt', 'claude' and 'gemini' over the past 90 days.",
            "What are the fastest-growing Pinterest searches in Canada?",
        ],
        "tips": [
            "Google Trends values are relative (0-100 within the request), not search counts; say so when comparing.",
            "Keyword rows cost more than trend rows: ask only for the keywords and countries the question needs.",
        ],
    },
    {
        "name": "google-flights-mcp",
        "displayName": "Google Flights fares",
        "server": "google-flights",
        "actor": "google-flights-mcp-server",
        "store": "https://apify.com/akhil_rajesh/google-flights-mcp-server",
        "category": "travel",
        "keywords": ["google flights", "flights", "airfare", "flight prices", "cheap flights", "travel", "mcp"],
        "description": "Live Google Flights fares for any route and date: the cheapest and cheapest nonstop fare, Google's "
                       "price level and price history, and each flight's price, airlines, times, stops, layovers, aircraft "
                       "and CO2, through an Apify MCP server.",
        "tools": [
            ("search_flights", "fares for a route on up to 3 departure dates, one way or round trip, with cabin, stops, "
                               "airline, price, duration and departure-time filters"),
            ("find_airport", "the airports and cities Google Flights offers for a name, with their codes (free)"),
            ("run_actor", "the Actor's whole input in one call, for several routes or Google Flights links"),
        ],
        "when": "the user asks about flight prices, cheap flights, fares on a route or date, nonstop or business class "
                "options, or whether today's fare is low or high for a route",
        "examples": [
            "What's the cheapest flight from Toronto to London on December 10?",
            "Find nonstop business class flights New York to Paris next month.",
            "Round trip LAX to Tokyo for a week, leaving in 45 days: is the price low right now?",
            "Compare fares from Chicago to Cancun on three Saturdays in March.",
        ],
        "tips": [
            "Places can be cities ('Toronto'), airport codes ('YYZ') or several codes with '/' ('JFK/EWR'); ask "
            "`find_airport` when a name is ambiguous.",
            "Fares are for all passengers together, in the currency asked for (USD by default); set `country` and "
            "`currency` for the user's market.",
            "`max_flights` is 10 by default; 0 returns only each date's cheapest fare and price level, the cheapest way to ask.",
            "If a filter is refused (the answer says why), tell the user rather than guessing fares.",
        ],
    },
    {
        "name": "shopify-mcp",
        "displayName": "Shopify store products",
        "server": "shopify",
        "actor": "shopify-mcp-server",
        "store": "https://apify.com/akhil_rajesh/shopify-mcp-server",
        "category": "ecommerce",
        "keywords": ["shopify", "ecommerce", "product data", "competitor prices", "product research", "mcp"],
        "description": "Products of any Shopify store: prices and compare-at prices, discounts, variants with SKUs and stock, "
                       "vendors, tags, images and collections, best sellers first and priced for any country, through an "
                       "Apify MCP server.",
        "tools": [
            ("get_products", "a store's or collection's products in the store's order, with keyword, vendor, type, tag, "
                             "price, stock, sale and date filters"),
            ("get_product", "single products by link, with every variant, image, the full description and SEO texts"),
            ("list_collections", "a store's collections (categories) with their links"),
            ("run_actor", "the Actor's whole input in one call"),
        ],
        "when": "the user asks about a Shopify store's products, prices, discounts, best sellers, new arrivals, stock, "
                "collections or a competitor's catalogue",
        "examples": [
            "What are allbirds.com's best sellers and their prices?",
            "Which products on gymshark.com are on sale right now, and by how much?",
            "Show me this store's products published in the last 30 days.",
            "Compare this product's price in the US and the UK.",
        ],
        "tips": [
            "Stores can be a domain ('allbirds.com'), a collection link or product links; up to 5 per call and 100 rows in all.",
            "Some stores with a custom front end don't answer; the answer names them as not read.",
            "Use `product_details` only when the question needs full descriptions or every image: it makes rows much larger.",
        ],
    },
]


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def url(p):
    return f"https://akhil-rajesh--{p['actor']}.apify.actor/mcp"


def plugin_files(p):
    base = ROOT / "plugins" / p["name"]
    manifest = {
        "name": p["name"],
        "displayName": p["displayName"],
        "version": "0.1.0",
        "description": p["description"],
        "author": OWNER,
        "homepage": p["store"],
        "repository": REPO,
        "license": "MIT",
        "keywords": p["keywords"],
        "userConfig": TOKEN_OPTION,
    }
    write(base / ".claude-plugin" / "plugin.json", json.dumps(manifest, indent=2) + "\n")
    mcp = {"mcpServers": {p["server"]: {
        "type": "http",
        "url": url(p),
        "headers": {"Authorization": "Bearer ${user_config.apify_token}"},
    }}}
    write(base / ".mcp.json", json.dumps(mcp, indent=2) + "\n")
    tools = "\n".join(f"- `{name}`: {what}" for name, what in p["tools"])
    tips = "\n".join(f"- {t}" for t in p["tips"])
    skill = f"""---
name: {p['server']}-data
description: Use the {p['server']} MCP tools when {p['when']}.
---

# {p['displayName']}

The `{p['server']}` MCP server is the live endpoint of the Apify Actor [{p['actor']}]({p['store']}). Use its tools for live data instead of answering from memory, and name the tool's source in the answer.

## Tools

{tools}

## Cost and limits

- Every row a tool returns is charged to the user's Apify account (pay-per-event, plus platform usage while the endpoint's run serves them). Ask for what the question needs, not more.
- A request that has started runs to its end even if the caller stops waiting.
- Answers name what wasn't found, what didn't load and what a limit left out (fields such as `notFound` and `notRead`). Report those to the user instead of filling the gap yourself.
- The first call can take about 5 to 10 seconds while the endpoint starts; later calls are faster.

## Tips

{tips}
"""
    write(base / "skills" / f"{p['server']}-data" / "SKILL.md", skill)
    examples = "\n".join(f"- *\"{e}\"*" for e in p["examples"])
    readme = f"""# {p['displayName']} (Claude Code plugin)

{p['description']}

The plugin connects Claude Code to the live MCP endpoint of the Apify Actor [{p['actor']}]({p['store']}) (`{url(p)}`) and adds a skill that tells Claude when to use it.

## Install

```bash
claude plugin marketplace add akhilrajesh213/apify-data-plugins
claude plugin install {p['name']}@akhil-rajesh-data
```

Claude Code asks for your **Apify API token** when the plugin is enabled and keeps it in your system's credential store. Create a free account at [apify.com](https://apify.com) and copy the token from Apify Console > Settings > API & Integrations.

## Tools

{tools}

## Ask in plain words

{examples}

## Cost

Calls run on your Apify account at the Actor's pay-per-event prices, shown on its [Apify page]({p['store']}), plus platform usage while the endpoint's run serves you. Apify's free plan includes monthly credits.

> This is an independent tool, not affiliated with or endorsed by the owners of the data source. All product and company names are the property of their respective owners.
"""
    write(base / "README.md", readme)


def main():
    for p in PLUGINS:
        plugin_files(p)
    market = {
        "name": "akhil-rajesh-data",
        "description": "Live web data for Claude Code: Yahoo Finance, YouTube channels, Google Trends, Google Flights and Shopify stores, through Apify MCP servers.",
        "owner": OWNER,
        "plugins": [
            {
                "name": p["name"],
                "source": f"./plugins/{p['name']}",
                "description": p["description"],
                "category": p["category"],
                "tags": p["keywords"],
            }
            for p in PLUGINS
        ],
    }
    write(ROOT / ".claude-plugin" / "marketplace.json", json.dumps(market, indent=2) + "\n")
    rows = "\n".join(f"| [`{p['name']}`](plugins/{p['name']}) | {p['description']} |" for p in PLUGINS)
    installs = "\n".join(f"claude plugin install {p['name']}@akhil-rajesh-data" for p in PLUGINS)
    write(ROOT / "README.md", f"""# Live web data plugins for Claude Code

Claude Code plugins that give Claude live data from the web through [Apify](https://apify.com) MCP servers. Each plugin connects to one Apify Actor's live endpoint and adds a skill that tells Claude when to use it.

| Plugin | What it gives Claude |
|---|---|
{rows}

## Install

```bash
claude plugin marketplace add akhilrajesh213/apify-data-plugins
```

Then install the plugins you want:

```bash
{installs}
```

Or, inside a session, run `/plugin` and browse the **akhil-rajesh-data** marketplace.

Each plugin asks for your **Apify API token** when it's enabled and keeps it in your system's credential store, never in a settings file. Create a free account at [apify.com](https://apify.com) and copy the token from Apify Console > Settings > API & Integrations.

## Cost

Calls run on your own Apify account, at each Actor's pay-per-event prices (shown on its Apify page) plus platform usage while its live endpoint serves you. Apify's free plan includes monthly credits. Rows the tools couldn't find aren't charged.

## Other MCP clients

The same endpoints work in Claude Desktop, Cursor and any client that speaks Streamable HTTP: point it at the URL in the plugin's `.mcp.json` with the header `Authorization: Bearer <YOUR_APIFY_TOKEN>`.

## Disclaimer

These are independent tools, not affiliated with or endorsed by Yahoo, Google, YouTube, Pinterest or Shopify. All product and company names are the property of their respective owners.

## License

MIT
""")
    write(ROOT / "LICENSE", """MIT License

Copyright (c) 2026 Akhil Rajesh

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
""")
    print("wrote", ROOT)


if __name__ == "__main__":
    main()
