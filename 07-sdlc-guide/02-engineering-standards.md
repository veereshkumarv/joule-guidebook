# Engineering Standards for SAP AI Builds

Applies to Joule Studio skills/agents, CAP services, ABAP Cloud extensions and Generative AI Hub integrations. Where a standard depends on SAP product behaviour that may change, it is marked **[VERIFY]**. Treat this document as the team's baseline; changes go through an ADR.

## 1. Repository and artefact layout

One repository per deployable solution (monorepo acceptable per scenario family). Everything that changes behaviour is in Git.

```
/ai-solution
  /srv               CAP services, custom tools/APIs
  /abap              ABAP Cloud packages (via abapGit/gCTS or the client's standard) 
  /joule             Studio skill/agent exports, action definitions, intents
  /prompts           System prompts, templates, few-shot examples (versioned, one file per prompt)
  /schemas           JSON schemas for tool inputs/outputs and model structured outputs
  /eval              Question bank (YAML/CSV), expected answers, must-not-reveal, rubric, runner
  /security          Threat model, abuse-case tests, red-team prompt set
  /infra             mta.yaml, xs-security.json, entitlements, destinations (no secrets)
  /docs              ADRs, runbooks, diagrams
  /.pipeline         CI definitions
```

- Branching: trunk-based with short-lived feature branches; protected `main`; PR required; at least one reviewer who did not write the change; security-sensitive paths (`/security`, `xs-security.json`, tool scopes) require the security engineer as reviewer.
- Versioning: semantic version for the solution; each prompt and tool schema carries a version and changelog line; **release = tag that pins code, prompts, schemas, eval set and model identifiers together**.
- Naming: `<domain>-<capability>-<verb>` for tools (e.g. `ap-blockedinvoice-explain`), snake or kebab consistently; scenario IDs from the scenario library appear in repo, tickets and dashboards.
- Exported Studio artefacts: confirm the export/transport format and whether Studio content can be managed in Git/CTMS in the client's tenant edition **[VERIFY]**. If not exportable, record each change as a ticketed manual step and include screenshots in the release notes; this is a known audit gap to flag to the client.

## 2. Platform and environment standards

### BTP account model
| Element | Standard |
|---|---|
| Global account | One per legal/contract entity; entitlements allocated by quota per subaccount |
| Directories | `ai-nonprod`, `ai-prod` (separate admins) |
| Subaccounts | `sandbox`, `dev`, `qa`, `prod` per region needed; prod separated; no shared subaccount between clients |
| Region | Chosen from data residency + model availability **[VERIFY per model]**; documented in ADR |
| Role collections | Defined in code (`xs-security.json`); no ad hoc user-level assignment in prod; groups mapped via IAS |
| Budgets/alerts | Consumption alert at 50/80/100% per subaccount; quota for Generative AI Hub deployments per scenario |
| Transport | Cloud Transport Management or CI/CD pipeline; manual change in prod is a Sev3 incident |

### Environments and data
| Env | Data | Models | Who can access |
|---|---|---|---|
| Sandbox | None/public | Any approved | Team |
| Dev | Synthetic or masked | Cheapest adequate | Team |
| QA | Production-like roles, masked/sampled data approved by data owner | Same as prod | Team + testers |
| Prod | Live | Approved register only | Users; admin by break-glass |

## 3. Conversation, UX and prompt design

**Conversation design rules**
1. State what the assistant can do on first use; show 3 example prompts per persona.
2. Resolve entities explicitly: "Invoice 5100234, vendor ACME GmbH, company code 1010, EUR 12,430. Release block?" Never act on an unresolved or ambiguous entity; ask.
3. Every answer shows sources or the underlying object link; numeric answers state date/time and scope of the data.
4. Write actions: confirmation screen listing every field to change, the approver, and what is not changing. Provide undo/compensation where the API allows.
5. Failure states are designed, not default: "I couldn't find that you have access to this" (without disclosing existence), "I'm not sure, here's the report", "Service is busy, open transaction X".
6. Collect feedback in-flow: thumbs plus reason codes (wrong data, wrong action, too slow, unclear). Reason codes feed the test bank.
7. Respect language and locale (dates, number formats, currency); test each supported language separately.
8. Accessibility for any custom UI (keyboard, screen reader, contrast); follow Fiori guidelines for embedded surfaces.
9. Label AI-generated content; provide a route to a human.

**Prompt standards**
- Structure: role and scope, allowed tools, constraints, output schema, refusal rules. Keep **instructions separate from retrieved data**, delimiting untrusted content explicitly.
- Never place secrets, credentials, or authorization logic in prompts. Authorization is enforced in tools/APIs.
- Prefer **structured output** (JSON schema) for anything a program consumes; validate before use.
- The model narrates; deterministic code calculates (amounts, dates, aggregates, thresholds).
- Keep prompts short; remove unused few-shot examples; measure token cost per prompt version.
- Every prompt change requires an eval run recorded in the PR.

## 4. Tool and API design standard (agent tools)

| Property | Rule |
|---|---|
| Granularity | One narrow purpose per tool; no "execute arbitrary query/script" tools |
| Input | Typed schema, enums for constrained values, max lengths, reject unknown fields |
| Authorization | Executes **as the calling user** (principal propagation); a technical user is allowed only by ADR with a scoped role and a documented reason |
| Idempotency | Write tools accept an idempotency key; repeating a call must not duplicate postings |
| Dry run | Write tools support `validate-only`/preview that returns what would change |
| Limits | Per-call record cap, per-user rate limit, timeout, max steps per agent run |
| Errors | Structured error codes; no stack traces or internal hostnames returned to the model |
| Audit | Log user, tool, parameters (masked), result code, correlation ID |
| Released APIs | Use released/public APIs only; no direct table access or unreleased function modules; enforce with ATC (clean-core checks) in CI **[VERIFY check variants available in the client system]** |
| Output | Return minimal fields required (data minimisation), already filtered by the user's authorizations |

## 5. Non-functional engineering

**Latency budget (example, p90 for read Q&A, 8 s):** intent routing 0.5 s, identity/token 0.3 s, data retrieval/API 2.0 s, vector retrieval 0.5 s, model 3.5 s, post-processing/validation 0.5 s, UI 0.7 s. Measure each segment with a correlation ID; optimise the largest first (usually the model and the S/4 call).

**Resilience**
- Timeouts on every hop; retries with exponential backoff and jitter only on idempotent calls; circuit breaker around each model endpoint.
- Secondary model/region defined and tested; degrade to deep link or static help (pattern P15).
- RTO/RPO set per scenario tier; vector index rebuild procedure tested; configuration restorable from Git.
- Load test and soak test before go-live; concurrency limits set below model quota.

**FinOps**
- Cost per interaction = (input tokens x price) + (output tokens x price) + retrieval + platform overhead; log tokens per call and attribute to scenario and cost centre.
- Route simple tasks to small models; cache identical or near-identical read queries with short TTL when authorization context allows (cache key includes user/role scope); trim context; cap output length.
- Per-scenario monthly budget and hard quota; automatic alert at 80%; agent step and token ceilings per run.
- Report monthly: cost per active user, per accepted answer, per completed transaction.

## 6. Test strategy (AI-specific)

**Evaluation harness requirements**
- Runs headless in CI against Dev and on demand against QA.
- Test case fields: ID, persona/identity to run as, input, expected facts/records, must-include sources, must-not-reveal, scoring method (exact, rubric, or LLM-as-judge with human-calibrated sample), severity.
- **Repeat each case at least 3 times**; report pass rate and variance; flaky cases are investigated, not ignored.
- Scoring: deterministic checks first (numbers, IDs, citations present, refusals), model-graded rubric only for free text, and calibrate any LLM judge against 50+ human-scored examples (agreement threshold agreed, e.g. ≥ 85%).
- Separate sets: *development set* (visible to engineers), *held-out set* (used only at the gate to prevent overfitting prompts), *adversarial set*, *regression set* (grows from production failures).
- Gate thresholds from requirements; any safety/leakage case failing blocks release regardless of average.
- Track results per release in a dashboard: pass rate by intent, persona, language.

**Other layers:** unit tests for tools and validators; contract tests with mocked/recorded SAP responses plus nightly tests against Dev; authorization tests as defined personas; load tests; chaos tests (kill model endpoint, slow S/4 API, malformed model output).

**Test data:** synthetic or masked; never copy production personal data to Dev without data-owner approval; maintain a seed dataset with known answers for deterministic checks.

## 7. CI/CD skeleton

| Stage | Checks | Blocks merge/promotion? |
|---|---|---|
| Pre-commit | Secret scan, format, lint | Yes |
| Build | Compile/build MTA, ABAP syntax and ATC (clean-core), dependency vulnerability scan, licence check, SBOM | Yes (high/critical) |
| Unit/contract | Tool and validator tests | Yes |
| Eval (Dev) | Dev + adversarial sets with thresholds | Yes |
| Deploy to Dev | Automated | n/a |
| Promote to QA | Held-out eval set, authorization tests, load smoke test | Yes |
| Promote to Prod | Change ticket, security sign-off for tier 3, release notes with prompt/tool/model versions, rollback artefact ready | Yes |
| Post-deploy | Smoke test, canary cohort, dashboard check | Auto-rollback on SLO breach |

## 8. Observability

Required telemetry (structured logs with correlation ID, no raw secrets; mask PII per policy):
- Request: user hash, persona/role set, scenario/skill, language
- Execution: tool calls (names, latency, status), retrieval hits and source IDs, model ID and version, token counts, step count
- Outcome: answer accepted/rejected, feedback code, action executed, approval result
- Safety: refusal reason, injection detector hits, authorization denials
- Cost: per call and rolled up

Dashboards: adoption, quality, latency, cost, safety. Alerts: error rate, p90 latency, cost > 80% budget, spike in denials, spike in thumbs-down, step-limit hits.
Use Cloud ALM / Application Logging / Cloud Logging and Audit Log services as available **[VERIFY]**. Protect logs: they contain business-confidential content.

## 9. AI-assisted development policy

Evidence on developer productivity is mixed (see `08-value-cases/`), so adopt with measurement:
- Approved tools list (SAP Build Code/Joule for developers, client-approved assistants) **[VERIFY availability for ABAP/CAP]**; no pasting client code or data into unapproved tools.
- AI-generated code is subject to the same review, ATC, tests and licence checks; reviewer must understand the code before approving.
- Do not rely on assistants for ABAP Cloud API choices without verifying against the released-API list; models may suggest obsolete or unreleased objects.
- Measure on your own team: cycle time per story, review rework rate, defect escape rate, before and after, over at least 8 weeks, with developers and seniority mix noted. Decide on evidence.

## 10. Coding standards checklist (review aid)
- [ ] Released APIs only; clean-core checks pass
- [ ] Authorization enforced in code via user context; no hard-coded users/roles
- [ ] Inputs validated; outputs encoded for their sink (OData/SQL/HTML/URL)
- [ ] No secrets, no PII in logs; destinations used for credentials
- [ ] Timeouts, retries, circuit breaker, step limits present
- [ ] Idempotency and dry-run on write tools
- [ ] Unit tests and at least one negative authorization test
- [ ] Prompt/schemas versioned; eval run attached to PR
- [ ] Cost per call measured; token ceiling set
- [ ] Documentation and runbook updated
