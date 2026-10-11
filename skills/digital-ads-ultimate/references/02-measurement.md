# 02 Measurement and Tracking

Ad platforms optimize toward the signal you send. Bad signal, bad optimization. This file is the gate before spend.

## 1. Define conversions

1. **Primary conversion** = the business outcome the platform should optimize toward (purchase, qualified lead, booked call).
2. **Secondary/supporting** = diagnostic events (view content, add to cart, form start, WhatsApp click). Report them, do not let them drive bidding unless volume forces a proxy.
3. **Value**: send real value (order value, or expected value per lead stage) so value-based bidding works. Use the same currency everywhere.
4. **Deduplicate**: one real-world conversion = one counted conversion per platform.

### Lead-quality ladder (for lead gen)

```
Lead submitted -> Marketing-qualified -> Sales-accepted -> Opportunity -> Won
```

Send later stages back to the platform as offline conversions (Google offline conversion import, Meta Conversions API for CRM, LinkedIn Conversions API, TikTok Events API/offline events). Optimize to the deepest stage that gets enough volume (heuristic: at least ~30 to 50 per month per campaign). Until then, optimize to lead and use qualification questions plus negative audiences to hold quality.

Assign provisional values by stage if the CRM has no revenue yet, for example value = close rate at that stage x average deal contribution.

## 2. Tracking architecture

| Layer | Purpose | Notes |
| --- | --- | --- |
| Browser tags/pixels | Fast events, remarketing audiences | Google tag/GTM, Meta Pixel, TikTok Pixel, LinkedIn Insight Tag |
| Server-side / conversion APIs | Recover signal lost to ad blockers, ITP, cookie limits; send CRM outcomes | Meta Conversions API, TikTok Events API, LinkedIn Conversions API, Google enhanced conversions + offline import |
| Analytics | Cross-channel sanity | GA4 (events, funnels, UTM-based channel view) |
| Source of truth | What actually got paid | Store/CRM/payment data |

Rule: **browser + server together, deduplicated** with a shared event ID (Meta `event_id`, TikTok `event_id`). Server-only without dedup double counts.

### Event naming and parameters (minimum viable set)

Ecommerce: `view_content`, `add_to_cart`, `initiate_checkout`, `purchase` (value, currency, transaction_id, items). Lead gen: `lead` (value, form_id), `qualified_lead`, `booked_call`, `closed_won`. Messaging: `whatsapp_click` (and, when possible, a confirmed conversation or order). Send hashed email/phone where policy and consent allow it, to raise match quality.

## 3. UTM convention

Use one scheme everywhere, lowercase, no spaces.

```
utm_source   = google | meta | tiktok | linkedin
utm_medium   = cpc | paid_social
utm_campaign = {objective}_{audience-or-theme}_{yyyymm}
utm_content  = {creative-id}_{hook}
utm_term     = {keyword}  (search only)
```

Use platform ValueTrack/dynamic macros where available (for example Google `{campaignid}`, Meta `{{campaign.id}}`, TikTok `__CAMPAIGN_ID__`) so reports join back to platform IDs. Keep a creative ID in `utm_content` to analyze creative performance in GA4 and the CRM.

## 4. Consent and privacy

- Honor consent. In regions that require it (EEA/UK) use Google Consent Mode v2 and consent-gated pixels. For Indonesian audiences, Law No. 27 of 2022 (UU PDP) requires a lawful basis and transparency for personal data processing: have a privacy policy, a clear notice at collection, and a process for data requests. Treat this as a prompt to confirm with the user's legal counsel, not as legal advice.
- Do not upload customer lists without lawful basis and the right to share them with the platform. Hash PII per platform specs.
- Sensitive categories (health, finance, children, protected traits) restrict targeting and events on several platforms. Check policies before building audiences from sensitive pages.

## 5. Platform signal quality

| Platform | Key signals to check | Where |
| --- | --- | --- |
| Google | Conversion status "Recording", enhanced conversions diagnostics, primary vs secondary actions, offline import match rate | Goals > Conversions, Diagnostics |
| Meta | Event Match Quality, deduplication rate, event coverage, "Learning limited" | Events Manager, Ads Manager |
| TikTok | Events API match rate, event diagnostics, learning status | Events Manager |
| LinkedIn | Insight Tag status, Conversions API match, conversion attribution windows | Campaign Manager > Analyze > Conversions |

Heuristic targets (verify against the live account): Meta Event Match Quality in the good range for purchase/lead events, both pixel and server events present, dedup working. Platform dashboards label quality bands; aim for the top band your data allows.

## 6. Attribution reality

Platforms over-claim: each takes credit for conversions it touched, windows differ, and view-through is included on some. Therefore:

- **Platform ROAS/CPA** = directional, for in-platform decisions.
- **MER / blended CAC** (total revenue or customers / total spend) = business truth, use for budget level decisions.
- **GA4 / CRM** = tie-breakers and channel overlap checks.
- **Incrementality** = the real test: geo holdout, conversion lift study (Meta, Google, TikTok, LinkedIn offer variants), or pausing a channel for a window and watching blended results. Plan one when spend is large enough that a wrong call is costly.

Keep attribution settings consistent when comparing periods. Platforms change defaults and windows over time (for example, Meta has narrowed view-through reporting options in recent API versions), so annotate changes in the report and re-baseline.

Lag: record typical click-to-conversion lag per platform and product. Do not judge a campaign inside its lag window. B2B and high-ticket lag can be weeks.

## 7. QA protocol (must pass before launch)

1. Test each event end to end on a real device: trigger it, see it in the platform's test/diagnostics tool, see it in GA4/debug.
2. Confirm value, currency, and ID parameters populate and are numeric.
3. Confirm dedup (browser and server event share one ID, count stays 1).
4. Confirm the thank-you page or event does not fire on refresh or for non-completions.
5. Confirm UTMs survive redirects and appear in analytics and the CRM.
6. Confirm form and checkout work on mobile, slow network, and in-app browsers (Instagram, TikTok, LinkedIn in-app browsers behave differently).
7. Confirm WhatsApp/phone click events fire and map to a way to count real conversations or orders.
8. Place a real test order or lead, then match it across platform, analytics, and the source system.
9. Record the tracking spec in the blueprint with owner and date.

## 8. Weekly measurement hygiene

- Compare platform-reported conversions vs source-of-truth conversions. Investigate drift beyond what attribution differences explain (a heuristic starting trigger is a gap that changes the conclusion, not a fixed percentage).
- Check event volume for sudden drops (broken tag after a site release).
- Check match quality and consent rates.
- Annotate site changes, promo calendar, outages, and platform changes in the report.
