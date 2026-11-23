# Scenario Index and Prioritisation

## Counts (as authored)
Functional library (`01`) and industry library (`02`) together list 241 scenarios (counted 2026-11-23). Add new ones with a unique ID and the same columns.

## ID prefixes
FIN/AR/AP/TRE/CO (finance), PRO (procurement), SCM (supply chain), MFG (manufacturing), EAM (maintenance), SAL/SRV (sales/service), HR, TE (travel and expense), SEC/OPS (security and operations), DEV (development), ESG, IND-* (industry).

## Quick-win shortlist (typically low effort, embedded or Studio, broad user base)
FIN-001, FIN-002, AP-001, AP-002, PRO-001, PRO-003, SAL-001, HR-001, HR-002, TE-001, DEV-001, SEC-005, OPS-007.

## High-value shortlist (more effort, strong business case; need data readiness)
FIN-003, AP-006, TRE-005, PRO-006, PRO-010, SCM-001, SCM-002, SCM-004, MFG-004, EAM-003, SEC-001, SEC-006, SEC-007.

## Strategic/transformational shortlist
Multi-agent end-to-end flows: procure-to-pay agent, order-to-cash agent, record-to-report agent, hire-to-retire agent, with human approval gates (P6 + P4).

## Scoring sheet

| Criterion | Weight | 1 (low) to 5 (high) |
|---|---|---|
| Business value (quantified) | 30% | |
| Technical feasibility (APIs, data, release) | 20% | |
| Data quality readiness | 15% | |
| Adoption likelihood (user pain, sponsor) | 15% | |
| Risk/compliance (5 = low risk) | 10% | |
| Strategic fit | 10% | |

Weighted score ≥ 3.8: pilot candidate. 3.0 to 3.8: backlog. < 3.0: park.

## Pillar coverage check
A good portfolio includes at least one scenario in each of F, E, S, P. If the client only wants cost savings, still include one S (e.g. SEC-005) and one P scenario to build a balanced story and manage risk.

## Risk tier hints (see governance doc)
- **Tier 1 (low):** read-only Q&A, summarisation of non-sensitive data.
- **Tier 2 (medium):** drafts and recommendations reviewed by humans; sensitive but internal data.
- **Tier 3 (high):** actions on financial/master data, HR decisions, regulated (GxP, safety), external-facing output. Require formal risk assessment and approvals.
