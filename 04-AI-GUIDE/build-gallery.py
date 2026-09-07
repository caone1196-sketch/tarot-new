#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quét thư mục cards/*.png → sinh gallery tĩnh (index.html) + cards/manifest.json.

Chạy lại bất cứ lúc nào sau khi sinh thêm lá:
    python 04-AI-GUIDE/build-gallery.py
"""
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CARDS = ROOT / "cards"

MAJOR_VN = {
    "00-fool": "Kẻ Ngây Thơ", "01-magician": "Pháp Sư", "02-priestess": "Nữ Tư Tế",
    "03-empress": "Nữ Hoàng", "04-emperor": "Hoàng Đế", "05-hierophant": "Giáo Hoàng",
    "06-lovers": "Tình Nhân", "07-chariot": "Chiến Xa", "08-strength": "Sức Mạnh",
    "09-hermit": "Ẩn Sĩ", "10-wheel": "Bánh Xe Số Phận", "11-justice": "Công Lý",
    "12-hanged": "Kẻ Treo Ngược", "13-death": "Tử Thần", "14-temperance": "Tiết Chế",
    "15-devil": "Ma Quỷ", "16-tower": "Tòa Tháp", "17-the-star": "Ngôi Sao",
    "18-moon": "Mặt Trăng", "19-sun": "Mặt Trời", "20-judgement": "Phán Xét",
    "21-world": "Thế Giới",
}
SUIT_VN = {"wands": "Gậy", "cups": "Chén", "swords": "Kiếm", "pentacles": "Xu"}
RANK_VN = {"ace": "Át", "02": "Hai", "03": "Ba", "04": "Bốn", "05": "Năm", "06": "Sáu",
           "07": "Bảy", "08": "Tám", "09": "Chín", "10": "Mười",
           "page": "Học Trò", "knight": "Kỵ Sĩ", "queen": "Hoàng Hậu", "king": "Vua"}

ORDER = list(MAJOR_VN) + [
    f"{s}-{r}" for s in SUIT_VN for r in
    ["ace", "02", "03", "04", "05", "06", "07", "08", "09", "10",
     "page", "knight", "queen", "king"]
]


def vn_name(slug: str) -> str:
    if slug in MAJOR_VN:
        return MAJOR_VN[slug]
    suit, rank = slug.split("-")
    return f"{RANK_VN[rank]} {SUIT_VN[suit]}"


def png_size(path: Path):
    """Đọc kích thước PNG từ header (không cần Pillow)."""
    with path.open("rb") as f:
        head = f.read(24)
    if head[:8] == b"\x89PNG\r\n\x1a\n":
        w = int.from_bytes(head[16:20], "big")
        h = int.from_bytes(head[20:24], "big")
        return w, h
    return None, None


def scene_line(slug: str) -> str:
    """Trích 1 câu bối cảnh từ cards.json để hiển thị dưới mỗi lá."""
    try:
        data = json.loads((ROOT / "cards.json").read_text(encoding="utf-8"))
        for c in data["cards"]:
            if c["slug"] == slug:
                return c.get("scene", "")
    except Exception:
        pass
    return ""


def main():
    files = sorted(p.name for p in CARDS.glob("*.png"))
    files.sort(key=lambda n: ORDER.index(n[:-4]) if n[:-4] in ORDER else 999)

    cards = []
    for name in files:
        slug = name[:-4]
        w, h = png_size(CARDS / name)
        cards.append({
            "slug": slug,
            "file": f"cards/{name}",
            "title": slug.split("-", 1)[1].upper().replace("-", " ")
            if slug not in MAJOR_VN else MAJOR_VN[slug],
            "title_en": TITLE_EN.get(slug, ""),
            "title_vn": vn_name(slug),
            "width": w,
            "height": h,
            "scene": scene_line(slug),
            "prompt": f"cards/prompts/{slug}.txt"
            if (CARDS / "prompts" / f"{slug}.txt").exists() else None,
        })

    (CARDS / "manifest.json").write_text(
        json.dumps({"deck": "Sensual Tarot 78", "generated": now(), "cards": cards},
                   ensure_ascii=False, indent=2),
        encoding="utf-8")

    html = HTML.replace("/*DATA*/", json.dumps(
        {"cards": cards, "total": 78, "generated": now()}, ensure_ascii=False))
    (ROOT / "index.html").write_text(html, encoding="utf-8")
    print(f"✅ index.html + cards/manifest.json — {len(cards)}/{78} lá")


def now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")


# ---- lấy tên tiếng Anh chuẩn từ prompts-full.json ----
try:
    _p = json.loads((ROOT / "prompts-full.json").read_text(encoding="utf-8"))["prompts"]
    TITLE_EN = {x["slug"]: x["title"] for x in _p}
except Exception:
    TITLE_EN = {}

HTML = r"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Sensual Tarot — Gallery</title>
<style>
  :root{ --gold:#c9a227; --gold-dim:#8a6f1e; --ink:#0b0a0f; --panel:#14121b; }
  *{box-sizing:border-box}
  body{margin:0;background:radial-gradient(1200px 700px at 50% -10%,#1d1726 0%,var(--ink) 60%);
       color:#e8e2d4;font-family:"Iowan Old Style",Georgia,"Times New Roman",serif}
  header{text-align:center;padding:44px 20px 26px;position:relative}
  header::after{content:"";position:absolute;left:50%;transform:translateX(-50%);bottom:0;
       width:min(560px,80%);height:1px;background:linear-gradient(90deg,transparent,var(--gold-dim),transparent)}
  h1{margin:0;font-size:clamp(28px,5vw,46px);letter-spacing:.14em;text-transform:uppercase;
     color:var(--gold);text-shadow:0 2px 18px rgba(201,162,39,.25)}
  .sub{margin:12px 0 0;color:#9b9284;letter-spacing:.28em;font-size:12px;text-transform:uppercase}
  .count{margin:18px 0 0;color:#b9ae97;font-size:14px}
  .bar{width:min(320px,70%);height:6px;margin:14px auto 0;border:1px solid #3a3350;border-radius:99px;overflow:hidden}
  .bar i{display:block;height:100%;background:linear-gradient(90deg,var(--gold-dim),var(--gold))}
  .cards{display:grid;gap:34px;padding:46px 24px 70px;justify-content:center;
         grid-template-columns:repeat(auto-fill,minmax(260px,1fr));max-width:1240px;margin:0 auto}
  figure{margin:0;text-align:center}
  .frame{border-radius:10px;overflow:hidden;box-shadow:0 18px 50px rgba(0,0,0,.65),0 0 0 1px #2c2740;
         background:#000;transition:transform .28s ease,box-shadow .28s ease;cursor:zoom-in}
  .frame:hover{transform:translateY(-6px) scale(1.02);box-shadow:0 26px 64px rgba(0,0,0,.8),0 0 0 1px var(--gold-dim)}
  img{display:block;width:100%;height:auto}
  figcaption{margin-top:14px}
  .en{color:var(--gold);letter-spacing:.16em;font-size:12px;text-transform:uppercase}
  .vn{color:#cfc6b4;font-size:15px;margin-top:4px}
  .meta{color:#7d7466;font-size:11px;margin-top:6px;letter-spacing:.06em}
  .scene{color:#8d8574;font-size:12px;max-width:34ch;margin:8px auto 0;line-height:1.5;font-style:italic}
  .dl{display:inline-block;margin-top:8px;color:#6f8fbf;font-size:11px;text-decoration:none;letter-spacing:.08em}
  .dl:hover{text-decoration:underline}
  .empty{text-align:center;color:#6b6455;padding:60px;font-style:italic}
  /* lightbox */
  #lb{position:fixed;inset:0;background:rgba(6,5,9,.94);display:none;place-items:center;z-index:50;padding:24px}
  #lb.on{display:grid}
  #lb img{max-height:88vh;max-width:min(92vw,620px);border-radius:8px;box-shadow:0 0 80px rgba(0,0,0,.9)}
  #lb .cap{margin-top:14px;text-align:center;color:var(--gold);letter-spacing:.2em;font-size:13px;text-transform:uppercase}
  #lb .hint{text-align:center;color:#6b6455;font-size:11px;margin-top:6px}
  footer{text-align:center;color:#5c5548;font-size:11px;padding:0 20px 50px;letter-spacing:.1em}
</style>
</head>
<body>
<header>
  <h1>Sensual Tarot</h1>
  <p class="sub">Full-bleed · v5 · 78 lá</p>
  <p class="count"><span id="n">0</span> / 78 lá đã hoàn thành</p>
  <div class="bar"><i id="bar" style="width:0%"></i></div>
</header>
<main class="cards" id="grid"></main>
<footer id="foot"></footer>

<div id="lb"><div>
  <img id="lbimg" alt=""><div class="cap" id="lbcap"></div>
  <div class="hint">click / ESC để đóng</div>
</div></div>

<script>
const DATA = /*DATA*/;
const grid = document.getElementById('grid');
const pct = Math.round(DATA.cards.length / DATA.total * 100);
document.getElementById('n').textContent = DATA.cards.length;
document.getElementById('bar').style.width = pct + '%';
document.getElementById('foot').textContent =
  'Sinh ' + DATA.generated + ' · prompt nguồn: prompts-full.json · tỉ lệ 7:12 full-bleed';

if (!DATA.cards.length) {
  grid.innerHTML = '<p class="empty">Chưa có lá nào. Chạy: python 04-AI-GUIDE/build-gallery.py</p>';
}
for (const c of DATA.cards) {
  const f = document.createElement('figure');
  const size = c.width ? c.width + '×' + c.height : '';
  const src = c.file + '?v=' + encodeURIComponent(DATA.generated);
  f.innerHTML =
    '<div class="frame"><img loading="lazy" src="' + src + '" alt="' + c.title_en + '"></div>' +
    '<figcaption>' +
      '<div class="en">' + c.title_en + '</div>' +
      '<div class="vn">' + c.title_vn + '</div>' +
      '<div class="meta">' + c.slug + (size ? ' · ' + size : '') + '</div>' +
      (c.scene ? '<div class="scene">' + c.scene.slice(0, 150) + (c.scene.length > 150 ? '…' : '') + '</div>' : '') +
      (c.prompt ? '<a class="dl" href="' + c.prompt + '" download>prompt đã dùng ↓</a>' : '') +
    '</figcaption>';
  f.querySelector('.frame').onclick = () => open(c);
  grid.appendChild(f);
}

const lb = document.getElementById('lb');
function open(c){
  document.getElementById('lbimg').src = c.file + '?v=' + encodeURIComponent(DATA.generated);
  document.getElementById('lbcap').textContent = c.title_en + ' — ' + c.title_vn;
  lb.classList.add('on');
}
lb.onclick = () => lb.classList.remove('on');
document.addEventListener('keydown', e => { if (e.key === 'Escape') lb.classList.remove('on'); });
</script>
</body>
</html>
"""

if __name__ == "__main__":
    main()
