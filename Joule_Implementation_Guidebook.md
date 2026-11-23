# SAP Joule Implementation Guidebook
### For firm architects and client stakeholders: use cases, architecture, roadmap, budget and value across four pillars (Finance, Efficiency, Security, Performance)

> **Status: DRAFT v0.1.** All costs, percentages and benefit figures are **illustrative planning assumptions**, not SAP list prices or guaranteed outcomes. Validate licensing (Joule entitlements, AI units, BTP consumption) with SAP and calibrate benefits in a client discovery workshop before quoting. Items marked **[VERIFY]** need confirmation against current SAP documentation.

---

## Part 1: Executive Summary (client-facing, 1 page)

**What Joule is:** SAP's generative-AI assistant, embedded across SAP applications (S/4HANA, SuccessFactors, Ariba, Concur, Integrated Business Planning and others). Users ask in natural language and Joule retrieves data, explains it, recommends actions and, increasingly, executes multi-step tasks through AI agents, all within SAP's security and role model.

**Why now:** Clients already hold their most valuable data in SAP. Joule works on that data in place, so there is no separate data-science programme to stand up first. The pre-condition is that master data and authorizations are in good enough shape for the chosen use cases; the readiness phase tests this and remediation is budgeted (see 5.1).

**What we propose:** A phased, value-gated adoption:
1. **Discover and prioritise** (4 weeks): pick 3 to 5 use cases with measurable KPIs.
2. **Pilot** (about 20 weeks: 12 weeks build and security review, 8 weeks live measurement): 2 to 3 use cases with one business unit, with a go/no-go against pre-agreed kill criteria.
3. **Scale** (6 to 12 months): extend to more processes, add custom skills/agents (Joule Studio), and embed governance.

**Headline value logic (to be validated per client):**

| Pillar | How Joule creates value | Typical KPI |
|---|---|---|
| Finance | Faster close, fewer manual reconciliations, better cash/working-capital decisions | Days to close, DSO, cost per invoice |
| Efficiency | Less navigation and searching, automated routine tasks, faster onboarding | Hours saved per user per week, ticket volume, cycle time |
| Security | Role-aware answers (when authorizations are clean), data handling governed by contract and architecture (SAP-hosted by default; any external model only via approved, masked, logged routes), auditable interactions, faster compliance lookups | Audit findings, access-review time, policy-query time |
| Performance | Better decisions from real-time data, fewer stock-outs/delays, better forecast accuracy | Forecast accuracy, OTIF, downtime, error rate |

---

## Part 2: Architecture Guide (for firm architects)

### 2.1 Capability layers

1. **Embedded Joule** in SAP cloud applications: out-of-the-box skills/scenarios per product. Lowest effort, fastest value.
2. **Joule cross-application:** one entry point navigating across SAP solutions (needs the shared Joule/BTP setup and identity).
3. **Joule Studio:** build custom skills and agents (low-code), call APIs/actions, orchestrate business processes. **[VERIFY availability and licensing by region/edition]**
4. **Generative AI Hub / AI Core (SAP BTP):** governed access to LLMs for custom extensions where Joule scenarios do not cover the need.
5. **Business Data Cloud / Datasphere / SAC:** semantic data foundation for analytics-heavy and cross-system questions. **[VERIFY product naming and Joule integration]**
6. **Non-SAP grounding:** documents and knowledge sources through retrieval (document grounding) with strict access controls.

### 2.2 Reference landscape

```
 Users (Fiori Launchpad / Work Zone / Mobile / Teams)
                    |
              SAP Joule (UI)
                    |
        +-----------+------------+
        |                        |
  Embedded skills          Joule Studio (custom skills/agents)
  (S/4, SF, Ariba,                |
   Concur, IBP ...)      BTP: Generative AI Hub / AI Core,
        |                Integration Suite, Build Work Zone,
        |                Event Mesh, Destination service
        |                        |
        +-----------+------------+
                    |
   Identity (IAS/IPS, SSO, role + authorization concepts)
                    |
   Data: S/4HANA, BDC/Datasphere, document grounding, 3rd-party APIs
```

### 2.3 Architecture decision checklist

| Area | Questions the architect must answer |
|---|---|
| Landscape readiness | Cloud (public/private) or on-premise S/4? Which release/support pack? Clean-core status? Is a cloud connector or hybrid needed? |
| Identity | IAS/IPS in place? SSO to all SAP and non-SAP sources? Are authorization roles clean enough that Joule will not surface data users should not see? |
| Data quality | Master-data quality for chosen use cases (vendors, materials, GL). Poor data produces poor answers. |
| Integration | Which APIs/OData services and events are exposed? Rate limits? |
| Custom vs standard | Does a standard Joule scenario cover it? Only build in Joule Studio when it does not. |
| Governance | Who approves new skills/agents? Prompt/answer logging, human-in-the-loop for write actions, model change control. |
| Region and compliance | Data residency, GDPR/sector rules, AI-regulation obligations (e.g. EU AI Act risk classification). |
| Non-functional | Latency targets, availability, support model, monitoring of usage and answer quality. |

### 2.4 Design principles

- **Standard first, extend second.** Use embedded scenarios before building custom agents.
- **Read before write.** Start with Q&A/summaries; add transactional actions with approvals once trust is established.
- **Authorization is the security boundary.** Joule must inherit user roles; fix role design before rollout.
- **Human in the loop** for financial postings, master-data changes, and anything irreversible.
- **Measure from day 0.** Baseline KPIs before the pilot or value cannot be proven.

---

## Part 3: Use-Case Catalogue (with pillar mapping)

Rating: Effort (L/M/H), Value (L/M/H). Pillars: **F**inance, **E**fficiency, **S**ecurity, **P**erformance.

### Finance (S/4HANA Finance, Concur, Ariba)

| # | Use case | Example prompt | Pillars | Effort | Value |
|---|---|---|---|---|---|
| F1 | Period-end close assistant | "Which close tasks are overdue and who owns them?" | F, E | M | H |
| F2 | Variance explanation | "Why is marketing cost 12% above plan in Q3?" | F, P | M | H |
| F3 | Accounts payable exception handling | "Show blocked invoices over 10k and the reason" | F, E | M | H |
| F4 | Cash and working-capital insight | "What is our overdue receivables by customer segment?" | F, P | M | H |
| F5 | Expense policy Q&A and audit assist (Concur) | "Is this hotel claim within policy?" | F, S | L | M |

### Efficiency (cross-functional)

| # | Use case | Example prompt | Pillars | Effort | Value |
|---|---|---|---|---|---|
| E1 | Natural-language navigation and "how do I" help | "How do I create a goods receipt for PO 4500001234?" | E | L | M |
| E2 | Procurement: requisition and sourcing help | "Create a requisition for 20 laptops, standard config" | E, F | M | H |
| E3 | HR: employee self-service and onboarding (SuccessFactors) | "Summarise my team's open requisitions" | E | L | M |
| E4 | Document and email summarisation, job-description or text drafting | "Draft a job posting for a plant engineer" | E | L | M |
| E5 | Service/IT ticket deflection | "Why was my access request rejected?" | E, S | M | M |

### Security and compliance

| # | Use case | Example prompt | Pillars | Effort | Value |
|---|---|---|---|---|---|
| S1 | Role-aware data access (inherent control) | n/a: design property, verified in pilot | S | L | H |
| S2 | Policy and control lookup | "What is our approval limit for contracts above 100k?" | S, E | L | M |
| S3 | Access-review and SoD analysis assistance | "Which users have both vendor-create and payment-run rights?" | S, F | H | H |
| S4 | Audit evidence gathering | "Collect evidence for control X for Q3" | S, F, E | H | H |

### Performance (supply chain, manufacturing, planning)

| # | Use case | Example prompt | Pillars | Effort | Value |
|---|---|---|---|---|---|
| P1 | Supply-chain disruption insight | "Which open sales orders are at risk from supplier delays?" | P, F | M | H |
| P2 | Inventory and demand planning assistant | "Which materials will stock out in 4 weeks?" | P, F | M | H |
| P3 | Maintenance/plant-performance Q&A | "Top 5 downtime causes this month at Plant 1010" | P, E | M | M |
| P4 | Sales: order status and customer insight | "Status of all orders for customer ACME" | P, E | L | M |

**Prioritisation method:** score each use case 1 to 5 on Value, Feasibility (data and system readiness), Adoption likelihood and Risk (inverse). Pick the top 3 to 5 with at least one from each of two different pillars so the story is balanced.

---

## Part 4: Worked Sample Use Cases (for the presentation)

All numbers are **illustrative** for a hypothetical mid-size manufacturer (EUR 800M revenue, 2,500 SAP users, 4 plants). Replace with client data.

### Sample A: Accounts Payable exception handling (Finance + Efficiency)
- **Problem:** AP team spends about 35% of time chasing blocked/mismatched invoices across screens.
- **Solution:** Joule summarises blocked invoices, explains the block reason (price/quantity mismatch), proposes the next action and routes to the buyer; posting stays human-approved.
- **Baseline:** 40,000 invoices/year, 9% exceptions, 25 min handling each.
- **Target:** reduce handling time by 40%.
- **Benefit:** 3,600 exceptions x 25 min x 40% = 600 hours/year. At EUR 55/hour loaded = **about EUR 33k/year direct**, plus faster early-payment discount capture (illustrative EUR 40 to 80k/year).
- **Honest note:** direct labour savings alone are modest; the case is stronger when cash/discount capture and error reduction are included. The 600 hours are **capacity, not cash**: they count as a hard benefit only if overtime, contractors or headcount actually fall, or if the hours are redeployed to named work (rule 5.4). Otherwise report them as redeployable.

### Sample B: Variance explanation for controllers (Finance + Performance)
- **Problem:** Controllers spend 2 to 3 days each month assembling explanations.
- **Target:** cut by 50% across 12 controllers: 12 x 2.5 days x 12 months x 50% = 180 days/year, about **EUR 100k/year** at EUR 550/day loaded, plus faster decisions.

### Sample C: Supply-chain disruption insight (Performance + Finance)
- **Problem:** Late supplier deliveries found after the customer is affected.
- **Target:** early-warning reduces expedite costs and penalties by 10%.
- **Benefit:** if expedite and penalty cost is EUR 2M/year, **EUR 200k/year**. This depends heavily on data quality and process change, so treat as the upside case.

### Sample D: Secure policy and access assistant (Security + Efficiency)
- **Problem:** Repetitive policy/access questions go to GRC and the IT service desk.
- **Target:** deflect 25% of 6,000 tickets/year at EUR 18 each = **about EUR 27k/year**, plus reduced policy-violation risk (not monetised here).

**Presentation message:** the direct hard savings of a first pilot are typically modest; the strategic value comes from scale across processes, risk reduction, and decision speed. Present both honestly. That is what earns client trust.

---

## Part 5: Budget Model

### 5.1 Cost components

| Component | Description | Basis |
|---|---|---|
| Licensing/entitlement | Joule included with some SAP cloud subscriptions; premium capabilities, Joule Studio, and AI units may be extra **[VERIFY with SAP account team]** | SAP contract |
| BTP consumption | AI Core / Generative AI Hub, Integration Suite, Build Work Zone | Usage/credits |
| Implementation services | Discovery, config, integration, custom skills/agents, testing | Our T&M or fixed fee |
| Data and security remediation | Master-data cleansing, role redesign | Services |
| Change management and training | Champions, enablement, comms | Services |
| Run and governance | Monitoring, model/skill updates, support, AI governance board | Annual |

### 5.2 Illustrative budget scenarios (EUR, services + platform, excluding SAP licence uplift)

| Phase | Small client (500 users) | Mid client (2,500 users) | Large client (10,000+ users) |
|---|---|---|---|
| Discovery and prioritisation (4 wks) | 30 to 50k | 50 to 90k | 90 to 150k |
| Pilot (2 to 3 use cases, 8 to 12 wks) | 120 to 200k | 200 to 350k | 350 to 600k |
| Scale-out (year 1) | 150 to 300k | 400 to 800k | 800k to 2M |
| Change mgmt and training | 30 to 60k | 80 to 150k | 150 to 400k |
| Annual run and governance | 40 to 80k | 100 to 200k | 200 to 500k |
| BTP/AI consumption (annual) | 10 to 40k | 40 to 120k | 120 to 400k |
| **Year 1 total (indicative)** | **~380k to 730k** | **~870k to 1.7M** | **~1.7M to 4.0M+** |

These ranges are placeholders to be rebuilt from our rate card, team mix and the client's scope.

### 5.3 ROI framing for a mid client (illustrative)

| Item | Year 1 | Year 2 | Year 3 |
|---|---|---|---|
| Investment | 1.2M | 0.4M | 0.4M |
| Hard benefits (labour, discounts, expedite, tickets) | 0.3M | 0.9M | 1.4M |
| Soft/risk benefits (not counted) | n/a | n/a | n/a |
| Cumulative net | -0.9M | -0.4M | +0.6M |

Break-even in about year 3 under these assumptions. Sensitivity matters: show a conservative (-30% benefits), base and optimistic (+30%) case. Do not promise a payback you cannot defend.

> **Reconciliation warning (v0.3):** the four worked samples in Part 4 total only about EUR 0.42M a year, and mostly capacity rather than cash. The 0.9M (Y2) and 1.4M (Y3) hard benefits above are placeholders for benefits from roughly 10 to 15 further scenarios at scale and are **not yet evidenced**. Do not present this table to a client. Use the rebuilt, evidence-based and discounted model in `08-value-cases/` instead.

### 5.4 Value realisation rules
- Agree KPI baselines before the pilot starts and who signs off the measurement.
- Count only benefits that are either cashable or redeployed to named higher-value work.
- Track adoption (weekly active users, prompts per user) alongside KPIs; low adoption is the commonest reason value fails.

---

## Part 6: Implementation Roadmap

| Phase | Weeks | Key activities | Exit gate |
|---|---|---|---|
| 0. Readiness | 1 to 4 | Landscape/identity/data assessment, use-case scoring, measured KPI baselines, licence check, kill criteria | Approved shortlist + business case + signed baseline |
| 1. Pilot build | 5 to 16 | Enable embedded Joule, configure, build 0 to 2 custom skills, security review, UAT | KPI movement shown with pilot users |
| 2. Pilot run | 17 to 24 | Real usage with 50 to 200 users, measure, collect feedback, tune | Go/no-go for scale vs. targets |
| 3. Scale | 6 to 12 months | More users and processes, Joule Studio agents, training, governance board | Benefits tracked quarterly |
| 4. Optimise | Ongoing | Usage analytics, new scenarios from SAP roadmap, cost control | Annual value review |

**Team (typical):** Engagement lead, Solution architect, BTP/AI engineer, 1 to 2 functional consultants per process, security/identity specialist, change lead, client product owner and business champions.

---

## Part 7: Risk and Governance

| Risk | Mitigation |
|---|---|
| Wrong or hallucinated answers | Grounding in SAP data, show sources, human approval for write actions, test sets of real questions |
| Data exposure via over-broad roles | Role clean-up before go-live, test with low-privilege users |
| Low adoption | Champions, in-flow prompts, role-based training, usage dashboards |
| Benefit overstatement | Baselines, conservative cases, finance sign-off |
| Cost creep (consumption) | Budgets/alerts on BTP usage, review custom builds against standard scenarios |
| Regulatory (AI Act, privacy) | Risk classification per use case, DPIA where needed, AI governance board, audit logs |
| Vendor roadmap change | Prefer standard scenarios; quarterly roadmap review with SAP |

---

## Part 8: Presentation Deck Outline (≈ 20 slides)

**Client version**
1. Title: "From SAP data to decisions: Joule for [Client]"
2. Why AI in your SAP landscape now (market and your goals)
3. What Joule is (one visual, plain language)
4. How it stays secure: roles, trust boundary, audit
5. Four value pillars (Finance, Efficiency, Security, Performance)
6. Use-case map (heatmap of value vs. effort)
7. Sample use case A, with a "day in the life" before/after
8. Sample use case B or C
9. Sample use case D (security)
10. Live demo or recorded demo
11. Business case: investment vs. benefits (3 scenarios)
12. Budget by phase
13. Roadmap (timeline)
14. Risks and how we control them
15. Governance model
16. Success metrics and how we'll prove them
17. Team and our approach
18. What we need from you (sponsor, data, SMEs)
19. Next step: 4-week readiness assessment (fixed fee)
20. Appendix: architecture, assumptions, FAQ

**Internal architect add-ons**
- Landscape readiness checklist (Part 2.3), integration patterns, Joule Studio design standards, estimation worksheet, reusable test-question bank, demo environment setup.

---

## Part 9: FAQ (client objections)

- **"Is our data used to train models?"** Confirm SAP's current data-handling commitments in writing **[VERIFY]**; present the contractual position, not assumptions.
- **"Can Joule post transactions on its own?"** Only where configured; recommend approval steps initially.
- **"What if the answer is wrong?"** Sources shown, test sets, feedback loop, and human review for critical actions.
- **"Do we need to be on S/4HANA Cloud?"** Capabilities differ by deployment and release **[VERIFY]**; assess in Phase 0.
- **"What does it cost beyond your fees?"** Licence/AI units and BTP consumption: itemised in the business case after SAP confirmation.

---

## Part 10: Next Steps for the Firm

1. Confirm target audience and industry (manufacturing, retail, utilities, etc.) to tailor use cases.
2. Fill in our real rate card to replace the Part 5 placeholders.
3. Get current SAP Joule licensing/packaging from the SAP partner team and resolve all **[VERIFY]** items.
4. Build the PowerPoint from Part 8 and a demo script on a sandbox/trial tenant.
5. Run a dry-run with an internal "mock client" before the first pitch.
