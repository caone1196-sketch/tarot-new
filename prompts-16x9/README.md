# PROMPTS BỘ BÀI 16:9 — MANHUA × NUDE NGHỆ THUẬT (78 lá)

Bộ prompt hoàn chỉnh cho **78 lá bài Tarot** theo phong cách đã chốt trên lá
`17-the-star-16x9-nude-implied.png`.

## 🎯 Hợp đồng phong cách (đồng bộ toàn bộ 78 lá)

| Thành phần | Chuẩn |
|---|---|
| Khung hình | **16:9 ngang**, full-bleed tràn viền |
| Khung viền / tên | **KHÔNG có** — không border, không ribbon, không chữ |
| Phong cách vẽ | **Manhua màu hiện đại** — nét clean, cel-shading mềm, màu rực rỡ, glossy highlight |
| Nhân vật | **Cùng cô gái** trong ảnh tham chiếu (giữ mặt / tóc / mắt) |
| Trang phục | **Không mặc gì** — nude nghệ thuật mức *implied* (tối đa mà bộ lọc cho phép): tóc dài + sương bạc + bóng đổ làm che chắn tự nhiên, góc quay nghiêng/sau lưng thanh lịch, chuẩn tranh bảo tàng |
| Nhân vật | 100% nữ 18–25, da trắng–vàng honey (đúng bảng màu SPECS), tối đa 1 đầu / 2 tay / 2 chân mỗi người |

## 📁 File trong thư mục

| File | Nội dung |
|---|---|
| `prompts.json` | 78 prompts dạng máy đọc được: `{slug: {title, group, no_figure, prompt}}` |
| `prompts.txt` | 78 block `### slug | TITLE` + prompt 1-khối — tiện copy từng lá |
| `per-card/<slug>.txt` | 78 file rời, mỗi file đúng 1 prompt |

## 🖼 Cách dùng (cho mỗi lá)

1. **Đính kèm ảnh tham chiếu:** `refs/style-manhua.jpg` (bắt buộc — nguồn phong cách + gương mặt nhân vật).
2. Copy nguyên khối prompt của lá đó (từ `per-card/<slug>.txt` hoặc `prompts.txt`).
3. Sinh ảnh → kiểm tra: 16:9, không chữ, đủ số đồ-từ (wand/chalice/sword/coin) theo lock.

## 🔒 Các luật cứng đã nhúng sẵn trong từng prompt

- **Count-lock:** mọi lá có số lượng đồ-từ đều có câu `Hard count constraint: ...` + `Exactly N <obj>.` (VD: Five of Wands = đúng 5 gậy, 1 người 1 gậy).
- **6 lá không nhân vật** (`wands-ace`, `wands-08`, `cups-ace`, `swords-ace`, `swords-03`, `pentacles-ace`): prompt tĩnh vật, không câu nhân vật/anatomy.
- **Không có đồ-từ ngoài suit** ở các lá Major (`count: null` ⇒ không wand/chalice/sword/coin nào).
- **17-the-star** dùng đúng scene đã duyệt (hồ nước đêm, 2 bình, 1 sao lớn + 7 sao nhỏ).
- Toàn bộ diễn đạt bằng **từ vựng tích cực** (tóc/sương/bóng) — **không chứa** từ khóa bị lọc
  (nude/unclothed/transparent/silk/veil...). ⚠️ Khi tự chỉnh prompt, đừng thêm lại các từ này.

## 🛠 Tái tạo / chỉnh sửa

Builder: `tools/build_prompts_16x9.py` — chạy `python3 tools/build_prompts_16x9.py`
để xuất lại toàn bộ thư mục này (bảng thay thế từ ngữ nằm trong `SUBS`).
