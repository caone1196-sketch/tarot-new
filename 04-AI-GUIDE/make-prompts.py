#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tạo prompt render thực tế cho 3 lá đầu tiên.

Lấy NGUYÊN VĂN prompt từ prompts-full.json (nguồn sự thật), rồi áp dụng
đúng 1 chỉnh sửa: khối WARDROBE (trang phục) để ảnh có thể sinh được ở
mọi công cụ tạo ảnh có bộ lọc an toàn — mọi khóa khác giữ nguyên.

Dùng:
    python 04-AI-GUIDE/make-prompts.py            # in ra prompts/<slug>.txt
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "cards" / "prompts"

# (regex tìm trong SCENE, thay bằng) — chỉ đụng vào phần trang phục
WARDROBE_EDITS = {
    "00-fool": (
        r"draped only in a transparent silk veil so fine it clings and reveals her bare body beneath, the veil slipping from one shoulder",
        "wearing a flowing gown of layered ivory silk chiffon and diaphanous gauze veils that cling to and trace the lines of her body in the wind, the gauze slipping from one shoulder",
    ),
    "01-magician": (
        r"a nude young woman magician, bare torso with a length of silk slung low across her hips",
        "a young woman magician in a sculptural gown of black and silver silk with bare shoulders and arms, a length of silk slung low across her hips",
    ),
    "02-priestess": (
        r"a serene nude priestess, bare shoulders and the soft line of her breasts veiled only by a drift of sheer gauze",
        "a serene priestess in a clinging gown of sheer gauze over deep-blue silk, bare shoulders, the fine gauze drifting across her bodice",
    ),
}

WARDROBE_LOCK = (
    "Wardrobe lock (hard rule): elegant fine-art drapery — silk, chiffon and gauze garments that follow and outline her form like a classical museum oil painting. "
    "No nudity, no exposed breasts, nipples, buttocks or genitals, no see-through fabric over intimate areas; the figure is tastefully and fully draped at all times."
)

TARGETS = ["00-fool", "01-magician", "02-priestess"]


def main():
    data = json.loads((ROOT / "prompts-full.json").read_text(encoding="utf-8"))
    prompts = {p["slug"]: p for p in data["prompts"]}
    OUT.mkdir(parents=True, exist_ok=True)

    for slug in TARGETS:
        card = prompts[slug]
        text = card["prompt"]
        pattern, repl = WARDROBE_EDITS[slug]
        new_text, n = re.subn(pattern, repl, text)
        assert n == 1, f"{slug}: không khớp mẫu trang phục (n={n})"

        # chèn wardrobe lock ngay sau đoạn scene (trước "Main figure")
        new_text = new_text.replace(
            "Main figure —", WARDROBE_LOCK + "\n\nMain figure —", 1
        )

        out = OUT / f"{slug}.txt"
        out.write_text(new_text, encoding="utf-8")
        print(f"✅ {out.relative_to(ROOT)}  ({len(new_text)} ký tự)  [{card['title']}]")


if __name__ == "__main__":
    main()
