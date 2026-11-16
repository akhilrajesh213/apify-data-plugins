# Google Flights fares (Claude Code plugin)

Live Google Flights fares for any route and date: the cheapest and cheapest nonstop fare, Google's price level and price history, and each flight's price, airlines, times, stops, layovers, aircraft and CO2, through an Apify MCP server.

The plugin connects Claude Code to the live MCP endpoint of the Apify Actor [google-flights-mcp-server](https://apify.com/akhil_rajesh/google-flights-mcp-server) (`https://akhil-rajesh--google-flights-mcp-server.apify.actor/mcp`) and adds a skill that tells Claude when to use it.

## Install

```bash
claude plugin marketplace add akhilrajesh213/apify-data-plugins
claude plugin install google-flights-mcp@akhil-rajesh-data
```

Claude Code asks for your **Apify API token** when the plugin is enabled and keeps it in your system's credential store. Create a free account at [apify.com](https://apify.com) and copy the token from Apify Console > Settings > API & Integrations.

## Tools

- `search_flights`: fares for a route on up to 3 departure dates, one way or round trip, with cabin, stops, airline, price, duration and departure-time filters
- `find_airport`: the airports and cities Google Flights offers for a name, with their codes (free)
- `run_actor`: the Actor's whole input in one call, for several routes or Google Flights links

## Ask in plain words

- *"What's the cheapest flight from Toronto to London on December 10?"*
- *"Find nonstop business class flights New York to Paris next month."*
- *"Round trip LAX to Tokyo for a week, leaving in 45 days: is the price low right now?"*
- *"Compare fares from Chicago to Cancun on three Saturdays in March."*

## Cost

Calls run on your Apify account at the Actor's pay-per-event prices, shown on its [Apify page](https://apify.com/akhil_rajesh/google-flights-mcp-server), plus platform usage while the endpoint's run serves you. Apify's free plan includes monthly credits.

## Data and privacy

This plugin runs no code on your machine. It adds one remote MCP server and one skill (instructions for Claude).

- **What is sent, and where:** when Claude calls one of the tools, Claude Code sends the tool's arguments (for example an origin, a destination, dates, passenger counts and filters) and your Apify API token, as an `Authorization` header, over HTTPS to `akhil-rajesh--google-flights-mcp-server.apify.actor`, the Actor's endpoint on the Apify platform. Nothing else from your conversation, files or machine is sent.
- **What the endpoint does with it:** the Actor reads the public pages or public data feeds of Google Flights that answer the request, returns the rows to Claude, and stores them in your own Apify account (a run's dataset), where Apify charges for them. It reads no logged-in or private data.
- **Who keeps what:** the run, its input and its rows stay in your Apify account under Apify's [privacy policy](https://apify.com/privacy-policy) and data retention, and you can delete them there. The plugin's author receives no copy of your requests, results or token, only the aggregate run counts and earnings Apify shows every Actor owner.
- **Your token** is kept by Claude Code in your system's credential store, never in a settings file, and is sent only to the endpoint above.

Full policy: [PRIVACY.md](https://github.com/akhilrajesh213/apify-data-plugins/blob/main/PRIVACY.md).

> This is an independent tool, not affiliated with or endorsed by the owners of the data source. All product and company names are the property of their respective owners.
