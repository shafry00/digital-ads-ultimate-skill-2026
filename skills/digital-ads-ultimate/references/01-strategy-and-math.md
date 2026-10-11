# 01 Strategy and Unit Economics

Everything downstream (bids, budgets, kill rules) comes from this file. Do it first.

## 1. Unit economics

```
Contribution per sale  = price - COGS - variable costs (shipping, payment fee, platform fee, support)
Contribution margin %  = contribution per sale / price
Break-even CPA         = contribution per sale          (first-order basis)
Break-even ROAS        = 1 / contribution margin %      (price / contribution)
Target CPA             = break-even CPA x (1 - desired profit share)   e.g. x 0.6 to 0.7
Target ROAS            = 1 / (contribution margin % x (1 - desired profit share))
MER (blended)          = total revenue / total ad spend
POAS                   = contribution before ads (from ad sales) / ad spend, break-even 1.0 (= ROAS x contribution margin %)
TACoS                  = ad spend / total store sales (marketplaces)
New-customer CAC       = ad spend / new customers
LTV:CAC                = lifetime contribution / CAC   (healthy range commonly cited: 3:1 or better; heuristic)
Payback period         = CAC / monthly contribution per customer
```

Example (IDR): price Rp 300.000, COGS + shipping + fees Rp 165.000. Contribution Rp 135.000 (45%). Break-even CPA Rp 135.000, break-even ROAS 2.22. With a 30% profit cushion, target CPA about Rp 95.000, target ROAS about 3.2.

If the business wins on repeat purchases, a first-order loss can be rational. Allow it only when the user has real repeat data (cohort repurchase rate) and the cash to wait. Otherwise plan to break even on the first order.

### Lead-gen economics (leads, calls, demos)

```
Value per lead  = lead-to-sale rate x contribution per sale
Break-even CPL  = value per lead
Target CPL      = break-even CPL x 0.6 to 0.7
```

Chain the funnel with real rates: lead -> qualified -> booked -> showed -> closed. If the user has no rates, ask for last 20 to 50 leads and count outcomes. With no data at all, label the CPL target provisional and plan to replace it after 30 to 50 leads reach a CRM outcome.

Optimize toward the **deepest event with enough volume**, not the cheapest event. A cheap form fill that never closes is the most common way lead-gen accounts burn money.

### Info products and courses

Low-ticket digital products have near-100% margin on COGS but real fees (payment, affiliate, platform). Use contribution after fees. Funnel is usually ad -> landing/sales page -> checkout, plus order bumps and email follow-up. Count revenue from bumps, upsells, and the first 7 to 30 days of email in the allowable CAC only if tracked.

## 2. Platform fit

Pick platforms by where the buyer is and how the purchase happens, not by trend.

| Business | Start with | Add next | Notes |
| --- | --- | --- | --- |
| Ecommerce, visual product, impulse to mid price | Meta, TikTok | Google Shopping/PMax for demand capture | Meta/TikTok create demand, Google captures it |
| Ecommerce, searched products, known category | Google Shopping/PMax, Search | Meta for retargeting and prospecting | Search intent is the cheapest source of buyers |
| Local service (clinic, salon, repair, tutoring) | Google Search (+ Maps/local), Meta with WhatsApp | TikTok for awareness | Phone and WhatsApp calls are conversions, track them |
| Info product, course, coaching | Meta, TikTok | Google Search on problem keywords | Creative and offer carry the result |
| B2B SaaS, ACV high | LinkedIn, Google Search | Meta retargeting | LinkedIn is expensive per click, justify with deal size |
| B2B SMB, low ACV | Google Search, Meta | LinkedIn only if ACV supports cost | Check break-even CPL against LinkedIn's typical cost |
| Mobile app | Meta, TikTok, Google App campaigns | Apple/other | Needs MMP and event setup |
| Marketplace seller (Shopee, Tokopedia, TikTok Shop) | Marketplace ads on proven products, TikTok GMV Max | Meta/TikTok/creators to feed marketplace traffic | See `12-marketplace-ads.md`, judge by POAS and MER |

Heuristic: LinkedIn CPCs are often several times Meta's. If break-even CPL is below roughly what 20 to 30 clicks cost on LinkedIn at the user's conversion rate, LinkedIn probably does not fit yet. Compute it, do not guess (`ads_math.py funnel`).

## 3. Funnel and objective map

| Stage | Goal | Typical campaign | Judge by |
| --- | --- | --- | --- |
| Capture existing demand | Buyers already searching | Google Search, Shopping, brand | CPA/ROAS, impression share |
| Create demand | New people who do not know you | Meta prospecting, TikTok, YouTube/Demand Gen, LinkedIn | CPA/ROAS at account level, new-customer share, assisted conversions |
| Convert warm | Visitors, engagers, past leads | Retargeting on all platforms | CPA/ROAS, frequency, incrementality |
| Retain | Customers, repeat, referral | Customer lists, email/WhatsApp (not ads only) | Repeat rate, LTV |

Start simple: one prospecting engine + one capture engine + one small retargeting layer. Add complexity only when a layer saturates.

## 4. Budget planning

### Minimum viable test budget

Platforms optimize on conversion events. Starve them and they cannot learn.

```
Daily budget per ad set/ad group  >=  target CPA x (events needed per week / 7)
```

Meta and TikTok both talk about roughly 50 optimization events per ad set or ad group per week to exit learning (verify in the account's learning status). That implies daily budget about 7x target CPA. If that is unaffordable, move up the funnel to a cheaper event (add to cart, lead instead of purchase), consolidate ad sets, or run fewer campaigns. Do not split a small budget across many ad sets.

Google Smart Bidding has no fixed floor, but a common rule of thumb is about 30 conversions per 30 days per campaign before tCPA/tROAS behaves reliably (heuristic, Google does not publish a hard minimum). With fewer, use Maximize Conversions without a target, or optimize toward a higher-volume proxy conversion.

### Starting allocation (heuristic, adjust to data)

| Situation | Suggested split |
| --- | --- |
| New account, ecommerce | 60% best-fit prospecting platform, 20% retargeting, 20% capture (Search/Shopping) |
| New account, local/lead gen | 60 to 70% Google Search, 30 to 40% Meta/TikTok lead or WhatsApp |
| New account, B2B | 50% LinkedIn or Google Search (whichever is cheaper per qualified lead), 30% retargeting, 20% test |
| Mature account | Shift by marginal CPA, not average. Fund the next dollar where it buys the cheapest incremental conversion |

Reserve about 10 to 20% as an experiment budget once the account has a proven baseline.

### Sizing for a revenue goal

```
Required conversions = revenue goal / AOV
Required clicks      = conversions / landing conversion rate
Required spend       = clicks x CPC            (or impressions x CPM / 1000)
```

Run it with a pessimistic, base, and optimistic case. Sanity check against target CPA. If required spend exceeds budget, the plan changes (raise AOV, improve CVR, lower expectations), not the math.

## 5. Offer and positioning checks (cheapest lever)

Before blaming the platform, check the offer. Weak offers cannot be fixed by targeting.

- Is the outcome specific, believable, and relevant to a segment?
- Is there a reason to act now that is true (real deadline, real stock limit, real seasonal need)?
- Is risk addressed truthfully (return policy, free trial, free consultation)? Only promise guarantees the business honors.
- Is the price anchored against a real alternative the buyer considers?
- Does the first click land on a page that continues the ad's promise?

## 6. Operating calendar (first 30 days)

| Days | Focus |
| --- | --- |
| Pre-launch | Math, tracking QA, creative, landing page, policy check |
| 1 to 3 | Launch, verify delivery and event firing, check search terms and placements. No big edits |
| 4 to 7 | Let learning finish. Kill only clear waste (irrelevant queries, zero-delivery, policy flags) |
| 8 to 14 | First real read once conversion lag has passed. Pause bottom creatives, add 2 to 4 new concepts |
| 15 to 30 | Scale winners in steps, start a structured test, build retargeting, fix landing page leaks |

## 7. Common strategic mistakes

- Starting with 6 campaigns on a budget that supports 1.
- Optimizing for clicks or traffic when the goal is sales.
- Judging a campaign before conversion lag or learning ends.
- Scaling on platform-reported ROAS that was never checked against the business's revenue.
- Running only one creative concept, then blaming the audience.
- Sending cold traffic to a homepage.
- Treating brand search conversions as proof that ads create demand.
