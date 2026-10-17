// Run in the browser pane on a ReelFarm niche page (reel.farm/dashboard/database/niche/<slug>), logged in.
// Reads the cards' own data from the page (no extra requests), sorted by most likes as the page shows it,
// keeps at most 2 slideshows per account, drops duplicates, and returns the JSON for
// database/niches/<slug>/reelfarm_raw.json (then: tools/reelfarm_db.py build database/niches/<slug>).
// Usage in the page: await __collect(25, 10, 3)  -> want, reserve, pages to scan (35 per page)
window.__rf = {
  props() {
    const el = document.querySelector('main div[class*=cursor-pointer][class*=aspect]');
    const fk = Object.keys(el).find(k => k.startsWith('__reactFiber'));
    let f = el[fk];
    for (let i = 0; i < 4; i++) f = f.return;
    return f.memoizedProps;
  },
  num(e) {
    if (!e || typeof e !== 'string') return 0;
    const t = e.toLowerCase().replace(/,/g, '').trim(), s = parseFloat(t);
    return isNaN(s) ? 0 : t.includes('m') ? 1e6 * s : t.includes('k') ? 1e3 * s : s;
  },
  rows() {
    const p = this.props();
    return p.currentPosts.map((c, i) => {
      const pr = c.profile, s = c.slideshow;
      return {
        rank: p.startIndex + i + 1, account: pr.unique_id, nickname: pr.nickname,
        followers: pr.follower_count, following: pr.following_count, account_region: pr.region,
        audience_regions: (pr.audience_regions || []).slice(0, 3).map(a => `${a.country} ${a.percentage}`),
        sells: pr.product, product_medium: pr.product_medium, link_in_bio: pr.link_in_bio, bio: pr.signature,
        slideshow_index: c.slideshowIndex, views: s.views, likes: s.likes, saves: s.bookmarks,
        engagement_rate: this.num(s.views) ? (this.num(s.likes) / this.num(s.views) * 100).toFixed(1) + '%' : null,
        slide_count: (s.images || []).length, images: s.images || [],
        account_slideshows_in_db: (pr.recent_slideshows || []).length,
      };
    });
  },
};
window.__collect = async (want = 25, reserve = 10, pages = 3) => {
  const all = [];
  for (let pg = 1; pg <= pages; pg++) {
    if (pg > __rf.props().totalPages) break;
    __rf.props().handlePageChange(pg);
    await new Promise(r => setTimeout(r, 1500));
    all.push(...__rf.rows());
  }
  const per = {}, seen = new Set(), pick = [];
  for (const r of all) {
    const k = r.images[0];
    if (!k || seen.has(k)) continue;
    seen.add(k);
    per[r.account] = (per[r.account] || 0) + 1;
    if (per[r.account] > 2) continue;
    pick.push(r);
    if (pick.length >= want + reserve) break;
  }
  const CDN = 'https://dh8vpkzn300g4.cloudfront.net/', S3 = 'https://reelfarm-slideshow-images.s3.us-west-1.amazonaws.com/';
  const short = r => ({ ...r, images: r.images.map(u => u.startsWith(CDN + r.account + '/') ? u.slice((CDN + r.account + '/').length) : u.startsWith(S3) ? 's3:' + u.slice(S3.length) : u) });
  const p = __rf.props();
  return { niche: p.currentNiche, total: p.totalPosts, sort: p.sortBy, scanned: all.length, want,
           posts: pick.slice(0, want).map(short), reserve: pick.slice(want).map(short) };
};
'ready';
