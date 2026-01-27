# Marketing API

Source: https://developer.ebay.com/api-docs/buy/static/api-marketing.html

# Marketing API

 

* [Home](/)
* [Develop](/develop)
* [Guides](/develop/guides)
* [Buying Integration Guide](/develop/guides/buying-ig-landing.html)
* Marketing API

Buying Integration Guide 

[Buy APIs Overview](buy-overview.html)

[Buy APIs Requirements](buy-requirements.html)

[Browse API](api-browse.html)

[Charity API](api-charity.html)

[Deal API](api-deal.html)

[Feed API](api-feed.html)

[Feed API beta](api-feed_beta.html)

[Marketing API](#)

[Offer API](api-offer.html)

[Order API](api-order.html)

[Categories for Buy APIs](buy-categories.html)

[Buy API Support by Marketplace](ref-marketplace-supported.html)

[Buy API Field Filters](ref-buy-browse-filters.html)

The Marketing API has the [merchandised\_product](/api-docs/buy/marketing/resources/methods) resource, which provides the ability to show eBay products based on a metric, such as Best Selling. It provides information such as, the eBay product ID (EPID), review ratings by condition, price, etc. This helps to inspire shoppers and to discover products. It motivates them to purchase items and can give them a feeling of confidence. It also encourages up-selling and cross-selling.

You can use this API do the following:

* You can create a landing page that shows the [best selling items](#best-selling-page) to your buyers based on their search.
* You can show [product reviews](#product-review) to encourage conversion.
* You can surface popular items specific for your buyer based on their buying history or buying behavior. For example, if you know that a specific customer purchases Canon camera equipment, you could surface popular Canon camera items when your buyer signs in.

## Create a best selling products page

You can motivate customers to buy by showing them the best selling products, which creates awareness about different products/items, to help buyers compare and research products/items.
You can use the **getMerchandisedProducts**  method to create a best selling items page based on category.

For example: `/merchandised_product?category_id=31388&metric_name=BEST_SELLING`.

The following uses the information returned in
the **title**, **image**, and **averageRating** fields.

![Bestselling Items](/api-docs/res/Resources/images/buy-ig/mkt-epid31388-bestselling.png)

## Show product reviews ratings

Showing reviews helps shoppers select an item and purchase with confidence. You can use the **ratingAspects** information from the **getMerchandisedProducts**  method to show the overall rating and aspect ratings.

![Item overall rating](/api-docs/res/Resources/images/buy-ig/mkt-epid31388-rating.png)       ![Item review rating by aspect](/api-docs/res/Resources/images/buy-ig/mkt-epid31388-rating-pie.png)

## Show 'also viewed' and 'also bought' products

The **getAlsoViewedByProduct** and **getAlsoBoughtByProduct** methods are no longer available in the **Marketing API**.

Related topics

* [Buying Apps](/api-docs/buy/static/buy-landing.html)
* [API Documentation](#)

  [Browse API](/api-docs/buy/browse/overview.html)[Deal API](/api-docs/buy/deal/overview.html)[Feed Beta API](/api-docs/buy/feed/overview.html)[Feed API](/api-docs/buy/feed/v1/overview.html)[Marketing API](/api-docs/buy/marketing/overview.html)[Offer API](/api-docs/buy/offer/overview.html)[Order API](/api-docs/buy/order/overview.html)
* [Guides](/develop/guides)
* [Related Docs](#)

  [Using eBay RESTful APIs](/api-docs/static/ebay-rest-landing.html)[Commerce APIs](/develop/apis/restful-apis/commerce-apis)[Developer APIs](/develop/apis/restful-apis/developer-apis)[Finding API](/devzone/finding/callref/index.html)[Shopping API](/devzone/shopping/docs/callref/index.html)