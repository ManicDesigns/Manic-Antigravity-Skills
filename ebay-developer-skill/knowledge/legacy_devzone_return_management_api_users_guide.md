# Return Management API Users Guide

Source: https://developer.ebay.com/Devzone/return-management/Concepts/ReturnManagementAPIGuide.html

# Return Management API Users Guide

  
  

**Note:** The Return Management API is no longer recommended. Instead, current users of the Return Management API should make plans to migrate to, and use the Return operations of the [Post-Order API](http://developer.ebay.com/Devzone/post-order/concepts/UsageGuide.html). New users interested is programmatically managing return requests, should also make plans to integrate with the Post-Order API. The Return Management API was developed to be used by sellers who had opted in to "Hassle-free Returns". Hassle-free Returns have been replaced by a new Returns Platform, where sellers fully or partially automate the processing of return requests through Return Automation Rules. The Return Management API does not support all features and logic of the new Returns Platform, and this API will be deprecated in the near future.

The Return Management API provides US and UK sellers a programmatic way to retrieve and manage eBay-Managed returns created through Return Center. The Return Management API allows sellers to perform the following actions:

* Retrieve summary information on buyer returns filed against their account. Filters are
  available to restrict results to a date range, a specific return status, a specific listing, a
  specific order, a specific order line item, and/or a specific eBay member (on the other side of
  a return from the user making the call).
* Retrieve summary information on returns for any other eBay user (as a buyer or seller). The
  same filtering options are available for other users that are available for a seller's own account.
* Retrieve detailed information on a specific buyer return.
* Retrieve one or more of the next possible actions that a seller can make on a return. Based
  on the activity option(s) that are returned, the seller can then make the appropriate Return
  Management API call.
* Retrieve all valid reasons for a buyer to return an item.
* Retrieve how many business days the seller is given to issue a refund to the buyer after the seller
  receives the returned item from the buyer
* Retrieve how many business days the seller is given to provide an Return Merchandise Authorization number
  (RMA) to the buyer once the buyer opens a return against the seller
* Issue a refund to the buyer for the return. Based on the specifics of an order, the seller
  refunds the buyer for the purchase price and original shipping costs, and possibly assesses
  a restocking fee charge against the buyer. This call only supports PayPal refunds.
* Upon a request from the buyer, the seller provides a Return Merchandise Authorization number
  (RMA) to the buyer.
* Provide the buyer with an alternative return shipping address.
* Provide the buyer with shipment tracking information for a replacement item.
* Mark a replacement item as received once the buyer receives the item

Refer to the Return Management API
[API Reference](../CallRef/index.html) for detailed information on each call,
including input fields, output fields, and samples.

## Retrieving Summary Information for Returns

The **getUserReturns** call retrieves summary information of one or more
buyer returns. This call can be used to retrieve returns created within the last 18 months.
The next three sections describe the filters, sorting, and pagination options that are available
with the **getUserReturns** call.

### Using Filters in getUserReturns

The **getUserReturns** call has filters available to restrict results to a
date range, a specific return status, a specific listing, a specific order, a specific order
line item, and/or a specific eBay member (on the other side of a return from the user
making the call)

The **creationDateRangeFilter** container is used to restrict results to returns
created within a specified date range. The maximum date range that can be used is 90 days.

The **returnStatusFilter** container is used to restrict results to returns
that are in a specific state in the return flow. More than one return state can be specified
in the **returnStatusFilter** container.

The **itemFilter** container is used to restrict results to a specific listing or
to a specific order line item. For a multi-quantity, fixed price listing, more than one return
may be retrieved.

The **otherUserFilter** container is used to retrieve returns for a specific
user whom is on the other side of one or more returns.

### Using Pagination in getUserReturns

If you expect the response payload of a **getUserReturns** call to be large,
pagination can be used to control the number of returns returned per page of data. If there are
multiple pages of returns to view, you can programmatically "scroll" through the pages by
making subsequent calls, incrementing the **paginationInput.pageNumber** value each
time until all pages have been viewed and/or handled.

See the **getUserReturns** API Reference for more information on pagination.

### Using Sorting in getUserReturns

There are sort options available in the **getUserReturns** request. The **sortOrderType**
field allows the caller to choose between displaying results in descending or ascending order. The
**sortType** field allows the caller to sort results based on the return filing
date, the estimated amount of the return, the due date of the refund, or the buyer's user name.

If the sorting fields are not included in the **getUserReturns** request, the
default value of **sortOrderType** is "Descending", and the default value of
**sortType** is "FilingDate".

See the **getUserReturns** API Reference for more information on sorting results.

### The getUserReturns Response

A **returns** node is returned for each return that satisfies the input
criteria. The following container/fields are always returned under a **returns** node:

* **creationDate**: timestamp indicating when the return was opened by the
  buyer.
* **ReturnId.id**: the unique identifier of the return. This value will be used in
  other Return Management API calls to identify the return to perform an action on.
* **otherParty**: this container identifies the other party
  involved in the return.
* **status**: this field contains an enumeration value that indicates the current
  status of the return.
* **returnRequest**: this container consists of details related to the item being
  returned, including the buyer's reason for returning the item.

The **responseDue** container is returned if the buyer or seller has a pending
response due in the return. The current status of the return dictates the type or response
that is due.

### Common Errors for getUserReturns

The following are some common errors that can occur when using filtering with the **getUserReturns**
call:

* An invalid Item ID is specified under the **itemFilter** container.
* An invalid Transaction ID is specified under the **itemFilter** container.
* the Item ID and Transaction ID values specified under the **itemFilter**
  container do not match.
* An invalid date range is specified in the **creationDateRangeFilter** container.
  Invalid date range errors may involve an incorrect date format, a "from" or "to" date in the future,
  a "from" date that is more recent than the "to" date, a "from" date older than 18 months, or a
  specified time range longer than three months.
* An invalid return status value is specified in the **ReturnStatusFilter**
  container.
* An invalid user ID or login name is specified in the **otherUserFilter**
  container.

## Using getReturnDetail

The **getReturnDetail** call is used to retrieve detailed information on a return.
The seller passes a return ID into the **ReturnId.id**
field of the request. The Return ID value can be obtained with the **getUserReturns**
call.

The two containers returned at the root level of the **getReturnDetail** response
are **ReturnSummary** and **ReturnDetail**.

The **ReturnSummary** container consists of the following information:

* **The creation date and last modified date of the return**: the **lastModifiedDate**
  value updates with each activity in the return.
* **ReturnId.id**: the unique identifier of the return.
* **status**: enumeration value that indicates the status of the return. This value is
  dynamic.
* **otherParty**: this container identifies the other party
  involved in the return.
* **returnRequest**: this container consists of details on the item being returned,
  the buyer's reason for the return, and any buyer comments.
* **responseDue**: this container is returned if the buyer or seller has a pending
  response due in the return. The current status of the return dictates the type or response
  that is due. This value is dynamic.

The **ReturnDetail** container consists of the following information:

* **refundInfo.estimatedRefundDetail**: the data in this container will reflect the
  buyer's costs in the original transaction, including the purchase price and shipping costs.
* **refundInfo.actualRefundDetail**: the data in this container will reflect the
  actual refund issued from the seller to the buyer during the return flow. An **itemizedRefund**
  container is required for each refund type, such as purchase price, original shipping, and
  restocking fee. The total refund amount is indicated in the **actualRefund.totalAmount**
  field.
* **refundInfo.refundDue**: the date on which the buyer's refund is due from the
  seller.
* **returnHistory**: a **returnHistory** node is returned for each
  activity logged in the return. Each node includes the date, description, and author (actor) of
  each activity.
* **globalId**: string value that indicates the site where the item was purchased.
* **shipmentInfo**: this container consists of detailed information on a package shipment, whether that shipment is the buyer returning an item, or the seller is providing the buyer with a replacement item. This container includes the shipping address of the package's destination, the shipping carrier used, the shipping costs, the estimated delivery date range, and the status of the shipment. If provided/available, the tracking number and Return Merchandise Authorization number may also appear in this container.
* **caseId**: this container will appear in the response if there is an eBay Buyer
  Protection case filed against the item associated with the return.

## Determining Next Action with getActivityOptions

The **getActivityOptions** call is used by the seller to determine the next
required action for the return. The seller passes a return ID into the
**ReturnId.id** field of the request. The Return ID value can be obtained with the
**getUserReturns** call.

The five possible activity options that are returned in the response are the following:

* **ISSUE\_REFUND**: if this option is returned, the seller can use the **issueRefund** call to issue a refund to the buyer.
* **PROVIDE\_SELLER\_INFO**: if this option is returned, the seller can provide a Return Merchandise Authorization number through the **provideSellerInfo** call.
* **SELLER\_MARK\_AS\_RECEIVED**: if this option is returned, the seller should use the **setItemAsReceived** call to mark the replacement item as received by the buyer.
* **SELLER\_PRINT\_SHIPPING\_LABEL**: if this option is returned, a printing label is available to the seller for shipping the replacement item to the buyer.
* **SELLER\_PROVIDE\_TRACKING\_INFO**: if this option is returned, the seller should use the **provideTrackingInfo** call to provide shipment tracking information for the replacement item to the buyer.

## Retrieving Return Metadata

The seller can use the **getReturnMetadata** call to retrieve the following data:

* **The list of possible buyer reasons for creating a return**. The seller passes 'RETURN\_REASONS' into the
  **metadataEntryCode** field to retrieve the return reasons.
* **The number of business days a seller has to provide a Return Merchandise Authorization number to the
  buyer**. The seller passes 'RMA\_DUE\_UPON\_RETURN\_START' into the **metadataEntryCode**
  field to retrieve the number of business days allowed to process the request. The integer value returned in
  the response is the number of business days beyond the start of the return that the seller has to provide
  an RMA to the buyer. The creation date of a return is returned in **getUserReturns**
  and **getReturnDetail**.
* **The number of business days a seller has to issue a refund after receiving the returned item from the
  buyer**. The seller passes 'REFUND\_DUE\_UPON\_ITEM\_ARRIVAL' into the **metadataEntryCode**
  field to retrieve the number of business days allowed to process the request. The integer value returned in
  the response is the number of business days after receiving the returned item that the seller has to issue
  a refund to the buyer. The delivery date of the returned item is returned in the **ReturnDetail.buyerReturnShipment.deliveryDate**
  field of **getReturnDetail**.

If the seller wishes to retrieve all return metadata, no **metadataEntryCode**
fields should be passed in the request.

## Using provideSellerInfo

The seller can use **provideSellerInfo** to provide a Return Merchandise
Authorization number to the buyer (upon request from the buyer), or to provide an
alternative return shipping address to the buyer.

The seller must also pass a return ID into the
**ReturnId.id** field of the request. The Return ID value can be obtained with the
**getUserReturns** call. eBay cannot verify the accuracy of the RMA number, so the
accuracy of this number is the responsibility of the seller.

The **returnAddress** container is used by the seller to provide the buyer with
an alternative return shipping address. If used in the call, this return shipping address will be
used by the buyer instead of the primary return shipping address on file for the seller.

## Issuing a Refund

The seller will use **issueRefund** to issue a refund to the buyer.

The seller passes a return ID into the **ReturnId.id** field of the request
to identify the return. The Return ID value can be obtained with the
**getUserReturns** call.

The **refundDetail** container is used to provide the refund type and amount. An
**itemizedRefund** container is required for each refund type, such as purchase
price, original shipping, and restocking fee (if a Restocking Fee value was specified at listing time). The total refund amount is passed
into the **refundDetail.totalAmount** field. The aggregate total of refund amounts
passed in one or more **itemizedRefund.amount** fields should match the **refundDetail.totalAmount**
value.

Optionally, the seller can provide a message regarding the refund using the **comments**
field.

A **RefundStatus** enumeration value is returned in the response. 'SUCCESS'
indicates that the refund to the buyer through PayPal was successful, and 'FAILED' indicates
that the refund to the buyer through PayPal failed. 'PENDING' is for future use.

[Back to top](#top)

## Providing Tracking Information

The seller will use **provideTrackingInfo** to provide shipment tracking information to the buyer if the seller is shipping a replacement item to the buyer. In the **provideTrackingInfo** call, the seller provides the shipping carrier used to ship the item and the tracking number associated with that shipment. Optionally, there is a field that allows the seller to provide additional comments about the return and/or the replacement item.

## Marking a Replacement Item as Received

In some cases, the buyer is OK with receiving a replacement item from the seller. The buyer can select this option through the eBay Return Center. The seller can use **setItemAsReceived** to mark the replacement item as received once it reaches the buyer.

## Platform Notifications for eBay Return Cases

Using the **SetNotificationPreferences** call of the Trading API, users can subscribe
to the following platform notifications related to the activity of eBay Returns and the Return
Management API.

* **ReturnCreated**: this notification type is sent to the subscribed user or application when a
  return is created by the buyer.
* **ReturnWaitingForSellerInfo**: this notification type is sent to the subscribed user or
  application when a return is waiting for the seller to provide an RMA number to the buyer.
* **ReturnSellerInfoOverdue**: this notification type is sent to the subscribed user or
  application when the due date for an RMA is overdue.
* **ReturnShipped**: this notification type is sent to the subscribed user or application when the
  item associated with a return is shipped back to the seller.
* **ReturnDelivered**: this notification type is sent to the subscribed user or application when
  the item associated with a return has been delivered to the seller.
* **ReturnRefundOverdue**: this notification type is sent to the subscribed user or application
  when the refund to the buyer is overdue.
* **ReturnClosed**: this notification type is sent to the subscribed user or application when a
  return is closed by the system.
* **ReturnEscalated**: This notification type is sent to the subscribed user or application when a
  (SNAD) return is escalated to the eBay Buyer Protection system.

For more information on these notifications and the Platform Notification process, see the [>Trading API Guide](../guides/ebayfeatures /index.html).

[Back to top](#top)

## Working with the Return Management API

### API Call Limits

Please refer to the [API Call Limits page](https://go.developer.ebay.com/api-call-limits) on the eBay Developers Program site for current default call limits and call limits for applications that have completed the [Compatible Application Check](http://developer.ebay.com/support/certification/), which is a free service that the eBay Developers Program provides to its members.

### Sandbox Environment

For more information about testing, refer to [Testing Overview](MakingACall.html#TestingOverview) in the Making a Return Management API Call document.

### API Reference

Refer to the [API Reference](../CallRef/index.html) for a list of calls in the Return Management API. The API Reference includes the following information:

* Prototypes of the request and response structure for each call
* Comprehensive list of inputs and outputs supported by each call and descriptions of their meaning and behavior
* Call samples (request and response)
* Index of schema elements (types, fields, enumerations)
* Change history information for each call

  
  
  
  