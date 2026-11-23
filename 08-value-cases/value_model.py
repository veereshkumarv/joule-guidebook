#!/usr/bin/env python3
"""Evidence-gated, discounted business-case model for an SAP AI programme.

Illustrative client: mid-size manufacturer, EUR 800M revenue, 2,500 SAP users.
Every input is a PLANNING ASSUMPTION to be replaced with client baselines.
Rules (see 02-business-case-model.md):
  * Benefits whose only support is vendor-claimed (tier D) appear ONLY in the upside case.
  * Time savings are capacity, not cash: they are multiplied by a realisation factor.
  * Costs are the unvalidated placeholders from the guidebook (mid-client column) and the
    licence/AI-unit uplift is an explicit input that defaults to 0 until SAP quotes it.

Usage:  python3 value_model.py            (prints all tables)
        python3 value_model.py --licence 150000
"""
import argparse

CASES = ("conservative", "base", "upside")
IDX = {c: i for i, c in enumerate(CASES)}


def pick(triple, case):
    return triple[IDX[case]]


# ---- shared inputs -------------------------------------------------------------------
HOURLY = 55          # EUR loaded cost per hour (guidebook Part 4)
CTRL_DAY = 550       # EUR per controller day (guidebook Part 4)
DEV_DAY = 700        # EUR per developer day (assumption)
COST_OF_CAPITAL = 0.08
DISCOUNT_RATE = 0.10

# realisation: share of saved time that becomes cash or named redeployed work
REAL_PROCESS = (0.25, 0.50, 0.75)  # process-specific, named work (AP team, controllers, devs)
REAL_DIFFUSE = (0.10, 0.25, 0.50)  # spread across many users (assistant, navigation)

# ---- benefits: steady-state annual value, EUR ----------------------------------------
# Each returns (value, tier). Tier: A/B independent evidence, C customer-reported, D vendor-only.


def b_ap_exceptions(case):
    hours = 40_000 * 0.09 * 25 / 60            # 1,500 h baseline
    red = pick((0.10, 0.20, 0.40), case)
    return hours * red * HOURLY * pick(REAL_PROCESS, case), "B/C"


def b_variance_commentary(case):
    days = 12 * 2.5 * 12                        # 360 controller-days baseline
    red = pick((0.10, 0.25, 0.50), case)
    return days * red * CTRL_DAY * pick(REAL_PROCESS, case), "C"


def b_assistant_time(case):
    users, weeks = 800, 44
    active = pick((0.22, 0.50, 0.64), case)     # Treasury / DBT telemetry range
    mins = pick((0, 30, 60), case)              # 0 = DBT null; 60 = HMRC conservative cohort
    hours = users * active * (mins / 60) * weeks
    return hours * HOURLY * pick(REAL_DIFFUSE, case), "B"


def b_developer(case):
    devs, days, eligible = 20, 220, 0.30
    gain = pick((0.0, 0.05, 0.15), case)        # METR negative .. Google RCT positive
    return devs * days * eligible * gain * DEV_DAY * pick(REAL_PROCESS, case), "A/B"


def b_service_desk(case):                       # vendor-only evidence -> upside only
    if case != "upside":
        return 0.0, "D"
    return 6000 * 18 * 0.40 * 0.75, "D"


def b_working_capital(case):                    # vendor-only evidence -> upside only
    if case != "upside":
        return 0.0, "D"
    days_dso = 1.0
    return 800_000_000 / 365 * days_dso * COST_OF_CAPITAL, "D"


def b_supply_chain(case):                       # no independent evidence -> upside only
    if case != "upside":
        return 0.0, "D"
    return 2_000_000 * 0.10 * 0.5, "D"


BENEFITS = (
    ("AP exception handling", b_ap_exceptions),
    ("Variance commentary (controllers)", b_variance_commentary),
    ("Assistant / navigation time (800 users)", b_assistant_time),
    ("SAP developer productivity (20 devs)", b_developer),
    ("Service-desk deflection", b_service_desk),
    ("Working capital (1 day DSO)", b_working_capital),
    ("Supply-chain expedite/penalty (10%)", b_supply_chain),
)

# ---- costs: guidebook mid-client placeholders, kEUR (low, high) ----------------------
COST_RANGES = {
    "discovery": (50, 90), "pilot": (200, 350), "scale": (400, 800),
    "change": (80, 150), "run": (100, 200), "consumption": (40, 120),
}


def cost_value(name, case, mult=1.0):
    lo, hi = COST_RANGES[name]
    # conservative case = worst (high) cost; base = midpoint; upside = low cost
    v = {"conservative": hi, "base": (lo + hi) / 2, "upside": lo}[case]
    return v * 1000 * mult


def costs_by_year(case, licence, mult=1.0):
    c = lambda n: cost_value(n, case, mult)
    y1 = c("discovery") + c("pilot") + 0.4 * c("scale") + 0.5 * c("change") + 0.5 * c("run") + 0.5 * c("consumption")
    y2 = 0.6 * c("scale") + 0.5 * c("change") + c("run") + c("consumption") + licence
    y3 = c("run") + c("consumption") + licence
    return [y1, y2, y3]


RAMP = (0.10, 0.60, 1.00)  # share of steady-state benefit realised in years 1..3


def npv(flows, r=DISCOUNT_RATE):
    return sum(f / (1 + r) ** (t + 1) for t, f in enumerate(flows))


def evaluate(case, licence=0.0, cost_mult=1.0, benefit_mult=1.0):
    steady = sum(fn(case)[0] for _, fn in BENEFITS) * benefit_mult
    benefits = [steady * r for r in RAMP]
    costs = costs_by_year(case, licence, cost_mult)
    net = [b - c for b, c in zip(benefits, costs)]
    cum, run = [], 0.0
    for n in net:
        run += n
        cum.append(run)
    return dict(steady=steady, benefits=benefits, costs=costs, net=net, cum=cum, npv=npv(net))


def breakeven_steady_benefit(case, licence=0.0, cost_mult=1.0):
    """Steady-state annual benefit needed for 3-year NPV = 0 at this case's costs."""
    costs = costs_by_year(case, licence, cost_mult)
    pv_cost = npv(costs)
    pv_ramp = npv(list(RAMP))
    return pv_cost / pv_ramp


def k(x):
    return f"{x / 1000:,.0f}k"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--licence", type=float, default=0.0, help="annual licence/AI-unit uplift in EUR from year 2")
    a = ap.parse_args()

    print("STEADY-STATE ANNUAL BENEFIT BY ITEM (EUR)  [tier: A/B independent, C customer, D vendor-only]")
    print(f"{'item':44}{'conserv.':>10}{'base':>10}{'upside':>10}  tier")
    tot = dict.fromkeys(CASES, 0.0)
    for name, fn in BENEFITS:
        vals = [fn(c)[0] for c in CASES]
        for c, v in zip(CASES, vals):
            tot[c] += v
        print(f"{name:44}" + "".join(f"{k(v):>10}" for v in vals) + f"  {fn('base')[1]}")
    print(f"{'TOTAL steady-state':44}" + "".join(f"{k(tot[c]):>10}" for c in CASES))

    print(f"\n3-YEAR VIEW (licence uplift EUR {a.licence:,.0f}/yr from Y2; discount {DISCOUNT_RATE:.0%})")
    for c in CASES:
        r = evaluate(c, a.licence)
        print(f"\n{c.upper()}")
        print("  year           Y1        Y2        Y3")
        print("  benefits " + "".join(f"{k(x):>9}" for x in r["benefits"]))
        print("  costs    " + "".join(f"{k(x):>9}" for x in r["costs"]))
        print("  net      " + "".join(f"{k(x):>9}" for x in r["net"]))
        print("  cumul.   " + "".join(f"{k(x):>9}" for x in r["cum"]))
        print(f"  3-yr NPV {k(r['npv'])}   break-even steady-state benefit needed: {k(breakeven_steady_benefit(c, a.licence))}")

    print("\nBASE CASE NPV (kEUR) vs programme-cost multiplier and licence uplift")
    mults = (0.5, 0.75, 1.0)
    lics = (0, 100_000, 250_000)
    print(f"{'licence/yr':>12}" + "".join(f"{'cost x' + str(m):>12}" for m in mults))
    for L in lics:
        print(f"{L:>12,}" + "".join(f"{k(evaluate('base', L, m)['npv']):>12}" for m in mults))

    print("\nBASE CASE NPV (kEUR) vs benefit multiplier (licence 0)")
    for bm in (0.5, 1.0, 1.5, 2.0, 3.0):
        print(f"  benefits x{bm:<4} NPV {k(evaluate('base', 0, 1.0, bm)['npv'])}")


if __name__ == "__main__":
    main()
