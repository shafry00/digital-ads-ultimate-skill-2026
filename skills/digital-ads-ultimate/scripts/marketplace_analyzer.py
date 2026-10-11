#!/usr/bin/env python3
"""Marketplace ads analyzer: ROAS, break-even ROAS, POAS, MER, TACoS from a CSV. Stdlib only.

  marketplace_analyzer.py sheet.csv [--total-sales 120000000] [--target-poas 1.3] [--min-orders 5]
  marketplace_analyzer.py selftest

Required columns: ad_spend, ad_sales. Optional: platform, campaign, orders, units, cogs_per_unit,
cogs_pct, fee_pct, fixed_fee_per_order, voucher_pct, shipping_subsidy_per_order, affiliate_pct,
return_pct. Percent columns are fractions (0.08 = 8%). Money is plain numbers (no "Rp", no dots).
Missing cost columns count as zero, which makes the result optimistic; the script warns.
POAS = contribution before ads / ad spend. Break-even = 1.0.
"""
import argparse
import csv
import sys

COSTS = ["fee_pct", "fixed_fee_per_order", "voucher_pct", "shipping_subsidy_per_order",
         "affiliate_pct", "return_pct"]


def num(row, key, default=0.0):
    v = (row.get(key) or "").strip().replace(",", "")
    if v.lower().startswith("rp"):
        v = v[2:]
    try:
        return float(v) if v else default
    except ValueError:
        raise SystemExit(f"bad number in column '{key}': {row.get(key)!r}")


def contribution(r):
    """Contribution before ads for one row's ad-attributed sales."""
    sales, orders, units = num(r, "ad_sales"), num(r, "orders"), num(r, "units")
    pct = sum(num(r, k) for k in ("fee_pct", "voucher_pct", "affiliate_pct", "return_pct"))
    per_order = num(r, "fixed_fee_per_order") + num(r, "shipping_subsidy_per_order")
    cogs = num(r, "cogs_per_unit") * (units or orders) if r.get("cogs_per_unit") else num(r, "cogs_pct") * sales
    return sales * (1 - pct) - per_order * orders - cogs


def verdict(poas, orders, target, min_orders):
    if orders < min_orders:
        return "LOW DATA"
    if poas >= target:
        return "SCALE"
    if poas >= 1.0:
        return "HOLD"
    if poas >= 0.7:
        return "FIX"
    return "CUT"


def analyze(rows, target=1.3, min_orders=5):
    out = []
    for r in rows:
        spend, sales = num(r, "ad_spend"), num(r, "ad_sales")
        if spend <= 0:
            continue
        c = contribution(r)
        roas, poas = sales / spend, c / spend
        out.append({
            "platform": r.get("platform", ""), "campaign": r.get("campaign") or r.get("sku", ""),
            "spend": spend, "sales": sales, "orders": num(r, "orders"),
            "roas": roas, "be_roas": sales / c if c > 0 else float("inf"),
            "poas": poas, "profit": c - spend,
            "verdict": verdict(poas, num(r, "orders"), target, min_orders),
        })
    return out


def portfolio(res, total_sales=None):
    spend, sales = sum(x["spend"] for x in res), sum(x["sales"] for x in res)
    contrib = sum(x["profit"] + x["spend"] for x in res)
    p = {"spend": spend, "ad_sales": sales, "roas": sales / spend, "poas": contrib / spend,
         "ad_profit": contrib - spend}
    if total_sales:
        margin = contrib / sales if sales else 0
        p.update(tacos=spend / total_sales, mer=total_sales / spend,
                 est_store_profit_after_ads=total_sales * margin - spend)
    return p


def fmt(v):
    return f"{v:,.0f}" if abs(v) >= 100 else f"{v:.2f}"


def report(path, total_sales, target, min_orders):
    with open(path, newline="", encoding="utf-8-sig") as f:
        rd = csv.DictReader(f)
        rows = list(rd)
        cols = set(rd.fieldnames or [])
    if not {"ad_spend", "ad_sales"} <= cols:
        raise SystemExit("CSV needs columns ad_spend and ad_sales")
    missing = [c for c in COSTS if c not in cols] + ([] if cols & {"cogs_per_unit", "cogs_pct"} else ["cogs"])
    if missing:
        print(f"WARNING: no {', '.join(missing)} column: treated as zero, results are optimistic\n", file=sys.stderr)
    res = analyze(rows, target, min_orders)
    if not res:
        raise SystemExit("no rows with ad_spend > 0")
    print(f"{'platform':<11}{'campaign':<22}{'spend':>12}{'ROAS':>7}{'BE-ROAS':>9}{'POAS':>7}{'profit':>13}  verdict")
    for x in sorted(res, key=lambda x: x["poas"]):
        print(f"{x['platform']:<11}{x['campaign'][:21]:<22}{fmt(x['spend']):>12}{x['roas']:>7.2f}"
              f"{x['be_roas']:>9.2f}{x['poas']:>7.2f}{fmt(x['profit']):>13}  {x['verdict']}")
    print()
    for k, v in portfolio(res, total_sales).items():
        print(f"{k}: {v:,.2f}")
    print(f"\nverdict rules: SCALE poas>={target}, HOLD 1.0-{target}, FIX 0.7-1.0, CUT <0.7, "
          f"LOW DATA orders<{min_orders} (heuristics, judge with trend and lag)")


def selftest():
    # price 150000: fee 8%, voucher 5%, fixed 1250, ship 3000, cogs 62000 -> contribution 64250/order
    row = {"ad_spend": "1000000", "ad_sales": "3000000", "orders": "20", "units": "20", "cogs_per_unit": "62000",
           "fee_pct": "0.08", "voucher_pct": "0.05", "fixed_fee_per_order": "1250", "shipping_subsidy_per_order": "3000"}
    x = analyze([row])[0]
    assert round(x["roas"], 2) == 3.0 and abs(x["poas"] - 1.285) < 1e-9, x
    assert round(x["be_roas"], 2) == 2.33, x
    assert x["verdict"] == "HOLD"  # 1.29 < 1.3 target
    low = analyze([{"ad_spend": "1000", "ad_sales": "5000", "orders": "1", "cogs_pct": "0.9"}])[0]
    assert low["verdict"] == "LOW DATA"
    loss = analyze([{"ad_spend": "100", "ad_sales": "500", "orders": "9", "cogs_pct": "0.92"}])[0]
    assert loss["verdict"] == "CUT" and loss["profit"] < 0  # ROAS 5, margin 8% -> POAS 0.4
    print("ok")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("csv")
    ap.add_argument("--total-sales", type=float)
    ap.add_argument("--target-poas", type=float, default=1.3)
    ap.add_argument("--min-orders", type=int, default=5)
    a = ap.parse_args()
    selftest() if a.csv == "selftest" else report(a.csv, a.total_sales, a.target_poas, a.min_orders)
