# Merchandising API Guide

Source: https://developer.ebay.com/Devzone/merchandising/docs/Concepts/merchandisingAPIGuide.html

# Merchandising API Users Guide

**Note:**  All calls in the **Merchandising API** have been deprecated as of July 29, 2024, and will be decommissioned on January 6, 2025.

The Merchandising API provides item and product recommendations that can be used to cross-sell and up-sell eBay items to buyers. This document gives an overview of the Merchandising API, explains what the API is for, describes how to use it, and points you to other resources where you can learn more. The Merchandising API can be used independently or it can be used together with other [eBay APIs](/develop/apis) to create rich applications.

* [Merchandising Service Overview](#intro)
* [Merchandising Use Cases](#work)
* [Working with the Merchandising API](#use)
* [Additional Resources](#resources)

## Merchandising Service Overview

The eBay Merchandising API retrieves valuable information about products or item listings on eBay to help you sell more merchandise to eBay buyers. Buying applications can provide suggested products or item listings based on buyers' searching or selection activity. Sellers can augment their own listings with cross-promotions to create a better shopping experience, which can help attract and retain buyers.

The Merchandising API consists of calls that return item or product recommendations based on simple inputs, such as a query, an item ID, or a category ID. The API returns the following types of merchandise recommendations:

* Most watched itemsâitems that are currently the most watched
* Related category itemsâitems from categories that are related to a specific item or category

Refer to the eBay Merchandising API [API Reference](../CallRef/index.html) for a list of API calls and the associated inputs and outputs for each.

|  |
| --- |
| **Note:** If you are familiar with the eBay Shopping API or the eBay Trading API, you may notice some differences in the API conventions and the way requests are routed for the Merchandising API. The cause for these differences is that the Merchandising API is built on eBay's Services Oriented Architecture (SOA) framework. For more information, see [What's Different](#whatsdiff) in this document. |

## Merchandising Use Cases

The eBay Merchandising API can be used with other eBay APIs to improve buying applications. The merchandising information returned by the service can also help sellers better manage their inventory.

### Improved Buying Experience

On its own, the Merchandising API does not provide enough search and selection capabilities to build a complete shopping, buying, or selling application. However, the merchandising data can be combined with information from other eBay APIs to create a better shopping and buying experience.

#### Improving Selection

Standard finding results can be enhanced with related items. Related item recommendations can provide cross-sell or up-sell opportunities. The **getRelatedCategoryItems** call displays items related to a specified category or item ID.

![Get items from categories related to a provided category or item](images/getrelatedscrn.jpg)

#### Capture Impulse Sales

Add interest and excitement for buyers by showing them what other people are watching. The **getMostWatchedItems** call does just that. To find out what people are buying or searching for on eBay, you can use the [getMerchandisedProducts](/api-docs/buy/marketing/resources/merchandised_product/methods/getMerchandisedProducts) call of the Buy Marketing API.

All these approaches help connect buyers with products and listings.

### Optimize Your Selling Strategy

The Merchandising API provides data that can help sellers make the most of their inventory. Data about eBay buying habits can inform seller decisions about inventory and pricing. The **getMostWatchedItems** call provides the current price for the most watched items, which might help sellers optimize their own pricing tactics. If buyers aren't finding what they are looking for in a seller's inventory, the seller can use **getRelatedCategoryItems** to supplement their inventory with related items to ensure buyers have a good experience.

**Note:** The Merchandising API provides dynamic merchandising data for active listings.

### Increase Affiliate Commission Revenue

If you use affiliate parameters, you can get commissions based on transactions and based on registrations of new users. Affiliate parameters enable the tracking of user activity and can be used with all Merchandising API calls.

See the [eBay Partner Network](https://partnernetwork.ebay.com/) for information about commissions.

Refer to [Making A Call](/Devzone/merchandising/docs/Concepts/MerchandisingAPI_FormatOverview.html) for information about how to specify your affiliate details when you make API calls.

### Combining with Other eBay APIs

The Merchandising API can be used in conjunction with any of the eBay APIs. We recommend you try using the Merchandising API together with one or more of the following APIs.

#### eBay Shopping API

[eBay Shopping API](/Devzone/shopping/docs/CallRef/index.html) offer access to public read-only data such as searching for items, products, and eBay member profiles.

#### eBay Trading API

[eBay Trading API](/Devzone/XML/docs/Reference/eBay/index.html) offer authenticated access to private eBay data to enable automation and innovation in the areas of listing items, retrieving seller sales status, managing post-transaction fulfillment, and accessing private user information such as My eBay and Feedback details.

#### Additional eBay APIs

See the [APIs](/develop/apis) landing page for information about all eBay APIs.

## Working with the Merchandising API

The Merchandising API is simple and easy to use. This section outlines the fundamentals of how to use the Merchandising API.

### What's Different?

The eBay Merchandising API works similarly to other eBay APIs. For example, the Merchandising API uses the same authentication as the Shopping API. In fact, you can use the same AppID. However, the Merchandising API is built on eBay's Services Oriented Architecture (SOA) framework, and as a result, there are some changes to the API conventions and how you route requests.

Here are the most notable differences:

* **Service Endpoint**âthe Merchandising API has unique gateway URLs (service endpoint) for Production:
  + Production endpoint: `https://svcs.ebay.com/MerchandisingService?`
* **HTTP headers and URL parameters**âthe Merchandising API uses a Service Oriented Architecture (SOA) framework, which requires a new set of HTTP headers and URL parameters. For example, although you can use the same AppID you use with the Shopping or Trading APIs, the header (`EBAY-SOA-CONSUMER-ID`) or URL parameter (`CONSUMER-ID`) you use is different. See [Standard URL HTTP Header Values](MerchandisingAPI_FormatOverview.html#StandardURLParameters) in Making a Merchandising API Call for more information.
* **Schema and data type changes**âthe Merchandising API does not share schema or data types with other eBay APIs. In the API, you will find the following differences from other eBay APIs:
  + New types, such as **Item**, with standard content like item ID, title, pricing information, time left, and a View Item page URL. Although the types and fields are slightly different, the eBay data is the same.
  + Completely new types, such as the **ErrorMessage** type, a completely new structure for error information
  + **No site ID!** Instead, we provide **globalId**, a unique identifier for a combination of site, language, and territory. See the [Global ID Values](/Devzone/merchandising/docs/concepts/siteidtoglobalid.html) table for a list of global IDs that map to site IDs. The global ID you use must map to an eBay site with a site ID.
* **Naming conventions**âthe naming conventions for the Merchandising API are slightly different. Most notably, call names and fields in the Merchandising API begin with lowercase letters.
* **Versioning strategy**âthe version numbering scheme for the Merchandising API is different from the scheme used by the eBay Shopping and Trading APIs. The Merchandising API version consists of three digits (e.g., 1.2.3):
  + The first digit indicates the major release version. Major releases are not backward compatible.
  + The second digit indicates the minor release version. Minor releases consist of feature additions or behavior changes that are backward compatible.
  + The third digit indicates the maintenance release version. Maintenance releases are for correcting small problems have minimal impact on the features or function of the Merchandising API.

See [Making a Merchandising API Call](MerchandisingAPI_FormatOverview.html) for information about how to construct a Merchandising API call. Refer to the [API Reference](../CallRef/index.html) for details about the API structure and logic.

### API Call Limits

Please refer to the [API Call Limits](/develop/apis/api-call-limits) page for current default call limits and call limits for applications that have completed the [Application Growth Check](/grow/application-growth-check), which is a free service that the eBay Developers Program provides to its members.

### Authentication

All that is required to use the Merchandising API is an AppID. If you already have an AppID for use with another eBay API, it will work for Merchandising API, as well. You must specify your AppID in the `EBAY-SOA-CONSUMER-ID` header (or `CONSUMER-ID` URL parameter) of every request.

To get your AppID:

1. Go to [https://developer.ebay.com/join](/join) and click the **Register Now** button.
2. Fill out the Join form.
3. Generate your Production keys.
4. Use your Production AppID for making calls in Production (the eBay website).

### Supported Request and Response Formats

The eBay Merchandising API supports HTTP POST and HTTP GET methods. The HTTP POST method supports SOAP or XML formats in the request and name-value (NV), SOAP, or XML formats in the or response. The HTTP GET method supports NV format for requests and NV, SOAP, or XML formats in the response.

For details about making calls using supported methods and formats, see [Making a Merchandising API Call](MerchandisingAPI_FormatOverview.html).

### API Reference

Refer to the [API Reference](../CallRef/index.html) for a list of calls in the Merchandising API. The Call Reference includes the following information:

* Prototypes of the request and response structure for each call
* Comprehensive list of inputs and outputs supported by each call and descriptions of their meaning and behavior
* Call samples (request and response)
* Index of schema elements (types, fields, enumerations)
* Change history information for each call

### Make a Call

The eBay Merchandising API is easy to use. All you need is your AppID. In the following steps, you will make a **getMostWatchedItems** call. The request uses the HTTP GET method and looks like this:

```json

https://svcs.ebay.com/MerchandisingService?
  OPERATION-NAME=getMostWatchedItems
  &SERVICE-NAME=MerchandisingService
  &SERVICE-VERSION=1.5.0
  &CONSUMER-ID=YourAppID
```

The response will be in XML format.

### Application Testing

The Merchandising API is optimized to retrieve information from the live eBay site and you can safely test your application with calls to the live eBay site, but the Sandbox supports the Merchandising API, as well.

For more information about testing, refer to [Testing Overview](MerchandisingAPI_FormatOverview.html#TestingOverview) in the Making a Merchandising API Call document.

## Additional Resources

You can get more information about the eBay Merchandising API at these locations:

* [Making a Merchandising API Call](MerchandisingAPI_FormatOverview.html)
* [API Reference](../CallRef/index.html)
* [Release Notes](../ReleaseNotes.html)

  
  
  
  