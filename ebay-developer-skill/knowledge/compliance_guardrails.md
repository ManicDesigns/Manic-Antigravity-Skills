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
- **GDPR/CCPA**: Your application must support data deletion requests.
- **Token Security**: Never expose Client Secrets or User Access Tokens in client-side code (browser). Use a backend proxy.

## 4. Restricted Categories
Some APIs (e.g., Feed API, Large Merchant Services) require special approval or "Compatibility Checks".
