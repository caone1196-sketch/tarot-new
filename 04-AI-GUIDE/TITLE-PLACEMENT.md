# 🔤 HƯỚNG DẪN ĐẶT TÊN LÁ BÀI THỦ CÔNG

Dùng khi bạn không tin model viết chữ — sinh ảnh **không chữ**, rồi tự đặt tên lá
bằng đúng font của lá mẫu trong Photoshop / GIMP / Canva / Affinity.

## 1. File bạn cần

| File | Là gì |
|---|---|
| `cards-notext/<slug>.png` | Ảnh lá bài đã **xóa sạch chữ**, phần tranh giữ nguyên (chỉ đổi ~1%) |
| `ref/title-specimen.png` | Chữ **THE MOON** cắt từ lá mẫu, phóng 400% — dùng để nhận diện font |
| `ref/title-lettering.png` | Bản mẫu chữ nền tối (dùng làm `--ref` nếu vẫn muốn model viết) |

## 2. Thông số đặt chữ (đo từ `the moon.png`, khung 784×1360)

```
Trục đứng (y):  dải chữ nằm ở y ≈ 1214 – 1278
                chiều cao chữ hoa ≈ 64px  = 4,7% chiều cao ảnh
                chân chữ cách mép dưới ≈ 82px

Trục ngang (x): canh giữa tại x = 392 (tâm ảnh)
                chiều rộng chữ tối đa ≈ 560px (71% chiều rộng ảnh)
                "THE MOON" (8 ký tự tính cả dấu cách) rộng ≈ 360px
                → trung bình ≈ 45px / ký tự
```

**Quy tắc co giãn:** giữ nguyên **chiều cao chữ ≈ 64px**; nếu tên dài (vd
`THE HIGH PRIESTESS` = 18 ký tự → ~810px, quá rộng) thì **giảm cỡ chữ** sao cho
chiều rộng không vượt 560px, rồi canh giữa lại theo trục đứng của dải chữ.

## 3. Kiểu chữ cần khớp với lá mẫu

- Kiểu: **antique serif in hoa**, nét đều, chân chữ rõ
- Màu: **vàng ấm** (antique gold), có **viền sáng bên trong** nét chữ
- Có **đổ bóng tối mềm** phía dưới để nổi trên nền tranh
- Giãn chữ vừa phải (không dính, không quá xa)
- **Chỉ có tên lá** — không số La Mã, không phụ đề, không dòng thứ hai

> Soi `ref/title-specimen.png` ở 400% để thấy rõ chân chữ và highlight;
> có thể đưa file này vào WhatTheFont / Fontspring Matcherator để tìm font gần nhất.

## 4. Tên 8 lá đã làm (để copy cho đúng chính tả)

| Slug | Tên tiếng Anh | Tên Việt |
|---|---|---|
| `00-fool` | THE FOOL | Kẻ Ngây Thơ |
| `01-magician` | THE MAGICIAN | Pháp Sư |
| `02-priestess` | THE HIGH PRIESTESS | Nữ Tư Tế |
| `03-empress` | THE EMPRESS | Nữ Hoàng |
| `04-emperor` | THE EMPEROR | Hoàng Đế |
| `05-hierophant` | THE HIEROPHANT | Giáo Hoàng |
| `06-lovers` | THE LOVERS | Tình Nhân |
| `07-chariot` | THE CHARIOT | Chiến Xa |

⚠️ Cặp dễ nhầm: **EMPEROR** (chữ O, vua) ↔ **EMPRESS** (chữ S kép, nữ hoàng).

## 5. Quy trình khuyến nghị

```bash
# 1. sinh bản không chữ cho các lá mới (sửa cục bộ, giữ nguyên tranh)
#    -> ảnh nằm ở cards-notext/<slug>.png
# 2. mở cards-notext/<slug>.png trong Photoshop
# 3. thêm text layer: font antique serif, IN HOA, màu vàng, size ~64px cap height
# 4. canh giữa x=392, đặt baseline sao cho chân chữ cách đáy ~82px
# 5. export PNG 784×1360 -> lưu đè lên cards/<slug>.png
python 04-AI-GUIDE/build-gallery.py     # cập nhật gallery
```

## 6. Nếu vẫn muốn model viết chữ

Prompt đã có sẵn 3 lớp bảo vệ: **Spelling lock** (đánh vần từng chữ) +
**Disambiguation lock** (chống nhầm EMPEROR/EMPRESS) + **khóa chống che chữ**.
Chạy `python 04-AI-GUIDE/make-prompts.py <slug>` rồi sinh ảnh kèm
`--ref ref/title-lettering.png`.
