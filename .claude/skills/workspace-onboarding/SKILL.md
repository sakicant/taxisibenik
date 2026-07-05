---
name: workspace-onboarding
description: Systematically explore a workspace to understand its structure, tech stack, key patterns, and how to work in it. Use when joining a new project, inheriting a codebase, or orienting in an unfamiliar workspace.
triggers:
  - onboard me
  - explore this project
  - what is this project
  - new to this workspace
---

# Workspace Onboarding

Explore this workspace systematically and produce a clear summary of what it is, how it works, and how to get started. This works for any project with files — not just code.

## Phase 1 — Identify the Project

Gather basic facts:

1. **Name and purpose.** Check README, CLAUDE.md, package.json, or any root-level docs for a project description.
2. **Tech stack.** Scan dependency files: package.json, Cargo.toml, pyproject.toml, go.mod, pom.xml, Gemfile, requirements.txt.
3. **Language and framework.** Identify the primary language and any frameworks from dependencies and file extensions.
4. **Build system.** Look for Makefile, scripts in package.json, CI configs (.github/workflows, .gitlab-ci.yml, Jenkinsfile).
5. **Age and activity.** Check git log for first commit date, last commit date, and commit frequency.

## Phase 2 — Map the Structure

Understand how files are organized:

1. **Top-level directories.** List and describe the purpose of each directory at the root.
2. **Key files.** Identify entry points: main.ts, index.html, app.py, main.go, etc.
3. **Configuration.** List config files and what they control (tsconfig, eslint, prettier, docker-compose, etc.).
4. **Documentation.** Identify all docs: README, CLAUDE.md, context/, reference/, docs/, wiki/.
5. **Tests.** Locate test directories and identify the testing framework.

## Phase 3 — Understand the Patterns

Identify how work is done in this project:

1. **Code organization.** Is it feature-based, layer-based, or domain-driven?
2. **State management.** How is state handled? (Store, context, database, files)
3. **Data flow.** Trace a typical operation from input to output.
4. **Error handling.** How are errors handled? Custom error types? Error boundaries?
5. **Naming conventions.** File naming, variable naming, function naming patterns.
6. **Import conventions.** Absolute vs relative imports, barrel files, path aliases.

## Phase 4 — How to Run It

Document the practical operations:

1. **Install dependencies.** What command installs everything needed?
2. **Start development.** How to run the project locally.
3. **Run tests.** How to run the test suite.
4. **Build for production.** How to create a production build.
5. **Deploy.** How deployment works (if discoverable from config/scripts).
6. **Environment variables.** What env vars are needed? (List names, not values)

## Phase 5 — Key Decisions and Constraints

Surface important context:

1. **Architecture decisions.** Any ADRs, decision logs, or documented constraints?
2. **Known limitations.** Any TODOs, FIXMEs, or known issues documented?
3. **Dependencies on external services.** APIs, databases, third-party tools.
4. **Access requirements.** What credentials or accounts are needed to work here?

## Output

Write the onboarding summary to `outputs/workspace-onboarding.md`:

```markdown
# Workspace Onboarding: [Project Name]
Date: [today]

## What This Is
[1-3 sentences]

## Tech Stack
| Component | Technology |
|-----------|-----------|

## Directory Structure
[Tree with descriptions]

## How to Run
[Commands with explanations]

## Key Patterns
[Bullet list of important conventions]

## Important Context
[Anything a newcomer must know]

## Open Questions
[Things that were unclear during exploration]
```

## Do NOT
- Skip any phase — even if the project seems simple, check everything
- Assume the README is current — verify claims against the actual files
- Ignore non-code files — context/, docs/, and config files are often more valuable than code for orientation
- Read every file in detail — scan broadly first, then dive into key files