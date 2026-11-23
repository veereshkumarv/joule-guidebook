# Evidence Register: What We Can and Cannot Cite

Purpose: a single place that says, for every number we might put in front of a client, **how good it is**. Underlying detail, URLs, dates and caveats are in `_research/` (`independent-roi-evidence.md`, `comparable-cases.md`, `sap-specific-evidence.md`, `forecasting-kg-mcp-evidence.md`). Research date 2026-11-23. The research agents had no web-search tool and several sources (sap.com, community.sap.com, Gartner, APQC, McKinsey pages) were blocked, so absence of evidence below often means "not reachable", not "does not exist".

## 1. Evidence tiers and citation rules

| Tier | Definition | May be used for |
|---|---|---|
| **A** | Independent, measured: randomised trials, administrative data, controlled evaluations | Base-case parameters |
| **B** | Independent surveys, benchmarks, government evaluations (often self-reported time) | Base-case parameters, with haircut |
| **C** | Customer-reported: a named customer quoted by a vendor or consultancy; not audited | Analogues and plausibility; base case only with haircut and explicit label |
| **D** | Vendor, partner or consultancy claim, including modelled "up to" figures and expected benefits | **Upside case only**, always labelled; never presented as the client's expected result |
| **Client pilot data** | Measured on the client's own baseline | Overrides everything above |

Rules:
1. Quote the figure, the sample, the date and the tier together. Never quote a figure alone.
2. Do not mix expected and realised results (Aeropuertos Argentina's 16% is "expected" in one SAP article and "cut" in another; FRoSTA's straight-through rate is 70% in one and about 60% in another).
3. Surveys of executives are self-reported; most come from firms that sell AI services (McKinsey, BCG, Deloitte, PwC, IBM, and IDC with Lenovo). Say so.
4. SAP's own footnote on its feature-level estimates: "All calculations are estimates based on SAP customer case studies, SAP benchmarks, and other research" and "Actual benefits may vary". Treat them as planning priors, not outcomes.
5. Do not cite the IDC "368% ROI, 8-month payback" figure as AI ROI. It is for SAP Integration Suite.
6. Do not quote a "70% people and process" or any TCO split as a measured finding. No verified source for a numeric split was opened.

## 2. The value gap: what sceptics and surveys say

| Finding | Source and sample | Tier | Caveat |
|---|---|---|---|
| 56% of CEOs report no significant financial benefit to date; 12% report both cost and revenue benefits | PwC 29th CEO Survey, 4,454 CEOs, Jan 2026 | B | Self-reported; PwC sells AI services |
| 37% attribute at least some EBIT impact to AI; about 6% are "high performers" | McKinsey State of AI 2026, 1,719 respondents, Aug 2026 | B | Self-reported |
| Only 5% achieve AI value at scale; 60% no material value | BCG, 1,250 executives, Sep 2025 | B | Self-reported; expected future impact counted unless stated realised |
| 15% of GenAI users report significant measurable ROI; typical satisfactory ROI in 2 to 4 years vs 7 to 12 months for usual technology | Deloitte, 1,854 executives (Europe, Middle East), Oct 2025 | B | Self-reported |
| 25% of initiatives delivered expected ROI; 16% scaled enterprise-wide | IBM CEO study, 2,000 CEOs, May 2025 | B | Vendor-sponsored |
| 42% of companies abandoned most AI initiatives (up from 17%) | S&P Global, 1,006 respondents, May 2025 | B | Survey |
| "95% of organizations getting zero return" | MIT NANDA, July 2025 | B (weak) | 52 interviews, 153 surveyed leaders, six-month window, "success" = deployment beyond pilot with KPIs; not peer-reviewed; press coverage described the sample differently from the PDF |
| Over 40% of agentic AI projects cancelled by end of 2027 | Gartner prediction, Jun 2025 | B (forecast) | A prediction, not a measurement |
| Inference cost per agentic workflow to rise more than fivefold through 2028 | Gartner prediction, Aug 2026 | B (forecast) | Prediction |
| Firms report AI raised annual labour-productivity growth by 0.2% over three years | Yotzov et al., NBER w34836, ~9,000 executives, 2026 | A/B | Central-bank-affiliated academic survey |
| Precise null effect on earnings and hours; effects above 2% ruled out | Humlum and Vestergaard, Danish administrative data, NBER w33777 | A | Two years after ChatGPT launch; about worker-level labour-market outcomes |

**How to present:** the direction is consistent across sources; the magnitude is uncertain; MIT's headline number is the weakest. Say that. A client who hears the sceptical evidence from us first is more likely to trust the rest.

## 3. Where measured gains exist

| Finding | Source and sample | Tier | Caveat |
|---|---|---|---|
| +14% issues resolved per hour; +34% for novices; minimal for experienced agents | Brynjolfsson, Li, Raymond, 5,179 support agents, NBER w31161 / QJE 2025 | A | One firm, support work |
| +12.2% tasks, 25.1% faster inside the "frontier"; 19% less likely to be correct outside it | Dell'Acqua et al., 758 BCG consultants | A | GPT-4 era; consulting tasks |
| 5.4% of work hours saved by users (about 2.2 hours a week); 1.4% across all workers | St. Louis Fed, Aug/Nov 2024 survey | B | Self-reported time |
| 80% report individual productivity improvement | McKinsey 2026 | B | Self-reported; coexists with only 37% reporting EBIT impact |
| Gains "largest in structured, measurable work" | Stanford AI Index 2026 | A/B (compilation) | Compilation |
| Commits +30% (autocomplete) to +240% (autonomous agents), but releases only +30% and no increase in app usage | Demirer et al., NBER w35275, 500,000+ GitHub developers | A | Output is not outcome |
| Positive ROI reported by 80%; strongly positive for 35% of departments measuring growth vs 13% measuring efficiency only | Wharton/GBK AI Adoption Report 2026 | B | Sample not captured |

## 4. Knowledge-assistant evaluations (government, Copilot-style)

| Evaluation | Result | Tier |
|---|---|---|
| UK GDS cross-government, 20,000 staff | Self-reported 26 min/day saved; adoption about 80% sustained; no control group | B |
| UK DWP, 3,549 licences | 19 min/day (regression vs non-users); 65% daily use (volunteers, self-report) | B |
| UK HMRC, 3,000 randomised licences | About 60 min/week after a ~20% downward adjustment; 83% used licence; 46% of non-users cited security/privacy | B (most conservative) |
| UK DBT, 1,000 licences | Weekly active 64%; daily 30% on working days; **did not find evidence time savings led to improved productivity**; some tasks took longer | B (null on productivity) |
| Australian Treasury, 218 staff, 14 weeks | Most used it 2 to 3 times a week or less; no clear evidence of improved work outcomes; break-even for licence cost about 13 minutes/week | B (null on outcomes) |

## 5. Developer productivity

| Finding | Source | Tier | Caveat |
|---|---|---|---|
| Tasks took 19% longer with AI; developers believed they were 20% faster | METR RCT, 16 experienced developers, 246 tasks, Jul 2025 | A | Small n; experienced developers on familiar mature repos |
| Follow-up: -18% and -4% time (faster), but authors call the data unreliable due to selection | METR, Feb 2026 | A (unreliable) | Authors' own caveat |
| About 21% less time on task | Google RCT, 96 engineers | A/B | Authors are Google employees; one task |
| +8.69% pull requests, +84% successful builds | GitHub/Accenture | D | Vendor-run; sample size not disclosed |
| Per 25% more AI adoption: +2.1% individual productivity, -1.5% throughput, -7.2% stability (2024); 2025: throughput now positive, stability still negative | DORA | B | Association, not causal |
| ABAP: "80% reported higher productivity; average gain 35%" | IDC white paper as cited by SAP (paper not opened) | D | SAP-promoted; tools may not be SAP's |
| ABAP: SAP estimates 20% less time writing and 25% less testing ABAP | SAP Release Highlights Q3 2025 | D | Estimate, not measurement |
| Bosch Digital: 20% productivity; 15% to 20% faster unit testing | SAP Release Highlights Q2 2026 | D | Method not stated |

**No independent study** of ABAP AI productivity, AI-assisted clean-core remediation or SAP test automation was found.

## 6. Finance, procurement, supply chain, service desk

| Finding | Source | Tier | Caveat |
|---|---|---|---|
| Cost per invoice $2.67 (best-in-class) vs $12.50 (others); touchless 55.2% vs 31.4%; approval cycle 4.1 vs 15.4 days | Ardent Partners AP Metrics 2026 (about 200 leaders), via Basware | B | Not AI-specific; best-in-class undefined |
| 91% of PO-referenced invoices automated; about 500 hours a month saved | De Agostini with SAP Document AI | C/D | SAP blog; story page not opened |
| 70% touchless (Oct 2025) vs about 60% (Dec 2025) | FRoSTA with SAP Build Process Automation + Document AI | C/D | Two SAP posts disagree |
| Exception orders cut from 2 to 5 days to 20 to 30 minutes; scope is the 20% of orders that were not automatic | Levi Strauss, SAP keynote quote | C | Agents not stated to be Joule-branded |
| >90% e-invoice auto-matching (35,000 invoices a year) | Rhätische Bahn with Basware | C | Not generative AI |
| 95% cash-application automation; DSO down about 33 days in 10 months | ResMed with HighRadius | D | Vendor case study; no baseline |
| Receivables automation more than doubled; 57,000 hours; 3-day vs 5-day close | Accenture Finance (custom, built on SAP platform) | C | Own finance function at very large scale; baselines not given |
| 7% reduction in HR support cases; 2 hours of HR workload eliminated per week | HR Path Brazil with Joule in SuccessFactors | C | Small and honest; shows realistic scale |
| Deflection 40% to 88% | Moveworks customer stories | D | No common definition; no independent realised rate |
| Forecast error -52%, inventory carrying cost -41%, expedites -59% ("up to") | Hackett "AI World Class" modelling | D | Modelled, method undisclosed; do not use |
| Excess working capital EUR 1.26 trillion (about 14% of revenue) among 1,000 largest European companies | Hackett working-capital survey, Nov 2026 | B | Size-of-prize context, not an AI result |
| **No independent or measured supply-chain forecasting/shortage case** | - | - | Insufficient evidence; run a controlled pilot |

## 7. Reversals and failures (use them)

| Case | What happened |
|---|---|
| Klarna | Claimed AI assistant did the work of about 700 agents (Feb 2024); CEO later said cost-weighting produced "lower quality" and the firm began recruiting human agents again (Fortune, May 2025). Klarna remains "AI-first" and says revenue rose while costs stayed flat (Nov 2025) |
| Commonwealth Bank of Australia | Reversed 45 job cuts after a voice-bot raised call volumes; called it an "error" (Aug 2025) |
| Deloitte Australia | Partial refund on a A$440,000 report with nonexistent citations (Oct 2025) |
| Air Canada | Tribunal held the airline liable for its chatbot's wrong policy statement (Feb 2024) |
| McDonald's / IBM | Ended drive-thru voice AI test (June 2024) |

## 8. Cost evidence

| Finding | Source | Tier |
|---|---|---|
| Fixed-capability inference prices fell 9x to 900x a year (median 50x) | Epoch AI, Mar 2025 | A/B |
| Frontier-tier list price fell from $15/$75 per million tokens (Opus 4.1) to $4/$20 (Opus 5.5); an agent session of one hour at 50k input and 15k output tokens is about $0.58 in the provider's own example | Provider price page, read 2026-11-23 | Primary price list |
| Derived cost per interaction: about $0.001 (small model, short Q&A) to about $0.10 (large model, RAG) | Calculation from list prices with assumed token counts | Calculation |
| Newer tokenizers produce about 30% more tokens for the same text | Provider price page | Primary |
| Only 44% of firms track per-unit inference cost; 20% say operating costs constrained AI use | Deloitte 2026; McKinsey 2026 | B |
| Open-weight models can handle routine agent steps at a fraction of the cost (about 5 to 6x saving per task after retries) | Gartner note via The Register, Nov 2026 | B (secondary, paywalled) |
| SAP Generative AI Hub: tokens converted into capacity units, extended plan only; **no price per capacity unit or AI unit found** | SAP documentation | Basis only |
| Agent builder in Joule Studio free until Dec 2026, then premium | SAP, Oct 2026 | D (packaging statement) |
| Gains come from "organization capital acquired through learning-by-doing" | Babina, He, Jiang, NBER w35684, Aug 2026 | A/B |

Falling per-token prices at fixed capability do not mean falling bills: agentic workflows and longer contexts raise token volume.
