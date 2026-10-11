# 12 Marketplace Ads: Shopee, Tokopedia, TikTok Shop

Marketplace ads are not Google or Meta ads with a different logo. The buyer is already shopping, the platform controls price visibility, fees, vouchers, and shipping, and the ad dashboard reports revenue that ignores most of your costs. The right scorecard is profit, not ROAS.

Currency of facts: fee tables, ad products, and attribution rules on these platforms change often (Shopee changed GMV Max attribution in May 2026 and category-based admin fees in 2026; Tokopedia and TikTok Shop were integrated in Indonesia in 2024 and their ad tooling has been moving). Numbers here are examples. Always read the current fee page in each Seller Center before computing margin.

## 1. The metric stack (use all of it)

| Metric | Formula | Answers | Blind spot |
| --- | --- | --- | --- |
| **ROAS** | ad-attributed sales / ad spend | Is the ad producing sales per rupiah | Ignores COGS, fees, vouchers, returns. Two products with the same ROAS can have opposite profit |
| **ACOS** | ad spend / ad-attributed sales (= 1 / ROAS) | Same as ROAS, inverted | Same |
| **TACoS** | ad spend / total store sales (ads + organic) | How dependent is the store on ads | Falling TACoS can be good (organic lift) or bad (ads cut too hard) |
| **MER** | total revenue / total marketing spend (all channels) | Is the whole marketing engine efficient | Needs honest total revenue and total spend; hides product-level leaks |
| **POAS** | contribution before ads (from ad-attributed sales) / ad spend | Profit per rupiah of ads | Needs a correct cost stack |
| **Net profit after ads** | contribution before ads - ad spend - overhead | Did we make money | Depends on overhead allocation |

Definitions used by this skill (state them in every report, other tools define POAS differently):

```
Net per order           = price - seller-funded voucher - commission/admin fee - order-processing fee
                          - payment fee - shipping subsidy - affiliate/creator commission
Contribution per unit   = net per order (per unit) - COGS - packaging/handling - return/cancel provision
Contribution margin %   = contribution per unit / price
POAS                    = (ad-attributed sales x contribution margin %) / ad spend      break-even = 1.0
POAS (identity)         = ROAS x contribution margin %
Break-even ROAS         = 1 / contribution margin %
Target ROAS             = break-even ROAS x target POAS
MER                     = total sales (all channels) / total marketing spend
TACoS                   = ad spend / total store sales
```

POAS 1.0 means ads paid for themselves at the contribution level. POAS 1.3 means each Rp 1 of ads returned Rp 1.30 of contribution before ad cost (Rp 0.30 profit). A planning target of roughly 1.2 to 1.5 leaves room for overhead and noise (heuristic, set it from the owner's overhead and risk appetite).

### Worked example (all numbers fictional)

Product A: price Rp 150.000. Commission 8%, order-processing fee Rp 1.250, seller voucher 5%, shipping subsidy Rp 3.000, COGS Rp 60.000, packaging Rp 2.000.

```
Net per order = 150.000 - 12.000 - 1.250 - 7.500 - 3.000 = 126.250
Contribution  = 126.250 - 62.000 = 64.250    (margin 42.8%)
Break-even ROAS = 150.000 / 64.250 = 2.33
Dashboard ROAS 3.0  ->  POAS = 3.0 x 0.4283 = 1.285   (profitable, thin cushion)
```

Product B: price Rp 80.000, contribution Rp 12.000 (15%). Dashboard ROAS 5.0 looks excellent, POAS = 5.0 x 0.15 = 0.75, a loss on every rupiah of ads. Break-even ROAS is 6.67, so a "good" ROAS target of 4 still loses money.

Rule: **never set a ROAS target from a generic number.** Derive it per product from break-even ROAS.

## 2. Cost stack checklist (collect once per product)

- Selling price (after seller-funded discount), real average realized price, not list price.
- Commission/admin fee by category and store tier (Shopee tiers by category and store status; TikTok Shop and Tokopedia have their own tables).
- Fixed per-order fees (order-processing fee), payment/transaction fees, program fees (free shipping programs, cashback programs, voucher programs).
- Shipping: subsidy you bear, return shipping, COD failure cost.
- Affiliate/creator commission (TikTok Shop and Shopee affiliate programs), sample costs.
- COGS landed (including inbound freight, packaging, quality loss).
- Return, cancel, and refund rate and their cost (use a provision per order from the last 90 days).
- Overhead per order (staff, warehouse), optional for POAS but required for net profit.

If any item is unknown, the analyzer assumes zero and the result is optimistic. Say so in the report.

## 3. Platform mechanics (verify in Seller Center)

### Shopee Ads

- Main formats reported by sources: product ads including GMV Max (automated, placement "All"), shop search ads, banner, and Live ads. Ad billing is mostly per click for search-style ads; GMV Max is automated with a ROAS/budget style target.
- **Attribution changes matter.** Shopee began applying new GMV Max attribution rules on 7 May 2026, reported to include click attribution over seven days. If reported ROAS jumps after a rule change without a change in store sales, you re-baselined the metric, not the business. Compare against total store sales (TACoS and MER) across the change date.
- Admin fees are tiered by product category and store type (reported 2026 range roughly 2,5% to 11,7% depending on category and Mall/Star/non-Star status), plus order-processing fee (reported Rp 1.250 per completed order since July 2025) and shipping program fees. Read the live table.
- Listing quality, rating, price competitiveness, chat response, stock, and shipping speed affect ad conversion more than ad settings do.

### Tokopedia

- After the 2024 integration with TikTok Shop, Tokopedia sellers operate under a Shop | Tokopedia model, and ad products (historically TopAds) and tooling have been in transition. No current official source on exact ad products was verified in this skill's research. Ask the user which ad products are visible in their Seller Center and what the fee page shows today, then treat that as the source of truth.
- Fundamentals still apply: promote products with proven conversion, keep reviews and stock healthy, use store-level voucher and free-shipping programs deliberately, and measure by profit.

### TikTok Shop

- GMV Max is the main Shop ad type for sales (reported as the default and only supported Shop Ads sales campaign type since mid-2025). It optimizes GMV against a budget and a target ROI. A high target ROI throttles spend, because it is a target, not a guarantee.
- Surfaces: shoppable videos, LIVE, product cards, search. Affiliates and creators drive a large share of sales, and creator commission is a real cost in POAS.
- Spark Ads on proven organic or creator videos keep social proof. See `06-tiktok-ads.md` for creative system, Events and policy.
- Separate campaigns by product or category so each can have its own budget and ROI target.

## 4. Operating model: listing first, ads second

```
Offer & price  ->  Listing quality  ->  Social proof  ->  Ads amplify  ->  Review profit weekly
```

1. **Price and offer**: check price against the closest 5 competitors on the marketplace, bundle to raise average order value, set voucher depth from contribution margin.
2. **Listing**: keyword-rich title, first 3 images that answer the buyer's top question, video, complete attributes, variants, size charts, honest description, clear shipping.
3. **Social proof**: rating, review count and photos, store score, chat response rate. Weak proof makes ads pay for clicks that do not convert.
4. **Ads** only on products that pass the readiness check: stock for 30+ days of expected volume, conversion rate at or above the category norm (compare to the store's own median), rating at a healthy level (heuristic: 4.5 or above), contribution margin high enough that a profitable ROAS is achievable.
5. **Profit review**: weekly POAS by product and campaign, MER and TACoS for the store.

## 5. Product portfolio triage

Score each SKU on contribution margin % and ad POAS, then act:

| Group | Profile | Action |
| --- | --- | --- |
| Hero | High margin, POAS above target, converts well | Scale budget in steps, add creative or creator content, protect stock |
| Traffic builder | Low margin, high volume, high CVR | Use for rank, reviews, and cross-sell. Cap loss, or run without ads, pair with a high-margin bundle |
| Margin lever | High margin, low traffic or weak listing | Fix listing and price first, then test ads |
| Drain | Low margin and POAS below 1 | Cut ads, raise price, change bundle or retire |

Heuristic: keep any single low-margin product from taking more than a modest share of ad budget unless it has a documented role (for example rank building for a launch window).

## 6. Setting targets

1. Compute break-even ROAS per product or product group from the cost stack.
2. Target ROAS = break-even ROAS x target POAS (you need more ROAS than break-even to earn profit). Example: break-even 2.33 x target POAS 1.3 = target ROAS about 3.0.
3. Give automated campaigns (GMV Max) a budget that can buy volume at that ROAS. A target set above what the listing can deliver starves spend. Lower the target gradually (for example 5 to 10% steps) when spend stalls and POAS has headroom, raise it gradually when POAS falls below target.
4. Group products with similar margins in one campaign so one target fits.

## 7. Calendar and campaign days

Indonesian marketplaces run recurring events: monthly paydays (around the 25th to the 1st), double dates (for example 9.9, 10.10, 11.11, 12.12), Harbolnas, Ramadan and Lebaran, school season, year-end. Pattern:

- 2 to 3 weeks before: confirm stock for the surge, set voucher and bundle plans from contribution margin, prepare creative and creator content, join official campaigns only where the contribution survives the campaign discount and fees.
- During: CPMs and CPCs rise. Volume goes up, margin per order may go down. Set a POAS floor you will not cross, and watch hourly or daily.
- After: expect a demand dip. Cut spend to match. Reconcile payouts and returns before declaring the event profitable.

## 8. Sheet-driven analysis (what the user can paste)

Minimum useful sheet (one row per product, campaign, or day):

| Column | Meaning |
| --- | --- |
| platform | shopee / tokopedia / tiktokshop |
| campaign (or sku) | row label |
| ad_spend | ad cost in the period |
| ad_sales | sales attributed to ads (GMV) |
| orders | ad-attributed orders |
| units | units sold through ads (optional) |
| price | average realized price (optional) |
| cogs_per_unit or cogs_pct | landed cost (one of the two) |
| fee_pct | commission/admin fee as fraction (0.08) |
| fixed_fee_per_order | order-processing and other fixed fees |
| voucher_pct | seller-funded voucher share of sales |
| shipping_subsidy_per_order | shipping cost the seller bears |
| affiliate_pct | creator or affiliate commission |
| return_pct | provision for returns and cancels, as a fraction of sales |
| impressions, clicks | optional, for CTR and CVR |

Plus optional store totals: `total_sales` for MER and TACoS.

Analyzer: `python3 scripts/marketplace_analyzer.py examples/marketplace_ads_sample.csv --total-sales 120000000 --target-poas 1.3`

It outputs per row: ROAS, break-even ROAS, POAS, contribution after ads, profit/loss, and a verdict (SCALE, HOLD, FIX, CUT, LOW DATA); and a portfolio block: blended ROAS, POAS, MER, TACoS, estimated profit. Missing cost columns default to zero and the script warns.

When no sheet exists, build a table by hand from the Seller Center ad reports and fees, and say which cells are assumptions.

## 9. Diagnosis for marketplaces

| Symptom | Likely cause | Check or fix |
| --- | --- | --- |
| ROAS fine, POAS below 1 | Margin thin, fee stack heavier than assumed, discounts | Recompute contribution, raise price or bundle, reduce voucher depth |
| ROAS jumped without store sales growth | Attribution rule change, halo of organic sales | Compare TACoS and MER, re-baseline |
| Spend high, orders low | Listing conversion weak, price uncompetitive, low rating, stockouts | Fix listing and price before more spend |
| GMV Max spend stalls | Target too high, low product score, small budget | Lower target in steps, check product labels and eligibility |
| Strong ads, weak total sales | Ads only capturing existing demand | Add traffic sources (creator, live, off-platform), check MER |
| Profit falls on campaign days | Discount plus fee plus ad cost stack | Set floor POAS, limit products, lower voucher depth |
| High returns | Description mismatch, quality, size issues | Fix listing, add size guide, QC, provision in POAS |
| TACoS rising for weeks | Organic sales shrinking or ads taking over | Check rank, reviews, stock, price vs competitors |

## 10. Cross-channel on marketplaces

Meta, TikTok video, creators, and Google can push traffic to marketplace listings, but marketplaces rarely return clean attribution to your ad accounts. Judge off-platform spend by MER and by marketplace store sales lift in the days after, using a before/after or a holdout across products or regions. Do not credit off-platform ads with marketplace sales without such evidence, and do not cut them just because marketplace dashboards show no direct conversions.

## 11. Recommendation example

```
[P1] Cut Shopee ad spend on SKU-B (kaos polos 3 pack) by 70%, keep a small test budget
Evidence:  14 days, spend Rp 4.2M, ad sales Rp 21M (ROAS 5.0), contribution margin 15% -> POAS 0.75, loss about Rp 1.05M
Why:       The margin cannot support a ROAS below 6.7, so even "good" ROAS loses money
Expected:  Saves about Rp 2.9M per 14 days, little GMV loss because SKU-B overlaps SKU-A bundle
Confidence: high
Effort:    10 minutes
Verify:    Day 7: store sales, TACoS, SKU-B organic rank
Rollback:  If store sales fall more than 10% with no other cause, restore budget to half
```
