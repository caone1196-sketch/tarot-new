#!/usr/bin/env python3
"""Compose generated central illustrations into the 78-card tarot layout.

The art is generated without typography/borders.  This script puts it behind the
exact supplied card-blank frame, then adds one consistent parchment title ribbon
and badge so all cards share the same border, lettering and ornament treatment.
Requires ImageMagick's `convert` and `composite` commands.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DECK = Path(__file__).resolve().parent
ART = DECK / "_art"
OUT = DECK / "cards"
CACHE = DECK / "_cache"
FRAME_SOURCE = ROOT / "card-blank.png"

W, H = 784, 1360
GOLD = "#a87532"
DARK_GOLD = "#70461e"
PARCHMENT = "#f1dfbd"


def run(*args: str) -> None:
    subprocess.run(list(args), check=True)


def ensure_assets() -> tuple[Path, Path]:
    CACHE.mkdir(parents=True, exist_ok=True)
    frame = CACHE / "frame-overlay.png"
    if not frame.exists():
        # Keep the supplied blank card opaque around its ornamented edge while
        # opening its large inner window for generated illustration.
        run(
            "convert", str(FRAME_SOURCE), "-alpha", "set", "-channel", "A",
            "-region", "676x1252+54+54", "-evaluate", "set", "0",
            "+region", str(frame),
        )
    return frame, CACHE / "title-overlay.png"


def title_overlay(title: str, badge: str) -> Path:
    _, overlay = ensure_assets()
    # Re-render for every title so the text is part of the same high-resolution
    # ornament layer.  Serif lettering follows the supplied samples while the
    # ribbon and badge echo their gold-on-aged-parchment construction.
    long = len(title) > 16
    very_long = len(title) > 21
    size = 27 if very_long else (30 if long else 34)
    cmd = [
        "convert", "-size", f"{W}x{H}", "xc:none",
        "-alpha", "set",
        # Upper medallion / badge
        "-fill", PARCHMENT, "-stroke", GOLD, "-strokewidth", "4",
        "-draw", "ellipse 392,108 150,61 0,360",
        "-stroke", "#d5a75b", "-strokewidth", "1",
        "-draw", "ellipse 392,108 139,50 0,360",
        "-fill", DARK_GOLD, "-stroke", "none", "-font", "DejaVu-Serif-Bold",
        "-pointsize", "24", "-gravity", "North", "-annotate", "+0+87", badge,
        # Title ribbon: parchment body, double gold edge and rolled ends.
        "-fill", PARCHMENT, "-stroke", GOLD, "-strokewidth", "4",
        "-draw", "roundrectangle 126,1126 658,1247 19,19",
        "-stroke", "#d5a75b", "-strokewidth", "1",
        "-draw", "roundrectangle 139,1138 645,1235 13,13",
        "-fill", PARCHMENT, "-stroke", GOLD, "-strokewidth", "3",
        "-draw", "ellipse 131,1187 22,42 0,360",
        "-draw", "ellipse 653,1187 22,42 0,360",
        "-fill", DARK_GOLD, "-stroke", "none", "-font", "DejaVu-Serif",
        "-pointsize", str(size), "-gravity", "North", "-annotate", "+0+1168", title,
        # Tiny divider ornaments in the same ink as the sample titles.
        "-pointsize", "22", "-annotate", "+0+1114", "•    ✦    •",
        "-pointsize", "22", "-annotate", "+0+1264", "•    ✦    •",
        str(overlay),
    ]
    run(*cmd)
    return overlay


def badge_for(card: dict) -> str:
    group = card["group"]
    n = card["n"]
    if group == "major":
        return n
    if n == "A":
        return {"wands": "W", "cups": "C", "swords": "S", "pentacles": "P"}[group]
    if n in {"P", "N", "Q", "K"}:
        return n
    return {"wands": "W", "cups": "C", "swords": "S", "pentacles": "P"}[group] + " " + n


def compose(card: dict, keep_art: bool = True) -> Path:
    frame, _ = ensure_assets()
    title = title_overlay(card["title"], badge_for(card))
    raw = ART / f"{card['slug']}.png"
    if not raw.exists():
        raise FileNotFoundError(raw)
    OUT.mkdir(parents=True, exist_ok=True)
    fitted = CACHE / f"{card['slug']}-fit.png"
    framed = CACHE / f"{card['slug']}-framed.png"
    final = OUT / f"{card['slug']}.jpg"
    run(
        "convert", str(raw), "-resize", f"{W}x{H}^", "-gravity", "center",
        "-extent", f"{W}x{H}", str(fitted),
    )
    run("composite", str(frame), str(fitted), str(framed))
    run("composite", str(title), str(framed), "-quality", "91", str(final))
    if not keep_art:
        raw.unlink(missing_ok=True)
    for temp in (fitted, framed):
        temp.unlink(missing_ok=True)
    return final


def main() -> int:
    manifest = DECK / "manifest.json"
    data = json.loads((ROOT / "cards.json").read_text())
    cards = data["cards"]
    manifest.write_text(json.dumps({"meta": data["meta"], "cards": cards}, indent=2, ensure_ascii=False) + "\n")
    wanted = sys.argv[1:]
    selected = [c for c in cards if not wanted or c["slug"] in wanted]
    for card in selected:
        print(compose(card, keep_art=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
