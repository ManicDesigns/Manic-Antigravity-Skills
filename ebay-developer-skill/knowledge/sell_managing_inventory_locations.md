# Managing inventory locations

Source: https://developer.ebay.com/api-docs/sell/static/inventory/managing-inventory-locations.html

# Managing inventory locations

 

* [Home](/)
* [Develop](/develop)
* [Selling Apps](/develop/selling-apps)
* Managing inventory locations

Selling Integration Guide 

[How to develop a selling application](../dev-app.html)

[Configuring seller accounts](../configuring-seller-accounts/configuring-seller-accounts.html)

[Getting category information and other metadata](../metadata/getting-metadata.html)

Managing inventory and offers 

[Matching inventory to catalog products](matching-products.html)

[From inventory item to eBay marketplace offer](inventory-item-to-offer.html)

[Managing inventory locations](#)

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

Offers published with the Inventory API become live eBay listings, and each offer must be associated with an inventory location.

## Creating inventory locations

The **createInventoryLocation** call is used to create an inventory location. The unique identifier of the inventory location, referred to as a **merchantLocationKey** in the Inventory API calls, is passed in as part of the call URI for the **createInventoryLocation** call. A **merchantLocationKey** value cannot be changed once it is set, and its length cannot exceed 50 characters. In addition to the **merchantLocationKey** value that is passed in to the call URI, the required data for all inventory locations include the following:

* **name**: The name of the inventory location is passed into the **name** field.
* **physical location**: The physical location of the inventory location. At a minimum, the postal code and country **or** city, state, and country should be specified.

Additionally, a **locationtypes** can be specified when creating an inventory location. The location types define the function(s) of the inventory location. The three main types of inventory locations are *warehouse*, *store*, and *fulfillment center*. In some cases, an inventory location can serve as more than one location type. The fields required when publishing an offer may vary depending on the location type(s) of the location. For more information, see [Required fields for publishing an offer](/api-docs/sell/static/inventory/publishing-offers.html#location).

If the **locationTypes** container is omitted when making a **createInventoryLocation** call, the location will default to `WAREHOUSE`.

### Warehouse locations

Warehouse locations are used for traditional shipping and only require the **name** and basic address (**postalCode** and **country** OR **city**, **state**, and **country**) fields to be specified.

### Store locations

Store locations are typically used by US merchants selling product through for In-Store Pickup program A full address (**addressLine1**, **city**, **stateOrProvince**, **postalCode**, and **country**) is required when creating a store location.

In addition, the following fields can be configured:

* **locationInstructions**: These instructions are only applicable for In-Store and Click and Collect orders, and will assist buyers with an easy pickup experience.
* **locationWebUrl**: The URL for the store's website.
* **phone**: [Required] The phone number for the store.
* **operatingHours**: The daily business hours for the store.
* **specialHours**: The special business hours for the store on specific dates.

### Fulfillment center locations

Fulfillment center locations are used by US sellers selling products through multiple inventory locations to get improved estimated delivery dates on their listings. A full address (**addressLine1**, **city**, **stateOrProvince**, **postalCode**, and **country**) is required when creating a fulfillment center location.

In addition, the following field must be configured:

* **fulfillmentCenterSpecifications**: The cut-off time schedule for same day shipping and any cut-off overrides.

## Updating an inventory location

Once an inventory location is established, you can update that inventory location with the **updateInventoryLocation** call. In this call, the inventory location is identified with its **merchantLocationKey** value, that is passed in as part of the call URI. The **updateInventoryLocation** call cannot be used to modify the **merchantLocationkey** value.For warehouse and store inventory locations, address fields can be updated any number of times. Address fields cannot be updated for fulfillment center locations. However, if any address fields were omitted during the **createInventoryLocation** call, they can be added through this method. The following information can be updated: name, phone, operating and special hours, time zone id, geographical coordinates, store website address, location pickup instructions, and additional information about the location. Note that any operating or special hours that are specified with an **updateInventoryLocation** call may overwrite the hours that are currently defined for the inventory location.

## Retrieving inventory locations

A specific inventory location can be retrieved by using the **getInventoryLocation** call. The inventory location to retrieve is identified with its **merchantLocationKey** value, and this value is passed in as part of the call URI. A successful call will retrieve all of the defined details for that inventory location.

If a seller wants to retrieve all inventory locations defined for their account, the **getInventoryLocations** call. To limit the number of inventory location records that are retrieved on one page of data, and/or to control which page of data is retrieved, the seller will use the **limit** and **offset** query parameters. A successful call will retrieve all inventory locations defined for the seller's account.

## Enabling and disabling inventory locations

Although the default behavior for a **createInventoryLocation** call is to enable that inventory location, it is possible to create an inventory location but start it out in the disabled mode. To do this, the seller will include the **merchantLocationStatus** field in the **createInventoryLocation** call, and set its value to `DISABLED`. And to enable a disabled inventory location, the seller will just use the **enableInventoryLocation** call. Similarly, if a seller wants to disable an enabled inventory location, the **disableInventoryLocation** call can be used.

## Deleting an inventory location

To delete an inventory location, the seller uses the **deleteInventoryLocation** call. The inventory location to delete is identified through its **merchantLocationKey** value, and this value is passed in as part of the call URI. Once an inventory location is deleted, it cannot be restored.

Related topics

* [Selling Apps](/api-docs/sell/static/sell-landing.html)
* [API Documentation](#)

  [Account v1 API](/api-docs/sell/account/overview.html)[Account v2 API](/api-docs/sell/account/v2/overview.html)[Inventory API](/api-docs/sell/inventory/overview.html)[Fulfillment API](/api-docs/sell/fulfillment/overview.html)[Finances API](/api-docs/sell/finances/overview.html)[Marketing API](/api-docs/sell/marketing/overview.html)[Negotiation API](/api-docs/sell/negotiation/overview.html)[Recommendation API](/api-docs/sell/recommendation/overview.html)[Analytics API](/api-docs/sell/analytics/overview.html)[Metadata API](/api-docs/sell/metadata/overview.html)[Compliance API](/api-docs/sell/compliance/overview.html)[Logistics API](/api-docs/sell/logistics/overview.html)[Feed API](/api-docs/sell/feed/overview.html)[Stores API](/api-docs/sell/stores/overview.html)
* [Guides](/develop/guides)
* [Related Docs](#)

  [Using eBay RESTful APIs](/api-docs/static/ebay-rest-landing.html)[Commerce APIs](/develop/apis/restful-apis/commerce-apis)[Developer APIs](/develop/apis/restful-apis/developer-apis)[Trading API](/devzone/xml/docs/reference/ebay/index.html)[Post-Order API](/Devzone/post-order/index.html)[Finding API](/devzone/finding/callref/index.html)[Platform Notifications](/api-docs/static/platform-notifications-landing.html)