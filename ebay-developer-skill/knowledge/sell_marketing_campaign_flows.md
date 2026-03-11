# eBay Promoted Listings Campaign Flows

This document details how to create and manage the various campaign structures available through the eBay Marketing API. Ads are associated with a single running campaign.

## 1. General Strategy Campaigns (Cost Per Sale)

General strategy campaigns can be Rules-Based or Key-Based.

### Rules-Based Campaigns
1. **Configure Campaign** (`createCampaign`): Use `COST_PER_SALE` and set a `bidPercentage`. Ad rates cannot be changed after campaign creation for rules-based campaigns. 
2. **Add Items by Rule**: Configure `campaignCriterion.selectionRules` with up to ten rule sets. Rules can match listings based on:
   - `brands`
   - `categoryIds`
   - `listingConditionIds` (e.g., 1000 for New, 3000 for Used)
   - `minPrice` / `maxPrice`
   eBay will automatically add any listings matching these conditions to the campaign.

### Key-Based Campaigns
1. **Create Campaign** (`createCampaign`): Configured identically, using `COST_PER_SALE` and optionally `bidPercentage`.
2. **Add Ads Explicitly**: Call `createAdByListingId` or `bulkCreateAdsByListingId` passing the `campaign_id` and the listing to add. You can override the `bidPercentage` at the individual ad level during creation. Limit: 50,000 listings per campaign. To modify an ad's bid, use the `updateBid` method.

## 2. Priority Strategy Campaigns (Cost Per Click)

Priority campaigns can use Manual Targeting or Smart Targeting.

### Manual Targeting Campaigns
1. **Create Campaign** (`createCampaign`): Use `COST_PER_CLICK` funding model. Set daily `budget`.
2. **Create Ad Group**: Organize items logically if necessary.
3. **Add Items**: Use `createAdByListingId` with the `adGroupId`.
4. **Create Keywords**: Use `createKeyword` indicating the `matchType` (`EXACT`, `PHRASE`, `BROAD`) and the text, to the `adGroupId`. Provide a bid amount.
5. **Negative Keywords**: Explicitly disqualify search terms via `createNegativeKeyword` using `EXACT` match.

*Note: Quick Setup methods are deprecated and will be decommissioned by March 2026.*

### Smart Targeting Campaigns
1. **Create Campaign** (`createCampaign`): Use `SMART` for `campaignTargetingType`. Fund via `COST_PER_CLICK`. Sellers can define `bidPreferences.maxCpc` (Maximum Cost Per Click) to limit the amount eBay automatically bids on their behalf. Set daily `budget`.
2. **Add Listings**: Use `createAdByListingId` or `bulkCreateAdsByListingId`. Limit: 3,000 listings. eBay fully automates the keyword generation and bidding processes underneath the hood.

## 3. Promoted Offsite Campaigns
1. **Eligibility Check**: Confirm using `getAdvertisingEligibility`.
2. **Retrieve Budget**: Optionally use `suggestBudget` endpoint.
3. **Create Campaign** (`createCampaign`): Provide `"OFF_SITE"` under the `channels` array. Define the daily budget. The funding model is `COST_PER_CLICK`. Only one offsite campaign per seller is supported at an account level.
