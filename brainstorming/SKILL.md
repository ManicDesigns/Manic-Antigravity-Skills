---
name: brainstorming
description: Collaboratively explores user intent, requirements, and design before implementation. Use when starting creative work, designing features, or gathering requirements.
---

# Brainstorming

## When to Use This Skill
- User has a vague idea or request
- Starting a new feature or component
- Requirements are unclear or need refinement
- User asks to "brainstorm" or "design" something

## Workflow

- [ ] **Phase 1: Understanding** - Clarify purpose, constraints, and success criteria one question at a time.
- [ ] **Phase 2: Exploration** - Propose 2-3 distinct approaches with trade-offs.
- [ ] **Phase 3: Design** - Present the chosen solution in small, digestible sections (200-300 words).
- [ ] **Phase 4: Handoff** - Finalize the design document for implementation.

## Instructions

### 1. Understanding the Idea
*   **Check Context**: Review existing files, docs, and recent commits first.
*   **One Question Rule**: Ask only **one question per message**.
*   **Multiple Choice**: Prefer giving options (A, B, C) over open-ended questions.
*   **Focus**: Nail down the purpose, constraints, and success criteria.

### 2. Exploring Approaches
*   Always propose **2-3 different approaches**.
*   Explain the **trade-offs** (pros/cons) for each.
*   Lead with your **recommended option** and explain why.

### 3. Presenting the Design
*   **Chunking**: Break the design into sections of 200-300 words.
*   **Incremental Validation**: Ask "Does this look right so far?" after each section.
*   **Coverage**: Include architecture, components, data flow, error handling, and testing strategies.
*   **YAGNI**: Ruthlessly cut unnecessary features.

### 4. Output
*   Once the design is validated, write it to a Markdown file (e.g., `docs/plans/YYYY-MM-DD-topic-design.md`).
*   Ask if the user is ready to proceed to **planning** or **implementation**.
