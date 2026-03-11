# eBay Commerce Taxonomy API Reference

The Taxonomy API helps you discover the most appropriate eBay categories for inventory items, discover the required and recommended item aspects for a category, and retrieve mapping for expired categories. This API is essential for building a robust listing flow to ensure items are not rejected for missing specifics or invalid categories.

## Overview & Use Cases

1. **Discover a category to use for a listing or promotion**: Before creating an eBay listing, find the best category match for an item. The API will also return the required item aspects (like Brand, Color, Size).
2. **Discover categories for buyers to browse**: Present the full category tree hierarchy to buyers to narrow down their search.
3. **Retrieve category mappings for expired categories**: Keep listings up to date by mapping expired an category to its active replacement.

## Key API Methods References

### `getDefaultCategoryTreeId`

- **Endpoint**: `GET /commerce/taxonomy/v1/get_default_category_tree_id?marketplace_id={marketplace_id}`
- **Usage**: Used to get the root tree version and id for a specific marketplace (e.g. `EBAY_US`).

### `getCategoryTree` & `getCategorySubtree`

- **Endpoint (Tree)**: `GET /commerce/taxonomy/v1/category_tree/{category_tree_id}`
- **Endpoint (Subtree)**: `GET /commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_subtree?category_id={category_id}`
- **Usage**: Retrieve the hierarchy of categories. `getCategoryTree` can return a very large payload, so gzip compression (`Accept-Encoding: gzip`) is highly recommended.

### `getCategorySuggestions`

- **Endpoint**: `GET /commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_suggestions?q={keyword}`
- **Usage**: Pass a keyword string (e.g., "iphone 14 pro max") to get suggested leaf categories based on eBay's classification algorithm.

### `getItemAspectsForCategory` & `fetchItemAspects`

- **Endpoint (Single)**: `GET /commerce/taxonomy/v1/category_tree/{category_tree_id}/get_item_aspects_for_category?category_id={category_id}`
- **Endpoint (Bulk)**: `GET /commerce/taxonomy/v1/category_tree/{category_tree_id}/fetch_item_aspects`
- **Usage**: Retrieve the item specifics required for a category.
- **Important Notes**:
  - `fetchItemAspects` returns a massive payload (over 100MB compressed). It will return a payload as a gzipped JSON file sent as a binary file (content-type: `application/octet-stream`).
  - To understand specifics constraints, inspect the `aspectConstraint` fields in the response. Key properties include `aspectRequired` (bool), `aspectDataType` (e.g. `STRING`, `NUMBER`), `aspectFormat` (e.g. `YYYY`, `int32`), and `itemToAspectCardinality` (`SINGLE` or `MULTI`).

### `getExpiredCategories`

- **Endpoint**: `GET /commerce/taxonomy/v1/category_tree/{category_tree_id}/get_expired_categories`
- **Usage**: Find the replacement category ID for an expired category ID.

## Integration Guide: Validating Item Specifics

To properly construct a listing payload (for either Trading API's `AddItem` or Inventory API's `createOffer`), you should ensure the listing satisfies the category's aspect constraints:

1. **Find Category**: Call `getCategorySuggestions` with the item title/keywords. Select the top resulting `categoryId`.
2. **Get Aspects**: Call `getItemAspectsForCategory` with the selected `categoryId`.
3. **Validate Rules**:
   - Filter aspects where `aspectConstraint.aspectRequired == true`. These **MUST** be supplied.
   - For each aspect, display/use the allowed values from `aspectValues` if available.
   - Enforce data types and formats using `aspectConstraint.aspectDataType` and `aspectConstraint.aspectFormat`.
4. **Build Specifics Payload**: Iterate through collected specifics and format them according to the target API requirements (e.g. `Product.aspects` for Inventory API, or `ItemSpecifics.NameValueList` for Trading API).

## Definitions & OpenAPI Specs

For the full schema, errors, and granular details, refer to the OpenAPI v3 definition files provided by eBay:

- YAML: `G:\Antigravity\Projects\Skills\zOther Example Files\Ebay Api\commerce_taxonomy_v1_oas3.yaml`
- JSON: `G:\Antigravity\Projects\Skills\zOther Example Files\Ebay Api\commerce_taxonomy_v1_oas3.json`
