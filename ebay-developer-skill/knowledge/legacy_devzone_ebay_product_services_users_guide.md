# eBay Product Services Users Guide

Source: https://developer.ebay.com/Devzone/product/Concepts/ProductAPIGuide.html

# eBay Product Services Users Guide

eBay Product Services APIs retrieve information about products on eBay to help sellers add products to the eBay catalogs or to list items with Parts Compatibility. Parts Compatibility is an eBay feature that uses structured data to associate compatible assemblies with parts listed on eBay. For example, Parts Compatibility enables sellers to specify accurately and comprehensively the vehicles on which a headlight or a rim will fit. Parts compatibility improves search relevancy and frees up item titles and descriptions for more detailed and informative descriptions of the part.

* [Services Overview](#over)
* [Use Cases](#work)
* [Working with the APIs](#use)
* [Additional Resources](#resources)

## Services Overview

eBay Product Services consists of two separate APIs, the Product API and Product Metadata API. These APIs retrieve valuable information and metadata about products on eBay to help you add new items to an eBay catalog or to list items with Parts Compatibility.

### Product API

The Product API consists of calls that return product information. For example, you can use the Product API to identify products that have associated compatibilities. Listing an item with a product that has compatibilities (e.g., specific vehicle applications, such as a 2004 Honda Accord) is one way to list an item with parts compatibility information.

The API lets you retrieve product information in a variety of ways:

* Find products that have fitment information for a specific vehicle
* Find the compatible vehicles for a specific product (part) based on its specifications
* Get the compatible applications (vehicles) associated with a specific product

|  |
| --- |
| **Note:** The ability for external users to add products to eBay catalogs has been disabled for many months. The related API calls, **addProducts** and **getProductSubmissions**, no longer provide value, so they have been removed from the documentation as of Wednesday, May 14, 2014. |

Refer to the [eBay Product API Reference](../CallRef/index.html) for a list of API calls and the associated inputs and outputs for each.

### Product Metadata API

The Product Metadata API consists of calls that return product metadata for specific categories. For example, you can use the Product Metadata API to retrieve the compatibility search names (e.g., Make and Model) and values (e.g., Honda and Accord) that are allowed for a given category. You can use this compatibility metadata to construct compatible applications for a specific category. Listing an item with compatible applications (e.g., a fender that fits specific cars) is one way to list an item with parts compatibility information. This is known as listing with compatibility by application.

The API returns the following types of metadata:

* Compatibility search names and search values, which can be used as filters or search criteria in the Product API or to construct compatible applications for listing with parts compatibility by application
* Bulk compatibility search values for building a local version of the metadata
* Metadata version information to help you monitor for changes, so you can effectively maintain the compatibility metadata locally

Refer to the [eBay Product Metadata API Reference](../../product-metadata/CallRef/index.html) for a list of API calls and the associated inputs and outputs for each.

## Use Cases

The eBay Product API and eBay Product Metadata API support [Parts Compatibility](#workcompatibility)

### Parts Compatibility

Parts Compatibility uses structured data to associate compatible assemblies with parts listed on eBay. For example, parts compatibility enables sellers to specify accurately and comprehensively the vehicles on which a side mirror or a rim will fit. Parts compatibility improves search relevancy and frees up item titles and descriptions for more useful descriptions of the part.

|  |
| --- |
| **Note:** Parts Compatibility is supported in select categories for eBay Motors (site ID 100, global ID EBAY-MOTOR) and eBay Germany (site ID 77, global ID EBAY-DE) in the Sandbox and Production environments. Parts Compatibility is enabled by category. Use [**GetCategoryFeatures**](http://developer.ebay.com/DevZone/XML/docs/Reference/eBay/GetCategoryFeatures.html) (use **FeatureID** values: CompatibilityEnabled, MinCompatibleApplications, MaxCompatibleApplications) to retrieve information about categories that support parts compatibility. |

#### Locating Products with Compatibilities

The easiest way to list an item with Parts Compatibility is to select a product that has compatibilies. If the part or accessory you want to list is in the eBay catalog for a category that supports compatibilities, you can use the eBay data to prefill your listings with rich structured data, including the compatible applications.

#### Identifying Compatibility Information

Parts Compatibilities (or compatible applications) consist of name-value pairs that describe an assembly with which a part or accessory is compatible. A compatible application for an item listed in an eBay Motors Parts & Accessories category will be name-value pairs that describe a vehicle (e.g., Make = Honda, Model = Accord, Year = 2004, etc.). The Product and Product Metadata APIs both return compatibility information. Use [**getProductCompatibilities**](http://developer.ebay.com/Devzone/product/CallRef/getProductCompatibilities.html) in the Product API to retrieve compatibilities associated with a specific product or set of product specifications. Use the Product Metadata API to retrieve compatibility data by category.

The primary use of the compatibility information returned by the Product and Product Metadata APIs is to add or revise item listings with parts compatibility. That is, the compatibility name-value pairs can be used to construct an item compatibility list (**Item.ItemCompatibilityList**) for use with the **AddItem** family of calls in the Trading API.

Compatibility information can also be used as a filter for product searches, use the [**findProductsByCompatibility**](http://developer.ebay.com/Devzone/product/CallRef/findProductsByCompatibility.html) call to restrict the products in the response to only those compatible with the specified application (e.g., vehicle) in the request.

#### Listing Items with Parts Compatibility

Once you have used the Product and Product Metadata API to collect compatibility information, you use the **AddItem** family of calls in the Trading API to list the item.

See [Specify parts compatibility manually](/api-docs/user-guides/static/trading-user-guide/manually-specify-compatibility.html) in the [Trading API User Guide](/api-docs/user-guides/static/trading-user-guide-landing.html) to learn more about how to list an item with parts compatibility information.

### Combining with Other eBay APIs

The Product and Product Metadata APIs are intended to be used in conjunction with the eBay Trading API.

#### eBay Trading API

[eBay Trading API](http://developer.ebay.com/Devzone/XML/docs/Reference/eBay/index.html) offers authenticated access to private eBay data to enable automation and innovation in the areas of listing items, retrieving seller sales status, managing post-transaction fulfillment, and accessing private user information such as My eBay and Feedback details.

Using the Trading API, you can:

* Determine which categories support parts compatibility data
* Add or revise items with parts compatibility data
* Retrieve parts compatibility data for items listed with compatibility by application

#### Additional eBay APIs

See the [API Documentation](https://go.developer.ebay.com/api-documentation) page to learn more about eBay APIs.

## Working with the APIs

The Product and Product Metadata APIs are simple and easy to use. This section outlines the fundamentals of how to use them.

### Authentication

All that is required to use the Product or Product Metadata APIs is an AppID. If you already have an AppID for use with another eBay API, such as the Shopping or Merchandising APIs, it will work with the Product and Product Metadata APIs, as well. You must specify your AppID in the `X-EBAY-SOA-SECURITY-APPNAME` HTTP header (or `SECURITY-APPNAME` URL parameter) of every request.

If you have not already, [join the eBay Developers Program](http://developer.ebay.com/join) and get your Access Keys.

Joining is free and you get 5,000 API calls a day just for joining! When you generate your application keys from your [My Account page](https://developer.ebay.com/DevZone/account/Default.aspx). You will need to generate separate keys for use with the Sandbox and Production environments.

### API Call Limits

Please refer to the [API Call Limits page](https://go.developer.ebay.com/api-call-limits) on the eBay Developers Program site for current default call limits and call limits for applications that have completed the [Compatible Application Check](http://developer.ebay.com/support/certification/), which is a free service that the eBay Developers Program provides to its members.

### Limitations and Restrictions

The Product and Product Metadata APIs are provided to support Parts Compatibility only. Parts Compatibility is supported in select categories for the eBay Motors (site ID 100, global ID EBAY-MOTOR) and eBay Germany (site ID 77, global ID EBAY-DE) sites only.

Use [**GetCategoryFeatures**](http://developer.ebay.com/DevZone/XML/docs/Reference/eBay/GetCategoryFeatures.html) in the Trading API to determine which categories support Parts Compatibility (feature ID: CompatibilityEnabled).

When submitting your Product or Product Metadata requests, you must set the global ID in the `X-EBAY-SOA-GLOBAL-ID` HTTP header (or `GLOBAL-ID` URL parameter) of every request to correspond to one of the supported sites, such as eBay Motors (global ID: `EBAY-MOTOR`) for Parts Compatibility. Most calls require you to specify the category ID in the request. Use only categories that support the feature you are using.

### Sandbox Environment

The Product and Product Metadata APIs work in the Sandbox for select categories. Use [**GetCategoryFeatures**](http://developer.ebay.com/DevZone/XML/docs/Reference/eBay/GetCategoryFeatures.html) in the Trading API to determine which categories support Parts Compatibility (feature ID: CompatibilityEnabled).

For more information about testing, refer to [Testing Overview](MakingACall.html#TestingOverview) in the Making an API Call document.

### API Reference

Refer to the [API Reference](LandAPIRef.html) for a list of calls in the Finding API. The API Reference includes the following information:

* Prototypes of the request and response structure for each call
* Comprehensive list of inputs and outputs supported by each call and descriptions of their meaning and behavior
* Call samples (request and response)
* Index of schema elements (types, fields, enumerations)
* Change history information for each call

## Additional Resources

You can get more information about the eBay Finding API at these locations:

* [Making an API Call](MakingACall.html)
* [API Reference](../CallRef/index.html)
* [Release Notes](../ReleaseNotes.html)

  
  
  
  