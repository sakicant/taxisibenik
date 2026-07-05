---
name: onboarding-guide
description: Create onboarding documentation and walkthroughs for new team members.
triggers:
  - create onboarding
  - new team member guide
  - getting started guide
---

# Onboarding Guide

You create onboarding documentation that gets new team members productive fast. The measure of a good onboarding guide is time to first meaningful contribution.

## Gather Context First

Check `context/` for existing team structure, tech stack, and process documentation. Ask only for what is missing:
1. **What role is being onboarded?** Engineer, designer, PM, sales, ops.
2. **What tools and systems do they need access to?**
3. **What does "productive" mean for this role?** First PR merged, first deal closed, first campaign launched.
4. **Who is the onboarding buddy or manager?**

## Onboarding Structure: The 30-60-90 Framework

### Pre-Day 1 (before they start)
- Account creation checklist (email, Slack, GitHub, tools).
- Hardware/software setup instructions sent in advance.
- Welcome message from the team with what to expect on Day 1.
- Onboarding buddy assigned and introduced.

### Day 1: Orient

**Morning (2 hours):**
1. Welcome meeting with manager: team mission, how this role fits, 30-day expectations.
2. Environment setup walkthrough (follow the step-by-step guide, note any failures).
3. Tour of key tools: where code lives, where docs live, where communication happens.

**Afternoon (2 hours):**
4. Architecture overview: one page, not a novel. Diagram of how systems connect.
5. Team norms doc: communication channels, meeting cadence, how decisions get made.
6. First task assigned: something small, completable in 1-2 hours, that touches the real codebase or workflow.

### Week 1: Learn (Days 2-5)

| Day | Focus | Outcome |
|-----|-------|---------|
| 2 | Codebase walkthrough (or process walkthrough for non-eng) | Can navigate the repo/tool |
| 3 | Shadow a teammate on a real task | Understand the daily workflow |
| 4 | Complete a guided task independently | First real contribution |
| 5 | 1:1 with manager: questions, blockers, initial impressions | Feedback loop established |

Key deliverables by end of Week 1:
- Dev environment fully working (or tool access fully configured).
- First small contribution completed (PR merged, task closed, etc.).
- Knows who to ask for what.
- Understands the team's current priorities.

### Days 8-30: Contribute
- Take on progressively larger tasks.
- Attend all team ceremonies and understand their purpose.
- Read the last 3 months of decision docs or meeting notes.
- Have 1:1s with 3-5 cross-functional partners.
- End of month: present what you have learned and what you would change.

### Days 31-60: Own
- Own a feature, project, or process end-to-end.
- Identify one improvement and propose it.
- Start contributing to team discussions and decisions.
- Mentor the next new hire on what you wish you had known.

### Days 61-90: Lead
- Drive a project or initiative independently.
- Contribute to team strategy or roadmap discussions.
- Update the onboarding guide based on your experience.

## Environment Setup Guide Template

Write setup instructions as a numbered checklist:

```markdown
## Environment Setup

### Prerequisites
- [ ] [Tool] version [X.Y] installed
- [ ] [Account] access granted

### Steps
1. Clone the repository: \`git clone [repo-url]\`
   Expected output: [what they should see]
2. Install dependencies: \`[command]\`
   Expected output: [what they should see]
3. Run the app: \`[command]\`
   Expected output: [what they should see]

### Troubleshooting
- **"Permission denied"**: [solution]
- **"Module not found"**: [solution]
```

Test these instructions on a clean machine before every new hire.

## Output Format

Save onboarding materials to `outputs/onboarding/`:

```
outputs/onboarding/
  day-1-guide.md
  environment-setup.md
  team-norms.md
  architecture-overview.md
  30-60-90-plan.md
  access-checklist.md
```

## Do NOT
- Dump a 50-page wiki on someone's first day. Sequence information over days.
- Skip testing the setup guide. If it fails on a fresh machine, it will fail for the new hire.
- Assume knowledge of internal acronyms, tools, or processes.
- Forget to assign an onboarding buddy. New hires need a safe person to ask "dumb" questions.
- Treat onboarding as a one-time event. It is a 90-day process.
- Leave the guide stale. Every new hire should update it when they finish onboarding.