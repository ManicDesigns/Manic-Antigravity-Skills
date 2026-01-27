# Post-Order API User Guide

Source: https://developer.ebay.com/api-docs/user-guides/static/post-order-user-guide-landing.html

# Post-Order API User Guide

 

* [Home](/)
* [Develop](/develop)
* [Guides](/develop/guides)
* [Traditional API User Guides](/develop/guides/traditional-api-user-guides)
* Post-Order API User Guide

Post-Order API User Guide 

[Business use cases](post-order-user-guide/post-order-business-use-cases.html)

[Handling order inquiries](post-order-user-guide/post-order-inquiries.html)

[Handling order cancellations](post-order-user-guide/post-order-cancellations.html)

[Handling returns](post-order-user-guide/post-order-returns.html)

[Escalating and resolving a case](post-order-user-guide/post-order-resolutions.html)

[API Reference](../../../devzone/post-order/index.html)

The **Post-Order API** addresses customer scenarios that can take place after an order is placed. Use the API to implement self-service flows that process order cancellations and item returns. You can also create flows that let buyers inquire about the status of an order and, in the extreme case that things don't go as planned, flows that let buyers and sellers pursue an escalation to the eBay customer support team.

**Note:** Post-purchase experiences (also referred to as "post-transaction" or "after-sale" processes) help to ensure buyers get the items they want. Buyers can cancel orders within an allotted time frame, return items that are significantly not as described (SNAD), and inquire about an item not received (INR).

## API Overview

The **Post-Order API** contains a RESTful set of operations that allow you to automate post-purchase flows, either partially or completely. Examples of flows supported by this API include returns, item inquiries, order cancellations, and buyer/seller disputes. The **Post-Order API** is available to buyers and sellers in different marketplaces. The list of available eBay marketplaces are contained in the [MarketplaceIdEnum](/devzone/post-order/types/MarketplaceIdEnum.html) type definition. This API is mostly useful to sellers, but buyers may also find some calls useful.

The major features of the API include:

* **[Order Inquiries](post-order-user-guide/post-order-inquiries.html)** - Inquiries let buyers look into shipments they have not received within a reasonable time frame. Sellers can respond to the inquiries with shipping information, or a refund if appropriate. This API includes a set of operations that allows sellers to manage Item Not Received (INR) inquiries they receive from buyers when an item doesn't arrive within the estimated delivery date window.
* **[Order Cancellations](post-order-user-guide/post-order-cancellations.html)** - Retail-standard cancellations let buyers cancel orders that haven't yet been shipped. This API includes a set of operations that allows the buyer or seller to cancel a paid or unpaid order, and allows a large seller to manage order cancellation requests.

  **Note:** Currently, cancellations apply to whole orders only. Buyers cannot cancel individual line items within multiple line item orders.
* **[Returns](post-order-user-guide/post-order-returns.html)** - Buyers are able to initiate a return and get a refund or a replacement for a received item. This API includes a large set of operations that allows sellers to accept return requests from buyers, issue partial or full refunds to buyers, send replacement items to buyers, and more.
* **[Case Management](post-order-user-guide/post-order-resolutions.html)** - Both buyers and sellers can escalate issues to the eBay customer support team when seller-to-buyer negotiations associated inquiries and returns do not resolve order issues. In these instances, the eBay customer service team will step in and resolve the order dispute. This API includes a set of operations that allows sellers to manage Item Not Received (INR) and Return cases. If a buyer and seller are not able to resolve an INR Inquiry or a Return request, the buyer or seller can escalate that inquiry or Return request to an eBay customer support case.

This API contains both seller and buyer-facing interfaces. Normally, you will implement only the seller-facing interfaces in your applications; the buyer-facing calls are included to facilitate application testing (buyers use eBay web flows to initiate cancellations, returns, inquiries, and escalations).

Although you can still use the **Trading API** to handle after-sale flows, to take advantage of updated features in your applications using specific fields in the Trading API that help streamline after-sale activities, you must use the **Post-Order API**. The material presented in these sections discuss how to incorporate these fields into your existing after-sale flows, as well as any required changes to create the best possible buyer experiences.

## Related information

See the following eBay help pages for related information and the flows available on the eBay website (non-programmatic flows):

* [How Sellers Manage Returns & Refunds](https://www.ebay.com/help/returns-refunds#returns-refunds-sellers)
* [Returning Items](https://www.ebay.com/help/returns-refunds#returning-item-purchased)
* [Resolving buyer issues](https://www.ebay.com/help/selling/resolving-buyer-issues/resolving-buyer-issues?id=4076)
* [Resolving issues with sellers](https://www.ebay.com/help/buying/resolving-issues-sellers/resolving-issues-sellers?id=4011)