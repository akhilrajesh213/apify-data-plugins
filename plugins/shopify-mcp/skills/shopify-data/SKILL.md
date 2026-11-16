---
name: shopify-data
description: "Use the shopify MCP tools when the user asks about a Shopify store's products, prices, discounts, best sellers, new arrivals, stock, collections or a competitor's catalogue."
---

# Shopify store products

The `shopify` MCP server is the live endpoint of the Apify Actor [shopify-mcp-server](https://apify.com/akhil_rajesh/shopify-mcp-server). Use its tools for live data instead of answering from memory, and name the tool's source in the answer.

## Tools

- `get_products`: a store's or collection's products in the store's order, with keyword, vendor, type, tag, price, stock, sale and date filters
- `get_product`: single products by link, with every variant, image, the full description and SEO texts
- `list_collections`: a store's collections (categories) with their links
- `run_actor`: the Actor's whole input in one call

## Cost and limits

- Every row a tool returns is charged to the user's Apify account (pay-per-event, plus platform usage while the endpoint's run serves them). Ask for what the question needs, not more.
- A request that has started runs to its end even if the caller stops waiting.
- Answers name what wasn't found, what didn't load and what a limit left out (fields such as `notFound` and `notRead`). Report those to the user instead of filling the gap yourself.
- The first call can take about 5 to 10 seconds while the endpoint starts; later calls are faster.

## Tips

- Stores can be a domain ('allbirds.com'), a collection link or product links; up to 5 per call and 100 rows in all.
- Some stores with a custom front end don't answer; the answer names them as not read.
- Use `product_details` only when the question needs full descriptions or every image: it makes rows much larger.
