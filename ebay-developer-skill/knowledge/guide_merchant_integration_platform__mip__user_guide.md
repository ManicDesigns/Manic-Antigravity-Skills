# Merchant Integration Platform (MIP) User Guide

Source: https://developer.ebay.com/api-docs/user-guides/static/mip-user-guide-landing.html

# Merchant Integration Platform (MIP) User Guide

 

* [Home](/)
* [Develop](/develop)
* [Guides](/develop/guides)
* Merchant Integration Platform (MIP) User Guide

Merchant Integration Platform (MIP) User Guide 

[Getting started](mip-user-guide/mip-overview-getting-started.html)

[Sample files](mip-user-guide/mip-sample-files.html)

[Inventory Management](mip-user-guide/mip-managing-inventory.html)

[Marketing Management](mip-user-guide/mip-managing-marketing.html)

[Report](mip-user-guide/mip-reports.html)

[Metadata](mip-user-guide/mip-feed-types-metadata.html)

[Settings](mip-user-guide/mip-settings.html)

[Enumerated values](mip-user-guide/mip-enum-values.html)

The eBay Merchant Integration Platform (MIP) is a powerful, easy-to-use application that eBay sellers can use to manage product listings and orders. See [Basic description](mip-user-guide/mip-overview-getting-started.html#basic-description) for additional information.

**Important!**  To avoid any unnecessary fees or charges, please refer to the [Best practices](mip-user-guide/mip-best-practices.html) section of this guide before you begin using the MIP platform.

To use MIP, you should already be familiar with selling on eBay.

**Purpose of this guide**

This guide explains how to:

* Set up MIP
* Create feeds to list your products on eBay
* Update your listings with price changes, quantity, and other information
* Retrieve Active Inventory and Order reports

**Compatibility with other management tools**

**Important!**  MIP **does not** detect changes that you make to listings using other tools, such as eBay web flows or Seller Hub. Do not use MIP in conjunction with any other method to make changes to an item listing.

To prevent issues such as duplicate listings, after you begin using MIP **do not continue** to use eBay web flows, mobile apps, or third-party tools to upload, revise, and manage your active listings and orders.

However, you can continue to use eBay.com web flows for the following tasks: feedback, returns, and responses to buyer cases.

## MIP updates

Periodically, new fields are added to MIP feeds. In most cases, new fields in CSV files are appended to the end of changed feed file, and new fields in XML files are added to the end of the request/response payload or to the end of an existing container. Changes are communicated through the [What's new](#new) section.

**Important!** All MIP users should monitor this guide to keep current on new and modified fields. For users who are programmatically using MIP, it is recommended that their integrations be coded to accommodate all updates. As a best practice, always reference the fields or columns by their names, and not by their absolute or relative position in a feed.

## What’s new

The following updates have been made to the Merchant Integration Platform.

| Release Date | Feature Description |
| --- | --- |
| September 2025 | **Important Update:** eBay's bulk integrations will be modified to address data handling requirements for developers in the following countries: China (and its territories), Russia, North Korea, Cuba, Iran, Venezuela. Usernames will be replaced with immutable user IDs, and financial data will be protected for certain users.  If you are using MIP SFTP and **not located in the regions listed above**, you can regenerate a new SFTP token and continue to have access to the full reports.  Learn more [here](/api-docs/static/data-handling-update.html).  **Username fields (buyerID & sellerID)**  Effective **September 30th, 2025**, MIP users who are downloading Order Reports by connecting to MIP SFTP, and located in the countries listed above, will no longer receive private username data for U.S. users through these fields. Instead, an immutable public user ID will be returned.  **PaymentMethod & PaymentInstrument fields**  Effective **September 30th, 2025**, MIP users who are downloading Order Reports by connecting to MIP SFTP, and located in the countries listed above, will no longer receive buyer payment details for U.S. users. If you are one of these select developers, you will receive a value of "CustomCode" in place of buyer payment details.  These changes will not affect data available to eBay sellers through their seller accounts. Sellers may continue to access this data by logging into the platform. |
| March 2025 | eBay has added enhanced performance, security, and user experience to the MIP UI. Access the refreshed interface through its eBay US interface at [www.ebay.com/mip](https://www.ebay.com/mip). See [Open the MIP interface](/api-docs/user-guides/static/mip-user-guide/mip-overview-getting-started.html#Launchin) for URLs of other marketplaces.  Also, the following feed types are now only available through [SFTP](/api-docs/user-guides/static/mip-user-guide/mip-setup-ftp-setup.html) (and not the [MIP UI](/api-docs/user-guides/static/mip-user-guide/mip-overview-getting-started.html)):   * [Promoted Listing](/api-docs/user-guides/static/mip-user-guide/mip-about-pl-feeds.html) * [Promoted Listing eligibility](/api-docs/user-guides/static/mip-user-guide/mip-about-pl-eligibility-feeds.html) * [Classification](/api-docs/user-guides/static/mip-user-guide/mip-about-classification-feeds.html) * [Category Metadata](/api-docs/user-guides/static/mip-user-guide/mip-about-category-metadata-feeds.html) |
| February 2025 | The SHA256 and MD5 fingerprints for the five supported host keys have been updated:   * **ed25519** * **rsa-sha2-512** * **rsa-sha2-256** * **ecdsa-sha2-nistp256** * **ecdsa-sha2-nistp384**   See [Verifying fingerprints for secure connection](/api-docs/user-guides/static/mip-user-guide/mip-setup-feed-schema.html#verifying-fingerprints) for supported fingerprint values.  The following SFTP server host keys have been deprecated:   * ecdh-sha2-nistp256 * ecdh-sha2-nistp384 * ecdh-sha2-nistp521   Refer to the [Deprecated Ciphers, MACs, and Key Exchange](mip-user-guide/mip-setup-feed-schema.html#deprecated) table for a complete list of deprecated ciphers, MACs, and key exchanges. |
| January 2025 | Added the **contactUrl** field to the **manufacturer** and **responsiblePersons** containers. This field allows sellers to add an electronic contact method for manufacturers and responsible persons when adding GPSR information to a listing. See [Distribution Feed Definitions](mip-user-guide/mip-definitions-distribution-feed.html), [Combined Feed Definitions](mip-user-guide/mip-definitions-product-combined-feed.html), and [Sample feed and response files](mip-user-guide/mip-sample-files.html).  Added two new condition enumerated values: `PRE_OWNED_EXCELLENT` and `PRE_OWNED_FAIR`. See [Conditions enumerated values](/api-docs/user-guides/static/mip-user-guide/mip-enum-conditions.html). |
| October 2024 | Removed Economic Operator fields from the Distribution and Combined feed requests. These fields will be ignored and silently dropped if included in feed files. |
| August 2024 | Added the following fields to Distribution and Combined Feed requests to support GPSR-related information:   * **manufacturer** * **responsiblePersons** * **productSafety** * **documents**   See [Distribution Feed Definitions](mip-user-guide/mip-definitions-distribution-feed.html), [Combined Feed Definitions](mip-user-guide/mip-definitions-product-combined-feed.html), and [Sample feed and response files](mip-user-guide/mip-sample-files.html). |
| July 2024 | As a part of implementing enhanced security measures, eBay will migrate from Port 22 to Port 2222 for SFTP connections to MIP Sandbox (mip.sandbox.ebay.com). SFTP connections through Port 22 will start being blocked on July 30, 2024. |
| June 2024 | Added the following fields to Distribution and Combined Feed requests to support eBay auctions:   * **auctionReservePrice** * **auctionStartPrice** * **listingDuration** * **listingStartDate** * **format**   See [Distribution Feed Definitions](mip-user-guide/mip-definitions-distribution-feed.html), [Combined Feed Definitions](mip-user-guide/mip-definitions-product-combined-feed.html), and [Sample feed and response files](mip-user-guide/mip-sample-files.html). |
| June 2024 | A new requirement adding support for EPA approved tuning devices and software products was added to category ID 173651 (Auto Performance Tuning Devices & Software). See [Distribution Feed Definitions](mip-user-guide/mip-definitions-distribution-feed.html) and [Tuning devices and software](mip-user-guide/mip-tuning-devices-and-software.html). |
| February 2024 | Added support for Economic Operator fields. See [Distribution Feed Definitions](mip-user-guide/mip-definitions-distribution-feed.html), [Combined Feed Definitions](mip-user-guide/mip-definitions-product-combined-feed.html), and [Sample feed and response files](mip-user-guide/mip-sample-files.html).  Added new security algorithms to support enhanced security measures. See [Feed Schema](/api-docs/user-guides/static/mip-user-guide/mip-setup-feed-schema.html#verifying-fingerprints) for more information. |
| January 2024 | The following CBC mode ciphers and MD5 MACs have been deprecated:   * chacha20-poly1305@openssh.com * hmac-sha2-512-etm@openssh.com * hmac-sha2-256-etm@openssh.com   Refer to the [Deprecated Ciphers, MACs, and Key Exchange](mip-user-guide/mip-setup-feed-schema.html#deprecated) table for a complete list of deprecated ciphers, MACs, and key exchanges.  For the list of preferred ciphers and MACs for use with the SFTP server, listed in order of preference, refer to [Preferred Ciphers and MACs](mip-user-guide/mip-setup-feed-schema.html#pref). |
| October 2023 | New **linkedLineItem** field added to Order Report. This field will provide data on a line item that is linked to the corresponding order, but not actually a part of the order. This can be used to provide details about a component (purchased from one seller) needed for its installation (purchased from a different seller). Details can identify the linked seller and also include delivery times, item information, and order information. See [Pending orders response definitions](mip-user-guide/mip-definitions-order-report.html). |
| August 2023 | This version of the MIP guide supersedes the previous version. Bookmark this page for future reference: [https://developer.ebay.com/api-docs/user-guides/static/mip-user-guide-landing.html](/api-docs/user-guides/static/mip-user-guide-landing.html) |
| July 2023 | Condition descriptors for specific trading card categories are now supported on all eBay marketplaces. See [Product Feed Definitions](mip-user-guide/mip-definitions-product-feed.html), [Combined Feed Definitions](mip-user-guide/mip-definitions-product-combined-feed.html), and [Sample feed and response files](mip-user-guide/mip-sample-files.html). |
| June 2023 | Added support for condition descriptors to specific trading card categories. Currently available only in the United Kingdom (GB), with rollout to all other marketplaces early July 2023. See [Product Feed Definitions](mip-user-guide/mip-definitions-product-feed.html), [Combined Feed Definitions](mip-user-guide/mip-definitions-product-combined-feed.html), and [Sample feed and response files](mip-user-guide/mip-sample-files.html). |
| May 2023 | Added support for Energy Efficiency Labels, Hazmat information, and Regional Seller Disclosures for the German (DE) marketplace. See [Distribution feed definitions](mip-user-guide/mip-definitions-distribution-feed.html), [Combined Feed Definitions](mip-user-guide/mip-definitions-product-combined-feed.html), and [Sample feed and response files](mip-user-guide/mip-sample-files.html). |
| January 2022 | Added support for Extended Producer Responsibility and compliance policies through listing creation and orders. See [Distribution feed definitions](mip-user-guide/mip-definitions-distribution-feed.html), [Combined Feed Definitions](mip-user-guide/mip-definitions-product-combined-feed.html), and [Sample feed and response files](mip-user-guide/mip-sample-files.html). Use Extended Producer Responsibility to provide IDs for the producer or importer related to the new item, and compliance policies to specify custom policy IDs. A custom policy ID refers to the relevant policy created for compliance and other purposes. |
| August 2021 | Due to security concerns with Cipher Block Chaining (CBC) and MD5 encryption when using the SFTP server, a number of CBC mode ciphers and MD5 MACs have been deprecated. See the **Deprecated Ciphers, MACs, and Key Exchange** table in [Uploading the sample feed](mip-user-guide/mip-setup-feed-schema.html#Uploadin2) for details. |
| July 2021 | Added a new eBayReferenceName field for describing VAT (Value Added Tax) for sales involving regions where VAT is applicable (see [Distribution feed definitions](mip-user-guide/mip-definitions-distribution-feed.html) and [Sample feed and response files](mip-user-guide/mip-sample-files.html)).  The field contains an eBay Tax Number and also possesses a **Name** attribute, which delineates the region for which the VAT is applied. |
| May 2021 | Added support for secondary categories and private listings to the distribution feed type (see [Distribution feed definitions](mip-user-guide/mip-definitions-distribution-feed.html) and [Sample feed and response files](mip-user-guide/mip-sample-files.html)).   * Use secondary categories to list the item under two categories. A fee may be charged when adding a secondary category to a listing. * With private listings, the user IDs of buyers/bidders are only shown to the seller of the listing, and not to any other eBay users   Other miscellaneous document updates. |

**Older releases**

| Release Date | Feature Description |
| --- | --- |
| Jan 2021 | * Added Category Metadata to the Inventory Management Feed Type (see [About category metadata feeds](mip-user-guide/mip-about-category-metadata-feeds.html), [Category metadata feed definitions](mip-user-guide/mip-definitions-category-metadata-feed.html), and [Sample feed and response files](mip-user-guide/mip-sample-files.html)). Use Category Metadata feeds to find category specifics and their accepted values (helps complete eBay listing requirements). Specifying the correct values optimizes your product listing so it is returned in relevant search results. * Other miscellaneous document updates. |
| Nov 2019 | * Added **totalIncludesEBayCollectedTax** to the order report to support [changes to the way taxes are processed](https://community.ebay.com/t5/Announcements/New-Internet-Sales-Tax-changes-that-impact-you/ba-p/30282351) in situations where eBay collects and remits taxes on behalf of sellers. eBay is responsible for collecting and remitting internet sales tax (IST) for [many US states](https://www.ebay.com/help/selling/fees-credits-invoices/taxes-import-charges?id=4121#section4) and also collects and remits goods and services taxes (GST) for [many items that ship to Australia and New Zealand](https://www.ebay.com.au/help/policies/selling-policies/tax-policy?id=4348). |
| July 2019 | * Added support for Promoted Listings feeds to [manage your inventory marketing](mip-user-guide/mip-managing-marketing.html) on eBay |
| May 2019 | * Support for catalog change requests has been removed. |
| Oct 2018 | * Increased number of attributes from 25 to 30. |
| Aug 2018 | * Added catalog request and catalog request status feeds, response files, and sample files. |
| Mar 2018 | * Added delete inventory and product search feeds, response files, and sample files * Added multi-channel listing capability * Added support for Product-based Shopping Experience * Product feeds now include using ePIDs to identify product listings. * Using the product search feed, users can specify an ePID or other criteria to search for catalog products. |
| Feb 2018 | * Added ePID, MPN, and Brand fields to product and combined-product feeds * Added fulfillment capability to location feed * Increased max compatibilities from 100 to 3000 in the distribution feed * Increased standard image (Picture URL) quantity from 12 to 24 * Increased group images (Picture URL) from 1 to 12 * Multiple carriers and tracking numbers per item allowed in Order Fulfillment feeds. |
| Nov 2017 | * Added buy online, pickup-in-store sample files. * Added classification and item-specifics feeds to provide detailed information and better search capabilities for buyers. |
| Oct 2017 | * Added buy online, pickup-in-store capability |
| Aug 2017 | * inventory feeds update the prices and available quantities of products already on the eBay site. * Location feeds update the eBay sites where the items are listed. * Description templates allow experienced users to create their own look and feel for their listings on eBay. |
| Jul 2017 | * Sample files are available for most feed types. |
| May 2017 | * A new version of channel management replaces global settings. It allows channelization operation and the ability to set a default channel. |
| Jan 2017 | * Support for unzipped feed files. You can upload feed files either zipped or unzipped. * A new combined product feed that you can optionally use instead of separate product, availability, and distribution feeds. * You can run different feed types in parallel for more convenient feed management. * You can set response files to be in either CSV or XML format. * Redesigned response file structure that is unified across product, distribution, and availability feeds. * You can set the warehouse location only with the MIP user interface. * When a feed contains duplicate SKUs, only the first occurrence of the SKU is processed. Subsequent duplicate SKUs are ignored. * Order Ack is now supported in the feed type Order Fulfillment. |