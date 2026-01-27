# Account Management Guide (v2)

Source: https://developer.ebay.com/develop/guides-v2/account-management/account-management-guide

The Account Management APIs allow sellers to define and manage their payment, return, and fulfillment business policies. These business policies can be applied to listings by referencing their IDs in the request payloads.

---

## API Use Cases

| Use Case | Description |
|----------|-------------|
| Managing business policies | Payment, return, fulfillment policies |
| Managing custom policies | Product compliance, take-back policies |
| Managing seller finances | Payouts, transactions, funds |
| Managing shipping rate tables | Domestic and international shipping costs |
| Retrieving subscription/eligibility | Ad eligibility, seller subscriptions |
| Managing sales tax settings | Tax configuration |
| User account calls | Account information |
| Managing opt-in programs | Program enrollment |

---

## Managing Business Policies

### Create Policies

| Policy Type | API Call |
|-------------|----------|
| Fulfillment | `createFulfillmentPolicy` |
| Payment | `createPaymentPolicy` |
| Return | `createReturnPolicy` |

### Retrieve All Policies (by Marketplace)

| Policy Type | API Call |
|-------------|----------|
| Fulfillment | `getFulfillmentPolicies` |
| Payment | `getPaymentPolicies` |
| Return | `getReturnPolicies` |

### Retrieve Policy by Name

| Policy Type | API Call |
|-------------|----------|
| Fulfillment | `getFulfillmentPolicyByName` |
| Payment | `getPaymentPolicyByName` |
| Return | `getReturnPolicyByName` |

### Retrieve Policy by ID

| Policy Type | API Call |
|-------------|----------|
| Fulfillment | `getFulfillmentPolicy` |
| Payment | `getPaymentPolicy` |
| Return | `getReturnPolicy` |

### Update Policies

| Policy Type | API Call |
|-------------|----------|
| Fulfillment | `updateFulfillmentPolicy` |
| Payment | `updatePaymentPolicy` |
| Return | `updateReturnPolicy` |

### Delete Policies

| Policy Type | API Call |
|-------------|----------|
| Fulfillment | `deleteFulfillmentPolicy` |
| Payment | `deletePaymentPolicy` |
| Return | `deleteReturnPolicy` |

### Shipping Discounts (Trading API)

| Operation | API Call |
|-----------|----------|
| Configure/Update | `SetShippingDiscountProfiles` |
| Retrieve | `GetShippingDiscountProfiles` |

---

## Managing Custom Policies

Custom policies include product compliance and take-back policies to meet regulatory requirements.

| Operation | API Call |
|-----------|----------|
| Create | `createCustomPolicy` |
| Get All | `getCustomPolicies` |
| Get by ID | `getCustomPolicy` |
| Update | `updateCustomPolicy` |

---

## Managing Seller Finances

The **Finances API** provides a comprehensive view of financial transactions and payouts.

### Payout Operations

| Operation | API Call | API |
|-----------|----------|-----|
| Get all payouts | `getPayouts` | Finances API |
| Get specific payout | `getPayout` | Finances API |
| Get payout settings | `getPayoutSettings` | Account API v2 |
| Update payout percentage | `updatePayoutPercentage` | Account API v2* |

*Only applicable to sellers based in mainland China.

### Transaction Operations

| Operation | API Call |
|-----------|----------|
| Get transactions | `getTransactions` |
| Get funds summary | `getSellerFundsSummary` |
| Get transfer details | `getTransfer` |
| Get account info | `GetAccount` (Trading API) |

> **EU/UK Compliance Note:** To comply with Strong Customer Authentication (SCA) regulations, specific API calls made on behalf of EU/UK domiciled sellers must include digital signatures.
> - Finances API: All methods
> - Trading API: GetAccount call

---

## Managing Shipping Rate Tables

Shipping rate tables define shipping costs based on buyer location.

| Operation | API Call | API Version |
|-----------|----------|-------------|
| Get all rate tables | `getRateTables` | Account API v1 |
| Get specific rate table | `getRateTable` | Account API v2 |
| Update shipping costs | `updateShippingCost` | Account API v2 |

---

## Related Documentation

- [Configuring Seller Accounts](sell_configuring_seller_accounts.md)
- [Using the Finances API](sell_using_the_finances_api.md)
- [Business Policies in Listing Creation](guide_listing_creation_v2.md)
