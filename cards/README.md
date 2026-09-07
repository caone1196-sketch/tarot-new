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

## ⚠️ 3 điểm khác so với `03-PROMPTS-78-FULL.md` (bản v2)

Script `04-AI-GUIDE/make-prompts.py` lấy prompt gốc và áp **đúng 3 chỉnh sửa**:

| # | Sửa gì | Vì sao |
|---|---|---|
| 1 | Đoạn "matching … THE MOON reference image" → **STYLE ANCHOR** mô tả phong cách bằng chữ | Dùng `the moon.png` làm ảnh tham chiếu làm model **kéo bối cảnh THE MOON sang lá khác** (tháp đôi, chó/sói, hồ trăng) |
| 2 | Thêm **Subject lock** + danh sách chống lẫn | Chốt đúng chủ đề, cấm mượn hình ảnh lá khác |
| 3 | Câu tả trang phục + **Wardrobe lock** | Prompt gốc mô tả khỏa thân rõ ("nude", "reveals her bare body") → đổi sang **lụa mỏng trong suốt dính sát người, da trần vai/lưng/eo** kiểu wet-drapery cổ điển |

```
Wardrobe lock (hard rule): the sensuality comes from clinging translucent silk, bare
shoulders, arms, back and midriff, and the pose — in the manner of a classical wet-drapery
marble sculpture. No explicit nudity: no visible breasts or nipples, no buttocks or genitals,
no see-through fabric over intimate areas, no sexual acts or overtly sexual posing.
```

**5 khóa gốc vẫn giữ nguyên 100%**: FRAMING · SKIN TONE · ANATOMY · COUNT · QUALITY.
Bố cục, nhân vật (mắt/tóc/da/vóc dáng/nét riêng), đạo cụ, count lock **không đổi** —
riêng Magician có thêm câu bảo vệ 4 món trên bàn thờ, Priestess bảo vệ 2 cột đá + cuộn giấy + trăng lưỡi liềm.

> Nếu công cụ của bạn cho phép khỏa thân nghệ thuật: xóa khối `Wardrobe lock` và khôi phục
> câu tả trang phục gốc trong `cards/prompts/<slug>.txt`, rồi sinh lại.

## 📜 Lịch sử

- **v1** (`63b94c4`) — có tham chiếu `the moon.png`, trang phục váy kín → **bị chê: sai tham chiếu, sai chủ đề, sai tạo hình/trang phục**
- **v2** (hiện tại) — bỏ tham chiếu, thêm Subject lock, trang phục lụa mỏng dính người

## Sinh thêm lá

```bash
python 04-AI-GUIDE/make-prompts.py      # (1) tạo prompt cho batch
# (2) sinh ảnh bằng công cụ tạo ảnh, lưu thành cards/<slug>.png
python 04-AI-GUIDE/build-gallery.py     # (3) cập nhật index.html + manifest.json
```

Xem gallery: `python3 -m http.server 8000` rồi mở `http://localhost:8000`.
