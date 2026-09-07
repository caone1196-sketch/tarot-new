# 🃏 cards/ — Ảnh đã sinh

Mỗi lá = 1 file PNG tên theo `slug`, tỉ lệ **784×1360 (7:12)**, full-bleed, không khung viền.

| File | Lá | Tên Việt | Trạng thái |
|---|---|---|---|
| `00-fool.png` | THE FOOL | Kẻ Ngây Thơ | ✅ batch 1 |
| `01-magician.png` | THE MAGICIAN | Pháp Sư | ✅ batch 1 |
| `02-priestess.png` | THE HIGH PRIESTESS | Nữ Tư Tế | ✅ batch 1 |
| `03-empress.png` | THE EMPRESS | Nữ Hoàng | ✅ batch 2 |
| `04-emperor.png` | THE EMPEROR | Hoàng Đế | ✅ batch 2 ⚠️ pose xem chú thích |
| `05-hierophant.png` | THE HIEROPHANT | Giáo Hoàng | ✅ batch 2 |
| `06-lovers.png` | THE LOVERS | Tình Nhân | ✅ batch 2 |
| `07-chariot.png` | THE CHARIOT | Chiến Xa | ✅ 2 sư tử gầm (1 trắng 1 đen) |

> ⚠️ **04-emperor** — tư thế gốc "nằm nghiêng trên ngai" **bị bộ lọc chặn 2 lần**:
> 1. `nằm nghiêng` → chặn → đổi thành ngồi ngự thẳng ✅
> 2. `ngồi nghiêng languid, một chân co` → chặn → đổi thành **ngồi tạc tượng, thân xoay 3/4,
>    dồn trọng tâm một hông, một tay vịn tựa ngai, cằm hơi ngẩng** ✅
> Các lá khác giữ nguyên tư thế gốc (kể cả Empress đang nằm). Chi tiết trong `wardrobe-standard.json` (trường `note`).

> 🦁 **07-chariot** — theo yêu cầu: thay **2 nhân sư** bằng **2 sư tử đang gầm, 1 trắng (trái) 1 đen (phải)**,
> bờm bay, miệng mở giữa tiếng gầm. Sư tử được **miễn trừ** khỏi danh sách chống lẫn
> ("no pair of dogs") để không bị xóa nhầm.

### 🔤 Khóa tên lá (thêm từ bản này)

Mọi prompt giờ có **Spelling lock**: tên lá được đánh vần từng chữ
(`T-H-E E-M-P-R-E-S-S`), cấm thêm/xóa/gấp đôi/đổi chỗ, cấm số La Mã và chữ thừa —
và **cấm nhân vật/đạo cụ che mất chữ**. Kiểm chứng bằng `edge_metric` trên dải chữ
(mẫu 11.6 · các lá 9.9–15.4 · bản lỗi 6.0).

## Cấu trúc

```
cards/
├── <slug>.png              # ảnh lá bài (full-bleed 7:12)
├── prompts/<slug>.txt      # prompt THỰC TẾ đã dùng để sinh ảnh đó
├── manifest.json           # máy đọc được — dùng cho gallery / API
└── README.md               # file này
cards-notext/
└── <slug>.png              # BẢN KHÔNG CHỮ — chỉ xóa dải chữ, tranh giữ nguyên (~1% khác)
```

### 🅰️ Bản không chữ (chắc chắn nhất)

Model viết chữ hay sai (nhầm EMPEROR↔EMPRESS, thiếu/gấp chữ). Cách chắc chắn:
dùng `cards-notext/<slug>.png` rồi tự đặt tên lá bằng đúng font của lá mẫu.

- **5/8 lá đã có bản không chữ**: `00-fool`, `03-empress`, `04-emperor`, `05-hierophant`, `07-chariot`
- Còn thiếu: `01-magician`, `02-priestess`, `06-lovers`
- Gallery có **nút gạt "Có chữ / Không chữ"** ở đầu trang
- Thông số đặt chữ (tọa độ, cỡ chữ, màu): 👉 `04-AI-GUIDE/TITLE-PLACEMENT.md`
- Mẫu chữ phóng to để nhận diện font: 👉 `ref/title-specimen.png`

## 👗 Chuẩn trang phục toàn bộ 78 lá

**Dải lụa mỏng quấn ngang hông** — định nghĩa nằm trong `04-AI-GUIDE/wardrobe-standard.json`:

> `narrow band of fine translucent silk wrapped low across her hips` — dải lụa mỏng quấn thấp qua hông,
> che phần hông và đùi trên; thêm một dải lụa mỏng lướt ngang ngực và voan mỏng bay từ vai.
> **Cấm**: váy, áo choàng, corset, nịt, giáp, dây đai, vải dày/mờ (velvet, brocade).
> Da trần ở vai, lưng, eo, hông, chân — sự gợi cảm đến từ da thịt và dải lụa, không phải từ quần áo.

Sửa chuẩn → sửa **1 file** `wardrobe-standard.json` → chạy lại `make-prompts.py` → 78 lá cùng đổi.
Lá nào cần câu riêng thì thêm vào `scene_rewrites` (theo slug); không có thì dùng `generic_rewrites`.

## ⚠️ Điểm khác so với `03-PROMPTS-78-FULL.md` (bản v4)

`04-AI-GUIDE/make-prompts.py` lấy prompt gốc và áp **4 chỉnh sửa**:

| # | Sửa gì | Vì sao |
|---|---|---|
| 1 | Đoạn "matching … THE MOON reference image" → **STYLE ANCHOR** bằng chữ | Ảnh tham chiếu nguyên lá làm model **kéo bối cảnh THE MOON sang lá khác** |
| 2 | Thêm **Subject lock** + danh sách chống lẫn | Chốt đúng chủ đề, cấm mượn hình lá khác |
| 3 | **Title lettering lock** — bám mẫu chữ `ref/title-lettering.png` | v2 viết chữ tự do → **sai kiểu chữ so với lá mẫu** |
| 4 | **Wardrobe standard** = dải lụa mỏng quấn hông (đọc từ `wardrobe-standard.json`) | Thống nhất trang phục cho cả 78 lá |

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
- **v3** (`6b2feb6`) — + title lettering lock bám mẫu chữ, + vải gossamer siêu mỏng
- **v4** (hiện tại) — **thống nhất trang phục: dải lụa mỏng quấn ngang hông**, chuẩn nằm riêng ở `04-AI-GUIDE/wardrobe-standard.json`

## Sinh thêm lá

```bash
python 04-AI-GUIDE/make-prompts.py      # (1) tạo prompt cho batch
# (2) sinh ảnh bằng công cụ tạo ảnh, lưu thành cards/<slug>.png
python 04-AI-GUIDE/build-gallery.py     # (3) cập nhật index.html + manifest.json
```

Xem gallery: `python3 -m http.server 8000` rồi mở `http://localhost:8000`.
