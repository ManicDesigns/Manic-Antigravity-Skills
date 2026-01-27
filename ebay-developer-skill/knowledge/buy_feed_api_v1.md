# Feed API v1

Source: https://developer.ebay.com/api-docs/buy/static/api-feed.html

# Feed API v1

 

* [Home](/)
* [Develop](/develop)
* [Guides](/develop/guides)
* [Buying Integration Guide](/develop/guides/buying-ig-landing.html)
* Feed API v1

Buying Integration Guide 

[Buy APIs Overview](buy-overview.html)

[Buy APIs Requirements](buy-requirements.html)

[Browse API](api-browse.html)

[Charity API](api-charity.html)

[Deal API](api-deal.html)

Feed API 

[Feed API methods overview](#Understa)

[Feed API integration](#Feed)

[Feed API beta](api-feed_beta.html)

[Marketing API](api-marketing.html)

[Offer API](api-offer.html)

[Order API](api-order.html)

[Categories for Buy APIs](buy-categories.html)

[Buy API Support by Marketplace](ref-marketplace-supported.html)

[Buy API Field Filters](ref-buy-browse-filters.html)

**Note:** 
Do you still need the beta version of the Feed API? Go to the [Feed API beta](api-feed_beta.html) section.

eBay has over a billion listings, providing you with a rich inventory that you can surface in your app or on your site. To get these items, you can use the Feed API to mirror an eBay category by downloading a GZIP file of the items in your chosen categories and specific marketplaces. You can then curate the items to fit your buyers and sync the item details with the live site—all offline—and then store the items in your database.

**Note:** 
This is a [![Limited Icon](/cms/img/docs/partners-api.svg "Limited Release") (Limited Release)](/api-docs/static/versioning.html#Limited). For information on how to obtain access to this API in production, see the [Buy APIs Requirements](buy-requirements.html).

## Feed API methods overview

The Feed API has the following methods:

* [getAccess](/api-docs/buy/feed/v1/resources/access/methods/getAccess) method—Returns the details of the application's feed file access configuration. Lists the marketplaces and categories for which the application can download feeds.
* [getFeedType](/api-docs/buy/feed/v1/resources/feed_type/methods/getFeedType) method—Returns a list of the feeds of a particular feed type that are available for download.  
  **Note:** For bootstrap, item, snapshot and priority feeds, continue to use the [Feed Beta API](/api-docs/buy/feed/resources/methods).
* [getFeedTypes](/api-docs/buy/feed/v1/resources/feed_type/methods/getFeedTypes) method—Returns a list of all the feeds available to download, listed by feed type. The response includes information on how frequently the feed is made available (DAILY, HOURLY, or WEEKLY—currently only DAILY and HOURLY are supported), supported feeds in each available type, each feed's supported marketplaces and each feed file's status (ACTIVE, PAUSED, DEPRECATED).
* [downloadFile](/api-docs/buy/feed/v1/resources/file/methods/downloadFile) method—Returns a specified GZIP feed file, as specified in the request URI. The downloaded file has detailed information on each listing in the feed file. For more information about fields that may be included in a feed file, see [Feed File Fields](/api-docs/buy/feed/resources/item/methods/getItemFeed#h3-response-fields).
* [getFile](/api-docs/buy/feed/v1/resources/file/methods/getFile) method—Returns a list of the metadata for a particular available download file. It includes details on the date of its feed, its file type, the frequency with which it is made available, its format, and its marketplace.
* [getFiles](/api-docs/buy/feed/v1/resources/file/methods/getFiles)—Returns a list of the feed files available to download. The file search can be filtered in the URI by feed type, feed pull frequency, L1 category, and how far back in time from the present the feed can be searched for.

## Feed API integration

The basic steps to integrate with the Feed API and keep the items in sync with the eBay site are:

* [Use getFeedTypes and getFeedType for details about a particular feed type](#Use_getFeedType)
* [Use getAccess to identify the feeds you can access](#Use_getAccess)
* [Use getFiles and getFile for details about your available feeds](#Use_getFile)
* [Use downloadFile to obtain a GZIP file of a particular feed](#Use_downloadFile)

### Use getFeedTypes and getFeedType for details about a particular feed type

Use the **getFeedTypes** method to create a list of the feeds you can download. The list provides details about each feed type including how frequently it is made available, the marketplaces it supports (e.g., EBAY\_US), and the authorization scopes needed for access (see [Specifying OAuth scopes](/api-docs/static/oauth-scopes.html#specifying-scopes "Go to Specifying OAuth scopes")).

**Note:** 
Refer to [Supported feed types](/api-docs/buy/feed/v1/static/overview.html#feed-types) for more details about the feed types supported by the Feed API.

The **getFeedTypes** method also gives you each feed type's **feedTypeId**, which you will use with the **getFeedType** method once you have identified a specific feed type you wish to target.

The **getFeedTypes** method is a simple GET call using a URI call and no input payload:

```json
GET https://api.ebay.com/buy/feed/v1/feed_type
```

You can filter your search in the URI by providing a **feed\_scope** parameter, so your returned list is not filled with unwanted feeds. You can also add a **marketplace\_ids** parameter, to limit your returns to useful markeplaces. For example, the following call limits the responses to feed files whose feed scope is sell.inventory, and whose marketplace is the U.S.

```json
GET https://api.ebay.com/buy/feed/v1/feed_type?feed_scope=DAILY&marketplace_ids=EBAY_US
```

Use the **getFeedType** method when you do not need the complete list of feeds provided by the **getFeedTypes** method. The **getFeedType** method provides the same information as the **getFeedTypes**, but confines the search to a specific feed type, as provided in the URI.

```json
GET https://api.ebay.com/buy/feed/v1/feed_type/{feed_type_id}
```

The refined search results in a smaller file whose data is easier to read and manipulate programatically.

### Use getAccess to identify the feeds you can access

When you submit an application for use with eBay, you will configure your application to allow access to a number of product categories within designated marketplaces (see [Buy APIs Requirements)](/api-docs/buy/static/buy-requirements.html "Go to Buy APIs Requirements document"). For instance, category **63**, **Comics**, in the US market, **EBAY\_US**. Before attempting to acquire a feed, it is useful to know which categories and marketplaces your application can access. The **getAccess** method gives you a list of those categories and marketplaces.

The **getAccess** method uses a simple URI call:

```json
GET https://api.ebay.com/buy/feed/v1/access
```

The response payload is a listing of the marketplaces and categories that pertain to your application, which can be used to focus a search using the **getFeedType(s**) and **getFile(s)** methods. The following is an example.

```json
{
  "accesses": [
    {
      "feedType": "CURATED_ITEM_FEED",
      "constraints": [
        {
          "marketplaceId": "EBAY_FR",
          "categoryIds": [
          "7000",
          "8000",
          "777"
          ]
        },
       {
          "marketplaceId": "EBAY_US",
          "categoryIds": [
          "7",
          "10000",
          "6000"
          ]
     }
  ]
}
```

### Use getFiles and getFile for details about your available feeds

A further way to granulate your data search is to use the **getFiles** and **getFile** methods.

It is possible to download a listing of all available feeds with a simple call **getFiles** call with no URI parameters.

```json
GET https://api.ebay.com/buy/feed/v1/file
```

However, the real power of the **getFiles** method is in its URI parameters, with which you can identify the exact file you need. You can use the feed type and feed scope you identified using the **getFeedType** method as containing the feed you want, then further focus your call with one or more category ids. Lastly, you can use the **look\_back** parameter to further confine your search to determine how recently you feed to have been pulled.

For example you could limit your search to curated item feeds, in cookware (**categoryid** of `974`) that have been made available in the two days (note that the look-back value's unit is always minutes, so two days is 2880 minutes).

```json
GET https://api.ebay.com/buy/feed/v1/file?feed-type_id=CURATED_ITEM_FEED&category_ids=974&k_back=2880
```

### Use downloadFile to obtain a GZIP file of a particular feed

The final step is to download the actual GZIP file, using the **downloadFile** method.

The **Feed** API methods require an eBay L1 (top-level) category ID. You can use the [Taxonomy API](/api-docs/commerce/taxonomy/resources/methods)
to get the L1 and leaf (child) categories for a specific eBay marketplace. This enables you to download items from a specific category, map the eBay categories to your categories, and use the leaf categories to curate the items.

eBay’s product category tree consists of the following elements that can be used for qualitative matching:

* categoryTreeId - identifies the respective marketplace
* categoryTreeVersion - identifies the current version and determines if you’ll have to update the matching
* categoryId - a unique id that identifies a certain product category in the category hierarchy for a given marketplace
* categoryName - name of the respective category
* categoryTreeNodeLevel - category level within the complete category tree
* leafCategoryTreeNode - indicates if the respective category is located on the leaf level of the category tree

#### Retrieving a GZIP feed file

**Note:** Instead of retrieving the feed file in "chunks", you can use the open source [Feed V1 SDK](https://github.com/eBay/ebay-feedv1-dotnet-sdk) to retrieve the feed file. This SDK is written in .NET and downloads, combines files into a single file when needed, and unzips the entire feed file. It also lets you specify field filters to curate the items in the file.

The TSV\_GZIP feed files, which are binary, can be streamed in chunks. You must specify the size of each chunk in bytes using the request **Range** header.

The maximum number of bytes you can request is 200 MB, which is 209715200 bytes. When you specify the **Range** header, the **content-range** response header is returned showing `rangeValueSpecified/totalSizeOfFile`.

In the following example, the request **Range** header is set to retrieve the maximum number of bytes. The **content-range** response shows that the total size of the file is 1076602 bytes. This means the entire feed file was retrieved. The HTTP status code will be 200 OK.

```json
Range bytes=0-209715200
```

```json
content-range 0-209715200/1076602
```

If the size of the feed file is greater than 209715200 bytes, it will take multiple methods to retrieve the entire file. This is discussed in the next section.

##### How to retrieve a feed file using multiple calls

When retrieving a feed file in chunks, it is important to remember that the response is for a certain number of bytes not records. This means you must combine the chunks in the correct order. Also note that the chunks are binary not human readable. Because you are retrieving the file in pieces, if one method fails, you do not have to start over, you can just resubmit that call.

**Note:** In the following example, we are assuming that the maximum size of a chunk is 10MB (10485760 bytes). But the maximum is 200MB.

To retrieve a file that is 24MB (25165824 bytes), you would make 3 calls, which can be multi-threaded. Each call will return a gzip file containing the number of bytes specified by the **Range** request header. These will be binary files and must be put together in the correct order to get the entire feed file.

The table below shows the value of the **Range** request header, the HTTP response status, and the **Content-range** response header for each call. The HTTP status code for a successful call is always 206, even for the last call, because the response is never the entire file.

|  |  |  |  |
| --- | --- | --- | --- |
|  | Range Request Header | HTTP Response Status | Content-range response Header |
| First method | Range: `bytes=0-10485760` | 206 (successful partial response) | `0-10485760/25165824` |
| Second method | Range: `bytes=10485761-20971520` | 206 (successful partial response) | `10485761-20971520/25165824` |
| Third method | Range: `bytes=20971521-31457280` | 206 (successful partial response) | `20971521-31457280/25165824` |

If the **Range** value is invalid, a 416 HTTP status code is returned.

Related topics

* [Buying Apps](/api-docs/buy/static/buy-landing.html)
* [API Documentation](#)

  [Browse API](/api-docs/buy/browse/overview.html)[Deal API](/api-docs/buy/deal/overview.html)[Feed Beta API](/api-docs/buy/feed/overview.html)[Feed API](/api-docs/buy/feed/v1/overview.html)[Marketing API](/api-docs/buy/marketing/overview.html)[Offer API](/api-docs/buy/offer/overview.html)[Order API](/api-docs/buy/order/overview.html)
* [Guides](/develop/guides)
* [Related Docs](#)

  [Using eBay RESTful APIs](/api-docs/static/ebay-rest-landing.html)[Commerce APIs](/develop/apis/restful-apis/commerce-apis)[Developer APIs](/develop/apis/restful-apis/developer-apis)[Finding API](/devzone/finding/callref/index.html)[Shopping API](/devzone/shopping/docs/callref/index.html)