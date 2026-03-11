# Marketing Performance & Analytics Reports

Reporting for Promoted Listings and overall store traffic spans the Marketing API (for Ad Reports) and the Analytics API (for Traffic Reports).

## Promoted Listings Reports (Marketing API)

Reports are generated asynchronously using the `createReportTask` method. Once `reportTaskStatus` hits `SUCCESS`, the report is retrievable via `getReportTask(s)`. If a report hits the 1,000,000 record threshold, it will `FAILED`. Limit dates or partition requests by campaign IDs to resolve.
Timeframes use ISO 8601 formatting (e.g., `2021-03-15T13:00:00-07:00`).

### Supported Ad Report Types:
- **Account Performance Report**: Summary of daily performance across all campaigns.
- **Campaign Performance Summary Report**: Campaign-level daily performance metrics. Requires `dimensionKeys` of `campaign_id` and `day`.
- **Campaign Performance Report (Item-level)**: Item-level performance. Highly granular. Requires `campaign_id` and `listing_id` dimensions. Priority campaigns also require `ad_group_id`.
- **Listing Performance Report**: Retrieves statistics based directly on Listing IDs.
- **Transaction Report**: Granular transaction specifics. Generation requests must be separated out by funding strategy (CPS vs CPC). Differentiates between \"Direct Sales\" vs \"Halo Item sales\" for Priority.

### Notes on Metrics:
- Click-Through Rate (CTR).
- Search Query Reports are available via API but not in the standard eBay UI dashboards. Reports can also be generated in bulk across accounts.

---

## Traffic Reports (Analytics API)

Traffic Reports provide holistic store data including clicks, views, follow data (from organic and offsite traffic, etc). The endpoint is `/sell/analytics/v1/traffic_report`.

You must URL-encode array filters like `{}` and `[]`.

### Generating by Date Range
- Set `dimension=DAY`
- Set filter `marketplace_ids:{EBAY_US},date_range:[YYYYMMDD..YYYYMMDD]`
- Use the `metric` parameter for values (comma-separated).

### Generating by Listings
- Set `dimension=LISTING`
- Filter using `listing_ids:{1234|5678|9012},date_range:[YYYYMMDD..YYYYMMDD]`
- Provide the `sort` parameter to sort records based on a specific metric (e.g., `sort=LISTING_IMPRESSION_TOTAL`).
- The `TRANSACTION` metric can only be sorted descending.

### Traffic Report Metrics
- `CLICK_THROUGH_RATE`: Item clicks from search results page divided by displays.
- `LISTING_IMPRESSION_SEARCH_RESULTS_PAGE`: Times items appeared on search result pages.
- `LISTING_IMPRESSION_STORE`: Times items appeared on seller's store.
- `LISTING_IMPRESSION_TOTAL`: Search results + Store impressions.
- `TOTAL_IMPRESSION_TOTAL`: Impressions across ANY page or flow, equivalent to the Seller Hub traffic page value.
- `LISTING_VIEWS_SOURCE_DIRECT`: Views from bookmarks/direct URLs.
- `LISTING_VIEWS_SOURCE_OFF_EBAY`: Views from non-eBay referrers (search engines).
- `LISTING_VIEWS_SOURCE_OTHER_EBAY`: Non-search, non-store eBay views.
- `LISTING_VIEWS_SOURCE_SEARCH_RESULTS_PAGE`: Search result page views.
- `LISTING_VIEWS_TOTAL`: Sum of all view sources.
- `SALES_CONVERSION_RATE`: Transactions / Total Listing Views (Cannot be sorted).
- `TRANSACTION`: Total number of completed transactions.

The response object returns an array in `records` featuring `dimensionValues` (e.g., the day or the listing) and `metricValues` that map equivalently to the requested `header.metrics` payload keys.
