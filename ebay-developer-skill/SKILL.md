---
name: developing-with-ebay
description: Provides access to eBay API documentation, examples, and architectural patterns. Use when the user asks to build eBay integrations, search eBay API references, or implement eBay OAuth/Buying/Selling flows.
---

# eBay Developer Skill

## When to Use This Skill

- User asks to "build an eBay app" or "integrate with eBay"
- User needs to look up eBay API endpoints (Sell, Buy, Trading, Taxonomy)
- User asks about eBay OAuth 2.0 flows
- User needs code examples for eBay SDKs (Node, Python)
- User asks to "discover categories", "find item aspects", or fix "missing specifics errors"
- User mentions "Update Ebay API Skill"

## Workflow

1. **Identify the goal**: Is it a Buying or Selling application?
2. **Search the Knowledge Base**: Use `grep_search` or `view_file` on the `knowledge/` directory to find relevant API specs.
3. **Check Compliance**: Refer to `knowledge/compliance_guardrails.md` before recommending implementation patterns.
4. **Implementation**: Use the Reference Library for code snippets.

## Instructions

- Use the **Architecture Guide** (`knowledge/architecture_guide.md`) to determine the correct API group.
- Check **`knowledge/commerce_taxonomy_api.md`** for handling categories and retrieving required item specifics.
- Check **`knowledge/marketing_and_discounts.md`** for creating Promotions/Ads.
- Use **`knowledge/sell_inventory_mapping_api.md`** when designing AI-driven or automated listing recommendations via GraphQL.
- Use **`knowledge/api_call_index.md`** to quickly find specific endpoints.
- Use **`knowledge/guide_listing_v2_and_bulk.md`** for multi-SKU inventory item groups and bulk listing operations.
- Use **`knowledge/ebay_github_official_tools.md`** for official eBay SDKs and the MCP AI server.
- **MCP Server**: For AI agent projects, configure the official `@ebay/npm-public-api-mcp` to give agents direct eBay API access.
- **Digital Signatures**: EU/UK seller apps MUST use `digital-signature-nodejs-sdk` — see compliance guardrails.
- **Taxonomy Tracking**: Use the `taxonomy-sdk` CLI to detect aspect metadata changes across eBay categories.
- Always check **Rate Limits** and **Compliance** policies.
- For updating the skill, run `scripts/crawl_ebay.py`.

## Resources

- [scripts/crawl_ebay.py](scripts/crawl_ebay.py) - Crawler for updating documentation.
- [knowledge/api_call_index.md](knowledge/api_call_index.md) - Master Index of API calls.
- [knowledge/marketing_and_discounts.md](knowledge/marketing_and_discounts.md) - Marketing & Discounts Guide.
- [knowledge/ebay_github_official_tools.md](knowledge/ebay_github_official_tools.md) - Official eBay GitHub SDKs & MCP Server.
- [knowledge/guide_listing_v2_and_bulk.md](knowledge/guide_listing_v2_and_bulk.md) - Multi-SKU & Bulk Listing Guide.
- [knowledge/](knowledge/) - The complete knowledge base.
