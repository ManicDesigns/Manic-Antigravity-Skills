# Sell Identity API

The Identity API primarily resolves eBay user details based on the authenticated request context.

## Key Endpoint
1. **Get User**:
   `GET /sell/identity/v1/user`
   This retrieves the fundamental eBay account information for the user tied to the active access token. It returns the username, marketplace constraints, standard registration status, and account type (Business or Individual).

## AI Agent Relevance
AI integrations that run across a multi-tenant application infrastructure should use the Identity API during initial OAuth 2.0 onboarding to permanently log the connected seller's `userId` in the backend database mapping. This ensures webhook notifications and token refreshes are reliably dispatched to the correct business profile.
