# eBay API Call Index

## Sell APIs

### Inventory API
- **Manage Inventory**: `GET /sell/inventory/v1/inventory_item`
- **Create/Replace Item**: `PUT /sell/inventory/v1/inventory_item/{sku}`
- **Bulk Update**: `POST /sell/inventory/v1/bulk_update_price_quantity`
- **Create Offer**: `POST /sell/inventory/v1/offer`
- **Publish Offer**: `POST /sell/inventory/v1/offer/{offerId}/publish`

#### Inventory Locations
- **Create Location**: `POST /sell/inventory/v1/location/{merchantLocationKey}`
- **Get Location**: `GET /sell/inventory/v1/location/{merchantLocationKey}`
- **Get All Locations**: `GET /sell/inventory/v1/location`
- **Update Location**: `POST /sell/inventory/v1/location/{merchantLocationKey}/update_location_details`
- **Enable Location**: `POST /sell/inventory/v1/location/{merchantLocationKey}/enable`
- **Disable Location**: `POST /sell/inventory/v1/location/{merchantLocationKey}/disable`
- **Delete Location**: `DELETE /sell/inventory/v1/location/{merchantLocationKey}`

### Account API
#### Business Policies
- **Create Fulfillment Policy**: `POST /sell/account/v1/fulfillment_policy`
- **Get Fulfillment Policies**: `GET /sell/account/v1/fulfillment_policy`
- **Create Payment Policy**: `POST /sell/account/v1/payment_policy`
- **Get Payment Policies**: `GET /sell/account/v1/payment_policy`
- **Create Return Policy**: `POST /sell/account/v1/return_policy`
- **Get Return Policies**: `GET /sell/account/v1/return_policy`

#### Custom Policies
- **Create Custom Policy**: `POST /sell/account/v1/custom_policy`
- **Get Custom Policies**: `GET /sell/account/v1/custom_policy`

### Fulfillment API
- **Get Orders**: `GET /sell/fulfillment/v1/order`
- **Get Order**: `GET /sell/fulfillment/v1/order/{orderId}`
- **Create Shipping Fulfillment**: `POST /sell/fulfillment/v1/order/{orderId}/shipping_fulfillment`

### Logistics API (Restricted)
- **Create Shipping Quote**: `POST /sell/logistics/v1/shipping_quote`
- **Create From Quote**: `POST /sell/logistics/v1/shipment/create_from_shipping_quote`
- **Download Label**: `GET /sell/logistics/v1/shipment/{shipmentId}/download_label_file`

### Marketing API
- **Create Campaign**: `POST /sell/marketing/v1/ad_campaign`
- **Get Campaigns**: `GET /sell/marketing/v1/ad_campaign`
- **Clone Campaign**: `POST /sell/marketing/v1/ad_campaign/{campaign_id}/clone`
- **Bulk Create Ads**: `POST /sell/marketing/v1/ad_campaign/{campaign_id}/bulk_create_ads_by_listing_id`
- **Get Promotions**: `GET /sell/marketing/v1/promotion`

### Finances API
- **Get Payouts**: `GET /sell/finances/v1/payout`
- **Get Transactions**: `GET /sell/finances/v1/transaction`
- **Get Seller Funds Summary**: `GET /sell/finances/v1/seller_funds_summary`

### Analytics API
- **Traffic Report**: `GET /sell/analytics/v1/traffic_report`
- **Seller Standards Profile**: `GET /sell/analytics/v1/seller_standards_profile`

### Recommendation API
- **Find Listing Recommendations**: `POST /sell/recommendation/v1/find`

### Metadata API
- **Get Policies**: `GET /sell/metadata/v1/marketplace/{marketplace_id}/get_automotive_parts_compatibility_policies`

---

## Buy APIs

### Browse API
- **Search**: `GET /buy/browse/v1/item_summary/search`
- **Get Item**: `GET /buy/browse/v1/item/{item_id}`
- **Get Items by Group**: `GET /buy/browse/v1/item/get_items_by_item_group`
- **Add to Cart**: `POST /buy/browse/v1/shopping_cart/add_item`
- **Get Cart**: `GET /buy/browse/v1/shopping_cart`

### Deal API
- **Get Events**: `GET /buy/deal/v1/event`
- **Get Event Items**: `GET /buy/deal/v1/event/{event_id}/event_item`
- **Get Deal Items**: `GET /buy/deal/v1/deal_item`

### Feed API
- **Get Item Feed**: `GET /buy/feed/v1/item`
- **Get Item Group Feed**: `GET /buy/feed/v1/item_group`
- **Get Item Snapshot Feed**: `GET /buy/feed/v1/item_snapshot`

### Marketing API (Buy)
- **Get Merchandised Products**: `GET /buy/marketing/v1/merchandised_product`

### Offer API
- **Place Proxy Bid**: `POST /buy/offer/v1/bidding/{item_id}/place_proxy_bid`
- **Get Bidding**: `GET /buy/offer/v1/bidding/{item_id}`

### Order API
- **Initiate Guest Checkout**: `POST /buy/order/v2/guest_checkout_session/initiate`
- **Place Guest Order**: `POST /buy/order/v2/guest_checkout_session/{checkoutSessionId}/place_order`
- **Get Guest Purchase Order**: `GET /buy/order/v2/guest_purchase_order/{purchaseOrderId}`

---

## Trading API (XML - Legacy)

### Listing
- **AddItem**: Create auction listing
- **AddFixedPriceItem**: Create fixed-price listing
- **AddItems**: Create up to 5 listings

### Orders
- **GetOrders**: Retrieve seller orders
- **CompleteSale**: Mark shipped, add tracking, leave feedback
- **GetSellerTransactions**: Get line item info

### Account
- **GetAccount**: Retrieve seller account balance and fees
- **SetShippingDiscountProfiles**: Configure shipping discounts
- **GetShippingDiscountProfiles**: Retrieve discount profiles

---

## Developer Tools
- **Application Growth Check**: `https://developer.ebay.com/grow/application-growth-check`
- **Platform Notifications**: `https://developer.ebay.com/api-docs/static/platform-notifications-landing.html`

