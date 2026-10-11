# 09 Optimization, Scaling, and Diagnosis

Optimization is controlled change: diagnose the layer, change one lever, log it, read it after the window. Panic edits destroy both learning and the ability to know what worked.

## 1. Before judging anything

A campaign is **readable** only if all are true:
- Tracking verified and unbroken during the window.
- Learning has had a fair chance (platform learning status cleared or the equivalent data volume gathered).
- Conversion lag has passed (check the typical click-to-conversion delay).
- No major concurrent changes (site, price, promo, budget jumps, creative swaps).
- Enough volume that noise is smaller than the effect (see significance in `11`).

If any is false, label the data "not yet readable" and say what to wait for.

## 2. Layered diagnosis (always top down)

```
1 DELIVERY     Is it spending? Approved? Limited by budget/bid/audience/policy?
2 COST TO REACH  CPM / CPC trend and auction pressure
3 ATTENTION    Hook rate, CTR (link), thumb-stop
4 LANDING      Landing page view rate, bounce, load speed, message match
5 CONVERSION   CVR on page/form/checkout, add-to-cart to purchase
6 VALUE        AOV, lead quality, close rate, refund, LTV
7 MEASUREMENT  Platform vs source of truth gap, attribution, dedup
```

Equation chain: `CPA = CPM / 1000 / (CTR x CVR)` per impression-based view, or `CPA = CPC / CVR`. Find which factor moved vs the prior comparable window, then fix that layer only.

| What moved | Interpretation | Primary levers |
| --- | --- | --- |
| CPM up | Auction heat, seasonality, audience narrowing, low relevance | Broaden audience, new creative, shift timing, avoid peak events if inefficient |
| CTR down | Fatigue, weak hook, audience mismatch | New hooks/concepts, refresh, check frequency, review placements |
| CPC up | CTR down or CPM up | See both rows above |
| CVR down | Landing/offer/tracking problem, traffic mix shift | Landing test, offer, speed, check segment mix by device/source |
| AOV down | Product mix, discounting | Bundles, thresholds, upsell, adjust target |
| Platform CPA good, business CPA poor | Attribution inflation, lead quality | Reconcile to CRM, optimize deeper, check dedup |
| CPA fine but volume low | Limited reach/budget/targets too tight | Raise budget, loosen target, expand audiences/keywords |

## 3. Decision rules

Use these as defaults and state when you deviate. They are heuristics, not platform rules.

### Pause / reduce
- Spend of at least about 2 to 3 x target CPA with zero conversions on a readable ad (cut it unless it is the only one supplying top-of-funnel evidence).
- CPA above 1.5 x target for the full readable window and worsening trend, after landing and tracking were ruled out.
- Policy or brand-risk flag, broken destination, tracking corruption (stop immediately, then fix).
- Search terms irrelevant: exclude the terms rather than pausing a healthy campaign.

### Keep / iterate
- CPA within target to 1.2 x target with stable or improving trend: keep, improve creatives or CVR.
- Good CTR but weak CVR: keep the ad, fix the page/offer.
- Low volume with good efficiency: raise budget or widen reach.

### Scale
All must hold: readable data, CPA or ROAS at or better than target for the window, at least one other creative or audience can absorb spend, inventory/fulfillment capacity, and cash buffer.

| Platform | Typical scale step (heuristic) |
| --- | --- |
| Google Search/Shopping/PMax | 10 to 20% budget increments every few days; relax tCPA/tROAS gradually |
| Meta | 15 to 25% every 2 to 3 days, or duplicate; bigger steps after a very stable week |
| TikTok | 20 to 30% every 2 to 3 days, or duplicate, with new creative supply |
| LinkedIn | Expand audience or raise bids before budget; check frequency |

After each step, evaluate marginal CPA (change in spend vs change in conversions), not just average CPA. Revert if marginal CPA exceeds break-even for two consecutive reads.

### Learning protection
Avoid more than one significant change (bid strategy, budget jump over about 30%, targeting, major creative swap) per campaign inside the learning window. Exceptions: tracking fixes, policy fixes, runaway spend.

## 4. Fatigue detection

Signals (per creative or ad set, vs its own first week):
- Frequency rising.
- CTR or hook rate falling for several consecutive days.
- CPM stable or rising while conversion rate flat.
- CPA rising with otherwise stable traffic quality.

Actions: introduce new concepts first, then refresh hooks on winners, then broaden audience. Keep the old winner running in parallel as a control until the new ad proves itself.

## 5. Weekly operating cycle (60 to 90 minutes per platform)

```
Mon  Pull last 7 vs prior 7 days. Check tracking health and spend pacing.
Tue  Diagnose by layer. Decide scale/hold/fix per campaign. Write recommendations.
Wed  Launch new creative/tests. Implement approved changes. Log them.
Thu  Light check: delivery, policy, any breakage.
Fri  Reconcile platforms vs source of truth. Plan next week's concepts and budget.
```

Daily (10 minutes): spend vs cap, tracking, policy, anomalies. Do not optimize on a single day.

Monthly: cohort and payback check, platform mix review by marginal efficiency, creative library review, landing page test results, forecast vs actual, strategy reset.

## 6. Budget reallocation

1. Compute marginal CPA or ROAS by campaign over the last readable window.
2. Move budget from the weakest marginal return to the strongest, in steps (10 to 20%), keeping minimums for learning.
3. Hold a floor for retargeting and brand protection so demand creation does not starve the capture layer.
4. Re-check blended MER after 1 to 2 weeks.

## 7. Troubleshooting playbooks

### No conversions
1. Tracking: do events fire? Is the conversion status active? Did the site change?
2. Delivery: spend, impressions, approval, geo/placement restrictions.
3. Click quality: bot traffic, accidental clicks (very high CTR with near-zero landing view), in-app browser issues.
4. Landing: loads, form works, checkout works on mobile.
5. Offer and price vs audience.

### CPA suddenly up
Compare against change log, promo calendar, competitor pushes, seasonality, stock status, site speed, and attribution changes. Check segment mix (device, placement, geo). Roll back the last non-essential change if the timing matches.

### ROAS drops but orders steady
AOV changed, returns/discounting, attribution window shift, brand share shift, or PMax/Advantage+ moving to cheaper low-value buyers. Check value tracking.

### Spend not delivering
Budget too low for the target, bid/target too strict, audience too small, creative disapproved or limited, learning stuck, payment issue, schedule limits.

### Leads good on paper, sales say they are bad
Add qualification, tighten targeting and keywords, change the offer to repel tire-kickers, import offline outcomes, compare lead sources by close rate not CPL.

### Account restricted or ads disapproved
Read the exact reason, fix the cause (claim, landing page, category), appeal with the fix documented. Keep a clean fallback account and verified business assets. Do not rapidly resubmit similar ads.

## 8. Recommendation quality bar

Every recommendation needs: evidence (metric and window), mechanism, expected effect with assumptions, confidence, effort, verification step, rollback. Reject recommendations that are really just "monitor" or "optimize creative" without specifics.

Example:

```
[P1] Move Meta prospecting from Purchase to Add to Cart event for 10 days
Evidence:  Ad set A: 14 purchases in 21 days at Rp 210k CPA; learning limited since launch
Why:       <50 events/week prevents stable delivery
Expected:  Exit learning, more stable CPM; CPA per purchase should recover toward Rp 150k to 180k (assumes ATC-to-purchase rate holds)
Confidence: medium
Effort:    15 minutes
Verify:    Day 7: learning status, ATC cost, ATC-to-purchase rate
Rollback:  If purchase rate from ATC drops 30%+, restore Purchase optimization with a consolidated ad set
```

## 9. Cross-channel interplay

- Creation channels (Meta, TikTok, YouTube) lift branded search and direct traffic. Brand search growth after launch is a positive signal, not coincidence.
- Retargeting efficiency depends on prospecting volume. Cutting prospecting starves it within weeks.
- Do not judge a single channel in isolation. Check blended MER and new-customer CAC at least monthly.
