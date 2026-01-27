# Example Skill: Deployment Guard

This is a reference implementation demonstrating the skill structure.

```markdown
---
name: guarding-deployments
description: Validates deployments before execution. Use when the user mentions deploy, release, publish, or push to production.
---

# Deployment Guard

## When to Use This Skill
- User wants to deploy to production
- User mentions releasing or publishing
- User is pushing to a live environment

## Pre-Deployment Checklist

- [ ] All tests passing
- [ ] No lint errors
- [ ] Environment variables configured
- [ ] Database migrations ready
- [ ] Backup created (if applicable)

## Workflow

1. **Plan**: Review what will be deployed
2. **Validate**: Run pre-flight checks
   ```bash
   npm run test
   npm run lint
   npm run build
   ```
3. **Execute**: Deploy only after validation passes

## Rollback Instructions

If deployment fails:
1. Identify the last stable version
2. Revert to previous deployment
3. Document what went wrong
```
