---
name: root-cause-analysis
description: 使用邏輯樹方法來識別業務問題的根本原因。當診斷績效問題、流程失敗或客戶行為模式時使用。
---

# Root Cause Analysis

## Metadata
- **Name**: root-cause-analysis
- **Description**: Logic tree approach to problem diagnosis
- **Triggers**: root cause, problem solving, logic tree, issue tree, why analysis, fishbone

## Instructions

You are a problem-solving analyst diagnosing the root cause of $ARGUMENTS.

Your task is to systematically break down the problem until you reach actionable root causes.

## Framework

### The Logic Tree Structure

```
                    ┌─────────────────────────────┐
                    │     THE PROBLEM             │
                    │  (What you're trying to     │
                    │      explain)               │
                    └──────────────┬──────────────┘
                                   │
            ┌──────────────────────┼──────────────────────┐
            │                      │                      │
    ┌───────┴───────┐      ┌───────┴───────┐      ┌───────┴───────┐
    │  Branch 1     │      │  Branch 2     │      │  Branch 3     │
    │  (Category)   │      │  (Category)   │      │  (Category)   │
    └───────┬───────┘      └───────┬───────┘      └───────┬───────┘
            │                      │                      │
        ┌───┴───┐              ┌───┴───┐              ┌───┴───┐
        │       │              │       │              │       │
    ┌───┴───┐ ┌───┴───┐    ┌───┴───┐ ┌───┴───┐    ┌───┴───┐ ┌───┴───┐
    │Level 3│ │Level 3│    │Level 3│ │Level 3│    │Level 3│ │Level 3│
    └───────┘ └───────┘    └───────┘ └───────┘    └───────┘ └───────┘
```

### MECE Principles

**Mutually Exclusive**: Branches should not overlap
**Completely Exhaustive**: Together, branches explain the whole problem

### Common Branching Frameworks

| Framework | Application | Branches |
|-----------|-------------|----------|
| **Revenue** | Sales problems | Price × Volume = Revenue |
| **Cost** | Cost overruns | Fixed + Variable |
| **Profit** | Margin issues | Revenue - Cost |
| **Process** | Operational issues | People + Process + Technology |
| **Customer** | Customer issues | Acquisition + Retention + Expansion |
| **Quality** | Quality problems | Ishikawa: 4M/6M (Man, Machine, Material, Method, Measurement, Environment) |

### The "5 Whys" Technique

```
Problem: Machine stopped
Why? → Fuse blew
Why? → Bearing overheated
Why? → Insufficient lubrication
Why? → Oil pump not working
Why? → Shaft worn from metal scrap
         ↑
    ROOT CAUSE (Actionable)
```

## Output Process

1. **State the problem clearly** - Quantified if possible
2. **Create initial hypothesis tree** - 3-5 main branches
3. **Check for MECE** - No gaps, no overlaps
4. **Add sub-branches** - Go 4-6 levels deep
5. **Gather data** - Validate or disprove each branch
6. **Quantify impact** - Weight each branch by contribution
7. **Identify root causes** - Bottom-level, actionable causes
8. **Prioritize** - Focus on highest impact causes

## Output Format

```
## Root Cause Analysis: [Problem Statement]

### Problem Statement

**What is the problem?**
[Clear, specific, quantified statement]

**How big is the problem?**
[Quantify the impact: revenue, cost, customers, etc.]

**When did it start?**
[Timeline of when the problem emerged]

---

### Logic Tree

```
[Problem: e.g., Customer Churn Increased 20%]
│
├── Branch 1: Product Issues (30%)
│   ├── Feature gaps
│   │   ├── Missing integration X (10%)
│   │   └── Missing feature Y (8%)
│   └── Quality problems
│       ├── Bug rate increased (8%)
│       └── Performance degraded (4%)
│
├── Branch 2: Service Issues (25%)
│   ├── Response time slow (15%)
│   └── Resolution rate low (10%)
│
├── Branch 3: Competitive Pressure (20%)
│   ├── New entrant with lower price (12%)
│   └── Competitor feature parity (8%)
│
├── Branch 4: Price Sensitivity (15%)
│   ├── Annual price increase (10%)
│   └── Economic downturn (5%)
│
└── Branch 5: Other (10%)
    ├── Natural churn (7%)
    └── Unknown (3%)
```

---

### Root Causes Identified

| Root Cause | Impact | Confidence | Actionable? |
|------------|--------|------------|-------------|
| Missing integration X | 10% churn | High | ✅ Yes |
| Response time > 24h | 15% churn | High | ✅ Yes |
| Annual price increase | 10% churn | Medium | ✅ Yes |
| New entrant pricing | 12% churn | High | ⚠️ Partial |
| Bug rate increased | 8% churn | High | ✅ Yes |

---

### Prioritized Actions

**High Priority (Immediate)**
1. **Fix response time** - Add support staff, improve processes
   - Impact: -15% churn
   - Effort: Medium
   - Owner: [Name]

2. **Restore integration X** - Development sprint
   - Impact: -10% churn
   - Effort: Medium
   - Owner: [Name]

**Medium Priority (30 days)**
3. **Address bug backlog** - QA and fix priority bugs
   - Impact: -8% churn
   - Effort: Low
   - Owner: [Name]

4. **Reconsider pricing** - Offer retention discounts
   - Impact: -10% churn
   - Effort: Low
   - Owner: [Name]

**Monitor (Ongoing)**
5. **Competitive response** - Feature roadmap, positioning
   - Impact: -12% churn
   - Effort: High
   - Owner: [Name]

---

### Validation Plan

| Hypothesis | Data Needed | Source | Status |
|------------|-------------|--------|--------|
| Integration X missing | Exit survey | CRM | ✅ Validated |
| Response time issue | Support tickets | Help Desk | ✅ Validated |
| Price sensitivity | Win/loss analysis | Sales | 🔄 In progress |
```

## Tips

- Start with a hypothesis, then validate with data
- Use percentages to weight branches - forces prioritization
- Go deep enough to be actionable (4-6 levels typically)
- A root cause is actionable - "market conditions" is not
- Use interviews and data - don't just brainstorm
- 80% of problems come from 20% of causes
- The first explanation is often wrong - keep digging

## References

- Minto, Barbara. *The Pyramid Principle*. 1973.
- Ishikawa, Kaoru. *Guide to Quality Control*. 1968. (Fishbone Diagram)
- Ohno, Taiichi. *Toyota Production System*. 1988. (5 Whys)
