# 🔮 SENSUAL TAROT 78 LÁ — MASTER PROMPT SPECIFICATION

Bản chuẩn hóa quy chuẩn tạo hình và bố cục toàn bộ 78 lá bài Tarot:

1. **Quy chuẩn hiển thị nội dung & khung viền — `FULL-BLEED v3`**:
   * **Ảnh tham chiếu DUY NHẤT: `cards/17-the-star.jpg`** (bản full-bleed, độ phủ 99.8%).
     ⚠️ **KHÔNG** dùng `17-the-star.png` ở thư mục gốc — đó là bản cũ còn viền bạc + dải giấy da
     (độ phủ 84.1%), đã **khai tử**. Đính kèm bản cũ trong khi prompt ghi "no silver mat" là đưa
     model hai chỉ thị mâu thuẫn, và ảnh luôn thắng chữ → viền bạc quay lại.
   * **Tranh phủ TOÀN BỘ mặt thẻ**, tràn hết 4 cạnh (full bleed). Không viền bạc, không vát xám,
     không lề giấy da, không panel tên riêng.
   * **Viền vàng Gothic mỏng vẽ ĐÈ LÊN TRÊN tranh** như một lớp mạ nổi, tranh chạy tiếp ra ngoài
     và vượt qua viền ở mọi phía.
   * **Tên lá** nằm trên **dải ruy băng vàng mảnh đặt trực tiếp lên tranh**, cảnh vẫn nhìn thấy
     phía sau và bên dưới ruy băng.
   * **Phần ảnh**: phong cách hội họa fine-art của The Star — ánh sáng ấm, chiều sâu không gian
     lùi dần về hậu cảnh, chi tiết sắc nét. Mỗi lá giữ bối cảnh và bảng màu riêng, chỉ chuẩn hóa
     chất lượng nét vẽ, cách đổ sáng và độ chi tiết.
   * **Loại bỏ cổng vòm / cột đá phụ chiếm diện tích**: không dùng cột đá nhân tạo đóng khung gò bó.

   | | Bố cục cũ (khai tử) | `FULL-BLEED v3` |
   |---|---|---|
   | Tranh chiếm | 84.1% | **99.8%** |
   | Lề chết T/B/L/R | 42/43/40/41 px | 0/1/0/1 px |
   | Panel tên | dải giấy da riêng | ruy băng đặt trên tranh |
   | Ảnh tham chiếu | `17-the-star.png` | `cards/17-the-star.jpg` |

2. **Quy chuẩn tạo hình nhân vật (Sensual Fine-Art Figure Standard)**:
   * Kế thừa phong cách tạo hình sống động, gợi cảm và cổ điển từ tài liệu gốc `01-CARD-TABLE.md` (hình mẫu tiêu biểu như lá **The Empress**: *"a voluptuous nude empress, one breast bared, a crown of flowers in loosened hair, reclining on a velvet throne amid ripe golden wheat and fruits, a heart-shaped shield of Venus leaning beside her"*).
   * **100% Nhân vật nữ** trong độ tuổi thanh xuân từ **18 đến 25 tuổi**.
   * Mỗi lá bài giữ nét đặc trưng độc bản về vóc dáng (*slender, voluptuous, athletic, statuesque*), mái tóc và thần thái.
   * **CẤM CƠ THỂ BỊ DI DẠNG (ANATOMY LOCK — HARD RULE)**: Mỗi nhân vật chỉ được có **tối đa 2 tay, 2 chân, 1 đầu, 1 thân**; mọi khớp (vai, khuỷu, cổ tay, hông, gối, cổ chân) phải nối tự nhiên với thân, **không thừa chi, không chi mọc dính vào sườn/hông/ngực, không tay cụt, không khớp biến dạng, không ngón tay sai số lượng**. Kiểm tra giải phẫu kỹ trước khi chốt ảnh: nếu thấy 3 tay / tay dính thân / chân sai khớp → **vẽ lại**, không chấp nhận bản lỗi. Ưu tiên tư thế 2 tay tách rõ khỏi thân (có nách, khuỷu, cổ tay rõ ràng) để giảm nguy cơ lỗi.

3. **Cấu trúc 4 Lớp Chiều Sâu (4-Layer Depth)**:
   * **Lớp 1 (Nền)**: Giấy da cổ (*Aged parchment/vellum*) nhuốm màu thời gian sepia ấm áp.
   * **Lớp 2 (Nội dung)**: Phối cảnh tự nhiên, thoáng đãng với ánh sáng ấm áp và chiều sâu không gian lùi dần về hậu cảnh. **Nội dung được PHÓNG TO, tràn nhẹ xuống dưới mép trong của khung viền vàng.**
   * **Lớp 3 (Khung viền)**: Khung viền mạ vàng Gothic mỏng, sắc nét, đối xứng hoàn hảo — **lấy chuẩn từ lá The Star**. **Hoa văn viền vàng ĐÈ LÊN TRÊN mép nội dung (foreground ornament over background scene) để tạo chiều sâu phân lớp — khung nổi phía trước, cảnh lùi ra sau.**
   * **Lớp 4 (Tên)**:đáy chứa tên lá bài.

---

## Master Prompt Template (`FULL-BLEED v3`)

> Template này là bản rút gọn để đọc. Bản thực thi do `pipeline/build_prompts.py` sinh ra
> (`FRAME_STANDARD` + `TITLE_STANDARD`), luôn đính kèm **`cards/17-the-star.jpg`**.

```text
A single tarot card "{TITLE}". The attached reference image is THE STAR from this same deck,
already in the correct FULL-BLEED layout — copy its layout exactly, and match its painterly
quality, palette discipline and lighting style.

FULL-BLEED LAYOUT — the painted scene covers the ENTIRE card surface, edge to edge and corner
to corner, 100% full bleed. There is NO brushed silver mat, NO grey bevel, NO parchment margin
and NO separate title panel anywhere: the painting itself IS the card. Painted ON TOP of that
full-bleed artwork, keep the thin gothic gold line-art border with its corner flourishes,
floating just inside the card edge like a gilded overlay so the artwork continues past it.

At the bottom, resting directly on the artwork, a slim gold-edged banner ribbon carries the
title "{TITLE}" in antique gold gothic lettering, correctly spelled and centered — the scene
stays visible behind and beneath the banner.

The scene, covering the whole card and running out under the gold border on every side,
composed with generous open space and deep air:
{SCENE}. {CHARACTER_SPECIFICATION} {COUNT_LOCK}

Depth: the painted scene is the full card; the gold line-art border, flourishes and title
banner are painted ON TOP of it. Compose so the subject sits clear of the gold overlay and
nothing important hides behind the banner.

Sensual fine-art anatomy, painterly warm lighting against subtle shadows, rich atmospheric
perspective, crisp detail, symmetrical gold overlay, perfectly centered, portrait 7:12,
vintage gothic fine-art illustration, high detail.

Avoid: no silver border, no grey mat, no brushed metal bevel, no parchment frame, no empty
margins, no letterboxing, no separate title panel, ...
```

---

## Kiểm tra tự động

```bash
python3 pipeline/build_prompts.py     # dừng ngay nếu spec này lệch khỏi FULL-BLEED v3
python3 pipeline/finalize.py check    # báo lá nào tụt về bố cục viền bạc (<93% phủ màu)
```
