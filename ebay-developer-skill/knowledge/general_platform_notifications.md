# Platform Notifications

Source: https://developer.ebay.com/api-docs/static/platform-notifications-landing.html

# Platform Notifications

 

* [Home](/)
* [Develop](/develop)
* [Guides](/develop/guides)
* Platform Notifications

Platform Notifications Guide 

[Auction/Sale Related Notifications](pn_ask-seller-question.html)

[eBay Buyer Protection Notifications](pn_ebay-buyer-protection.html)

[eBay Managed Returns Notifications](pn_return-closed.html)

[Feedback Related Notifications](pn_feedback.html)

[Informational Alerts](pn_account-activity.html)

[Item Related Notifications](pn_item-added-to-watch-list.html)

[Deprecated Events](pn_deprecated-events.html)

Platform notifications are triggered by events on the eBay site, such as the ending of a listing or the creation of a transaction. Notifications are Simple Object Access Protocol (SOAP) messages about events on the eBay site that are sent to subscribing applications.

You subscribe to notifications by setting your application's platform notification preferences which tell eBay for which events you want notifications, and the URLs to which you want the notifications delivered. Once you're subscribed, eBay Platform Notifications asynchronously pushes the notifications to your delivery location.

Subscribing to notifications is a good way to reduce the number of times your application has to execute transaction retrieval, feedback, and other routine API calls. Notifications do not count as API calls, and do not count against your daily API call limit.

You should use API calls to confirm the data received using notifications. For example, if you have subscribed to the [AuctionCheckoutComplete](pn_auction-checkout-complete.html) notification, verify that you have also configured the periodic polling of [GetOrders](/devzone/XML/docs/Reference/eBay/GetOrders.html).

Your application should respond to notifications with a standard HTTP status of `200 OK`. Absent this response to a notification, eBay will attempt redelivery, but after a significant number of unacknowledged notifications, eBay may stop sending notifications to your application.

Platform notifications are not identical to the email messages that buyers and sellers might get when an item is listed, bid on, or purchased, though they may contain some of the same data.

For a brief demonstration of a user subscribing to and receiving notifications, refer to the API flow tutorial, [Getting Notifications](/Devzone/XML/docs/HowTo/Notifications/Notifications_listing.html).

**Note:**  For a list of notification events that have been deprecated and are no longer supported refer to [Deprecated events](pn_deprecated-events.html).

## Related Documentation

In addition to the information in this guide, detailed schema reference documentation is also available for the Trading API (and all other traditional APIs). The schema reference documentation for the Trading API is described below:

* [Call Index](/devzone/XML/docs/Reference/eBay/index.html): a user can drill down in this index page to find the call they want to learn about. Each call reference page describes each input and output field, provides some details about using the call, and contains static call samples.
* [Type Reference](/devzone/XML/docs/Reference/eBay/types/index.html#TypeIndex): this reference page is an alphabetical list of all complex and enumerated types used by the Trading API. Each type page shows all of the fields and attributes used by that type, and also displays the calls and types that use that type. The Type Index can be useful if you are using an eBay SDK and you want to map the types in the schema to classes in the SDK. However, note that some calls only use a subset of the fields defined on a type (that's why you usually need to look at the "Call" view of the schema).
* [Errors by Number](/devzone/XML/docs/Reference/eBay/Errors/ErrorMessages.htm#ErrorsByNumber): this page is a complete list of all errors and warnings that may be triggered when using the Trading API. The information for each error includes: error code, error severity, short error string, and long error string. All error messages are supplied only in English, but the error codes can be used as an index for a structure, array, or string table to supply messages in whatever language is desired.

When the rules and/or behaviors differ for a given property based on what API call is using the property, these differences/exceptions are called out in the reference documentation.

## Notifications for Buyers and Sellers

Some notifications provide information that is specifically useful to sellers only, and these are restricted to sellers. Other notifications provide information that is useful to buyers only, or to both buyers and sellers.

Refer to [NotificationEventTypeCodeType](/Devzone/XML/docs/Reference/eBay/types/NotificationEventTypeCodeType.html) for a description of each notification event and to whom it applies.

## Subscribing to Platform Notifications

Your application can subscribe to notifications using **SetNotificationPreferences** (refer to [SetNotificationPreferences](/Devzone/XML/docs/Reference/eBay/SetNotificationPreferences.html) in the Call Reference).

Refer to [NotificationEventTypeCodeType](/Devzone/XML/docs/Reference/eBay/types/NotificationEventTypeCodeType.html) for the kinds of events to which an application can subscribe.

Existing preference settings can be reviewed by issuing a **GetNotificationPreferences** call. Refer to [GetNotificationPreferences](/Devzone/XML/docs/Reference/eBay/GetNotificationPreferences.html) for additional information.

Platform notification usage can be monitored by issuing a **GetNotificationsUsage** call. For more information on **GetNotificationsUsage** and how to use it to troubleshoot notification problems, refer to [GetNotificationsUsage](/Devzone/XML/docs/Reference/eBay/GetNotificationsUsage.html).

### Basic Requirements

The Compatible Application Check is not a requirement for using Platform Notifications.

Your application needs to be able to receive SOAP messages at a notification delivery URL of your choice. You can then parse the SOAP message for the XML content contained in the SOAP envelope.

#### Notification Delivery URL Requirements

Notifications can be delivered to a secure server/URL using the *https* protocol. This URL can be specified in your notification preferences. Use the **ApplicationDeliveryPreferences.ApplicationURL** field of the [SetNotificationPreferences](/devzone/XML/docs/Reference/eBay/SetNotificationPreferences.html) call to specify a URL to receive notifications for your application. Notifications will not be sent to any URL(s) if **ApplicationDeliveryPreferencesType.ApplicationEnable** is set to `Disable`.

Notification delivery URLs can include query string variables. For example, the following URLs are valid:

`https://my_hostname.com/cgi/my_notifications.asp`

`https://my_hostname.com/cgi/my_notifications.asp?myvar1=45&myvar2=123456789`

**Note:** We recommend that you specify URLs that are currently functional. That is, your application should be ready to receive and respond to SOAP messages that are sent to these URLs. The subscription request will succeed even if the delivery URLs are not functional URLs at the time the subscription request is made.

However, if eBay begins sending notifications to the URLs and your application does not respond with a standard HTTP status 200 OK, eBay will interpret the lack of response as a notification failure.

If a significant number of consecutive notifications fail, eBay may stop sending notifications for events associated with your `AppId`. If this occurs, verify the URLs are functional and then contact Developer Technical Support to reinstate your notification delivery.

#### Specifying Multiple Notification URLs

Up to 25 notification URLs may be specified for an application.

Settings for up to 25 notification URLs (including the URL name in **DeliveryURLName**) are configured in separate **ApplicationDeliveryPreferences.DeliveryURLDetails** containers in a [SetNotificationPreferences](/devzone/XML/docs/Reference/eBay/SetNotificationPreferences.html) request.

A user token is associated with a notification URL (or up to 25 URLs) by using the token in a [SetNotificationPreferences](/devzone/XML/docs/Reference/eBay/SetNotificationPreferences.html) request that specifies the URL name in **SetNotificationPreferencesRequest.DeliveryURLName**.

For multiple URLs that have been defined in **ApplicationDeliveryPreferences.DeliveryURLDetails**, use a comma-separated format to enable them for a user token in **SetNotificationPreferencesRequest.DeliveryURLName.**

Use **ApplicationDeliveryPreferences.ApplicationURL** to specify a default URL to receive notifications for your application.

Notifications will not be sent to any URL(s) if **ApplicationDeliveryPreferencesType.ApplicationEnable** is set to `Disable`.

### Notifications for Fixed-Price Listings with Variations or Multiple Quantities

Because you can edit multiple-item, fixed-price listings, even after one or more of the items in that listing has been sold, sellers or buyers of items in a multiple-quantity listing can get a snapshot of the listing as it was at the time of a given purchase by calling [GetItem](/Devzone/XML/docs/Reference/eBay/GetItem.html) with a `Transaction ID` as input.

Sellers of an item are allowed to view all transactional snapshots of the listing, whereas buyers can only view the transactional snapshots for which they are the successful buyer. Past transactional views of an item are available for up to 90 days from the date the transaction took place.

You can set a transaction event to trigger your notifications, or you can set an event related to the entire listing to trigger your notifications. If you're using item transaction snapshot data, **Listing Status** may report an **Active** status because the listing was **Active** on the transaction date, but the listing may actually have **Ended**.

## Receiving Platform Notifications

After notification delivery is enabled for your application, eBay will send notifications related to listings that your application has submitted using **AddItem**, **RelistItem**, and **ReviseItem**. When your application uses one of these calls, eBay identifies the application by its **AppId** (via the user token). The application's **AppId** is then associated with the listing. This is how eBay knows which application to notify when transactional or feedback events occur in relation to the listing.

Refer to [Specifying Multiple Notification URLs](#multiple-urls) for additional information.

### Responding to Notifications

When a notification is sent, your application needs to respond with a standard HTTP status **200 OK**. If you do not respond, eBay records the notification attempt as a failure, and the system does not resend the message. However, the database record for the event will still exist in the eBay system, so you can retrieve the event information by using the transaction-retrieval and feedback API functions (for example, **GetSellerEvents**).

If a significant number of notification failures occur consecutively (typically due to a problem with your delivery URLs or your application's ability to respond), eBay may stop sending notifications for events associated with your application's AppId.

### SOAP Message Fields

Notifications are sent as SOAP messages. Each SOAP message consists of:

* An HTTP header.
* An XML processing instruction (the Platform Notifications feature only supports UTF-8 character encoding).
* A SOAP envelope containing a SOAP header and SOAP body.

The SOAP header contains the notification signature that is used for security, and the SOAP body contains the actual event.

#### HTTP Header

Each SOAP message contains an HTTP header that consists of the following pieces of information:

* `Post` — contains the path of the URL that you provide.
* `PROTOCOL` — HTTP/1.1 (The HTTP post is sent via HTTP, not HTTPS, because the data does not need the security of a certificate.)
* `HOST` — contains the server specified in the URL that you provide
* `CONTENT_TYPE` — contains "text/xml" and the XML encoding of the message
* `CONTENT_LENGTH` �� contains the length, in the form of a number, of the SOAP message
* `SOAPACTION` — contains a URL that ends with the name of the event that the notification is being sent for. The value at the end will be one of the values specified in the [NotificationEventTypeCodeType](/Devzone/XML/docs/Reference/eBay/types/NotificationEventTypeCodeType.html) type in the schema.

The following example shows an HTTP header for an **EndOfAuction** notification. This customer–provided eBay with the URL `my_hostname.com/cgi/my_notifications.asp`.

**EndOfAuction Notification Header Example**

```json
POST: /cgi/my_notifications.asp
PROTOCOL: HTTP/1.1
HOST: my_hostname.com
CONTENT_TYPE: text/xml; charset="utf-8"
CONTENT_LENGTH: 1252
SOAPACTION: "HTTPS://developer.ebay.com/notification/EndOfAuction"
```

#### SOAP Message Header: Notification Signature

Each notification message contains a notification signature in the SOAP header for third-party application security. Your application should use the signature for message authentication to make sure the message was actually sent by eBay and that the notification signature was not copied by another party.

The notification signature is an MD5 hash signature that is generated using the following formula of concatenated strings, where DevId, AppId, and CertId are your application's Production Keys:

`eBayTime + DevId + AppId + CertId`

This hash is then Base64-encoded to reduce its length.

To have your application authenticate the signature:

1. Compute the MD5 hash using a standard routine, such as Microsoft crypto API, or OpenSSL open source.

   Refer to <http://www.openssl.org/> for additional information about these routines.
2. Convert the hash to Base64 encoding.
3. Compare the inputs in the notification signature to their actual values.

The `eBayTime` part of the signature should match the value of the **Timestamp** element in the SOAP message. Your application should check to make sure that the value of `eBayTime` is within 10 minutes of the actual time in GMT. The following code, written in C#, shows how to validate the notification hash:

**Example of How to Validate the Notification Hash (C#)**

```json
private bool CheckSignature(DateTime TimeStamp) {
  const string AppId = "myproductionappid";
  const string DevId = "myproductiondevid";
  const string CertId = "myproductioncertid";
  // Converts the TimeStamp back to universal time, because in .NET, XML schema time values
  // are converted to local time
  // If you are retrieving the time stamp directly from the XML body of the notification
  // message, you would not need to convert it.
  string sig = TimeStamp.ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ss.fffZ") + DevId +
      AppId + CertId;
  byte[] sigdata = System.Text.Encoding.ASCII.GetBytes(sig);
  System.Security.Cryptography.MD5 md5 =
      new System.Security.Cryptography.MD5CryptoServiceProvider();
  string md5Hash = System.Convert.ToBase64String(md5.ComputeHash(sigdata));
  return (mRequesterCredentials.NotificationSignature ==
      md5Hash DateTime.Now.Subtract(TimeStamp).Duration().TotalMinutes <= 10);
}
```

#### SOAP Message Body

The following notification-related fields of **AbstractResponseType** are, or can be, returned in the body of a notification:

* **NotificationEventName**
* **RecipientUserID**
* **EIASToken**

**NotificationSignature** is returned in the header.

Refer to [AbstractResponseType](/devzone/XML/docs/Reference/eBay/types/AbstractResponseType.html) for additional information and descriptions of these fields.

Each SOAP message body contains a top-level element, the name of which is the call that was issued to generate the data, with **Response** appended. For example, the element name for the **EndOfAuction** call is **GetItemTransactionsResponse**. This element contains one attribute to specify the namespace: `xmlns="urn:ebay:apis:eBLBaseComponents"`. Child elements include some elements common to all notifications, such as **Timestamp**, which specifies the time the notification was sent. Other child elements are specific to the notification being sent. In the **EndOfAuction** notification, the **Item** element contains most of the data for the notification.

### Notification Payloads

The content, or "payload," of a notification is equivalent to the response from a corresponding API call.

With **SetNotificationPreferences**, you can use the **PayloadVersion** field to specify the API version for all notifications for the calling application.

With **GetNotificationPreferences**, this field contains the API version for all notifications for the calling application.

**Note:**  For all order-related notifications returned through the **GetItemTransactions** response payload, it will be necessary for the seller to set the Payload Version of Platform Notifications to '1113' (or higher) in order to retrieve order IDs in the new format. To do this, issue a **SetNotificationPreferences** call, including the **ApplicationDeliveryPreferences**.**PayloadVersion** field, and setting its value to '1113' or above.

#### Testing Platform Notifications

Notifications are generated when certain events occur. To test the Platform Notifications feature in the Production environment:

* Subscribe to the notifications you want (refer to [Subscribing to Platform Notifications](#subscribe)).
* Create listings, bids, disputes, or anything else you want to test. Do something that generates a notification that your application is subscribed to, such as leaving feedback for a seller or having a buyer respond to a dispute.
* Make sure that your application can receive notifications.
* Make sure that your application responds to notifications with an HTTP status of **200 OK**.
* Use **GetNotificationsUsage** to review the platform notification usage history for your application.
* Contact eBay Developer Technical Support if you have questions.

Related topics

* [Start Here](/api-docs/static/ebay-rest-landing.html)
* [API Documentation](#)

  buy[Feed API](/api-docs/buy/feed/overview.html)[Browse API](/api-docs/buy/browse/overview.html)[Marketing API](/api-docs/buy/marketing/overview.html)[Offer API](/api-docs/buy/offer/overview.html)[Order API](/api-docs/buy/order/overview.html)[Marketplace Insights API](/api-docs/buy/marketplace-insights/overview.html)sell[Account API](/api-docs/sell/account/overview.html)[Inventory API](/api-docs/sell/inventory/overview.html)[Fulfillment API](/api-docs/sell/fulfillment/overview.html)[Finances API](/api-docs/sell/finances/overview.html)[Marketing API](/api-docs/sell/marketing/overview.html)[Negotiation API](/api-docs/sell/negotiation/overview.html)[Recommendation API](/api-docs/sell/recommendation/overview.html)[Analytics API](/api-docs/sell/analytics/overview.html)[Metadata API](/api-docs/sell/metadata/overview.html)[Compliance API](/api-docs/sell/compliance/overview.html)[Logistics API](/api-docs/sell/logistics/overview.html)[Listing API](/api-docs/sell/listing/overview.html)[Feed API](/api-docs/sell/feed/overview.html)commerce[Catalog API](/api-docs/commerce/catalog/overview.html)[Identity API](/api-docs/commerce/identity/overview.html)[Taxonomy API](/api-docs/commerce/taxonomy/overview.html)[Translation API Beta](/api-docs/commerce/translation/overview.html)[Translation API Expermental](/api-docs/commerce/translation-exp/overview.html)developer[Analytics API](/api-docs/developer/analytics/overview.html)
* [Integration Guides](#)

  [Buying Integration Guide](/api-docs/buy/static/buying-ig-landing.html)[Selling Integration Guide](/api-docs/sell/static/selling-ig-landing.html)
* [Related Docs](#)

  [Sell API](/api-docs/sell/static/sell-landing.html)[Buy API](/api-docs/buy/static/buy-landing.html)[Commerce APIs](/api-docs/commerce/static/commerce-landing.html)[Developer APIs](/api-docs/developer/static/developer-landing.html)