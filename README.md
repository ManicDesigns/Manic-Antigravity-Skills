# Matrix Solutions - Global Skills Repository

This repository contains the Master Skills Library for Antigravity Agents.

## Available Skills
The following skills are ready for deployment:
- **ebay-developer-skill**: Complete eBay integration guide.
- **managing-excel-files**: Create, edit, and analyze Excel spreadsheets.
- **managing-pdf-files**: Manipulate PDFs (merge, split, extract text).
- **managing-word-docs**: Create and edit Word documents.
- **building-mcp-servers**: Guide for MCP server creation.
- **antigravity-skill-creator**: Standards for creating new skills.
- **brainstorming**: Collaborative design and ideation (from `obra/superpowers`).
- **planning**: Detailed implementation planning (from `obra/superpowers`).
- *...and more.*

## Usage

### To make these skills available in another project:
Run the deployment script:
```powershell
python "c:\Users\MatrixSolutions\Documents\AntiGravity Projects\Skills\deploy_skills.py" "C:\Your\Project\Path"
```

### Keeping Skills Updated (The "Manic" Workflow)
This repository aggregates skills from multiple sources via `scripts/sync_skills.py`.
To check for updates from upstream repositories (`anthropics`, `superpowers`) and sync them here:

1. Use the Agent Workflow: "Check for skill updates"
2. Or run manually:
   ```powershell
   python scripts/sync_skills.py --push
   ```
