# eBay Application Architecture Guide

## 1. Determine Your Application Type

### Selling Applications
**Goal**: Manage inventory, process orders, handle customer service for sellers.
- **Key APIs**:
    - `Sell Inventory API`: Manage listings (SKU-based). See [Listing Creation Guide](guide_listing_creation_v2.md).
    - `Sell Inventory API - Locations`: Manage merchant locations (warehouse, store, fulfillment center). See [Managing Inventory Locations](sell_managing_inventory_locations.md).
    - `Sell Fulfillment API`: Handle orders and shipping. See [Order Management Guide](guide_order_management_v2.md).
    - `Sell Analytics API`: Seller performance metrics.
    - `Sell Account API`: Business policies (returns, shipping). See [Account Management Guide](guide_account_management_v2.md).
    - `Sell Marketing API`: Promoted Listings, discounts, campaigns. See [Marketing & Promotions Guide](guide_marketing_promotions_v2.md).

### Buying Applications
**Goal**: Enable users to browse, search, and purchase items.
- **Key APIs**:
    - `Buy Browse API`: Search for items (keyword, category).
    - `Buy Order API`: Guest checkout or member checkout.
    - `Buy Feed API`: Ingest large catalogs for caching (requires approval).
    - `Buy Deal API`: Search for eBay deals and events.
    - `Buy Marketing API`: Add marketing info for conversions.
    - `Buy Offer API`: Place proxy bids on auction items.
- See [Buying Integration Guide](buy_integration_guide.md) for complete overview.

## 2. Authentication Strategy (OAuth 2.0)

### Application-Only (Client Credentials)
- **Use Case**: Searching for items, getting public metadata.
- **Flow**: `client_credentials` grant.
- **Access**: Public data (no user context).

### User-Acting (Authorization Code)
- **Use Case**: Listing an item, viewing private orders, bidding.
- **Flow**: `authorization_code` grant with **Consent Screen**.
- **Access**: Private user data. requires `redirect_uri`.

## 3. Recommended Tech Stack
- **Node.js**: [eBay OAuth Client](https://github.com/eBay/ebay-oauth-nodejs-client)
- **Python**: [eBay OAuth Client](https://github.com/eBay/ebay-oauth-python-client)
- **Java/C#**: Official SDKs available.

## 4. Testing Pattern
1. **Sandbox**: strictly for functional testing. Mock data.
    - **Note**: Sandbox has its own endpoints (`api.sandbox.ebay.com`).
2. **Production**: Live data. Start with low volume.

## 5. Documentation Guides

| Guide | Description |
|-------|-------------|
| [Listing Creation (v2)](guide_listing_creation_v2.md) | Single/multi-SKU listings, bulk creation |
| [Account Management (v2)](guide_account_management_v2.md) | Business policies, finances, rate tables |
| [Order Management (v2)](guide_order_management_v2.md) | Fulfillment, shipping, cancellations |
| [Marketing & Promotions (v2)](guide_marketing_promotions_v2.md) | Promoted Listings, discounts, campaigns |
| [Buying Integration](buy_integration_guide.md) | Browse, Order, Feed, Deal APIs |
| [TPP Guide](regulatory_third_party_providers.md) | Regulated third party provider requirements |

