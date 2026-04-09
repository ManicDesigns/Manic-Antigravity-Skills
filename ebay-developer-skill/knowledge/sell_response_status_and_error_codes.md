# Response Status and Error Codes

Source: https://developer.ebay.com/develop/api/sell/error_codes

## Search Documentation

* sell
* buy

Guides

Release Notes

Request Headers

Response Status and Error Codes

Listing Management

[Inventory Mapping](#api-inventory_mapping)

**Mutations**

* startListingPreviewsCreation

**Queries**

* listingPreviewsCreationTaskById

Listing Metadata

[Charity API](#api-charity_api)

**charity\_org**

* getCharityOrg
* getCharityOrgs

[Catalog](#api-catalog)

**product**

* getProduct

**search**

* search

Offers and Leads

[Negotiation](#api-negotiation)

**offer**

* findEligibleItems
* sendOfferToInterestedBuyers

Other APIs

[Identity API](#api-identity_api)

**get**

* getUser

## API Response Status Errors

If your request encounters problems during processing, the eBay servers can respond with either an error or warning condition. While processing might continue if a warning is encountered, the processing stops when errors are encountered.

### REST API Errors

#### 4xx and 5xx HTTP Status Codes

When you make a call to an eBay API, you can get a response that contains errors or warnings as described above. However, each API can also return *common errors*, which are error conditions that can occur while processing a call to any API. Common errors stop processing and they must be addressed before you can get a successful response from your call.

##### Types

* **ErrorType**

  This error type is used by both REST and GraphQL APIs, and defines the details of a specific error or warning.

  **errorId**longConditional

  The unique identifier for the error.

  **domain**stringConditional

  The name of the domain containing the service or application.

  **subDomain**stringConditional

  The name of the domain's subsystem or subdivision.

  **category**[ErrorCategory](#error-group-0.errorcategory)Conditional

  The error category for this error or warning.

  **message**stringConditional

  An end user and app developer friendly message.

  **longMessage**stringConditional

  An expanded version of message.

  **inputRefIds**array of stringConditional

  This array identifies specific request elements associated with the error.

  **outputRefIds**array of stringConditional

  This array identifies specific response elements associated with the error.

  **parameters**array of [ErrorParameter](#error-group-0.errorparameter)Conditional

  A list of context-specific ErrorParameter objects.

* **ErrorCategory**

  This enumerated type defines the classification of the error or warning. This can be one of three following values:

  **Possible Values:**

  | Value | Description |
  | --- | --- |
  | **APPLICATION** | This value indicates an exception or error occurred in the application code or at runtime. |
  | **BUSINESS** | This value indicates that your service or a dependent service refused to continue processing due to a business rule violation. |
  | **REQUEST** | This value indicates there is something wrong with the request, such as authentication, syntactical errors, or missing headers. |

* **ErrorParameter**

  This error type identifies the input parameter that caused the error or warning.

  **name**stringConditional

  The name of the input parameter that caused the error (e.g. `itemId`).

  **value**stringConditional

  The value of the input parameter that caused the error.

##### HTTP Status Codes

* **HTTP 400: Bad Request**

  | Error ID | Error Category | Message | Long Message | Domain |
  | --- | --- | --- | --- | --- |
  | 1002 | REQUEST | Missing access token | Access token is missing in the Authorization HTTP request header. | OAuth |
  | 1003 | REQUEST | "Token type in the Authorization header is invalid:" + scheme | "Token type in the Authorization header is invalid:" plus scheme | OAuth |
  | 2004 | REQUEST | Invalid request | Request has errors. For help, see the documentation for this API. | ACCESS |
  | 3001 | REQUEST | Request rejected |  | ROUTING |
  | 3002 | REQUEST | Malformed request | The request has errors. For help, see the documentation for this API. | ROUTING |

* **HTTP 401: Unauthorized**

  | Error ID | Error Category | Message | Long Message | Domain |
  | --- | --- | --- | --- | --- |
  | 1001 | REQUEST | Invalid access token | Invalid access token. Check the value of the Authorization HTTP request header. | OAuth |

* **HTTP 403: Forbidden**

  | Error ID | Error Category | Message | Long Message | Domain |
  | --- | --- | --- | --- | --- |
  | 1100 | REQUEST | Access denied | Insufficient permissions to fulfill the request. | OAuth |

* **HTTP 404: Not Found**

  | Error ID | Error Category | Message | Long Message | Domain |
  | --- | --- | --- | --- | --- |
  | 2002 | REQUEST | Resource not resolved | A resource (URI) associated with the request could not be resolved. | ACCESS |

* **HTTP 429: Too Many Requests**

  | Error ID | Error Category | Message | Long Message | Domain |
  | --- | --- | --- | --- | --- |
  | 2001 | REQUEST | Too many requests | The request limit has been reached for the resource. | ACCESS |

* **HTTP 500: Internal Server Error**

  | Error ID | Error Category | Message | Long Message | Domain |
  | --- | --- | --- | --- | --- |
  | 2003 | APPLICATION | Internal error | There was a problem with an eBay internal system or process. Contact eBay developer support for assistance. | ACCESS |
  | 3004 | APPLICATION | Internal error |  | ROUTING |

* **HTTP 502: Bad Gateway**

  | Error ID | Error Category | Message | Long Message | Domain |
  | --- | --- | --- | --- | --- |
  | 3005 | APPLICATION | Internal error |  | ROUTING |

Schema

{ /\* [ErrorType](#error-group-0.errortype) \*/ 

"[errorId](#error-group-0.errortype.errorid)" : "long",

"[domain](#error-group-0.errortype.domain)" : "string",

"[subDomain](#error-group-0.errortype.subdomain)" : "string",

"[category](#error-group-0.errortype.category)" : "[ErrorCategory](#error-group-0.errorcategory)",

"[message](#error-group-0.errortype.message)" : "string",

"[longMessage](#error-group-0.errortype.longmessage)" : "string",

"[inputRefIds](#error-group-0.errortype.inputrefids)" : "[[string]](#error-group-0.[string])",

"[outputRefIds](#error-group-0.errortype.outputrefids)" : "[[string]](#error-group-0.[string])",

"[parameters](#error-group-0.errortype.parameters)" : [

{ /\* [ErrorParameter](#error-group-0.errorparameter) \*/ 

"[name](#error-group-0.errorparameter.name)" : "string",

"[value](#error-group-0.errorparameter.value)" : "string"

}

]

}

### GraphQL API Errors

#### 4xx and 5xx HTTP Status Codes

These errors occur infrequently and are usually related to authentication/authorization, malformed HTTP requests, or upstream service failures. These errors are less common in GraphQL and are usually related to authentication/authorization, invalid HTTP requests, or unexpected server errors.

##### Types

* **ErrorType**

  This error type is used by both REST and GraphQL APIs, and defines the details of a specific error or warning.

  **errorId**longConditional

  The unique identifier for the error.

  **domain**stringConditional

  The name of the domain containing the service or application.

  **subDomain**stringConditional

  The name of the domain's subsystem or subdivision.

  **category**[ErrorCategory](#error-group-0.errorcategory)Conditional

  The error category for this error or warning.

  **message**stringConditional

  An end user and app developer friendly message.

  **longMessage**stringConditional

  An expanded version of message.

  **inputRefIds**array of stringConditional

  This array identifies specific request elements associated with the error.

  **outputRefIds**array of stringConditional

  This array identifies specific response elements associated with the error.

  **parameters**array of [ErrorParameter](#error-group-0.errorparameter)Conditional

  A list of context-specific ErrorParameter objects.

* **ErrorCategory**

  This enumerated type defines the classification of the error or warning. This can be one of three following values:

  **Possible Values:**

  | Value | Description |
  | --- | --- |
  | **APPLICATION** | This value indicates an exception or error occurred in the application code or at runtime. |
  | **BUSINESS** | This value indicates that your service or a dependent service refused to continue processing due to a business rule violation. |
  | **REQUEST** | This value indicates there is something wrong with the request, such as authentication, syntactical errors, or missing headers. |

* **ErrorParameter**

  This error type identifies the input parameter that caused the error or warning.

  **name**stringConditional

  The name of the input parameter that caused the error (e.g. `itemId`).

  **value**stringConditional

  The value of the input parameter that caused the error.

##### HTTP Status Codes

* **HTTP 400: Bad Request**

  | Error ID | Error Category | Message | Long Message | Domain |
  | --- | --- | --- | --- | --- |
  | 1002 | REQUEST | Missing access token | Access token is missing in the Authorization HTTP request header. | OAuth |
  | 1003 | REQUEST | "Token type in the Authorization header is invalid:" + scheme | "Token type in the Authorization header is invalid:" plus scheme | OAuth |
  | 2004 | REQUEST | Invalid request | Request has errors. For help, see the documentation for this API. | ACCESS |
  | 3001 | REQUEST | Request rejected |  | ROUTING |
  | 3002 | REQUEST | Malformed request | The request has errors. For help, see the documentation for this API. | ROUTING |

* **HTTP 401: Unauthorized**

  | Error ID | Error Category | Message | Long Message | Domain |
  | --- | --- | --- | --- | --- |
  | 1001 | REQUEST | Invalid access token | Invalid access token. Check the value of the Authorization HTTP request header. | OAuth |

* **HTTP 404: Not Found**

  | Error ID | Error Category | Message | Long Message | Domain |
  | --- | --- | --- | --- | --- |
  | 2002 | REQUEST | Resource not resolved | A resource (URI) associated with the request could not be resolved. | ACCESS |

* **HTTP 500: Internal Server Error**

  | Error ID | Error Category | Message | Long Message | Domain |
  | --- | --- | --- | --- | --- |
  | 2003 | APPLICATION | Internal error | There was a problem with an eBay internal system or process. Contact eBay developer support for assistance. | ACCESS |
  | 3004 | APPLICATION | Internal error |  | ROUTING |

Schema

{ /\* [ErrorType](#error-group-0.errortype) \*/ 

"[errorId](#error-group-0.errortype.errorid)" : "long",

"[domain](#error-group-0.errortype.domain)" : "string",

"[subDomain](#error-group-0.errortype.subdomain)" : "string",

"[category](#error-group-0.errortype.category)" : "[ErrorCategory](#error-group-0.errorcategory)",

"[message](#error-group-0.errortype.message)" : "string",

"[longMessage](#error-group-0.errortype.longmessage)" : "string",

"[inputRefIds](#error-group-0.errortype.inputrefids)" : "[[string]](#error-group-0.[string])",

"[outputRefIds](#error-group-0.errortype.outputrefids)" : "[[string]](#error-group-0.[string])",

"[parameters](#error-group-0.errortype.parameters)" : [

{ /\* [ErrorParameter](#error-group-0.errorparameter) \*/ 

"[name](#error-group-0.errorparameter.name)" : "string",

"[value](#error-group-0.errorparameter.value)" : "string"

}

]

}

#### HTTP 200 Status Code

Many errors that would typically be represented as 4xx/5xx in REST are returned as `HTTP 200` with error details in the GraphQL response body. Always check for `errors[]`, and note that partial `data` may be returned.

Response shape (HTTP 200):

* **message**: human-readable error message
* **extensions.errorCode**: stable machine-readable code (optional)
* **locations** and **path** may be present depending on the error type

##### Types

* **ErrorType**

  This error type defines the response payload of a GraphQL call. If one or more errors have occurred, information about the error(s) will be returned instead.

  **data**object | nullConditional

  The payload of the GraphQL response. This object is returned 'null' when one or more error occurs.

  **errors**array of [GraphQLError](#error-group-1.graphqlerror)Conditional

  This array returns a list of one or more errors (and associated metadata) returned by the GraphQL call.

* **GraphQLError**

  This error type defines the details of a Graph QL error, such as the error message, location, path, and extension data.

  **message**stringConditional

  The description of the error.

  **locations**array of [GraphQLSourceLocation](#error-group-1.graphqlsourcelocation)Conditional

  The source locations in the request that correspond to this error.

  **path**array of stringConditional

  The path in the response that led to this error.

  **extensions**[GraphQLErrorExtensions](#error-group-1.graphqlerrorextensions)Conditional

  The extension data for this error.

* **GraphQLSourceLocation**

  This type defines the information about the location of the error, such as the column and line number where it occurred.

  **line**intConditional

  The line number in the source where the error occurred.

  **column**intConditional

  The column number in the source where the error occurred.

* **GraphQLErrorExtensions**

  This type defines the extension data for the error.

  **errorCode**stringConditional

  The application-specific error code.

##### HTTP Status Codes

* **INTERNAL\_SERVER\_ERROR**

  A server-side error occurred while resolving the field.

* **FORBIDDEN**

  The authenticated user does not have sufficient permissions to access the field.

* **BAD\_INPUT\_VALUE**

  The caller has exceeded the allowed number of requests in a given time period.

* **RATE\_LIMITED**

  This error indicates that the caller has exceeded the allowed number of requests in a given time period. Rate limiting may be applied at the operation level, field level, or endpoint level to protect resources from overuse.

Schema

{ /\* [ErrorType](#error-group-1.errortype) \*/ 

"[data](#error-group-1.errortype.data)" : "object | null",

"[errors](#error-group-1.errortype.errors)" : [

{ /\* [GraphQLError](#error-group-1.graphqlerror) \*/ 

"[message](#error-group-1.graphqlerror.message)" : "string",

"[locations](#error-group-1.graphqlerror.locations)" : [

{ /\* [GraphQLSourceLocation](#error-group-1.graphqlsourcelocation) \*/ 

"[line](#error-group-1.graphqlsourcelocation.line)" : "int",

"[column](#error-group-1.graphqlsourcelocation.column)" : "int"

}

],

"[path](#error-group-1.graphqlerror.path)" : [

"string"

],

"[extensions](#error-group-1.graphqlerror.extensions)" : 

{ /\* [GraphQLErrorExtensions](#error-group-1.graphqlerrorextensions) \*/ 

"[errorCode](#error-group-1.graphqlerrorextensions.errorcode)" : "string"

}

}

]

}

[FAQs](/support/faq)[Developer Community Forum](https://community.ebay.com/t5/Developer-Groups/ct-p/developergroup)[Developer Technical Support](/my/support/tickets)[APIs](/develop/apis)[API License Agreement](/join/api-license-agreement)

Copyright 1999—2026 eBay Inc. All rights reserved. [User agreement](http://pages.ebay.com/help/policies/user-agreement.html?rt=nc "opens in new window or tab"), [Privacy policy](http://pages.ebay.com/help/policies/privacy-policy.html?rt=nc "opens in new window or tab"), [Cookies](http://pages.ebay.com/help/account/cookies-web-beacons.html "opens in new window or tab").