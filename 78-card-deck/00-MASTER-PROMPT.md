# 🔮 SENSUAL TAROT 78 LÁ — MASTER PROMPT SPECIFICATION

Bản chuẩn hóa quy chuẩn tạo hình và bố cục toàn bộ 78 lá bài Tarot:

1. **Quy chuẩn hiển thị nội dung & khung viền (Visual Anchor Standard — the moon)**:
   * Lấy lá **`08-strength.png`** làm tham chiếu DUY NHẤT cho **nhân vật, ánh sáng, màu sắc và chất liệu hội họa**. KHÔNG sao chép bất kỳ khung viền nào.
   * **Phần viền ngoài**: LOẠI BỎ HOÀN TOÀN khung viền, đường viền vàng, hoa văn góc, nền giấy da và mọi ornament bao quanh. Hình ảnh phải full-bleed sát cả bốn mép canvas.
   * **Phần ảnh bên trong**: phong cách hội họa fine-art theo `08-strength.png` — phối cảnh thoáng đãng, ánh sáng khí quyển, chiều sâu không gian lùi dần về hậu cảnh, chi tiết sắc nét. Mỗi lá vẫn giữ bối cảnh và bảng màu riêng của mình, chỉ chuẩn hóa về chất lượng nét vẽ, cách đổ sáng và độ chi tiết theo tham chiếu The Strength reference.
   * Vùng hiển thị nội dung full-bleed, phủ kín toàn bộ canvas từ mép này sang mép kia, không khung viền, không lề giấy da, không panel inset.
   * **Loại bỏ cổng vòm / cột đá phụ chiếm diện tích**: Không dùng cột đá nhân tạo đóng khung gò bó, để không gian khoáng đạt, tự nhiên theo đúng bối cảnh của từng lá bài.

2. **Quy chuẩn tạo hình nhân vật (Sensual Fine-Art Figure Standard)**:
   * Kế thừa phong cách tạo hình sống động, gợi cảm và cổ điển từ tài liệu gốc `01-CARD-TABLE.md` (hình mẫu tiêu biểu như lá **The Empress**: *"a voluptuous nude empress, one breast bared, a crown of flowers in loosened hair, reclining on a velvet throne amid ripe golden wheat and fruits, a heart-shaped shield of Venus leaning beside her"*).
   * **100% Nhân vật nữ** trong độ tuổi thanh xuân từ **18 đến 25 tuổi**.
   * Mỗi lá bài giữ nét đặc trưng độc bản về vóc dáng (*slender, voluptuous, athletic, statuesque*), mái tóc và thần thái.
   * **CẤM CƠ THỂ BỊ DI DẠNG (ANATOMY LOCK — HARD RULE)**: Mỗi nhân vật chỉ được có **tối đa 2 tay, 2 chân, 1 đầu, 1 thân**; mọi khớp (vai, khuỷu, cổ tay, hông, gối, cổ chân) phải nối tự nhiên với thân, **không thừa chi, không chi mọc dính vào sườn/hông/ngực, không tay cụt, không khớp biến dạng, không ngón tay sai số lượng**. Kiểm tra giải phẫu kỹ trước khi chốt ảnh: nếu thấy 3 tay / tay dính thân / chân sai khớp → **vẽ lại**, không chấp nhận bản lỗi. Ưu tiên tư thế 2 tay tách rõ khỏi thân (có nách, khuỷu, cổ tay rõ ràng) để giảm nguy cơ lỗi.

3. **Cấu trúc 4 Lớp Chiều Sâu (4-Layer Depth)**:
   * **Lớp 1 (Nền)**: Nền cảnh của chính lá bài, chạy sát cả bốn mép canvas; không dùng giấy da làm lề ngoài.
   * **Lớp 2 (Nội dung)**: Phối cảnh tự nhiên full-bleed, ánh sáng khí quyển, chiều sâu lùi dần về hậu cảnh; không cắt khung nội dung.
   * **Lớp 3 (Khung viền)**: KHÔNG CÓ KHUNG VIỀN. Không vẽ đường viền, hoa văn góc, medallion, emblem, icon, banner hay ornament bao quanh.
   * **Lớp 4 (Tên)**:đáy chứa tên lá bài.

---

## Master Prompt Template (Chuẩn 08-strength.png)

```text
A single borderless tarot card "{TITLE}" built as full-bleed artwork on a portrait canvas, matching the character rendering, atmospheric lighting, scale and color depth of 08-strength.png only. Do not reproduce its frame, parchment margin, corner ornaments, medallion, emblem, icon or banner.

At the BOTTOM: place the title "{TITLE}" directly over the artwork in clean antique-gold Gothic lettering, with no ribbon, banner, frame or box.

In the full-bleed portrait canvas (filling the entire image edge to edge with no border or inset panel):
{SCENE}. {CHARACTER_SPECIFICATION} {COUNT_LOCK}

Depth layering: let the scene fill the entire canvas edge to edge. Do not paint any frame, border, corner flourishes, medallion, emblem, icon, banner, or parchment margin over the artwork. The title is the only graphic text and sits directly over the bottom of the scene. Symbols explicitly required inside the card scene remain part of that scene.

Sensual fine-art anatomy, painterly warm lighting against subtle shadows, rich atmospheric perspective and depth, perfectly centered, portrait orientation 7:12 aspect ratio, vintage fine-art illustration, ultra-high detail, razor-sharp microdetail, crisp fine brushwork, no blur or soft focus, high-resolution finish, high pixel density. Minimal wardrobe lock: use only the garments explicitly named in cards.json, with no added armor, costume layers, shoes, or modern clothing.
```
