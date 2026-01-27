# Offer API

Source: https://developer.ebay.com/api-docs/buy/static/api-offer.html

# Offer API

 

* [Home](/)
* [Develop](/develop)
* [Guides](/develop/guides)
* [Buying Integration Guide](/develop/guides/buying-ig-landing.html)
* Offer API

Buying Integration Guide 

[Buy APIs Overview](buy-overview.html)

[Buy APIs Requirements](buy-requirements.html)

[Browse API](api-browse.html)

[Charity API](api-charity.html)

[Deal API](api-deal.html)

[Feed API](api-feed.html)

[Feed API beta](api-feed_beta.html)

[Marketing API](api-marketing.html)

[Offer API](#)

[Order API](api-order.html)

[Categories for Buy APIs](buy-categories.html)

[Buy API Support by Marketplace](ref-marketplace-supported.html)

[Buy API Field Filters](ref-buy-browse-filters.html)

**Note:** 
This is a [![Limited Icon](/cms/img/docs/partners-api.svg "Limited Release") (Limited Release)](/api-docs/static/versioning.html#Limited). For information on how to obtain access to this API in production, see the [Buy APIs Requirements](buy-requirements.html).

You use the Offer API to place bids for buyers and return the buyer's bidding details of auctions where they have placed bids.

1. **Find an auction**

   Use the [Browse API](/api-docs/buy/browse/resources/methods) **search** method to find an auction item the buyer wants to bid on.

   ![Find an Auction](/api-docs/res/Resources/images/buy-ig/offer_flow_1.jpg)

   For example, the following searches by keyword and returns iPhone auctions.

   ```json
   /buy/browse/v1/item_summary/search?q=iphone&filter=buyingOptions:{AUCTION}
   ```
2. **Place a bid for the buyer**

   Use the Offer API **placeProxyBid** method to place a bid of the maximum amount the buyer is willing to pay for the item.

   ```json
   /buy/offer/v1_beta/bidding/{item_id}/place_proxy_bid  
   {  
     "maxAmount": {  
       "currency": "USD",  
       "value": "800.00  
     }  
   }
   ```
3. **Retrieve buyer's bidding details**

   Use the Offer API **getAuction** method to retrieve the bidding details specific to the buyer.

   ![Retrieve Bidding Details](/api-docs/res/Resources/images/buy-ig/offer_flow_2.jpg)

   ```json
   /buy/offer/v1_beta/bidding/{item_id}
   ```

   **Determine if the buyer has won the auction.**

   You can check if the buyer has won the auction using the response from this call. If the value of **auctionStatus** is `ENDED` and the value of **highBidder** is `true`, this indicates the buyer has won the auction.
4. **Get general bidding details**

   Use the [Browse API](/api-docs/buy/browse/resources/methods) **getItem** method to retrieve general bidding details about the auction, such as minimum bid price and the count of unique bidders.

   ![General Bidding Details](/api-docs/res/Resources/images/buy-ig/offer_flow_3.jpg)

   ```json
   /buy/browse/v1/item/{item_id}
   ```

Related topics

* [Buying Apps](/api-docs/buy/static/buy-landing.html)
* [API Documentation](#)

  [Browse API](/api-docs/buy/browse/overview.html)[Deal API](/api-docs/buy/deal/overview.html)[Feed Beta API](/api-docs/buy/feed/overview.html)[Feed API](/api-docs/buy/feed/v1/overview.html)[Marketing API](/api-docs/buy/marketing/overview.html)[Offer API](/api-docs/buy/offer/overview.html)[Order API](/api-docs/buy/order/overview.html)
* [Guides](/develop/guides)
* [Related Docs](#)

  [Using eBay RESTful APIs](/api-docs/static/ebay-rest-landing.html)[Commerce APIs](/develop/apis/restful-apis/commerce-apis)[Developer APIs](/develop/apis/restful-apis/developer-apis)[Finding API](/devzone/finding/callref/index.html)[Shopping API](/devzone/shopping/docs/callref/index.html)