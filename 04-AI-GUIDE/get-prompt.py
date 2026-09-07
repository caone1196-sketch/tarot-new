#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Lấy prompt tarot nhanh theo slug / tên Anh / tên Việt.

Ví dụ:
    python get-prompt.py 18-moon
    python get-prompt.py "mặt trăng"
    python get-prompt.py "nine of swords"
    python get-prompt.py --list
    python get-prompt.py --json 18-moon     # xuất JSON {slug,title,prompt}
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE.parent / "prompts-full.json"

MAJOR_VN = {
    "00-fool": "kẻ ngây thợ", "01-magician": "pháp sư", "02-priestess": "nữ tư tế",
    "03-empress": "nữ hoàng", "04-emperor": "hoàng đế", "05-hierophant": "giáo hoàng",
    "06-lovers": "tình nhân", "07-chariot": "chiến xa", "08-strength": "sức mạnh",
    "09-hermit": "ẩn sĩ", "10-wheel": "bánh xe số phận", "11-justice": "công lý",
    "12-hanged": "kẻ treo ngược", "13-death": "tử thần", "14-temperance": "tiết chế",
    "15-devil": "ma quỷ", "16-tower": "tòa tháp", "17-the-star": "ngôi sao",
    "18-moon": "mặt trăng", "19-sun": "mặt trời", "20-judgement": "phán xét",
    "21-world": "thế giới",
}
SUIT_VN = {"wands": "gậy", "cups": "chén", "swords": "kiếm", "pentacles": "xu"}
RANK_VN = {"ace": "át", "02": "hai", "03": "ba", "04": "bốn", "05": "năm", "06": "sáu",
           "07": "bảy", "08": "tám", "09": "chín", "10": "mười",
           "page": "học trò", "knight": "kỵ sĩ", "queen": "hoàng hậu", "king": "vua"}


def vn_name(slug: str) -> str:
    if slug in MAJOR_VN:
        return MAJOR_VN[slug]
    suit, rank = slug.split("-")
    return f"{RANK_VN[rank]} {SUIT_VN[suit]}"


def norm(s: str) -> str:
    return " ".join(s.strip().lower().split())


def load():
    if not DATA.exists():
        sys.exit(f"Không tìm thấy {DATA} — chạy từ thư mục repo tarot-new.")
    return json.loads(DATA.read_text(encoding="utf-8"))["prompts"]


def find(prompts, query: str):
    q = norm(query)
    # 1) slug trực tiếp
    for p in prompts:
        if p["slug"].lower() == q:
            return p
    # 2) tên Anh
    for p in prompts:
        if norm(p["title"]) == q:
            return p
    # 3) tên Việt
    for p in prompts:
        if vn_name(p["slug"]) == q:
            return p
    # 4) số ẩn chính (0–21)
    if q.isdigit():
        n = int(q)
        for p in prompts:
            if p["group"] == "major" and p["slug"].split("-")[0] == f"{n:02d}":
                return p
    # 5) chứa một phần (slug/tên Anh/tên Việt)
    for p in prompts:
        if q in p["slug"].lower() or q in norm(p["title"]) or q in vn_name(p["slug"]):
            return p
    return None


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(1)
    prompts = load()
    if args[0] == "--list":
        for p in prompts:
            print(f"{p['slug']:<16} {p['title']:<22} {vn_name(p['slug'])}")
        return
    as_json = "--json" in args
    query = [a for a in args if a != "--json"][0]
    card = find(prompts, query)
    if not card:
        gợi_ý = ", ".join(p["slug"] for p in prompts if norm(query)[:3] in p["slug"])
        sys.exit(f"Không tìm thấy lá '{query}'. Gợi ý gần: {gợi_ý or 'chạy --list để xem danh sách'}")
    if as_json:
        print(json.dumps(card, ensure_ascii=False, indent=2))
    else:
        print(f"# {card['title']} ({card['slug']}) — {vn_name(card['slug'])}")
        print()
        print(card["prompt"])


if __name__ == "__main__":
    main()
