---
name: yahoo-finance-data
description: "Use the yahoo-finance MCP tools when the user asks about stocks, ETFs, indices, crypto or currencies: prices, history, fundamentals, options, earnings, analysts, holders, filings, news or the day's movers."
---

# Yahoo Finance data

The `yahoo-finance` MCP server is the live endpoint of the Apify Actor [yahoo-finance-scraper](https://apify.com/akhil_rajesh/yahoo-finance-scraper). Use its tools for live data instead of answering from memory, and name the tool's source in the answer.

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

## Cost and limits

- Every row a tool returns is charged to the user's Apify account (pay-per-event, plus platform usage while the endpoint's run serves them). Ask for what the question needs, not more.
- A request that has started runs to its end even if the caller stops waiting.
- Answers name what wasn't found, what didn't load and what a limit left out (fields such as `notFound` and `notRead`). Report those to the user instead of filling the gap yourself.
- The first call can take about 5 to 10 seconds while the endpoint starts; later calls are faster.

## Tips

- Indian stocks can be typed as NSE symbols (`RELIANCE`) or with Yahoo's suffix (`RELIANCE.NS`); other markets need Yahoo's suffix (`SHEL.L`, `7203.T`).
- Ask `search_symbols` first when the user gives a company name rather than a ticker.
- Ask for the period and interval the question needs: a year of daily bars, not all history.
