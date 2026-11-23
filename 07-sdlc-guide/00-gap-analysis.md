# Gap Analysis of the Existing Guidebook (v0.2)

Reviewed: `Joule_Implementation_Guidebook.md` and all files in `01` to `06`. Review date 2026-11-23.

**Overall verdict.** The v0.2 repository is a strong *pre-sales and architecture* pack: good pattern catalogue, sensible risk tiers, honest tone about benefits. It is **not yet a delivery guide**. A development lead picking it up today would find what to build and why, but not how to run the build: no engineering standards, no test strategy beyond a question bank, no CI/CD, no operations model, no decommissioning, and a value case that rests on invented numbers. This document lists every gap, ranks it, and points to where v0.3 closes it.

Severity: **C** = would cause a failed or unsafe delivery or a lost client argument; **H** = material quality/rework risk; **M** = improves maturity.

---

## 1. Defects in the current content (fix first)

| # | Finding | Evidence | Sev | Fixed in |
|---|---|---|---|---|
| D1 | **Benefit model is not supported by its own worked samples.** Samples A to D total about EUR 420k/yr (33k + 40-80k + 100k + 200k + 27k). The ROI table (5.3) assumes EUR 0.9M hard benefit in Y2 and 1.4M in Y3. The gap (about 1M/yr) is unexplained. | Guidebook Part 4 vs Part 5.3 | C | `08-value-cases/` (rebuilt model) |
| D2 | **Labour savings counted as hard benefit** in Samples A and B, contradicting rule 5.4 ("count only cashable or redeployed to named work"). Saved hours are capacity, not cash, until headcount, overtime or contractor spend actually falls. | Part 4 vs 5.4 | C | `08-value-cases/` |
| D3 | **Security overclaim.** Part 1 says "no data leaving the SAP trust boundary", but `multi-ai-patterns.md` routes data to Azure OpenAI, Bedrock, Vertex and others. A client's security team will catch this. | Part 1 pillar table vs multi-AI doc | C | Corrected in guidebook; see `03-secure-by-design.md` |
| D4 | **Data readiness understated.** "No separate data-science programme" and "works on that data in place" ignore that answer quality depends on master-data and role quality (which the doc itself says in 2.3). | Part 1 vs 2.3 | H | Corrected in guidebook |
| D5 | **Timeline inconsistency.** Part 1: pilot 8 to 12 weeks. Part 6: pilot build weeks 5 to 16 plus pilot run 17 to 24 = 20 weeks after a 4-week readiness phase. | Part 1 vs Part 6 | H | Corrected in guidebook |
| D6 | **No time value of money.** Cumulative cash view with no discounting, no NPV/IRR, no cost of capital. CFOs will ask. | 5.3 | H | `08-value-cases/` |
| D7 | **Budget table has no basis.** Ranges are admitted placeholders; there is no unit-cost build-up (tokens, users, days). | 5.2 | H | `08-value-cases/` (unit economics) |
| D8 | **Broken references.** README points to `05-templates/scenario-one-pager.md`; the file is `templates.md`. Scenario index claims "well over 250" scenarios; actual count is 241. | README, index | M | Corrected |
| D9 | **Mixed audience.** The "client-facing" guidebook contains internal items ("our rate card", "firm architects", "dry-run with mock client"). | Parts 5.2, 10 | M | Split noted in README |
| D10 | **29 unresolved `[VERIFY]` tags** on licensing, availability, MCP/A2A support, model catalogue, data-use terms. A guide cannot be "stable" while these float. | all files | H | `08-value-cases/` and research appendix resolve what can be sourced; remainder tracked in `07-sdlc-guide/05-verify-register.md` |

---

## 2. Gaps by discipline

### 2.1 Development
| # | Gap | Why it matters | Sev | Fixed in |
|---|---|---|---|---|
| DEV1 | No engineering standards: repo layout, branching, naming, code review, definition of done. | Without them, every Studio skill and CAP service is bespoke and unreviewable. | H | `02-engineering-standards.md` |
| DEV2 | **Prompts, skill definitions, tool schemas and evaluation sets are not treated as versioned artefacts with release management** (only one line in 2.9). | Prompt edits change behaviour like code edits do. | H | `02-engineering-standards.md` |
| DEV3 | No CI/CD design: build, lint, unit test, eval run, security scan, transport, promotion gates. | Manual promotion is the main source of Dev/Prod drift. | H | `02-engineering-standards.md` |
| DEV4 | **Test strategy covers only a question bank.** Missing: unit tests for tools/APIs, contract tests, non-determinism handling (repeat runs, thresholds), regression on model change, load/performance, UAT script design, negative/security tests. | Generative output is non-deterministic; classic pass/fail tests are not enough. | C | `02-engineering-standards.md` section 6 |
| DEV5 | Clean-core enforcement is mentioned but not operationalised (ATC checks for released-API use, ABAP Cloud language version, extensibility rules). | Clean core erodes silently without automated checks. | H | `02-engineering-standards.md` |
| DEV6 | No tool/API design standard for agents: narrow, idempotent, typed, least-privilege, with dry-run mode. | Tool quality drives agent safety and accuracy more than the model. | H | `02-engineering-standards.md` section 4 |
| DEV7 | AI-assisted development (P10) is a single pattern with no policy on code provenance, review, licensing, or measured benefit. | Evidence on developer AI productivity is mixed (see `08-value-cases/`). | M | `02-engineering-standards.md` section 9 |
| DEV8 | No technical debt / dependency / SAP-release-cadence management (quarterly cloud releases, deprecations, model retirements). | Scenarios that worked in Q1 can break in Q3. | H | `01-sdlc-playbook.md` Operate phase |

### 2.2 Architecture
| # | Gap | Why it matters | Sev | Fixed in |
|---|---|---|---|---|
| ARC1 | **No BTP account model**: global account, directories, subaccount per environment/region, entitlements, role-collection strategy. | Everything else sits on this; hard to change later. | H | `02-engineering-standards.md` section 2 |
| ARC2 | **No resilience design**: HA/DR, RTO/RPO, behaviour when LLM provider/region is down, circuit breakers, timeouts, retries. P15 (fallback) exists but is not specified. | AI becomes a dependency of daily work. | H | `02-engineering-standards.md` section 5 |
| ARC3 | **Identity propagation is asserted, not designed.** Missing: token exchange chain Joule to Studio to Cloud Connector to ABAP, when a technical user is allowed, agent identity, on-behalf-of vs service identity, audit attribution. | The central security claim ("Joule inherits user roles") depends on this holding at every hop. | C | `03-secure-by-design.md` section 3 |
| ARC4 | No capacity/sizing and latency-budget breakdown (retrieval, tool calls, model, post-processing). The < 5 to 8 s target has no decomposition. | Latency target cannot be engineered without a budget. | M | `02-engineering-standards.md` section 5 |
| ARC5 | No data architecture: data classification to model-routing rules, lineage, retention for prompts/logs/vector index, embedding refresh. | Drives both privacy and answer quality. | H | `03-secure-by-design.md` section 6 |
| ARC6 | Decision records are a template only; no starter ADR set. | Leads need the 8 to 10 decisions that always arise. | M | `01-sdlc-playbook.md` Design phase (ADR starter list) |
| ARC7 | Brownfield/legacy not covered: ECC, old S/4 releases, heavily customised Z-code, non-SAP middleware. | Many clients are here. | H | `01-sdlc-playbook.md` section on landscape variants |
| ARC8 | No FinOps architecture: token budgets by scenario, model routing policy, caching design, chargeback. Cost control exists as bullet points (P14, governance 5). | The client's top concern is cost vs value. | H | `08-value-cases/` unit economics + engineering standards |

### 2.3 Design
| # | Gap | Why it matters | Sev | Fixed in |
|---|---|---|---|---|
| DES1 | **No conversation/UX design guidance**: persona journeys, turn design, confirmation screens, error and "I don't know" states, feedback capture, accessibility, i18n. | Adoption is "the commonest reason value fails" (guidebook 5.4), yet nothing designs for it. | H | `02-engineering-standards.md` section 3 |
| DES2 | No **autonomy-level model** (suggest / draft / act-with-approval / act-autonomously) tied to risk tier. | Gives a precise language for "human in the loop". | H | `01-sdlc-playbook.md` + `03-secure-by-design.md` |
| DES3 | No requirements method for non-functional AI qualities (accuracy thresholds, refusal behaviour, explainability, fairness). | Requirements stay vague, tests stay arbitrary. | H | `01-sdlc-playbook.md` Requirements phase |
| DES4 | Prompt design standard absent (system prompt structure, separation of instructions and data, output schemas, language handling). | Reproducibility and injection resistance. | M | `02-engineering-standards.md` section 3 |

### 2.4 Security
The existing security reference is a good baseline (least privilege, threat table, go-live gate). Gaps:

| # | Gap | Sev | Fixed in |
|---|---|---|---|
| SEC1 | No mapping to **OWASP Top 10 for LLM Applications (2025)**, NIST AI RMF, ISO/IEC 42001, MITRE ATLAS. Reviewers expect these. | H | `03-secure-by-design.md` section 1 |
| SEC2 | **Indirect prompt injection** is listed but there is no design rule like "never combine private data + untrusted content + an outbound or write channel in one agent without approval". | C | `03-secure-by-design.md` section 2 |
| SEC3 | **MCP / tool-server security** absent: server authentication, token passthrough prohibition, confused-deputy risk, tool-description poisoning, allow-listed servers, per-tool scopes. Guidebook recommends MCP interoperability without its threat model. | C | `03-secure-by-design.md` section 4 |
| SEC4 | Agents as **identities in SoD**: maker-checker for agent actions, agent inclusion in access reviews, non-human identity lifecycle. | H | `03-secure-by-design.md` section 3 |
| SEC5 | Output handling: model output used in OData filters, SQL, URLs, HTML, or downstream API calls without validation. | H | `03-secure-by-design.md` section 2 |
| SEC6 | Vector store security: per-chunk ACL enforcement at query time, poisoning, embedding inversion, tenant separation. (Only a one-line watch-out in P2.) | H | `03-secure-by-design.md` section 6 |
| SEC7 | No secure SDLC controls: threat modelling at design, SAST/dependency/secret scanning in CI, SBOM, pen-test scope definition, security regression suite. | H | `03-secure-by-design.md` section 7 |
| SEC8 | Logging is specified but log *confidentiality* and DSAR/erasure handling are thin. Prompts and responses contain business secrets and personal data. | M | `03-secure-by-design.md` section 8 |
| SEC9 | EU AI Act dates and obligations are described generally; no per-tier obligations or timeline; status of the proposed delay to high-risk obligations needs verification. | M | `03-secure-by-design.md` section 9, `05-verify-register.md` |
| SEC10 | Incident response mentions a kill switch but no playbooks (injection, leakage, runaway cost, model regression), drills or ownership. | H | `03-secure-by-design.md` section 8 |

---

## 3. Gaps by SDLC phase

| Phase | What exists | What is missing | Closed in |
|---|---|---|---|
| **1. Discover / Business case** | Scoring sheet, scenario library, template T1/T5 | Baseline measurement protocol; control group design; cost-per-outcome; stage-gated funding; kill criteria; evidence from comparable deployments | `08-value-cases/` |
| **2. Requirements** | KPIs, pillars | Functional + non-functional AI requirements; acceptance criteria; data requirements; autonomy level; legal/risk classification at intake; stakeholder map | `01-sdlc-playbook.md` |
| **3. Architecture and design** | Patterns, reference architectures, ADR template | Starter ADR list; account model; identity design; resilience; FinOps; conversation design; threat model workshop | `01`, `02`, `03` |
| **4. Build** | Pattern guidance | Repo/branching/naming; prompt-as-code; tool standards; coding standards for ABAP Cloud/CAP/Studio; review checklist | `02-engineering-standards.md` |
| **5. Test and evaluate** | Test-question bank (T4) | Test pyramid for AI; eval harness; non-determinism tolerance; red-team plan; performance/load; UAT; regression on model/prompt/SAP-release change | `02-engineering-standards.md` section 6 |
| **6. Release / Deploy** | Environment table, CTMS mention | Promotion gates; feature flags; canary/pilot cohorts; rollback; release checklist; cutover communications | `01-sdlc-playbook.md` |
| **7. Operate** | Metrics list, cost alerts | Support model L1/L2/L3; SLOs and error budgets; dashboards spec; runbooks; model-deprecation handling; drift monitoring; quarterly SAP release regression | `01-sdlc-playbook.md` |
| **8. Optimise / Retire** | Quarterly review (one line) | Benefits tracking cadence; scenario retirement criteria; decommission steps; knowledge transfer | `01-sdlc-playbook.md` |
| **Cross-cutting: Handover to client dev leads** | Nothing | 90-day runbook, RACI, definition of ready/done, onboarding checklist | `04-lead-implementation-runbook.md` |

---

## 4. Priorities for the next 30 days (recommendation)

1. **Fix the business case first** (D1, D2, D6). It is the client's biggest objection and the current numbers will not survive a CFO review. Use `08-value-cases/`.
2. **Resolve the `[VERIFY]` register** with the SAP partner team (D10). Licensing and Joule Studio availability change the budget more than anything else.
3. **Adopt the engineering standards and CI/CD skeleton** on one pilot scenario before scaling (DEV1 to DEV6).
4. **Run an identity-propagation proof** (ARC3) in the pilot's first sprint; it is the highest-risk technical assumption.
5. **Stand up the evaluation harness before the first skill** (DEV4). Retrofitting evals after the build is the most common failure pattern.
