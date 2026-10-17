# P021 run-01 · tier list of marketing for your business

**Pillar:** P021 Tier list chart (format from @mentalapp's dopamine sources tier list). **Content:** the rankings from the owner's video (a founder ranking marketing channels to camera: `content-bank/_sources/ig_tierlist_inspo/manual-20261013-233616`). **Persona:** none. **Mode:** brand (pillar format followed strictly). **Caption style:** none (no brand, no bio plug, no disclosure).

## How the inputs combine
- **Format, from the TikTok:** the 2-slide carousel (a "tier list of" cover around one vivid hero cut-out, then the filled chart), the tier colours and order, the plus gap before F, the thin grotesque, the corner glyph and 3D object on the cover, a challenge title and the F-row "your option (comment)" cell.
- **Background, owner's ask:** the source's pale grey-green #EDF2EB turned orange at the same lightness (Lab L 94.8): **#FEEDE1**, a pale peach. A strict chroma match (#F7EFE9) reads almost white, so the orange is pushed to about 2x the source's tint. Changing the colour is one value in `spec.json` (`theme.bg`).
- **Icons, owner's ask:** the same mixed families as the source (photoreal object cut-outs, glossy 3D emoji-style icons, flat black glyphs in the F row), generated as sheets with a style reference built from the source's own non-text icons (trophy, weather tile, frying pan, controller), then cut out in code. No people, no brand logos (the source used real people's photos and logos, which we never copy).
- **Content, from the video:** every ranking the speaker gave is kept as said.

| Item | Tier | From |
|---|---|---|
| short form video | S | video ("S tier, especially short form") |
| posting consistently on social media | S | **owner swap** (replaced the video's "quizzes", 2026-10-14) |
| writing a book | S | video ("becoming an author") |
| personal brand | S | video |
| seo | A | video ("still an A tier approach") |
| Facebook ads | A | video ("A or B", settled on A) |
| cold email | D | video |
| referrals | A | **added** to fill the chart |
| podcast guesting, paid search, influencer collabs | B | **added** |
| flyers, radio ads, billboards | C | **added** |
| cold calling, random giveaways | D | **added** |
| buying followers, spam dms, fake reviews | F | **added** |

The video only ranks 7 channels (S, A and D), and the format needs every row filled. The added items are common, uncontroversial placements; swap or delete any of them in `spec.json` and re-render for free.

## Hooks (mechanic named)
- Cover: **"tier list of / customer / sources"** (owner pick 2026-10-14, replaced "marketing / for your business"; mirrors the source's "Dopamine / sources" shape): formula phrase "tier list of" is the trend wording, kept word for word.
- Chart title, mechanic **challenge / dare to disagree** (source: "prove me wrong"): **"change my mind"**.
- Closing line, mechanic **interactive ask** (replaces the source's bio plug, because caption style is none): **"which tier are you stuck in?"**
- F-row cell, mechanic **interactive ask**: "your option (comment)", kept, it is the format's comment driver.

## Slides
| # | Visual | Text (drawn in code) |
|---|---|---|
| 1 | Peach card; a vintage megaphone as a neon false-colour scan in the middle; a black rising chart line with round nodes bottom-left; a glossy red magnet bottom-right | tier list of / marketing / for your business |
| 2 | Peach card; the tier table (S red, A orange, B light orange, C yellow, D light green), plus sign, F row periwinkle; 19 cut-out icons and a drawn question mark | change my mind · tier taglines · item labels · which tier are you stuck in? |

## Caption (`caption.txt`)
See `caption.txt` (built by `caption.py`). Voice: one casual lowercase line with the takeaway, then a comment ask; 5 hashtags (topic, parent topic, format).

## Posting
- Post as a photo carousel with a trending slowed song (the source used one). Pick the sound inside TikTok, which is the licensed way.
- Evening slot (the source went out 22:25 local on a Tuesday).
- Switch on TikTok's AI-generated content label (the icons are AI-generated).
- Optional: credit the video's speaker in the caption if you want to point people to the source of the rankings.

## Production
Reference set (source icon crops, no text) → 3 icon sheets and 1 hero with `gpt25s` → `tiercards.py cut` → `tiercards.py render spec.json` → `measure.py check --record` → `originality.py` → `caption.py check`.

## Background versions (owner, 2026-10-14)
Same slides, four card colours, each at the source's lightness (Lab L 94.8) and the same tint strength as the peach. Specs `spec_<colour>.json`, slides in `output/versions/<colour>/`, all four side by side in `output/versions/contact_sheet.jpg`.

| Version | Background |
|---|---|
| orange | #FEEDE1 (pale peach, the main version) |
| white | #FFFFFF |
| blue | #E3F2FF (pale sky blue) |
| green | #E9F3E4 (pale green, a touch greener than the source's grey-green #EDF2EB) |
