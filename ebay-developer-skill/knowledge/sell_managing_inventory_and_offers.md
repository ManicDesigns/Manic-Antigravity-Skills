# Managing inventory and offers

Source: https://developer.ebay.com/api-docs/sell/static/inventory/managing-inventory-and-offers.html

# Managing inventory and offers

 

* [Home](/)
* [Develop](/develop)
* [Guides](/develop/guides)
* [Selling Integration Guide](/develop/guides/selling-ig-landing.html)
* Managing inventory and offers

Selling Integration Guide 

[How to develop a selling application](../dev-app.html)

[Configuring seller accounts](../seller-accounts/configuring-seller-accounts.html)

[Getting category information and other metadata](../metadata/getting-metadata.html)

Managing inventory and offers 

[Matching inventory to catalog products](matching-products.html)

[From inventory item to eBay marketplace offer](inventory-item-to-offer.html)

[Managing inventory locations](managing-inventory-locations.html)

[Creating and managing inventory item groups](inventory-item-groups.html)

[Bulk quantity and price updates](bulk-updates.html)

[Retrieving expected listing fees](expected-listing-fees.html)

[Managing inventory items](managing-inventory-items.html)

[Managing images](managing-image-media.html)

[Managing video media](managing-video-media.html)

[Managing documents](managing-document-media.html)

[Managing charitable listings](managing-charitable-listings.html)

[Managing offers](managing-offers.html)

[Migrating listings to Inventory API objects](migrating-listings.html)

[Managing product compatibility](managing-product-compatibility.html)

[Tuning devices and software](tuning-devices-and-software-rest.html)

[Real-time inventory check](realtime-inventory-check.html)

[Authenticity Guarantee](authenticity-guarantee.html)

[Required fields for publishing an offer](publishing-offers.html)

[In-store pickup flow](in-store-pickup.html)

[Multi-warehouse program](multi-warehouse-program.html)

[Energy efficiency information](energy-efficiency.html)

[Common Charger Directive](common-charger-directive.html)

[Inventory API error details](inventory-error-details.html)

[Product Identifier Text](product-identifier-text.html)

[Handling orders](../orders/handling-orders.html)

[Marketing seller inventory](../marketing/marketing-seller-inventory.html)

[Analyzing seller performance](../performance/analyzing-performance.html)

[Using the Sell Feed API](../feed/sell-feed.html)

[Using the Finances API](../finances/finances-landing.html)

The Inventory API is used to create and manage offers on eBay marketplaces. Before diving into the specifics of the API, it is important to know the API's major components. These components are explained below:

* **Location** - A seller must have at least one inventory location set up before that seller can start creating and publishing offers with the Inventory API. Every inventory location must also have a seller-defined merchant location key value.
* **Inventory Item** - An inventory item record must exist for a product before an offer for that product is published on an eBay marketplace and made available for sale. An inventory item record defines a product and includes the following information:
  + A seller-defined SKU (Stock-Keeping Unit) value for the product. This value must be unique within that seller's inventory;
  + Product details, including a product description, product title, item specifics, and image links;
  + Quantity available for purchase through standard shipping, or pickup through the Click and Collect or In-Store Pickup programs;
  + Condition of the product.
* **Inventory Item Group** - A group of related products, that will usually only differ by one or two aspects. For example, the same style of shirt will be available in multiple color and sizes. So, the seller will place each variation of that shirt into an inventory item group. An inventory item group includes the following information:
  + A seller-defined **inventoryItemGroupKey** value for the inventory item group. This value must be unique within that seller's inventory;
  + The products (defined by their SKU value) that are a part of the inventory item group;
  + Title and description of the inventory item group;
  + Product aspects that each item within the group share, and aspects where they differ, such as color and/or size;
  + Links to product images.
* **Offer** - A published offer is the equivalent of an eBay listing. Through the inventory item entity, the product details have already been defined, so the actual offer object adds the following information:
  + The eBay marketplace where the product will be offered;
  + The available quantity of that product on that eBay marketplace;
  + The listing format;
  + The eBay category where the product will be listed;
  + Referenced Payment, Fulfillment, and Return listing policies that set payment, shipping, and return-related values and settings in the offer;
  + The price of the product, and if applicable, the Minimum Advertised Price and Strikethrough Price information;
  + Full paths to one or two eBay Store categories for sellers who own an eBay Store and wish to upload the product to one or two eBay Store categories;
  + Unique identifier of a merchant's store if the product will be made available for sale through the In-Store Pickup or Click and Collect programs;
  + Any tax-related information including the use of tax tables, VAT percentages, or third-party tax category exception codes.
* **Compatible Products** - the product compatibility calls allow the seller to create a compatible vehicle list, or vehicles that are compatible with a motor vehicle part or accessory.

Related topics

* [Selling Apps](/api-docs/sell/static/sell-landing.html)
* [API Documentation](#)

  [Account v1 API](/api-docs/sell/account/overview.html)[Account v2 API](/api-docs/sell/account/v2/overview.html)[Inventory API](/api-docs/sell/inventory/overview.html)[Fulfillment API](/api-docs/sell/fulfillment/overview.html)[Finances API](/api-docs/sell/finances/overview.html)[Marketing API](/api-docs/sell/marketing/overview.html)[Negotiation API](/api-docs/sell/negotiation/overview.html)[Recommendation API](/api-docs/sell/recommendation/overview.html)[Analytics API](/api-docs/sell/analytics/overview.html)[Metadata API](/api-docs/sell/metadata/overview.html)[Compliance API](/api-docs/sell/compliance/overview.html)[Logistics API](/api-docs/sell/logistics/overview.html)[Feed API](/api-docs/sell/feed/overview.html)[Stores API](/api-docs/sell/stores/overview.html)
* [Guides](/develop/guides)
* [Related Docs](#)

  [Using eBay RESTful APIs](/api-docs/static/ebay-rest-landing.html)[Commerce APIs](/develop/apis/restful-apis/commerce-apis)[Developer APIs](/develop/apis/restful-apis/developer-apis)[Trading API](/devzone/xml/docs/reference/ebay/index.html)[Post-Order API](/Devzone/post-order/index.html)[Finding API](/devzone/finding/callref/index.html)[Platform Notifications](/api-docs/static/platform-notifications-landing.html)