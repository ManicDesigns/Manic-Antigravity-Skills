# Order Management Guide (v2)

Source: https://developer.ebay.com/develop/guides-v2/order-management/order-management-guide

The Order Management APIs provide sellers with the ability to handle various aspects of the order management process, including retrieving order details, updating order statuses, managing shipping and tracking information, handling INR inquiries, order cancellations, and item returns.

---

## API Use Cases

| Use Case | Description |
|----------|-------------|
| Retrieving and fulfilling orders | Get order details and mark as shipped |
| Managing order cancellations | Handle buyer/seller cancellation requests |
| Managing INR inquiries | Handle Item Not Received cases |
| Managing returns | Process item returns |
| Managing payment disputes | Handle payment dispute cases |

---

## Retrieving and Fulfilling Orders

### Using Fulfillment API (REST - Recommended)

The **Fulfillment API** allows sellers to efficiently manage order fulfillment.

#### Retrieve Orders

| Operation | API Call | Description |
|-----------|----------|-------------|
| Get single order | `getOrder` | Retrieve specific order by ID |
| Get multiple orders | `getOrders` | Retrieve by IDs, date range, or status |

#### Key Response Fields

| Field | Path | Description |
|-------|------|-------------|
| Line item quantity | `lineItems.quantity` | Number of items ordered |
| Shipping address | `fulfillmentStartInstructions.shippingStep.shipTo` | Buyer's address |
| Carrier code | `fulfillmentStartInstructions.shippingStep.shippingCarrierCode` | Selected carrier |
| Shipping service | `fulfillmentStartInstructions.shippingStep.shippingServiceCode` | Selected service |
| Max delivery date | `fulfillmentStartInstructions.maxEstimatedDeliveryDate` | Latest expected delivery |
| Min delivery date | `fulfillmentStartInstructions.minEstimatedDeliveryDate` | Earliest expected delivery |
| Ship-by date | `lineItems.lineItemFulfillmentInstructions.shipByDate` | Required ship date |
| Order total | `pricingSummary.total` | Total order cost |
| Delivery cost | `pricingSummary.deliveryCost` | Shipping cost |
| Tax amount | `pricingSummary.tax` | Tax collected |
| Fulfillment status | `orderFulfillmentStatus` | Current status (e.g., FULFILLED) |

#### Mark Order as Shipped

| Scenario | Action |
|----------|--------|
| eBay shipping label purchased | eBay automatically marks as fulfilled with tracking |
| External shipping | Use `createShippingFulfillment` to mark shipped and add tracking |

#### Shipping Fulfillment Operations

| Operation | API Call |
|-----------|----------|
| Create fulfillment | `createShippingFulfillment` - Assign line items to package + tracking |
| Get fulfillment | `getShippingFulfillment` - Details for specific package |
| Get all fulfillments | `getShippingFulfillments` - All packages in order |

> **Note:** Call `createShippingFulfillment` for each package in an order.

---

### Using Trading API (XML - Legacy)

#### Retrieve Orders

| Operation | API Call |
|-----------|----------|
| Get orders | `GetOrders` |
| Get seller transactions | `GetSellerTransactions` |
| Get item transactions | `GetItemTransactions` |

#### Key Response Fields

| Field | Path | Description |
|-------|------|-------------|
| Quantity | `TransactionArray.Transaction.QuantityPurchased` | Items ordered |
| Address | `Order.ShippingAddress` | Buyer's address |
| Shipping service | `ShippingServiceSelected.ShippingService` | Selected service |
| Order total | `Order.Total` | Total cost |
| Shipping cost | `Transaction.ShippingServiceSelected.ShippingServiceCost` | Shipping cost |
| Tax | `Transaction.Taxes` | Tax amount |
| Order status | `Order.OrderStatus` | Fulfillment status |

#### Post-Sale Operations

| Operation | API Call | Description |
|-----------|----------|-------------|
| Mark shipped/paid | `CompleteSale` | Update order status, add tracking |
| Send invoice | `SendInvoice` | Email invoice reminder to buyer |
| Combine orders | `AddOrder` | Combine unpaid line items into one order |

---

## Downloading USPS Shipping Labels (Logistics API)

> **Note:** The Logistics API is **restricted** and only accessible to approved eBay partners. Supports domestic US shipping with USPS only.

### Label Download Flow

1. **Get shipping quotes**: Use `createShippingQuote`
   - Required: `shipFrom`, `shipTo`, `packageSpecification`
   
2. **Select quote and create label**: Use `createFromShippingQuote`
   - Pass `shippingQuoteId` and `rateId` from step 1
   
3. **Download label**: Use `downloadLabelFile`
   - Pass `shipmentId` from step 2
   - Returns PDF of shipping label

---

## Managing Order Cancellations

Handle buyer-initiated and seller-initiated cancellation requests.

---

## Managing Item Not Received (INR) Inquiries

Handle cases where buyers report items not received.

---

## Managing Returns

Process buyer return requests and refunds.

---

## Managing Payment Disputes

Handle chargeback and payment dispute cases.

---

## Related Documentation

- [Handling Orders](sell_handling_orders.md)
- [Using the Finances API](sell_using_the_finances_api.md)
- [Fulfillment API Overview](https://developer.ebay.com/api-docs/sell/fulfillment/overview.html)
