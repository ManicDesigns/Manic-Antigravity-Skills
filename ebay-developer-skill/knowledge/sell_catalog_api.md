# Sell Catalog API

The Catalog API provides search capabilities and specific eBay Product ID (ePID) lookups. Using the Catalog API is highly encouraged to ensure listings conform directly to eBay's standardized master product catalog.

## Key Endpoints
1. **Get Product**: 
   `GET /sell/catalog/v1/product/{epid}`
   Retrieves detailed product catalog information by eBay Product ID.
   
2. **Search Catalog**:
   `GET /sell/catalog/v1/product_summary/search`
   Accepts generalized search criteria (like `q=iPhone+15`) or global identifiers (GTIN/UPC) and returns matching catalog reference numbers (ePID).

## Integrating with AI
- When AI agents are constructing listings for standardized products, always instruct agents to `search` the Catalog API first.
- Construct the final inventory payload utilizing the matched `epid`, rather than leaving the AI to arbitrarily guess or hallucinate `product.aspects`.
