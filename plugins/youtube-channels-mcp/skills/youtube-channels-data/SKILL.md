---
name: youtube-channels-data
description: "Use the youtube-channels MCP tools when the user asks about YouTube channels, creators or competitors: subscribers, views, upload pace, recent or popular videos, Shorts, playlists, hashtags, or finding channels on a topic."
---

# YouTube channel data

The `youtube-channels` MCP server is the live endpoint of the Apify Actor [youtube-channel-scraper](https://apify.com/akhil_rajesh/youtube-channel-scraper). Use its tools for live data instead of answering from memory, and name the tool's source in the answer.

## Tools

- `get_channel_info`: subscribers, exact total views and video count, joined date, country, description, links
- `get_channel_videos`: a channel's videos, Shorts, streams and popular videos, with filters
- `compare_channels`: one row per channel, biggest first, with median views, upload pace and days since the last upload
- `find_channels`: channels for a topic, from its hashtag page, with their stats
- `get_playlist_videos`: a public playlist and its first 100 videos
- `get_hashtag_videos`: a hashtag's counts and the videos on its page, with exact views
- `run_actor`: the Actor's whole input in one call

## Cost and limits

- Every row a tool returns is charged to the user's Apify account (pay-per-event, plus platform usage while the endpoint's run serves them). Ask for what the question needs, not more.
- A request that has started runs to its end even if the caller stops waiting.
- Answers name what wasn't found, what didn't load and what a limit left out (fields such as `notFound` and `notRead`). Report those to the user instead of filling the gap yourself.
- The first call can take about 5 to 10 seconds while the endpoint starts; later calls are faster.

## Tips

- Channels can be given as `@handle`, a channel link or a channel id.
- Video transcripts and comments aren't available; say so rather than guessing.
- Each tool call reads up to 5 channels and 200 rows; split bigger asks into several calls.
