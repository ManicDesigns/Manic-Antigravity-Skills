# Inventory Mapping API

The Inventory Mapping API is a GraphQL-based API designed to help sellers create high-quality listings by leveraging AI-powered recommendations generated from their existing product data.

## Key Capabilities
- **AI-Generated Listings**: Provides AI content suggestions to list products faster and get inventory in front of buyers sooner.
- **Improved Listing Quality**: Enhances visibility, buyer trust, and conversion rates by generating optimized listing attributes.

## Marketplace Restrictions
- **U.S. Marketplace Only**: Currently, this API is available strictly for the U.S. marketplace.
- Results generated from this API should only be used for listings on the U.S. site until coverage expands.

## Developer & AI Integration Guardrails
When building AI agents or automated connections that utilize the Inventory Mapping API results, adhere to the following rules:

1. **Diagnosis and Tracking (`mappingReferenceID`)**: You **must** include the `mappingReferenceID` field within the payload for all listings generated or revised using recommendations from the Inventory Mapping API. This is critical for quickly diagnosing and resolving any issues or hallucinations derived from AI-generated listing data.
2. **GraphQL Protocol**: Unlike REST APIs, this API is built entirely on GraphQL. Ensure your application architecture handles GraphQL endpoints correctly. Use the [eBay GraphQL API Explorer](https://developer.ebay.com/my/graphql_explorer) (Production env) to support your query testing and design.
3. **Target Scope Verification**: Validate that the seller's intent and target marketplace match the US limit before initiating an AI processing path that calls this API.
4. **Access Escalation**: If your integration scales and requires expanded API usage, you must apply for an "Application Growth Check".
