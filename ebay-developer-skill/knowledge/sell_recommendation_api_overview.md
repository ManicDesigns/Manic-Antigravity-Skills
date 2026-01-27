# Recommendation API Overview

Source: https://developer.ebay.com/api-docs/sell/recommendation/static/overview.html

# Recommendation API Overview

v1.1.0

 

* [Home](/)
* [Develop](/develop)
* [Selling Apps](/develop/selling-apps)
* [Other APIs](/develop/selling-apps/other-apis-1)
* Recommendation API Overview

[API overview](/api-docs/sell/recommendation/overview.html)

API reference 

[Resources](/api-docs/sell/recommendation/resources/methods)

listing\_recommendation 

[findListingRecommendations](/api-docs/sell/recommendation/resources/listing_recommendation/methods/findListingRecommendations)

[Index](/api-docs/sell/recommendation/fields)

[API release notes](/api-docs/sell/recommendation/release-notes.html)

[OpenAPI 3 JSON Contract (beta)](/api-docs/master/sell/recommendation/openapi/3/sell_recommendation_v1_oas3.json)

[OpenAPI 3 YAML Contract (beta)](/api-docs/master/sell/recommendation/openapi/3/sell_recommendation_v1_oas3.yaml)

The **Recommendation API** returns information that sellers can use to configure Promoted Listings ad campaigns.

**Note:** The Recommendation API only applies to general strategy campaigns that use the Cost Per Sale (CPS) funding model; it does not apply to priority strategy campaigns that use the Cost Per Click (CPC) funding model.

The Recommendation API currently has a single recommendation type, `AD`, that returns information pertaining to **Promoted Listings** ad campaigns. Seller can use the recommendations returned as guidelines for setting up campaigns.

In the eBay marketplace, where an increased visibility directly correlates to the buyer conversion rate, information returned with the `AD` recommendation type can help you know which listings to promote and how to configure ad campaigns.

For details about creating and running ad campaigns, see [Promoted Listings](/api-docs/sell/static/marketing/promoted-listings.html) in the *Selling Integration Guide*.

## Technical overview

The Recommendation API currently contains the following resource:

* **listing\_recommendation**

This resource has a single method, **findListingRecommendations**, that returns information that can help sellers optimize their listing configurations.

Currently, **findListingRecommendations** supports the `AD` recommendation type, which returns information that sellers can use to set up Promoted Listings ad campaigns. Here's the structure of the returned `AD` type:

```json
  "ad": {
    "promoteWithAd": "[RECOMMENDED, UNDETERMINED]",
    "bidPercentage": [
      {
        "value": "string",
        "basis": "Basis : TRENDING"
      }
    ]
  }
```

With the above returned information, sellers can judge whether or not to place a listing in an ad campaign. In addition, the **bidPercentage** value offers guidance on the bid percentage (also known as the *ad rate*) that they should set for the campaign.

## Business use cases

The Recommendation API returns information related to a seller's active items; it supports the following use cases:

* Retrieve all of a seller's listings that could be improved with Promoted Listings
* Retrieve Promoted Listings information for a supplied set of listing IDs
* Get the current trending bid percentage

### Find items whose visibility could be escalated with a Promoted Listings ad campaign

If you're a seller who wants to know which of your items would benefit the most from including them in a Promoted Listings ad campaign, use the Recommendation API to return the subset of the seller's listings whose visibility on the eBay marketplace would be benefit the most by placing them in an ad campaign.

While promoting any item will help its visibility, some items are prime for ad campaigns. Listings that are "recommended" for Promoted Listings are those with the highest potential benefit from being promoted. The recommendations are based on marketplace trends, such as buyer demand and the competition in the item’s category.

### Retrieve ad recommendations for a supplied set of listing IDs

If desired, you can call **findListingRecommendation** with a specific set of listing IDs for which you want Promoted Listings information. You can request information for up to 500 individual listing IDs per request, where the IDs identify listings the seller currently has in the **Active** state.

When requesting information on specific listing IDs, the response includes information on all the supplied listing IDs, regardless of which ones eBay recommends they be placed in a Promoted Listings campaign.

### Establish your bid percentage based on the trending rate

The `AD` response for each listing ID includes information on the *trending bid percentage*, a value that indicates the average ad rate for similar promoted items at the sub category level.

With some exceptions, the **bidPercentage** value is returned with every listing ID returned in the response, regardless of how you structure your request.

## Recommendations API requirements and restrictions

The Recommendation API is currently supported in the Australian (**EBAY\_AU**), German (**EBAY\_DE**), Great Britain (**EBAY\_GB**), and United States (**EBAY\_US**) eBay marketplaces.

Related topics

* [Selling Apps](/api-docs/sell/static/sell-landing.html)
* [API Documentation](#)

  [Account v1 API](/api-docs/sell/account/overview.html)[Account v2 API](/api-docs/sell/account/v2/overview.html)[Inventory API](/api-docs/sell/inventory/overview.html)[Fulfillment API](/api-docs/sell/fulfillment/overview.html)[Finances API](/api-docs/sell/finances/overview.html)[Marketing API](/api-docs/sell/marketing/overview.html)[Negotiation API](/api-docs/sell/negotiation/overview.html)[Recommendation API](/api-docs/sell/recommendation/overview.html)[Analytics API](/api-docs/sell/analytics/overview.html)[Metadata API](/api-docs/sell/metadata/overview.html)[Compliance API](/api-docs/sell/compliance/overview.html)[Logistics API](/api-docs/sell/logistics/overview.html)[Feed API](/api-docs/sell/feed/overview.html)[Stores API](/api-docs/sell/stores/overview.html)
* [Guides](/develop/guides)
* [Related Docs](#)

  [Using eBay RESTful APIs](/api-docs/static/ebay-rest-landing.html)[Commerce APIs](/develop/apis/restful-apis/commerce-apis)[Developer APIs](/develop/apis/restful-apis/developer-apis)[Trading API](/devzone/xml/docs/reference/ebay/index.html)[Post-Order API](/Devzone/post-order/index.html)[Finding API](/devzone/finding/callref/index.html)[Platform Notifications](/api-docs/static/platform-notifications-landing.html)