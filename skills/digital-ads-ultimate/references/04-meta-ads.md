# 04 Meta Ads (Facebook and Instagram)

Meta is the demand-creation engine. Delivery is driven by creative: the system matches creative to people, so concept diversity and signal quality matter more than hand-built audiences.

Currency of facts: Advantage+ products, defaults, and attribution options changed through 2025 and 2026. Practitioner blogs often cite Meta internal numbers without sources. Treat uplift percentages as unverified and check Meta Business Help Center for the live rule.

## 1. Objectives (outcome-based)

| Business goal | Objective | Optimization event |
| --- | --- | --- |
| Online sales | Sales | Purchase (or Add to Cart/Initiate Checkout if purchase volume is too low) |
| Leads | Leads | Conversion leads (optimize for quality) or Leads; website lead event |
| WhatsApp/Messenger sales | Sales or Leads/Engagement with Messaging | Conversations, or purchase via messaging when event signal exists |
| Traffic to content | Traffic | Landing page views (not link clicks) |
| Awareness | Awareness | Reach / ThruPlay / Ad recall lift |
| App | App promotion | Install / in-app event |

Choose the lowest-funnel event that still yields enough volume (see `01` budget rule). Optimize for the thing that pays.

## 2. Account and campaign structure

Principle: **consolidate**. Fewer campaigns and ad sets give each more data and more room to exit learning.

Default starting structure (small to mid budget):

```
Campaign A: Prospecting (Sales/Leads)  Advantage+ or broad, 1 to 3 ad sets by concept family or placement strategy
Campaign B: Retargeting (lower budget)  Site/app/engagement/customer list, 7 to 30 day windows, exclude purchasers
Campaign C: Creative test (optional)    Isolated budget for new concepts using one ad set per test cell
```

- Use **Advantage+ sales/leads campaign** experiences where available. Provide customer lists as audience suggestions rather than restrictions, and an existing-customer cap if the goal is new customers.
- Use **Advantage+ audience** (broad with suggestions) and **Advantage+ placements** by default. Exclude placements only on evidence (for example, if Audience Network wastes spend in a specific account).
- Budget at campaign level (campaign budget optimization/Advantage campaign budget) when ad sets have similar goals. Use ad set budgets for cell-isolated tests.
- Minimum viable budget: see `01`. If you cannot afford about 50 optimization events per ad set per week, reduce ad sets or move up a funnel event.
- Naming: `PROSP | Sales | Broad | 2026-10 | Concept-A` and `RET | Sales | ATC30 | 2026-10`.

Learning phase: ad sets exit when they gather enough optimization events (Meta's published guideline is about 50 per week). "Learning limited" means the structure or budget cannot get there. Fix by consolidating, widening targeting, raising budget, or moving to a higher-volume event.

## 3. Audiences

### Prospecting

- Start **broad** (age/gender/location only, plus suggestions). Meta's delivery model now finds the buyer from creative signal and history.
- Detailed targeting interests act as suggestions under Advantage+. Use them for steering new accounts with no data, then remove if they hold delivery back.
- Lookalikes/value-based lookalikes as suggestions from the best customer source (purchasers, high-LTV customers, qualified leads). Larger seeds (hundreds to thousands) and higher-quality events beat bigger percentages.

### Retargeting

Segment by recency and intent and **exclude converters**:

| Audience | Window | Message |
| --- | --- | --- |
| Product/page viewers | 7 to 14 days | Reminder, benefit, objection |
| Add to cart/checkout starters | 3 to 7 days | Urgency (real), shipping, guarantee, support |
| Engaged video viewers/IG engagers | 30 to 60 days | Proof, deeper education |
| Past customers | 30 to 180 days | Cross-sell, replenishment, referral |

Keep retargeting small and cheap. If retargeting looks amazing and prospecting struggles, the account is harvesting demand that already existed. Judge on blended results.

### Exclusions

Existing customers (for acquisition), recent converters, employees, and leads already in CRM when appropriate.

## 4. Creative: the main lever

Meta's retrieval system favors **diversity**. Many near-identical variations are treated as one idea. Plan **concepts**, then variations.

### Concept matrix

Vary these dimensions (different problem, promise, proof, format, person):

| Dimension | Examples |
| --- | --- |
| Angle | pain removal, aspiration, comparison, myth-busting, how-it-works, price/value, social proof, founder story |
| Format | UGC-style selfie video, product demo, static with strong headline, carousel, before/after (where allowed), testimonial, screen recording, founder talk, motion graphic |
| Awareness stage | problem-aware, solution-aware, product-aware, most-aware |
| Persona/use case | different buyers or uses |
| Hook | first 3 seconds or first line, different each |

Starting volume heuristic: 5 to 10 distinct concepts per prospecting campaign, each with 2 to 3 hook variants, then refresh weekly to biweekly based on fatigue signals. Third-party guides suggest anywhere from 5 to 20 depending on budget, so scale concept count to budget (more spend needs more creative supply).

### Specs (verify current)

| Placement | Ratio | Notes |
| --- | --- | --- |
| Reels, Stories | 9:16 (1080x1920) | Keep key content inside safe zones, away from top/bottom UI |
| Feed | 4:5 (1080x1350) or 1:1 | 4:5 uses more screen height |
| Video length | 6 to 30 seconds is common for conversion; test longer for complex products | Captions on, sound-optional |
| Text | Short, benefit-led primary text; first line = hook | Headline <= 40 chars; primary text visible portion is short on mobile |

### Advantage+ Creative enhancements

Recent defaults enable many auto-enhancements for new campaigns. Preview each. Disable text/appearance changes that can alter claims, brand look, or misrepresent price/offer. Keep ones that only adjust format or brightness if they pass your quality check.

### Hook patterns (use real facts only)

See `07`. In short: 1) specific pain, 2) surprising fact with number, 3) result in a timeframe from a real customer, 4) visual demonstration, 5) "I tried X so you do not have to", 6) clear comparison with the usual alternative.

## 5. Conversions API (CAPI) and signal

- Run Pixel + CAPI together, deduplicated (same `event_id`/event name). Send `purchase` with value, currency, order ID; `lead` with value; CRM stages as offline events.
- Pass customer information parameters (hashed email/phone, `fbp`, `fbc`, IP/user agent where lawful) to lift match quality.
- Watch Event Match Quality and dedup in Events Manager weekly.
- Domain verification and event prioritization are largely automated now; confirm in Events Manager what applies to the account.
- Attribution: compare 7-day click vs 1-day click and understand that view-through options have narrowed in recent API versions. Keep settings stable and compare against blended results.

## 6. Lead generation on Meta

| Option | Pros | Cons | Use when |
| --- | --- | --- | --- |
| Instant Form (lead ad) | Lowest friction, volume | Lower intent, spam risk | Fast follow-up exists; use "higher intent" form type and qualifying questions |
| Website lead (conversion) | Higher intent, landing page persuades | Lower volume | Product needs explanation |
| Click-to-WhatsApp / Messenger | Natural in Indonesia, conversational | Needs fast staffed replies | Services, high-consideration retail, COD-heavy ecommerce |

Quality levers: use "conversion leads"-style optimization (optimizing toward leads that become qualified via CRM feedback) when available, add 1 to 2 qualification questions (budget, timeline, need), use a review step, and reply fast. Speed to lead is often the biggest quality lever: respond within minutes, not hours.

### Click-to-WhatsApp playbook

1. Objective: Sales/Leads with messaging destination, or Engagement with WhatsApp where appropriate.
2. Prefilled message that includes the product/ad ref so sales knows context.
3. Greeting and quick replies set in WhatsApp Business app/API; first reply under about 5 minutes during business hours.
4. Track: conversations started, qualified conversations, orders. Send confirmed purchases back via CAPI for business messaging when possible.
5. Compare cost per conversation to cost per **order**. Conversation volume alone proves nothing.

## 7. Scaling on Meta

Order of preference:
1. **Add creative** concepts (the real constraint).
2. **Raise budget** on winning campaigns in steps. Heuristic: 15 to 25% every 2 to 3 days, or larger jumps after a stable week. Large jumps can reset learning, so step instead of doubling overnight.
3. **Duplicate** winning ad set into a new ad set with fresh budget, only if the structure supports it (avoid audience overlap competing with itself).
4. **Broaden** (countries, ages, placements) when a segment saturates.
5. **Lift upstream** (new offers, bundles, higher AOV) so the allowable CPA rises.

Monitor frequency, CPM, CTR trend, CPA, and new-customer share while scaling. Stop and diagnose if CPA climbs two steps in a row.

## 8. Special categories and policy

- Special Ad Categories (credit, employment, housing, social issues/politics): restricted targeting, extra review.
- Health, weight loss, financial products, crypto, alcohol, gambling: stricter rules and claim limits. In Indonesia also respect local regulators (OJK for financial products, BPOM for food/health/cosmetics) and the Indonesian advertising ethics code.
- Do not imply knowledge of personal attributes ("Are you diabetic?", "Struggling with debt?"). Rewrite to speak about the product or topic generally.
- Before/after imagery, miracle claims, and fake urgency are common rejection reasons. Use only truthful claims.
- Landing page must match the ad and comply (policy pages, working links, no deceptive redirects).
- Review a rejected ad's reason and fix; repeated violations risk account restrictions. Keep a backup ad account and verified Business Manager hygiene (two admins, two-factor).

## 9. Research

- Meta Ad Library: study competitor ads (active duration is a weak proxy for performance), landing pages, offers, hooks. Do not copy; extract angles.
- Own data: top-scoring comments, sales chat questions, reviews, support tickets. These are your best hooks.

## 10. Weekly Meta routine

1. Delivery and learning status; budget pacing.
2. Creative leaderboard: spend, hook rate (3-second plays / impressions), hold rate, CTR (link), CPA/ROAS, frequency. Pause losers that had fair spend; keep clear winners as controls.
3. Launch 2 to 4 new concepts weekly or biweekly depending on spend.
4. Check placement, device, and age/geography splits for outliers (act only on stable patterns).
5. CAPI and Event Match Quality health.
6. Comments moderation and policy status.
7. Reconcile with store/CRM: platform conversions vs orders/leads.

## 11. Common failure modes

| Symptom | Likely cause | Fix |
| --- | --- | --- |
| Learning limited everywhere | Too many ad sets, low budget, low-volume event | Consolidate, raise budget, optimize one step higher |
| CPM rising, CTR falling | Creative fatigue or audience saturation | New concepts, broaden audience, check frequency |
| Good CTR, poor conversion | Landing page, price, offer mismatch, wrong audience | Check LP, offer, ad-to-page message match, mobile speed |
| Cheap leads, no sales | Low-intent form, slow response | Add qualification, speed up follow-up, optimize to deeper event |
| Retargeting hero, prospecting zero | Harvesting existing demand | Evaluate blended MER, invest in prospecting creative |
| Sudden CPA spike | Tracking break, promo ended, policy limited, competitor push | Event health, change log, delivery insights, calendar |
