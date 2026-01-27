# Buying Integration Guide

Source: https://developer.ebay.com/api-docs/buy/static/buying-ig-landing.html

The eBay Buy APIs are RESTful APIs that use OAuth authentication, JSON payloads, and eBay HTTP headers. They provide the capabilities you need to create an eBay shopping and buying experience in your app or website.

---

## Overview

### What You Can Do with Buy APIs
- **Surface eBay items** by searching or using feed files (Browse and Feed API)
- **Add marketing information** for items to promote conversion and up-sell/cross-sell (Marketing API)
- **Search for eBay deals and events** and retrieve deal and event items (Deal API)
- **Change cart contents** and quantity of items in an eBay member's cart (Browse API)
- **Place proxy bids** on auction items for buyers (Offer API)
- **Let buyers purchase items** on your app or site without the Partner being PCI compliant (Order API)
- **Let buyers view purchase orders** and track delivery (Order API)
- **Update inventory** with priority tracking payload information (Feed API)

---

## Buy API Categories

| API | Description | Documentation |
|-----|-------------|---------------|
| **Browse API** | Search and browse eBay items, manage shopping carts | [Overview](https://developer.ebay.com/api-docs/buy/browse/overview.html) |
| **Charity API** | Access charity information for charitable listings | [Guide](https://developer.ebay.com/api-docs/buy/static/api-charity.html) |
| **Deal API** | Search for eBay deals and events | [Overview](https://developer.ebay.com/api-docs/buy/deal/overview.html) |
| **Feed API** | Ingest large catalogs for caching (requires approval) | [Overview](https://developer.ebay.com/api-docs/buy/feed/overview.html) |
| **Feed API Beta** | Beta version with additional features | [Overview](https://developer.ebay.com/api-docs/buy/feed/v1/overview.html) |
| **Marketing API** | Add marketing info for conversions, up-sell/cross-sell | [Overview](https://developer.ebay.com/api-docs/buy/marketing/overview.html) |
| **Offer API** | Place proxy bids on auction items | [Overview](https://developer.ebay.com/api-docs/buy/offer/overview.html) |
| **Order API** | Guest and member checkout, purchase tracking | [Overview](https://developer.ebay.com/api-docs/buy/order/overview.html) |

---

## Buyer Types

Buyers can be:
- **eBay Guests**: Anonymous buyers (not signed in)
- **eBay Members**: Buyers signed into eBay

---

## API Requirements

> **Important!** The eBay Buy APIs are available as a public beta release. There may be some limitations and conditions on their use.

See [Buy APIs Requirements](https://developer.ebay.com/api-docs/buy/static/buy-requirements.html) for detailed requirements.

---

## Key Resources

### Categories for Buy APIs
[Categories Reference](https://developer.ebay.com/api-docs/buy/static/buy-categories.html)

### Buy API Support by Marketplace
[Marketplace Support](https://developer.ebay.com/api-docs/buy/static/ref-marketplace-supported.html)

### Buy API Field Filters
[Field Filters Reference](https://developer.ebay.com/api-docs/buy/static/ref-buy-browse-filters.html)

---

## Related APIs

| API | Type | Description |
|-----|------|-------------|
| Finding API | Traditional | Legacy search API |
| Shopping API | Traditional | Legacy browse API |
| Commerce APIs | REST | Additional commerce functionality |
| Developer APIs | REST | Developer tools |
