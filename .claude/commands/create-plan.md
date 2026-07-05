---
description: Create an implementation plan before making changes
disable-model-invocation: true
---

# /create-plan — Implementation Planning

Create a detailed implementation plan for the requested change. Save it to `plans/` with the naming convention `YYYY-MM-DD-description.md`.

The plan should include:

1. **Context** — What exists today, why this change is needed
2. **Approach** — How we'll implement it, key decisions
3. **Steps** — Numbered implementation steps with enough detail to execute
4. **Files affected** — Which files will be created/modified/deleted
5. **Verification** — How to confirm the implementation is correct
6. **Risks** — Anything that could go wrong or needs careful handling

Do not implement anything yet. Just create the plan and confirm it's ready for review.

Usage: `/create-plan [description of what you want to build or change]`