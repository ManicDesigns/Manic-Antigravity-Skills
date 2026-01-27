---
name: creating-skills
description: Guides the creation of high-quality Antigravity agent skills. Use when the user asks to create, build, or generate a new skill, or mentions '.agent/skills/', skill templates, or agent capabilities.
---

# Antigravity Skill Creator

You are an expert developer specializing in creating "Skills" for the Antigravity agent environment. Your goal is to generate high-quality, predictable, and efficient `.agent/skills/` directories based on user requirements.

## When to Use This Skill

- User asks to "create a skill" or "build a skill"
- User mentions `.agent/skills/` or skill templates
- User wants to extend agent capabilities with custom logic
- User needs a structured workflow for a repeatable task

## Core Structural Requirements

Every skill you generate must follow this folder hierarchy:

```
<skill-name>/
├── SKILL.md          # Required: Main logic and instructions
├── scripts/          # Optional: Helper scripts
├── examples/         # Optional: Reference implementations
└── resources/        # Optional: Templates or assets
```

## YAML Frontmatter Standards

The `SKILL.md` must start with YAML frontmatter following these strict rules:

| Field | Requirements |
|-------|-------------|
| **name** | Gerund form (e.g., `testing-code`, `managing-databases`). Max 64 chars. Lowercase, numbers, and hyphens only. No "claude" or "anthropic" in the name. |
| **description** | Written in **third person**. Must include specific triggers/keywords. Max 1024 chars. |

### Description Example
> "Extracts text from PDFs. Use when the user mentions document processing or PDF files."

## Writing Principles

Adhere to these best practices when writing `SKILL.md`:

- **Conciseness**: Assume the agent is smart. Focus only on the unique logic of the skill.
- **Progressive Disclosure**: Keep `SKILL.md` under 500 lines. Link to secondary files (e.g., `[See ADVANCED.md](ADVANCED.md)`) only one level deep.
- **Forward Slashes**: Always use `/` for paths, never `\`.

### Degrees of Freedom

| Freedom Level | Format | Use Case |
|---------------|--------|----------|
| High | Bullet Points | Heuristics, flexible guidance |
| Medium | Code Blocks | Templates, configurable patterns |
| Low | Specific Commands | Fragile operations, exact steps |

## Workflow & Feedback Loops

For complex tasks, include:

- [ ] **Checklists**: Markdown checklists the agent can copy and update to track state
- [ ] **Validation Loops**: "Plan-Validate-Execute" pattern (e.g., run a script to check config BEFORE applying changes)
- [ ] **Error Handling**: Instructions for scripts should be "black boxes"—tell the agent to run `--help` if unsure

## Output Template

When creating a skill, use this structure:

```markdown
---
name: [gerund-name]
description: [3rd-person description with trigger keywords]
---

# [Skill Title]

## When to Use This Skill
- [Trigger 1]
- [Trigger 2]

## Workflow
[Insert checklist or step-by-step guide]

## Instructions
[Specific logic, code snippets, or rules]

## Resources
- [Link to scripts/ or resources/]
```

## Skill Creation Checklist

Use this checklist when creating any new skill:

- [ ] Create skill folder: `.agent/skills/[skill-name]/`
- [ ] Create `SKILL.md` with valid YAML frontmatter
- [ ] Validate `name` field (gerund form, lowercase, hyphens only)
- [ ] Validate `description` field (third person, includes triggers)
- [ ] Add "When to Use This Skill" section
- [ ] Add workflow/checklist for complex tasks
- [ ] Add specific instructions or code snippets
- [ ] Create `scripts/` folder if automation is needed
- [ ] Create `examples/` folder if reference implementations help
- [ ] Create `resources/` folder for templates or assets
- [ ] Keep total line count under 500

## Example: Minimal Skill

```markdown
---
name: formatting-code
description: Formats code files using project standards. Use when the user mentions code formatting, linting, or style fixes.
---

# Code Formatter

## When to Use This Skill
- User asks to format code
- User mentions linting or style issues

## Instructions
1. Detect the project's formatter (Prettier, Black, gofmt, etc.)
2. Run the formatter on specified files
3. Report any files that were modified
```

## Resources

For advanced patterns, see:
- [examples/](examples/) - Reference skill implementations
- [resources/](resources/) - Reusable templates
