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

## ⚠️ Điểm khác so với `03-PROMPTS-78-FULL.md` (bản v3)

`04-AI-GUIDE/make-prompts.py` lấy prompt gốc và áp **4 chỉnh sửa**:

| # | Sửa gì | Vì sao |
|---|---|---|
| 1 | Đoạn "matching … THE MOON reference image" → **STYLE ANCHOR** bằng chữ | Ảnh tham chiếu nguyên lá làm model **kéo bối cảnh THE MOON sang lá khác** |
| 2 | Thêm **Subject lock** + danh sách chống lẫn | Chốt đúng chủ đề, cấm mượn hình lá khác |
| 3 | **Title lettering lock** — bám mẫu chữ `ref/title-lettering.png` | v2 viết chữ tự do → **sai kiểu chữ so với lá mẫu** |
| 4 | Vải = **GOSSAMER** siêu mỏng | v2 ra lụa còn dày → cấm rõ vải dày/mờ |

**Tham chiếu kiểu chữ** — tách riêng dải chữ từ `the moon.png` (y 1206–1290) dán lên nền tối
784×1360, nên model chỉ học **chữ**, không học bối cảnh:

```
ref/title-lettering.png   # bản mẫu chữ (dùng làm --ref khi sinh ảnh)
ref/title-compare.png     # so sánh 4 dải chữ: mẫu + 3 lá v3
```

Kiểm chứng: đỉnh tương phản dải chữ của mẫu ở **y=1264 (cách đáy 96px)**;
3 lá v3 ở **y=1263–1267 (cách đáy 93–97px)** — khớp vị trí, cỡ chữ và độ tương phản.

```
Wardrobe lock (hard rule): the fabric is GOSSAMER — ultra-fine, near-transparent silk chiffon
and gauze, weightless and wet-clinging, reading as a second skin so that the body's contours,
muscles and warm skin tone are legible through it. FORBIDDEN: thick, heavy, stiff or opaque
cloth — no velvet, no brocade, no heavy layered drapery, no quilted or padded panels, no opaque
gowns. The cloth must read as a whisper of silk, not as clothing. No explicit nudity: no visible
breasts or nipples, no buttocks or genitals, no see-through fabric directly over intimate areas,
no sexual acts or overtly sexual posing.
```

**5 khóa gốc vẫn giữ nguyên 100%**: FRAMING · SKIN TONE · ANATOMY · COUNT · QUALITY.
Bố cục, nhân vật (mắt/tóc/da/vóc dáng/nét riêng), đạo cụ, count lock **không đổi**.

> Nếu công cụ của bạn cho phép khỏa thân nghệ thuật: xóa khối `Wardrobe lock` và khôi phục
> câu tả trang phục gốc trong `cards/prompts/<slug>.txt`, rồi sinh lại.

## 📜 Lịch sử

- **v1** (`63b94c4`) — tham chiếu `the moon.png` + váy kín → sai tham chiếu, sai chủ đề, sai trang phục
- **v2** (`390bd12`) — bỏ tham chiếu + subject lock + lụa dính → **sai kiểu chữ, lụa quá dày**
- **v3** (hiện tại) — + title lettering lock bám mẫu chữ, + vải gossamer siêu mỏng

## Sinh thêm lá

```bash
python 04-AI-GUIDE/make-prompts.py      # (1) tạo prompt cho batch
# (2) sinh ảnh bằng công cụ tạo ảnh, lưu thành cards/<slug>.png
python 04-AI-GUIDE/build-gallery.py     # (3) cập nhật index.html + manifest.json
```

Xem gallery: `python3 -m http.server 8000` rồi mở `http://localhost:8000`.
