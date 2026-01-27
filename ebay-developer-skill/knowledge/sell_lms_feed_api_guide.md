# LMS Feed API Guide

Source: https://developer.ebay.com/api-docs/sell/static/feed/lms-feeds.html

# LMS Feed API Guide

 

* [Home](/)
* [Develop](/develop)
* [Guides](/develop/guides)
* [Selling Integration Guide](/develop/guides/selling-ig-landing.html)
* LMS Feed API Guide

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

LMS Feed API Guide 

[Working with the Sell Feed API using LMS feed types](lms-feeds-working-with-lms.html)

[XML data files overview](lms-feeds-overview.html)

[Inventory upload feed types flow](trading-upload-flow.html)

[Fulfillment upload feed types flow](merchant-data-xml-upload-flow.html)

[Report download feed types flow](merchant-data-downloadable-reports-flow.html)

[Quick reference](lms-feeds-quick-reference.html)

[Rate limits](data-file-limits.html)

[Managing your inventory and orders](lms-feeds-managing-inventory.html)

[Testing and troubleshooting](lms-feeds-testing-and-troubleshooting.html)

[API References](lms-feeds-api-references.html)

[Seller Hub Feed API Guide](fx-feeds.html)

[Using the Finances API](../finances/finances-landing.html)

eBay's LMS feed types make it possible for a Seller's application to send very large amounts of inventory to the eBay site and to download information on single and multiple line-item orders. These services make a large merchant's workflow more efficient by leveraging the eBay infrastructure to use parallel execution and to automatically retry on errors. eBay's LMS feed types make it possible for a Seller's application to:

* Upload large amounts of new inventory, revise existing inventory, end active listings, or re-list ended items
* Acknowledge numerous fulfilled items
* Provide shipping tracking information for numerous items
* Download customizable active inventory reports
* Download customizable order reports

This solution is designed to support merchants who need to manage thousands or tens of thousands (or possibly hundreds of thousands) of eBay listings at one time.

Advantages of using eBay's LMS feed types:

* Shift the processing burden for large call volume (and call retries) from your servers to the eBay servers
* Reduce your network bandwidth and connection requests significantly
* Upload and manage price and quantity (near real-time) updates for thousands of eBay items
* Manage your inventory by eBay Item ID or by SKU
* Download large amounts of information on orders and active listings

The Merchant Data API is a remnant of eBay’s Large Merchant Services solution. Before Large Merchant Services was deprecated, the seller would set up tasks (both upload and download) using the Bulk Data Exchange API, and would then upload and download XML files using the File Transfer API. Although not technically an API, the Merchant Data API defines all of the fields of the files that may be uploaded and all of the fields for the reports that may be downloaded.

The now deprecated Large Merchant Services solution used APIs for inventory management and reporting, coupled with other APIs (such as the Trading API), to complete an overall large merchant solution. Large Merchant Services (LMS) functionality as a SOAP service has been replaced by sending the same files, through the eBay [Sell Feed API](/api-docs/sell/feed/overview.html) using LMS feed types.

This user guide provides an overview of working with the LMS feed types, the XML data files used with LMS feed types, and describes how to use them with the Sell Feed API in different flows, as well as providing additional reference information.

Related topics

* [Selling Apps](/api-docs/sell/static/sell-landing.html)
* [API Documentation](#)

  [Account v1 API](/api-docs/sell/account/overview.html)[Account v2 API](/api-docs/sell/account/v2/overview.html)[Inventory API](/api-docs/sell/inventory/overview.html)[Fulfillment API](/api-docs/sell/fulfillment/overview.html)[Finances API](/api-docs/sell/finances/overview.html)[Marketing API](/api-docs/sell/marketing/overview.html)[Negotiation API](/api-docs/sell/negotiation/overview.html)[Recommendation API](/api-docs/sell/recommendation/overview.html)[Analytics API](/api-docs/sell/analytics/overview.html)[Metadata API](/api-docs/sell/metadata/overview.html)[Compliance API](/api-docs/sell/compliance/overview.html)[Logistics API](/api-docs/sell/logistics/overview.html)[Feed API](/api-docs/sell/feed/overview.html)[Stores API](/api-docs/sell/stores/overview.html)
* [Guides](/develop/guides)
* [Related Docs](#)

  [Using eBay RESTful APIs](/api-docs/static/ebay-rest-landing.html)[Commerce APIs](/develop/apis/restful-apis/commerce-apis)[Developer APIs](/develop/apis/restful-apis/developer-apis)[Trading API](/devzone/xml/docs/reference/ebay/index.html)[Post-Order API](/Devzone/post-order/index.html)[Finding API](/devzone/finding/callref/index.html)[Platform Notifications](/api-docs/static/platform-notifications-landing.html)