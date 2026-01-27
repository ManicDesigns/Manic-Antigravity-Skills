# Deal API

Source: https://developer.ebay.com/api-docs/buy/static/api-deal.html

# Deal API

 

* [Home](/)
* [Develop](/develop)
* [Guides](/develop/guides)
* [Buying Integration Guide](/develop/guides/buying-ig-landing.html)
* Deal API

Buying Integration Guide 

[Buy APIs Overview](buy-overview.html)

[Buy APIs Requirements](buy-requirements.html)

[Browse API](api-browse.html)

[Charity API](api-charity.html)

[Deal API](#)

[Feed API](api-feed.html)

[Feed API beta](api-feed_beta.html)

[Marketing API](api-marketing.html)

[Offer API](api-offer.html)

[Order API](api-order.html)

[Categories for Buy APIs](buy-categories.html)

[Buy API Support by Marketplace](ref-marketplace-supported.html)

[Buy API Field Filters](ref-buy-browse-filters.html)

The eBay Deal API allows third-party developers to search for and retrieve details about eBay deals and events, as well as the items associated with those deals and events.

**Note:** 
This is a [![Limited Icon](/cms/img/docs/partners-api.svg "Limited Release") (Limited Release)](/api-docs/static/versioning.html#Limited). For information on how to obtain access to this API in production, see the [Buy APIs Requirements](buy-requirements.html).

The Deal API leverages the following resources in order to facilitate event discovery, as well as deal and item retrievals by marketplace:

* **deal\_item** – The **getDealItem** method returns a paginated set of deal items. The result set contains all deal items associated with the specified search criteria and marketplace ID.
* **event** – The **getEvent** method retrieves the details for an eBay event, such as applicable coupons, start and end dates, and event terms. The **getEvents** method returns paginated results containing all eBay events for the specified marketplace.
* **event\_item** – The **getEventItems** method returns a paginated set of event items. The result set contains all event items associated with the specified search criteria and marketplace ID.

**Note:** 
For information about using RESTful APIs, see [Using eBay Restful APIs](/api-docs/static/ebay-rest-landing.html).

## Deal API functionality

The eBay Deal API supports the following general use cases:

* [Retrieve deal items](#deal-items)
* [Retrieve events for a marketplace](#events)
* [Retrieve event items](#event-items)

**Note:** 
The marketplace ID is required when using these methods.

### Retrieve deal items

Buyers can retrieve a set of items associated with eBay deals. The result set contains the deal items available in the specified marketplace.

This sample retrieves **1** eBay deal item within the category associated with category ID **257818**:

```json
/buy/deal/v1/deal_item?category_ids=257818&limit=1
```

### Retrieve events for a marketplace

Buyers can retrieve the details associated with events for a specific eBay marketplace. The event details returned include:

* Applicable coupons
* Event description
* Start and end dates
* Event terms

This sample retrieves detailed information for the eBay event associated with event ID **5efd358dc0b33c2**:

```json
/buy/deal/v1/event/5efd358dc0b33c2
```

### Retrieve events items

Buyers can retrieve a set of items associated with eBay events. The result set contains the event items available in the specified marketplace.

This sample retrieves **1** eBay event item within the event associated with event ID **5f063b3ba8f4407ef3d37951**:

```json
/buy/deal/v1/event_item?event_ids=5f063b3ba8f4407ef3d37951&limit=1
```

## Deal API usage

After using the Deal API methods to retrieve the details for eBay deals and events, buyers can leverage the eBay Order API to update existing orders or to create new orders.

For example, you can use the **getEvent** Deal API method to retrieve the available coupons associated with an eBay event. The response returns the coupon redemption code in the **applicableCoupons.redemptionCode** field. You can then apply the redemption code to an existing order using the **applyCoupon** Order API method.

**Note:** 
For more information, see the [Order API](/api-docs/buy/static/api-order.html) section of this Buying Integration Guide.

Related topics

* [Buying Apps](/api-docs/buy/static/buy-landing.html)
* [API Documentation](#)

  [Browse API](/api-docs/buy/browse/overview.html)[Deal API](/api-docs/buy/deal/overview.html)[Feed Beta API](/api-docs/buy/feed/overview.html)[Feed API](/api-docs/buy/feed/v1/overview.html)[Marketing API](/api-docs/buy/marketing/overview.html)[Offer API](/api-docs/buy/offer/overview.html)[Order API](/api-docs/buy/order/overview.html)
* [Guides](/develop/guides)
* [Related Docs](#)

  [Using eBay RESTful APIs](/api-docs/static/ebay-rest-landing.html)[Commerce APIs](/develop/apis/restful-apis/commerce-apis)[Developer APIs](/develop/apis/restful-apis/developer-apis)[Finding API](/devzone/finding/callref/index.html)[Shopping API](/devzone/shopping/docs/callref/index.html)