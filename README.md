# Digital Ads Ultimate Skill 2026

One agent skill for **Google Ads, Meta Ads, LinkedIn Ads, TikTok Ads, and marketplace ads (Shopee, Tokopedia, TikTok Shop)**. It covers the whole job: strategy and unit economics, tracking, campaign build, creative and copy, launch, optimization, scaling, audits, and reports with ranked recommendations.

It judges ads by **profit, not ROAS alone**: ROAS, break-even ROAS, **POAS**, **MER**, and **TACoS** side by side.

Works with Claude Code and any agent that reads `SKILL.md` skills.

[Bahasa Indonesia](#bahasa-indonesia) | [English](#english)

---

## English

### What you get

| Stage | What the skill does |
| --- | --- |
| Strategy | Break-even CPA/ROAS, platform fit, budget sizing, funnel and objective map |
| Tracking | Conversion design, Pixel + server events with dedup, consent, UTMs, QA protocol |
| Build | Structure and naming per platform, keyword and audience plans, creative matrix, copy specs |
| Launch | Paused-first build, safety gate for live accounts, launch checklist |
| Optimize | Layered diagnosis (delivery, cost, attention, landing, conversion, value, measurement), decision rules, fatigue detection |
| Scale | Step sizes, marginal CPA checks, creative supply plans |
| Marketplace | Fee stack, break-even ROAS, POAS, MER, TACoS, product triage, campaign-day plan, sheet analysis |
| Audit | Scored checklists per platform with evidence rules |
| Report | Weekly and monthly templates, recommendations ranked by impact, confidence, effort |
| Math | `ads_math.py` (break-even, funnel, sample size, A/B test) and `marketplace_analyzer.py` (CSV to POAS/MER/TACoS verdicts) |

### Install

```bash
git clone https://github.com/shafry00/digital-ads-ultimate-skill-2026.git
cp -r digital-ads-ultimate-skill-2026/skills/digital-ads-ultimate ~/.claude/skills/
```

Restart the session. Replace everything in `[BRACKETS]` in the prompts below.

### Metrics cheat sheet

| Metric | Formula | Use it for |
| --- | --- | --- |
| ROAS | ad sales / ad spend | Ad efficiency inside one platform |
| Break-even ROAS | 1 / contribution margin % | The ROAS floor before ads lose money |
| POAS | contribution before ads from ad sales / ad spend | Profit per rupiah of ads. Break-even is 1.0 |
| MER | total revenue / total marketing spend | Is the whole engine efficient |
| TACoS | ad spend / total store sales | How dependent the store is on ads |

POAS = ROAS x contribution margin %. A product with ROAS 5.0 and 15% margin has POAS 0.75: it loses money.

### Copy-paste prompts (English)

**1. Marketplace: analyze my ads sheet (the main one)**

Attach a CSV or paste a table. Columns are listed in [Sheet format](#sheet-format).

```
Use the digital-ads-ultimate skill. I sell [PRODUCT CATEGORY] under the brand [BRAND] on [Shopee / Tokopedia / TikTok Shop].
Here is my ads data for [DATE RANGE]: [ATTACH CSV OR PASTE TABLE].
Store total sales in the same period: Rp [TOTAL SALES]. Overhead per month: Rp [OVERHEAD, or "unknown"].
Analyze ROAS, break-even ROAS, POAS, MER, and TACoS per product and for the whole store.
Tell me which products to scale, hold, fix, or cut, and why. Give a ranked recommendation list with evidence, expected impact, confidence, and how to verify. List every assumption you made for missing cost data.
```

**2. Marketplace: quick check with no sheet**

```
Use the digital-ads-ultimate skill. Product: [PRODUCT] from brand [BRAND] on [PLATFORM].
Selling price Rp [PRICE]. COGS Rp [COGS]. Commission/admin fee [X]%. Order processing fee Rp [X]. Seller voucher [X]%. Shipping subsidy Rp [X]. Affiliate commission [X]%. Return rate [X]%.
My dashboard shows ROAS [X] on ad spend Rp [SPEND] over [DAYS] days.
Calculate break-even ROAS and POAS. Am I making or losing money? What target ROAS should I set in my ads?
```

**3. Marketplace: set up ads for a product or launch**

```
Use the digital-ads-ultimate skill. Plan marketplace ads for [PRODUCT] (price Rp [PRICE], margin [X]%) on [PLATFORM]. Monthly ad budget Rp [BUDGET]. Goal: [sales / launch / clear stock]. Current rating [X], reviews [X], stock [X] units.
Check listing readiness first, set a ROAS target from break-even, propose campaign structure, a creative and creator plan, and a 14 day operating calendar with scale and stop rules.
```

**4. Marketplace: campaign day (9.9, 11.11, 12.12, Harbolnas)**

```
Use the digital-ads-ultimate skill. Plan my [EVENT] on [PLATFORM] for brand [BRAND]. Products: [LIST WITH PRICE AND MARGIN]. Budget Rp [BUDGET]. Stock: [LIST].
Set a POAS floor, voucher depth per product, budget split, and a day-by-day checklist for before, during, and after.
```

**5. Strategy from scratch (any platform)**

```
Use the digital-ads-ultimate skill. Business: [BUSINESS] by brand [BRAND], selling [PRODUCT/SERVICE] at Rp [PRICE] with gross margin [X]%. Audience: [WHO, WHERE]. Goal: [sales / leads / bookings]. Budget: Rp [AMOUNT] per month. Existing assets: [WEBSITE, PIXEL, CRM, WHATSAPP, CREATIVE].
Do the break-even math, choose platforms (Google, Meta, TikTok, LinkedIn, marketplaces), split the budget, and give me a campaign blueprint with a tracking spec and the first 14 days.
```

**6. Audit an account**

```
Use the digital-ads-ultimate skill. Audit my [GOOGLE / META / LINKEDIN / TIKTOK] ads account for [BRAND]. Data attached: [EXPORT, SCREENSHOTS, OR PASTED TABLE] for the last [30/90] days. Target CPA is Rp [X] (or "unknown").
Score it with the audit checklist, list the top 5 issues, and give a 30/60/90 day fix plan. Mark anything you could not verify as unknown.
```

**7. Diagnose a drop**

```
Use the digital-ads-ultimate skill. On [PLATFORM], CPA for [CAMPAIGN] went from Rp [A] to Rp [B] between [DATE] and [DATE]. Changes I made: [LIST OR NONE]. Data: [PASTE TABLE].
Diagnose layer by layer (delivery, cost, attention, landing, conversion, value, measurement) and give ranked fixes.
```

**8. Write ad copy and creative briefs**

```
Use the digital-ads-ultimate skill. Write [PLATFORM] ads for [PRODUCT] by [BRAND]. Audience: [WHO]. Main pain: [PAIN]. Offer: [OFFER]. Real proof I can use: [REVIEWS, NUMBERS]. Tone: [CASUAL / PROFESSIONAL].
Give 5 concept angles, 3 hooks each, platform-ready copy within character limits, and a creative brief per concept. Do not invent claims or testimonials.
```

**9. Scale decision**

```
Use the digital-ads-ultimate skill. Campaign [NAME] on [PLATFORM] has spent Rp [SPEND] over [DAYS] days with [CONVERSIONS] conversions, CPA Rp [CPA], ROAS [ROAS], target CPA Rp [TARGET]. Daily budget Rp [BUDGET]. Data: [PASTE].
Is the data readable? Should I scale, hold, or fix? Give exact budget steps and stop conditions.
```

**10. Weekly report**

```
Use the digital-ads-ultimate skill. Write my weekly ads report for [BRAND]. This week: [PASTE TABLE]. Last week: [PASTE TABLE]. Targets: [CPA/ROAS/POAS TARGETS].
Include a scorecard, what worked, what did not, layered diagnosis, ranked recommendations, tests to run next week.
```

### Sheet format

One row per product, campaign, or day. Plain numbers (no "Rp", no thousand separators), percentages as fractions (0.08 = 8%).

| Column | Required | Meaning |
| --- | --- | --- |
| `platform` | no | shopee, tokopedia, tiktokshop |
| `campaign` | no | campaign or product name |
| `ad_spend` | **yes** | ad cost in the period |
| `ad_sales` | **yes** | sales attributed to ads |
| `orders`, `units` | recommended | ad-attributed orders and units |
| `cogs_per_unit` or `cogs_pct` | recommended | landed product cost |
| `fee_pct` | recommended | commission/admin fee |
| `fixed_fee_per_order` | recommended | order-processing and similar fixed fees |
| `voucher_pct` | optional | seller-funded voucher share |
| `shipping_subsidy_per_order` | optional | shipping cost you carry |
| `affiliate_pct` | optional | creator/affiliate commission |
| `return_pct` | optional | return and cancel provision |

Missing cost columns count as zero, so results look better than reality. The skill will say so.

Run it yourself, no agent needed:

```bash
python3 skills/digital-ads-ultimate/scripts/marketplace_analyzer.py examples/marketplace_ads_sample.csv --total-sales 120000000 --target-poas 1.3
```

The sample file is fictional. In it, "Kaos Polos 3 Pack" shows ROAS 5.00 but POAS 0.25 and is marked CUT.

### Practice workbook (Excel)

`examples/Digital_Ads_Practice_Workbook_2026.xlsx` is a full hands-on file with fictional data (brand "Nusa Apparel"). One sheet per platform, live formulas, color-coded inputs, and a verdict per row.

| Sheet | What you practice |
| --- | --- |
| Panduan | How to use, color code, metric definitions |
| Asumsi | Unit economics, break-even ROAS, target POAS, thresholds (edit the yellow cells) |
| Google Ads | 6 campaigns incl. brand vs PMax brand share, plus a search-terms table for negative keywords |
| Meta Ads | 7 ads: fatigue, strong hook but weak landing, low data |
| TikTok Ads | 7 creatives: hook rate, hold rate, CTR drop, Spark |
| LinkedIn Ads | B2B down to SQL and Won deals: cheap leads that never become SQL |
| Marketplace | Shopee, Tokopedia, TikTok Shop: ROAS vs POAS, fee stack, TACoS per platform |
| Mingguan | 8 weeks of MER, break-even MER, platform claims vs real revenue, CAC |
| Dashboard | Cross-platform summary, worst rows, charts |
| Latihan | 13 tasks with live answer keys and copy-paste prompts |

Replace the blue cells with your own exports, set the yellow assumptions, then attach the file to your agent. Prompts are in the Latihan sheet (Indonesian) and in the sections above.

### Layout

```
skills/digital-ads-ultimate/
  SKILL.md                     orchestrator: rules, safety gate, workflow, routing
  references/
    01-strategy-and-math.md    05-linkedin-ads.md        09-optimize-and-diagnose.md
    02-measurement.md          06-tiktok-ads.md          10-audit-checklists.md
    03-google-ads.md           07-creative-and-copy.md   11-testing-reports-templates.md
    04-meta-ads.md             08-landing-and-funnel.md  12-marketplace-ads.md
  scripts/ads_math.py
  scripts/marketplace_analyzer.py
examples/marketplace_ads_sample.csv
examples/Digital_Ads_Practice_Workbook_2026.xlsx
```

### Principles and honest limits

1. Numbers before tactics. Tracking before spend. Profit before ROAS.
2. Evidence over opinion: every diagnosis cites a metric and a comparison.
3. Heuristics are labeled. Platform fees, ad products, and attribution rules change often (Shopee changed GMV Max attribution and fee tiers in 2026; Tokopedia and TikTok Shop tooling has been in transition). Read the current fee page in your Seller Center and give the skill the real numbers.
4. 2026 platform features come largely from practitioner sources, not official docs, and are marked for verification.
5. No promised results, no invented proof. Live accounts change only after explicit approval, and campaigns are built paused.
6. Legal and regulatory notes (including Indonesian rules) are prompts to check with counsel, not legal advice.

---

## Bahasa Indonesia

### Isinya

Satu skill untuk **Google Ads, Meta Ads, LinkedIn Ads, TikTok Ads, dan iklan marketplace (Shopee, Tokopedia, TikTok Shop)**, dari nol sampai optimasi: hitung break-even, tracking, struktur campaign, brief kreatif dan copy, launch, diagnosis, scale, audit berskor, dan laporan dengan rekomendasi berurutan.

Penilaiannya pakai **profit, bukan cuma ROAS**: ROAS, break-even ROAS, **POAS**, **MER**, dan **TACoS** dilihat bersamaan.

### Pasang

```bash
git clone https://github.com/shafry00/digital-ads-ultimate-skill-2026.git
cp -r digital-ads-ultimate-skill-2026/skills/digital-ads-ultimate ~/.claude/skills/
```

Restart sesi. Ganti semua yang ada di `[KURUNG SIKU]` pada prompt di bawah.

### Cheat sheet metrik

| Metrik | Rumus | Fungsi |
| --- | --- | --- |
| ROAS | omzet dari iklan / biaya iklan | Efisiensi iklan di satu platform |
| Break-even ROAS | 1 / margin kontribusi | Batas bawah ROAS sebelum iklan rugi |
| POAS | kontribusi sebelum iklan dari omzet iklan / biaya iklan | Untung per rupiah iklan. Impas di 1,0 |
| MER | total omzet / total biaya marketing | Apakah seluruh mesin marketing efisien |
| TACoS | biaya iklan / total omzet toko | Seberapa bergantung toko pada iklan |

POAS = ROAS x margin kontribusi. Produk dengan ROAS 5,0 dan margin 15% punya POAS 0,75, artinya rugi walau ROAS kelihatan bagus.

### Prompt siap copy-paste (Bahasa Indonesia)

**1. Marketplace: analisis sheet data iklan (yang utama)**

Lampirkan CSV atau tempel tabel. Kolomnya ada di [Format sheet](#format-sheet).

```
Pakai skill digital-ads-ultimate. Saya jualan [KATEGORI PRODUK] dengan brand [BRAND] di [Shopee / Tokopedia / TikTok Shop].
Ini data iklan saya periode [TANGGAL AWAL] sampai [TANGGAL AKHIR]: [LAMPIRKAN CSV ATAU TEMPEL TABEL].
Total omzet toko di periode yang sama: Rp [TOTAL OMZET]. Biaya operasional per bulan: Rp [BIAYA OPERASIONAL, atau "belum tahu"].
Analisis ROAS, break-even ROAS, POAS, MER, dan TACoS per produk dan untuk seluruh toko.
Kasih tahu produk mana yang harus di-scale, ditahan, diperbaiki, atau dihentikan, lengkap dengan alasannya. Beri daftar rekomendasi berurutan dengan bukti, perkiraan dampak, tingkat keyakinan, dan cara verifikasinya. Sebutkan semua asumsi untuk data biaya yang kosong.
```

**2. Marketplace: cek cepat tanpa sheet**

```
Pakai skill digital-ads-ultimate. Produk: [PRODUK] dari brand [BRAND] di [PLATFORM].
Harga jual Rp [HARGA]. HPP Rp [HPP]. Biaya komisi/admin [X]%. Biaya proses pesanan Rp [X]. Voucher toko [X]%. Subsidi ongkir Rp [X]. Komisi affiliate [X]%. Rasio retur [X]%.
Dashboard iklan saya menunjukkan ROAS [X] dengan biaya iklan Rp [BIAYA] selama [JUMLAH] hari.
Hitung break-even ROAS dan POAS. Saya untung atau rugi? Target ROAS berapa yang sebaiknya saya pasang di iklan?
```

**3. Marketplace: pasang iklan untuk produk atau launching**

```
Pakai skill digital-ads-ultimate. Rencanakan iklan marketplace untuk [PRODUK] (harga Rp [HARGA], margin [X]%) di [PLATFORM]. Budget iklan per bulan Rp [BUDGET]. Tujuan: [penjualan / launching / habiskan stok]. Rating saat ini [X], jumlah ulasan [X], stok [X] unit.
Cek kesiapan listing dulu, tentukan target ROAS dari break-even, usulkan struktur campaign, rencana kreatif dan kreator, plus kalender operasional 14 hari lengkap dengan aturan scale dan stop.
```

**4. Marketplace: tanggal kembar dan event (9.9, 11.11, 12.12, Harbolnas)**

```
Pakai skill digital-ads-ultimate. Susun rencana [EVENT] saya di [PLATFORM] untuk brand [BRAND]. Produk: [DAFTAR DENGAN HARGA DAN MARGIN]. Budget Rp [BUDGET]. Stok: [DAFTAR].
Tentukan batas bawah POAS, kedalaman voucher per produk, pembagian budget, dan checklist harian untuk sebelum, saat, dan sesudah event.
```

**5. Strategi dari nol (semua platform)**

```
Pakai skill digital-ads-ultimate. Bisnis: [BISNIS] dengan brand [BRAND], menjual [PRODUK/JASA] seharga Rp [HARGA], margin kotor [X]%. Target pasar: [SIAPA, DI MANA]. Tujuan: [penjualan / leads / booking]. Budget: Rp [JUMLAH] per bulan. Aset yang sudah ada: [WEBSITE, PIXEL, CRM, WHATSAPP, KREATIF].
Hitung break-even, pilih platform (Google, Meta, TikTok, LinkedIn, marketplace), bagi budget, dan buatkan blueprint campaign lengkap dengan spesifikasi tracking dan rencana 14 hari pertama.
```

**6. Audit akun**

```
Pakai skill digital-ads-ultimate. Audit akun iklan [GOOGLE / META / LINKEDIN / TIKTOK] milik [BRAND]. Data terlampir: [EXPORT, SCREENSHOT, ATAU TABEL] untuk [30/90] hari terakhir. Target CPA Rp [X] (atau "belum tahu").
Beri skor dengan checklist audit, sebutkan 5 masalah utama, dan rencana perbaikan 30/60/90 hari. Tandai "unknown" untuk hal yang tidak bisa diverifikasi.
```

**7. Diagnosis performa turun**

```
Pakai skill digital-ads-ultimate. Di [PLATFORM], CPA campaign [NAMA CAMPAIGN] naik dari Rp [A] ke Rp [B] antara [TANGGAL] dan [TANGGAL]. Perubahan yang saya lakukan: [DAFTAR ATAU TIDAK ADA]. Data: [TEMPEL TABEL].
Diagnosis per lapisan (delivery, biaya, perhatian, landing, konversi, nilai, pengukuran) dan beri perbaikan yang diurutkan prioritasnya.
```

**8. Tulis copy iklan dan brief kreatif**

```
Pakai skill digital-ads-ultimate. Tulis iklan [PLATFORM] untuk [PRODUK] dari [BRAND]. Audiens: [SIAPA]. Masalah utama mereka: [MASALAH]. Penawaran: [PENAWARAN]. Bukti asli yang boleh dipakai: [ULASAN, ANGKA]. Gaya bahasa: [SANTAI / PROFESIONAL].
Beri 5 angle konsep, 3 hook per konsep, copy siap pakai sesuai batas karakter platform, dan brief kreatif per konsep. Jangan mengarang klaim atau testimoni.
```

**9. Keputusan scale**

```
Pakai skill digital-ads-ultimate. Campaign [NAMA] di [PLATFORM] sudah menghabiskan Rp [SPEND] selama [JUMLAH] hari dengan [JUMLAH KONVERSI] konversi, CPA Rp [CPA], ROAS [ROAS], target CPA Rp [TARGET]. Budget harian Rp [BUDGET]. Data: [TEMPEL].
Apakah datanya sudah layak dibaca? Sebaiknya scale, tahan, atau perbaiki? Beri langkah kenaikan budget yang tepat dan syarat berhenti.
```

**10. Laporan mingguan**

```
Pakai skill digital-ads-ultimate. Tulis laporan iklan mingguan untuk [BRAND]. Minggu ini: [TEMPEL TABEL]. Minggu lalu: [TEMPEL TABEL]. Target: [TARGET CPA/ROAS/POAS].
Sertakan scorecard, yang berhasil, yang gagal, diagnosis per lapisan, rekomendasi berurutan, dan tes untuk minggu depan.
```

### Format sheet

Satu baris per produk, campaign, atau hari. Angka polos (tanpa "Rp", tanpa pemisah ribuan), persen ditulis pecahan (0,08 ditulis 0.08 untuk 8%).

| Kolom | Wajib | Arti |
| --- | --- | --- |
| `platform` | tidak | shopee, tokopedia, tiktokshop |
| `campaign` | tidak | nama campaign atau produk |
| `ad_spend` | **ya** | biaya iklan di periode itu |
| `ad_sales` | **ya** | omzet yang diatribusikan ke iklan |
| `orders`, `units` | disarankan | jumlah pesanan dan unit dari iklan |
| `cogs_per_unit` atau `cogs_pct` | disarankan | HPP produk sampai gudang |
| `fee_pct` | disarankan | komisi/biaya admin |
| `fixed_fee_per_order` | disarankan | biaya proses pesanan dan biaya tetap sejenis |
| `voucher_pct` | opsional | porsi voucher yang ditanggung toko |
| `shipping_subsidy_per_order` | opsional | ongkir yang ditanggung toko |
| `affiliate_pct` | opsional | komisi kreator/affiliate |
| `return_pct` | opsional | cadangan untuk retur dan pembatalan |

Kolom biaya yang kosong dihitung nol, jadi hasilnya terlihat lebih bagus dari kenyataan. Skill akan memberi tahu.

Bisa dijalankan sendiri tanpa agent:

```bash
python3 skills/digital-ads-ultimate/scripts/marketplace_analyzer.py examples/marketplace_ads_sample.csv --total-sales 120000000 --target-poas 1.3
```

File contoh itu fiktif. Di dalamnya, "Kaos Polos 3 Pack" punya ROAS 5,00 tapi POAS 0,25 dan ditandai CUT.

### Workbook latihan (Excel)

`examples/Digital_Ads_Practice_Workbook_2026.xlsx` adalah file praktik lengkap dengan data fiktif (brand "Nusa Apparel"). Satu sheet per platform, rumus hidup, sel input berwarna biru, dan verdict di tiap baris.

| Sheet | Yang dilatih |
| --- | --- |
| Panduan | Cara pakai, kode warna, definisi metrik |
| Asumsi | Ekonomi per pesanan, break-even ROAS, target POAS, ambang penilaian (ganti sel kuning) |
| Google Ads | 6 campaign termasuk porsi brand di PMax, plus tabel search terms untuk negative keyword |
| Meta Ads | 7 iklan: fatigue, hook kuat tapi landing lemah, data kurang |
| TikTok Ads | 7 kreatif: hook rate, hold rate, CTR turun, Spark |
| LinkedIn Ads | B2B sampai SQL dan deal Won: lead murah yang tidak jadi SQL |
| Marketplace | Shopee, Tokopedia, TikTok Shop: ROAS vs POAS, tumpukan biaya, TACoS per platform |
| Mingguan | 8 minggu MER, break-even MER, klaim platform vs omzet nyata, CAC |
| Dashboard | Ringkasan lintas platform, baris terburuk, grafik |
| Latihan | 13 tugas dengan kunci jawaban rumus hidup dan prompt siap salin |

Ganti sel biru dengan ekspor akunmu, atur asumsi kuning, lalu lampirkan file ke agent. Prompt ada di sheet Latihan dan di bagian atas.

### Batasan jujur

- Biaya admin, jenis iklan, dan aturan atribusi marketplace sering berubah (Shopee mengubah atribusi GMV Max dan tarif admin bertingkat di 2026; tooling iklan Tokopedia dan TikTok Shop masih bertransisi). Cek halaman biaya terbaru di Seller Center dan masukkan angka aslinya.
- Fitur platform 2026 sebagian besar dari sumber praktisi, bukan dokumen resmi, dan ditandai untuk diverifikasi.
- Tidak ada janji hasil. Akun live hanya diubah setelah kamu setujui, dan campaign dibuat dalam keadaan paused.
- Catatan hukum (termasuk aturan Indonesia) hanya pengingat untuk dicek ke ahli hukum, bukan nasihat hukum.

## License

MIT. See [LICENSE](LICENSE) and [CREDITS.md](CREDITS.md).
