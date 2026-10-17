# Review · P019 run-02 · peak creator purchases, 5 versions

## 7-point format check
| Point | Source (layout B) | This run | Match |
|---|---|---|---|
| Structure | 1 slide, centre title + 8 labelled items in a ring | same | yes |
| Hook | peak <identity> purchases / <tribe> edition | peak creator purchases / guy or girl edition | yes |
| Camera & motion | packshots, icons, a text item on white | same | yes |
| Pacing | about 25 words | about 24 | yes |
| Text overlay | heavy lowercase centre title, grey subline, Title Case labels | same, labels lowercase (owner rule; brand names keep capitals) | yes |
| Audio | music | add a trending sound in TikTok | yes |
| Arc | recognition, in-joke items | same | yes |

## Measured checks
- `originality.py` (5 boards as slides 1 to 5, against both P019 sources): words **pass** on every board (raw overlap 15%, content words 17%, longest shared run 1 word; shared words "claude", "edition", "peak", "purchases"). Images **pass**, closest 11 bits (limit 10), from the shared ring layout, not copied pixels. Hook overlap **67%**, flagged FAIL: the shared words are the trend phrase "peak … purchases"; "creator" is new. The domain stack ".ai .xyz .com" is the source's text, kept at the owner's request.
- `measure.py check --record` on all 5 records: 0 box problems (`raw/boxcheck/`).
- `caption.py check`: not run. No caption by the owner's choice.
- Board text by eye: lowercase except the names Amplify, Claude and Max; no dashes, colons or semicolons.

## Redone during the run
- Guy-2 headphones: the first take looked like a real brand's aluminium headphones (`raw/art/g2_headphones_rejected_looks-like-a-real-brand.png`). Redone as olive with round cups.
- Mid-right app slot: first a code-drawn "ai" icon labelled "the pro ai plan"; changed at the owner's request to the real Claude mark and "Claude Max plan". Domains changed from ".com .co .io" to the source's ".ai .xyz .com" at the owner's request.

## Brands on the board
- Amplify logo: the owner's own file, unchanged.
- Claude mark: real pixels from claude.com/pricing (screenshot 2026-10-11), unchanged, no other brand or face in the crop. Third-party mark used as a prop, as in the source.
- Everything else is unbranded.

## Models used
GPT Image 2.5 Sunburst only (20 calls, 120 credits). On the approved list.

## Known limits
- Guy-1 and girl-2 share the same oak desk (same prompt, cache hit).
- The white desk on girl-1 is white on white; it reads but is the faintest item.

## Tester ratings
Pending.

## Owner verdict
Pending.
