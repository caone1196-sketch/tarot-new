#!/usr/bin/env python3
"""Upscale generated tarot PNGs to the deck's 2x delivery size.

The image generator currently returns 784x1360 cards. This keeps the artwork
lossless as PNG and produces the requested 1568x2720 pixel delivery files.
"""
from __future__ import annotations

import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CARD_DIR = ROOT / "78-card-deck" / "cards"
TARGET = "1568x2720"

for source in sorted(CARD_DIR.glob("*.png")):
    size = subprocess.check_output(
        ["identify", "-format", "%wx%h", str(source)], text=True
    ).strip()
    if size == TARGET:
        continue
    temp = source.with_name(source.stem + ".hires.png")
    subprocess.run(
        [
            "convert", str(source),
            "-filter", "Lanczos", "-resize", "200%",
            "-unsharp", "0x1.0+0.8+0.02",
            "-define", "png:compression-level=9",
            str(temp),
        ],
        check=True,
    )
    temp.replace(source)
    print(f"Upscaled {source.name}: {size} -> {TARGET}")
