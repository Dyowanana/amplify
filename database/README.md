# Slideshow format database

TikTok slideshows that performed, grouped by niche, with the account behind each one, its numbers and every slide, so any brand can pick a niche and remake a format. Approved niches are reviewed by the owner.

## By business type

What Amplify's users sell, with the ReelFarm niches and the templates already studied (`content-bank/`) for each.

| Business type | Brands | Niches collected | Templates studied | Gap |
|---|---|---|---|---|
| [AI tools and SaaS](categories/ai-tools-and-saas.md) | ~41 | 5 of 6 | 7 (+4 with a tweak) | ⚠️ ReelFarm has few real B2B or AI-software slideshows (the best one has 363K views) |
| [Health, fitness and wellness](categories/health-fitness-and-wellness.md) | ~12 | 5 of 5 | 11 (+5 with a tweak) | ⚠️ Prescription-only medicines (GLP-1, Mounjaro, Wegovy) can't be advertised to the public in the UK |
| [Food](categories/food.md) | ~9 | 1 of 1 | 2 (+4 with a tweak) | ⚠️ ReelFarm has no food niche beyond healthy eating (no pizza ovens, bakeries, Filipino food or kitchen equipment) |
| [Creators and personal brands](categories/creators-and-personal-brands.md) | ~9 | 2 of 5 | 8 (+2 with a tweak) |  |
| [Money, investing and crypto](categories/money-investing-and-crypto.md) | ~8 | 0 of 1 | 4 (+3 with a tweak) | ⚠️ ReelFarm has personal finance only (129 slideshows) |
| [Education and coaching](categories/education-and-coaching.md) | ~6 | 3 of 4 | 5 (+3 with a tweak) |  |
| [Fashion, beauty and kids](categories/fashion-beauty-and-kids.md) | ~4 | 0 of 7 | 5 (+3 with a tweak) | ⚠️ Kids and storybooks are thin on ReelFarm (mom life and booktok are the closest) |
| [Everything else](categories/everything-else.md) | ~4 | 0 of 3 | 2 (+2 with a tweak) | ⚠️ Photography has only 28 slideshows on ReelFarm, and there's nothing for lab automation or business marketplaces |

## All niches

| Niche | Status | Slideshows | Accounts | Slides | Collected | Notes |
|---|---|---|---|---|---|---|
| [apps and saas](niches/apps-and-saas/README.md) | approved | 25 | 21 | 132 | 2026-10-17 |  |
| [career](niches/career/README.md) | approved | 13 | 8 | 73 | 2026-10-17 |  |
| [creator growth](niches/creator-growth/README.md) | approved | 11 | 7 | 62 | 2026-10-17 |  |
| [fitness](niches/fitness/README.md) | approved | 23 | 14 | 136 | 2026-10-17 |  |
| [gut health](niches/gut-health/README.md) | approved | 3 | 2 | 19 | 2026-10-17 | Thin on ReelFarm: only 3 of 45 pass 100K views. Add accounts by hand. |
| [healthy eating](niches/healthy-eating/README.md) | approved | 24 | 14 | 200 | 2026-10-17 |  |
| [marketing](niches/marketing/README.md) | approved | 9 | 7 | 71 | 2026-10-17 | Thin niche on ReelFarm (162 slideshows, mostly social media managers and branding studios). Owner kept the 9 strongest (700K+ views). |
| [mental health](niches/mental-health/README.md) | approved | 25 | 18 | 155 | 2026-10-17 |  |
| [productivity](niches/productivity/README.md) | approved | 12 | 8 | 76 | 2026-10-17 |  |
| [self improvement](niches/self-improvement/README.md) | approved | 25 | 22 | 166 | 2026-10-17 |  |
| [wellness](niches/wellness/README.md) | approved | 23 | 16 | 190 | 2026-10-17 |  |

## How a niche is collected

1. Open the niche in the ReelFarm database (logged in, browser pane). The page holds each card's profile and slideshow data.
2. Take the first pages sorted by most likes, keep at most 2 slideshows per account, drop duplicates, stop at 25.
3. Save that as `niches/<slug>/reelfarm_raw.json`, then `tools/reelfarm_db.py build niches/<slug>` downloads every slide and writes the page.
4. The owner reviews the niche page: approve, ask for more, or name slideshows to remove. Only then is it pushed.

ReelFarm shows the account, not the TikTok post link, so `post_url` is empty for now.
