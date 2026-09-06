#!/usr/bin/env python3
"""
Post-render utilities for the deck.

  python3 pipeline/finalize.py convert   # PNG renders -> q92 4:4:4 JPEG, drop the PNG
  python3 pipeline/finalize.py sheet     # build the contact sheet of everything rendered
  python3 pipeline/finalize.py status    # what is rendered / still missing

Why JPEG: 78 cards as full PNG is ~210 MB, over the repo artifact budget. At quality 92 with
no chroma subsampling a 784x1360 card is ~450 KB and visually indistinguishable, so the whole
deck lands around 35 MB.
"""
import json
import sys
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
CARDS = ROOT / "cards"
PIPE = ROOT / "pipeline"

JPEG_OPTS = dict(quality=92, optimize=True, subsampling=0, progressive=True)


def order():
    data = json.loads((PIPE / "prompts.json").read_text(encoding="utf-8"))
    return [c["slug"] for c in data["cards"]], {c["slug"]: c for c in data["cards"]}


def convert():
    n = 0
    for png in sorted(CARDS.glob("*.png")):
        jpg = png.with_suffix(".jpg")
        with Image.open(png) as im:
            im.convert("RGB").save(jpg, **JPEG_OPTS)
        png.unlink()
        n += 1
        print(f"  {png.name} -> {jpg.name} ({jpg.stat().st_size // 1024} KB)")
    print(f"converted {n} file(s)")


def rendered():
    slugs, _ = order()
    return [s for s in slugs if (CARDS / f"{s}.jpg").exists() or (CARDS / f"{s}.png").exists()]


def status():
    slugs, meta = order()
    have = set(rendered())
    print(f"rendered {len(have)}/{len(slugs)}")
    missing = [s for s in slugs if s not in have]
    if missing:
        print("\nstill missing:")
        for s in missing:
            print(f"  {s:22s} {meta[s]['title']}")
    size = sum(f.stat().st_size for f in CARDS.iterdir() if f.is_file())
    print(f"\ncards/ total: {size / 1024 / 1024:.1f} MB")


def check():
    """Flag any card that regressed to the old matted layout.

    Full-bleed cards read ~99% colour coverage; the retired silver-mat layout reads ~84%
    with a dead ~40px border on every side.
    """
    slugs, _ = order()
    bad = []
    for slug in slugs:
        p = CARDS / f"{slug}.jpg"
        if not p.exists():
            p = CARDS / f"{slug}.png"
        if not p.exists():
            continue
        with Image.open(p) as im:
            im = im.convert("RGB")
            W, H = im.size
            px = im.load()

            def sat_row(y):
                t = 0
                for x in range(0, W, 6):
                    r, g, b = px[x, y]
                    mx, mn = max(r, g, b), min(r, g, b)
                    t += 0 if mx == 0 else (mx - mn) / mx
                return t / len(range(0, W, 6))

            def sat_col(x):
                t = 0
                for y in range(0, H, 6):
                    r, g, b = px[x, y]
                    mx, mn = max(r, g, b), min(r, g, b)
                    t += 0 if mx == 0 else (mx - mn) / mx
                return t / len(range(0, H, 6))

            TH = 0.16
            top = next((y for y in range(0, H, 2) if sat_row(y) > TH), 0)
            bot = next((y for y in range(H - 1, 0, -2) if sat_row(y) > TH), H)
            left = next((x for x in range(0, W, 2) if sat_col(x) > TH), 0)
            right = next((x for x in range(W - 1, 0, -2) if sat_col(x) > TH), W)
            pct = 100 * (right - left) * (bot - top) / (W * H)

        flag = "" if pct >= 93 else "  <-- MATTED, re-render"
        if pct < 93:
            bad.append(slug)
        print(f"  {slug:<20} coverage {pct:5.1f}%{flag}")

    print(f"\n{'FAIL: ' + str(len(bad)) + ' matted card(s)' if bad else 'OK: all cards full-bleed'}")
    return 1 if bad else 0


def sheet():
    slugs, meta = order()
    have = [s for s in slugs if (CARDS / f"{s}.jpg").exists() or (CARDS / f"{s}.png").exists()]
    if not have:
        print("nothing rendered yet")
        return

    cols = 6
    tw, th = 280, 486          # thumb size, keeps the 7:12 card ratio
    pad, top = 14, 44
    rows = (len(have) + cols - 1) // cols
    W = cols * tw + pad * (cols + 1)
    H = top + rows * (th + pad) + pad

    sheet_img = Image.new("RGB", (W, H), (26, 22, 18))
    for i, slug in enumerate(have):
        p = CARDS / f"{slug}.jpg"
        if not p.exists():
            p = CARDS / f"{slug}.png"
        with Image.open(p) as im:
            im = im.convert("RGB").resize((tw, th), Image.LANCZOS)
            x = pad + (i % cols) * (tw + pad)
            y = top + (i // cols) * (th + pad)
            sheet_img.paste(im, (x, y))

    out = ROOT / "contact-sheet.jpg"
    sheet_img.save(out, quality=88, optimize=True, progressive=True)
    print(f"contact sheet: {out.name}  ({len(have)} cards, {out.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "status"
    sys.exit({"convert": convert, "sheet": sheet, "status": status, "check": check}[cmd]() or 0)
