#!/usr/bin/env python3
"""normalize_cards.py — Kiểm tra & chuẩn hoá kích thước lá bài theo CANVAS LOCK 784x1360.
Dùng: python3 tools/normalize_cards.py <file|thư_mục> [--dry-run]
"""
import struct, sys
from pathlib import Path

TARGET_W, TARGET_H = 784, 1360
EXTS = {".png", ".jpg", ".jpeg"}

def png_size(p):
    with open(p,'rb') as f: d=f.read(33)
    return struct.unpack('>II', d[16:24])

def jpeg_size(p):
    data=open(p,'rb').read(); i=2
    while i < len(data):
        if data[i]!=0xFF: i+=1; continue
        m=data[i+1]
        if m in (0xC0,0xC1,0xC2,0xC3,0xC5,0xC6,0xC7,0xC9,0xCA,0xCB,0xCD,0xCE,0xCF):
            h,w=struct.unpack('>HH', data[i+5:i+9]); return w,h
        if m in (0xD8,0xD9) or 0xD0<=m<=0xD7: i+=2; continue
        i += 2 + struct.unpack('>H', data[i+2:i+4])[0]
    raise ValueError('not jpeg')

def get_size(p):
    return png_size(p) if p.suffix.lower()=='.png' else jpeg_size(p)

def fix(path, dry):
    from PIL import Image
    img = Image.open(path)
    w,h = img.size
    scale = max(TARGET_W/w, TARGET_H/h)
    nw,nh = round(w*scale), round(h*scale)
    if (nw,nh)!=(w,h):
        img = img.resize((nw,nh), Image.LANCZOS)
    l=(nw-TARGET_W)//2; t=(nh-TARGET_H)//2
    img = img.crop((l,t,l+TARGET_W,t+TARGET_H))
    if not dry:
        img.save(path, quality=93)
    print(f"  -> FIXED {w}x{h} -> {TARGET_W}x{TARGET_H}")

def main():
    args=[a for a in sys.argv[1:] if a!='--dry-run']; dry='--dry-run' in sys.argv
    targets=[]
    for a in args:
        p=Path(a)
        targets += sorted(x for x in p.rglob('*') if x.suffix.lower() in EXTS) if p.is_dir() else ([p] if p.is_file() else [])
    print(f"CANVAS LOCK {TARGET_W}x{TARGET_H} — {len(targets)} ảnh")
    for t in targets:
        try: w,h=get_size(t)
        except Exception as e: print(f"  ⚠️ {t}: {e}"); continue
        if (w,h)==(TARGET_W,TARGET_H): print(f"  ✅ {t.name}: {w}x{h}")
        else:
            print(f"  ❌ {t.name}: {w}x{h} LỆCH")
            if not dry: fix(t,dry)

if __name__=='__main__': main()
