# Yahoo Finance data (Claude Code plugin)

Stock quotes, price history, options chains with Greeks, financial statements, analyst ratings, ownership, news, SEC filings and market movers from Yahoo Finance, through an Apify MCP server.

The plugin connects Claude Code to the live MCP endpoint of the Apify Actor [yahoo-finance-scraper](https://apify.com/akhil_rajesh/yahoo-finance-scraper) (`https://akhil-rajesh--yahoo-finance-scraper.apify.actor/mcp`) and adds a skill that tells Claude when to use it.

## Install

```bash
claude plugin marketplace add akhilrajesh213/apify-data-plugins
claude plugin install yahoo-finance-mcp@akhil-rajesh-data
```

Claude Code asks for your **Apify API token** when the plugin is enabled and keeps it in your system's credential store. Create a free account at [apify.com](https://apify.com) and copy the token from Apify Console > Settings > API & Integrations.

## Tools

- `get_quotes`: live quotes with fundamentals: price, change, market cap, P/E, dividend yield, sector, analysts' target
- `get_price_history`: historical prices for any period and interval, one row per ticker
- `get_options_chain`: US options with Greeks, filtered by type, strike range, volume or open interest
- `get_financial_statements`: income statement, balance sheet and cash flow, annual or quarterly
- `get_analyst_data`: rating changes with price targets, earnings against estimates, EPS and revenue estimates
- `get_ownership`: largest institutional and fund holders, insiders and their transactions
- `get_news`: latest headlines per ticker
- `get_sec_filings`: newest SEC filings of US listings and ADRs
- `get_market_movers`: day gainers, losers and most actives (US and 20 other markets), trending tickers, ETFs, crypto
- `search_symbols`: tickers matching a company name or word
- `run_actor`: the Actor's whole input in one call, for reads the other tools can't express

## Ask in plain words

- *"Compare NVDA, AMD and INTC on P/E, margins and analysts' targets."*
- *"Show me AAPL's quarterly revenue and net income for the last two years."*
- *"What are today's biggest gainers in India?"*
- *"Find SPY puts expiring next month with open interest above 10,000."*

## Cost

Calls run on your Apify account at the Actor's pay-per-event prices, shown on its [Apify page](https://apify.com/akhil_rajesh/yahoo-finance-scraper), plus platform usage while the endpoint's run serves you. Apify's free plan includes monthly credits.

> This is an independent tool, not affiliated with or endorsed by the owners of the data source. All product and company names are the property of their respective owners.
