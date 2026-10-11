# 11 Testing, Reporting, and Templates

## 1. Testing system

### Hypothesis format

```
We believe [change] for [audience/placement] will [improve metric] by [rough size]
because [evidence/mechanism]. We will know in [duration] when [decision rule].
```

### Test design

- One variable per test (concept, hook, offer, landing section, audience, bid strategy).
- Equal conditions: same budget, schedule, audience. On Meta/TikTok, either separate ad sets with equal budgets or use the platform's A/B test tool (split test) for clean randomization. Google: campaign experiments/drafts with traffic split.
- Primary metric chosen **before** launch. Secondary metrics diagnose, they do not decide.
- Minimum run: whole business cycles (at least 7 days to cover weekday patterns) and past conversion lag.
- Stop rule fixed in advance (sample size or date). Do not peek and stop on a lucky day.

### Sample size and significance

Use `scripts/ads_math.py`:

```
python3 scripts/ads_math.py samplesize --baseline 0.02 --lift 0.25
python3 scripts/ads_math.py sig --a-n 4200 --a-conv 84 --b-n 4100 --b-conv 112
```

Practical guidance: with low baseline rates, detecting a 10 to 20% relative lift needs thousands of visitors per variant. If you cannot afford that, test bigger differences (new concept, new offer), choose a higher-volume proxy metric (CTR, add to cart), or accept directional evidence and say so. The common "100 conversions per variant" rule is a rough floor, not a guarantee.

Avoid: testing five things at once, declaring winners at 80% confidence on tiny samples, ignoring novelty effects, and comparing different time windows.

### Test backlog (ICE score)

Rank ideas by Impact x Confidence x Ease (1 to 10 each). Keep the backlog in the report.

| Priority tests by platform | Examples |
| --- | --- |
| Google | Broad vs phrase, tROAS level, RSA angles, landing page, PMax holdout, AI Max experiment |
| Meta | New concept vs control, Advantage+ vs manual, optimization event, lead form vs landing page, CTWA vs form |
| TikTok | Hook A/B/C, creator vs brand-made, Smart+ vs manual, 15s vs 30s |
| LinkedIn | TLA vs single image, Lead Gen Form vs landing page, job-title cluster A vs B, offer ladder step |

### Test log (keep in the repo or sheet)

`Date | Platform | Hypothesis | Variant IDs | Metric | Result | Decision | Learning`

## 2. Launch checklist

```
[ ] Break-even/target CPA approved, budget cap set
[ ] Primary conversion tested end to end, value/ID/currency correct
[ ] Browser + server events deduplicated; consent/privacy in place
[ ] UTMs and naming convention applied
[ ] Landing page: mobile speed OK, message match OK, form works, thank-you event once
[ ] Creative: 2+ concepts, policy-checked, safe zones, captions
[ ] Claims substantiated; no sensitive-attribute copy
[ ] Audiences/keywords set, exclusions and negatives in place
[ ] Campaign created PAUSED; settings reviewed (geo, language, schedule, placements, bidding, budget)
[ ] Lead handling owner and response SLA ready
[ ] Alerts for spend and tracking set
[ ] Approval from the user for go-live
[ ] 24-hour post-launch check scheduled
```

## 3. Campaign Blueprint template

```markdown
# Campaign Blueprint: {Business} | {Offer} | {Date}

## 1. Goal and economics
Goal / primary conversion:
Price / contribution / break-even CPA / target CPA / target ROAS:
Monthly budget / hard cap / test duration:

## 2. Platform plan
| Platform | Role (create/capture/retarget) | Budget % | Why |

## 3. Tracking spec
Events, parameters, dedup keys, offline events, UTMs, owner, QA status.

## 4. Structure
Campaign | Objective | Optimization event | Audience/keywords | Budget | Naming

## 5. Creative matrix
Concept | Angle | Awareness stage | Format | Hook variants | Proof | CTA | Status

## 6. Copy
(Per platform, per concept, with character counts)

## 7. Landing/lead flow
URL, key changes, form, response SLA, CRM stages.

## 8. Risks and compliance notes

## 9. First 14 days
Day 0 launch, Day 1 check, Day 3 first read, Day 7 review, Day 14 decision.

## 10. Success rules
Scale if... Pause if... Test next...
```

## 4. Weekly report template

```markdown
# Weekly Ads Report | {Business} | {Week}

## Headline
One sentence: what happened, why, what we do next.

## Scorecard (this week vs last week vs target)
Spend | Conversions | CPA/CPL | Revenue | ROAS/MER | New customer share | Qualified leads

## By platform
(Spend, results, efficiency, notes, status: scale / hold / fix)

## What worked / what did not
Top 3 creatives, top 3 queries or audiences, worst waste.

## Diagnosis
Layered read (delivery, cost, attention, landing, conversion, value, measurement).

## Recommendations (ranked P1/P2/P3)
Use the standard recommendation block from SKILL.md.

## Tests
Running, concluded (with result), next up.

## Risks and asks
Tracking, policy, stock, budget needs.
```

## 5. Monthly strategy review

Contribution after ad spend, blended MER, new-customer CAC, payback, cohort LTV, platform marginal efficiency, creative library performance, landing and funnel stats, test learnings, forecast vs actual, next month's budget and bets.

## 6. Account audit report template

```markdown
# Ads Audit | {Account} | {Date}
Overall score, band, spend covered, data window, evidence gaps
Top 5 issues (impact, effort)
Section scores (X, G, M, L, T)
Findings table: ID | Severity | Evidence | Fix | Effort | Owner
Quick wins (this week), 30/60/90 plan
Appendix: data pulled, assumptions, what was not checked
```

## 7. Creative testing scorecard

| Creative ID | Concept | Hook | Spend | Impr | Hook rate | CTR | CPC | CVR | CPA | Verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Verdict options: Winner (scale + iterate), Keep (needs more data), Kill, Rework (good hook, weak body or CTA).

## 8. Naming conventions

```
Campaign:  {PLATFORM}_{OBJ}_{FUNNEL}_{GEO}_{YYYYMM}      e.g. META_SALES_PROSP_ID_202610
Ad set/group: {AUDIENCE}_{PLACEMENT}_{EVENT}              e.g. BROAD_ADV+_PURCHASE
Ad:        {CONCEPT}_{HOOK}_{FORMAT}_{LEN}_{ID}          e.g. PAIN_H2_UGC_30s_017
```

IDs map to `utm_content` and the creative library.

## 9. Ad hoc prompts the skill should handle

- "Bikin strategi iklan untuk [bisnis], budget Rp X per bulan" -> intake, math, platform plan, blueprint.
- "Audit akun Meta saya" -> evidence request, checklist C + X, score, plan.
- "Kenapa CPA Google naik minggu ini?" -> layered diagnosis, change log check, ranked recommendations.
- "Tulis copy iklan TikTok untuk [produk]" -> messaging map, 5 hooks, scripts, compliance check.
- "Bagaimana scale kampanye ini?" -> readable-data check, scale gates, step plan, monitoring.
- "Weekly report" -> template above filled with data.
