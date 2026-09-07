#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tạo prompt render thực tế từ prompts-full.json (nguồn sự thật) — BẢN v4.

v4: TRANG PHỤC đọc từ 04-AI-GUIDE/wardrobe-standard.json (chuẩn dải lụa mỏng quấn hông),
    áp dụng thống nhất cho mọi lá — sửa chuẩn thì sửa 1 file, 78 lá cùng đổi.

Lịch sử:
  v1  tham chiếu the moon.png + váy kín        -> sai tham chiếu, sai chủ đề, sai trang phục
  v2  bỏ tham chiếu + subject lock + lụa dính  -> sai kiểu chữ so với lá mẫu, lụa quá dày
  v3  + TITLE LETTERING LOCK (bám mẫu chữ ref/title-lettering.png)
      + lụa GOSSAMER siêu mỏng (cấm vải dày/mờ)
  v4  + CHUẨN TRANG PHỤC thống nhất: dải lụa mỏng quấn ngang hông (wardrobe-standard.json)

Mọi khóa gốc (framing / skin-tone / anatomy / count / quality) GIỮ NGUYÊN 100%.

Dùng:  python 04-AI-GUIDE/make-prompts.py
       (sinh ảnh kèm --ref ref/title-lettering.png)
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "cards" / "prompts"

# batch 1-2 (chạy thêm: python 04-AI-GUIDE/make-prompts.py 08-strength 09-hermit)
TARGETS = [
    "00-fool", "01-magician", "02-priestess",
    "03-empress", "04-emperor", "05-hierophant", "06-lovers", "07-chariot",
]

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
    "03-empress": " The crown of flowers, the heart-shaped shield of Venus, the ripe wheat and the throne are required by this card and must not be removed by any other rule.",
    "04-emperor": " The stone throne carved with ram heads, the ankh sceptre and the barren mountains are required by this card and must not be removed by any other rule.",
    "05-hierophant": " The two kneeling female acolytes, the sacred temple pillars and the raised blessing hand are required by this card and must not be removed by any other rule.",
    "06-lovers": " The great winged angel, the tree of knowledge with the serpent and the tree of flames are required by this card and must not be removed by any other rule.",
    "07-chariot": " The two sphinxes, the stone chariot, the starry canopy and the walled city are required by this card and must not be removed by any other rule.",
}

# ---------------------------------------------------------- 4. TRANG PHỤC
# Chuẩn trang phục nằm riêng trong wardrobe-standard.json — sửa 1 chỗ, áp dụng mọi lá.
STD = json.loads((Path(__file__).resolve().parent / "wardrobe-standard.json").read_text(encoding="utf-8"))
WARDROBE_LOCK = STD["wardrobe_lock"]


def scene_rewrite(slug: str, text: str) -> str:
    """Áp dụng chuẩn trang phục vào câu tả cảnh của lá."""
    rw = STD["scene_rewrites"].get(slug)
    if rw:
        text, n = re.subn(re.escape(rw["find"]), rw["replace"], text)
        if n:
            for find, repl in rw.get("extra", []):
                text = re.sub(re.escape(find), repl, text)
            return text
    # không có rewrite riêng -> dùng rule chung
    for g in STD["generic_rewrites"]:
        text = re.sub(g["find"], g["replace"], text)
    return text


def main(slugs=None):
    data = json.loads((ROOT / "prompts-full.json").read_text(encoding="utf-8"))
    prompts = {p["slug"]: p for p in data["prompts"]}
    OUT.mkdir(parents=True, exist_ok=True)

    for slug in (slugs or TARGETS):
        card = prompts[slug]
        title = card["title"]
        text = card["prompt"]

        # 1) bỏ đoạn tham chiếu -> style anchor bằng chữ
        text, n = RE_REF_PARA.subn(STYLE_ANCHOR.format(TITLE=title), text, count=1)
        assert n == 1, f"{slug}: không thay được đoạn tham chiếu"

        # 2) đoạn tiêu đề -> title lettering lock (bám mẫu chữ)
        text, n = RE_TITLE_PARA.subn(TITLE_LETTERING.format(TITLE=title), text, count=1)
        assert n == 1, f"{slug}: không thay được đoạn tiêu đề"

        # 3) chuẩn trang phục (từ wardrobe-standard.json)
        before = text
        text = scene_rewrite(slug, text)
        assert text != before, f"{slug}: không áp dụng được chuẩn trang phục"
        text = text.replace("Main figure —", WARDROBE_LOCK + "\n\nMain figure —", 1)

        # 4) subject lock (trước skin-tone lock)
        lock = SUBJECT_LOCK.format(TITLE=title, ANTI=ANTI_BLEED,
                                   PROPS=PROPS_GUARD.get(slug, ""))
        text = text.replace("Skin-tone lock (hard rule):", lock + "\n\nSkin-tone lock (hard rule):", 1)

        out = OUT / f"{slug}.txt"
        out.write_text(text, encoding="utf-8")
        print(f"✅ {out.relative_to(ROOT)}  ({len(text)} ký tự)  [{title}]")


if __name__ == "__main__":
    import sys
    main(sys.argv[1:] or None)
