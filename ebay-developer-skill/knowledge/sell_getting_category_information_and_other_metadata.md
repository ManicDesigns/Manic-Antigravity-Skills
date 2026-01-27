# Getting category information and other metadata

Source: https://developer.ebay.com/api-docs/sell/static/metadata/getting-metadata.html

# Getting category information and other metadata

 

* [Home](/)
* [Develop](/develop)
* [Guides](/develop/guides)
* [Selling Integration Guide](/develop/guides/selling-ig-landing.html)
* Getting category information and other metadata

Selling Integration Guide 

[How to develop a selling application](../dev-app.html)

[Configuring seller accounts](../seller-accounts/configuring-seller-accounts.html)

Getting category information and other metadata 

[Finding categories for a listing or promotion](sell-categories.html)

[Item condition ID and name values](condition-id-values.html)

[Specifying hazardous material related information](feature-regulatorhazmatcontainer.html)

[Specifying product safety related information](feature-productsafety.html)

[Managing inventory and offers](../inventory/managing-inventory-and-offers.html)

[Handling orders](../orders/handling-orders.html)

[Marketing seller inventory](../marketing/marketing-seller-inventory.html)

[Analyzing seller performance](../performance/analyzing-performance.html)

[Using the Sell Feed API](../feed/sell-feed.html)

[Using the Finances API](../finances/finances-landing.html)

Creating inventory items often requires you to have specific information about the eBay marketplaces into which you sell. You need to target the correct category for your items and you must create business policies that adhere to the policies of the categories into which you list. In addition, when you create an item, the condition ID and string used to define the condition must match the values for the marketplace where you're listing your item.

The topics in this section address how to get specific information about eBay categories, and other types of metadata that you might need as you configure the items that you place into inventory.

## Finding the correct category ID and item condition for your item

For the best selling results, you should list your items in the categories that most closely match the items you list. The following topics have information where to list your items, and the condition values you should use when listing:

* [Finding categories for a listing or promotion](sell-categories.html)
* [Item condition ID and name values](condition-id-values.html)

## Getting listing policies for different categories

When you list an item in a specific eBay category, you must be sure you follow the listing policies associated with that category.

For example, if you are listing automotive parts, you must list into specific categories that allow for automotive-parts-compatibility items and you must follow the policies for listing the parts in those categories. In this case, you can use the **getAutomotivePartsCompatiblityPolicies** method to retrieve the policies for the specific categories into which you plan to list your automotive parts.

The Metadata API provides the following methods for retrieving the eBay policies that govern how you can list items in the different categories on the different eBay marketplaces:

* [getAutomotivePartsCompatibilityPolicies](/api-docs/sell/metadata/resources/marketplace/methods/getAutomotivePartsCompatibilityPolicies) - Returns the policies that define how to list automotive-parts-compatibility items in the categories of a specific marketplace.
* [getExtendedProducerResponsibilityPolicies](/api-docs/sell/metadata/resources/marketplace/methods/getExtendedProducerResponsibilityPolicies) - Returns the policies that define support for Extended Producer Responsibilities in the categories of a specific marketplace.
* [getItemConditionPolicies](/api-docs/sell/metadata/resources/marketplace/methods/getItemConditionPolicies) - Returns the policies that define how to specify item conditions in the categories of a specific marketplace.
* [getListingStructurePolicies](/api-docs/sell/metadata/resources/marketplace/methods/getListingStructurePolicies) - Returns the policies that define the allowed listing structures (i.e. whether item variations are supported) for the categories of a specific marketplace.
* [getNegotiatedPricePolicies](/api-docs/sell/metadata/resources/marketplace/methods/getNegotiatedPricePolicies) - Returns the policies that define the supported negotiated price (best offer) features for the categories of a specific marketplace.
* [getReturnPolicies](/api-docs/sell/metadata/resources/marketplace/methods/getReturnPolicies) - Returns the policies that define whether or not you must include a return policy for the items you list in the categories of a specific marketplace.

## Getting a list of tax jurisdictions

The Metadata API has a method that retrieves the tax jurisdictions for several countries that have different sales tax percentage rates for the different jurisdictions within the country. For details, see [getSalesTaxJurisdictions](/api-docs/sell/metadata/resources/country/methods/getSalesTaxJurisdictions) to retrieve details on a county's different sales tax jurisdictions, then use the **sales\_tax** resource of the **Accounts API** to set up and manage your sales tax tables.

Related topics

* [Selling Apps](/api-docs/sell/static/sell-landing.html)
* [API Documentation](#)

  [Account v1 API](/api-docs/sell/account/overview.html)[Account v2 API](/api-docs/sell/account/v2/overview.html)[Inventory API](/api-docs/sell/inventory/overview.html)[Fulfillment API](/api-docs/sell/fulfillment/overview.html)[Finances API](/api-docs/sell/finances/overview.html)[Marketing API](/api-docs/sell/marketing/overview.html)[Negotiation API](/api-docs/sell/negotiation/overview.html)[Recommendation API](/api-docs/sell/recommendation/overview.html)[Analytics API](/api-docs/sell/analytics/overview.html)[Metadata API](/api-docs/sell/metadata/overview.html)[Compliance API](/api-docs/sell/compliance/overview.html)[Logistics API](/api-docs/sell/logistics/overview.html)[Feed API](/api-docs/sell/feed/overview.html)[Stores API](/api-docs/sell/stores/overview.html)
* [Guides](/develop/guides)
* [Related Docs](#)

  [Using eBay RESTful APIs](/api-docs/static/ebay-rest-landing.html)[Commerce APIs](/develop/apis/restful-apis/commerce-apis)[Developer APIs](/develop/apis/restful-apis/developer-apis)[Trading API](/devzone/xml/docs/reference/ebay/index.html)[Post-Order API](/Devzone/post-order/index.html)[Finding API](/devzone/finding/callref/index.html)[Platform Notifications](/api-docs/static/platform-notifications-landing.html)