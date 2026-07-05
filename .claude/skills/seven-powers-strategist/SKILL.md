---
name: seven-powers-strategist
description: Evaluate a business or product's competitive moat using Hamilton Helmer's 7 Powers framework. Use when assessing strategic positioning, evaluating competitors, or deciding where to invest for durable advantage.
triggers:
  - seven powers
  - competitive moat
  - strategic advantage
  - 7 powers analysis
---


## Read context first

Before answering, read `context/gtm.md` if it exists. It captures the company's positioning, ICP, value propositions, voice, and competitive landscape — use it and only ask the user for details that aren't already covered.

If `context/gtm.md` is missing, suggest running the `gtm-context-builder` skill once before continuing. The output of every GTM skill is sharper when this foundation is in place.


# Seven Powers Strategist

A business is durable only if it has at least one Power — a structural condition that creates persistent differential returns. Analyze where power exists, where it could be built, and where your position is vulnerable.

## The Seven Powers

Evaluate the subject against each power. For each, determine: present (strong evidence), emerging (early signs), absent (no evidence), or not applicable.

### 1. Scale Economies
Unit costs decline as volume increases, and competitors cannot easily match your scale.

**Test:** Would a new entrant at 1/10th your volume face meaningfully higher unit costs?
**Indicators:** Fixed cost dominance, network infrastructure, bulk purchasing leverage, R&D amortization
**Example:** AWS, where massive server fleets drive costs below what smaller providers can match.

### 2. Network Effects
The product becomes more valuable as more people use it.

**Test:** Does each new user make the product better for existing users?
**Types:** Direct (same-side: more users = more value), Indirect (cross-side: more buyers attract more sellers), Data (more usage = better algorithms)
**Example:** LinkedIn, where each new profile makes the network more useful for recruiters and job seekers.

### 3. Counter-Positioning
Your business model is something incumbents cannot copy without damaging their existing business.

**Test:** Would a rational incumbent choose not to adopt your approach even after seeing it work?
**Indicators:** Channel conflict, margin compression, cannibalization of existing revenue
**Example:** Netflix streaming vs. Blockbuster's physical stores.

### 4. Switching Costs
Customers face real costs (time, data, learning, integration) if they switch away.

**Test:** Would a customer switch to a free, slightly better alternative tomorrow?
**Types:** Financial (contracts, migration), Procedural (retraining, workflow change), Relational (loss of history, trust)
**Example:** Salesforce, where years of customization and team training create high switching friction.

### 5. Branding
A durable positive association in the customer's mind that justifies premium pricing or preferential choice.

**Test:** Would customers pay more or choose you over an identical unbranded alternative?
**Indicators:** Price premium, unprompted recall, emotional attachment, trust during uncertainty
**Example:** Apple, where brand perception justifies hardware pricing above spec-equivalent competitors.

### 6. Cornered Resource
Exclusive access to a valuable asset — talent, IP, data, regulatory license, or supply.

**Test:** Could a well-funded competitor reproduce this resource?
**Types:** Patents, exclusive data sets, regulatory approvals, key personnel, geographic rights
**Example:** Qualcomm's patent portfolio on cellular technology.

### 7. Process Power
An organization has embedded a superior way of operating that competitors cannot easily replicate even if they understand it.

**Test:** If you published your process in detail, could competitors match your output within two years?
**Indicators:** Culture-dependent, requires years of refinement, tacit knowledge embedded in teams
**Example:** Toyota Production System, where decades of continuous improvement are baked into operations.

## Evaluation

### Power Assessment Table
| Power | Status | Evidence | Strength (1-5) | Durability (1-5) |
|-------|--------|----------|-----------------|-------------------|
| Scale Economies | | | | |
| Network Effects | | | | |
| Counter-Positioning | | | | |
| Switching Costs | | | | |
| Branding | | | | |
| Cornered Resource | | | | |
| Process Power | | | | |

### Synergies
Identify where powers reinforce each other. Network effects + switching costs is a classic combination. Scale + process power creates compounding advantages.

### Vulnerabilities
Where is the position weakest? Which powers could erode? What would a well-funded competitor target first?

## Output

Write the analysis to `outputs/seven-powers-[subject].md`:

1. **Subject** — what you are analyzing
2. **Power Assessment** — the table above with evidence
3. **Strongest Powers** — where the moat is deepest, with reasoning
4. **Vulnerabilities** — where the position is weakest
5. **Strategic Recommendations** — where to invest to build or strengthen power

## Do NOT
- Claim a power exists without specific evidence — "we have a good brand" is not branding power
- Confuse operational advantages with structural powers — being good at something is not the same as having a moat
- Evaluate all seven equally when only two or three matter for the business stage
- Ignore that powers are dynamic — what exists today can erode