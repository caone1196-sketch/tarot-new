# 🔮 SENSUAL TAROT 78 LÁ — MASTER PROMPT SPECIFICATION

Bản chuẩn hóa quy chuẩn tạo hình và bố cục toàn bộ 78 lá bài Tarot:

1. **Quy chuẩn hiển thị nội dung & khung viền (Visual Anchor Standard — the moon)**:
   * Lấy lá **`the moon.png`** làm quy chuẩn DUY NHẤT cho toàn bộ bộ bài — chuẩn cho cả **phần ảnh bên trong** lẫn **phần viền bên ngoài**.
   * **Phần viền ngoài**: khung viền mạ vàng Gothic mỏng, sắc nét, đối xứng hoàn hảo trên nền giấy da cổ (*aged parchment/vellum*).
   * **Phần ảnh bên trong**: phong cách hội họa fine-art của The Star — phối cảnh thoáng đãng, ánh sáng ấm, chiều sâu không gian lùi dần về hậu cảnh, chi tiết sắc nét. Mỗi lá vẫn giữ bối cảnh và bảng màu riêng của mình, chỉ chuẩn hóa về chất lượng nét vẽ, cách đổ sáng và độ chi tiết theo The Star.
   * Vùng hiển thị nội dung mở rộng tối đa, phủ kín toàn bộ vòm trung tâm từ mép này sang mép kia của khung viền Gothic mỏng.
   * **Loại bỏ cổng vòm / cột đá phụ chiếm diện tích**: Không dùng cột đá nhân tạo đóng khung gò bó, để không gian khoáng đạt, tự nhiên theo đúng bối cảnh của từng lá bài.

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

## Master Prompt Template (Chuẩn The Star)

```text
A single tarot card "{TITLE}" built inside the reference frame, matching the EXACT open window display, scale, and lighting style of THE STAR: keep the intricate thin golden line-art border in vintage gothic style and aged parchment background texture.

At the BOTTOM: inside the ribbon banner, the title "{TITLE}" in clean antique gold lettering.

In the large open center panel (filling the entire inner window edge to edge and bleeding slightly beneath the golden border, matching the open space of The Star without heavy inner arch barriers):
{SCENE}. {CHARACTER_SPECIFICATION} {COUNT_LOCK}

Depth layering: enlarge the scene so its edges extend slightly beneath the inner edge of the golden border, then paint the thin golden line-art border, corner flourishes, oval medallion and ribbon banner ON TOP of the scene edges — foreground ornament overlapping the background content for a strong sense of depth.

Sensual fine-art anatomy, painterly warm lighting against subtle shadows, rich atmospheric perspective and depth, symmetrical golden frame border, perfectly centered, portrait orientation 7:12 aspect ratio, vintage gothic fine-art illustration, high detail.
```
