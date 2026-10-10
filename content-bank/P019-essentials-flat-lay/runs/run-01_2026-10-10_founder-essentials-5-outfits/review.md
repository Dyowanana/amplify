# Review · P019 run-01 · founder essentials, 5 outfits

## 7-point format check
| Point | Source | This run | Match |
|---|---|---|---|
| Structure | 1 slide, title + 13 cut-outs, outfit stacked on one side | 1 slide, title + 11 (8 cut-outs, 3 widgets), outfit stacked on one side | yes |
| Hook | `<identity> Essentials` | `founder essentials` | yes |
| Camera & motion | packshots + UI snippets on white | same | yes |
| Pacing | 2-word title, small UI text | same | yes |
| Text overlay | bold grotesk title, centred, near-black | Inter Bold (SF Pro look-alike), centred, #111, lowercase | yes (lowercase by owner rule) |
| Audio | music, no voiceover | add a trending sound in TikTok | yes |
| Arc | "that's me" recognition + in-joke widgets | same: usage limit, payment ping, mrr up | yes |

## Measured checks
- `originality.py` (the 5 boards run as slides 1 to 5): words **pass** on every board, raw overlap 13%, content words 18%, longest shared run 1 word ("essentials"; shared words also "mrr", "usage", "8"). Images **pass**: closest 24 bits (near-duplicate at 10 or less). Hook overlap **50%**, flagged FAIL by the tool: the shared word is the formula word "essentials", which the skill allows to stay word for word; the identity word is new. Verdict in `output/originality.json` is FAIL for that reason only.
- `measure.py check --record` on all 5 records: 0 box problems (`raw/boxcheck/`).
- `caption.py check`: PASS (none, 104 characters, 4 hashtags).
- Punctuation and case on the board checked by eye: lowercase, no dashes, colons or semicolons.

## Redone during the run
- Smartwatch: the first one had a square face, crown and woven loop that read as a real brand's watch. Regenerated as a round, generic watch (`raw/art/watch_rejected_looks-like-a-real-brand.png`).
- Sage pants (girl-3): the model drew the whole two-piece set, so the top showed twice. Regenerated as pants only.
- Layout: with the source's layout (outfit on the left) the navy fleece board hit 10 bits on dhash, the near-duplicate line, because a big dark top sat where the source's black hoodie sits. The fleece was redone in dusty blue (`g2_top_rejected_…`) and the whole layout mirrored (outfit on the right). All five boards now sit at 24 to 31 bits.

## Models used
GPT Image 2.5 Sunburst only (23 calls, 138 credits). On the approved list.

## Known limits
- The white shirt on girl-2 is white on white. It reads, but it's the lightest item on any board.
- The laptop is generic but still close to a familiar aluminium laptop shape; there's no logo.
- Widget numbers are invented and the widgets are not any real app's UI.

## Tester ratings
Pending.

## Owner verdict
Pending.
