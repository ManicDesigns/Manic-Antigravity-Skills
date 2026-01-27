# Configuring seller accounts

Source: https://developer.ebay.com/api-docs/sell/static/seller-accounts/configuring-seller-accounts.html

# Configuring seller accounts

 

* [Home](/)
* [Develop](/develop)
* [Guides](/develop/guides)
* [Selling Integration Guide](/develop/guides/selling-ig-landing.html)
* Configuring seller accounts

Selling Integration Guide 

[How to develop a selling application](../dev-app.html)

Configuring seller accounts 

[How to get account status and selling limits](ht_get-selling-limits.html)

[eBay business policies](business-policies.html)

[Configuring shipping options](configuring-shipping-options.html)

[Establishing tax tables](tax-tables.html)

[Getting category information and other metadata](../metadata/getting-metadata.html)

[Managing inventory and offers](../inventory/managing-inventory-and-offers.html)

[Handling orders](../orders/handling-orders.html)

[Marketing seller inventory](../marketing/marketing-seller-inventory.html)

[Analyzing seller performance](../performance/analyzing-performance.html)

[Using the Sell Feed API](../feed/sell-feed.html)

[Using the Finances API](../finances/finances-landing.html)

The base for all eBay merchants is their eBay seller account, and eBay offers various ways for sellers to configure and customize their eBay selling accounts.

Using the **Account API**, sellers can set up policies for how they conduct their business, configure sales tax tables for the ares in which they do business, and opt-in to various seller programs offered by eBay.

Also in the Account API, the **getPrivileges** call retrieves a merchant's selling limits, as well as the status of their business account.

## Seller policies

eBay has three policies that sellers should configure to easily and successfully conduct business on eBay:

* Payment policy
* Fulfillment policy
* Return policy

While sellers should set up one of each type of policy, they can set multiple policies for each type, distinguishing the policies by marketplace, type of categories addressed by the policy, and more. Sellers also denote a default policy so that they don't need to specify a policy for individual listings.

## Set sales-tax tables

Some regions have more than a single sales tax rate, and eBay gives sellers the ability to set up tax tables for individual sales tax *jurisdictions*.

**Note:**  Sales-tax tables are only available for the US (EBAY\_US) and Canada (EBAY\_CA) marketplaces.

  

**Important!**  In the US, eBay now calculates, collects, and remits sales tax to the proper taxing authorities in all 50 states and Washington, DC. Sellers can no longer specify sales-tax rates for these jurisdictions using a tax table.

However, sellers may continue to use a sales-tax table to set rates for the following US territories:

* American Samoa (AS)
* Guam (GU)
* Northern Mariana Islands (MP)
* Palau (PW)
* US Virgin Islands (VI)

For additional information, refer to [Taxes and import charges](https://www.ebay.com/help/selling/fees-credits-invoices/taxes-import-charges?id=4121).

## eBay seller programs

eBay currently offers three different seller programs, each of which sellers can opt-in to if they so desire:

* *Out of stock control* is a tool that allows sellers to monitor their inventory across a set of inventory locations.
* *Selling policy management* lets sellers identify which of their business policies they want to reference for an item listing. Sellers can reference any of their payment, fulfillment, or return policies in an item listing once they opt-in to this eBay seller program.
* *Partner Motors Program* enables registered business users to create motor vehicle listings. Note that this program is currently only supported in the UK marketplace, and sellers must complete the [eBay Motors Pro](https://www.ebaymotorspro.co.uk/emp/index.html) registrations flow in order to create motor vehicle listings.

Related topics

* [Selling Apps](/api-docs/sell/static/sell-landing.html)
* [API Documentation](#)

  [Account v1 API](/api-docs/sell/account/overview.html)[Account v2 API](/api-docs/sell/account/v2/overview.html)[Inventory API](/api-docs/sell/inventory/overview.html)[Fulfillment API](/api-docs/sell/fulfillment/overview.html)[Finances API](/api-docs/sell/finances/overview.html)[Marketing API](/api-docs/sell/marketing/overview.html)[Negotiation API](/api-docs/sell/negotiation/overview.html)[Recommendation API](/api-docs/sell/recommendation/overview.html)[Analytics API](/api-docs/sell/analytics/overview.html)[Metadata API](/api-docs/sell/metadata/overview.html)[Compliance API](/api-docs/sell/compliance/overview.html)[Logistics API](/api-docs/sell/logistics/overview.html)[Feed API](/api-docs/sell/feed/overview.html)[Stores API](/api-docs/sell/stores/overview.html)
* [Guides](/develop/guides)
* [Related Docs](#)

  [Using eBay RESTful APIs](/api-docs/static/ebay-rest-landing.html)[Commerce APIs](/develop/apis/restful-apis/commerce-apis)[Developer APIs](/develop/apis/restful-apis/developer-apis)[Trading API](/devzone/xml/docs/reference/ebay/index.html)[Post-Order API](/Devzone/post-order/index.html)[Finding API](/devzone/finding/callref/index.html)[Platform Notifications](/api-docs/static/platform-notifications-landing.html)