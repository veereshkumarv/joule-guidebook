# SDLC Playbook for SAP AI Delivery (Joule, Studio, BTP, Custom)

Audience: SAP development leads and solution architects. Scope: embedded Joule configuration, Joule Studio skills/agents, and custom BTP builds (CAP, ABAP Cloud, Generative AI Hub). Product specifics marked **[VERIFY]** are tracked in `05-verify-register.md`.

Each phase lists: **Purpose, Activities, Deliverables, Exit gate, Common failure**. Gates are pass/fail; a gate owner signs.

```
0 Discover ─▶ 1 Require ─▶ 2 Design ─▶ 3 Build ─▶ 4 Evaluate ─▶ 5 Release ─▶ 6 Operate ─▶ 7 Optimise/Retire
   G0           G1           G2          G3          G4           G5           (SLOs)         G7
```

## Shared concepts

### Autonomy levels (use in every requirement and design)
| Level | Behaviour | Typical risk tier | Required controls |
|---|---|---|---|
| A0 Inform | Answers questions, cites sources | 1 | Logging, authorization in tools |
| A1 Suggest | Proposes an action or draft; user does everything | 1 to 2 | Evaluation set, citations |
| A2 Act with approval | Prepares the transaction; named human approves; system executes | 2 to 3 | Approval workflow, idempotent API, audit, confirmation text with resolved entities |
| A3 Act autonomously (bounded) | Executes without approval within hard limits (amount, object type, reversible) | 3 | Formal risk sign-off, hard limits enforced in the tool not the prompt, sampling review, kill switch |

Default for pilots: A0 to A2. A3 only after at least one quarter of A2 data showing approval rate > 95% and error rate within threshold agreed with the process owner.

### Roles (minimum)
Product owner (business), delivery lead (you), solution architect, AI/BTP engineer, ABAP/CAP developer, functional consultant, security/identity engineer, QA/eval engineer, change lead. One person can hold two roles on small pilots, but **not** developer and independent security reviewer.

---

## Phase 0: Discover and business case
**Purpose:** decide whether to proceed, on evidence.

**Activities**
1. Score scenarios with the sheet in `03-scenarios/00-scenario-index-and-prioritisation.md`; require a named business owner per scenario.
2. **Measure the baseline** before any build: volumes, handling times (sampled, not guessed; minimum 30 observations or a system-log extract), error/rework rates, cost per transaction. Record the method and who validated it.
3. Define the **value hypothesis** per scenario in one sentence: "If X, then metric M moves from B to T within N weeks, worth V, realised as cash / capacity redeployed to Z / risk avoided."
4. Classify each benefit as **Cashable, Redeployable (named work), Soft, or Risk-avoidance**; only the first two enter the base case (see `08-value-cases/`).
5. Check that a standard embedded capability does not already do it (avoid building what SAP ships).
6. Readiness assessment (T2) and licence check; record red items with owners.
7. Pre-assign provisional risk tier and EU AI Act classification question (HR, credit, employment-related = likely high-risk).
8. Define **kill criteria** up front (e.g. "stop if after 8 weeks of pilot, weekly active use < 40% of invited users or accepted-answer rate < 70%").

**Deliverables:** scored shortlist, baseline report, benefit register (per scenario: low/base/high, type, owner), readiness RAG, funded pilot charter with kill criteria.
**Gate G0:** sponsor and finance sign the baseline and the base-case benefit; pilot funded in tranches (see value cases doc: stage-gated funding).
**Common failure:** baseline estimated from interviews, so savings cannot be proved later.

---

## Phase 1: Requirements
**Purpose:** turn each scenario into testable requirements.

**Functional:** user personas, intents/questions in scope and **explicitly out of scope**, data sources, actions, autonomy level, approvals, notification channels.

**Non-functional (AI-specific; fill all)**
| Quality | Requirement format | Example |
|---|---|---|
| Accuracy | % correct on curated set, per intent class | ≥ 90% overall, ≥ 98% on numeric lookups |
| Groundedness | % answers with valid citation | ≥ 95% |
| Refusal | Must refuse list and expected message | Refuse salary lookups for non-HR personas: 100% |
| Latency | p50/p90 per intent type | p90 < 8 s read, < 15 s for multi-step |
| Availability | SLO and fallback | Fallback to deep link within 3 s of timeout |
| Cost | Max cost per interaction and monthly cap | ≤ EUR 0.05 per read query; alert at 80% |
| Explainability | What the user can see | Sources + resolved entity IDs |
| Language | Languages tested | EN, DE |
| Accessibility | Standard | WCAG 2.2 AA for custom UI |
| Auditability | Fields logged | user, intent, tools, objects, model, tokens, outcome |

**Data requirements:** objects, fields, quality threshold (e.g. ≥ 98% complete vendor master for in-scope company codes), owner of remediation.
**Legal/risk:** DPIA trigger, works-council or employee-representative consultation where required, AI Act classification, sector rules.
**Deliverables:** requirement set with acceptance criteria; risk tier; data-readiness actions; backlog with Definition of Ready met.
**Gate G1:** each requirement has a measurable acceptance criterion; risk tier and autonomy level agreed by product owner and security.
**Common failure:** "answers must be accurate" with no number.

---

## Phase 2: Architecture and design
**Purpose:** make the decisions that are expensive to reverse, early and in writing.

**Activities**
1. Pick the reference architecture (A standard, B extended, C data-driven, D multi-AI) from `01-architecture/ecosystem-architecture.md`. Default to the lowest that meets the requirement.
2. Produce the **starter ADR set** (one ADR each):
   1. Embedded vs Studio vs custom BTP for each scenario
   2. BTP account/subaccount model and region (`02-engineering-standards.md` section 2)
   3. Identity propagation and technical-user policy (`03-secure-by-design.md` section 3)
   4. Model selection and routing policy; approved-model register
   5. Data access: live API vs replicated/semantic layer (BDC/Datasphere)
   6. Retrieval design: chunking, ACL metadata, refresh cadence (if RAG)
   7. Approval and write-back pattern (P4), idempotency and rollback
   8. Observability and evaluation harness
   9. Resilience and fallback behaviour
   10. FinOps: budgets, quotas, caching, chargeback
3. **Threat-model workshop** (security lead facilitates; use STRIDE plus the AI threats in `03-secure-by-design.md`). Output: threat register with owner and mitigation per item.
4. **Conversation and UX design** (section 3 of `02-engineering-standards.md`): journeys, confirmation screens, error states, feedback capture.
5. Tool/API design review: each tool has a schema, scope, idempotency, dry-run, rate limit.
6. Estimate with T3 using delivery actuals; add 15% PM and 15 to 25% contingency.

**Landscape variants to address explicitly**
| Variant | Design implication |
|---|---|
| S/4HANA Cloud public | Embedded and side-by-side only; clean core mandatory |
| S/4HANA private/on-prem | Cloud Connector, released APIs, release/add-on prerequisites **[VERIFY]**; plan replication for analytics |
| ECC or old S/4 release | Most embedded Joule capability will not be available; options: upgrade path, side-by-side agent over APIs/IDocs, or defer. State this in the business case |
| Heavy Z-code | Inventory with ATC; wrap Z-logic behind released-style APIs; do not let agents call unreleased function modules |
| Non-SAP systems in scope | Integration Suite/API Management; MCP only with the controls in `03-secure-by-design.md` section 4 |

**Deliverables:** ADRs, architecture diagram, threat register, UX flows, tool catalogue, estimate, test strategy outline.
**Gate G2:** architecture review board approval; security sign-off on threat register; no open "critical" threat without mitigation.
**Common failure:** building before identity propagation is proven to work end to end.

---

## Phase 3: Build
**Purpose:** deliver in small, evaluated increments.

**Rules** (details in `02-engineering-standards.md`)
- Sprint 0 delivers **platform skeleton**: repos, CI pipeline, environments, eval harness with 10 seed questions, logging, secrets, budget alerts. No feature work before this passes.
- Build **thin vertical slices**: one question or action end to end (identity, API, model, answer, log) before breadth.
- Read-only slice first; write actions only after the read slice passes evaluation.
- Every change is a pull request: code review, automated tests, eval run, security scan.
- Prompts, skill definitions, tool schemas and eval sets live in source control and are versioned together.
- Definition of Done (section "Definitions" below) applies to every story.

**Deliverables:** working increments in Dev, passing CI, updated test bank, updated threat register.
**Gate G3 (code complete):** DoD met; no critical/high defects; evaluation thresholds met in Dev on the synthetic/masked set.

---

## Phase 4: Evaluate (test, security, UAT)
**Purpose:** prove quality, safety and value readiness before real users.

| Test layer | What | Pass criterion |
|---|---|---|
| Unit | Tool functions, validators, formatters | 100% of tools covered; coverage target agreed (suggest ≥ 80% on custom code) |
| Contract/API | Each S/4 or non-SAP API used | Schema and error paths verified; authorization negative tests |
| Evaluation (offline) | 50 to 100+ questions per scenario, by persona, including adversarial | Meets requirement thresholds; run 3 times per question to measure variance |
| Authorization | Low-privilege and cross-role tests in QA with production-like roles | 0 leakage |
| Security | Injection (direct and indirect), exfiltration, tool misuse, cost abuse | All high findings fixed or accepted by risk owner |
| Performance | Load at 2x expected peak concurrency | Latency SLOs met; no throttling failures |
| Resilience | Model/API outage, timeout, malformed output | Fallback works; no data corruption |
| UAT | Real users on real tasks, scripted plus free exploration | Task success ≥ agreed %, SUS/satisfaction ≥ agreed |
| Regression | Re-run after any prompt, model, SAP release change | No drop beyond tolerance |

**Gate G4 (go-live gate):** the security gate in `02-reference/security-identity-reference.md` section 8 plus: evaluation thresholds met in QA, UAT sign-off, support model staffed, runbooks written, rollback tested, kill switch tested, baseline instrumentation live.
**Common failure:** testing with admin users; testing once instead of repeatedly.

---

## Phase 5: Release
**Activities**
1. **Pilot cohort first**: 50 to 200 users, selected to include sceptics, with a matched control group where feasible (needed for credible value proof).
2. Feature flags per skill/action; enable write actions separately from read.
3. Promote via Cloud Transport Management (or the agreed pipeline); no manual changes in Prod.
4. Release checklist: budgets and alerts set, monitoring dashboards live, on-call named, comms sent, training done, rollback plan rehearsed.
5. Hypercare: 2 to 4 weeks, daily triage of failed questions into the test bank.

**Gate G5:** exit hypercare when SLOs met 2 consecutive weeks and open Sev1/Sev2 = 0.

---

## Phase 6: Operate
| Area | Standard |
|---|---|
| Support model | L1 service desk (how-to, access), L2 AI support engineer (answer quality, config), L3 development + SAP incident |
| SLOs | Availability, p90 latency, accepted-answer rate, safety incidents = 0; error budget reviewed monthly |
| Monitoring | Usage, cost per interaction, failed/refused questions, thumbs-down reasons, tool error rates, token consumption by scenario |
| Drift | Weekly sampled review (30 conversations) by product owner; monthly eval re-run on fresh production questions |
| Change | Model version, prompt, skill change = ticketed change with eval evidence; emergency path with post-review |
| SAP release cadence | Regression-run the eval set on each SAP quarterly release and on BTP service updates; subscribe to deprecation notices |
| Model lifecycle | Track model retirement dates; maintain a tested fallback model; no model upgrade without eval re-run |
| Incidents | Playbooks (`03-secure-by-design.md` section 8); post-mortem within 5 working days |
| Cost | Monthly FinOps review: cost per active user and per outcome vs plan |

---

## Phase 7: Optimise and retire
- **Quarterly value review**: KPI delta vs baseline (against control group where available), adoption, cost per outcome. Output: continue, expand, fix, or retire.
- **Retirement criteria** (apply automatically): weekly active users < 20% of target for two consecutive quarters, or cost per outcome above the manual alternative, or the standard SAP capability now covers it.
- **Retire steps:** announce, disable via flag, export logs per retention policy, remove credentials/destinations/role assignments, archive code and eval sets, update the register.
- **Re-assess build vs standard** each quarter against the SAP roadmap; migrating custom skills to embedded standard is a success, not a failure.
- **Gate G7:** documented decision with owner.

---

## Definitions

**Definition of Ready (story):** business outcome and persona stated; autonomy level and risk tier set; data/API available in Dev; acceptance criteria measurable; test questions drafted; security notes included.

**Definition of Done (story):**
- Code reviewed by a second developer; coding standards met; ATC/static checks clean
- Unit and contract tests pass; evaluation set re-run with no regression; new questions added to bank
- Authorization negative test added and passing
- No secrets in code or prompts; dependency scan clean
- Logging fields verified; error and fallback paths tested
- Documentation and runbook updated; prompt and tool versions recorded
- Cost per interaction measured and within budget

## RACI (summary)
| Activity | Product owner | Delivery lead | Architect | Security | QA/Eval | Client IT ops |
|---|---|---|---|---|---|---|
| Baseline and benefit sign-off | A | R | C | I | C | I |
| Architecture decisions | C | R | A | C | I | C |
| Threat model | C | R | C | A | C | I |
| Build | I | A | R | C | R | I |
| Evaluation and go-live gate | A | R | C | R | R | C |
| Operate and incident response | A | C | C | R | C | R |
