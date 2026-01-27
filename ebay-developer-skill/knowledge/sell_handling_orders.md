# Handling orders

Source: https://developer.ebay.com/api-docs/sell/static/orders/handling-orders.html

# Handling orders

 

* [Home](/)
* [Develop](/develop)
* [Guides](/develop/guides)
* [Selling Integration Guide](/develop/guides/selling-ig-landing.html)
* Handling orders

Selling Integration Guide 

[How to develop a selling application](../dev-app.html)

[Configuring seller accounts](../seller-accounts/configuring-seller-accounts.html)

[Getting category information and other metadata](../metadata/getting-metadata.html)

[Managing inventory and offers](../inventory/managing-inventory-and-offers.html)

Handling orders 

[Order fulfillment](order-fulfillment.html)

[Discovering unfulfilled orders](discovering-unfulfilled-orders.html)

[Handling unfulfilled line items](handling-unfulfilled-lineitems.html)

[Managing fulfillments](managing-fulfillments.html)

[Working with Order Feeds](generating-and-retrieving-order-reports.html)

[Marketing seller inventory](../marketing/marketing-seller-inventory.html)

[Analyzing seller performance](../performance/analyzing-performance.html)

[Using the Sell Feed API](../feed/sell-feed.html)

[Using the Finances API](../finances/finances-landing.html)

Handling orders is the phase of selling that includes completing the process of packaging, addressing, handling, and shipping each order, as well as dealing with any issues that arise after each order is shipped, such as cancellations, returns, inquiries, and disputes between seller and buyer.

## Completing the fulfillment process

The set of specifications for addressing, handling, and shipping each package is known as a *shipping fulfillment*. The following topics cover the process of creating and completing shipping fulfillments:

* [Order fulfillment](/api-docs/sell/static/orders/order-fulfillment.html) introduces the API objects involved in the order fulfillment process, and illustrates the relationships between those objects.
* [Discovering unfulfilled orders](/api-docs/sell/static/orders/discovering-unfulfilled-orders.html) describes how to determine which of a seller's orders have not been completely fulfilled yet.
* [Handling unfulfilled line items](/api-docs/sell/static/orders/handling-unfulfilled-lineitems.html) helps you to ensure that all of an order's line items are packaged and assigned to a shipping fulfillment.
* [Managing fulfillments for an order](/api-docs/sell/static/orders/managing-fulfillments.html) covers the process of overseeing the completion of all shipping fulfillments, sending the order on its way to the buyer.
* [Working with order feeds](generating-and-retrieving-order-reports.html) covers generating and retrieving order reports using the Order Task Feed flow.

## Resolving order issues

The eBay Post-Order API is the current tool that you can use to resolve buyer cancellations, returns, inquiries, and disputes. You will find information about these issues and the API at [Post-Order API – Usage Guide](https://developer.ebay.com/devzone/post-order/concepts/usageguide.html).

Related topics

* [Selling Apps](/api-docs/sell/static/sell-landing.html)
* [API Documentation](#)

  [Account v1 API](/api-docs/sell/account/overview.html)[Account v2 API](/api-docs/sell/account/v2/overview.html)[Inventory API](/api-docs/sell/inventory/overview.html)[Fulfillment API](/api-docs/sell/fulfillment/overview.html)[Finances API](/api-docs/sell/finances/overview.html)[Marketing API](/api-docs/sell/marketing/overview.html)[Negotiation API](/api-docs/sell/negotiation/overview.html)[Recommendation API](/api-docs/sell/recommendation/overview.html)[Analytics API](/api-docs/sell/analytics/overview.html)[Metadata API](/api-docs/sell/metadata/overview.html)[Compliance API](/api-docs/sell/compliance/overview.html)[Logistics API](/api-docs/sell/logistics/overview.html)[Feed API](/api-docs/sell/feed/overview.html)[Stores API](/api-docs/sell/stores/overview.html)
* [Guides](/develop/guides)
* [Related Docs](#)

  [Using eBay RESTful APIs](/api-docs/static/ebay-rest-landing.html)[Commerce APIs](/develop/apis/restful-apis/commerce-apis)[Developer APIs](/develop/apis/restful-apis/developer-apis)[Trading API](/devzone/xml/docs/reference/ebay/index.html)[Post-Order API](/Devzone/post-order/index.html)[Finding API](/devzone/finding/callref/index.html)[Platform Notifications](/api-docs/static/platform-notifications-landing.html)