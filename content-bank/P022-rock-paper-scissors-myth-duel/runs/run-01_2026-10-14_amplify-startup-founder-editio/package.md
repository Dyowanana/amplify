# Package · P022 run-01 · amplify, startup founder edition

**Pillar** P022 Rock paper scissors myth duel (from @brightbraintech's "think you know marketing?" carousel). **Brand** `brands/amplify.md` plus the Amplify design system (navy #0E1A24, tangerine #FF7A00, the chevron mark) and the look of @withamplifyai's feed (navy card, faint grid, condensed heavy headline, tangerine accent line, tracked handle top-left, counter top-right). **Caption** soft.

## How pillar and brand combine
- **Format kept:** the game. Cover with a call to play and a standoff, then one round per slide, two cut-out hands from opposite edges at one height, the losing line above the left hand, the winning line under the right hand. The right gesture really beats the left one on every round.
- **Brand on top:** the red felt becomes a navy felt grain with the feed's faint grid; the winning line is tangerine (one accent per view), the losing line white; the real chevron logo + `withamplify.ai` top-left, `NN / 07` top-right.
- **Owner's direction:** two men, coder look, styled as different people. Left: light olive skin, charcoal hoodie with a worn ribbed cuff, black braided cord bracelet. Right: deep brown skin, light grey hoodie, black watch strap, silver ring. Paper shows the palm with the fingers slightly apart. The source's iOS edit menu became a coder motif: a thin tangerine text caret right after "shoot" and a pointer resting on the word.

## Hooks
| Option | Mechanic | Overlap with source hook |
|---|---|---|
| **rock, paper, scissors, shoot / startup founder edition** (used, the owner's line) | game call + edition (trend wording) | 0% with the source hook; "rock paper scissors" is the trend's name and also sits in the source caption |
| think you know startups? / swipe to play | challenge to know-how (the source's mechanic) | "think you know" is the formula phrase |

## Slides
| # | Left (loses) | Right (wins) | Text |
|---|---|---|---|
| 1 | rock | scissors | `rock, paper, scissors, shoot` · `startup founder edition` · `swipe to play →` |
| 2 | rock | paper | shipping another feature · **marketing the product you already built** |
| 3 | paper | scissors | adding 10 more functions · **launching with one mvp** |
| 4 | scissors | rock | building in silence · **building in public** |
| 5 | rock | paper | the perfect marketing post · **low effort posts every day** |
| 6 | paper | scissors | waiting until it's ready · **posting while it's still ugly** |
| 7 | scissors | rock | redesigning the logo again · **posting something today** |

Text is the owner's, lowercased, with the colons and periods dropped.

## Caption (`caption.txt`, built by `caption.py`)
```
rock, paper, scissors, founder edition 🪨📄✂️ which round are you still losing?

most of these rounds come down to posting more. Amplify learns formats that already work on TikTok and Instagram and makes new posts for your product in them.

#startup #founder #buildinpublic #saas #startupmarketing

this is an advertisement.
```

## Posting
Instagram carousel, 4:5. Turn on the AI label (the hands are generated) and, for the soft sell, the paid-partnership or branded content toggle if the account uses it. Weekday evening, the slot the account already uses.

## Production
1. 6 hand images, `nbp` 2K 3:2 on chroma green: left rock first and the other left gestures with it as the reference; right rock as a new person, and his other gestures with it as the reference. Paper prompts ask for the palm toward the camera with a small gap between every finger. The right player's size is evened out with `zoom` (measured by wrist thickness).
2. `tools/rpscards.py spec.json`: keys the green, puts each fingertip at 45.5 / 54.5% and keeps every hoodie cuff at least 8% inside the frame, then draws the background, mark, counter, text, caret and pointer.
3. `measure.py check --record` per slide, `originality.py`, `caption.py check`.
