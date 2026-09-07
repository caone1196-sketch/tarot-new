#!/usr/bin/env python3
"""build_prompt.py — Ghép prompt hoàn chỉnh cho từng lá từ cards.json + 02-CHARACTER-SPECS.md.
Dùng: python3 tools/build_prompt.py <slug> | --all [--outdir=thư_mục]
Template: chuẩn v3.4 (CANVAS/BORDER/WARDROBE/HARD-COUNT lock + full-bleed + title Blackletter).
"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TARGET = "784x1360"

SANITIZE_PAIRS = [
    (r"\bnude\s+", ""), (r"\bnaked\s+", ""), (r"\btopless\s+", ""),
    (r",?\s*one breast bared,?", ""),
    (r"\bbare (?:body|chest|breast)s?\b", "figure"),
    (r"\bso fine it clings and reveals her figure beneath\b", "so fine it flows with her silhouette"),
]

def clean(s): return re.sub(r"\s+"," ",s.replace("**","").strip())

def load_cards():
    d=json.loads((ROOT/'cards.json').read_text(encoding='utf-8'))
    return {c['slug']:c for c in d['cards']}

def load_specs():
    specs={}
    for line in (ROOT/'02-CHARACTER-SPECS.md').read_text(encoding='utf-8').splitlines():
        line=line.strip()
        if not line.startswith('|') or '`' not in line or line.startswith('|--'): continue
        m=re.search(r"`([a-z0-9]+(?:-[a-z0-9]+)+)`", line)
        if not m: continue
        c=[x.strip() for x in line.strip('|').split('|')]
        if len(c)<8: continue
        specs[m.group(1)] = dict(age=clean(c[1]),eyes=clean(c[2]),hair=clean(c[3]),
                                 build=clean(c[4]),skin=clean(c[5]),signature=clean(c[6]),aura=clean(c[7] if len(c)>7 else ''))
    return specs

def count_lock(card):
    c=card.get('count')
    if c: return f"HARD COUNT RULE — {c['layout'].strip()} Count every instance before finalizing; a wrong count is a critical error that forces a repaint."
    return "No cup, sword, wand or coin appears anywhere on the card."

def figure_spec(s):
    if s is None: return "This card has NO human figure — it is a pure object/landscape scene."
    parts=[f"She is {s['age']} years old",f"Eyes: {s['eyes']}",f"Hair: {s['hair']}",f"Build: {s['build']}",
           f"Skin tone: {s['skin']}",f"UNIQUE SIGNATURE that must be clearly visible on her: {s['signature']}"]
    if s['aura']: parts.append(f"Mood/aura of the scene: {s['aura']}")
    return ". ".join(parts)+"."

TEMPLATE = """A single tarot card "{title}", vertical portrait, full-bleed painted artwork covering the ENTIRE card — top, side and bottom edges beneath the golden border like THE STAR reference. No parchment strip anywhere; the title sits DIRECTLY on the painted scene.
OUTPUT CANVAS: exactly 784x1360 pixels, portrait, same canvas as the reference cards.

The FIRST reference (blank card) gives ONLY its thin double golden border lines and corner scrollwork — the TWO PARALLEL THIN golden lines and golden corner flourishes must be replicated EXACTLY, overlaid ON TOP of the painting; a single-line border is an error. Do NOT copy its empty parchment areas. THE SECOND (THE STAR) is only a quality/lettering reference — do not copy her face or identity.

WARDROBE LOCK: dress the figure(s) exactly like the woman in THE STAR reference — essentially bare classical fine-art figure, at most a thin wisp of translucent silk as an accent, long hair as natural drapery. NO dresses, NO gowns, NO armor unless the scene requires a minimal story piece.

IDENTITY: {identity}

Scene: {scene} {count}

At the bottom center, over the painting, the title "{title}" in antique gold Blackletter lettering identical in style to THE STAR's title. Spelling must be exact, letter-for-letter: "{title}". No box, no strip, no frame around the letters.

Anatomy: each figure exactly one head, one torso, two arms, two legs, natural joints, correct fingers."""

def build(slug, cards, specs):
    c=cards[slug]
    scene=c['scene']
    for pat,rep in SANITIZE_PAIRS: scene=re.sub(pat,rep,scene,flags=re.I)
    scene=re.sub(r"\s+"," ",scene).strip()
    return TEMPLATE.format(title=c['title'], identity=figure_spec(specs.get(slug)),
                           scene=scene[0].upper()+scene[1:], count=count_lock(c))

def main():
    cards,specs=load_cards(),load_specs()
    a=sys.argv[1:]
    if '--all' in a:
        od=ROOT/'prompts'
        for x in a:
            if x.startswith('--outdir='): od=ROOT/x.split('=',1)[1]
        od.mkdir(parents=True,exist_ok=True)
        for s in cards: (od/f'{s}.txt').write_text(build(s,cards,specs),encoding='utf-8')
        print(f"Đã xuất {len(cards)} prompt -> {od}/")
    else:
        print(build(a[0],cards,specs))

if __name__=='__main__': main()
