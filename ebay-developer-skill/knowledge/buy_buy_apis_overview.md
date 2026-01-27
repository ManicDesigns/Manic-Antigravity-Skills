# Buy APIs Overview

Source: https://developer.ebay.com/api-docs/buy/static/buy-overview.html

# Buy APIs Overview

 

* [Home](/)
* [Develop](/develop)
* [Guides](/develop/guides)
* [Buying Integration Guide](/develop/guides/buying-ig-landing.html)
* Buy APIs Overview

Buying Integration Guide 

[Buy APIs Overview](#)

[Buy APIs Requirements](buy-requirements.html)

[Browse API](api-browse.html)

[Charity API](api-charity.html)

[Deal API](api-deal.html)

[Feed API](api-feed.html)

[Feed API beta](api-feed_beta.html)

[Marketing API](api-marketing.html)

[Offer API](api-offer.html)

[Order API](api-order.html)

[Categories for Buy APIs](buy-categories.html)

[Buy API Support by Marketplace](ref-marketplace-supported.html)

[Buy API Field Filters](ref-buy-browse-filters.html)

The Buy APIs work together to enable eBay partners to sell eBay items from the Partner's app or website. This document contains an overview of each Buy API.

Many of the Buy APIs are a  [![Limited Release](/cms/img/docs/partners-api.svg "Limited Release")Limited](/api-docs/static/versioning.html#Limited) release available only to select developers approved by business units. For information on how to obtain access to these APIs in production, see the [Buy APIs Requirements](buy-requirements.html).

The following lists the Buy APIs:

* [Browse API](api-browse.html#top)
  + Lets shoppers search for specific items by keyword, GTIN, category, charity, product, or item aspects and refine the results by using filters.
  + Lets you retrieve the details of a specific item or all the items in an item group, which is an item with variations such as color and size and check if a product is compatible with the specified item, such as if a specific car is compatible with a specific part.
  + Provides a bridge between the eBay legacy APIs, such as Finding, and the RESTful APIs, such as Browse, which use
    different formats for the item IDs enabling you to retrieve the details of the item and the RESTful item ID using a legacy item ID.
  + Lets you search for compatible items and check the compatibility of a specific item.
  + Lets shoppers search for specific items by image. You can refine the results by using URI parameters and filters.
* [![Limited Release](/cms/img/docs/partners-api.svg "Limited Release")(Limited Release)](/api-docs/static/versioning.html#Limited) [Deal API](api-deal.html) – Searches for and retrieves details about eBay deals and events, as well as the items associated with those deals and events.
* [![Limited Release](/cms/img/docs/partners-api.svg "Limited Release")(Limited Release)](/api-docs/static/versioning.html#Limited) [Feed API beta](api-feed_beta.html) - Lets you download:
  + A daily **Item** feed file of the newly listed eBay items for a specific category, date, and marketplace.
  + A weekly **Item Bootstrap** feed file of all the eBay items in a specific category and marketplace.
  + Item group (item variation information) feed files for the items returned in the **Item** and **Item Bootstrap** feed files.
  + An hourly **Snapshot** feed file of the latest information for items that have changed within that hour for a specific category, date, and marketplace.
  + A daily **Item Priority** feed of the changes in status of priority items in a specified campaign.After you have the items, you can curate them specifically for your app or website and then add them to a database.
* [Marketing API](api-marketing.html#top) – Returns products, which lets shoppers discover new products and assists shoppers with deciding which product to purchase.
* [![Limited Release](/cms/img/docs/partners-api.svg "Limited Release")(Limited Release)](/api-docs/static/versioning.html#Limited) [Offer API](api-offer.html#top) – Lets Partners place bids on behalf of a buyer on auction items and retrieve the bidding details for an auction where the buyer has placed a bid.
* [![Limited Release](/cms/img/docs/partners-api.svg "Limited Release")(Limited Release)](/api-docs/static/versioning.html#Limited) [Order API](api-order.html#top) – Lets both eBay guests and eBay members pay for items and view their purchase order details. The payment flows for guest and member are different. For details, see [payment flows](/api-docs/buy/static/api-order.html#Payment). It also provides the ability to apply a coupon to the order and track the delivery of the order. For eBay member checkouts, you can use the [Post Order API](/Devzone/post-order/index.html#CallIndex) for returns and cancellations. See [Handling post order tasks](api-order.html#Post) for details.

The graphic below shows how the Buy APIs can be used together in a buying flow.

![Examples of screens built using the Buy APIs](/api-docs/res/Resources/images/buy-ig/buyoverview_1116x535.png)

##

Related topics

* [Buying Apps](/api-docs/buy/static/buy-landing.html)
* [API Documentation](#)

  [Browse API](/api-docs/buy/browse/overview.html)[Deal API](/api-docs/buy/deal/overview.html)[Feed Beta API](/api-docs/buy/feed/overview.html)[Feed API](/api-docs/buy/feed/v1/overview.html)[Marketing API](/api-docs/buy/marketing/overview.html)[Offer API](/api-docs/buy/offer/overview.html)[Order API](/api-docs/buy/order/overview.html)
* [Guides](/develop/guides)
* [Related Docs](#)

  [Using eBay RESTful APIs](/api-docs/static/ebay-rest-landing.html)[Commerce APIs](/develop/apis/restful-apis/commerce-apis)[Developer APIs](/develop/apis/restful-apis/developer-apis)[Finding API](/devzone/finding/callref/index.html)[Shopping API](/devzone/shopping/docs/callref/index.html)