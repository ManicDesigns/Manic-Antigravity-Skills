# Marketing & Discounts Guide

## Overview
eBay's Marketing APIs allow sellers to create promotions, manage ad campaigns, and offer discounts to buyers. This guide focuses on the `Sell Marketing API`.

## Key Concepts

### 1. Promotions
Promotions act as discounts for buyers. Common types include:
- **Codeless Coupons**: Link-based discounts sent to specific buyers.
- **Volume Pricing**: "Buy 2, save 10%".
- **Markdown Events**: Strikes through the price (e.g., $100 -> $80).
- **Order Discounts**: "Spend $50, get $10 off".

#### Creating a Promotion (Discount)
Use the `POST /sell/marketing/v1/promotion_manager/promotion` endpoint.

**Example Payload (Volume Pricing)**:
```json
{
  "promotionName": "BuyMoreSaveMore",
  "promotionStatus": "SCHEDULED",
  "promotionType": "VOLUME_PRICING",
  "startDate": "2025-01-01T00:00:00.000Z",
  "endDate": "2025-02-01T00:00:00.000Z",
  "marketplaceId": "EBAY_US",
  "discountRules": [
    {
      "discountBenefit": {
        "percentageOffOrder": "10"
      },
      "discountSpecification": {
        "minQuantity": 2
      }
    }
  ],
  "inventoryCriterion": {
    "inventoryCriterionType": "INVENTORY_BY_RULE",
    "listingIds": ["123456789012"]
  }
}
```

### 2. Promoted Listings (Ad Campaigns)
These are paid ads to boost visibility.
- **Standard**: Pay only on sale (CPA).
- **Advanced**: Cost-Per-Click (CPC) with keyword targeting.

#### Creating a Campaign
Use `POST /sell/marketing/v1/ad_campaign`.

**Example Payload**:
```json
{
  "campaignName": "Spring Sale Ads",
  "campaignStatus": "RUNNING",
  "marketplaceId": "EBAY_US",
  "fundingStrategy": {
    "bidPercentage": "5.0", // 5% ad rate
    "fundingModel": "COST_PER_SALE"
  },
  "startDate": "2025-03-01T00:00:00.000Z"
}
```

## Best Practices
- **Testing**: Use the Sandbox to create promotions. Note that ad visibility logic might not fully simulate Live ranking.
- **Compliance**: Ensure discounts are genuine. Do not mark up prices just to mark them down.
- **Analytics**: Use `sell_analytics_api_overview.md` to track conversion rates of your campaigns.
