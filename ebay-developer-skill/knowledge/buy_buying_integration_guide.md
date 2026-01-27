# Buying Integration Guide

Source: https://developer.ebay.com/api-docs/buy/static/buying-ig-landing.html

# Buying Integration Guide

 

* [Home](/)
* [Develop](/develop)
* [Guides](/develop/guides)
* Buying Integration Guide

Buying Integration Guide 

[Buy APIs Overview](buy-overview.html)

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

The eBay Buy APIs ([Browse](/api-docs/buy/browse/resources/methods),
[Deal](/api-docs/buy/deal/resources/methods), [Feed](/api-docs/buy/feed/resources/methods),
[Marketing](/api-docs/buy/marketing/resources/methods), [Offer](/api-docs/buy/offer/resources/methods), [Order for eBay member](/api-docs/buy/order_v1/resources/methods), and [Order for guest](/api-docs/buy/order/resources/methods))
are RESTful APIs that use [OAuth authentication](/api-docs/static/oauth-tokens.html), JSON payloads,
and [eBay HTTP headers](/api-docs/static/rest-request-components.html#headers). They provide the capabilities you need to create an eBay
shopping and buying experience in your app or website. You can use the eBay Buy APIs to:

* Surface eBay items by searching or using feed files (Browse and Feed API)
* Add marketing information for these items to promote conversion and up-sell and cross-sell (Marketing API)
* Search for eBay deals and events and retrieve deal and event items (Deal API)
* Change the contents and quantity of an item in an eBay member's cart (Browse API)
* Place proxy bids on auction items for buyers (Offer API)
* Let buyers purchase items on your app or site (without the Partner being PCI compliant (Order API)
* Let buyers view the details of their purchase orders and track the delivery of the order (Order API)
* Update your inventory with priority tracking payload information (Feed API)

Buyers can be eBay guests (buyer is anonymous) or eBay members (buyer is signed into eBay).

![Buy API Flows](/api-docs/res/Resources/images/buy-ig/buy-flow.svg)

**Important!** The
eBay Buy APIs are available as a public beta release. Accordingly, there may be some limitations and conditions on their use.
For more information, refer to [API launch stages](/api-docs/static/versioning.html#stages) in the Using eBay RESTful APIs
Guide and the [Buy APIs Requirements](/api-docs/buy/static/buy-requirements.html) in the Buying Integration Guide.

Related topics

* [Buying Apps](/api-docs/buy/static/buy-landing.html)
* [API Documentation](#)

  [Browse API](/api-docs/buy/browse/overview.html)[Deal API](/api-docs/buy/deal/overview.html)[Feed Beta API](/api-docs/buy/feed/overview.html)[Feed API](/api-docs/buy/feed/v1/overview.html)[Marketing API](/api-docs/buy/marketing/overview.html)[Offer API](/api-docs/buy/offer/overview.html)[Order API](/api-docs/buy/order/overview.html)
* [Guides](/develop/guides)
* [Related Docs](#)

  [Using eBay RESTful APIs](/api-docs/static/ebay-rest-landing.html)[Commerce APIs](/develop/apis/restful-apis/commerce-apis)[Developer APIs](/develop/apis/restful-apis/developer-apis)[Finding API](/devzone/finding/callref/index.html)[Shopping API](/devzone/shopping/docs/callref/index.html)