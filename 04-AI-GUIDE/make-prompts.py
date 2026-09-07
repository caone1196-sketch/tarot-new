#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tạo prompt render thực tế từ prompts-full.json (nguồn sự thật) — BẢN v2.

Sửa 3 lỗi của bản v1:
  1. SAI THAM CHIẾU  -> bỏ ảnh tham chiếu (gây lẫn bối cảnh THE MOON sang lá khác),
                        thay bằng STYLE ANCHOR mô tả phong cách bằng chữ.
  2. SAI CHỦ ĐỀ      -> thêm SUBJECT LOCK + danh sách chống lẫn lá khác.
  3. SAI TRANG PHỤC  -> khôi phục đúng tinh thần gốc: lụa mỏng trong suốt dính sát
                        người, da trần vai/lưng/eo (wet-drapery), thay vì "váy kín".

Mọi khóa gốc (framing / skin-tone / anatomy / count / quality) GIỮ NGUYÊN 100%.

Dùng:  python 04-AI-GUIDE/make-prompts.py
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "cards" / "prompts"

TARGETS = ["00-fool", "01-magician", "02-priestess"]

# ---------------------------------------------------------------- 1. STYLE
STYLE_ANCHOR = (
    "A full-bleed tarot card artwork \"{TITLE}\": the painted scene fills the ENTIRE image edge to edge "
    "like a classical fine-art oil painting, in the style of a vintage gothic tarot deck — warm chiaroscuro "
    "lit by a single soft light source, a palette of antique gold, oxblood, deep teal and midnight blue, "
    "luminous highlights on skin against atmospheric shadow, ornate decorative detail, visible painterly "
    "brushwork, museum-grade oil painting."
)

RE_REF_PARA = re.compile(
    r"^A full-bleed tarot card artwork \".*?\": the painted scene fills the ENTIRE image edge to edge "
    r"like a classical fine-art painting, matching the painterly style.*?outer border and frame\.$",
    re.S | re.M,
)

# ------------------------------------------------- 2. SUBJECT LOCK + chống lẫn
ANTI_BLEED = (
    "no twin towers, no howling wolf or pair of dogs, no crayfish or lobster, "
    "no moonlit pool or stream, no winding path receding to a distant horizon, no full moon dominating the sky"
)

SUBJECT_LOCK = (
    "Subject lock (hard rule): this card is \"{TITLE}\" — depict EXACTLY and ONLY the scene described above. "
    "Do not borrow imagery from any other tarot card: {ANTI}. "
    "Every object, prop and creature on the card must come from the scene description above — nothing invented, nothing carried over from another card."
)

# ---------------------------------------------------------- 3. TRANG PHỤC
WARDROBE_EDITS = {
    # giữ nguyên "lụa mỏng trong suốt dính sát" — chỉ đổi câu "lộ cơ thể trần truồng"
    "00-fool": (
        r"draped only in a transparent silk veil so fine it clings and reveals her bare body beneath",
        "draped only in a transparent silk veil so fine it clings to her and traces every line of her figure beneath the fabric",
    ),
    "01-magician": (
        r"a nude young woman magician, bare torso with a length of silk slung low across her hips",
        "a young woman magician, her bare shoulders, arms, back and midriff rising above a length of clinging translucent silk wrapped across her chest and slung low across her hips",
    ),
    "02-priestess": (
        r"a serene nude priestess, bare shoulders and the soft line of her breasts veiled only by a drift of sheer gauze",
        "a serene priestess, her bare shoulders and long neck rising above a clinging gown of sheer gauze that covers her breasts and pools on the stone floor",
    ),
}

WARDROBE_LOCK = (
    "Wardrobe lock (hard rule): the sensuality comes from clinging translucent silk, bare shoulders, arms, back and midriff, "
    "and the pose — in the manner of a classical wet-drapery marble sculpture. No explicit nudity: no visible breasts or nipples, "
    "no buttocks or genitals, no see-through fabric over intimate areas, no sexual acts or overtly sexual posing."
)


def main():
    data = json.loads((ROOT / "prompts-full.json").read_text(encoding="utf-8"))
    prompts = {p["slug"]: p for p in data["prompts"]}
    OUT.mkdir(parents=True, exist_ok=True)

    for slug in TARGETS:
        card = prompts[slug]
        title = card["title"]
        text = card["prompt"]

        # 1) thay đoạn tham chiếu bằng style anchor
        text, n = RE_REF_PARA.subn(STYLE_ANCHOR.format(TITLE=title), text, count=1)
        assert n == 1, f"{slug}: không thay được đoạn tham chiếu"

        # 3) trang phục
        pattern, repl = WARDROBE_EDITS[slug]
        text, n = re.subn(pattern, repl, text)
        assert n == 1, f"{slug}: không khớp mẫu trang phục (n={n})"
        text = text.replace("Main figure —", WARDROBE_LOCK + "\n\nMain figure —", 1)

        # 2) subject lock (trước skin-tone lock)
        lock = SUBJECT_LOCK.format(TITLE=title, ANTI=ANTI_BLEED)
        text = text.replace("Skin-tone lock (hard rule):", lock + "\n\nSkin-tone lock (hard rule):", 1)

        out = OUT / f"{slug}.txt"
        out.write_text(text, encoding="utf-8")
        print(f"✅ {out.relative_to(ROOT)}  ({len(text)} ký tự)  [{title}]")


if __name__ == "__main__":
    main()
