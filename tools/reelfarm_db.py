#!/usr/bin/env python3
"""Slideshow format database: one folder per niche, built from what the ReelFarm database shows.

Usage:
  reelfarm_db.py build database/niches/<slug>    download the slides, write slideshows.json and README.md
  reelfarm_db.py index                           rewrite database/README.md (every niche, its status and counts)
  reelfarm_db.py status <slug> approved|pending|needs-more [--note "…"]
  reelfarm_db.py keep <slug> "1-9" [--note "…"]  keep only those numbers (the owner's review), renumbered

Input: <niche folder>/reelfarm_raw.json, read from the logged-in ReelFarm database page in the browser pane
(the page holds each card's profile and slideshow data; see "How a niche is collected" in database/README.md).
Fields per slideshow: account, nickname, followers, following, account and audience regions, what the account
sells and through what (product medium), link in bio, bio, views, likes, saves, engagement rate (likes / views,
the same formula ReelFarm shows), and every slide image.

Output per niche:
  slides/<account>_<i>/<k>.jpg    every slide, downloaded from ReelFarm's image host, re-saved as JPEG (max 720 wide, keeps the repo small)
  slideshows.json                 the normalised records with local slide paths
  README.md                       the gallery: cover, numbers, account card and the slide strip for each slideshow
  _preview.jpg                    first slide of each, for the owner's review (not committed)

ReelFarm does not show the TikTok post link, only the account. `post_url` stays null until it is matched.

A niche can also hold slideshows the owner picked as TikTok links: <niche folder>/tiktok_raw.json, read from the
logged-in TikTok post and profile pages in the browser pane ({"niche", "collected", "rule", "profiles": {account:
{nickname, followers, following, bio, link_in_bio, sells, product_medium}}, "posts": [{account, post_id, posted,
caption, views, likes, saves, comments, shares, app, images}]}, counts as exact numbers). A niche can have only this
file. These posts are all kept (no `want` cap), get `source: tiktok`, a `post_url` and their slides under
slides/<account>_<post id>/, and join the ReelFarm ones in most-likes order.
"""
import argparse
import io
import json
import re
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import date
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
DB = ROOT / "database"
CDN = "https://dh8vpkzn300g4.cloudfront.net/"
UA = {"User-Agent": "Mozilla/5.0", "Referer": "https://reel.farm/"}


S3 = "https://reelfarm-slideshow-images.s3.us-west-1.amazonaws.com/"


def url_of(acct, img):
    """Full image URL. The collector shortens ReelFarm's two hosts: a bare file name is on the CDN under the account,
    's3:<account>/<file>' is on the S3 bucket."""
    if img.startswith("http"):
        return img
    if img.startswith("s3:"):
        return S3 + img[3:]
    if img.startswith("s:"):  # compact: s:<id>.<ext> = S3 bucket, <account>/slideshow_<id>.<ext>
        return f"{S3}{acct}/slideshow_{img[2:]}"
    if img.startswith("c:"):  # compact: c:<id>.<ext> = CDN, <account>/slideshow_<id>.<ext>
        return f"{CDN}{acct}/slideshow_{img[2:]}"
    return f"{CDN}{acct}/{img}"


def expand(raw):
    """Compact collector output: account details once in 'profiles', posts carry only their own numbers."""
    prof = raw.get("profiles")
    if prof:
        for key in ("posts", "reserve"):
            raw[key] = [{**prof[p["account"]], **p} for p in raw.get(key, [])]
    return raw


def fetch(url, out):
    """Download one slide and re-save it as JPEG. None when the host refuses it or the format can't be read
    (some ReelFarm copies are TikTok's own 'vvic' image format, which no browser shows either)."""
    if out.exists():
        return out.stat().st_size
    try:
        data = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60).read()
        im = Image.open(io.BytesIO(data)).convert("RGB")
    except Exception:
        return None
    if im.width > 720:
        im = im.resize((720, round(im.height * 720 / im.width)), Image.LANCZOS)
    out.parent.mkdir(parents=True, exist_ok=True)
    im.save(out, "JPEG", quality=82, optimize=True, progressive=True)
    return out.stat().st_size


def num(s):
    if not s or not isinstance(s, str):
        return 0
    t = s.lower().replace(",", "").strip()
    try:
        v = float(re.sub(r"[^0-9.]", "", t))
    except ValueError:
        return 0
    return v * 1e6 if "m" in t else v * 1e3 if "k" in t else v


def clean(v):
    return None if v in (None, "", "None", "none", "No product", "null", "Analysis failed") else v


def short(n):
    """TikTok's exact counts in ReelFarm's display style (585.0K, 2.9M, 124), so every record reads the same."""
    n = int(n or 0)
    return f"{n / 1e6:.1f}M" if n >= 1e6 else f"{n / 1e3:.1f}K" if n >= 1e3 else str(n)


def pct(a, b):
    return f"{num(a) / num(b) * 100:.1f}%" if num(b) else None


def download(folder, d, urls, acct):
    """Download one slideshow into <folder>/<d>/NN.jpg. Returns (slide paths, sizes), or (None, failures) when any slide fails."""
    got = [(img, f"{d}/{k:02}.jpg") for k, img in enumerate(urls, 1)]
    with ThreadPoolExecutor(8) as ex:
        res = list(ex.map(lambda j: fetch(url_of(acct, j[0]), folder / j[1]), got))
    if not got or None in res:
        for _, s_ in got:
            (folder / s_).unlink(missing_ok=True)
        return None, res.count(None) if got else 0
    return [s_ for _, s_ in got], res


def build(folder):
    rf_p, tt_p = folder / "reelfarm_raw.json", folder / "tiktok_raw.json"
    raw = expand(json.loads(rf_p.read_text(encoding="utf-8"))) if rf_p.exists() else None
    tt = json.loads(tt_p.read_text(encoding="utf-8")) if tt_p.exists() else None
    meta_p = folder / "niche.json"
    meta = json.loads(meta_p.read_text(encoding="utf-8")) if meta_p.exists() else {"status": "pending", "notes": []}
    if raw:
        meta.update(niche=raw["niche"], slug=folder.name,
                    source=raw.get("source") or "reel.farm/dashboard/database/niche/" + folder.name,
                    reelfarm_total=raw["total"], sort=raw["sort"], scanned=raw["scanned"], collected=str(date.today()),
                    rule=raw.get("rule") or "top by likes from the first pages, at most 2 slideshows per account, duplicates removed")
    else:
        meta.update(niche=tt["niche"], slug=folder.name, source="TikTok links picked by the owner", reelfarm_total=None,
                    sort="likes-most", scanned=None, collected=tt["collected"], rule=tt["rule"])
    want = meta.get("want") or (raw or {}).get("want", 25)
    removed = set(meta.get("removed", []))
    records, sizes, broken = [], [], []
    for p in (raw["posts"] + raw.get("reserve", [])) if raw else []:
        if len(records) >= want:
            break
        d = f"slides/{p['account']}_{p['slideshow_index']}"
        if d.split("/")[1] in removed:
            continue
        slides, res = download(folder, d, p["images"], p["account"])
        if not slides:
            broken.append(f"@{p['account']} (ReelFarm rank {p['rank']}): {res} of {len(p['images'])} slides unreadable on ReelFarm")
            continue
        sizes += res
        records.append({
            "n": 0, "source": "reelfarm", "reelfarm_rank": p["rank"], "account": p["account"], "nickname": p["nickname"],
            "account_url": f"https://www.tiktok.com/@{p['account']}", "post_url": None, "posted": None, "caption": None,
            "followers": p["followers"], "following": p["following"],
            "account_region": p["account_region"], "audience_regions": p["audience_regions"],
            "sells": clean(p["sells"]), "product_medium": clean(p["product_medium"]),
            "link_in_bio": p["link_in_bio"], "bio": p["bio"],
            "views": p["views"], "likes": p["likes"], "saves": p["saves"], "comments": None, "shares": None,
            "engagement_rate": p["engagement_rate"], "save_rate": pct(p["saves"], p["views"]),
            "app": p.get("app"), "found_in": p.get("found_in"),
            "slide_count": len(slides), "slides": slides,
            "source_images": [url_of(p["account"], img) for img in p["images"]],
        })
    rf_count = len(records)
    # Posts the owner picked as TikTok links: all kept (no cap), slides saved under <account>_<post id>.
    # TikTok's image links expire after a few days, so a rebuild relies on the slides already on disk.
    for p in tt["posts"] if tt else []:
        a = {**tt["profiles"][p["account"]], **p}
        d = f"slides/{a['account']}_{a['post_id']}"
        if d.split("/")[1] in removed:
            continue
        slides, res = download(folder, d, a["images"], a["account"])
        if not slides:
            broken.append(f"@{a['account']} post {a['post_id']}: {res} of {len(a['images'])} slides could not be downloaded from TikTok")
            continue
        sizes += res
        v, l, s_ = short(a["views"]), short(a["likes"]), short(a["saves"])
        records.append({
            "n": 0, "source": "tiktok", "reelfarm_rank": None, "account": a["account"], "nickname": a["nickname"],
            "account_url": f"https://www.tiktok.com/@{a['account']}", "post_url": f"https://www.tiktok.com/@{a['account']}/photo/{a['post_id']}",
            "posted": a["posted"], "caption": a["caption"],
            "followers": short(a["followers"]), "following": short(a["following"]),
            "account_region": None, "audience_regions": None,
            "sells": a.get("sells"), "product_medium": a.get("product_medium"),
            "link_in_bio": a.get("link_in_bio"), "bio": a.get("bio") or None,
            "views": v, "likes": l, "saves": s_, "comments": short(a["comments"]), "shares": short(a["shares"]),
            "engagement_rate": f"{a['likes'] / a['views'] * 100:.1f}%" if a["views"] else None,
            "save_rate": f"{a['saves'] / a['views'] * 100:.1f}%" if a["views"] else None,
            "app": a.get("app"), "found_in": "owner's TikTok link",
            "slide_count": len(slides), "slides": slides, "source_images": a["images"],
        })
    if len(records) > rf_count:  # owner's picks join ReelFarm's "most likes" order
        records.sort(key=lambda r: -num(r["likes"]))
    for i, r in enumerate(records, 1):
        r["n"] = i
    meta.update(slideshows=len(records), accounts=len({r["account"] for r in records}), slides=sum(r["slide_count"] for r in records),
                from_tiktok_links=len(records) - rf_count, size_mb=round(sum(sizes) / 1e6, 1), skipped_broken=broken)
    if raw and rf_count < want:
        print(f"  only {rf_count} of {want} from ReelFarm: add more reserve posts")
    (folder / "slideshows.json").write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")
    meta_p.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    (folder / "README.md").write_text(readme(meta, records), encoding="utf-8")
    preview(folder, records)
    print(f"{folder.name}: {len(records)} slideshows, {meta['accounts']} accounts, {meta['slides']} slides, {meta['size_mb']} MB")
    for b in broken:
        print("  skipped", b)


def preview(folder, records):
    """_preview.jpg: the first slide of every slideshow with its number, account and numbers, for the owner's review."""
    from PIL import ImageDraw, ImageFont
    W, H, cols = 180, 320, 9
    rows = (len(records) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * W, max(1, rows) * (H + 44)), "white")
    d = ImageDraw.Draw(sheet)
    font = ImageFont.truetype(str(ROOT / "assets" / "fonts" / "Inter-VF.ttf"), 13)
    for i, r in enumerate(records):
        im = Image.open(folder / r["slides"][0]).convert("RGB")
        im.thumbnail((W - 6, H))
        x, y = (i % cols) * W, (i // cols) * (H + 44)
        sheet.paste(im, (x + 3 + (W - 6 - im.width) // 2, y + (H - im.height) // 2))
        d.text((x + 4, y + H + 2), f"{r['n']}. @{r['account'][:20]}", fill="black", font=font)
        d.text((x + 4, y + H + 20), f"{r['views']} views · {r['likes']} · {r['slide_count']}sl", fill=(90, 90, 90), font=font)
    sheet.save(folder / "_preview.jpg", quality=85)


def md(s):
    return (s or "").replace("|", "\\|").replace("\n", " ")


def readme(meta, records):
    title = meta["niche"].title()
    picks = meta.get("from_tiktok_links") or 0
    if meta.get("reelfarm_total"):
        where = (f"from ReelFarm ({meta['reelfarm_total']} "
                 f"{'candidates' if meta.get('source', '').find('/medium/') >= 0 else 'in this niche there'}, sorted by most likes; {meta['rule']})")
        if picks:
            where += f", plus {picks} from TikTok links the owner picked"
    else:
        where = f"from TikTok links the owner picked ({meta['rule']})"
    out = [f"# {title}", "",
           f"**Status:** {meta['status']} · {meta['slideshows']} slideshows from {meta['accounts']} accounts · "
           f"{meta['slides']} slides · collected {meta['collected']} {where}.", ""]
    for n in meta.get("notes", []):
        out.append(f"> {n}")
    out += ["", "## Overview", "",
            "| # | Cover | Account | Views | Likes | Saves | ER | Slides | Sells | Medium |",
            "|---|---|---|---|---|---|---|---|---|---|"]
    for r in records:
        out.append(f"| [{r['n']}](#{r['n']}-{r['account'].replace('.', '').replace('_', '')}) | <img src=\"{r['slides'][0]}\" width=\"70\"> "
                   f"| [@{r['account']}]({r['account_url']}) | {r['views']} | {r['likes']} | {r['saves']} | {r['engagement_rate']} "
                   f"| {r['slide_count']} | {md(r['sells']) or '—'} | {md(r['product_medium']) or '—'} |")
    out += ["", "## Slideshows", ""]
    for r in records:
        out += [f"### {r['n']}. @{r['account']}", "",
                f"**{r['views']}** views · **{r['likes']}** likes · **{r['saves']}** saves · ER **{r['engagement_rate']}** · save rate {r['save_rate']} · {r['slide_count']} slides"
                + (f" · {r['comments']} comments · {r['shares']} shares" if r.get("comments") else ""), ""]
        if r.get("post_url"):
            out += [f"[Open the post on TikTok]({r['post_url']}) · posted {r['posted']}", ""]
        out += [f"[@{r['account']}]({r['account_url']}) ({md(r['nickname'])}) · {r['followers']} followers · {r['following']} following"
                + (f" · account region {r['account_region']}" if r["account_region"] else ""), ""]
        if r["bio"]:
            out += [f"> {md(r['bio'])}", ""]
        facts = []
        if r["sells"]:
            facts.append(f"Sells: {md(r['sells'])}")
        if r["product_medium"]:
            facts.append(f"Medium: {md(r['product_medium'])}")
        if r.get("found_in") and r.get("source") != "tiktok":
            facts.append(f"From ReelFarm's {r['found_in'].replace('-', ' ')} page")
        if r.get("app"):
            facts.append(f"Promotes: {md(r['app'])}")
        if r["link_in_bio"]:
            facts.append(f"Link in bio: {md(r['link_in_bio'])}")
        if r["audience_regions"]:
            facts.append("Audience: " + ", ".join(r["audience_regions"]))
        if facts:
            out += [" · ".join(facts), ""]
        out += [" ".join(f'<img src="{s}" width="120">' for s in r["slides"]), ""]
    return "\n".join(out) + "\n"


CB = ROOT / "content-bank"


def pillars():
    """Front matter, link and a cover image for every template in content-bank/ (P###)."""
    import yaml
    out = {}
    for f in sorted(CB.glob("P[0-9][0-9][0-9]-*/pillar.md")):
        m = re.match(r"---\n(.*?)\n---\n", f.read_text(encoding="utf-8").replace("\r\n", "\n"), re.S)
        fm = yaml.safe_load(m.group(1)) if m else {}
        imgs = sorted(i for i in (f.parent / "originals").rglob("*") if i.suffix.lower() in (".jpg", ".jpeg", ".png", ".webp")
                      and "boxcheck" not in i.parts and i.name != "sheet.jpg")
        cover = (next((i for i in imgs if i.parent.name == "slides"), None)
                 or next((i for i in imgs if i.parent.name == "frames"), None) or (imgs[0] if imgs else None))
        out[fm.get("id", f.parent.name[:4])] = {**fm, "folder": f.parent.name, "cover": cover}
    return out


def categories(niche_meta):
    """database/categories/<slug>.md: each business type with its ReelFarm niches and the templates already studied."""
    cats = json.loads((DB / "categories.json").read_text(encoding="utf-8"))
    ps = pillars()
    (DB / "categories").mkdir(exist_ok=True)
    for c in cats:
        out = [f"# {c['name']}", "", f"**Brands of this type on Amplify:** {c['brands']} · {c['sell']}", ""]
        if c.get("gap"):
            out += [f"> ⚠️ {c['gap']}", ""]
        if c.get("notes"):
            out += [f"> {c['notes']}", ""]
        out += ["## Slideshow niches", "", "| Niche | Status | Slideshows | Accounts |", "|---|---|---|---|"]
        for n in c["niches"]:
            m = niche_meta.get(n)
            out.append(f"| [{m['niche']}](../niches/{n}/README.md) | {m['status']} | {m['slideshows']} | {m['accounts']} |" if m
                       else f"| {n.replace('-', ' ')} | not collected yet | | |")
        for key, title in (("made_for_it", "Templates already studied for this type"), ("works_with_a_tweak", "Templates that also work, with a tweak")):
            out += ["", f"## {title}", "", "| | Template | Type | Confidence | Status | What it is |", "|---|---|---|---|---|---|"]
            for pid in c["templates"].get(key, []):
                pl = ps.get(pid)
                if not pl:
                    continue
                img = f'<img src="../../{pl["cover"].relative_to(ROOT).as_posix()}" width="70">' if pl["cover"] else ""
                out.append(f"| {img} | [{pid} {md(pl.get('name'))}](../../content-bank/{pl['folder']}/pillar.md) | {pl.get('type')} "
                           f"| {pl.get('confidence')} | {pl.get('status')} | {md(pl.get('summary'))} |")
        (DB / "categories" / f"{c['slug']}.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    return cats


def index():
    rows = []
    for f in sorted((DB / "niches").glob("*/niche.json")):
        m = json.loads(f.read_text(encoding="utf-8"))
        rows.append(m)
    status_order = {"approved": 0, "needs-more": 1, "pending": 2}
    cats = categories({m["slug"]: m for m in rows})
    out = ["# Slideshow format database", "",
           "TikTok slideshows that performed, grouped by niche, with the account behind each one, its numbers and every slide, "
           "so any brand can pick a niche and remake a format. Approved niches are reviewed by the owner.", "",
           "Building on this data? The files and fields are explained in [DEVELOPERS.md](DEVELOPERS.md).", "",
           "## By business type", "",
           "What Amplify's users sell, with the ReelFarm niches and the templates already studied (`content-bank/`) for each.", "",
           "| Business type | Brands | Niches collected | Templates studied | Gap |", "|---|---|---|---|---|"]
    done = {m["slug"] for m in rows}
    for c in cats:
        got = [n for n in c["niches"] if n in done]
        out.append(f"| [{c['name']}](categories/{c['slug']}.md) | {c['brands']} | {len(got)} of {len(c['niches'])} "
                   f"| {len(c['templates'].get('made_for_it', []))} (+{len(c['templates'].get('works_with_a_tweak', []))} with a tweak) "
                   f"| {'⚠️ ' + c['gap'].split(':')[0].split('.')[0] if c.get('gap') else ''} |")
    out += ["", "## All niches", "",
           "| Niche | Status | Slideshows | Accounts | Slides | Collected | Notes |", "|---|---|---|---|---|---|---|"]
    for m in sorted(rows, key=lambda m: (status_order.get(m["status"], 3), m["niche"])):
        out.append(f"| [{m['niche']}](niches/{m['slug']}/README.md) | {m['status']} | {m['slideshows']} | {m['accounts']} | {m['slides']} "
                   f"| {m['collected']} | {md(' '.join(m.get('notes', [])))} |")
    out += ["", "## How a niche is collected", "",
            "1. Open the niche in the ReelFarm database (logged in, browser pane). The page holds each card's profile and slideshow data.",
            "2. Take the first pages sorted by most likes, keep at most 2 slideshows per account, drop duplicates, stop at 25.",
            "3. Save that as `niches/<slug>/reelfarm_raw.json`, then `tools/reelfarm_db.py build niches/<slug>` downloads every slide and writes the page.",
            "4. The owner reviews the niche page: approve, ask for more, or name slideshows to remove. Only then is it pushed.", "",
            "ReelFarm shows the account, not the TikTok post link, so `post_url` is empty for ReelFarm slideshows.", "",
            "Slideshows the owner picks as TikTok links go in `niches/<slug>/tiktok_raw.json` (read from the logged-in post and profile "
            "pages: exact stats, caption, posting date, bio and link in bio) and are built the same way, with `source: tiktok` and a `post_url`."]
    (DB / "README.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"database/README.md: {len(rows)} niches")


def set_status(slug, status, note):
    p = DB / "niches" / slug / "niche.json"
    m = json.loads(p.read_text(encoding="utf-8"))
    m["status"] = status
    if note:
        m.setdefault("notes", []).append(note)
    p.write_text(json.dumps(m, ensure_ascii=False, indent=2), encoding="utf-8")
    records = json.loads((p.parent / "slideshows.json").read_text(encoding="utf-8"))
    (p.parent / "README.md").write_text(readme(m, records), encoding="utf-8")
    index()


def keep(slug, spec, note):
    """Keep only the slideshows numbered in spec ("1-9", "1,3,5-8"); the rest are removed for good (their slides are
    deleted and a rebuild won't bring them back), and the kept ones are renumbered."""
    folder = DB / "niches" / slug
    m = json.loads((folder / "niche.json").read_text(encoding="utf-8"))
    records = json.loads((folder / "slideshows.json").read_text(encoding="utf-8"))
    nums = set()
    for part in spec.split(","):
        a, _, b = part.partition("-")
        nums |= set(range(int(a), int(b or a) + 1))
    kept = [r for r in records if r["n"] in nums]
    for r in records:
        if r["n"] not in nums:
            d = Path(r["slides"][0]).parent.name
            m.setdefault("removed", []).append(d)
            for s_ in r["slides"]:
                (folder / s_).unlink(missing_ok=True)
            (folder / "slides" / d).rmdir()
    for i, r in enumerate(kept, 1):
        r["n"] = i
    m.update(want=len(kept), slideshows=len(kept), accounts=len({r["account"] for r in kept}),
             slides=sum(r["slide_count"] for r in kept))
    if note:
        m.setdefault("notes", []).append(note)
    (folder / "slideshows.json").write_text(json.dumps(kept, ensure_ascii=False, indent=2), encoding="utf-8")
    (folder / "niche.json").write_text(json.dumps(m, ensure_ascii=False, indent=2), encoding="utf-8")
    (folder / "README.md").write_text(readme(m, kept), encoding="utf-8")
    preview(folder, kept)
    index()
    print(f"{slug}: kept {len(kept)} of {len(records)}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    b = sub.add_parser("build"); b.add_argument("folder", type=Path)
    sub.add_parser("index")
    s = sub.add_parser("status"); s.add_argument("slug"); s.add_argument("status", choices=["approved", "pending", "needs-more"]); s.add_argument("--note")
    k = sub.add_parser("keep"); k.add_argument("slug"); k.add_argument("spec", help='e.g. "1-9" or "1,3,5-8"'); k.add_argument("--note")
    a = ap.parse_args()
    if a.cmd == "build":
        build(a.folder if a.folder.is_absolute() else ROOT / a.folder)
        index()
    elif a.cmd == "index":
        index()
    elif a.cmd == "keep":
        keep(a.slug, a.spec, a.note)
    else:
        set_status(a.slug, a.status, a.note)


if __name__ == "__main__":
    sys.exit(main())
