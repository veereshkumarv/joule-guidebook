# Handling "AI costs a lot and returns little": a Conversation Guide

For sales leads, architects and engagement leads. Principle: **agree with what is true in the objection, show the evidence, show the numbers including the unfavourable ones, then offer a structure where the client controls the downside.** Every figure below is traceable to `01-evidence-register.md`.

## 1. The opening position (use almost verbatim)

> "You're right to be sceptical, and the evidence backs you up. Across independent surveys, most companies still cannot show financial impact: PwC found 56% of 4,454 CEOs saw no significant benefit to date; McKinsey found 37% attribute any EBIT impact. Many headline failure rates are weaker than they sound, and most surveys are self-reported by firms that sell AI services, so we don't rely on them in either direction. What we can do is measure it on your processes before you commit the budget, show you the case where it doesn't pay, and let you stop early."

## 2. Objections and responses

| Objection | Response | Evidence |
|---|---|---|
| "95% of AI projects fail (MIT)" | Fair concern, weak number. It rests on 52 interviews and 153 surveyed leaders, a six-month window, and a definition of success as deployment beyond pilot with KPIs; it is not peer-reviewed. The direction matches other sources (S&P: 42% abandoned most initiatives; IDC with Lenovo: 4 of 33 POCs reached production). The lesson is to design for the pilot-to-production gap: owners, baselines, adoption plan. | Evidence register section 2 |
| "Vendor numbers are marketing" | Agreed. We label every figure by source type. SAP's own estimates carry the footnote "Actual benefits may vary". Named SAP customer results are unaudited, and two conflict with themselves. We use them as analogues and only count independently supported benefits in the base case. | SAP-specific evidence file |
| "Show me comparable cases" | Here is what exists and how good it is (section 3 of this guide). For several use cases (supply-chain forecasting, ABAP productivity) there is no independent evidence yet; we say so and propose a controlled pilot to create it. | Use-case cards |
| "The licence and consumption costs are hidden" | Costs we can state: SAP's structure is Base AI (no extra charge, per product), Premium AI (AI units), and developer/platform items. Joule Studio's agent builder is free until December 2026, then premium. Generative AI Hub is metered in tokens converted to capacity units on the extended plan. We cannot state prices until SAP quotes them, so the model carries the licence as an explicit input and shows how the result moves with it. | VERIFY register V1, V2, V9 |
| "Inference costs will balloon" | Possible: Gartner forecasts agentic cost per workflow to rise more than fivefold through 2028 even while fixed-capability token prices fall 9x to 900x a year. Only 44% of firms track unit cost; we track cost per interaction and per accepted outcome from day one, route routine steps to cheaper models, and set quotas and alerts. | Cost evidence |
| "Our people will just save a few minutes; nothing changes" | That is the most common outcome in government trials: UK DBT found no evidence time savings improved productivity. So we credit saved time at 10% to 25% realisation unless a named owner redeploys it, and we put the unrealised capacity in the "soft" column. | Model, section 2 |
| "Why not wait until it is cheaper and better?" | A reasonable option for generic tools. Two considerations: the benefit of waiting is real for fixed-capability prices; the cost is lost learning, since academic work attributes AI gains to organisational capital built by learning-by-doing (NBER w35684). A small, cheap, gated pilot buys that learning without a large commitment. | Evidence register |
| "Will you cut headcount?" | We do not position it that way. Klarna rehired human agents after quality dropped; CBA reversed 45 job cuts. We target capacity for named higher-value work and external spend. | Reversals table |
| "What if it gives wrong answers?" | Grounding reduces but does not eliminate errors: the one independent test of RAG-based commercial tools found 17% to 33% hallucination in legal research. We measure the rate on your data, require sources, compute numbers in tools, abstain when unsure, and keep humans approving actions. | Confidence chapter |
| "Is our data used to train models?" | SAP publicly states it does not share customer data with anyone to train or improve large language models. That is a public statement; we confirm it against your contract and each model provider's terms in writing. | VERIFY register V5 |
| "Why a knowledge graph or MCP? Sounds like more cost" | Only where they earn their place. Independent evidence says graphs help multi-hop relationship questions and not simple lookups, so we run a bake-off on your questions and drop the graph if it doesn't win. MCP is a standard tool interface; its security is not automatic, so we mandate authorization controls. | Confidence chapter; forecasting chapter |

## 3. The comparables, presented honestly (a one-slide table)

| Use case | Best comparable | Source type | What we plan on |
|---|---|---|---|
| AP exceptions | Best-in-class touchless 55.2% vs 31.4% others | Benchmark (B) | 10% to 20% time reduction, partly realised |
| Cash application | ResMed 95% automated, DSO down about 33 days | Vendor (D) | Nothing until measured |
| Close commentary | Accenture: over 90% of commentaries approved | Customer-reported (C) | 10% to 25% |
| Supply-chain planning | SLB: forecast accuracy about 50% to about 90% on some lines | Customer-reported via SAP (C) | Nothing until measured |
| Service desk | Vendor stories 40% to 88%; HR Path 7% fewer cases | Vendor (D) and customer (C) | Nothing in base; start at about 20% |
| Knowledge assistant | HMRC about 60 min a week; DBT null | Government evaluations (B) | 0 to 30 min a week per active user |
| Developer productivity | METR -19% vs Google +21% (time) | Randomised trials (A) | 0% to 5% of coding time |

## 4. Showing the unfavourable number
Present the model output (`02-business-case-model.md`) as it stands: conservative and base cases are negative for a programme of about EUR 1M, because the independently supported benefits cover about 17% of the benefit needed to break even. Then say:

> "That is why we don't propose a EUR 1M programme. We propose a gated discovery-plus-pilot of about EUR 0.25M to 0.45M whose job is to measure the benefits that could change this picture (working capital, expedite and penalty cost, service-desk deflection, assistant time, developer productivity), and a scale decision only if the measured benefit run-rate exceeds measured run cost. If it doesn't, you've spent a fraction of the budget and have a documented answer."

(The pilot cost range comes from the guidebook's placeholders and must be rebuilt from the rate card.)

## 5. The offer structure that transfers risk
1. Fixed-fee readiness phase ending in a signed baseline and written licence quote.
2. Pilot tranche with kill criteria agreed up front (adoption, accepted-answer rate, cost per interaction).
3. Measured benefits classified and signed by Finance; matched control group where feasible.
4. Scale funding released only when measured benefit run-rate exceeds measured run cost including AI units.
5. Optional fee-at-risk linked to agreed KPIs. Note that no independent evidence was found on whether outcome-based pricing improves results; propose it only where measurement is robust.

## 6. What we will not say
- "AI typically pays back in X months." Deloitte reports 2 to 4 years as typical for satisfactory ROI, against 7 to 12 months for conventional technology; the independent evidence does not support a universal payback.
- "SAP customers see N% savings." SAP-published figures are unaudited and sometimes inconsistent.
- "The knowledge graph / MCP makes answers accurate / secure." Neither is shown by the evidence found.
- "No data leaves the SAP boundary." Not true if external models are used (corrected in the guidebook).
- Any figure from the Hackett "up to" modelling, the IDC Integration Suite ROI, or the expected-benefit statements (Novartis, SEIDOR, Aeropuertos Argentina's May article) as realised results.
