# Business Case Model (replaces guidebook Part 5.3)

Runnable model: `value_model.py` (standard library only). Run `python3 value_model.py` and `python3 value_model.py --licence 150000`. All inputs are **planning assumptions** for an illustrative mid-size manufacturer (EUR 800M revenue, 2,500 SAP users) to be replaced with client baselines. Costs are the guidebook's own unvalidated placeholders; the licence/AI-unit uplift is **zero until SAP provides a quote** and is shown as a sensitivity.

## 1. Why the old table was replaced
The original 5.3 table assumed hard benefits of EUR 0.9M (year 2) and 1.4M (year 3). The four worked samples in Part 4 total about EUR 0.42M a year, mostly capacity not cash. The rebuilt model fixes four things: benefits are **evidence-gated**, time savings are **converted to cash only through a realisation factor**, cash flows are **discounted**, and the model reports **what would have to be true** to break even.

## 2. Method

**Benefit classes (record one per benefit):**
| Class | Meaning | Enters base case? |
|---|---|---|
| Cashable | External spend, overtime, contractors, avoided hiring, working-capital financing | Yes, if evidence tier A to C |
| Redeployable | Capacity redirected to named work with an owner | Yes, multiplied by a realisation factor |
| Soft | Satisfaction, speed, "better decisions" | No |
| Risk avoided | Expected loss = frequency x severity from the client's own incident/audit history | Only with client loss data |

**Evidence gate** (`01-evidence-register.md`): benefits supported only by vendor or consultancy claims (tier D) appear **only in the upside case**. A client pilot that measures a benefit promotes it to the base case.

**Realisation factors** (share of saved time that becomes cash or named redeployed work):
| Work type | Conservative / Base / Upside | Why |
|---|---|---|
| Process-specific named work (AP team, controllers, SAP developers) | 25% / 50% / 75% | A manager can redirect or release the capacity |
| Diffuse time spread over many users (assistant, navigation) | 10% / 25% / 50% | BCG 2026: 66% of frontline users get little or no guidance on using saved time; UK DBT found no evidence time savings improved productivity |

**Ramp:** 10% / 60% / 100% of steady-state benefit in years 1 / 2 / 3. **Discount rate:** 10%. **Cost of capital for working-capital value:** 8%. **Horizon:** 3 years (benefits beyond year 3 are not credited; see section 5).

**Costs** (guidebook 5.2 mid-client ranges, EUR k): discovery 50 to 90; pilot 200 to 350; scale-out 400 to 800; change management 80 to 150; annual run 100 to 200; annual consumption 40 to 120. Conservative uses the top of each range, base the midpoint, upside the bottom. Licence uplift is an input.

## 3. Benefits by item (steady state, EUR per year; model output)

| Item | Conservative | Base | Upside | Tier |
|---|---|---|---|---|
| AP exception handling (1,500 baseline hours; 10% / 20% / 40% reduction) | 2k | 8k | 25k | B/C |
| Variance commentary (360 controller-days; 10% / 25% / 50%) | 5k | 25k | 74k | C |
| Assistant/navigation time (800 users; active 22% / 50% / 64%; 0 / 30 / 60 min a week) | 0k | 121k | 620k | B |
| SAP developer productivity (20 developers; 0% / 5% / 15% on 30% eligible time) | 0k | 23k | 104k | A/B |
| Service-desk deflection (6,000 tickets at EUR 18; upside only, 40%) | 0k | 0k | 32k | D |
| Working capital (1 day DSO at EUR 800M revenue, 8% = EUR 175k; upside only) | 0k | 0k | 175k | D |
| Supply-chain expedite/penalty (10% of EUR 2M, 50% realised; upside only) | 0k | 0k | 100k | D |
| **Total steady state** | **7k** | **177k** | **1,130k** | |

Three observations that matter for the client conversation:
1. The upside is dominated by one diffuse-time item (EUR 620k) and by three vendor-only items. Without them the upside would be about EUR 0.3M.
2. Base-case AP exception handling is worth only about EUR 8k a year at these volumes. Each exception is worth about EUR 2.29 at 20% reduction and 50% realisation, so covering EUR 50k of incremental run cost needs about 21,800 exceptions a year.
3. A conservative reading of the independent evidence is close to zero for productivity items (DBT and METR found no gain or a slowdown in their settings).

## 4. Results (3-year, discounted; EUR thousands; licence uplift 0)

| | Conservative | Base | Upside |
|---|---|---|---|
| Year 1 net | -994 | -740 | -407 |
| Year 2 net | -871 | -541 | +258 |
| Year 3 net | -313 | -53 | +990 |
| Cumulative at end of Y3 | -2,178 | -1,334 | +841 |
| 3-year NPV at 10% | -1,859 | -1,160 | +587 |
| Steady-state benefit needed to break even | 1,396 | 1,044 | 691 |

With a EUR 150k a year licence uplift from year 2, base NPV falls to about -1,396k.

**Base-case NPV sensitivity (EUR k):**
| Licence uplift per year | Cost x 0.5 | Cost x 0.75 | Cost x 1.0 |
|---|---|---|---|
| 0 | -461 | -810 | -1,160 |
| 100,000 | -619 | -968 | -1,317 |
| 250,000 | -856 | -1,205 | -1,554 |

Even tripling base benefits leaves NPV at about -686k.

## 5. What this result means (read before presenting)

**What it says.** With the guidebook's placeholder costs, what we can defend with independent evidence (about EUR 177k a year) covers only **17% of the EUR 1.04M steady-state benefit needed to break even** in three years. Base-case annual run and consumption cost alone (about EUR 230k) exceeds base benefits. The case turns positive only if the vendor-claimed items (working capital, supply-chain, deflection) and the diffuse-time item at the upside parameters are all real.

**What it does not say.**
- It does not show AI cannot pay back. The cost inputs are unvalidated placeholders, the benefit set is eight narrow use cases, risk-avoided and strategic benefits are excluded, and benefits after year 3 are not credited.
- It does show that **a programme costing about EUR 1M cannot be justified on labour-time savings from a handful of use cases**, which is exactly the argument clients are making.

**Design consequences (these are the levers that change the answer):**
1. **Cost discipline:** standard-first and embedded Base AI where it exists (no AI-unit charge per SAP documentation, per product), custom builds only where standard capability does not cover the need, and shared platform costs across scenarios. Halving programme cost raises the base-case break-even requirement down to about EUR 0.52M a year.
2. **Aim at cash-linked benefits:** working capital, external spend, expedite and penalty costs, contractor and BPO reduction. These are only credited at upside today because the independent evidence is missing, so **the pilot's job is to measure them and move them into the base case**.
3. **Portfolio breadth on one platform:** run cost should be spread across many scenarios; a single scenario rarely carries a platform.
4. **Stage the money:** fund discovery and the pilot only; release scale-out funds when measured benefits reach pre-agreed thresholds (section 6).
5. **Check the run-rate:** before any scale decision compare measured annual benefit with measured annual run cost including AI units. If benefit is below run cost, do not scale.

## 6. Stage gates and kill criteria

| Gate | Evidence required | Release | Stop or pivot if |
|---|---|---|---|
| G0 discovery | Signed baselines; benefit register with class and tier; licence quote in writing | Pilot tranche | Baseline cannot be measured; no named owner; licence cost removes the case at base-case benefits |
| G1 pilot mid-point (week 12 of live use) | Weekly active use ≥ agreed (e.g. 40% of invited); accepted-answer rate ≥ agreed (e.g. 70%); cost per interaction within budget | Continue pilot | Below thresholds after remediation attempt |
| G2 pilot end | Measured KPI delta vs control; measured run cost; benefits reclassified by tier | Scale tranche 1 | Measured benefit run-rate below measured run cost |
| G3 scale review (quarterly) | Benefit vs plan; adoption; incidents | Next tranche | Two consecutive quarters below plan, or retirement criteria met |

Thresholds are examples; set them with Finance.

## 7. How to adapt for a client
1. Replace each input with a sampled baseline (minimum 30 observations or a system extract) and record the method.
2. Fill the licence/AI-unit line from SAP's written quote.
3. Replace the placeholder costs with the rate card and team mix.
4. Add benefits only with a named owner, class, tier and measurement method.
5. Present conservative, base and upside side by side, plus the break-even requirement and the stage gates.
6. Re-run after the pilot with measured values; discard assumptions that the pilot replaced.

## 8. Known limitations of the model
- Three-year horizon and no terminal value; benefits probably continue after year 3, costs too.
- Ramp and realisation factors are judgement; show them as inputs the client can change.
- Costs are placeholders; the largest uncertainty is SAP licence and consumption cost.
- Independent evidence for most SAP-specific items does not exist; tiers reflect that.
- No allowance for rework or stability cost from AI-generated code (DORA finds stability worsens with adoption), nor for the possibility that inference cost per agentic workflow rises (Gartner forecasts more than fivefold through 2028).
