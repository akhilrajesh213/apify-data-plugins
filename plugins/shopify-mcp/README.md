# Shopify store products (Claude Code plugin)

Products of any Shopify store: prices and compare-at prices, discounts, variants with SKUs and stock, vendors, tags, images and collections, best sellers first and priced for any country, through an Apify MCP server.

The plugin connects Claude Code to the live MCP endpoint of the Apify Actor [shopify-mcp-server](https://apify.com/akhil_rajesh/shopify-mcp-server) (`https://akhil-rajesh--shopify-mcp-server.apify.actor/mcp`) and adds a skill that tells Claude when to use it.

## Install

```bash
claude plugin marketplace add akhilrajesh213/apify-data-plugins
claude plugin install shopify-mcp@akhil-rajesh-data
```

Claude Code asks for your **Apify API token** when the plugin is enabled and keeps it in your system's credential store. Create a free account at [apify.com](https://apify.com) and copy the token from Apify Console > Settings > API & Integrations.

## Tools

- `get_products`: a store's or collection's products in the store's order, with keyword, vendor, type, tag, price, stock, sale and date filters
- `get_product`: single products by link, with every variant, image, the full description and SEO texts
- `list_collections`: a store's collections (categories) with their links
- `run_actor`: the Actor's whole input in one call

## Ask in plain words

- *"What are allbirds.com's best sellers and their prices?"*
- *"Which products on gymshark.com are on sale right now, and by how much?"*
- *"Show me this store's products published in the last 30 days."*
- *"Compare this product's price in the US and the UK."*

## Cost

Calls run on your Apify account at the Actor's pay-per-event prices, shown on its [Apify page](https://apify.com/akhil_rajesh/shopify-mcp-server), plus platform usage while the endpoint's run serves you. Apify's free plan includes monthly credits.

## Data and privacy

This plugin runs no code on your machine. It adds one remote MCP server and one skill (instructions for Claude).

- **What is sent, and where:** when Claude calls one of the tools, Claude Code sends the tool's arguments (for example store addresses such as `allbirds.com`, product links and filters) and your Apify API token, as an `Authorization` header, over HTTPS to `akhil-rajesh--shopify-mcp-server.apify.actor`, the Actor's endpoint on the Apify platform. Nothing else from your conversation, files or machine is sent.
- **What the endpoint does with it:** the Actor reads the public pages or public data feeds of the Shopify stores named that answer the request, returns the rows to Claude, and stores them in your own Apify account (a run's dataset), where Apify charges for them. It reads no logged-in or private data.
- **Who keeps what:** the run, its input and its rows stay in your Apify account under Apify's [privacy policy](https://apify.com/privacy-policy) and data retention, and you can delete them there. The plugin's author receives no copy of your requests, results or token, only the aggregate run counts and earnings Apify shows every Actor owner.
- **Your token** is kept by Claude Code in your system's credential store, never in a settings file, and is sent only to the endpoint above.

Full policy: [PRIVACY.md](https://github.com/akhilrajesh213/apify-data-plugins/blob/main/PRIVACY.md).

> This is an independent tool, not affiliated with or endorsed by the owners of the data source. All product and company names are the property of their respective owners.
