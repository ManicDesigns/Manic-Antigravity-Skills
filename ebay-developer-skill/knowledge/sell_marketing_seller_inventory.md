# Marketing seller inventory

Source: https://developer.ebay.com/api-docs/sell/static/marketing/marketing-seller-inventory.html

# Marketing seller inventory

 

* [Home](/)
* [Develop](/develop)
* [Guides](/develop/guides)
* [Selling Integration Guide](/develop/guides/selling-ig-landing.html)
* Marketing seller inventory

Selling Integration Guide 

[How to develop a selling application](../dev-app.html)

[Configuring seller accounts](../seller-accounts/configuring-seller-accounts.html)

[Getting category information and other metadata](../metadata/getting-metadata.html)

[Managing inventory and offers](../inventory/managing-inventory-and-offers.html)

[Handling orders](../orders/handling-orders.html)

Marketing seller inventory 

[Promoted Listings playbook](pl-landing.html)

[Discounts Manager](promotions-manager.html)

[Offers to buyers](offers-to-buyers.html)

[Store Email Campaigns](store-email-campaigns.html)

[Analyzing seller performance](../performance/analyzing-performance.html)

[Using the Sell Feed API](../feed/sell-feed.html)

[Using the Finances API](../finances/finances-landing.html)

The eBay provides two APIs to help sellers market their inventory:

* [Negotiation API](/api-docs/sell/negotiation/resources/methods "Negotiation API Reference") – Sellers can reach out to buyers who have shown an interest in their listings and offer them a discount on the listing price.
* [Marketing API](/api-docs/sell/marketing/resources/methods "Marketing API Reference") – Sellers can promote select listings in their inventory, and offer discounted prices on existing listings.

## The Negotiation API

The **Negotiation API** lets sellers discover which of their listings have "interested" buyers (listings that buyers have either added to their Watch list or their shopping cart).

Buyers who have shown an interest in a listing are eligible to receive a "seller-initiated offer" on that listing, meaning sellers can reach out to the them with an offer that reduces the price of the listing.

## The Marketing API

The **Marketing API** lets sellers attract buyers to their inventory by highlighting their items with **Promoted Listings** ad campaigns and discount promotions created with **Discounts Manager**. This API also allows sellers to create and send email campaigns with **Store Email Campaigns**.

These marketing tools let big brands replicate the deals they offer on their websites and in brick-and-mortar stores, and they give smaller eBay sellers tools that can help them scale their sales.

**Important!** The Marketing API is available to any seller who has an eBay Store subscription.

These marketing tools, however, do have some listing requirements and site restrictions. For details, see:

* [Promoted Listings requirements and restrictions](/api-docs/sell/marketing/static/overview.html#PL-requirements)
* [Discounts Manager requirements and restrictions](/api-docs/sell/marketing/static/overview.html#PM-requirements)

### Promoted Listings

*Promoted Listings*  is an advertising service that improves the visibility of a seller's listings by promoting selected listings across the eBay buyer flows.

Sellers create Promoted Listings *campaigns*  and include sets of listings in the campaigns by creating "ads" for the listings they want to promote.

A **SPONSORED** badge is displayed on listings that are in ad campaigns and eBay surfaces ads in prominent locations, such as in Search Result pages and other eBay buyer flows (such as in the *Sponsored* section of an eBay search results page).

**Tip:** For details on ad campaigns, including how to create and manage them, see [Promoted Listings Playbook](pl-landing.html).

### Discounts Manager

*Discounts Manager*  is a discount engine that sellers use to attract buyers with offers like **Buy 1 Get 1 Free** and **Buy $50, get 15% off**.

Discount *teasers* are displayed on discounted listings, and eBay surfaces these in prominent locations in the eBay buyer flows (such as on Search Results pages, View Item pages, and in cart and checkout flows). The teasers and special messaging creates interest in discounted items and entices shoppers to further explore the items in a seller's inventory.

To help you create sales events, eBay creates web pages with *static links* for each of your discounted items, which gives you an unchanging way to link to your discounts from mailers and other marketing collateral.

And perhaps the best part is that eBay offers all item discount features for *free*, there is no fee associated with any of the discounts you run via Discounts Manager.

**Tip:** For information on the available types of discounts, including how to create and manage them, see [Discounts Manager](promotions-manager.html).

### Marketing reports

The Marketing API provides interfaces to create and retrieve reports that detail a seller's Promoted Listings campaign performance and their Discount Manager sales. The reports offer insights into a seller's marketing efforts and gives them the tools needed to evaluate and fine tune their marketing strategies.

See the following topics for more the Marketing API reporting capabilities:

* [Promoted Listings reports](pl-reports.html)
* [Discount Manager reports](pm-summary-report.html)

### Store Email Campaigns

*Store Email Campaigns*  allows users to create and send email campaigns to customers who have signed up to receive newsletters from a seller's store.

Email campaign *types* are available to sellers. Each of these types have different proposes, such as welcoming a customer, highlighting new products, distributing coupons, and more.

To help get your email campaign reach the most relevant groups, the *audience* can be set, giving you the ability to choose who receives a newsletter.

You can also retrieve *reports* for your email campaigns, showing you information about the report, such as its click count and the amount earned it earned in sales.

**Tip:** For information on email campaigns, including how to create and send them, see [Store Email Campaigns](store-email-campaigns.html).

Related topics

* [Selling Apps](/api-docs/sell/static/sell-landing.html)
* [API Documentation](#)

  [Account v1 API](/api-docs/sell/account/overview.html)[Account v2 API](/api-docs/sell/account/v2/overview.html)[Inventory API](/api-docs/sell/inventory/overview.html)[Fulfillment API](/api-docs/sell/fulfillment/overview.html)[Finances API](/api-docs/sell/finances/overview.html)[Marketing API](/api-docs/sell/marketing/overview.html)[Negotiation API](/api-docs/sell/negotiation/overview.html)[Recommendation API](/api-docs/sell/recommendation/overview.html)[Analytics API](/api-docs/sell/analytics/overview.html)[Metadata API](/api-docs/sell/metadata/overview.html)[Compliance API](/api-docs/sell/compliance/overview.html)[Logistics API](/api-docs/sell/logistics/overview.html)[Feed API](/api-docs/sell/feed/overview.html)[Stores API](/api-docs/sell/stores/overview.html)
* [Guides](/develop/guides)
* [Related Docs](#)

  [Using eBay RESTful APIs](/api-docs/static/ebay-rest-landing.html)[Commerce APIs](/develop/apis/restful-apis/commerce-apis)[Developer APIs](/develop/apis/restful-apis/developer-apis)[Trading API](/devzone/xml/docs/reference/ebay/index.html)[Post-Order API](/Devzone/post-order/index.html)[Finding API](/devzone/finding/callref/index.html)[Platform Notifications](/api-docs/static/platform-notifications-landing.html)