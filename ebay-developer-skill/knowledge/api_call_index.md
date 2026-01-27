# eBay API Call Index

## Sell APIs

### Inventory API
- **Manage Inventory**: `GET /sell/inventory/v1/inventory_item`
- **Bulk Update**: `POST /sell/inventory/v1/bulk_update_price_quantity`
- **Offers**: `POST /sell/inventory/v1/offer`

### Fulfillment API
- **Get Orders**: `GET /sell/fulfillment/v1/order`
- **Create Shipping Label**: `POST /sell/logistics/v1/shipping_quote`

### Marketing API
- **Create Campaign**: `POST /sell/marketing/v1/ad_campaign`
- **Get Promotions**: `GET /sell/marketing/v1/promotion`
- **Clone Campaign**: `POST /sell/marketing/v1/ad_campaign/{campaign_id}/clone`

### Analytics API
- **Traffic Report**: `GET /sell/analytics/v1/traffic_report`
- **Seller Standards Profile**: `GET /sell/analytics/v1/seller_standards_profile`

### Metadata API
- **Get Policy**: `GET /sell/metadata/v1/marketplace/EBAY_US/get_automotive_parts_compatibility_policies`

## Buy APIs

### Browse API
- **Search**: `GET /buy/browse/v1/item_summary/search`
- **Get Item**: `GET /buy/browse/v1/item/{item_id}`

### Order API
- **Initiate Guest Checkout**: `POST /buy/order/v1/guest_checkout_session/initiate`
- **Place Guest Order**: `POST /buy/order/v1/guest_checkout_session/{checkoutSessionId}/place_order`

## Developer Tools
- **Application Growth Check**: `https://developer.ebay.com/grow/application-growth-check`
- **Platform Notifications**: `https://developer.ebay.com/api-docs/static/platform-notifications-landing.html`
