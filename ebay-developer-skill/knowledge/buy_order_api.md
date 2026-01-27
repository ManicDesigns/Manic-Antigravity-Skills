# Order API

Source: https://developer.ebay.com/api-docs/buy/static/api-order.html

# Order API

 

* [Home](/)
* [Develop](/develop)
* [Guides](/develop/guides)
* [Buying Integration Guide](/develop/guides/buying-ig-landing.html)
* Order API

Buying Integration Guide 

[Buy APIs Overview](buy-overview.html)

[Buy APIs Requirements](buy-requirements.html)

[Browse API](api-browse.html)

[Charity API](api-charity.html)

[Deal API](api-deal.html)

[Feed API](api-feed.html)

[Feed API beta](api-feed_beta.html)

[Marketing API](api-marketing.html)

[Offer API](api-offer.html)

[Order API](#)

[Categories for Buy APIs](buy-categories.html)

[Buy API Support by Marketplace](ref-marketplace-supported.html)

[Buy API Field Filters](ref-buy-browse-filters.html)

**Note:** 
Both the Order API for Guest checkout and the Order API for Member checkout are a [![Limited Icon](/cms/img/docs/partners-api.svg "Limited Release") (Limited Release)](/api-docs/static/versioning.html#Limited). For information on how to obtain access to these APIs in production, see the [Buy APIs Requirements](buy-requirements.html).

The Order API supports both eBay **guest** and eBay **member** checkouts.

* A **guest** checkout is where someone does not sign into the eBay site and you must collect or have all the information needed in order to purchase and ship the item.
* An eBay **member** checkout is where the buyer is logged into eBay and you can use the information from their account to purchase and ship the item.

The basic differences between these checkouts are described in the following table.

| eBay Guest Checkout | eBay Member (signed in) Checkout |
| --- | --- |
| * You will use an oauth application token. For information about this token, see [Get OAuth access tokens](/api-docs/static/oauth-tokens.html). * The buyer pays for items using a credit card, direct debit, or other supported payment method through the **Checkout with eBay** widget. Because all guest payments are handled by the **Checkout with eBay** widget, [Payment Card Industry Data Security Standards (PCI DSS)](https://www.pcisecuritystandards.org/) do not apply to the Guest Checkout flow. * For **guest** checkout, the production resource URI is `https://apix.ebay.com/buy/order/v2`.   For details see, [guest Order API resources](/api-docs/buy/order/resources/methods). | * You will use an oauth user token. For information about this token, see [Get OAuth access tokens](/api-docs/static/oauth-tokens.html). * The buyer uses a credit card saved to their eBay member account to pay for their order. If the buyer does not have a stored credit card, you will need to supply the payment information. To do this, your application **must** comply with [Payment Card Industry Data Security Standards (PCI DSS)](https://www.pcisecuritystandards.org/) to ensure proper handling of sensitive credit card data. * For **member** checkout, the production resource URI is `https://apix.ebay.com/buy/order/v1`.   For details see, [member Order API resources](/api-docs/buy/order_v1/resources/methods). |

## Order API methods overview

The Order API has **checkout\_session**, **purchase\_order**, **guest\_checkout\_session**, and **guest\_purchase\_order** resources to support checkouts for eBay members and eBay guests.

The checkout functionality is described below:

* **Create a checkout session**

  You use the **initiateGuestCheckoutSession** or **initiateCheckoutSession** method to create a checkout session. This is the first step in all checkout flows.
* **Update quantity and shipping method**

  You can change the quantity and/or the shipping method of a specific line item using the **updateGuestQuantity**, and **updateGuestShippingOption** or **updateQuantity**, and**updateShippingOption** methods. This lets your buyer adjust the quantity and gives them
  the ability to have a unique shipping method for each line item. For example, they might pay more to have one item expedited but have the other
  items shipped in a less expensive way.
* **Apply and remove a coupon**

  You can use the **applyGuestCoupon** or **applyCoupon** method to add a coupon to the purchase order. The coupon discount with be applied
  to all the eligible items in the order. You can also remove a coupon from the purchase order with the **removeGuestCoupon** or **removeCoupon**
  method.

  **Note:**[![Limited Icon](/cms/img/docs/partners-api.svg "Limited Release")(Limited Release)](/api-docs/static/versioning.html#Limited)
  You must be white listed to use these methods.
* **Update the shipping address**

  You can change the shipping address using the **updateShippingAddress** and **updateGuestShippingAddress** methods. There can be only one shipping address for a checkout session. But it does not have to be the buyer's address. This gives the buyer the ability to
  purchase items and have them sent to someone else.
* **Update Addon Services Status**

  For **member** checkouts, changes the selection of add-on services for the checkout session. This is not available for **guest** checkout.
* **Update/add payment information**
  + For **guest** checkouts, all payment information is entered through the **Checkout with eBay** widget flow.
    For details, see [Checkout with eBay Button flow](#psb-checkout).
  + For **member** checkouts, you can add/change the payment information any time after the session has started using
    **updatePaymentInfo**. This allows the buyer to change their payment information. The payment information isn't required
    when you initially create the checkout session.
* **Retrieve the checkout session details**

  You can retrieve all the checkout session details using **getGuestCheckoutSession** and **getCheckoutSesson**.
  This gives you the ability to review the order with the buyer and get their approval before creating the purchase order and submitting it for payment.
* **Submit the purchase order for payment**

  + For **member** checkouts, you use the **placeOrder** method to complete the checkout flow. The method creates the purchase order, initiates
    the payment process, and terminates the specified checkout session. The payment process can sometimes take a few minutes. The response often shows that the
    payment for the purchase order is "PENDING".
  + **Guest** checkouts do not have a **placeOrder** method. This is handled by the **Checkout with eBay widget**. For details, see [Checkout with eBay Button flow](#psb-checkout).
* **Check payment status**

  You can retrieve the details of a purchase order using **getGuestPurchaseOrder** and **getPurchaseOrder**. The value returned in the **purchaseOrderPaymentStatus** field shows whether the purchase order has been paid for. If it has been paid for, this field will return `PAID`.
* **Retrieve purchase order details**

  You can retrieve the details, including the shipment tracking information, for a specific purchase order
  using **getGuestPurchaseOrder** and **getPurchaseOrder**.
  This enables you to store a record of this transaction.

  For eBay **member** checkout, the details also include the fields that enable you to use the **Post Order API** to
  handle returns and an cancellations. For more information, see [Handling post
  order tasks](#Post).

### Order API error details

This section provides more information on troubleshooting errors that may occur with the **Order API**.

**Error code 15002 for invalid itemId**

There are several possibilities why an item is not be available for purchase, and the **15002** error code will be triggered.

* The item is out of stock. The buyer will need to track that item to see if seller adds more quantity.
* The listing has ended. The buyer will need to find a similar item in another listing.
* The buyer is an active bidder in an auction, but the auction has not ended yet. The buyer will need to track the auction until it ends, and make higher bids as necessary. The auction item will only be purchasable if the buyer is the winner of the auction.
* The buyer is not the winner of the auction. The buyer will need to find a similar item in another listing.

## Payment flows overview

The Order API supports the following flows:

* The [Order API eBay member payment flow](#order-checkout). This flow is for eBay **members** using the Order API.
* The [Checkout with eBay Button flow](#psb-checkout). This flow is for eBay **guests** using
  the Checkout with eBay button. This flow does not require the Partner to be CPI complaint.

### Order API eBay member payment flow

An eBay member can use this flow to pay for items using a payment method saved to their account, which is passed in using
the **updatePaymentInfo** method.

The following describes the Order API payment flow.

![Order API Member Payment Flow Image](/api-docs/res/Resources/images/buy-ig/order-api-member-payment-flow.png)

1. **Start the checkout session**

   Pass in the item ID, quantity, the Buyer's contact information, and the shipping address.

   If the eBay member wants to use a credit card, pass in the buyer's credit card information.

   This method returns the checkout session ID (**checkoutSessionId**).
2. **Make adjustments to the order**

   Use the update methods to change the quantity of an item, the shipping option of a line item, or the shipping address of the order.

   These methods return the order details.
3. **Review the order**

   Use the **getCheckoutSession** method to pass in the checkout session ID (**checkoutSessionId**).

   This method returns the order details.
4. **Place the order**

   To complete the transaction and retrieve the order details, use the **placeOrder** method and the checkout session ID (**checkoutSessionId**).

   This method returns the purchase order ID and payment status.

### Checkout with eBay Button flow

The **Checkout with eBay** flow is *only* for eBay **guests**. You use the **Checkout with eBay** button to pay for items with a credit card, direct debit, or other supported payment method, without leaving your app or site. This flow does not require [Payment Card Industry Data Security Standards (PCI DSS)](https://www.pcisecuritystandards.org/) compliance.

The **Checkout with eBay** button process is a web flow that requires eBay partners to integrate eBay's client-side
REST `checkout.js` JavaScript into their site. For more details on integrating the JavaScript, see [Integrating the Checkout with eBay button](#Integrat).

The following walks you through the process of having an eBay guest pay using the **Checkout with eBay** button with the **Order** API.

**Note:** For attribution, you must pass the EPN campaign and reference ID in the **EBAY-C-ENDUSERCTX** header in the **initiateCheckoutSession** method. For more information about headers and accepted values, refer to [Request components](/api-docs/static/rest-request-components.html#headers).

![Order API Guest Payment Flow Image](/api-docs/res/Resources/images/buy-ig/order-api-guest-payment-flow.png)

1. **Start the checkout session**

   Pass in the item ID, quantity, the Buyer's contact information, and the shipping address.

   This method returns the checkout session ID (**checkoutSessionId**) and a security token.
2. **Make adjustments and review the order**

   Use the update methods to change the quantity of an item, the shipping option of a line item, or the shipping address of the order.

   These methods return the order details.
3. **Review the order**

   Use the **getGuestCheckoutSession** method to pass in the checkout session ID (**checkoutSessionId**).

   This method returns the order details.
4. **Complete the order using the Checkout with eBay button.**

   Use the **Checkout with eBay** button to let the buyer enter payment information and purchase the item.

* The **security token**, **sessionId**, **paymentActions**, **onSuccess**, affiliate details, **onChange**, **onError** values and any additional data are passed to eBay Checkout.
* The Buyer uses the **Checkout with eBay** button to complete payment.
* The **Checkout with eBay** button passes the values for **purchaseOrderId**, **purchaseStatus**, **checkoutSessionId** .

### Integrating the Checkout with eBay button

The **Checkout with eBay** widget allows eBay guests to pay for items without leaving your site.
To implement the
**Checkout with eBay** payment option, you must include the **Checkout with eBay** Javascript
SDK to your web page.

1. Add the following code:

```json
<body>  
  const script = document.createElement('script');	  
  script.src = 'https://checkout.ebay.com/sdk/js?locale=<locale>&token=<encodedURIComponent(token)>sessionid=<sessionid>';  
  document.body.appendChild(script);  
</body>
```

This adds the necessary scripts to the body of the web page. You will pass the following variables to the script:

| Variable | Type | Description |
| --- | --- | --- |
| **locale** | string | Pass this variable to identify the site content's language. Available options are `en-US` and `de-DE` Default value: `en-US` |
| **token** | string | Used to authenticate your request. You should receive this value from the **Buy** API method that you initially made to create session.  The token must be encoded.  **Occurrence:** Required |
| **sessionid** | string | Used to authenticate your request. You should receive this value from the **Buy** API method that you initially made to create session.  **Occurrence:** Required |

2. Add/Render the **Checkout with eBay** button to your web page. After you have added the **Checkout with eBay** Javascript SDK to your web page, the next step is to initialize JavaScript function that loads the **Checkout with eBay** button.

```json
<body>
	<div id='checkout-with-ebay-container'></div>

	new window.ebaypay.Button({
	    token: <encodedURIComponent(token)>,
	    sessionId: <sessionid>,
	    paymentActions: {
	        onSuccess: (data) => {
	            // your code goes here
	        },
	        onError: (error) => {
	        	// your code goes here
	        }
	        onCancel: (data) => {
	        	// your code goes here
	        }
	    }
	}).render('#checkout-with-ebay-container');
</body>
```

| Variable | Type | Description |
| --- | --- | --- |
| **token** | string | Used to authenticate your request. You receive this value from the**Buy** API method you initially used to create session.  **Occurrence:** Required |
| **sessionid** | string | Used to authenticate your request. You receive this value from the **Buy** API method you initially used to create session.  **Occurrence:** Required |
| **paymentActions** | object | Object variable that contains callbacks upon success (**onSuccess**), cancellation (**onCancel**), and failure (**onError**). |
| **paymentActions.onSuccess** | JavaScript object | A JavaScript object containing two keys, **purchaseOrderId** and **purchaseStatus**. The callback options will pass the data back to you for use when an operation is successful:  **purchaseOrderId**:  **Type:** string  **Value:** purchaseOrderId for this order, created through the purchase order method.  **purchaseStatus**:  **Type:** string  **Value:** one of `"PAID"` or `"PENDING"`  **Example:**   ```json { "purchaseOrderId": "1********7", "purchaseStatus": "PAID" } ``` |
| **paymentActions.onCancel** | JavaScript object | A JavaScript object containing one key, **sessionid**.  The callback options will pass the data back to you for use when an operation is cancelled (e.g., when the user closes the mini-browser or something abrupt happens to close the mini-browser).  **sessionid**:  **Type**: string  **Value:** sessionId created through the checkout session method.  **Example:**   ```json { "sessionid": "1********7" } ``` |
| **paymentActions.onError** | JavaScript exception | The callback options will pass an exception back to you for use when an operation is cancelled (e.g., when something abrupt happens while loading the mini-browser or due to a Javascript exception).  These callback options will pass the error object back to you so you can correct the error.  **error:**  **Type:** A Javascript exception. |

## Handling post order tasks

This section describes how post order (after sales) transactions, such as returns, disputes, cancellations, etc. are handled for eBay **member** and **guest** checkouts.

### For eBay member checkouts

For eBay member checkouts, you can use the **Post Order** API to complete returns or cancellations. The Order API returns the **legacyItemId**, **legacyTransactionId**, and the **legacyOrderId** information. This information can be used with the [Post Order API](/Devzone/post-order/index.html#CallIndex) to create a return request or submit a cancellation request. See [Using the Post Order API](#Using)  for more information.

For post order tasks other than a return or cancellation, the shopper must log into their eBay account. The post order transaction is handled by the seller on the eBay site.

### For eBay guest checkouts

For guest checkouts, all post order transactions are handled on the eBay site. When a shopper purchases items on eBay without signing into eBay, eBay sends the shopper an order confirmation email for each seller. This email contains a **View order details** link. To initiate a post order transaction, the buyer clicks on the link in the email, follows the instructions, and then signs into eBay as a guest using their email address. From there they can contact the seller to report the issue.

## Using the Post Order API

This section describes how you use the **legacyReference** fields returned by the Order API to create return requests and submit cancellation requests using the **Post Order** API. This section describes the following:

* [Understanding the legacyReference fields](#legacyReference)
* [Creating a return request using the Post Order API](#Creating)
* [Submitting a cancellation request using the Post Order API](#Create2)

### Understanding the legacyReference fields

When you place an order, the checkout session is ended and a purchase order is created. So for any order there is only one **checkoutSessionId** and one **purchaseOrderId**. When the purchase order has more than one line item:

* Each item has a unique **lineItemID**, **itemId**, and **legacyItemId**
* Each seller has a unique **legacyOrderId**
* All the items have the same **purchaseOrderId** and **legacyTransactionId**

The following shows a portion of a purchase order response that has two items from different sellers.

```json
{
 "purchaseOrderId": "5********0",
 "purchaseOrderCreationDate": "2016-01-06T19:49:38.000Z",
 "lineItems": [
   {
     "lineItemId": "6********0",
     "itemId": "v1|1********4|0",
     "title": "Lego Marvel Super Heroes",
     "image": {
       "imageUrl": "http://pics.ebaystatic.com..."
     },
     "seller": {
       "username": "m***R"
     },
     "quantity": 1,
     "netPrice": {
       "value": "18.99",
       "currency": "USD"
     },
     "lineItemPaymentStatus": "PAID",
     "lineItemStatus": "PENDING",
     "shippingDetail": {
       "shippingServiceCode": "USPS First Class Package",
       "shippingCarrierCode": "USPS",
       "minEstimatedDeliveryDate": "2016-01-09T08:00:00.000Z",
       "maxEstimatedDeliveryDate": "2016-01-13T08:00:00.000Z"
     },
     "legacyReference": {
       "legacyTransactionId": "9********9",
       "legacyItemId": "1********4",
       "legacyOrderId": "1********4-9********9!5********0"
     }
   }
   {
     "lineItemId": "6********0",
     "itemId": "v1|3********5|0",
     "title": "LEGO Marvel Heroes Doctor Strange",
     "image": {
       "imageUrl": "http://pics.ebaystatic.com..."
     },
     "seller": {
       "username": "t***s"
     },
     "quantity": 1,
     "netPrice": {
       "value": "24.99",
       "currency": "USD"
     },
     "lineItemPaymentStatus": "PAID",
     "lineItemStatus": "PENDING",
     "shippingDetail": {
       "shippingServiceCode": "USPS First Class Package",
       "shippingCarrierCode": "USPS",
       "minEstimatedDeliveryDate": "2016-01-09T08:00:00.000Z",
       "maxEstimatedDeliveryDate": "2016-01-13T08:00:00.000Z"
     },
     "legacyReference": {
       "legacyTransactionId": "9********",
       "legacyItemId": "3********5",
       "legacyOrderId": "3********5-9********9!5********0"
     }
   } ... ]
```

**Note:** The [legacyReference](#legacyReference) fields are returned for both guest and member checkouts. But using the values of these fields with the Post Order API is supported only for eBay **member** checkouts.

### Creating a return request using the Post Order API

The **lineItems.legacyReference.legacyItemId** and **lineItemslegacyReference.legacyTransactionId** fields returned by the Order API **getPurchaseOrder** method are used in the Post Order API **Create Return Request** method to initiate a return. Once the return process is started, you can use the Post Order API to perform all other return tasks required to complete the return process.

The table below, lists the fields required by the Post Order API **Create Return Request** method and the corresponding fields returned by the **getPurchaseOrder** method.

| Post Order API Field | Order API Field | Value Returned by Order API |
| --- | --- | --- |
| `returnRequest.itemId` | `lineItems.legacyReference.legacyItemId` | 3\*\*\*\*\*\*\*\*4 |
| `returnRequest.transactionId` | `lineItems.legacyReference.legacyTransactionId` | 8\*\*\*\*\*\*\*\*4 |

The following shows the **Order API** response and the **Post Order API** [Create Return Request](/Devzone/post-order/post-order_v2_return__post.html) method using the values of the **legacyTransactionId** and **legacyOrderId** fields.

| Order API getPurchaseOrder Method Response | Post Order API Create Return Request |
| --- | --- |
| ```json   "legacyReference" :     {       "legacyItemId" : "3*********4",       "legacyTransactionId" : "8********",       "legacyOrderId" : "3********4-8********4!1********1"     },     ... "purchaseOrderPaymentStatus": "PENDING", ... 	 ``` | ```json POST https://api.ebay.com/post-order/v2/return {   "returnRequest":   {     "itemId": "3********4",     "transactionId": "8********4"   } } ``` |

### Submitting a cancellation request using the Post Order API

The **lineItems.legacyReference.legacyOrderId** field is returned by the Order API **getPurchaseOrder** method and is used in the Post Order API **Submit Cancellation Request** method to initiate a cancellation. Once the cancellation process is started, you can use the Post Order API to perform all other tasks required to complete a cancellation.

The table below, lists the field required by the Post Order API **Submit Cancellation Request** method and the corresponding field returned by the **getPurchaseOrder** method.

| Post Order API Field | Order API Field | Value Returned by Order API |
| --- | --- | --- |
| `legacyOrderId` | `lineItems.legacyReference.legacyOrderId` | `3********4-8********!1********1` |
| `buyerPaid` This is a Post Order boolean field. | `lineItems.purchaseOrderPaymentStatus` | `PENDING` |
| `cancelReason` This is a Post Order API [enum value](/Devzone/post-order/post-order_v2_cancellation__post.html#Request.cancelReason) |  |  |

The following shows the **Order API** response and the **Post Order API** [Submit Cancellation Request](/Devzone/post-order/post-order_v2_cancellation__post.html) method using the values of the **legacyOrderId** and **purchaseOrderPaymentStatus** fields.

| Order API getPurchaseOrder Method Response | Post Order API Create Return Request |
| --- | --- |
| ```json    "legacyReference" :      {        "legacyItemId" : "3********4",        "legacyTransactionId" : "8********4",        "legacyOrderId" : "3********4-8********4!1********1"      },      ... "purchaseOrderPaymentStatus": "PENDING", ... ``` | ```json  POST https://api.ebay.com/post-order/v2/cancellation {   "legacyOrderId": "3********4-8********4!1********1",   "buyerPaid": "false",   "cancelReason":"ORDER_MISTAKE" } ``` |

Related topics

* [Buying Apps](/api-docs/buy/static/buy-landing.html)
* [API Documentation](#)

  [Browse API](/api-docs/buy/browse/overview.html)[Deal API](/api-docs/buy/deal/overview.html)[Feed Beta API](/api-docs/buy/feed/overview.html)[Feed API](/api-docs/buy/feed/v1/overview.html)[Marketing API](/api-docs/buy/marketing/overview.html)[Offer API](/api-docs/buy/offer/overview.html)[Order API](/api-docs/buy/order/overview.html)
* [Guides](/develop/guides)
* [Related Docs](#)

  [Using eBay RESTful APIs](/api-docs/static/ebay-rest-landing.html)[Commerce APIs](/develop/apis/restful-apis/commerce-apis)[Developer APIs](/develop/apis/restful-apis/developer-apis)[Finding API](/devzone/finding/callref/index.html)[Shopping API](/devzone/shopping/docs/callref/index.html)