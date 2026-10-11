# 10 Audit Checklists

Use for full account audits. Each item is a **control**: pass (1), partial (0.5), fail (0), or N/A/unknown (excluded from the score, but listed). Severity weights: Critical 5, High 3, Medium 2, Low 1.

```
Section score = sum(weight x result) / sum(weight of applicable items) x 100
Overall = weighted average of platform scores by spend share
Bands: 85+ healthy, 70 to 84 minor issues, 50 to 69 meaningful leaks, below 50 structural problems
```

Rules: an item is only scored when you have evidence (screenshot, export, API pull). "Unknown" is not a pass. Cross-check thresholds against the account's own economics (see `01`), not a generic benchmark. Report quick wins (high impact, low effort) first.

Audit output skeleton: summary score + top 5 issues, per-section scores, findings table (item, severity, evidence, fix, effort), and a 30/60/90 plan. Use the recommendation format from `09` and templates in `11`.

## A. Cross-platform foundation

| ID | Check | Sev |
| --- | --- | --- |
| X1 | Break-even and target CPA/ROAS documented and approved | Critical |
| X2 | Primary conversion defined, matches business outcome, fires once | Critical |
| X3 | Conversion value/currency passed correctly (where used) | High |
| X4 | Browser + server tracking, deduplicated | High |
| X5 | Consent/privacy compliant, policy pages live | High |
| X6 | UTMs consistent and reaching analytics/CRM | Medium |
| X7 | Platform vs source-of-truth reconciliation done in last 30 days | High |
| X8 | Offline/CRM outcomes returned for lead gen | High |
| X9 | Landing page loads fast on mobile, message match with ads | High |
| X10 | Lead response process under 15 minutes (lead gen) | High |
| X11 | Budget caps and spend alerts set | Medium |
| X12 | Change log and test log maintained | Medium |
| X13 | Ad accounts secured (2FA, admins, billing owner) | Medium |
| X14 | Claims substantiated, policy-risk copy reviewed | High |

## B. Google Ads

| ID | Check | Sev |
| --- | --- | --- |
| G1 | Conversion actions: only meaningful ones set Primary, no duplicates (for example page view or click-to-call counted as sale) | Critical |
| G2 | Enhanced conversions / offline import active where relevant | High |
| G3 | Brand and non-brand separated | High |
| G4 | Search terms reviewed weekly, negatives lists in place | High |
| G5 | Match types intentional, broad match only with strong signals and tested | Medium |
| G6 | Ad groups tightly themed, 2+ RSAs each, 10+ unique headlines | Medium |
| G7 | Assets/extensions complete (sitelinks, callouts, call/location where applicable) | Medium |
| G8 | Bidding aligned to data volume, targets realistic vs history | High |
| G9 | Budget not limiting profitable campaigns | High |
| G10 | Quality Score components checked for top spend keywords | Medium |
| G11 | Geo (presence vs interest), language, and schedule settings correct | High |
| G12 | PMax: brand exclusions, URL expansion controls, asset groups complete, holdout or sanity check on cannibalization | High |
| G13 | PMax/Shopping feed healthy: no mass disapprovals, titles and GTINs good | High |
| G14 | Demand Gen/YouTube: full asset sets, separate from retargeting for measurement | Medium |
| G15 | Audience lists built (remarketing, customer match) and used as exclusions/observation | Medium |
| G16 | Search partners/Display expansion settings reviewed on Search campaigns | Medium |
| G17 | Impression share lost to rank/budget reviewed for money campaigns | Medium |
| G18 | Experiments used for major changes (AI Max, broad match, tROAS) | Low |
| G19 | Auto-applied recommendations reviewed and unwanted ones disabled | High |
| G20 | Disapprovals and policy status clean | High |

## C. Meta Ads

| ID | Check | Sev |
| --- | --- | --- |
| M1 | Pixel + Conversions API live, deduplicated, strong event match quality | Critical |
| M2 | Domain verified, correct events prioritized/configured | Medium |
| M3 | Campaign objectives match the business goal, optimization event has enough volume | Critical |
| M4 | Structure consolidated; few ad sets, none starved ("learning limited" resolved) | High |
| M5 | Advantage+ audience/placements used, exclusions justified | Medium |
| M6 | Existing customers excluded from acquisition or capped | Medium |
| M7 | 5+ distinct creative concepts live in prospecting, not just variants | High |
| M8 | Creative mix across formats (video 9:16, static 4:5, carousel/UGC) | Medium |
| M9 | Fatigue monitored: frequency, CTR trend, new concepts on cadence | High |
| M10 | Advantage+ Creative enhancements reviewed deliberately | Medium |
| M11 | Retargeting segmented, converters excluded, budget proportionate | Medium |
| M12 | Lead ads: qualification, fast follow-up, CRM sync, quality feedback | High |
| M13 | Messaging/WhatsApp flow measured down to orders | High |
| M14 | Attribution setting consistent and understood | Medium |
| M15 | Special Ad Category compliance, no sensitive-attribute copy | High |
| M16 | Account quality/policy status clean, backup and permissions set | Medium |
| M17 | Placement and breakdown reviews done for outliers | Low |
| M18 | Naming conventions consistent | Low |

## D. LinkedIn Ads

| ID | Check | Sev |
| --- | --- | --- |
| L1 | Insight Tag and Conversions API installed, conversions defined with proper windows | Critical |
| L2 | Break-even CPL vs actual CPL supports the channel | Critical |
| L3 | ICP documented, audience built on function+seniority/company data | High |
| L4 | Audience size in a workable range, no needless over-narrowing | Medium |
| L5 | Audience Network and expansion deliberate (off or tested) | Medium |
| L6 | Employees/competitors/customers excluded as intended | Medium |
| L7 | Objective matches goal (lead gen vs conversions vs engagement) | High |
| L8 | Bidding matches data volume, budget pacing healthy | Medium |
| L9 | 3+ creatives per campaign, rotated, fresh within 4 weeks for small audiences | Medium |
| L10 | Thought Leader Ads used or considered with proper permissions | Low |
| L11 | Lead Gen Forms: qualification, CRM sync, follow-up SLA | High |
| L12 | Retargeting pools and ABM lists built, match rates checked | Medium |
| L13 | Offer ladder: content -> engagement -> demo | Medium |
| L14 | CRM-based reporting: cost per qualified lead/opportunity | High |
| L15 | Frequency and audience fatigue monitored | Medium |

## E. TikTok Ads

| ID | Check | Sev |
| --- | --- | --- |
| T1 | Pixel + Events API installed, deduplicated, match rate checked | Critical |
| T2 | Objective and optimization event match business goal and volume | Critical |
| T3 | Budget supports about 50 events/week per ad group, or event moved up funnel | High |
| T4 | Creative native 9:16, captions, hook in first 3 seconds | High |
| T5 | Weekly creative supply, 3+ distinct hooks per test | High |
| T6 | Fatigue monitored, refresh cadence defined | Medium |
| T7 | Spark Ads used for proven posts, authorization expiry tracked | Medium |
| T8 | Smart+ vs manual used deliberately, test lane maintained | Medium |
| T9 | Targeting broad where signal is strong, exclusions set | Medium |
| T10 | Retargeting built and converters excluded | Medium |
| T11 | In-app browser landing experience tested | High |
| T12 | Comments moderated, blocked words, inventory filter set | Low |
| T13 | Policy compliance (claims, partnership disclosure, music licensing) | High |
| T14 | TikTok Shop: product feed quality, GMV Max targets realistic, per-category campaigns | High |
| T15 | Lead gen: qualification and fast follow-up | High |

## H. Marketplace ads (Shopee, Tokopedia, TikTok Shop)

| ID | Check | Sev |
| --- | --- | --- |
| P1 | Per-product cost stack documented (fees, vouchers, shipping, affiliate, returns, COGS) | Critical |
| P2 | Break-even ROAS and target POAS set per product or margin group | Critical |
| P3 | Ad budget concentrated on products with POAS above target | High |
| P4 | Reports show POAS, MER, TACoS, not ROAS alone | High |
| P5 | Fee table and attribution rules checked in the last 30 days (rules change) | High |
| P6 | Listing quality, rating, price vs competitors, stock checked before ads | High |
| P7 | Low-margin products capped or excluded from ads | High |
| P8 | Campaign-day plan: stock, voucher depth, POAS floor | Medium |
| P9 | Affiliate/creator commission included in margin | High |
| P10 | Returns/cancel provision included | Medium |
| P11 | Automated campaigns (GMV Max style) have realistic targets, grouped by margin | Medium |
| P12 | Payout reconciliation vs reported sales | Medium |

## F. Scoring walkthrough (example)

Meta items scored: M1 pass (5), M3 pass (5), M4 fail (0 of 3), M7 partial (1.5 of 3), M12 pass (3), M9 fail (0 of 3). Sum applicable weights = 5+5+3+3+3+3 = 22. Score = (5+5+0+1.5+3+0)/22 = 14.5/22 = 66. Band: meaningful leaks. Fix M4 and M9 first (structure and fatigue), they unlock M7.

## G. Audit evidence checklist

Ask for or pull: 90 days of campaign/ad set/ad data, conversion settings, tracking diagnostics, search terms (Google), placements and breakdowns, audience definitions, creative list with spend, landing page URLs, CRM funnel counts, budget and economics sheet, change history, policy/disapproval list, and the last 3 tests with outcomes. Missing items go in an "evidence gaps" section and cap confidence.
