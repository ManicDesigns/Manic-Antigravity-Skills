# eBay Application Architecture Guide

## 1. Determine Your Application Type

### Selling Applications
**Goal**: Manage inventory, process orders, handle customer service for sellers.
- **Key APIs**:
    - `Sell Inventory API`: Manage listings (SKU-based).
    - `Sell Fulfillment API`: Handle orders and shipping.
    - `Sell Analytics API`: Seller performance metrics.
    - `Sell Account API`: Business policies (returns, shipping).

### Buying Applications
**Goal**: Enable users to browse, search, and purchase items.
- **Key APIs**:
    - `Buy Browse API`: Search for items (keyword, category).
    - `Buy Order API`: Guest checkout or member checkout.
    - `Buy Feed API`: Ingest large catalogs for caching (requires approval).

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
