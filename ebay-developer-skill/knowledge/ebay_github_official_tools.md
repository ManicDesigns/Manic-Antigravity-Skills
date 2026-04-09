# eBay Official GitHub Tools & SDKs

This document catalogs the official open-source repositories from eBay's GitHub organization ([github.com/eBay](https://github.com/eBay)) that are relevant to building eBay sales, sourcing, and listing tools across mobile, web, and AI platforms.

---

## 🔥 HIGH PRIORITY — Direct Integration Value

### 1. eBay Public API MCP Server (`npm-public-api-mcp`)
- **Repo**: https://github.com/eBay/npm-public-api-mcp
- **Language**: TypeScript (91%)
- **What it does**: An official **Model Context Protocol (MCP) server** that lets AI assistants (Claude, Cursor, Copilot, etc.) discover, browse, and **call eBay APIs directly** using natural language.
- **Why it matters**: This is eBay's official bridge between AI agents and their entire API ecosystem. It enables:
  - 🔍 Searching for eBay APIs by keyword
  - 📋 Browsing full API documentation inline
  - 🚀 Making live API calls to production or sandbox
  - 💬 Natural language interface for endpoint discovery
- **Installation**:
  ```bash
  EBAY_CLIENT_TOKEN='token' EBAY_API_ENV='production' npx @ebay/npm-public-api-mcp@latest
  ```
- **AI Agent Config (Claude Desktop / VS Code)**:
  ```json
  {
    "mcpServers": {
      "ebay-api": {
        "command": "npx",
        "args": ["-y", "@ebay/npm-public-api-mcp@latest"],
        "env": {
          "EBAY_CLIENT_TOKEN": "YOUR_ACCESS_TOKEN",
          "EBAY_API_ENV": "production"
        }
      }
    }
  }
  ```
- **Coverage**: Selling APIs, Buying APIs, Commerce APIs, Marketing APIs, Developer APIs
- **Tokens expire every 2 hours** — agents must handle refresh logic.

---

### 2. Digital Signature Node.js SDK (`digital-signature-nodejs-sdk`)
- **Repo**: https://github.com/eBay/digital-signature-nodejs-sdk
- **Language**: JavaScript (57%) / TypeScript (43%)
- **What it does**: Generates and validates HTTP message signatures required by eBay for EU/UK seller API calls (SCA regulatory compliance).
- **Why it matters**: Any production application serving European or UK sellers **must** sign requests using this SDK. Without it, API calls will be rejected.
- **Key Headers Generated**:
  - `Content-Digest` — SHA-256 digest of the HTTP payload (RFC 9530)
  - `Signature-Input` — Ordered list of headers used in signature (RFC 9421)
  - `Signature` — Cryptographic signature using Key Management API private key
  - `x-ebay-signature-key` — JWE from Key Management API
- **Installation**:
  ```bash
  npm install digital-signature-nodejs-sdk
  ```
- **Configuration requires**: `digestAlgorithm`, `jwe`, `privateKey`, `signatureComponents`, `signatureParams`
  - Keys are generated via the **Key Management API**: https://developer.ebay.com/api-docs/developer/key-management/overview.html

---

### 3. Taxonomy SDK (`taxonomy-sdk`)
- **Repo**: https://github.com/eBay/taxonomy-sdk
- **Language**: Java (100%)
- **What it does**: A Spring Boot CLI tool that performs deep comparison of eBay's category aspects metadata. It reports what's new, modified, or removed between bulk data snapshots.
- **Why it matters**: eBay's category aspects evolve rapidly. For sourcing/listing tools, staying current on required Item Specifics is critical. This SDK:
  - Compares two downloaded bulk aspect files and reports structured diffs
  - Can compare a local cache against the latest live data using OAuth tokens
  - Outputs precise JSON showing new/modified/removed categories, aspects, constraints, and values
- **Usage**:
  ```bash
  java -jar taxonomy-metadata-sdk-1.0.0-RELEASE.jar \
    --previous_file={A} --current_file={B} --out={outputDir}
  ```
- **AI Agent Integration**: Use this to build automated alerts when eBay changes required Item Specifics for categories your sellers frequently list in.

---

## ⚡ MEDIUM PRIORITY — Useful Patterns

### 4. GraphQL2JSONSchema (`GraphQL2JSONSchema`)
- **Repo**: https://github.com/eBay/GraphQL2JSONSchema
- **Language**: Java
- **What it does**: Converts GraphQL schemas to JSON Schema format.
- **Relevance**: The new **Inventory Mapping API** is GraphQL-based. This tool can help generate type-safe client bindings from eBay's GraphQL schema definitions.

### 5. nice-modal-react (`nice-modal-react`)
- **Repo**: https://github.com/eBay/nice-modal-react
- **Language**: TypeScript
- **Stars**: 2.3k ⭐
- **What it does**: A zero-dependency React modal state manager. Modals are managed via a global provider pattern — you call `NiceModal.show(MyModal)` from anywhere.
- **Relevance**: Useful for listing confirmation dialogs, Quick-Edit modals, and sourcing result detail overlays in the Profit Engine web app. Built and maintained by eBay's own frontend team.

### 6. evo-web (`evo-web`)
- **Repo**: https://github.com/eBay/evo-web
- **Language**: TypeScript, CSS, Sass
- **What it does**: eBay's own "Evo" branded CSS + React/Marko component library with full accessibility (a11y) support.
- **Relevance**: Reference implementation for building eBay-compliant UI components. Useful if building seller-facing tools that need to match eBay's visual language.

---

## 📋 LOW PRIORITY — Reference Only

| Repo | Purpose | Relevance |
|------|---------|-----------|
| `digital-signature-java-sdk` | Java version of the digital signature SDK | Only if using Java backend |
| `flow-telemetry` | OpenTelemetry for feature flows | Observability patterns |
| `visual-html` | Visual regression testing for HTML | Testing patterns |
| `mindpatterns` | HTML accessibility pattern examples | a11y reference |
| `browserslist-config` | eBay's browserslist targets | Build config reference |

---

## Not Relevant (Filtered Out)
The following repos were reviewed and excluded as they serve eBay's internal infrastructure and have no direct relevance to seller tools, sourcing, or AI integration:
- `HomeStore` / `HomeObject` — C++ storage engines
- `NuRaft` / `Gringofts` — Distributed systems / consensus
- `sisl` — C++ data structures
- `flink-dynamic-config` — Apache Flink configs
- `TasCreed` — Task orchestration
- `ejmask` — Java/Kotlin data masking
- `spec_dec` — ML speculative decoding
- `unilogit-acl-2025` — ML research benchmarks
- `ConsID-Gen` — ML image generation
- `imhotep` — Static analysis bot
- `NSTSuite` — Java testing framework
- `orchestra` — Java orchestration
- `Muse` — JavaScript (minimal docs)
- `nice-dag` — DAG diagram visualization
