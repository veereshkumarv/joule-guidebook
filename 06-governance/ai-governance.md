# AI Governance and Operating Model

## 1. Roles
| Role | Responsibility |
|---|---|
| Executive sponsor | Funding, priorities, value accountability |
| AI governance board | Approves scenarios by risk tier, models, policies |
| Product owner (per scenario) | Backlog, KPIs, adoption |
| AI/solution architect | Design standards, pattern selection |
| Security and privacy officer | Threat model, DPIA, access |
| Data steward | Source quality, document approval |
| Platform team | BTP operations, cost, monitoring |
| Change lead | Training, communications |

## 2. Risk tiering and required controls

| Tier | Examples | Required controls |
|---|---|---|
| 1 Low | Navigation help, summaries of non-sensitive data | Standard security review, usage logging |
| 2 Medium | Drafts, recommendations, sensitive internal data | Evaluation set, citations, role tests, owner sign-off |
| 3 High | Postings, master-data changes, HR decisions, regulated or safety processes, external communications | Formal risk assessment, human approval, red-team, legal/compliance sign-off, periodic re-validation |

## 3. Lifecycle gates
1. **Idea:** one-pager, tier assigned.
2. **Design:** ADR, threat model, data and model approvals.
3. **Build:** source-controlled prompts/skills, test bank.
4. **Evaluate:** quality, security, bias, performance thresholds met.
5. **Release:** change control, kill switch, runbook.
6. **Operate:** monitoring, feedback, incident process.
7. **Review:** quarterly value and risk review; retire unused scenarios.

## 4. Evaluation metrics
| Dimension | Metric |
|---|---|
| Accuracy | % answers judged correct on test bank |
| Groundedness | % answers with valid source |
| Safety | Injection/leakage test pass rate |
| Latency | p50/p90 response time |
| Adoption | Weekly active users, prompts/user |
| Value | KPI delta vs. baseline |
| Cost | Cost per interaction, monthly spend vs. budget |
| Satisfaction | Thumbs up/down, survey |

## 5. Cost control practices
- Budget per scenario and per environment; alerts at 50/80/100%.
- Smaller models for simple tasks; caching; shorter contexts.
- Quarterly rationalisation of unused skills.

## 6. Change management
- Champions network (1 per 50 users).
- Role-based training with real prompts from the test bank.
- "Prompt library" for each function.
- Communicate what AI will and will not do; address job-impact concerns openly; consult employee representatives where required.

## 7. Incident handling
Define severities (wrong answer causing financial impact, data exposure, harmful content). Steps: contain (kill switch), assess, notify (privacy/regulator if applicable), fix, post-mortem, update test bank.

## 8. Continuous improvement
Feed production questions that failed into the test bank; review SAP release notes and roadmap each quarter; re-assess "build vs. standard" as SAP adds capabilities.
