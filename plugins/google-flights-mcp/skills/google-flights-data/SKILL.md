---
name: google-flights-data
description: Use the google-flights MCP tools when the user asks about flight prices, cheap flights, fares on a route or date, nonstop or business class options, or whether today's fare is low or high for a route.
---

# Google Flights fares

The `google-flights` MCP server is the live endpoint of the Apify Actor [google-flights-mcp-server](https://apify.com/akhil_rajesh/google-flights-mcp-server). Use its tools for live data instead of answering from memory, and name the tool's source in the answer.

## Tools

- `search_flights`: fares for a route on up to 3 departure dates, one way or round trip, with cabin, stops, airline, price, duration and departure-time filters
- `find_airport`: the airports and cities Google Flights offers for a name, with their codes (free)
- `run_actor`: the Actor's whole input in one call, for several routes or Google Flights links

## Cost and limits

- Every row a tool returns is charged to the user's Apify account (pay-per-event, plus platform usage while the endpoint's run serves them). Ask for what the question needs, not more.
- A request that has started runs to its end even if the caller stops waiting.
- Answers name what wasn't found, what didn't load and what a limit left out (fields such as `notFound` and `notRead`). Report those to the user instead of filling the gap yourself.
- The first call can take about 5 to 10 seconds while the endpoint starts; later calls are faster.

## Tips

- Places can be cities ('Toronto'), airport codes ('YYZ') or several codes with '/' ('JFK/EWR'); ask `find_airport` when a name is ambiguous.
- Fares are for all passengers together, in the currency asked for (USD by default); set `country` and `currency` for the user's market.
- `max_flights` is 10 by default; 0 returns only each date's cheapest fare and price level, the cheapest way to ask.
- If a filter is refused (the answer says why), tell the user rather than guessing fares.
