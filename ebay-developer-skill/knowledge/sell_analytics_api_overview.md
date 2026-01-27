# Analytics API Overview

Source: https://developer.ebay.com/api-docs/sell/analytics/static/overview.html

# Analytics API Overview

1.3.2

 

* [Home](/)
* [Develop](/develop)
* [Selling Apps](/develop/selling-apps)
* [Analytics and Reporting](/develop/selling-apps/analytics-and-reporting)
* Analytics API Overview

[API overview](/api-docs/sell/analytics/overview.html)

API reference 

[Resources](/api-docs/sell/analytics/resources/methods)

customer\_service\_metric 

[getCustomerServiceMetric](/api-docs/sell/analytics/resources/customer_service_metric/methods/getCustomerServiceMetric)

seller\_standards\_profile 

[findSellerStandardsProfiles](/api-docs/sell/analytics/resources/seller_standards_profile/methods/findSellerStandardsProfiles)

[getSellerStandardsProfile](/api-docs/sell/analytics/resources/seller_standards_profile/methods/getSellerStandardsProfile)

traffic\_report 

[getTrafficReport](/api-docs/sell/analytics/resources/traffic_report/methods/getTrafficReport)

[Index](/api-docs/sell/analytics/fields)

[API release notes](/api-docs/sell/analytics/release-notes.html)

[OpenAPI 3 JSON Contract (beta)](/api-docs/master/sell/analytics/openapi/3/sell_analytics_v1_oas3.json)

[OpenAPI 3 YAML Contract (beta)](/api-docs/master/sell/analytics/openapi/3/sell_analytics_v1_oas3.yaml)

The **Analytics API** provides information about an individual seller’s business through different report and data gathering resources:

* Customer service metric ratings and benchmark data
* The Traffic Report
* The Seller Standard Profiles Report

Understanding the health and performance of your business is crucial to maintaining and planning your business growth.

The methods in the Analytics API return metric ratings and information that

* **Traffic reports** gives you insight in how buyers engage with your listings
* **Customer service metrics** detail how you are meeting buyers’ customer-service expectations
* **Seller profiles** detail the returns the eBay seller rating of a seller in the regions in which the seller is active.

The calls in the API support reporting changes over time, and depending on your trading history, you might have multiple years of available data to work with. You can look at different history configurations to see how seasonal changes affect your business, or use the tools do an other time-based analysis.

## Technical overview

The Analytics API provides one or more methods in each of the following resources:

* `customer_service_metric`
* `traffic_report`
* `seller_standards_profile`

The main objects in each resource are as follows:

* **Customer service metric**
  + *dimension* - Specifies the attributes and time constraints that group the set of transactions used for the metric and benchmark data, and metric rating that's returned in the associated **metric**.
  + *metric* - Returns a set of metric and benchmark data, and the seller's metric rating, based on the transactions that meet the attributes defined by the associated **dimension**.
* **Traffic Report**
  + *dimensionKeys* - the report's aggregation method, for example, days
  + *metrics* - the report's type of data, for example, total listing page views
  + *records* - the report's individual records, bucketed by **dimensionKeys**
* **Seller Standards Profile**
  + *program* - marketplace region where a seller conducts business
  + *cycle* - current or projected evaluation cycle

See the *Business use cases* section that follows for the details on how you can use these resources.

## Business use cases

The following are some of the high-level use cases for the Analytics API:

* [Retrieve a seller's customer service metric rating](#Retrieve)
* [Track buyer engagement with a seller's top listings](#Track)
* [Benchmark buyer behavior on your listings over the past 2 years](#Benchmark)
* [Understand the impact of change on buyer engagement](#Understand)
* [Correlate eBay standards performance to buyer engagement](#Correlate)
* [Monitor your eBay standards performance](#Monitor)

### Retrieve a seller's customer service metric rating

Use [getCustomerServiceRating](/api-docs/sell/analytics/resources/customer_service_metric/methods/getCustomerServiceMetric "API Reference") to retrieve *metric* data, which contains metric and benchmark data, and the customer service metric rating for a seller. The transactions considered for the data and rating are constrained by the attributes defined in the *dimension*.

### Track buyer engagement with a seller's top listings

Some listings may generate the majority of your sales, by volume or by profit. It's important to know if links to these listings are showing up on eBay as often as you expect, or if buyers are starting to view or purchase those items less often than previous periods.

### Benchmark buyer behavior on your listings over the past 2 years

You can compare buyer behavior on your listings over the past 2 years. This can help you understand when particular items are more likely to sell, or the information can let you know that interest in an item has declined steadily over time. For the latter, you might want to run a promotion to either try to revitalize sales or close out your inventory of the item.

### Understand the impact of change on buyer engagement

Changes to listings can impact buyer engagement. For example, you can check to see if a marketing campaign has successfully led to more item views and sale conversions.

### Correlate eBay standards performance to buyer engagement

You can correlate your eBay standards performance to engagement with your listings. For example, if you recently earned Top Rated Seller status, buyers may view and purchase your items more frequently due to the knowledge that you'll provide excellent customer service.

### Monitor your eBay standards performance

Sellers can monitor their sales performance and evaluate the customer-service areas they can focus on to maintain or improve their evaluation. For example, you can focus on standards criteria in which you are not performing in the Top Rated Seller level.

### Additional Information

More detailed reports on the various metrics can be found on the [Seller Standards Dashboard](https://sellerstandards.ebay.com/dashboard). You may want to add these US program links to your dashboard.

* [Transaction defect rate](http://www.sps.ebay.com/sd/reports/defect?programs=US&evalType=ESTIMATED_FUTURE)
* [Late shipment rate](http://www.sps.ebay.com/sd/reports/shipping?programs=US&evalType=ESTIMATED_FUTURE)
* [Tracking uploaded on time and validated](http://www.sps.ebay.com/sd/spreports#trackingReport?programs=US)

## Analytics API requirements and restrictions

Each resource, and its associated methods, are supported in distinct marketplaces, as outlined in the following sections.

### customer\_service\_metric

The **customer\_service\_metric** resource has a single method, [getCustomerServiceMetric](/api-docs/sell/analytics/resources/customer_service_metric/methods/getCustomerServiceMetric "API Ref"), which is supported by the following eBay marketplaces:

* **Australia** (`EBAY_AU`)
* **Canada** (`EBAY_CA`)
* **France** (`EBAY_FR`)
* **Germany** (`EBAY_DE`)
* **Great Britain** (`EBAY_GB`)
* **Italy** (`EBAY_IT`)
* **Spain** (`EBAY_ES`)
* **United States** (`EBAY_US`)

For more information, see the [Service metrics](https://www.ebay.com/help/policies/selling-policies/seller-performance-policy/service-metrics-policy?id=4769#section2 "eBay Help page") section of the *Service metrics policy* page.

### traffic\_report

The **traffic\_report** resource has a single method, [getTrafficReport](/api-docs/sell/analytics/resources/traffic_report/methods/getTrafficReport "API Ref"), which is supported by the following eBay marketplaces:

* **Australia** (`EBAY_AU`)
* **France** `(EBAY_FR)`
* **Germany** (`EBAY_DE`)
* **Great Britain** (`EBAY_GB`)
* **Italy** `(EBAY_IT)`
* **Spain** `(EBAY_ES)`
* **United States** (`EBAY_US`)

Use this method for up to a few thousand listings per day; it is not intended to return daily metrics for all your listings. We hope to increase this rate limit In the future.

### seller\_standard\_profile

The methods in the **seller\_standard\_profile** resource are supported by the same marketplaces that provide support for the **customer\_service\_metric** resource.

Be aware that some fields returned by the methods in the **seller\_standar\_profile** resource may be subject to change. This includes future possible updates to the structure of the **program**, **metrics**, **cycle**, and **threshold** response fields, so please code your applications to gracefully handle any such changes.

Related topics

* [Selling Apps](/api-docs/sell/static/sell-landing.html)
* [API Documentation](#)

  [Account v1 API](/api-docs/sell/account/overview.html)[Account v2 API](/api-docs/sell/account/v2/overview.html)[Inventory API](/api-docs/sell/inventory/overview.html)[Fulfillment API](/api-docs/sell/fulfillment/overview.html)[Finances API](/api-docs/sell/finances/overview.html)[Marketing API](/api-docs/sell/marketing/overview.html)[Negotiation API](/api-docs/sell/negotiation/overview.html)[Recommendation API](/api-docs/sell/recommendation/overview.html)[Analytics API](/api-docs/sell/analytics/overview.html)[Metadata API](/api-docs/sell/metadata/overview.html)[Compliance API](/api-docs/sell/compliance/overview.html)[Logistics API](/api-docs/sell/logistics/overview.html)[Feed API](/api-docs/sell/feed/overview.html)[Stores API](/api-docs/sell/stores/overview.html)
* [Guides](/develop/guides)
* [Related Docs](#)

  [Using eBay RESTful APIs](/api-docs/static/ebay-rest-landing.html)[Commerce APIs](/develop/apis/restful-apis/commerce-apis)[Developer APIs](/develop/apis/restful-apis/developer-apis)[Trading API](/devzone/xml/docs/reference/ebay/index.html)[Post-Order API](/Devzone/post-order/index.html)[Finding API](/devzone/finding/callref/index.html)[Platform Notifications](/api-docs/static/platform-notifications-landing.html)