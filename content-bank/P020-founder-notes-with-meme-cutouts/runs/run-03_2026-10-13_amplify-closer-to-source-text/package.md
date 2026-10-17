# P020 · run 03 · amplify closer to source text

Owner request (2026-10-13): text closer to the original. Copy the hook exactly ("pov reality of building a saas in 2026") and slide 2's title ("the game has changed"); slide 3 onward can change. Same message as run-01 (distribution is the game, simple slideshows get millions of views, AI makes the content, 30 free posts from Amplify, two scheduled posts a day, kill flops, double down). Headings follow the source's sequence more closely ("the game has changed", "conclusion"). Card in the source's grey #e4e3df. All 7 people are new, classic film-still style with the film grade. Cutouts fill the bottom.

| # | Heading | Body (short) | Person |
|---|---|---|---|
| 1 | pov reality of building a saas in 2026 (source hook, colon dropped by the owner's punctuation rule) | swipe arrow | young man on the floor with a laptop on a cardboard box, tired stare, halftone |
| 2 | the game has changed (source title) | building used to be the edge, now ai writes the code, the edge is who sees it | older man lowering a newspaper in shock |
| 3 | distribution is the game | the 17.4M-view single-selfie slideshow, no editing or budget, simple slideshows get millions while polished apps launch to nobody | man in suspenders jabbing at bar charts |
| 4 | flip the order | months of coding then panic about marketing, post from day one, "i used Amplify … 30 posts. didn't pay for any of them." (link in bio) | woman in an armchair with a laptop and popcorn |
| 5 | post twice a day | one a week is a lottery ticket, batch weekly, schedule two a day on TikTok | coach in a tracksuit, two fingers up, stopwatch |
| 6 | double down | after two weeks most formats flop, kill them, make ten more of the hit | man in a loosened tuxedo pushing two stacks of poker chips forward |
| 7 | conclusion (source title) | everyone's shipping, post daily and keep what works, no team no budget, Amplify is the link in my bio | woman in a denim jacket on a desk with a mug, halftone |

## Caption (soft, `caption.txt`, PASS)
```
read this before you build a saas in 2026 📌

the posts are the hard part. i got 30 for my saas from Amplify, for free.

#saas #developer #appdeveloper #socialmediagrowth #fyp

this is an advertisement.
```
The first line and 4 of the 5 hashtags follow the source caption, as asked.

Production: 7 × `kie.py image --model gpt25s --resolution 2K --aspect 3:2`, prompts in `raw/art/prompts.tsv` (70 credits, $0.35), all first take. Cover art cropped on the left (`crop_x`) so the person is bigger. Render: `tools/memecards.py spec.json`.
Posting: photo carousel, a trending low-key track, the AI label and commercial content toggle on.
