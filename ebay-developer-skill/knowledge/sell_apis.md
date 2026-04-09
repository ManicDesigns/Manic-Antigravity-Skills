# APIs

Source: https://developer.ebay.com/develop/api/sell/identity_api

## Search Documentation

* sell
* buy

Guides

Release Notes

Request Headers

Response Status and Error Codes

Listing Management

[Inventory Mapping](#api-inventory_mapping)

**Mutations**

* startListingPreviewsCreation

**Queries**

* listingPreviewsCreationTaskById

Listing Metadata

[Charity API](#api-charity_api)

**charity\_org**

* getCharityOrg
* getCharityOrgs

[Catalog](#api-catalog)

**product**

* getProduct

**search**

* search

Offers and Leads

[Negotiation](#api-negotiation)

**offer**

* findEligibleItems
* sendOfferToInterestedBuyers

Other APIs

[Identity API](#api-identity_api)

**get**

* getUser

### Inventory Mapping

Copy Markdown [View as Markdown](/develop/api/sell/inventory_mapping.md)

The **Inventory Mapping API** helps sellers create high-quality listings with AI-powered recommendations generated from their existing product data. This API allows sellers and third-party partners to use existing product data to create eBay listing previews, which are then used to create listings through eBay's Listing APIs.

  

Specifically, the API accepts various input types, including item photos, titles, aspects, and product identifiers, and provides users with an AI-powered listing preview that includes recommendations for category, eBay-normalized item aspects, and description.

  

This API exposes the data through GraphQL queries and mutations. This allows you to use only those fields needed or available, and provides a process that creates eBay Listing Previews based on the seller's external product information.

#### How to get started

Try out the **Inventory Mapping API** using the [GraphQL Explorer](/my/graphql_explorer?index=0).

1. Sign in to your developer account and use this explorer to run test calls to this API in the Production environment (Sandbox is not supported).
2. Include the **mappingReferenceID** field for all listings generated or revised with **Inventory Mapping API** recommendations to quickly diagnose and resolve issues.
3. Share your feedback on recommendations and use cases to help us improve the product.

\* If you need expanded access to support your use cases, you can Apply for an [Application Growth Check](/grow/application-growth-check) to scale your integration.

  

**NOTE:** The **Inventory Mapping API** can be integrated with the **Notification API** to inform sellers when any of their listing preview creation tasks have completed through the LISTING\_PREVIEW\_CREATION\_TASK\_STATUS topic ID. If you are not familiar with the **Notification API**, see the [Notification API Overview](/api-docs/sell/notification/overview.html).

  

**NOTE:** The **Inventory Mapping API** is currently available only for the U.S. marketplace, and results should only be used solely for listings on the U.S. site. Set the marketplace by including the **X-EBAY-C-MARKETPLACE-ID** header with the value `EBAY_US`.

* **eBay Motors** (motor vehicles) and subordinate categories including **Parts & Accessories** are not presently supported.
* We'll notify you as soon as coverage expands to additional marketplaces.

GraphQL

API Spec Release Notes

###### Endpoints

* MutationstartListingPreviewsCreation
* QuerylistingPreviewsCreationTaskById

### Charity API

Copy Markdown [View as Markdown](/develop/api/sell/charity_api.md)

The eBay **Charity API** provides buyers and sellers a formal way to search for supported charitable organizations and charitable organization details.

**Note:** The **Charity API** is supported only in the UK and US marketplaces.

For more information about using RESTful APIs, see [Get started with eBay APIs](/develop/guides-v2/get-started-with-ebay-apis/get-started-with-ebay-apis#overview) and [Using eBay RESTful APIs](/develop/guides-v2/using-ebay-restful-apis/using-ebay-restful-apis#overview).

#### Sandbox vs. Production data

The data in the eBay Sandbox environment is static. It can be limited in scope and quantity, and is sometimes simulated or mock data. As a result, you should not depend on data in the Production environment to have the same limitations. Use good coding practices to anticipate the wider range and variability of data that your application is likely to encounter.

REST

API Spec Release Notes

###### Endpoints

* GET/charity\_org
* GET/charity\_org

### Catalog

Copy Markdown [View as Markdown](/develop/api/sell/catalog.md)

The **Catalog API** allows users to search for and locate an eBay catalog product that is a direct match for the product that they wish to sell. Listing against an eBay catalog product helps insure that all listings (based off of that catalog product) have complete and accurate information. In addition to helping to create high-quality listings, another benefit to the seller of using catalog information to create listings is that much of the details of the listing will be prefilled, including the listing title, the listing description, the item specifics, and a stock image for the product (if available). Sellers will not have to enter item specifics themselves, and the overall listing process is a lot faster and easier.

REST

API Spec Release Notes

###### Endpoints

* GET/product/{epid}
* GET/product\_summary/search

### Negotiation

Copy Markdown [View as Markdown](/develop/api/sell/negotiation.md)

The **Negotiation API** gives sellers the ability to proactively send discount offers to buyers who have shown an "interest" in their listings.   
  
By sending buyers discount offers on listings where they have shown an interest, sellers can increase the velocity of their sales.   
  
There are various ways for a buyer to show *interest* in a listing. For example, if a buyer adds the listing to their **Watch** list, or if they add the listing to their shopping cart and later abandon the cart, they are deemed to have shown an interest in the listing.   
  
In the offers that sellers send, they can discount their listings by either a percentage off the listing price, or they can set a new discounted price that is lower than the original listing price.   
  
For details about how seller offers work, see [Sending offers to buyers](https://developer.ebay.com/api-docs/sell/static/marketing/offers-to-buyers.html "\\"Selling").

REST

API Spec Release Notes

###### Endpoints

* GET/find\_eligible\_items
* POST/send\_offer\_to\_interested\_buyers

### Identity API

Copy Markdown [View as Markdown](/develop/api/sell/identity_api.md)

The **Identity API** returns data for an authenticated user (user access token) based on the OAuth scopes provided. Non-confidential information, such as eBay `userID` is returned using the default scope. Confidential data for an individual, such as address, email, phone, etc. are returned based on the OAuth scope you use in the call. For business users, all the public business information is returned using the default OAuth scope.

The Identity API can be used to let users log into your app or site using eBay, which frees you from needing to store and protect user's PII (Personal Identifiable Information) data.

REST

API Spec Release Notes

###### Endpoints

* GET/user

[FAQs](/support/faq)[Developer Community Forum](https://community.ebay.com/t5/Developer-Groups/ct-p/developergroup)[Developer Technical Support](/my/support/tickets)[APIs](/develop/apis)[API License Agreement](/join/api-license-agreement)

Copyright 1999—2026 eBay Inc. All rights reserved. [User agreement](http://pages.ebay.com/help/policies/user-agreement.html?rt=nc "opens in new window or tab"), [Privacy policy](http://pages.ebay.com/help/policies/privacy-policy.html?rt=nc "opens in new window or tab"), [Cookies](http://pages.ebay.com/help/account/cookies-web-beacons.html "opens in new window or tab").