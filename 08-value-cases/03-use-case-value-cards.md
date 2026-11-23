# Use-Case Value Cards: Comparable Cases, Planning Ranges, and When It Does Not Pay

One card per use-case family. Each card says what comparable evidence exists (with tier from `01-evidence-register.md`), what planning range we are willing to use, how to measure it, and the conditions under which the use case should **not** be pursued. Tiers: A/B independent, C customer-reported, D vendor/consultancy. All figures are quoted from `_research/` files; "insufficient evidence" is a finding, not a gap to paper over.

## How to read a card
- **Base-case range** is what the model uses (`value_model.py`). Anything tier D is upside only.
- **Benefit class** is Cashable, Redeployable, Soft or Risk-avoided (`02-business-case-model.md`).
- **Prove it in the pilot** says which measurement would move a benefit up a tier.

---

## 1. AP exception handling and invoice capture (scenarios AP-001, AP-002, AP-004)

| | |
|---|---|
| Comparable evidence | Ardent Partners (about 200 leaders, via Basware): best-in-class vs others cost per invoice $2.67 vs $12.50; touchless 55.2% vs 31.4%; approval cycle 4.1 vs 15.4 days (**B**, not AI-specific). De Agostini with SAP Document AI: 91% of PO-referenced invoices automated, about 500 hours a month (**C/D**). FRoSTA: 70% touchless in one SAP post, about 60% in another (**C/D**, inconsistent). Rhätische Bahn: over 90% e-invoice auto-match (**C**, not generative AI). |
| Base-case range | 10% / 20% reduction in exception handling time (conservative / base); 40% upside |
| Benefit class | Redeployable (cashable only if temps, overtime or outsourced per-invoice fees fall) |
| Where value is larger than labour | Duplicate and error prevention, early-payment discount capture (no independent figure found; measure before claiming) |
| Break-even logic | Each exception is worth about EUR 2.29 at 25 minutes, 20% reduction, EUR 55/hour, 50% realisation. Covering EUR 50k of incremental annual run cost needs about 21,800 exceptions a year. |
| Prove it in the pilot | Sample 30+ exceptions for time and rework before and after; touchless rate; errors escaped; per-exception cost including AI cost |
| Do not pursue when | Exception volume is below the break-even; vendor/PO master data is poor (capture and matching both degrade); the standard embedded capability already delivers the result at Base AI |

## 2. Cash application and collections (AR-001, AR-004, AR-003)

| | |
|---|---|
| Comparable evidence | ResMed with HighRadius: 95% automated cash application, DSO down about 33 days in 10 months, no baseline stated (**D**). Accenture Finance (custom, on SAP platform): receivables automation "more than doubled", about 57,000 hours across finance solutions, close in 3 days instead of 5 (**C**, own function at large scale, no baselines). SAP estimate for payment advice processing "about 70% less document processing time" (**D**). |
| Base-case range | **0 in base** (vendor-only evidence for working-capital effect); upside values 1 day of DSO |
| Arithmetic | One day of DSO at EUR 800M revenue releases about EUR 2.19M of cash; at an 8% cost of capital that is about EUR 175k a year of financing value |
| Benefit class | Cashable (financing cost), validated by Treasury |
| Prove it in the pilot | Auto-match rate, unapplied cash, DSO on the pilot customer segment vs a matched control segment, over at least two collection cycles |
| Do not pursue when | The business already has high auto-match and low unapplied cash; DSO is driven by customer terms or disputes, not by posting delays |

## 3. Close, variance and management commentary (FIN-002, FIN-003, FIN-009)

| | |
|---|---|
| Comparable evidence | Accenture: over 90% of narrative commentaries "simply approved" (**C**, large finance function, no baseline). No independent study found. |
| Base-case range | 10% / 25% reduction in commentary preparation time; 50% upside |
| Benefit class | Redeployable |
| Risk | Hallucinated numbers in a board pack. Numbers must come from tools; the model narrates (pattern P8). |
| Prove it in the pilot | Controller time per pack before and after; accepted-without-edit rate; number-error rate in audit sample |
| Do not pursue when | Close is not time-constrained by commentary; no review capacity to verify generated text |

## 4. Procurement, supply-chain planning, forecasting and shortage detection (SCM-001/002/003/004/006/013/019, IND-MFG-01/05; design in `09-forecasting-shortage/`)

| | |
|---|---|
| Comparable evidence | SLB with IBP: forecast accuracy around 50% to about 90% on some business lines, over USD 1 billion inventory savings over four years, DIO down 37% over three years (**C**, SAP-published; no metric definition, no counterfactual). BRF with IBP: data access 33% faster (**C**). Doehler: about a third of troubleshooting time recovered (**C**). Hackett "up to" figures (forecast error -52%, carrying cost -41%, expedites -59%) are modelled (**D**, not to be used). **No independent or measured supply-chain case found.** |
| Base-case range | **0 in base; upside only** (10% of expedite/penalty cost) |
| Forecast quality evidence | Tuned gradient boosting and ensembles do well on intermittent retail data; time-series foundation models are competitive zero-shot with leakage caveats; M4/M5 primary results not verified |
| Benefit class | Cashable (expedite, penalties, inventory financing, lost margin) |
| Prove it in the pilot | Forecast Value Added vs naive and statistical baselines at planner lag and level; shortage detection lead time gained and precision; expedite spend and stock-outs vs matched product families |
| Do not pursue when | IBP's standard demand sensing and Exception Management Agent already cover it; lead-time and BOM master data are unreliable; no baseline for expedite cost or stock-outs; alerts cannot be acted on faster than they arrive |

## 5. Service desk and HR self-service (E5, E3, S2)

| | |
|---|---|
| Comparable evidence | Moveworks customer stories: deflection 40% to 88%, definitions vary, Broadcom ramp about 10% to 88% over an unstated period (**D**). HR Path Brazil with Joule in SuccessFactors: 7% fewer standard HR support cases and 2 hours of HR workload a week (**C**, small and honest). SAP estimate: Explain Pay "50% reduction in pay-statement-related tickets" (**D**). Agent-assist in support: +14% issues per hour, +34% for novices (**A**). |
| Base-case range | **0 in base**; upside 40% of tickets at 75% realisation. Start planning rate no higher than about 20% until your own pilot measures it |
| Benefit class | Cashable only with per-ticket outsourcing or avoided hiring; otherwise Redeployable |
| Risk | Reversals when quality drops (Klarna, CBA); legal liability for wrong policy answers (Air Canada) |
| Prove it in the pilot | Resolved-without-human rate (single agreed definition), reopen rate, satisfaction, escalation quality |
| Do not pursue when | Ticket volume is low; answers depend on policies that are inconsistent or out of date; no human fallback |

## 6. Knowledge assistant and navigation help (E1, E3, E4)

| | |
|---|---|
| Comparable evidence | UK HMRC (randomised licences): about 60 min a week after a 20% downward adjustment; 83% used licence (**B**). DWP 19 min a day; GDS 26 min a day self-reported (**B**). **UK DBT: no evidence time savings improved productivity**; Treasury: no clear evidence of improved work outcomes, most used it 2 to 3 times a week or less (**B**). Danish administrative data: effects above 2% on earnings and hours ruled out (**A**). |
| Base-case range | 0 / 30 minutes a week per active user; active share 22% / 50% (conservative / base); upside 60 minutes and 64% |
| Realisation | Diffuse time: 10% / 25% (upside 50%). BCG 2026: 66% of frontline users get little or no guidance on using saved time |
| Benefit class | Redeployable at best; soft otherwise |
| Break-even check | With 800 users, 50% active, 25% realisation, EUR 55/hour, each EUR 50k of annual cost needs about 12 minutes a week per active user |
| Prove it in the pilot | Telemetry (weekly active use, repeat use); matched control group; task-level time study; manager attestation of what the freed time was used for |
| Do not pursue when | Adoption stays below the threshold; no plan for freed time; the use is generic chat that employees already get elsewhere |

## 7. SAP developer productivity (DEV-001..010; ABAP AI, CAP, test generation)

| | |
|---|---|
| Comparable evidence | METR RCT (16 experienced developers): 19% slower, believed 20% faster (**A**, small); METR 2026 follow-up declared unreliable by its authors (**A**); Google RCT (96 engineers): about 21% less time on task (**A/B**); GitHub/Accenture +8.69% pull requests (**D**); DORA: +2.1% individual productivity but -7.2% delivery stability per 25% more adoption (2024), stability still negative in 2025 (**B**); NBER commit/release study: 240% more commits but 30% more releases (**A**). SAP/ABAP: SAP estimates 20% less time to write and 25% less to test ABAP (**D**); Bosch Digital 20% and 15% to 20% faster unit tests (**D**, method unstated); IDC-via-SAP 35% self-reported (**D**). **No independent ABAP, clean-core or SAP test-automation study found.** |
| Base-case range | 0% / 5% gain on the 30% of developer time that is coding/testing; upside 15% |
| Benefit class | Redeployable (backlog throughput) |
| Costs to net off | Review and rework, test effort, stability regressions, AI-unit billing (SAP described a move to usage-based billing for Joule for developers; docs are inconsistent on cost) |
| Prove it in the pilot | Run your own controlled comparison over at least 8 weeks: cycle time per story, review rework, defect escape rate, by seniority |
| Do not pursue when | Team is small, work is mostly analysis and configuration rather than coding, or the code base is highly specialised and the assistant produces unreleased-API suggestions |

## 8. Security, compliance and policy assistants (S1..S4, FIN-017)

| | |
|---|---|
| Comparable evidence | No measured evidence found. Governance and loss cases exist (Air Canada liability; Deloitte Australia refund) but they are illustrations of risk, not benefit data. |
| Base-case range | **0**; do not monetise risk reduction without the client's own loss history |
| Method if monetising | Expected annual loss = frequency x severity from the client's audit findings, incidents and fines; credit only the share the use case demonstrably reduces |
| Benefit class | Risk-avoided (with client loss data) or Soft |
| Why still do it | Often a precondition for scaling other use cases (identity, role clean-up, audit trail) and required by regulators; justify as enabling cost, not as ROI |

---

## Where AI most often does not pay back (checklist for Phase 0)

| Pattern | Evidence or reason |
|---|---|
| Savings are diffuse and nobody owns the freed time | BCG 2026; UK DBT; Danish null effect |
| Volume is below the break-even for the platform cost | Section 1 arithmetic; model result that base-case run cost exceeds base-case benefits |
| Custom build of something SAP ships at Base AI | Licensing structure (Base vs Premium); IBP agents; MIT NANDA buy-vs-build correlation (about 67% vs 33% deployment, correlational) |
| Poor master data or roles | RAND root causes; Gartner POC abandonment reasons |
| Agentic design where a deterministic workflow would do | Gartner: inference cost per agentic workflow to rise more than fivefold through 2028; run routine steps on small or open models |
| Full replacement instead of augmentation | Klarna, CBA |
| Benefit claimed from vendor figures | Evidence register tiers; SAP footnote "estimates ... actual benefits may vary" |
| Expected results reported as realised | Aeropuertos Argentina "expected 16%" vs "cut costs by 16%" |
| No baseline | Cannot prove value afterwards; Forrester: fewer than one third can tie AI value to P&L |
