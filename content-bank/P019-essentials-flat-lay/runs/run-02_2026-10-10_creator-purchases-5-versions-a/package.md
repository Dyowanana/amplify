# P019 run-02 · peak creator purchases · 5 versions with the Amplify logo

Layout B (ring) from @nicodunlap's "peak solopreneur purchases / builder edition". For the Amplify account. The Amplify logo takes the source's mid-left app slot. **No caption, by the owner's choice** (2026-10-11), so no brand file and no caption check.

## How it maps to the source
| Slot | Source | This run |
|---|---|---|
| Title | peak solopreneur purchases / builder edition | **peak creator purchases** / **guy edition** or **girl edition** |
| Text item | .ai .xyz .com / Domain Names | **.ai .xyz .com** (kept at the owner's request) / unused domains |
| Work tool | branded laptop, closed | silver laptop, no logo (art reused from run-01) / the new laptop |
| Headphones | black over-ear | varies per version / good headphones |
| Mid-left app | an AI product's mascot icon | **Amplify logo** (owner's file, pasted unchanged) / Amplify |
| Mid-right app | Claude app icon / Claude Max | real Claude mark, cropped unchanged from a `webshot.py` screenshot of claude.com/pricing / Claude Max plan |
| Fitness | dumbbells / Gym Subscription | guys: gym gear / gym membership. Girls: pilates gear / pilates subscription |
| Mic | branded condenser mic / A Proper Mic | varies per version / a real mic |
| Desk | walnut and black standing desk | varies per version / standing desk |

The owner asked for "Claude Pro Max plan"; Claude's pricing page lists Pro and Max as separate plans, so the label reads "Claude Max plan" (as in the source).

## Hook (mechanic labelled)
"peak creator purchases" + edition line. Mechanic: **identity starter pack**. "peak … purchases" and "edition" are the trend words, kept; "creator" is new (Amplify's audience).

## The 5 versions
| File | Mic | Headphones | Desk | Fitness |
|---|---|---|---|---|
| `output/guy-1_white-mic-oak-desk-kettlebell.png` | white, desk tripod | matte black over-ear | oak top, white frame | black kettlebell |
| `output/guy-2_boom-mic-black-desk-dumbbells.png` | black on a boom arm | olive, round cups, leather band | all black | adjustable dumbbells |
| `output/girl-1_pink-mic-white-desk-reformer.png` | pastel pink | cream over-ear | all white | pilates reformer |
| `output/girl-2_sage-mic-retro-headphones-ring.png` | sage green | retro baby blue on-ear, coiled cable | oak top, white frame | pilates ring and grip socks |
| `output/girl-3_lilac-mic-walnut-desk-mat.png` | lilac | beige, tan leather band | walnut top, white frame | mat, ball and ankle weights |

All five side by side: `all_5_versions.jpg`.

## Posting
- Photo mode, one image per post, trending sound picked in TikTok. Switch on TikTok's AI-generated label.
- No caption (owner's choice). The post shows another company's mark (Claude) next to Amplify's; it's a lifestyle prop as in the source, not a partnership claim. Don't add wording that suggests one.

## Production
20 items with `kie.py image --model gpt25s --resolution 1K --aspect 1:1` (prompts in `raw/art/objects.tsv`; `w2_desk` reused `g1_desk` from the cache, same prompt), 1 redone. Claude mark: `webshot.py https://claude.com/pricing --scale 8`, cropped to the mark (`raw/claude/claude_mark.png`). Board: `tools/flatlay.py spec.json` (renderer now draws layout B: the centre title block, item labels, text items, app icons, and a per-version title).

## Cost
120 credits ($0.60): 20 GPT Image 2.5 Sunburst calls at 6 credits. Itemised in `costs.json`.
