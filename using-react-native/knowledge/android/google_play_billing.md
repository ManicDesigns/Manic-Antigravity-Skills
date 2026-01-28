# Google Play Billing (In-App Purchases)

> **Source**: https://developer.android.com/google/play/billing

## Overview

Google Play's billing system enables selling digital products and subscriptions in Android apps. Required for all digital goods sold on Play Store.

---

## Product Types

| Type | Description | Example |
|------|-------------|---------|
| **One-time products** | Single purchase | Premium unlock, remove ads |
| **Consumables** | Can be re-purchased | Coins, gems, credits |
| **Subscriptions** | Recurring billing | Monthly/yearly plans |

---

## Play Console Setup

### 1. Create Products
1. Google Play Console → Your App → Monetize
2. Products → Create Product
3. Fill in:
   - Product ID (e.g., `premium_unlock`)
   - Name and description
   - Price

### 2. Create Subscriptions
1. Monetize → Subscriptions
2. Create base plan and offers
3. Configure trial periods, introductory pricing

---

## React Native Implementation

### Installation

```bash
npm install react-native-iap
```

### Initialize

```typescript
import * as IAP from 'react-native-iap';

// Products to fetch
const productIds = ['premium_unlock', 'coins_100'];
const subscriptionIds = ['premium_monthly', 'premium_yearly'];

async function initIAP() {
  try {
    await IAP.initConnection();
    
    // Fetch products
    const products = await IAP.getProducts({ skus: productIds });
    const subscriptions = await IAP.getSubscriptions({ skus: subscriptionIds });
    
    console.log('Products:', products);
    console.log('Subscriptions:', subscriptions);
  } catch (error) {
    console.error('IAP init failed:', error);
  }
}
```

### Purchase Flow

```typescript
import * as IAP from 'react-native-iap';

async function purchaseProduct(productId: string) {
  try {
    // Request purchase
    await IAP.requestPurchase({
      skus: [productId],
      andDangerouslyFinishTransactionAutomaticallyIOS: false,
    });
  } catch (error) {
    if (error.code === 'E_USER_CANCELLED') {
      console.log('User cancelled');
    } else {
      console.error('Purchase failed:', error);
    }
  }
}

// Listen for purchase updates
useEffect(() => {
  const purchaseListener = IAP.purchaseUpdatedListener((purchase) => {
    const receipt = purchase.transactionReceipt;
    
    if (receipt) {
      // Verify on your server
      verifyPurchaseOnServer(receipt).then(() => {
        // Acknowledge/finish the purchase
        IAP.finishTransaction({ purchase });
      });
    }
  });

  const errorListener = IAP.purchaseErrorListener((error) => {
    console.error('Purchase error:', error);
  });

  return () => {
    purchaseListener.remove();
    errorListener.remove();
  };
}, []);
```

### Subscription Purchase

```typescript
async function purchaseSubscription(productId: string, offerToken: string) {
  try {
    await IAP.requestSubscription({
      sku: productId,
      subscriptionOffers: [{ sku: productId, offerToken }],
    });
  } catch (error) {
    console.error('Subscription purchase failed:', error);
  }
}
```

---

## Acknowledging Purchases

**Critical**: All purchases must be acknowledged within 3 days or they will be refunded.

```typescript
// Acknowledge after server verification
await IAP.acknowledgePurchaseAndroid({
  token: purchase.purchaseToken,
});

// Or consume for consumables
await IAP.consumePurchaseAndroid({
  token: purchase.purchaseToken,
});
```

---

## Subscription Management

### Check Active Subscriptions

```typescript
async function getActiveSubscriptions() {
  try {
    const purchases = await IAP.getAvailablePurchases();
    return purchases.filter(p => 
      p.productId === 'premium_monthly' || 
      p.productId === 'premium_yearly'
    );
  } catch (error) {
    console.error('Failed to get subscriptions:', error);
    return [];
  }
}
```

### Cancel Subscription
Direct users to Play Store subscription management:

```typescript
import { Linking } from 'react-native';

function openSubscriptionManagement() {
  Linking.openURL(
    'https://play.google.com/store/account/subscriptions'
  );
}
```

---

## Server-Side Verification

### Verify Purchase

```typescript
async function verifyPurchaseOnServer(purchase) {
  const response = await fetch('/api/verify-purchase', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      packageName: 'com.your.app',
      productId: purchase.productId,
      purchaseToken: purchase.purchaseToken,
      platform: 'android',
    }),
  });
  
  return response.json();
}
```

### Real-Time Developer Notifications (RTDN)
Set up Pub/Sub notifications for:
- Subscription renewals
- Cancellations, pauses, resumes
- Account holds
- Grace periods

---

## Testing

### Test Accounts
1. Play Console → Settings → License testing
2. Add Gmail addresses
3. Testers use real purchase flow with test cards

### Test Cards
- "Test card, always approves"
- "Test card, always declines"
- "Test card, slow decline"

---

## Grace Period & Account Hold

### Grace Period
- User's payment fails
- Subscription continues 3-30 days
- Handle: `purchaseState === PENDING`

### Account Hold
- After grace period
- Subscription paused
- Block premium features

```typescript
function checkSubscriptionState(purchase) {
  if (purchase.isAcknowledgedAndroid && purchase.purchaseStateAndroid === 1) {
    return 'active';
  } else if (purchase.purchaseStateAndroid === 2) {
    return 'pending'; // Grace period
  } else if (purchase.purchaseStateAndroid === 4) {
    return 'on_hold';
  }
  return 'inactive';
}
```

---

## Best Practices

- [x] Verify all purchases server-side
- [x] Acknowledge/consume within 3 days
- [x] Handle network failures gracefully
- [x] Support subscription restore
- [x] Show clear pricing before purchase
- [x] Implement subscription status checks
- [x] Handle pending purchases (slow cards)

---

## Resources
- Play Billing: https://developer.android.com/google/play/billing
- Testing: https://developer.android.com/google/play/billing/test
- react-native-iap: https://github.com/dooboolab/react-native-iap
