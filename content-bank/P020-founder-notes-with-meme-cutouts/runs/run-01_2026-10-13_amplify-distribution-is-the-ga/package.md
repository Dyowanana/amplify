# P020 · run 01 · amplify distribution is the game

@founderscale's "pov: reality of building a saas 2026" carousel, remade for Amplify. Instead of a newsletter plug, the post argues that distribution is the game: simple TikTok slideshows get huge views, AI makes the content, two scheduled posts a day, cut the formats that flop and double down on the ones that hit. Amplify sits where the source puts its plugs (the bracketed bio line on the main lesson and the CTA on the conclusion), in the owner's first person. Caption style **soft**, brand `brands/amplify.md` (drafted in this run from the owner's request).

## Hook options (mechanic: reality check aimed at a builder identity, "pov" kept as the trend word, colon dropped by the owner's rule)
| Option | Overlap with the source hook |
|---|---|
| **pov you launched and got zero signups** (used) | 14% (shared: pov) |
| pov your app is live and the only user is you | not measured, backup |
| pov you spent 3 months building and 0 people saw it | not measured, backup |

## Slides (1080 x 1350, `spec.json` → `tools/memecards.py`)
| # | Role | Heading | Body (short) | Cutout |
|---|---|---|---|---|
| 1 | Hook | pov you launched and got zero signups | (none) + swipe arrow | young man in a hoodie slumped at a laptop, flat stare, halftone |
| 2 | The game changed | shipping is the easy part | ai builds it in a weekend for everyone, so the app isn't the edge, getting it seen is | woman in a blazer shrugging, bottom right |
| 3 | Proof | distribution is the game | the apps growing are the ones you keep seeing. one single-selfie post i broke down got 17.4 million views. no face cam, no editing, no ad budget | man in a suit tapping his temple |
| 4 | Main lesson + plug | let ai make the content | founders stop because it takes forever. remake formats that already pull views. "i did this with Amplify and got 30 posts for my saas. for free." (Amplify is the link in my bio) | man leaning back, hands behind head, laptop |
| 5 | Posting system | post twice a day | a week of posts in one sitting, schedule two a day on TikTok, more posts means more data | woman holding up a phone, pointing at it |
| 6 | Kill and double down | kill what flops | after two weeks a few formats pull views, stop the ones that stall, make ten more of the ones that hit | man tossing a crumpled paper over his shoulder |
| 7 | Conclusion + CTA | the short version | build less, post more, the whole system in three lines, no team, no ad budget, "Amplify is the link in my bio." | woman with arms crossed, calm smile, halftone |

Proof on slide 3 is real: the 17.4M-view single-selfie slideshow is @emmakeeleykawesha's post in our own bank (P013, `post.json`), described without naming the account.

## Caption (soft, `caption.txt`)
```
save this before you build another app nobody sees 📌

the hard part is having enough posts. i made 30 for my saas with Amplify, for free.

#saas #solofounder #buildinpublic #contentmarketing #fyp

this is an advertisement.
```

## Posting
- Post as a photo carousel, 7 images in order, with a trending low-key track (the source used a fan upload of an indie song; pick it in TikTok, it's not attached here).
- TikTok's AI-generated content label on (the people are AI) and the commercial content toggle on (it promotes Amplify).
- Evening or early morning in the audience's time zone. The source went out at 04:43 Manila time (US evening).

## Production
- People: 7 × `kie.py image --model gpt25s --resolution 2K --aspect 4:3` on chroma green, prompts in `raw/art/prompts.tsv` (70 credits, $0.35). All 7 used first take.
- Render: `tools/memecards.py spec.json` (new in this run). Keys the green, turns the person grayscale, adds a halftone screen on the cover and closer and the white sticker outline. Heading and monospace body drawn in code (Inter Bold, DejaVu Sans Mono).
- Checks: `originality.py`, `caption.py check`, `measure.py check --record` on every slide (`output/checks/`).
