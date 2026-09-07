# 🃏 cards/ — Ảnh đã sinh

Mỗi lá = 1 file PNG tên theo `slug`, tỉ lệ **784×1360 (7:12)**, full-bleed, không khung viền.

| File | Lá | Tên Việt | Trạng thái |
|---|---|---|---|
| `00-fool.png` | THE FOOL | Kẻ Ngây Thơ | ✅ batch 1 |
| `01-magician.png` | THE MAGICIAN | Pháp Sư | ✅ batch 1 |
| `02-priestess.png` | THE HIGH PRIESTESS | Nữ Tư Tế | ✅ batch 1 |

## Cấu trúc

```
cards/
├── <slug>.png            # ảnh lá bài (full-bleed 7:12)
├── prompts/<slug>.txt    # prompt THỰC TẾ đã dùng để sinh ảnh đó
├── manifest.json         # máy đọc được — dùng cho gallery / API
└── README.md             # file này
```

## ⚠️ Một điểm khác duy nhất so với `03-PROMPTS-78-FULL.md`

Prompt nguồn của 3 lá đầu mô tả nhân vật **khỏa thân** ("nude", "reveals her bare body").
Để sinh được trên các công cụ tạo ảnh có bộ lọc an toàn, script `04-AI-GUIDE/make-prompts.py`
giữ nguyên **toàn bộ** prompt gốc và chỉ thay đúng câu tả trang phục + chèn thêm 1 khối:

```
Wardrobe lock (hard rule): elegant fine-art drapery — silk, chiffon and gauze garments
that follow and outline her form like a classical museum oil painting. No nudity, no
exposed breasts, nipples, buttocks or genitals, no see-through fabric over intimate
areas; the figure is tastefully and fully draped at all times.
```

**5 khóa gốc vẫn giữ nguyên 100%**: FRAMING · SKIN TONE · ANATOMY · COUNT · QUALITY.
Bố cục, nhân vật (mắt/tóc/da/vóc dáng/nét riêng), đạo cụ và count lock **không đổi**.

> Nếu công cụ của bạn cho phép khỏa thân nghệ thuật: xóa khối `Wardrobe lock` và khôi phục
> câu tả trang phục gốc trong `cards/prompts/<slug>.txt`, rồi sinh lại.

## Sinh thêm lá

```bash
python 04-AI-GUIDE/make-prompts.py      # (1) tạo prompt cho batch
# (2) sinh ảnh bằng công cụ tạo ảnh, lưu thành cards/<slug>.png
python 04-AI-GUIDE/build-gallery.py     # (3) cập nhật index.html + manifest.json
```

Xem gallery: `python3 -m http.server 8000` rồi mở `http://localhost:8000`.
