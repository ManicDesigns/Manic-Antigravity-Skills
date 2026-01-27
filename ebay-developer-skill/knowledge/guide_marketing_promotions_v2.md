# Marketing and Promotions Guide (v2)

Source: https://developer.ebay.com/develop/guides-v2/marketing-and-promotions/marketing-and-promotions-guide

The Marketing API allows sellers to create and manage Promoted Listings campaigns, discounts, and store email campaigns to increase visibility and sales.

---

## API Use Cases

| Use Case | Description |
|----------|-------------|
| Promoted Listings - General Strategy | CPS (Cost Per Sale) campaigns |
| Promoted Listings - Priority Strategy | Priority placement campaigns |
| Promoted Offsite | External advertising campaigns |
| Promoted Listings Reports | Campaign performance reporting |
| Discounts | Item-level and order-level discounts |
| Store Email Campaigns | Email marketing to store subscribers |

---

## Promoted Listings: General Strategy Campaigns

General strategy campaigns use the **Cost Per Sale (CPS)** funding model. eBay's Recommendation API can suggest which listings will perform best.

### Campaign Types

| Type | Description |
|------|-------------|
| **Key-based** | Manually add specific listings to campaign |
| **Rules-based** | Auto-add listings matching defined criteria |

### Creating a General Strategy Campaign

#### Step 1: Create Campaign Structure

Use `createCampaign` with required fields:

| Field | Description |
|-------|-------------|
| `marketplaceId` | Target marketplace |
| `campaignName` | Name for the campaign |
| `startDate` | Campaign start date |

#### Step 2: Configure Funding Strategy

| Field | Required | Description |
|-------|----------|-------------|
| `fundingStrategy.bidPercentage` | Yes | Ad rate percentage |
| `fundingStrategy.fundingModel` | Yes | Set to `COST_PER_SALE` |
| `fundingStrategy.adRateStrategy` | No | Optional strategy settings |

#### Step 3: Add Listings

**For Key-Based Campaigns:**

| API Call | Description |
|----------|-------------|
| `bulkCreateAdsByListingId` | Add multiple listings by listing ID |
| `createAdByListingId` | Add single listing by listing ID |
| `bulkCreateAdsByInventoryReference` | Add multiple by Inventory API SKU |
| `createAdByInventoryReference` | Add single by Inventory API SKU |

**For Rules-Based Campaigns:**

Use `selectionRules` criteria:

| Criteria | Description |
|----------|-------------|
| `brands` | Array of brand names |
| `categoryIds` | eBay leaf or store category IDs |
| `listingConditionIds` | Item condition IDs |
| `minPrice` / `maxPrice` | Price thresholds |

> **Tip:** Set `autoSelectFutureInventory: true` to auto-add future matching listings.

### Recommendation API Integration

Use `findListingRecommendations` to get:
- Suggested listings for campaigns
- Trending bid percentages

---

## Promoted Listings: Priority Strategy Campaigns

Priority strategy campaigns provide enhanced placement for higher visibility.

---

## Promoted Offsite Campaigns

Advertise eBay listings on external platforms and websites.

---

## Creating and Retrieving Reports

### Promoted Listings Reports

Track campaign performance metrics.

### Promoted Offsite Reports

Track external advertising performance.

---

## Managing Discounts

Create item promotions and discounts to drive sales.

### Discount Types

| Type | Description |
|------|-------------|
| **Item-level** | Discounts on specific items |
| **Order-level** | Discounts based on order total/quantity |

### Discount Reports

Track discount effectiveness and usage.

---

## Store Email Campaigns

eBay Store owners can send email campaigns to store subscribers.

### Campaign Management

Create, schedule, and send email campaigns to promote listings and sales.

---

## Related Documentation

- [Marketing API Overview](sell_marketing_api_overview.md)
- [Marketing and Discounts](marketing_and_discounts.md)
- [Marketing Seller Inventory](sell_marketing_seller_inventory.md)
- [Recommendation API Overview](sell_recommendation_api_overview.md)
