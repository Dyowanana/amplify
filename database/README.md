# Slideshow format database

TikTok slideshows that performed, grouped by niche, with the account behind each one, its numbers and every slide, so any brand can pick a niche and remake a format. Approved niches are reviewed by the owner.

| Niche | Status | Slideshows | Accounts | Slides | Collected | Notes |
|---|---|---|---|---|---|---|
| [marketing](niches/marketing/README.md) | approved | 9 | 7 | 71 | 2026-10-17 | Thin niche on ReelFarm (162 slideshows, mostly social media managers and branding studios). Owner kept the 9 strongest (700K+ views). |
| [self improvement](niches/self-improvement/README.md) | approved | 25 | 22 | 166 | 2026-10-17 |  |

## How a niche is collected

1. Open the niche in the ReelFarm database (logged in, browser pane). The page holds each card's profile and slideshow data.
2. Take the first pages sorted by most likes, keep at most 2 slideshows per account, drop duplicates, stop at 25.
3. Save that as `niches/<slug>/reelfarm_raw.json`, then `tools/reelfarm_db.py build niches/<slug>` downloads every slide and writes the page.
4. The owner reviews the niche page: approve, ask for more, or name slideshows to remove. Only then is it pushed.

ReelFarm shows the account, not the TikTok post link, so `post_url` is empty for now.
