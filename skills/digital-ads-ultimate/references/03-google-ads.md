# 03 Google Ads

Google is the intent engine: people tell you what they want. Win by matching intent, giving the algorithm clean conversion data, and keeping query quality tight.

Currency of facts: AI Max for Search, Performance Max reporting, and Demand Gen features changed repeatedly through 2025 and 2026. Treat product names and feature availability below as "verify in the live account and Google Ads Help".

## 1. Campaign type selection

| Goal | Campaign type | Use when |
| --- | --- | --- |
| Capture high-intent searches | **Search** | Always the first build for anything people search for |
| Ecommerce with a product feed | **Shopping / Performance Max (feed-based)** | Merchant Center is clean; margin data available |
| Cross-channel conversion volume | **Performance Max** | At least ~30 conversions per month of clean data; creative assets and feed available |
| Visual demand creation on YouTube/Discover/Gmail | **Demand Gen** | You have video and image assets and want upper/mid-funnel demand with conversion goals |
| Video reach/consideration | **Video / YouTube** | Brand and consideration, remarketing to viewers |
| App installs | **App campaign** | Needs app events and measurement partner |
| Local store visits | Local/PMax store goals | Only with verified business profile |

Build order for most accounts: Brand Search (small, defensive) -> Non-brand Search on bottom/mid-funnel intent -> Shopping/PMax if ecommerce -> Demand Gen/YouTube for demand creation and remarketing.

## 2. Search campaigns

### Structure

- **Segment by intent and economics**, not by keyword count. Separate: brand, competitor, high-intent non-brand (service + location, "buy", "price"), research-intent non-brand, and generic/exploratory.
- Tight themes: an ad group is one intent cluster with 5 to 20 closely related keywords, one message, one landing page. Avoid thousands of one-keyword groups (legacy "SKAG"), modern matching and bidding reward consolidation with clear themes.
- Keep brand separate so brand's cheap conversions do not hide non-brand performance.

### Keyword research

Sources: customer language (sales calls, WhatsApp chats, reviews), Keyword Planner, search terms report from existing campaigns, competitor sites, autocomplete and "People also ask". Group by funnel stage:

| Stage | Pattern | Example (ID) |
| --- | --- | --- |
| Problem | cara, kenapa, masalah | "cara mengatasi laptop lemot" |
| Solution | jasa, perbandingan, vs, review | "jasa service laptop jakarta" |
| Purchase | harga, biaya, beli, promo, near me, + city | "biaya ganti ssd laptop" |
| Brand | brand, brand + login/review | "[brand] service" |

Intent modifiers that usually signal value: price, cost, buy, quote, near me, city, urgent, same day. Common waste modifiers to start as negatives: free/gratis, jobs/lowongan, salary/gaji, diy, template, pdf, course (if you do not sell it), used/bekas (if relevant), login (if non-brand and you are not a SaaS login target), and competitors' unrelated products.

### Match types in the Smart Bidding era

| Type | Role |
| --- | --- |
| Exact | Highest control for brand, proven winners, expensive terms |
| Phrase | Default workhorse for non-brand intent clusters |
| Broad | Works with Smart Bidding, strong conversion data, and good negatives; use in a separate test campaign with a clear budget cap |

Rule: broad match without conversion tracking and negatives is how budgets get wasted. Broad match with them can find incremental queries. Test it on purpose, compare its CPA to phrase/exact over a full conversion cycle.

**AI Max for Search** (opt-in feature layer on Search: expanded matching beyond keywords, text customization, final URL expansion) can expand reach but changes what the search terms and URL reports mean. If enabled: watch search terms matched via expansion, exclude brand terms and off-topic URL paths, restrict final URL expansion with URL exclusions, and review auto-generated text for claims you cannot support. Test via an experiment, not an account-wide flip.

### Negative keywords

- Weekly: review the search terms report for the last 7 to 14 days. Add irrelevant terms as negatives at the right level (ad group, campaign, or shared list).
- Maintain shared lists: universal negatives, brand-protection negatives, competitor lists.
- Use phrase/exact negatives carefully; a broad negative can block good traffic.

### Responsive Search Ads (RSA)

- Limits: up to 15 headlines (30 characters each), 4 descriptions (90 characters each). Aim for 12 to 15 unique headlines and 4 descriptions.
- Cover distinct angles: keyword/product, benefit, proof, offer, objection, CTA, location. Do not pad with near-duplicates.
- Pin sparingly (brand or legal line in a position). Heavy pinning cripples learning.
- Include the keyword theme in at least 2 headlines and one CTA that states the action ("Ask for a quote today", "See prices").
- Create 2 to 3 RSAs per ad group with different angles, retire the weakest after enough impressions.
- Fill extensions/assets: sitelinks (4+), callouts, structured snippets, price, call, location, image, lead form where relevant. Assets raise CTR and take SERP space.
- Ad strength is a guide, not a goal. Judge by conversions and CPA.

Indonesian example for a local service (placeholders, replace with real facts):

```
H1: Service AC Jakarta Selatan
H2: Teknisi Datang di Hari yang Sama
H3: Biaya Dicek Sebelum Dikerjakan
H4: Garansi Servis [X] Hari
H5: Chat WhatsApp untuk Jadwal
D1: Cuci AC, isi freon, perbaikan bocor. Cek harga di WhatsApp, kerjakan setelah setuju.
D2: Teknisi bersertifikat [bila benar]. Garansi pengerjaan [X] hari. Area: Jaksel dan sekitarnya.
```

### Quality Score and relevance

Expected CTR, ad relevance, landing page experience. Use as a diagnostic: low expected CTR -> rewrite ads and tighten keywords. Low ad relevance -> split ad groups, add keyword to copy. Low landing page experience -> speed, relevance, mobile UX (see `08`).

### Bidding

| Situation | Strategy |
| --- | --- |
| New campaign, little data | Maximize Conversions (no target) or Maximize Clicks with a CPC cap to gather data briefly. Move to a goal strategy once data exists |
| Enough conversion data (heuristic ~30 per 30 days) | Target CPA (leads) or Target ROAS (ecommerce, value tracking in place) |
| Value varies a lot per conversion | Maximize Conversion Value, then add tROAS |
| Brand | Target impression share or low-CPC strategy; protect, do not overpay |

Rules of thumb:
- Set the first tCPA/tROAS **at or near the account's recent actual**, then tighten gradually. A target far stricter than history throttles spend and volume.
- Make bidding changes in modest steps (heuristic: 10 to 20% per change) and wait out the learning window (heuristic: 1 to 2 weeks, or the status in the UI) before the next.
- Avoid stacking budget, bid, creative, and structure edits at once.
- Portfolio strategies only for campaigns with the same economics and enough combined volume.
- Seasonal adjustments and data exclusions exist for known tracking outages and short, sharp promos. Use them rather than manual panic.
- Bid adjustments for device/location/schedule: inputs for Smart Bidding are signals, not hard multipliers, except where the platform supports them as explicit adjustments. Use location and schedule exclusions to cut proven waste.

### Budgets

Budget should let the campaign spend what its target can profitably buy. If "limited by budget" and CPA is below target, raise budget. If CPA is above target, fix efficiency first. Heuristic increments: up to about 20% at a time, wait a few days between steps.

## 3. Performance Max

Powerful, opaque. Run it deliberately.

**Prerequisites**: reliable conversion tracking with real values, enough volume, strong assets, clean feed (ecommerce), brand exclusions plan.

Setup:
- One campaign per distinct goal/economic group (for example by margin tier or product category), not by every SKU.
- **Asset groups** by theme/audience. Provide the full set: multiple images (landscape, square, portrait), logos, videos (vertical and horizontal; if you do not supply video, Google makes one, often weak), 5+ headlines, 5+ descriptions, long headlines, business name.
- **Audience signals** (customer lists, remarketing, custom segments) steer learning, they do not restrict delivery.
- **Search themes** guide query matching.
- **Brand exclusions** and brand lists to stop PMax from harvesting brand demand and inflating ROAS. Use the "new customer acquisition" goal when new customers are the objective.
- **Final URL expansion**: limit with URL exclusions for pages you do not want promoted (careers, login, policies).
- **Reporting**: use the channel/placement, asset, search category, and landing page reports. Recent changes split PMax network reporting into channel-level rows, so any custom report or data connector filtering on the old "cross-network" value needs updating.
- **Feed-only (Shopping-style) PMax** for ecommerce gives more product control; segment by margin or bestseller tiers using custom labels.

Evaluate PMax on incremental value: compare with a holdout (experiment), watch branded vs non-branded share of conversions, and check blended MER.

## 4. Demand Gen (and YouTube)

- Visual placements: YouTube Shorts/in-stream/in-feed, Discover, Gmail. Goal: create and capture mid-funnel demand, not harvest bottom-funnel.
- Provide video in 9:16, 1:1, and 16:9 plus at least ~10 images in varied crops (heuristic from Google/third-party guidance), multiple headlines and descriptions.
- Audiences: customer lists, lookalike-style segments, custom segments from search terms/URLs, YouTube viewers, remarketing.
- Bidding: conversions-focused after the account has volume. Google's own guidance cited by practitioners recommends enough daily budget relative to target CPA (for tCPA a daily budget a multiple of target CPA, commonly cited around 10x) and avoiding heavy edits until about 50 conversions (verify current Help page).
- Run Demand Gen with remarketing exclusions so you can measure new-to-brand reach separately from retargeting.
- Creative testing mirrors Meta/TikTok principles: distinct hooks and formats, first 3 seconds, captions on, sound-optional.

## 5. Shopping and feed hygiene

- Merchant Center: no disapprovals, correct GTIN/brand/MPN where applicable, accurate price and availability, high-quality images, titles with brand + product type + key attributes (size, color, model).
- Use custom labels (margin, bestseller, season, price band) to segment bids/budgets.
- Add negative keywords to Shopping/PMax at campaign level where supported, and use product-level exclusions for low-margin or out-of-stock items.
- Promotions and shipping annotations raise CTR.

## 6. Lead generation on Google

- Search + call/WhatsApp/form conversion. Track **calls from ads** with a minimum duration filter, call asset, and website call conversions.
- Lead form assets only with a plan for fast follow-up and quality feedback via offline import.
- Offline conversion import (GCLID or enhanced conversions for leads) with CRM stages, so bidding learns which leads close. Without this, Google will find cheap, low-quality leads.
- Add form friction on purpose when quality matters (budget/timeline/qualification questions).

## 7. Audiences

- Use audiences in **observation** on Search to learn bid-value insight, in **targeting** for Display/Demand Gen/YouTube.
- Customer Match lists (hashed, consented) for retention and exclusions.
- Exclude existing customers from acquisition campaigns when new customers are the goal.
- Remarketing lists need volume thresholds before serving; build them from day one.

## 8. Weekly Google routine

1. Spend and pacing vs budget; conversion tracking status.
2. Search terms: add negatives, promote winners to exact/phrase.
3. Impression share lost to budget vs rank for money campaigns.
4. CPA/ROAS by campaign vs target; marginal CPA after recent changes.
5. Ad asset performance: replace "low" assets with new angles.
6. Landing page and Quality Score diagnostics.
7. Experiments status (broad vs phrase, tROAS levels, PMax holdout).
8. Policy and disapprovals.

## 9. Frequent failure modes

| Symptom | Likely causes | First checks |
| --- | --- | --- |
| Clicks but no conversions | Tracking broken, wrong keyword intent, weak landing page | Conversion status, search terms, LP load and mobile UX |
| High CPC | Competitive auction, low QS, broad intent terms | QS parts, match types, geo/device mix |
| Spend but junk leads | Optimizing on low-value event, broad match, no negatives | Offline import, form questions, search terms |
| PMax ROAS looks great, sales flat | Brand cannibalization, retargeting-heavy | Brand exclusions, channel report, holdout |
| tCPA campaign stopped spending | Target too strict, little data | Target vs actual, learning status, relax target |
| Sudden drop in conversions | Tag broken, site release, budget cap, disapproval | Conversion status, change history, policy center |

Use the change history to correlate drops with edits.
