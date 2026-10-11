#!/usr/bin/env python3
"""Ad math: break-even, funnel forecast, budget sizing, A/B significance. Stdlib only.

  ads_math.py breakeven --price 300000 --cost 165000 [--profit-cushion 0.3]
  ads_math.py funnel --budget 15000000 --cpc 2500 --cvr 0.02 [--aov 300000]
  ads_math.py budget --cpa 95000 [--events-per-week 50]
  ads_math.py samplesize --baseline 0.02 --lift 0.25 [--alpha 0.05 --power 0.8]
  ads_math.py sig --a-n 4200 --a-conv 84 --b-n 4100 --b-conv 112
  ads_math.py selftest
"""
import argparse
import math
from statistics import NormalDist

Z = NormalDist()


def breakeven(price, cost, cushion=0.3):
    contrib = price - cost
    if contrib <= 0:
        raise SystemExit("cost >= price: no contribution, fix the offer before buying traffic")
    margin = contrib / price
    return {
        "contribution": contrib,
        "margin": margin,
        "breakeven_cpa": contrib,
        "breakeven_roas": 1 / margin,
        "target_cpa": contrib * (1 - cushion),
        "target_roas": 1 / (margin * (1 - cushion)),
    }


def funnel(budget, cpc, cvr, aov=None):
    clicks = budget / cpc
    conv = clicks * cvr
    out = {"clicks": clicks, "conversions": conv, "cpa": budget / conv if conv else math.inf}
    if aov:
        out["revenue"] = conv * aov
        out["roas"] = out["revenue"] / budget
    return out


def daily_budget(cpa, events_per_week=50):
    return cpa * events_per_week / 7


def sample_size(baseline, lift, alpha=0.05, power=0.8):
    """Per-variant n to detect a relative lift in a conversion rate (two-sided)."""
    p1, p2 = baseline, baseline * (1 + lift)
    za, zb = Z.inv_cdf(1 - alpha / 2), Z.inv_cdf(power)
    pbar = (p1 + p2) / 2
    num = (za * math.sqrt(2 * pbar * (1 - pbar)) + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2
    return math.ceil(num / (p2 - p1) ** 2)


def significance(an, ac, bn, bc):
    """Two-proportion z-test. Returns rates, relative lift of B over A, two-sided p."""
    pa, pb = ac / an, bc / bn
    pool = (ac + bc) / (an + bn)
    se = math.sqrt(pool * (1 - pool) * (1 / an + 1 / bn))
    z = (pb - pa) / se if se else 0.0
    return {"rate_a": pa, "rate_b": pb, "lift": (pb - pa) / pa if pa else math.inf,
            "z": z, "p_value": 2 * (1 - Z.cdf(abs(z)))}


def selftest():
    b = breakeven(300000, 165000, 0.3)
    assert round(b["breakeven_roas"], 2) == 2.22 and round(b["target_cpa"]) == 94500
    f = funnel(1_000_000, 2500, 0.02, 300000)
    assert round(f["conversions"], 1) == 8.0 and round(f["roas"], 2) == 2.4
    assert round(daily_budget(70000)) == 500000
    n = sample_size(0.02, 0.25)
    assert 13000 < n < 15000, n  # about 14k per arm
    s = significance(4000, 80, 4000, 80)
    assert abs(s["z"]) < 1e-9 and s["p_value"] > 0.99
    assert significance(4000, 80, 4000, 130)["p_value"] < 0.01
    print("ok")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("breakeven")
    a.add_argument("--price", type=float, required=True)
    a.add_argument("--cost", type=float, required=True, help="COGS + shipping + fees per sale")
    a.add_argument("--profit-cushion", type=float, default=0.3)
    a = sub.add_parser("funnel")
    a.add_argument("--budget", type=float, required=True)
    a.add_argument("--cpc", type=float, required=True)
    a.add_argument("--cvr", type=float, required=True, help="landing conversion rate, e.g. 0.02")
    a.add_argument("--aov", type=float)
    a = sub.add_parser("budget")
    a.add_argument("--cpa", type=float, required=True)
    a.add_argument("--events-per-week", type=float, default=50)
    a = sub.add_parser("samplesize")
    a.add_argument("--baseline", type=float, required=True)
    a.add_argument("--lift", type=float, required=True, help="relative lift, 0.2 = +20%%")
    a.add_argument("--alpha", type=float, default=0.05)
    a.add_argument("--power", type=float, default=0.8)
    a = sub.add_parser("sig")
    for k in ("a-n", "a-conv", "b-n", "b-conv"):
        a.add_argument("--" + k, type=float, required=True)
    sub.add_parser("selftest")
    x = p.parse_args()

    if x.cmd == "breakeven":
        r = breakeven(x.price, x.cost, x.profit_cushion)
    elif x.cmd == "funnel":
        r = funnel(x.budget, x.cpc, x.cvr, x.aov)
    elif x.cmd == "budget":
        r = {"min_daily_budget_per_ad_set": daily_budget(x.cpa, x.events_per_week)}
    elif x.cmd == "samplesize":
        r = {"per_variant": sample_size(x.baseline, x.lift, x.alpha, x.power)}
    elif x.cmd == "sig":
        r = significance(x.a_n, x.a_conv, x.b_n, x.b_conv)
        r["verdict"] = "significant at 95%" if r["p_value"] < 0.05 else "not significant, keep running or call it a tie"
    else:
        return selftest()
    for k, v in r.items():
        print(f"{k}: {v:,.4f}" if isinstance(v, float) else f"{k}: {v}")


if __name__ == "__main__":
    main()
