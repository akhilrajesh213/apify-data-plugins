# Live web data plugins for Claude Code

Claude Code plugins that give Claude live data from the web through [Apify](https://apify.com) MCP servers. Each plugin connects to one Apify Actor's live endpoint and adds a skill that tells Claude when to use it.

| Plugin | What it gives Claude |
|---|---|
| [`yahoo-finance-mcp`](plugins/yahoo-finance-mcp) | Stock quotes, price history, options chains with Greeks, financial statements, analyst ratings, ownership, news, SEC filings and market movers from Yahoo Finance, through an Apify MCP server. |
| [`youtube-channels-mcp`](plugins/youtube-channels-mcp) | YouTube channel stats (subscribers, exact total views, video count), recent videos and Shorts with views, channel comparisons, channels by topic, playlists and hashtags, through an Apify MCP server. No YouTube API key needed. |
| [`google-trends-mcp`](plugins/google-trends-mcp) | Google Trends' Trending Now in 125 countries, keyword interest over time with rising and top related searches, keyword comparisons, and Pinterest Trends lists, through an Apify MCP server. |

## Install

```bash
claude plugin marketplace add akhilrajesh213/apify-data-plugins
```

Then install the plugins you want:

```bash
claude plugin install yahoo-finance-mcp@akhil-rajesh-data
claude plugin install youtube-channels-mcp@akhil-rajesh-data
claude plugin install google-trends-mcp@akhil-rajesh-data
```

Or, inside a session, run `/plugin` and browse the **akhil-rajesh-data** marketplace.

Each plugin asks for your **Apify API token** when it's enabled and keeps it in your system's credential store, never in a settings file. Create a free account at [apify.com](https://apify.com) and copy the token from Apify Console > Settings > API & Integrations.

## Cost

Calls run on your own Apify account, at each Actor's pay-per-event prices (shown on its Apify page) plus platform usage while its live endpoint serves you. Apify's free plan includes monthly credits. Rows the tools couldn't find aren't charged.

## Other MCP clients

The same endpoints work in Claude Desktop, Cursor and any client that speaks Streamable HTTP: point it at the URL in the plugin's `.mcp.json` with the header `Authorization: Bearer <YOUR_APIFY_TOKEN>`.

## Disclaimer

These are independent tools, not affiliated with or endorsed by Yahoo, Google, YouTube or Pinterest. All product and company names are the property of their respective owners.

## License

MIT
