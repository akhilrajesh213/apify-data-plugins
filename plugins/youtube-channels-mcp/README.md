# YouTube channel data (Claude Code plugin)

YouTube channel stats (subscribers, exact total views, video count), recent videos and Shorts with views, channel comparisons, channels by topic, playlists and hashtags, through an Apify MCP server. No YouTube API key needed.

The plugin connects Claude Code to the live MCP endpoint of the Apify Actor [youtube-channel-scraper](https://apify.com/akhil_rajesh/youtube-channel-scraper) (`https://akhil-rajesh--youtube-channel-scraper.apify.actor/mcp`) and adds a skill that tells Claude when to use it.

## Install

```bash
claude plugin marketplace add akhilrajesh213/apify-data-plugins
claude plugin install youtube-channels-mcp@akhil-rajesh-data
```

Claude Code asks for your **Apify API token** when the plugin is enabled and keeps it in your system's credential store. Create a free account at [apify.com](https://apify.com) and copy the token from Apify Console > Settings > API & Integrations.

## Tools

- `get_channel_info`: subscribers, exact total views and video count, joined date, country, description, links
- `get_channel_videos`: a channel's videos, Shorts, streams and popular videos, with filters
- `compare_channels`: one row per channel, biggest first, with median views, upload pace and days since the last upload
- `find_channels`: channels for a topic, from its hashtag page, with their stats
- `get_playlist_videos`: a public playlist and its first 100 videos
- `get_hashtag_videos`: a hashtag's counts and the videos on its page, with exact views
- `run_actor`: the Actor's whole input in one call

## Ask in plain words

- *"Compare MrBeast, Mark Rober and Veritasium on median views and upload pace."*
- *"What were @mkbhd's 10 most popular videos this year?"*
- *"Find small cooking channels that post Shorts."*

## Cost

Calls run on your Apify account at the Actor's pay-per-event prices, shown on its [Apify page](https://apify.com/akhil_rajesh/youtube-channel-scraper), plus platform usage while the endpoint's run serves you. Apify's free plan includes monthly credits.

## Data and privacy

This plugin runs no code on your machine. It adds one remote MCP server and one skill (instructions for Claude).

- **What is sent, and where:** when Claude calls one of the tools, Claude Code sends the tool's arguments (for example channel handles such as `@mkbhd`, a playlist link or a topic) and your Apify API token, as an `Authorization` header, over HTTPS to `akhil-rajesh--youtube-channel-scraper.apify.actor`, the Actor's endpoint on the Apify platform. Nothing else from your conversation, files or machine is sent.
- **What the endpoint does with it:** the Actor reads the public pages or public data feeds of YouTube that answer the request, returns the rows to Claude, and stores them in your own Apify account (a run's dataset), where Apify charges for them. It reads no logged-in or private data.
- **Who keeps what:** the run, its input and its rows stay in your Apify account under Apify's [privacy policy](https://apify.com/privacy-policy) and data retention, and you can delete them there. The plugin's author receives no copy of your requests, results or token, only the aggregate run counts and earnings Apify shows every Actor owner.
- **Your token** is kept by Claude Code in your system's credential store, never in a settings file, and is sent only to the endpoint above.

Full policy: [PRIVACY.md](https://github.com/akhilrajesh213/apify-data-plugins/blob/main/PRIVACY.md).

> This is an independent tool, not affiliated with or endorsed by the owners of the data source. All product and company names are the property of their respective owners.
