# eBay Promoted Listings & Marketing Information

This document contains information on eBay's Promoted Listings (PL) and Marketing API.

## Overview

Promoted Listings allow sellers to increase the visibility of their listings by creating ad campaigns. When a listing is promoted, it receives a \"SPONSORED\" badge and may appear in buyer search flows.

There are three primary campaign types:
1. **General Strategy (PLS)**: Uses the Cost Per Sale (CPS) funding model. A Promoted Listings fee is only charged if a buyer purchases the item within 30 days after clicking on the ad. Funding is configured via an ad rate (bid percentage between 2% and 100%).
2. **Priority Strategy (PLA)**: Uses the Cost Per Click (CPC) funding model. Sellers specify a daily budget and bid amount for keywords. Sellers are charged for clicks regardless of whether the item sells. Priority campaigns can surface in slot one of search results.
3. **Promoted Offsite (OA)**: Allows sellers to promote their eBay listings in leading external search channels using a CPC model.

## Program Eligibility

Sellers must be Above Standard or Top Rated. New accounts take a few weeks to become eligible.
- Listings must be fixed-price. Auction listings are not supported for Priority (CPC) campaigns.
- Sellers can check eligibility via the Account API `getAdvertisingEligibility` method. A `SellerEligibilityEnum` indicates if a seller is eligible, or returns reasons like `NOT_ENOUGH_ACTIVITY`, `NOT_IN_GOOD_STANDING`, or `RESTRICTED`.

## Ad Rates and Budgets (Funding Strategy)

When configuring a campaign via `createCampaign`, the `fundingStrategy` object handles fees:
- **Cost Per Sale (CPS):** Set `fundingModel` to `COST_PER_SALE`. Provide `bidPercentage` (ad rate). Ad rates cannot be updated after campaign creation for rules-based campaigns. Ad rates apply at the ad level.
- **Cost Per Click (CPC):** Set `fundingModel` to `COST_PER_CLICK`. Used with `budget` (daily amount) and keywords with bids. Sellers can query suggested maximum CPCs (`suggestMaxCpc` endpoint) or keyword bids (`suggestBids` endpoint).

## API vs UI Comparison

- **Day Level Reporting:** Supported via API.
- **Bulk Requests:** API supports bulk report requests.
- **Transaction Reports:** While campaign performance is viewable in the UI, API gives granular transaction reports with enhanced metrics (separate for PLA and PLS).
- **Search Query Report:** Available in API, not available in the UI for Priority campaigns.

## Campaign Restrictions

- **Limits:** Max 5 active rules-based campaigns, 2,000 active key-based campaigns (CPS). 500 max active manual PLA campaigns and 500 active smart PLA campaigns.
- **Ad creation limits:** 50,000 items/ads per general/priority campaign. Smart targeting is limited to 3,000 listings per campaign.
- **Budgets (PLA):** Min daily budget $1.00 USD, Max $1,000,000 USD. Min CPC bid is $0.02 USD (some category minimums go up to $1.16).
- **Keywords:** Must be < 80 chars. 1,000 keywords per ad group. Exhaustive negative matching available (EXACT match only currently).
