# Listing Creation Guide (v2)

Source: https://developer.ebay.com/develop/guides-v2/listing-creation/listing-creation

This guide explores various methods for creating new eBay listings. It covers creating individual listings for single-SKU products, managing listings with multiple variations (multiple-SKU), bulk listing creation, and generating listings based on existing eBay Catalog products.

---

## Overview

### Available APIs for Listing Creation

| API | Type | Description |
|-----|------|-------------|
| **Inventory API** | REST | Manage inventory locations, inventory item records, and offer objects. Recommended for new integrations. |
| **Sell Feed API** | REST | Bulk upload using `LMS_ADD_FIXED_PRICE_ITEM` or `LMS_ADD_ITEM` feed types. |
| **Trading API** | XML | Create listings with `AddItem`, `AddFixedPriceItem`, or up to 5 with `AddItems`. |

---

## API Use Cases

| Use Case | Description |
|----------|-------------|
| Single-SKU listing | Create a single listing for one product |
| Multiple-SKU listing | Create listings with variations (size, color, etc.) |
| Bulk listing creation | Upload many listings at once |
| Catalog-based listings | Create listings using eBay catalog products |
| Magical listing previews | Generate listing previews |

---

## Creating a Single-SKU Listing with Inventory API

> **Recommended**: eBay recommends using the Inventory API for new integrations.

### Required Objects
1. **Location object** - Inventory location
2. **Inventory_item object** - Product details
3. **Offer object** - Listing configuration

### Step-by-Step Flow

#### Step 1: Create Inventory Location
Use `createInventoryLocation` to create the location.

**Key Fields:**
- `merchantLocationKey` - Seller-defined identifier (passed in URI, max 50 chars)
- `locationTypes` - Type of location (WAREHOUSE, STORE, FULFILLMENT_CENTER)

#### Step 2: Create Inventory Item
Use `createOrReplaceInventoryItem` to define the item.

**Key Fields:**

| Field | Description |
|-------|-------------|
| `sku` | Seller-defined stock-keeping unit (path parameter) |
| `product.title` | Listing title |
| `product.description` | Listing description |
| `product.subtitle` | Optional subtitle |
| `product.aspects` | Item specifics as name-value pairs |
| `product.imageUrls` | Array of image URLs (at least one required) |
| `product.videoIds` | Optional array of video IDs |
| `product.epid` | eBay product ID |
| `condition` | Item condition (required in most categories) |
| `conditionDescription` | Description for non-new items |
| `conditionDescriptors` | Info for trading cards (Graded/Ungraded) |
| `availability.shipToLocationAvailability.quantity` | General quantity |
| `availability.availabilityDistributions.quantity` | Location-specific quantity |
| `availability.pickupAtLocationAvailability` | In-store pickup availability |

#### Step 3: Create Offer
Use `createOffer` to define the listing configuration.

**Key Fields:**

| Field | Description |
|-------|-------------|
| `sku` | Links to the inventory item |
| `marketplaceId` | Target eBay marketplace |
| `format` | AUCTION or FIXED_PRICE |
| `merchantLocationKey` | Location of the item |
| `categoryId` | eBay leaf category |
| `secondaryCategoryId` | Optional secondary category |
| `storeCategoryNames` | eBay Store categories (array) |
| `pricingSummary.price` | Fixed-price or Buy It Now price |
| `pricingSummary.auctionStartPrice` | Starting bid for auctions |
| `pricingSummary.auctionReservePrice` | Reserve price for auctions |
| `availableQuantity` | Override quantity from inventory item |
| `listingDescription` | Override description from inventory item |

**Business Policies (Required):**

| Field | Description |
|-------|-------------|
| `listingPolicies.paymentPolicyId` | Payment policy ID |
| `listingPolicies.returnPolicyId` | Return policy ID |
| `listingPolicies.fulfillmentPolicyId` | Fulfillment/shipping policy ID |

---

## Creating a Single-SKU Listing with Trading API

### AddFixedPriceItem
Use for fixed-price listings.

### AddItem
Use for auction-style listings.

### AddItems
Use to create up to 5 listings in one call.

---

## Creating Listings in Bulk

Use the **Sell Feed API** with:
- `LMS_ADD_FIXED_PRICE_ITEM` - For fixed-price listings
- `LMS_ADD_ITEM` - For auction listings

---

## Related Documentation

- [Managing Inventory Locations](sell_managing_inventory_locations.md)
- [Managing Inventory and Offers](sell_managing_inventory_and_offers.md)
- [Business Policies](sell_configuring_seller_accounts.md)
