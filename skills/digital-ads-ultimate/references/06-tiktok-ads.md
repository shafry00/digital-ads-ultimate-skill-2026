# 06 TikTok Ads

TikTok is a creative-first discovery platform. People are in a lean-back, entertainment mindset, so ads that look and sound native win. Creative supply and iteration speed decide results.

Currency of facts: Smart+ and GMV Max have been rolled out and iterated through 2025 and 2026. Many numeric thresholds below come from practitioner guides, not TikTok documentation. Verify current limits in TikTok Ads Manager and the TikTok Business Help Center.

## 1. Objectives and campaign types

| Goal | Objective | Notes |
| --- | --- | --- |
| Sales/leads on a website | Sales/Conversions (web) | Needs Pixel + Events API; Smart+ or manual |
| Shop sales (TikTok Shop sellers) | Product sales / **GMV Max** | Default and primary ad type for Shop sales objective (since 2025 per guides), runs across Shop surfaces |
| Lead capture in app | Lead generation (Instant Form) | Qualify and follow up fast |
| Traffic | Traffic | Optimize to landing page views, not clicks |
| Reach / video views | Reach, Video views | Awareness, used with measurement of lift or branded search |
| App | App promotion | Needs MMP events |

**Smart+ campaigns** automate budget, targeting, and creative combination using the assets you provide. **Manual campaigns** give control over audiences and individual ads, useful for testing hooks and diagnosing. Practitioner guidance: use manual structures to find winning creative, then scale in Smart+ once the pixel has stable conversion volume (a commonly cited threshold is about 50 conversion events per week, unconfirmed).

## 2. Structure

```
Campaign 1: Creative testing (manual)   1 ad group broad, 3 to 6 new videos each with a different hook
Campaign 2: Scale (Smart+ or manual)    proven creatives, broad targeting, higher budget
Campaign 3: Retargeting                  site visitors, add to cart, video viewers, customer lists (exclude purchasers)
```

- Keep audiences **broad** by default (country, age band, language). Interest/behavior targeting adds little under delivery automation. Use custom/lookalike audiences for retargeting and suggestions.
- Budget math: ad group daily budget >= about 7 x target CPA to give ~50 events a week (see `01`). Platform floors apply, check them in Ads Manager for your country.
- Placement: TikTok feed first. Pangle/other placements can dilute quality, test deliberately.
- Naming: `TEST | Sales | Broad | H1-pain | 2026-10`.

## 3. Creative system (the whole game)

### Format

- Vertical 9:16 (1080x1920), safe zone away from bottom caption and right-side buttons.
- Length: many conversion videos run roughly 9 to 30 seconds, commonly shorter is better when the idea is simple (heuristic). Longer works for demos and storytelling if retention holds.
- Native look: shot on phone, real person talking to camera, on-screen text and captions, trending but fitting audio where licensed (use Commercial Music Library for ads).
- Sound-on matters on TikTok more than on other platforms. Still add captions.

### Structure: Hook -> Body -> CTA

| Part | Time | Job |
| --- | --- | --- |
| Hook | 0 to 3 s (up to 8 s for some formats) | Stop the scroll: pain, curiosity gap, shock stat, pattern break, relatable moment, demonstration |
| Body | 3 to ~20 s | Show 2 to 4 selling points through scenes and demonstration, not narration alone; proof; before/after only where policy permits |
| CTA | last 3 to 5 s | State the exact next step (visit, tap, order via cart, chat) and one reason to do it now |

Hook types: relatable pain ("Nobody warned me about...") / curiosity ("I did not expect this to work...") / shock stat with real number / personal story / myth-bust / comparison / "wait for it" payoff. Hook rate (3-second views / impressions) is your hook scorecard.

### Video types by business

| Business | Strong formats |
| --- | --- |
| Commerce | Product demo, scenario/skit, before-after of use, unboxing, reviewer or creator POV, comment-reply video |
| Education/info product | Teacher POV, quick tip series, student results (real), Q&A |
| Local service | Behind the scenes, process, owner talking, customer story (consented), price transparency |
| Finance/health (regulated) | Educational narrative with disclaimers, strict claim limits, no income or health promises |
| B2B | Founder talks, myth vs fact, customer pain skit |

### Selling points

Select 2 to 6 sellpoints grouped as scenario, audience, feature, benefit, proof of effect, user experience, discount/service. Test which sellpoint leads the hook. Each new concept leads with a different sellpoint.

### Creative volume and fatigue

- Plan a weekly cadence of new concepts, 3 to 6 new videos in testing per week at modest budgets, more as spend grows. One guide suggests starting TikTok Shop with 50 or more creator videos live before turning on ads (a Shop-scale heuristic).
- TikTok creative fatigue is fast. Watch hook rate, CTR, CPA, and frequency. Use the platform's creative fatigue tooling in Ads Manager where available. Heuristic refresh window for scaled ads: every 1 to 3 weeks.
- Never edit a live ad's video in place. Create new ads, keep the winner as control.
- Use **Spark Ads** (boost an organic post from your account or a creator) to retain social proof and comments. Request authorization codes with long enough validity (options exist from days to a year, verify) and track expiry dates because expired authorization stops delivery.
- Creators/UGC: brief with required hook, product points, do-not-say list (claims policy), usage rights and whitelisting terms. Pay for raw files if you want to cut variants.

### AI helpers

TikTok's creative tools (for example Symphony for resizing, scripts, avatars, translation) speed up variants. They do not replace a good concept or compliance review. Disclose AI-generated content where policy requires it.

## 4. Tracking

- Pixel plus **Events API** with shared `event_id` for dedup. Standard events: ViewContent, AddToCart, InitiateCheckout, CompletePayment (purchase), SubmitForm/Lead. Include value and currency.
- Verify in Events Manager diagnostics: match rate and event volume.
- UTM tags and platform macros in URLs. TikTok in-app browser: test forms and checkout there.
- For lead gen, send CRM stages as offline events.
- For TikTok Shop, performance lives in Shop analytics. Reconcile ads data with Shop orders.

## 5. TikTok Shop and GMV Max

- Needs a connected, healthy Shop (product feed approved, competitive price, stock, ratings, shipping and fulfillment ok).
- GMV Max optimizes for gross merchandise value using a budget and a target ROI (target ROAS), distributing across ads, live, and product cards. Budget and ROI inputs behave as targets, not guarantees: a high ROI target throttles spend.
- Practical setup: separate campaigns by product or category so budgets and ROI targets can differ, feed it many creator/product videos, boost proven organic videos as Spark Ads, and watch Shop-level profit (not only ROI).
- Expect surges around campaign days (mega sales days). Plan inventory, discounts, and budgets ahead.
- Follow Indonesian marketplace rules (product listings, BPOM for food/cosmetics, halal and labeling where relevant).

## 6. Lead generation

- Instant Form for speed, landing page for quality. Add 1 to 2 qualifying questions. Reply quickly via WhatsApp/phone.
- Creative should preview the offer honestly. Do not bait with prizes and then ask for sensitive data.
- Optimize to the deepest feasible event, and send offline outcomes back.

## 7. Policy and brand safety

- Strict on misleading claims, before/after in health/weight, financial promises, fake urgency/countdowns, and unverifiable endorsements.
- Disclose paid partnerships and branded content with the proper toggles.
- Use inventory filters (expanded, standard, limited) to match brand risk tolerance. Moderate comments and use blocked words lists.
- Check restricted categories and country rules before building (alcohol, gambling, financial services, health products, politics).

## 8. Scaling

1. Confirm a stable winner: 3 to 5+ days of conversions near target, not a single lucky day.
2. Add budget in steps (heuristic 20 to 30% every 2 to 3 days) or duplicate a winning ad group at a higher budget.
3. Keep feeding new concepts. TikTok scale dies from creative fatigue, not audience exhaustion.
4. Move winners into Smart+ (when you have signal) and keep a manual test lane.
5. Add Spark Ads of best organic and creator posts.
6. Expand geography or languages with localized creative (real native speakers).

## 9. Weekly TikTok routine

1. Delivery, learning status, budget pacing.
2. Creative scoreboard: hook rate, hold rate (e.g., 6s views / impressions or average watch time), CTR, CVR, CPA/ROAS, frequency.
3. Kill clear losers; scale winners; log hooks tested and outcomes.
4. Brief and shoot next week's concepts from comments, search, and winners.
5. Events API health, landing page speed in-app.
6. Comments moderation, policy status, Spark authorization expiry.
7. Reconcile to source of truth (store orders, CRM).

## 10. Failure modes

| Symptom | Likely cause | Fix |
| --- | --- | --- |
| Low hook rate | First seconds weak, not native | New hooks, show payoff/problem within 1 to 2 s, pattern break |
| Good CTR, no conversions | Page or in-app browser issue, offer mismatch | Test page on TikTok browser, shorten flow, align message |
| Learning limited | Budget too low for event volume | Fewer ad groups, higher budget, higher funnel event |
| Fast decay after a good week | Creative fatigue | New concepts, rotate controls, expand audience |
| GMV Max low spend | ROI target too high, shop quality low | Lower target step by step, fix shop and listings |
| Spark ad stopped | Authorization expired or post removed | Renew code, keep a backup creative |
