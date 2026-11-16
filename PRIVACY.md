# Privacy policy

Applies to every plugin in this repository (https://github.com/akhilrajesh213/apify-data-plugins). Last updated 2026-11-16.

## What the plugins are

Each plugin is a configuration file that adds one remote MCP server to Claude Code, plus a skill: written instructions telling Claude when to use that server. The plugins contain no code that runs on your machine, collect no analytics and have no servers of their own.

## What is sent, and to whom

When Claude calls one of a plugin's tools, Claude Code sends two things over HTTPS to that plugin's endpoint on the [Apify](https://apify.com) platform:

1. the tool's arguments, which Claude writes from your request (tickers, channel handles, keywords, routes and dates, store addresses), and
2. your Apify API token, in an `Authorization` header, so that the call runs on your Apify account.

Nothing else is sent: not your conversation, files, environment variables or other credentials.

| Plugin | Endpoint | Public data it reads |
|---|---|---|
| `yahoo-finance-mcp` | `akhil-rajesh--yahoo-finance-scraper.apify.actor` | Yahoo Finance |
| `youtube-channels-mcp` | `akhil-rajesh--youtube-channel-scraper.apify.actor` | YouTube |
| `google-trends-mcp` | `akhil-rajesh--google-trends-scraper.apify.actor` | Google Trends and Pinterest Trends |
| `google-flights-mcp` | `akhil-rajesh--google-flights-mcp-server.apify.actor` | Google Flights |
| `shopify-mcp` | `akhil-rajesh--shopify-mcp-server.apify.actor` | the Shopify stores named |

Each endpoint is an Apify Actor published by the author of these plugins. It reads only public pages or public data feeds of the source named above (no logged-in or private data) and returns the rows to Claude.

## Where the data is kept

Every call is an Apify run on **your** Apify account. Its input, log and result rows are stored in your account's storage under [Apify's privacy policy](https://apify.com/privacy-policy) and Apify's retention periods, and you can view or delete them in Apify Console. Apify charges your account for the rows at each Actor's published prices.

The plugins' author is the Actors' owner on Apify. Apify does not show Actor owners other users' runs, inputs, results or tokens; the author sees only aggregate figures Apify reports to every Actor owner (such as run counts, users and earnings).

## Your token

Claude Code asks for your Apify API token when you enable a plugin and keeps it in your operating system's credential store (marked `sensitive` in the plugin), never in a settings file. It is sent only to the plugin's endpoint. You can revoke it at any time in Apify Console > Settings > API & Integrations.

## Children

The plugins are not intended for people under 18.

## Changes and contact

Changes to this policy are committed to this repository, and its history shows every version. Questions: open an issue at https://github.com/akhilrajesh213/apify-data-plugins/issues.
