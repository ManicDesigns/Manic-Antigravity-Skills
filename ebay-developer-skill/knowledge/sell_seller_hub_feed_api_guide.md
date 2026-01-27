# Seller Hub Feed API Guide

Source: https://developer.ebay.com/api-docs/sell/static/feed/fx-feeds.html

# Seller Hub Feed API Guide

 

* [Home](/)
* [Develop](/develop)
* [Guides](/develop/guides)
* [Selling Integration Guide](/develop/guides/selling-ig-landing.html)
* Seller Hub Feed API Guide

Selling Integration Guide 

[How to develop a selling application](../dev-app.html)

[Configuring seller accounts](../seller-accounts/configuring-seller-accounts.html)

[Getting category information and other metadata](../metadata/getting-metadata.html)

[Managing inventory and offers](../inventory/managing-inventory-and-offers.html)

[Handling orders](../orders/handling-orders.html)

[Marketing seller inventory](../marketing/marketing-seller-inventory.html)

[Analyzing seller performance](../performance/analyzing-performance.html)

Using the Sell Feed API 

[General Sell Feed API tasks (flows)](general-feed-tasks.html)

[Creating schedules](creating_schedules.html)

[LMS Feed API Guide](lms-feeds.html)

Seller Hub Feed API Guide 

[Using Seller Hub feed types](../feed/fx-feeds-sell-feed-and-fx.html)

[Seller Hub feed flow](../feed/fx-feeds-overview.html)

[Quick reference](../feed/fx-feeds-quick-reference.html)

[Seller Hub feed API references](../feed/fx-feeds-references.html)

[Using the Finances API](../finances/finances-landing.html)

This guide provides information on extending Seller Hub programmatically through a RESTful API. Sellers can upload feeds using the [task](/api-docs/sell/feed/resources/methods#h2-task) resource (part of the [Sell Feed API](/api-docs/sell/feed/overview.html), a REST web service) with Seller Hub feed types, and their feed data file. The feed data file is the same one as used with Seller Hub. Uploading feeds allow sellers to:

* Add, revise, and end listings (`FX_LISTING`)
* Provide the status of your orders and be used for order fulfillment. This allows updates to fulfillment related information like tracking, shipping carriers, and similar details (`FX_FULFILLMENT`)

**Note:** The same feed file is used with Seller Hub and with the Sell Feed API feeds.

This guide contains an overview of using Seller Hub feed types, describes how to use them with the Sell Feed API including the data files (the Seller Hub feed flow), and provides additional reference information.

Related topics

* [Selling Apps](/api-docs/sell/static/sell-landing.html)
* [API Documentation](#)

  [Account v1 API](/api-docs/sell/account/overview.html)[Account v2 API](/api-docs/sell/account/v2/overview.html)[Inventory API](/api-docs/sell/inventory/overview.html)[Fulfillment API](/api-docs/sell/fulfillment/overview.html)[Finances API](/api-docs/sell/finances/overview.html)[Marketing API](/api-docs/sell/marketing/overview.html)[Negotiation API](/api-docs/sell/negotiation/overview.html)[Recommendation API](/api-docs/sell/recommendation/overview.html)[Analytics API](/api-docs/sell/analytics/overview.html)[Metadata API](/api-docs/sell/metadata/overview.html)[Compliance API](/api-docs/sell/compliance/overview.html)[Logistics API](/api-docs/sell/logistics/overview.html)[Feed API](/api-docs/sell/feed/overview.html)[Stores API](/api-docs/sell/stores/overview.html)
* [Guides](/develop/guides)
* [Related Docs](#)

  [Using eBay RESTful APIs](/api-docs/static/ebay-rest-landing.html)[Commerce APIs](/develop/apis/restful-apis/commerce-apis)[Developer APIs](/develop/apis/restful-apis/developer-apis)[Trading API](/devzone/xml/docs/reference/ebay/index.html)[Post-Order API](/Devzone/post-order/index.html)[Finding API](/devzone/finding/callref/index.html)[Platform Notifications](/api-docs/static/platform-notifications-landing.html)