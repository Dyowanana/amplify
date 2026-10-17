# P023 learnings

## Production rules (run-01, 2026-10-14)
- The source's 4-column ring on a pale card scored 4 bits on dhash against the source (a near-duplicate), whatever the items or card colour. A 5-column top and bottom row with 2 items per side scored 24. Run `originality.py` before finishing.
- `fetch.py` can come back with only the audio for a photo post (the yt-dlp fallback). Take the slide from the public post page (the photomode image) and set `post.json` to a slideshow.
- For a collected, non-AI look: ask the image model for "a real product photo cut from a cheap online shop listing or an old stock photo", generate meme people and animals on chroma green with an old flash or film-still prompt, draw the pictograms in code, and give each item a finish in `ringcard.py` (stock, flash, film).
- A long brand label ("automated content") won't fit on one line in a side slot. Use 3 lines with "(check bio)" last.

## Owner feedback (run-01 → run-02, 2026-10-14)
- The owner prefers 4 items across the top and 5 down each side, with no bottom row. On a pale card, keep the title under the figure and that ring lands at 6 bits on dhash (a near-duplicate). With the title above the figure and the figure filling the bottom, it's 11. Saturated cards (blue, orange) pass easily (25).
- Colour versions of the same board are a cheap set: the same art and only the card changes (`versions` in the `ringcard.py` spec). On a saturated card the glow figure needs an opaque white core, or the card shows through it.

## Owner feedback (run-02 → run-03, 2026-10-14)
- The ring goes all the way round: items along the bottom too (4 top, 3 per side, 4 bottom; "5 on each side" counts the corners). Never leave a side of the ring empty.
- The title sits right under the centre figure, not far below it (`gap_below_centre` in the `ringcard.py` spec).
- With that layout on a pale card, dhash against the source is 3 to 6 bits, whatever the size of the figure or title. It passes only on a saturated card (blue 17, orange 21). Tell the owner when a pale version fails rather than moving the layout away from what they asked for.

