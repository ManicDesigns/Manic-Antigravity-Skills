# The authorization code grant flow | eBay Developers Program

Source: https://developer.ebay.com

# The authorization code grant flow

 

* [Home](/)
* [Develop](/develop)
* [Guides](/develop/guides)
* [Authorization Guide](/develop/guides/authorization_guide_landing.html)
* The authorization code grant flow

Authorization Guide 

[Using OAuth to access eBay APIs](oauth-scopes.html)

Get OAuth access tokens 

[The client credentials grant flow](oauth-client-credentials-grant.html)

The authorization code grant flow 

[Getting User Consent](oauth-consent-request.html)

[Exchanging the authorization code for a User access token](oauth-auth-code-grant-request.html)

[Using a refresh token to update a User access token](oauth-refresh-token-request.html)

[Getting your redirect\_uri value](oauth-redirect-uri.html)

[Generating your Base64-encoded credentials](oauth-base64-credentials.html)

[Getting access tokens through the Developer Portal](oauth-ui-tokens.html)

[OAuth best practices](oauth-best-practices.html)

[Access token rate limits](oauth-rate-limits.html)

[Understand Auth'n'Auth tokens](understand_auth_n_auth_tokens.html)

[Get Auth'n'Auth tokens](get_auth_n_auth_tokens.html)

[Using OAuth with traditional APIs](oauth-trad-apis.html)

The authorization code grant flow is used to create an OAuth User access token.

**OAuth client libraries**

The processes in this topic describe how to manually get OAuth tokens. To help with this process, eBay offers several client libraries that you can use to quickly implement the minting of OAuth tokens in your applications:

* [OAuth client library for Android](https://github.com/eBay/ebay-oauth-android-client "https://github.com/eBay/ebay-oauth-android")
* [OAuth client library for C#](https://github.com/eBay/ebay-oauth-csharp-client "https://github.com/eBay/ebay-oauth-csharp-client")
* [OAuth client library for Java](https://github.com/eBay/ebay-oauth-java-client "https://github.com/eBay/ebay-oauth-java-client")
* [OAuth client library for Node.js](https://github.com/eBay/ebay-oauth-nodejs-client "https://github.com/eBay/ebay-oauth-nodejs-client")
* [OAuth client library for Python](https://github.com/eBay/ebay-oauth-python-client "(https://github.com/eBay/ebay-oauth-python-client")

## Sequence for getting and using a User access token

The following sequence diagram outlines the authorization code grant flow, where a User access token is minted, then used in an API request:

![Authorization token process flow](/api-docs/res/resources/images/ebay-rest/authorization_code_650x486.png)
  
 *Sequence diagram for generating a User access token*

Getting a new access token for a user through the authorization code grant flow is a two-step process. First get consent from the eBay user to make API calls on their behalf (see [Getting user consent](oauth-consent-request.html)), and then generate the User access token for each user (see [Exchanging the authorization code for a User access token](oauth-auth-code-grant-request.html)).

Related topics

* [Start Here](/api-docs/static/ebay-rest-landing.html)
* [API Documentation](#)

  buy[Feed API](/api-docs/buy/feed/overview.html)[Browse API](/api-docs/buy/browse/overview.html)[Marketing API](/api-docs/buy/marketing/overview.html)[Offer API](/api-docs/buy/offer/overview.html)[Order API](/api-docs/buy/order/overview.html)[Marketplace Insights API](/api-docs/buy/marketplace-insights/overview.html)sell[Account API](/api-docs/sell/account/overview.html)[Inventory API](/api-docs/sell/inventory/overview.html)[Fulfillment API](/api-docs/sell/fulfillment/overview.html)[Finances API](/api-docs/sell/finances/overview.html)[Marketing API](/api-docs/sell/marketing/overview.html)[Negotiation API](/api-docs/sell/negotiation/overview.html)[Recommendation API](/api-docs/sell/recommendation/overview.html)[Analytics API](/api-docs/sell/analytics/overview.html)[Metadata API](/api-docs/sell/metadata/overview.html)[Compliance API](/api-docs/sell/compliance/overview.html)[Logistics API](/api-docs/sell/logistics/overview.html)[Listing API](/api-docs/sell/listing/overview.html)[Feed API](/api-docs/sell/feed/overview.html)commerce[Catalog API](/api-docs/commerce/catalog/overview.html)[Identity API](/api-docs/commerce/identity/overview.html)[Taxonomy API](/api-docs/commerce/taxonomy/overview.html)[Translation API Beta](/api-docs/commerce/translation/overview.html)[Translation API Expermental](/api-docs/commerce/translation-exp/overview.html)developer[Analytics API](/api-docs/developer/analytics/overview.html)
* [Integration Guides](#)

  [Buying Integration Guide](/api-docs/buy/static/buying-ig-landing.html)[Selling Integration Guide](/api-docs/sell/static/selling-ig-landing.html)
* [Related Docs](#)

  [Sell API](/api-docs/sell/static/sell-landing.html)[Buy API](/api-docs/buy/static/buy-landing.html)[Commerce APIs](/api-docs/commerce/static/commerce-landing.html)[Developer APIs](/api-docs/developer/static/developer-landing.html)