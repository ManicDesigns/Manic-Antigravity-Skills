# Sell Negotiation API

The Negotiation API handles the mechanics of buyer and seller offers for eligible listings. 

## Key Endpoints
1. **Find Eligible Items**:
   `GET /sell/negotiation/v1/find_eligible_items`
   Determines which active listings can currently send offers to interested buyers.

2. **Send Offer to Buyers**:
   `POST /sell/negotiation/v1/send_offer_to_interested_buyers`
   Pushes a discount offer directly to users inherently tracking or watching the item.

3. **Respond to Buyer Offers**:
   Sellers receive offers via Notifications. Agents can read the offers and programmatically Accept, Decline, or Counter using specific transactional endpoints.

## AI Usage
When wrapping agents around Negotiation logic:
- Acknowledge latency: Offers have a 48-hour expiration natively.
- Provide agents with absolute discount floor brackets logic before permitting automated `POST /send_offer_to_interested_buyers` calls.
