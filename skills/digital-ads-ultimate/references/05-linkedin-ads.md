# 05 LinkedIn Ads

LinkedIn is the B2B precision engine: you buy people by job, company, and seniority. It is also the most expensive per click of the four platforms, so it only pays when deal value is high and targeting is tight.

Currency of facts: no official LinkedIn "2026 best practices" guide was found during research. Benchmarks below come from vendors and vary widely. Use them only to sanity check, and replace them with account data fast.

## 1. When LinkedIn is worth it

```
Break-even CPL (see 01) vs expected LinkedIn CPL
Expected CPL = CPC / landing-or-form conversion rate
```

Typical practitioner ranges (heuristic, vary by region/industry): CPC several USD up to double digits for senior B2B, form conversion rates higher on Lead Gen Forms than on landing pages. If break-even CPL is lower than the expected CPL, do not start on LinkedIn. Use Google Search plus Meta retargeting first, or raise the offer's value.

Good fits: SaaS with ACV in the thousands of USD or more, enterprise/B2B services, recruiting/employer brand, events, high-ticket training for managers and executives, ABM against named accounts.

## 2. Objectives and formats

| Goal | Objective | Format notes |
| --- | --- | --- |
| Lead capture | Lead generation | Lead Gen Forms (prefilled), best with an asset or demo offer |
| Website leads/sales | Website conversions | Needs Insight Tag/CAPI and conversions defined |
| Traffic to content | Website visits | Optimize on landing page clicks, not impressions |
| Engagement/social proof | Engagement | Good for Thought Leader Ads and retargeting seed audiences |
| Brand | Brand awareness / Video views | Pair with measurement of lift or branded search |
| Hiring | Job applicants | Employer brand creative |

Formats: single image, carousel, video, document ads (PDF carousels, strong for gated or insight content), Conversation/message ads (use sparingly, relevance critical), event ads, text/dynamic ads (low priority), **Thought Leader Ads** (boost a person's or company's organic post, including from employees/experts, with permission).

## 3. Targeting

### Build around ICP

Define ideal customer profile: industry, company size, geography, function, seniority, job titles, pains. Start with 2 to 4 audience segments and test.

| Method | Use |
| --- | --- |
| Job titles/functions + seniority | Core targeting. Combine function+seniority, avoid stacking too many narrow facets |
| Company lists (ABM) | Upload named accounts (match rates vary, expect partial matches) |
| Contact lists | Prospect or customer emails, for retargeting/exclusions |
| Website retargeting | Insight Tag; segment by pages (pricing, product, blog) |
| Engagement/video retargeting | People who watched or interacted |
| Predictive audiences | Platform-built from your conversion data, when available |
| Interests/groups | Weak signal, use cautiously |

Audience size: LinkedIn's planning range shown in Campaign Manager is a guide. Practitioners commonly target about 50,000 to 300,000 members for cold audiences (heuristic). Below roughly 10,000 delivery is thin and fatigue sets in fast. Matched Audiences (lists, CAPI-matched) need at least 300 members to be usable (per LinkedIn's developer documentation).

Settings to review on every campaign:
- **Audience expansion**: off at first, test later.
- **LinkedIn Audience Network**: off at first for quality control, test later.
- Exclude your own employees, competitors, existing customers (or run them separately), and job titles that are irrelevant (students, interns, recruiters) when needed.
- Language/location: check member language targeting and data quality for the country.

Indonesia note: audiences are smaller. Use broader function/seniority groups, regional (APAC/SEA) expansions when the offer supports it, and lean on ABM lists plus retargeting.

## 4. Campaign structure

```
Campaign group: {Product or Offer} {Quarter}
  Campaign 1: Cold ICP - Offer A (Lead Gen Form or landing page)
  Campaign 2: Cold ICP - Thought Leader Ads (engagement/awareness feeding retargeting)
  Campaign 3: Retargeting - site/video/engagers -> demo or consultation offer
  Campaign 4: ABM - named accounts (smaller budget, higher bids)
```

One audience per campaign keeps reads clean. 3 to 5 creatives per campaign. Rotate evenly while testing.

## 5. Bidding and budget

Options: maximum delivery (automated, bills per impression), cost cap, manual CPC. Practitioner consensus is mixed:

- New campaigns: maximum delivery for fast learning with a hard budget cap and daily monitoring, or manual CPC starting a bit below LinkedIn's suggested range if you need cost control. Claims that automation "overspends by ~50%" are unsourced, so test against your own account.
- Use **cost cap** when you know target cost per result and have conversion volume.
- Raise bids if delivery is below budget and relevance is high; lower them if CPC is far above value.

Budget: LinkedIn has minimum daily/lifetime budgets (verify in Campaign Manager). Give each campaign enough to collect meaningful clicks per week; if one campaign gets only a handful of leads a month, pool audiences or lengthen the test window.

## 6. Lead Gen Forms vs landing pages

| | Lead Gen Form | Landing page |
| --- | --- | --- |
| Conversion rate | Higher (prefilled, native) | Lower |
| Lead quality | Lower on average, needs qualification | Higher intent |
| Data | Name, email, company, title prefilled | You control fields |
| Best for | Webinars, guides, templates, quick offers | Demos, pricing-led offers, complex products |

Quality controls: hidden or custom qualification questions (company size, role, timeline), disable "easy submit" style shortcuts only if quality suffers, sync to CRM immediately, filter free-email domains, follow up within minutes. Feed down-funnel results back via the Conversions API so LinkedIn can find similar accounts.

## 7. Thought Leader Ads

- Boost posts from real people (founder, expert, executive) so the ad appears with a personal profile, often earning lower cost per engagement than standard single-image ads (vendor benchmarks differ: one 2026 vendor report cites median CTR near 2.7% vs about 0.4% for single image, another cites about 4.7% vs 0.7%; budget share advice ranges from single digits to 40%). Do not copy those figures as targets, they use different definitions.
- Patterns seen in vendor analyses of top performers: first-person voice, a concrete insight or story instead of a pitch, links placed late in the post text, visuals native to the feed (photos/slides rather than glossy ads).
- Need author permission and an approval flow. Use organic posts that already perform as seeds.
- Use TLAs for audience warming and retargeting pool growth, then convert via a lead form or demo offer to a retargeted audience.

## 8. Creative and copy

- Lead with a business problem, a number, or a counterintuitive insight for the role you are targeting. Speak in their metrics (pipeline, churn, hiring time, audit risk).
- Intro text: first 150 characters show before truncation (verify current limits). Headline 70 characters or less.
- Social proof that is real: customer logos with permission, named case studies, concrete results with timeframe.
- Document ads: use a cover that states the benefit and 6 to 12 pages of scannable value; gate after a few pages if using Lead Gen Form.
- Offer ladder: content (guide, benchmark) -> low-friction interaction (audit, calculator, webinar) -> high-intent (demo, consultation). Retarget upwards.
- CTA says what happens: "Get the 2026 salary benchmark (PDF)", "Book a 20-minute pipeline audit".

## 9. Tracking and attribution

- Install **Insight Tag**, add **Conversions API** for server-side signal, define conversions with sensible attribution windows (click and view) that match your sales cycle.
- Tag key pages for retargeting segments (pricing, product, case studies, demo page).
- UTM everything (`utm_source=linkedin`, `utm_medium=paid_social`, `utm_campaign`, `utm_content`), because LinkedIn and CRM attribution differ.
- B2B cycles are long. Judge on pipeline sourced/influenced and cost per qualified opportunity, not just CPL. Use offline conversions from the CRM.
- Check company-level engagement reports (account engagement) for ABM.

## 10. Weekly LinkedIn routine

1. Delivery vs budget, bid competitiveness, audience size trend.
2. CTR, CPC, CPL by creative; pause creatives with sustained poor CTR after enough impressions.
3. Lead quality: share of leads that match ICP, MQL/SQL rates by campaign.
4. Frequency and audience fatigue; refresh creative every 2 to 4 weeks for small audiences.
5. Retargeting pools growing? Move spend toward retargeting offers as pools mature.
6. CRM reconciliation: leads, meetings, opportunities by campaign.
7. Exclusions: employees, competitors, current customers.

## 11. Failure modes

| Symptom | Likely cause | Fix |
| --- | --- | --- |
| High CPC, low CTR | Message not role-specific, crowded audience | Sharper pain-led copy, test TLAs, narrow or shift audience |
| Many leads, few meetings | Lead Gen Form friction too low, wrong ICP | Add qualifying questions, tighten targeting, change offer, speed follow-up |
| Delivery stalls | Audience too small, bid too low | Broaden, increase bid, extend duration |
| Good clicks, no form fills | Landing page mismatch, long form | Match ad promise, shorten, test Lead Gen Form |
| CPL fine, pipeline poor | Wrong stage offer or wrong titles | Offer closer to buying decision, retarget, exclude non-decision roles |
