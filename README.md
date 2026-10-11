# Digital Ads Ultimate Skill 2026

One agent skill for Google Ads, Meta Ads, LinkedIn Ads, and TikTok Ads. It covers the whole job: strategy and unit economics, tracking, campaign build, creative and copy, launch, optimization, scaling, audits, and reports with ranked recommendations.

Works with Claude Code and any agent that reads `SKILL.md` skills.

## What you get

| Stage | What the skill does |
| --- | --- |
| Strategy | Break-even CPA/ROAS, platform fit, budget sizing, funnel and objective map |
| Tracking | Conversion design, Pixel + server events with dedup, consent, UTMs, QA protocol |
| Build | Structure and naming per platform, keyword and audience plans, creative matrix, copy specs |
| Launch | Paused-first build, safety gate for live accounts, launch checklist |
| Optimize | Layered diagnosis (delivery, cost, attention, landing, conversion, value, measurement), decision rules, fatigue detection |
| Scale | Step sizes, marginal CPA checks, creative supply plans |
| Audit | Scored checklists per platform with evidence rules |
| Report | Weekly and monthly templates, recommendations ranked by impact, confidence, effort |
| Math | `ads_math.py`: break-even, funnel forecast, budget sizing, sample size, A/B significance |

## Install

Claude Code:

```bash
git clone https://github.com/shafry00/digital-ads-ultimate-skill-2026.git
cp -r digital-ads-ultimate-skill-2026/skills/digital-ads-ultimate ~/.claude/skills/
```

Restart the session. The skill triggers on requests like "audit akun Meta saya", "buatkan strategi Google Ads untuk toko saya", "kenapa CPA TikTok naik", or "plan LinkedIn campaign for my SaaS".

## Layout

```
skills/digital-ads-ultimate/
  SKILL.md                     orchestrator: rules, safety gate, workflow, routing
  references/
    01-strategy-and-math.md
    02-measurement.md
    03-google-ads.md
    04-meta-ads.md
    05-linkedin-ads.md
    06-tiktok-ads.md
    07-creative-and-copy.md
    08-landing-and-funnel.md
    09-optimize-and-diagnose.md
    10-audit-checklists.md
    11-testing-reports-templates.md
  scripts/ads_math.py          stdlib calculator, run `selftest` to verify
```

The agent loads only the files a task needs.

## Principles

1. Numbers before tactics. No budget or bid advice without break-even math.
2. Tracking before spend. Nothing launches until the conversion fires correctly.
3. Evidence over opinion. Every diagnosis cites a metric and a comparison.
4. Heuristics are labeled. Platform rules change, so the skill tells the agent to verify live facts.
5. No promised results and no invented proof. Compliance is part of the workflow.
6. Draft first. Live accounts change only after explicit approval, and campaigns are built paused.

## Honest limits

- Platform features and defaults change every few months. 2026 items (AI Max, Performance Max channel reporting, Advantage+ defaults, Smart+, GMV Max) come largely from practitioner sources, not official docs. They are marked for verification.
- Benchmarks differ across vendors and definitions. The skill compares accounts to their own history and economics instead.
- Legal and regulatory notes (including Indonesian rules) are prompts to check with counsel, not legal advice.

## Ringkasan (Bahasa Indonesia)

Satu skill untuk Google Ads, Meta Ads, LinkedIn Ads, dan TikTok Ads, dari nol sampai optimasi. Isinya: hitung break-even dulu, pasang tracking dan verifikasi sebelum spend, bangun struktur campaign per platform, brief kreatif dan copy, checklist launch, diagnosis performa per lapisan, aturan scale dan kill, audit berskor, serta laporan dengan rekomendasi yang diurutkan berdasarkan dampak, keyakinan, dan usaha. Skill otomatis menjawab dalam bahasa yang kamu pakai, termasuk contoh dalam Rupiah dan alur WhatsApp.

Pakai: salin folder `skills/digital-ads-ultimate` ke `~/.claude/skills/`, lalu minta misalnya "buatkan strategi iklan untuk bisnis saya, budget Rp 5 juta per bulan".

## License

MIT. See [LICENSE](LICENSE) and [CREDITS.md](CREDITS.md).
