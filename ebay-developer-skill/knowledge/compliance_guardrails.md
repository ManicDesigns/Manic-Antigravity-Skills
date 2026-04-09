# eBay API Compliance Guardrails

## 1. API License Agreement (ALA)
All developers must adhere to the **eBay API License Agreement**. Key points include:
- **No scraping** of eBay pages (use APIs instead).
- **Data retention**: Do not store User Data indefinitely. Delete it when no longer needed or upon request (eBay Marketplace Account Deletion/Closure Notifications).
- **Branding**: Follow eBay Branding Guidelines when displaying logos.

## 2. Rate Limiting & Quotas
eBay imposes strict rate limits to ensure stability.
- **Sandbox**: Typically **5,000 calls/day**.
- **Production**: Varies by application tier. Check your [Developer Portal](https://developer.ebay.com/my/stats) for current limits.
- **Best Practice**: Implement exponential backoff for `429 Too Many Requests` errors.

## 3. Data Protection
- **PII (Personally Identifiable Information)**: Handle with extreme care. Encrypt at rest.
- **Marketplace User Account Deletion (GDPR/CCPA)**: Your application MUST subscribe to eBay's Marketplace Account Deletion webhooks. If an eBay user requests data deletion, eBay will fire a notification to your configured endpoint. You are contractually obligated to wipe their associated PII from your local databases immediately.
- **Token Security**: Never expose Client Secrets or User Access Tokens in client-side code (browser). Use a backend proxy.

## 4. Restricted Categories
Some APIs (e.g., Feed API, Large Merchant Services) require special approval or "Compatibility Checks".

## 5. Digital Signatures for APIs
Several high-risk HTTP headers and APIs (particularly Finance APIs, fulfillment, and certain identity resolution paths) require full Digital Signatures to guarantee payload integrity. Agents constructing requests for these endpoints must compute and append the `Signature` and `Signature-Input` HTTP headers using strict cryptographic standards outlined by eBay.
