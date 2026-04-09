# Listing Creation V2 & Bulk Guide

This guide outlines the modern (Restful V2) processes for handling complex eBay listing structures, specifically focusing on Multi-SKU products and bulk operations.

## Multi-SKU (Variations) Listings
Instead of relying on the legacy Trading API, modern inventory management organizes variations uses an `inventory_item_group`.

1. **Create Base Inventory Items**:
   Create a specific inventory item (`PUT /sell/inventory/v1/inventory_item/{sku}`) for each variation (e.g., SKU "SHIRT-RED-L", SKU "SHIRT-RED-M"). Each needs distinct product traits (size, color) mapped in the `product.aspects` payload.
2. **Create the Inventory Item Group**:
   Group these distinct SKUs under a single variation banner (`PUT /sell/inventory/v1/inventory_item_group/{inventoryItemGroupKey}`).
   - The payload requires `variantSKUs` specifying all associated SKUs.
   - The group defines the shared product data.
3. **Publish the Group**:
   Once grouped and offers are created for all child SKUs, you cannot arbitrarily publish a single child offer directly; you publish or manage at the Group level for visibility.

## Bulk operations

### 1. Light Bulk (In-Line API)
For slight adjustments (price/quantity) across multiple items simultaneously, use:
- `POST /sell/inventory/v1/bulk_update_price_quantity`

### 2. Heavy Bulk (Sell Feed API)
For high-volume sellers needing to list hundreds to thousands of items via files instead of iterating API calls:
- Use the **Sell Feed API** to upload CSV/XML inventory payloads asynchronously.
- The lifecycle: `createTask` -> `uploadFile` -> `taskStatus` -> `downloadResultFile`
- Useful for massive catalog sync tasks mapped directly from a seller’s warehouse ERP.
