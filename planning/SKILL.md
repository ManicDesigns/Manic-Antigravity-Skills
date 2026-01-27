---
name: planning
description: Generates detailed, step-by-step implementation plans for complex tasks. Use when a design is ready, before writing code, or when the user asks for a "plan".
---

# Planning

## When to Use This Skill
- A design or detailed requirement list exists
- The task involves multiple files or complex logic
- User asks for an "implementation plan"
- You need to break down a large feature into safe steps

## Workflow

- [ ] **Phase 1: Context** - Establish the goal, architecture, and tech stack.
- [ ] **Phase 2: Task Breakdown** - extensive breakdown into bite-sized (2-5 min) steps.
- [ ] **Phase 3: Validation** - Ensure every step has a verification method (test, build, or manual check).

## Instructions

### 1. The Mindset
*   Assume the implementer has **zero context** and **questionable taste**.
*   **Detailed**: Explicitly state which files to create, modify, or delete.
*   **Bite-Sized**: Each step should be roughly 2-5 minutes of work.
*   **TDD**: Write the test -> Fail -> Implement -> Pass -> Commit.

### 2. Plan Structure
Every plan **MUST** start with the standard header and follow the strict task structure.

**👉 [See Plan Header Template](resources/plan-header-template.md)**
**👉 [See Task Structure Template](resources/task-structure-template.md)**

### 3. Granularity Rules
*   **Exact Paths**: Always use full file paths (e.g., `src/components/Button.tsx`).
*   **Complete Code**: Do not say "add validation"; provide the snippet.
*   **Exact Commands**: Provide the exact `npm run test ...` command to verify.

### 4. Execution Handoff
After saving the plan (e.g., to `docs/plans/YYYY-MM-DD-feature.md`), offer:
1.  **Subagent-Driven**: Dispatching subagents for each task (faster iteration).
2.  **Sequential**: Executing step-by-step in the current session.
