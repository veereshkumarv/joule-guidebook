# Development Lead Runbook: First 90 Days

For the SAP development lead taking a Joule / SAP AI pilot from approved scope to a measured go/no-go. Follow with the playbook (`01`), standards (`02`) and security addendum (`03`). Durations assume one pilot business unit, 2 to 3 scenarios, a team of about 6 to 8; scale proportionally.

## Week 0: Before you start (checklist)
- [ ] Funding released for the pilot tranche only; kill criteria written in the charter
- [ ] Baselines signed by finance and process owner
- [ ] Licence and entitlements confirmed in writing (Joule edition, Studio, AI units, BTP credits) **(`05-verify-register.md`)**
- [ ] BTP global account and subaccounts requested; region decided
- [ ] Named: product owner, security engineer (independent of developers), QA/eval engineer, client IT ops contact, SAP basis/authorization contact
- [ ] Access: Dev/QA tenants, S/4 sandbox with released APIs, IAS admin, Cloud Connector admin
- [ ] Approved-model register has at least one entry; data-use terms on file

## Weeks 1 to 2: Sprint 0 (platform skeleton) — nothing else starts until done
| Task | Done when |
|---|---|
| Repos, branching, protected main, PR templates | First PR reviewed and merged |
| CI pipeline (secret scan, build, ATC, unit, eval) | Green pipeline on a hello-world tool |
| Environments and transport path | A trivial change promoted Dev→QA via pipeline |
| Eval harness with 10 seed questions and 3-run variance report | Report generated automatically |
| Logging and correlation IDs; dashboards v0 | One request traceable end to end |
| Secrets and destinations in managed stores | No secret in repo (scan proves it) |
| Budgets and alerts at 50/80/100% | Test alert received |
| Threat-model workshop held | Register in repo |
| **Identity-chain proof** (5 personas, every hop) | Backend log shows the end user; low-privilege persona refused |

**If the identity proof fails, stop and fix it.** Everything else depends on it.

## Weeks 3 to 8: Build in vertical slices
Sprint cadence 2 weeks. Suggested order per scenario:
1. **Slice 1 (read, single intent):** e.g. "Why is invoice X blocked?" with citation, evaluated on 30 questions across personas.
2. **Slice 2 (read, breadth):** more intents, retrieval if needed, low-privilege and adversarial tests added.
3. **Slice 3 (write with approval, A2):** one write action with preview, approval, idempotency, audit; security reviewer signs.
4. **Slice 4:** feedback capture, fallback and error states, cost tuning.

Each sprint ends with: demo to product owner; eval dashboard review; threat-register update; cost per interaction vs budget; adoption-instrumentation check.

**Weekly lead routine (30 minutes):** review failed/refused questions → add to test bank; review cost and latency; review open risks; confirm no scope creep into A3 or new data sources without ADR.

## Weeks 9 to 12: Evaluate and release to pilot cohort
- Run the full test layers (playbook Phase 4). Use a held-out set the team has not tuned on.
- Security gate (`03-secure-by-design.md` section 10), incident tabletop, kill-switch drill.
- Training for pilot users using real prompts from the bank; champions named (1 per 50 users).
- Release to cohort with feature flags; include a matched control group if possible.
- Hypercare daily triage.

## Weeks 13 to 24: Pilot run and decision
- Weekly: adoption (weekly active users, prompts per user, repeat use), quality (accepted-answer rate, thumbs-down reasons), safety (incidents), cost per interaction.
- Monthly: KPI delta vs baseline and control; cost per outcome; benefits classified as cashable / redeployable / soft with evidence.
- Week 20 to 24: **go/no-go review** against the charter. Options: scale, fix and extend pilot, pivot scenario, stop. Stopping on kill criteria is a valid, valuable outcome and should be reported as such.

## Estimation guardrails
Use T3 in `05-templates/templates.md`. Typical sources of overrun: identity/authorization remediation, data-quality work, evaluation set creation (often under-estimated by half), and change management. Keep 15% PM and 15 to 25% contingency visible; do not absorb them into task estimates.

## Decision log (maintain from day 1)
| Date | Decision | ADR | Owner | Review date |
|---|---|---|---|---|

## Top 10 pitfalls and their counters
| Pitfall | Counter |
|---|---|
| Build before baseline | G0 requires signed baseline |
| Test as admin | Persona-based tests mandatory |
| One-time testing | CI eval on every change; repeat runs |
| LLM does arithmetic | Deterministic tools compute |
| Custom build of something SAP ships | Standard-first check in Phase 0 and each quarter |
| Technical user shortcut | ADR required; proof test |
| Prompts edited in the console | Source control; PR with eval |
| No owner after hypercare | Support model and product owner named at G4 |
| Scope creep to autonomy | Autonomy level in charter; changes need risk re-tiering |
| Value claimed on hours "saved" | Benefit classification and finance sign-off |

## Handover pack (to client run team at G5)
Architecture and ADRs; runbooks and incident playbooks; evaluation harness and sets; dashboards and alert definitions; access list and role-collection map; cost model and budgets; model/provider register; release notes with versions; backlog and known issues; training materials; contact and escalation matrix.
