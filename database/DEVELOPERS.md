# Slideshow database · developer guide

A guide for building the slideshow database into the Amplify app. The data is plain JSON plus JPEG files. No database server or API is needed.

**What's in it:** 36 niches, 567 TikTok slideshows that performed well, and 3,916 slide images (about 410 MB). The niches are grouped into 9 business types (what Amplify's users sell), and each business type is linked to the Amplify templates that suit it. Most slideshows (524) come from the ReelFarm slideshow database (reel.farm/dashboard/database). The other 43 are TikTok posts the owner picked, read straight from TikTok with exact stats and the post link. Everything was collected on 2026-10-17.

## Layout

```
database/
  categories.json                 the 9 business types: their niches and templates  ← start here
  categories/<type>.md            generated page per business type
  README.md                       generated overview (what GitHub shows)
  DEVELOPERS.md                   this file
  niches/<slug>/
    niche.json                    niche summary: status, counts, how it was collected
    slideshows.json               the slideshows (array)  ← the main data
    slides/<account>_<index or post id>/01.jpg, 02.jpg …   the slide images, in order
    README.md                     generated gallery page
    reelfarm_raw.json             ReelFarm capture used by the builder (don't read it in the app)
    tiktok_raw.json               owner-picked TikTok posts used by the builder (only in some niches, don't read it in the app)
content-bank/P0xx-<name>/pillar.md   the Amplify templates the business types point to
```

The `README.md` and `categories/*.md` files are generated. Read the JSON files, not the markdown.

## categories.json

An array of business types.

| Field | Type | Meaning |
|---|---|---|
| `slug` | string | id, also the file name in `categories/` |
| `name` | string | display name, e.g. "AI tools and SaaS" |
| `brands` | string | roughly how many Amplify brands sell in this type, e.g. "~41" |
| `sell` | string | what those brands sell |
| `niches` | string[] | niche slugs, each one a folder in `niches/` |
| `templates.made_for_it` | string[] | template ids (`P014`) that fit as they are |
| `templates.works_with_a_tweak` | string[] | template ids that fit with a small change |
| `gap` | string, optional | what's missing or a rule to respect (e.g. UK rules on GLP-1 ads) |
| `notes` | string, optional | extra caution for this type |

A niche can belong to more than one business type (e.g. `creator-growth` is in AI tools and in Creators). A template id maps to a folder: `P014` is `content-bank/P014-tool-demo-listicle/`. Its `pillar.md` starts with YAML front matter with `id`, `name`, `type`, `summary`, `status` and `confidence`.

## niches/&lt;slug&gt;/niche.json

| Field | Meaning |
|---|---|
| `slug`, `niche` | folder name and display name (`hair-care`, "hair care") |
| `status` | `approved`, `pending` or `needs-more`. **Only show `approved`.** |
| `slideshows`, `accounts`, `slides`, `size_mb` | counts |
| `collected` | date the stats were captured. Views and likes are a snapshot from that date |
| `source`, `reelfarm_total`, `sort`, `scanned`, `rule` | where it came from and how the slideshows were chosen. A niche built only from the owner's TikTok links has `reelfarm_total` and `scanned` set to null |
| `from_tiktok_links` | how many of the slideshows are owner-picked TikTok posts |
| `notes` | owner notes |
| `skipped_broken` | slideshows that were left out because their images couldn't be downloaded |
| `removed` (optional) | slideshow folders the owner removed. The builder won't add them back |

## niches/&lt;slug&gt;/slideshows.json

An array, best first (most likes first). Every record has the same fields. `source` says where a record came from: `reelfarm`, or `tiktok` for a post the owner picked from TikTok.

| Field | Example | Notes |
|---|---|---|
| `n` | `1` | position in this niche |
| `source` | `"reelfarm"` or `"tiktok"` | where the record came from |
| `reelfarm_rank` | `1` or `null` | rank on ReelFarm before filtering, null for `tiktok` records |
| `account` | `"studyw.tok"` | TikTok handle, no @ |
| `nickname` | `"A+ Student Tips 💡"` | display name, may contain emoji |
| `account_url` | `"https://www.tiktok.com/@studyw.tok"` | |
| `post_url` | `"https://www.tiktok.com/@dropship/photo/7400…"` or `null` | set for `tiktok` records. ReelFarm doesn't expose the post link, so it's null for `reelfarm` records |
| `posted`, `caption` | `"2024-08-07"`, `"Dropshipping in 24hrs
#entrepreneur …"` | posting date (UTC) and the post's title plus caption. `tiktok` records only, null otherwise |
| `followers`, `following` | `"1.0M"`, `"124"` | display strings |
| `account_region` | `"NL"` or `null` | ISO country code. TikTok doesn't show it, so null for `tiktok` records |
| `audience_regions` | `["South Africa 38.71%", …]` or `null` | top 3, display strings. Null for `tiktok` records |
| `sells` | `"Study tools and motivation"` or `null` | what the account promotes: ReelFarm's guess, or for `tiktok` records written from the bio, link in bio and slides |
| `product_medium` | `"Website"` or `null` | how it's sold |
| `link_in_bio`, `bio` | | as shown on the profile, may be null |
| `views`, `likes`, `saves` | `"22.3M"`, `"2.9M"`, `"585.0K"` | display strings |
| `comments`, `shares` | `"8.7K"`, `"15.0K"` or `null` | display strings, `tiktok` records only (ReelFarm doesn't show them) |
| `engagement_rate` | `"13.0%"` | likes ÷ views, the same formula ReelFarm uses |
| `save_rate` | `"2.6%"` | saves ÷ views |
| `app` | `"sage ai"` or `null` | the promoted app, when the slideshow advertises one |
| `found_in` | `"mobile-app"`, `"owner's TikTok link"` or `null` | the ReelFarm category it came from (used in `apps-and-saas`), or `"owner's TikTok link"` |
| `slide_count` | `3` | |
| `slides` | `["slides/studyw.tok_1/01.jpg", …]` | paths **relative to the niche folder**, in slide order |
| `source_images` | `["https://reelfarm-slideshow-images…/slideshow_2ae9c8b9.jpg", …]` | the originals at full size (ReelFarm's host, or TikTok's signed links, which expire within days). They can stop working at any time, so use `slides` |

**Numbers are display strings.** Turn them into numbers like this: `"585.0K"` → 585000, `"2.9M"` → 2900000, `"13.0%"` → 13.0. Strip commas first.

**Slides** are JPEGs, at most 720 px wide (mostly 720 × 960, 720 × 1280 or 720 × 900), quality 82. A public URL for a slide:

```
https://raw.githubusercontent.com/Dyowanana/amplify/main/database/niches/<slug>/<slide path>
```

For production, copy the images to your own storage or CDN instead of serving them from GitHub.

## Quick start

Python:

```python
import json
from pathlib import Path

DB = Path("database")

def num(s):
    s = str(s).replace(",", "").rstrip("%")
    mult = {"K": 1e3, "M": 1e6, "B": 1e9}.get(s[-1:], 1)
    return float(s[:-1] if mult != 1 else s) * mult

types = json.loads((DB / "categories.json").read_text(encoding="utf-8"))
ai = next(t for t in types if t["slug"] == "ai-tools-and-saas")

for slug in ai["niches"]:
    folder = DB / "niches" / slug
    if json.loads((folder / "niche.json").read_text(encoding="utf-8"))["status"] != "approved":
        continue
    for s in json.loads((folder / "slideshows.json").read_text(encoding="utf-8")):
        cover = folder / s["slides"][0]
        print(slug, "@" + s["account"], num(s["views"]), s["engagement_rate"], cover)
```

JavaScript (from GitHub, no clone):

```js
const RAW = "https://raw.githubusercontent.com/Dyowanana/amplify/main/database";
const types = await (await fetch(`${RAW}/categories.json`)).json();
const shows = await (await fetch(`${RAW}/niches/skincare/slideshows.json`)).json();
const coverUrl = `${RAW}/niches/skincare/${shows[0].slides[0]}`;
```

## A suggested flow in the app

1. The user picks a business type (`categories.json`), or it comes from their brand.
2. Show that type's niches, then the slideshows as cover cards with views, likes and engagement rate, like ReelFarm's database page.
3. Open a slideshow to show every slide plus the account card.
4. Beside it, offer the matching templates (`made_for_it` first) so the user can make their own version.

## Rules to keep

- **These are reference posts. Never repost them.** The slides belong to their creators. Amplify learns the format (the structure, pacing and hook type) and makes new posts with new wording, characters and art (rule 3 in `doc/Owner Rules.md`). Don't build a "repost" or "download and post" button.
- **Some hooks need care.** Dating has manipulation-style hooks ("make him obsessed"), and mental health has dark-psychology ones. They're fine as format examples, but a brand shouldn't repeat that message. Health: prescription medicines such as GLP-1 can't be advertised to the public in the UK (see the `gap` field).
- **Thin niches:** weddings (2 slideshows), pets (3), faith (3), gut health (3), photography (4), art (6), beauty (7) and hair care (7) are small because ReelFarm has few strong posts there. Hide or label them if you set a minimum.
- **Gaps the owner will fill by hand later:** food beyond healthy eating, crypto, forex and mutual funds, B2B and AI software, kids and storybooks, gut health, and travel. New niches will have the same files and fields.

## Updating the data

Only the owner collects new slideshows (they need a ReelFarm login). The builder is `tools/reelfarm_db.py`:

```
python tools/reelfarm_db.py build database/niches/<slug>     download slides, write slideshows.json and the README
python tools/reelfarm_db.py keep <slug> "1-9"                keep only these slideshows, delete the rest
python tools/reelfarm_db.py status <slug> approved           set the status
python tools/reelfarm_db.py index                            rewrite database/README.md and categories/*.md
```

The fields above won't be renamed without updating this guide. Watch for new optional fields.
