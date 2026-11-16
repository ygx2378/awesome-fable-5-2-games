#!/usr/bin/env python3
"""检查 aiarcade.games 是否上线了清单里仍缺试玩链接的作品。

用法：
    python3 scripts/sync_play_links.py              # 报告新增试玩页与可能的对应作品
    python3 scripts/sync_play_links.py --json       # 机器可读输出
    python3 scripts/sync_play_links.py --update-snapshot  # 把当前 slug 列表记为基线

只读脚本，不修改 README / CSV。真正的写入由人（或自动化里的 agent）在确认对应关系后完成，
因为 slug 里常带随机后缀（如 black-tide-hdab0j），仅靠字符串匹配会误配。
"""
from __future__ import annotations

import argparse
import csv
import difflib
import json
import re
import sys
import urllib.request
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SNAPSHOT = ROOT / "data" / "play_slugs_snapshot.json"
GAMES_CSV = ROOT / "data" / "games.csv"
SITEMAP = "https://aiarcade.games/sitemap.xml"
PLAY_BASE = "https://aiarcade.games/play/"

STOPWORDS = {
    "the", "a", "an", "of", "and", "for", "to", "in", "on", "at", "with",
    "fable", "game", "games", "demo", "run", "runs",
}


def fetch(url: str, timeout: int = 25) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (compatible; awesome-list-checker)"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8", "replace")


def live_slugs() -> list[str]:
    xml = fetch(SITEMAP)
    slugs = {m.split("/play/")[-1] for m in re.findall(r"https://aiarcade\.games/play/[a-z0-9\-]+", xml)}
    return sorted(slugs)


def tokens(text: str) -> set[str]:
    text = re.sub(r"([a-z])([A-Z])", r"\1 \2", text)
    parts = re.split(r"[^A-Za-z0-9]+|(?<=[a-z])(?=[A-Z])", text.lower())
    return {p for p in parts if p and p not in STOPWORDS and len(p) > 1}


def score(slug: str, name: str) -> float:
    """0–1，越大越像同一款游戏。"""
    flat_slug = slug.replace("-", "")
    flat_name = re.sub(r"[^a-z0-9]", "", name.lower())
    if not flat_name:
        return 0.0
    best = difflib.SequenceMatcher(None, flat_slug, flat_name).ratio()
    if flat_name in flat_slug:
        best = max(best, 0.92)
    nt, st = tokens(name), tokens(slug.replace("-", " "))
    if nt and st:
        overlap = len(nt & st) / len(nt)
        best = max(best, overlap * 0.88)
    return round(best, 3)


def page_title(slug: str) -> str:
    try:
        html = fetch(PLAY_BASE + slug, timeout=20)
    except Exception as exc:  # noqa: BLE001
        return f"<抓取失败: {exc}>"
    m = re.search(r"<title[^>]*>(.*?)</title>", html, re.S)
    if not m:
        return "<无 title>"
    title = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", m.group(1))).strip()
    return title[:120]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true", help="输出 JSON")
    ap.add_argument("--update-snapshot", action="store_true", help="用当前站点状态覆盖基线")
    ap.add_argument("--titles", action="store_true", help="为新增页面抓取网页标题（较慢但更准）")
    args = ap.parse_args()

    live = live_slugs()
    known: list[str] = []
    if SNAPSHOT.exists():
        known = json.loads(SNAPSHOT.read_text(encoding="utf-8")).get("slugs", [])

    rows = list(csv.DictReader(GAMES_CSV.open(encoding="utf-8")))
    pending = [r for r in rows if not (r.get("play_url") or "").strip()]
    used = {r["play_url"].rstrip("/").split("/play/")[-1] for r in rows if (r.get("play_url") or "").strip()}
    fresh = [s for s in live if s not in set(known) and s not in used]

    report = []
    for slug in fresh:
        cands = sorted(((score(slug, p["name"]), p["id"], p["name"]) for p in pending), reverse=True)
        top = [c for c in cands if c[0] >= 0.55][:3]
        item = {"slug": slug, "url": PLAY_BASE + slug, "candidates": [{"score": s, "id": i, "name": n} for s, i, n in top]}
        if args.titles:
            item["title"] = page_title(slug)
        report.append(item)

    out = {
        "date": date.today().isoformat(),
        "live_total": len(live),
        "known_total": len(known),
        "pending_games": [{"id": p["id"], "name": p["name"], "repo": p["repo"]} for p in pending],
        "new_pages": report,
    }

    if args.update_snapshot:
        SNAPSHOT.write_text(
            json.dumps({"date": date.today().isoformat(), "slugs": live}, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        print(f"基线已更新：{len(live)} 个 slug -> {SNAPSHOT.relative_to(ROOT)}")

    if args.json:
        print(json.dumps(out, ensure_ascii=False, indent=2))
        return 0

    print(f"站点在线试玩页：{len(live)}（基线 {len(known)}，已收录 {len(used & set(live))}）")
    print(f"清单中仍缺试玩的游戏：{len(pending)} 款")
    if not report:
        print("\n没有新增试玩页。")
        return 0

    print(f"\n发现 {len(report)} 个新页面：")
    for it in report:
        print(f"\n  {it['slug']}")
        print(f"    {it['url']}")
        if it.get("title"):
            print(f"    标题：{it['title']}")
        if it["candidates"]:
            for c in it["candidates"]:
                print(f"    → 疑似 #{c['id']} {c['name']}（相似度 {c['score']}）")
        else:
            print("    → 未匹配到待补作品，可能是站点独占新作")
    return 0


if __name__ == "__main__":
    sys.exit(main())
