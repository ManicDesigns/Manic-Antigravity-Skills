---
name: developing-with-ebay
description: Provides access to eBay API documentation, examples, and architectural patterns. Use when the user asks to build eBay integrations, search eBay API references, or implement eBay OAuth/Buying/Selling flows.
---

# eBay Developer Skill

## When to Use This Skill
- User asks to "build an eBay app" or "integrate with eBay"
- User needs to look up eBay API endpoints (Sell, Buy, Trading)
- User asks about eBay OAuth 2.0 flows
- User needs code examples for eBay SDKs (Node, Python)
- User mentions "Update Ebay API Skill"

## Workflow
1. **Identify the goal**: Is it a Buying or Selling application?
2. **Search the Knowledge Base**: Use `grep_search` or `view_file` on the `knowledge/` directory to find relevant API specs.
3. **Check Compliance**: Refer to `knowledge/compliance_guardrails.md` before recommending implementation patterns.
4. **Implementation**: Use the Reference Library for code snippets.

## Instructions
- Use the **Architecture Guide** (`knowledge/architecture_guide.md`) to determine the correct API group.
- Check **`knowledge/marketing_and_discounts.md`** for creating Promotions/Ads.
- Use **`knowledge/api_call_index.md`** to quickly find specific endpoints.
- Always check **Rate Limits** and **Compliance** policies.
- For updating the skill, run `scripts/crawl_ebay.py`.

## Resources
- [scripts/crawl_ebay.py](scripts/crawl_ebay.py) - Crawler for updating documentation.
- [knowledge/api_call_index.md](knowledge/api_call_index.md) - Master Index of API calls.
- [knowledge/marketing_and_discounts.md](knowledge/marketing_and_discounts.md) - Marketing & Discounts Guide.
- [knowledge/](knowledge/) - The complete knowledge base.
