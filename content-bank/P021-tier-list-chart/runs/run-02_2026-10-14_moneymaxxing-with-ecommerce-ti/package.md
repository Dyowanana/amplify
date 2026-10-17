# P021 run-02 · tier list of moneymaxxing with ecommerce

**Pillar:** P021 Tier list chart (the source is the same TikTok, `vt.tiktok.com/ZSboCTLHp`, @mentalapp's dopamine sources tier list). **Topic:** dropshipping and ecommerce. **Persona:** none. **Mode:** brand (pillar format followed strictly). **Caption style:** none (no brand file, no bio plug, no disclosure).

## How the inputs combine
- **Format, from the TikTok:** the 2-slide carousel (a "tier list of" cover around one vivid false-colour hero, then the filled chart), tier colours and order, the plus gap before F, the thin grotesque, the corner line glyph and 3D object on the cover, a challenge title and the F-row "your option (comment)" cell.
- **Background, owner's ask ("same shade but orange"):** #FEEDE1, the source's #EDF2EB turned orange at the same lightness (Lab L 94.8), the same value run-01 used.
- **Icons, owner's ask ("not perfect, meme like, not cute, more edgy"):** run-01's icons were clean glossy 3D. This run leans on the source's rougher side: grimy flash-photo object cut-outs (dirty laptop, crushed box, burning card, junk tub, snail), classic meme-style fictional people cropped at the upper body like the source's people (hyped ugc guy, gold-chain guru, trench-coat watch seller, skeleton waiting on a bench), one glossy 3D fire and one flat black glyph. All people are generated and fictional; no real faces, no brand logos drawn by the model.
- **Shopify at the top, owner's ask:** the first S-tier cell is a beat-up laptop whose screen is a **real screenshot of shopify.com** (`webshot.py`, MacBook Air size). The homepage hero is a video of real people, so the screen uses Shopify's own "control everything in one place" card instead (their logo plus their UI labels, no people, no other brands). The composite is `raw/screen.py`.
- **Less stuff, owner's ask:** 15 cells instead of the source's 24 (2 to 3 per row).

| Tier | Tagline | Items |
|---|---|---|
| S | prints, scales | Shopify store · winning product · ugc ads |
| A | works, takes grind | organic TikTok · abandoned cart emails |
| B | solid, slow | print on demand · paid ads |
| C | mid, risky | general store · cheap suppliers · slow shipping |
| D | mostly cope | guru courses · dead trends |
| F | bans, refunds | knockoffs · fake reviews · your option (comment) |

## Hooks (mechanic named)
- Cover: **"tier list of / moneymaxxing / with ecommerce"**. Formula phrase "tier list of" is trend wording, kept word for word.
- Chart title, mechanic **challenge / dare to disagree** (source "prove me wrong"): **"fight me on this"**.
- Closing line, mechanic **interactive ask**: **"which tier is your store in?"**
- F-row cell, mechanic **interactive ask**: "your option (comment)", kept (it's the format's comment driver).

## Slides
| # | Visual | Text (drawn in code) |
|---|---|---|
| 1 | Peach card, an open shipping box overflowing with gold coins and bars as a neon false-colour scan, a black rising chart line bottom-left, a glossy gold coin stack bottom-right | tier list of / moneymaxxing / with ecommerce |
| 2 | Peach card, tier table S to D plus F, 14 cut-out icons and a question mark | fight me on this · taglines · labels · which tier is your store in? |

## Caption
`caption.txt` (built by `caption.py`): one casual lowercase line with the takeaway, a comment ask, 5 hashtags (dropshipping, ecommerce, tierlist, shopify, sidehustle).

## Posting
- Photo carousel with a trending slowed song picked inside TikTok (the licensed way).
- Evening slot (the source went out 22:25 local).
- Switch on TikTok's AI-generated content label (icons and hero are AI-generated).

## Production
Style ref from the source's own photo icons (food, CD, water, coffee; the cash and fast-food cells were left out because they show a real portrait and a logo) → 3 icon sheets and 1 hero with `gpt25s` → `tiercards.py cut` → shopify.com screenshot on the laptop (`raw/screen.py`) → upper-body crops (`raw/crops.py`) → `tiercards.py render spec.json` → `measure.py check --record` → `originality.py` → `caption.py check`.
