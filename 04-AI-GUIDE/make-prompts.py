#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tạo prompt render thực tế từ prompts-full.json (nguồn sự thật) — BẢN v3.

Lịch sử:
  v1  tham chiếu the moon.png + váy kín        -> sai tham chiếu, sai chủ đề, sai trang phục
  v2  bỏ tham chiếu + subject lock + lụa dính  -> sai kiểu chữ so với lá mẫu, lụa quá dày
  v3  + TITLE LETTERING LOCK (bám mẫu chữ ref/title-lettering.png)
      + lụa GOSSAMER siêu mỏng (cấm vải dày/mờ)

Mọi khóa gốc (framing / skin-tone / anatomy / count / quality) GIỮ NGUYÊN 100%.

Dùng:  python 04-AI-GUIDE/make-prompts.py
       (sinh ảnh kèm --ref ref/title-lettering.png)
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

# ------------------------------------------------- 2. KIỂU CHỮ (bám lá mẫu)
TITLE_LETTERING = (
    "At the BOTTOM of the image, elegantly overlaid on the artwork: the title \"{TITLE}\" — the lettering "
    "MUST match the specimen shown in the reference image EXACTLY: the same antique serif typeface, the same "
    "serif shape and stroke weight, the same letter-spacing, the same capitals, the same size relative to the "
    "card width, the same warm gold colour with the same bright inner highlight and the same soft dark drop "
    "shadow for legibility. This is the ONLY text on the card. The reference image is a lettering specimen "
    "only — copy its lettering style, but IGNORE the specimen's own wording and its dark panel, and render the title \"{TITLE}\"."
)

RE_TITLE_PARA = re.compile(
    r"^At the BOTTOM of the image, elegantly overlaid on the artwork: the title \".*?\" "
    r"in clean antique lettering with a soft shadow for legibility — this is the ONLY text on the card\.$",
    re.S | re.M,
)

# ------------------------------------------------- 3. SUBJECT LOCK + chống lẫn
ANTI_BLEED = (
    "no twin towers, no howling wolf or pair of dogs, no crayfish or lobster, "
    "no moonlit pool or stream, no winding path receding to a distant horizon, no full moon dominating the sky"
)

SUBJECT_LOCK = (
    "Subject lock (hard rule): this card is \"{TITLE}\" — depict EXACTLY and ONLY the scene described above. "
    "Do not borrow imagery from any other tarot card: {ANTI}. "
    "Every object, prop and creature on the card must come from the scene description above — nothing invented, nothing carried over from another card."
    "{PROPS}"
)

# đạo cụ bắt buộc riêng từng lá (bảo vệ khỏi các khóa khác vô tình xóa mất)
PROPS_GUARD = {
    "01-magician": " The four suit objects on the altar — cup, sword, wand, coin — are required by this card and must not be removed by any other rule.",
    "02-priestess": " The two stone pillars, the scroll in her lap and the silver crescent at her feet are required by this card and must not be removed by any other rule.",
}

# ---------------------------------------------------------- 4. TRANG PHỤC
WARDROBE_EDITS = {
    "00-fool": (
        r"draped only in a transparent silk veil so fine it clings and reveals her bare body beneath",
        "draped only in a veil of gossamer-fine transparent silk, near-weightless and almost see-through, "
        "clinging wetly to her so the whole line of her body reads clearly through the fabric",
    ),
    "01-magician": (
        r"a nude young woman magician, bare torso with a length of silk slung low across her hips",
        "a young woman magician, her bare shoulders, arms, back and midriff above a length of gossamer-fine "
        "translucent silk wrapped across her chest and slung low across her hips, the fabric so sheer that the "
        "line of her body and her warm skin tone read clearly through it",
    ),
    "02-priestess": (
        r"a serene nude priestess, bare shoulders and the soft line of her breasts veiled only by a drift of sheer gauze",
        "a serene priestess, her bare shoulders and long neck rising above a drift of gossamer-fine sheer gauze "
        "that covers her breasts and falls to the stone floor, the gauze so diaphanous that the line of her body "
        "reads clearly beneath it",
    ),
}

WARDROBE_LOCK = (
    "Wardrobe lock (hard rule): the fabric is GOSSAMER — ultra-fine, near-transparent silk chiffon and gauze, "
    "weightless and wet-clinging, reading as a second skin so that the body's contours, muscles and warm skin "
    "tone are legible through it. FORBIDDEN: thick, heavy, stiff or opaque cloth — no velvet, no brocade, no "
    "heavy layered drapery, no quilted or padded panels, no opaque gowns. The cloth must read as a whisper of "
    "silk, not as clothing. No explicit nudity: no visible breasts or nipples, no buttocks or genitals, "
    "no see-through fabric directly over intimate areas, no sexual acts or overtly sexual posing."
)


def main():
    data = json.loads((ROOT / "prompts-full.json").read_text(encoding="utf-8"))
    prompts = {p["slug"]: p for p in data["prompts"]}
    OUT.mkdir(parents=True, exist_ok=True)

    for slug in TARGETS:
        card = prompts[slug]
        title = card["title"]
        text = card["prompt"]

        # 1) bỏ đoạn tham chiếu -> style anchor bằng chữ
        text, n = RE_REF_PARA.subn(STYLE_ANCHOR.format(TITLE=title), text, count=1)
        assert n == 1, f"{slug}: không thay được đoạn tham chiếu"

        # 2) đoạn tiêu đề -> title lettering lock (bám mẫu chữ)
        text, n = RE_TITLE_PARA.subn(TITLE_LETTERING.format(TITLE=title), text, count=1)
        assert n == 1, f"{slug}: không thay được đoạn tiêu đề"

        # 3) trang phục gossamer
        pattern, repl = WARDROBE_EDITS[slug]
        text, n = re.subn(pattern, repl, text)
        assert n == 1, f"{slug}: không khớp mẫu trang phục (n={n})"
        text = text.replace("Main figure —", WARDROBE_LOCK + "\n\nMain figure —", 1)

        # 4) subject lock (trước skin-tone lock)
        lock = SUBJECT_LOCK.format(TITLE=title, ANTI=ANTI_BLEED,
                                   PROPS=PROPS_GUARD.get(slug, ""))
        text = text.replace("Skin-tone lock (hard rule):", lock + "\n\nSkin-tone lock (hard rule):", 1)

        out = OUT / f"{slug}.txt"
        out.write_text(text, encoding="utf-8")
        print(f"✅ {out.relative_to(ROOT)}  ({len(text)} ký tự)  [{title}]")


if __name__ == "__main__":
    main()
