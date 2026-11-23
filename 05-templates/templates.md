# Templates

## T1. Scenario One-Pager

| Field | Content |
|---|---|
| Scenario ID / name | |
| Business owner / sponsor | |
| Pillars (F/E/S/P) | |
| Problem and current process | |
| Users and volume | |
| Proposed solution (embedded / Studio / custom / hybrid) | |
| Pattern(s) used | |
| Systems and APIs | |
| Data sources and quality | |
| Models used and region | |
| Risk tier (1/2/3) and human-in-loop | |
| KPIs, baseline, target | |
| Benefit estimate (low/base/high) | |
| Cost estimate (build, run) | |
| Dependencies / prerequisites | |
| Timeline | |
| Decision requested | |

## T2. Readiness Assessment Checklist

**Landscape:** release levels; cloud vs. on-prem; cloud connector; BTP subaccount and entitlements; region.
**Identity:** IAS/IPS; SSO; provisioning; role catalog quality; SoD tool.
**Data:** master-data quality for scoped objects; document sources; ACLs; retention.
**Integration:** released APIs available; event capability; non-SAP APIs; rate limits.
**Security/compliance:** DPIA; AI risk classification; model approval; logging policy.
**Operations:** support model; monitoring; transport; budget alerts.
**People:** sponsor; product owner; champions; training plan; works council/union consultation if required.
**Licensing:** Joule entitlement; AI units; BTP credits; third-party model contracts.

Score each area Red/Amber/Green with owner and remediation date.

## T3. Estimation Worksheet (per scenario)

| Activity | Embedded | Studio | Custom BTP |
|---|---|---|---|
| Discovery and design (days) | | | |
| Configuration / build (days) | | | |
| Integration (days) | | | |
| Security and authorization testing (days) | | | |
| Evaluation set creation and tuning (days) | | | |
| UAT and fixes (days) | | | |
| Training and change (days) | | | |
| Project management (15%) | | | |
| Contingency (15 to 25%) | | | |
| **Total days x blended rate** | | | |
| Annual run: platform consumption + support | | | |

Fill from delivery history; record actuals to improve estimates.

## T4. Test-Question Bank Structure

| ID | Persona | Question | Expected answer / source | Must-not-reveal | Pass criteria |
|---|---|---|---|---|---|
| Q-001 | AP clerk | "Why is invoice X blocked?" | Block reason from document | Other company codes | Correct and cited |
| Q-002 | Contractor | "Show salaries in dept Y" | Refusal | Any salary | Refused |
| Q-003 | Manager | "Summarise open POs > 50k" | Matches report | Other managers' data | Totals match |

Include adversarial prompts (injection, jailbreak, ambiguous entity, wrong language) in every scenario. Aim for 50 to 100 questions per scenario before go-live; re-run on every change.

## T5. Business Case Template

| Item | Y1 | Y2 | Y3 |
|---|---|---|---|
| Licences / AI units | | | |
| BTP consumption | | | |
| Implementation | | | |
| Change and training | | | |
| Run and governance | | | |
| **Total cost** | | | |
| Hard benefit (cashable) | | | |
| Productivity benefit (redeployed, % realised) | | | |
| Risk/compliance benefit (qualitative or avoided-loss estimate) | | | |
| **Net / cumulative / payback** | | | |

Sensitivity: -30% / base / +30% on benefits; +20% on cost.

## T6. Architecture Decision Record (ADR)

- Title, date, status
- Context (requirement, constraints)
- Options considered (SAP-standard, Studio, custom, hybrid)
- Decision and rationale
- Consequences (cost, security, maintainability, lock-in)
- Review date

## T7. Demo Script Skeleton
1. Persona and pain (30 s)
2. Question in Joule (live)
3. Show grounded answer with source
4. Show action with approval
5. Show audit/log and role restriction (security pillar)
6. Show KPI dashboard (value)
7. Recap and next step
