# Apple In-App Purchase (StoreKit)

> **Source**: https://developer.apple.com/in-app-purchase/

## Overview

In-App Purchase (IAP) enables selling digital products within your app. Apple handles payment processing, taxes, and fraud detection.

---

## IAP Types

| Type | Description | Example |
|------|-------------|---------|
| **Consumable** | Can be purchased multiple times | Coins, gems, lives |
| **Non-Consumable** | One-time unlock, permanent | Premium unlock, remove ads |
| **Auto-Renewable Subscription** | Recurring billing | Monthly/yearly plans |
| **Non-Renewing Subscription** | Fixed duration, no auto-renew | Season pass |

---

## StoreKit 2 (Recommended)

### Setup in React Native

```bash
npm install react-native-iap
cd ios && pod install
```

### Basic Usage

```typescript
import * as IAP from 'react-native-iap';

// Initialize
await IAP.initConnection();

// Get products
const products = await IAP.getProducts({
  skus: ['premium_monthly', 'premium_yearly']
});

// Purchase
const purchase = await IAP.requestPurchase({
  sku: 'premium_monthly'
});

// Verify and finish
await IAP.finishTransaction({ purchase });
```

### Subscription Example

```typescript
const subscriptions = await IAP.getSubscriptions({
  skus: ['premium_monthly', 'premium_yearly']
});

// Current active subscriptions
const available = await IAP.getAvailablePurchases();
const hasActiveSubscription = available.some(
  p => p.productId === 'premium_monthly' || p.productId === 'premium_yearly'
);
```

---

## App Store Connect Setup

### 1. Create Product
1. App Store Connect → Your App → In-App Purchases
2. Click (+) to create product
3. Choose type (Consumable, Non-Consumable, Subscription)
4. Fill in:
   - Reference Name (internal)
   - Product ID (e.g., `com.company.app.premium`)
   - Price tier
   - Display name and description

### 2. Subscription Groups
- Group related subscription tiers
- Users can upgrade/downgrade within group
- Only one active subscription per group

### 3. Sandbox Testing
- Create sandbox tester accounts in App Store Connect
- Sign out of App Store on device
- Use sandbox account when prompted during purchase

---

## Subscription Offers

### Introductory Offers
- Free trial (e.g., 7-day free)
- Pay-as-you-go (reduced price for X periods)
- Pay up front (discounted single payment)

```typescript
// Check eligibility
const eligible = await IAP.isEligibleForIntroOffer('premium_monthly');
```

### Promotional Offers
- For existing/lapsed subscribers
- Requires server signature
- Great for win-back campaigns

### Offer Codes
- Generate in App Store Connect
- Distribute via marketing channels
- Users redeem on device

---

## Server-Side Verification

### Receipt Validation
Always validate receipts server-side to prevent fraud.

```typescript
// Send receipt to your server
const receiptData = await IAP.getReceiptIOS();
const response = await fetch('/api/verify-receipt', {
  method: 'POST',
  body: JSON.stringify({ receipt: receiptData })
});
```

### App Store Server Notifications
Configure webhook in App Store Connect for:
- Initial purchase
- Subscription renewal
- Cancellation
- Refund
- Grace period events

---

## Best Practices

### UI
- [ ] Clear pricing before purchase
- [ ] Explain subscription terms (billing cycle, free trial length)
- [ ] Restore purchases button (required)
- [ ] Manage subscriptions link

### Technical
- [ ] Always finish transactions
- [ ] Implement receipt validation
- [ ] Handle interrupted purchases
- [ ] Support restore purchases
- [ ] Test with sandbox accounts

### Compliance
- [ ] No external payment prompts for digital goods
- [ ] Children's apps: parental gate for purchases
- [ ] Clear cancellation instructions

---

## Restore Purchases

**Required** for non-consumable and subscription apps:

```typescript
const handleRestore = async () => {
  try {
    const purchases = await IAP.getAvailablePurchases();
    // Unlock features based on restored purchases
    for (const purchase of purchases) {
      if (purchase.productId === 'premium_unlock') {
        // Unlock premium features
      }
    }
  } catch (error) {
    console.error('Restore failed:', error);
  }
};
```

---

## Resources
- StoreKit Documentation: https://developer.apple.com/documentation/storekit
- In-App Purchase Overview: https://developer.apple.com/in-app-purchase/
- react-native-iap: https://github.com/dooboolab/react-native-iap
