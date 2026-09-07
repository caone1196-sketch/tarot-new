# 🔮 SENSUAL TAROT 78 LÁ — MASTER PROMPT SPECIFICATION (v3 · FULL-DETAIL)

Bản chuẩn hóa quy chuẩn tạo hình và bố cục toàn bộ 78 lá bài Tarot.

**Thay đổi chính của v3** (so với v2):

1. **Prompt đầy đủ 100% — không còn slot trống**: mỗi lá là MỘT prompt khép kín gồm **bối cảnh chi tiết (scene) + toàn bộ 8 thông số nhân vật** (tuổi · mắt: màu + dáng + ánh nhìn · tóc · màu da · vóc dáng A–D · nét riêng · không khí) + **emblem** + **count lock**. Bộ prompt dựng sẵn: `03-PROMPTS-78-FULL.md` (copy-paste được ngay) và `prompts-full.json` (bản máy đọc).
2. **SKIN TONE LOCK — khóa màu da toàn lá (HARD RULE)**: mọi nhân vật trên mỗi lá — nhân vật chính, người tình/bạn đồng hành, đám đông, trẻ em, cả tay thần thánh — **chỉ dùng 10 tông da sáng** `porcelain → amber-gold`. **Loại bỏ hoàn toàn nhân vật da đen / da sẫm**: đã rà sạch và sửa trong `cards.json` (lá Judgement từng có *"one deep-skinned with tight black coils"* → thay bằng *"one porcelain-skinned with soft raven-black waves"*; tương tự Four/Five of Wands) và áp khóa vào cả 78 prompt.
3. **Thống nhất anchor THE MOON** (`the moon.png`) cho cả viền ngoài lẫn ảnh trong — v3 sửa nốt câu template cũ còn ghi "THE STAR".
4. Thêm **emblem từng lá** (lấy từ `cards.json`) vào medallion tròn phía trên.

---

## 1. Quy chuẩn khung viền & hiển thị nội dung (Visual Anchor Standard — THE MOON)

* Lấy lá **`the moon.png`** làm quy chuẩn DUY NHẤT cho toàn bộ bộ bài — chuẩn cho cả **phần ảnh bên trong** lẫn **phần viền bên ngoài**.
* **Viền ngoài**: khung viền mạ vàng Gothic mỏng, sắc nét, đối xứng hoàn hảo trên nền giấy da cổ (*aged parchment/vellum*).
* **Ảnh trong**: phong cách hội họa fine-art — phối cảnh thoáng đãng, ánh sáng ấm, chiều sâu không gian lùi dần về hậu cảnh, chi tiết sắc nét. Mỗi lá giữ bối cảnh và bảng màu riêng, chỉ chuẩn hóa theo chất lượng nét vẽ, cách đổ sáng và độ chi tiết của The Moon.
* Vùng nội dung mở rộng tối đa, phủ kín toàn bộ vòm trung tâm từ mép này sang mép kia của khung viền Gothic mỏng. **Loại bỏ cổng vòm / cột đá phụ**: không dùng cột đá nhân tạo đóng khung, để không gian khoáng đạt tự nhiên theo đúng bối cảnh từng lá.
* **Cách dùng thực tế**: mỗi lần tạo ảnh, đính kèm 2 ảnh tham chiếu — `card-blank.png` (vị trí 1: khung trống) và `the moon.png` (vị trí 2: chuẩn phong cách) — rồi dán prompt của lá cần tạo.

## 2. Quy chuẩn tạo hình nhân vật (Sensual Fine-Art Figure Standard)

* **100% nhân vật nữ**, độ tuổi **18–25**, gợi cảm · uyển chuyển · mê hoặc (không dùng ngôn ngữ chiến binh/cơ bắp/vai rộng).
* Vóc dáng chuẩn hóa 4 cấp, **trần là "trung bình"**: **A** thanh mảnh (29 lá) · **B** thon gọn (30 lá) · **C** trung bình mềm (9 lá) · **D** trung bình đầy đặn (4 lá: 03-empress, 15-devil, wands-queen, pentacles-queen). Không plus-size, không phóng đại.
* **8 trường bắt buộc cho mỗi nhân vật** (tổ hợp không trùng lặp giữa 72 nhân vật):

| # | Trường | Nội dung |
|---|---|---|
| 1 | **Tuổi** | 18–25, cố định theo bảng chuẩn `01-CARD-TABLE.md` |
| 2 | **Đôi mắt** | Màu + dáng (almond, doe, heavy-lidded, hooded, upturned, cat, round, narrow, wide-set, dreamy) + ánh nhìn riêng |
| 3 | **Tóc** | Kiểu dáng + màu, giữ nguyên 100% so với bảng chuẩn |
| 4 | **Màu da** | 1 trong 10 tông sáng (xem mục 3) — thuộc tính CỐ ĐỊNH, không đổi khi vẽ lại |
| 5 | **Vóc dáng** | Cấp A–D + mô tả chi tiết |
| 6 | **Nét riêng (signature)** | Đúng 1 chi tiết độc bản: nốt ruồi, sẹo nhỏ, tàn nhang, xăm nhỏ, khuyên, lúm đồng tiền, bớt… |
| 7 | **Không khí (aura)** | 3–4 từ khoá cảm xúc/bối cảnh của nhân vật |
| 8 | **Trang phục** | Theo scene (voan lụa trong suốt / tương ứng bối cảnh từng lá) |

* **ANATOMY LOCK (HARD RULE)**: mỗi nhân vật tối đa **2 tay, 2 chân, 1 đầu, 1 thân**; mọi khớp nối tự nhiên — không thừa chi, không chi mọc dính sườn/hông/ngực, không tay cụt, không khớp biến dạng, không sai số lượng ngón. Ưu tiên tư thế 2 tay tách rõ khỏi thân. Thấy lỗi giải phẫu → vẽ lại, không chấp nhận.

## 3. SKIN TONE LOCK (HARD RULE) — loại bỏ nhân vật da đen / da sẫm

Toàn bộ nhân vật trên mọi lá chỉ dùng **10 tông da sáng**, kể cả khi đổ bóng/ánh nến không được làm da sẫm hơn tông gốc:

| Tông da | Mô tả (English cho prompt) |
|---|---|
| `porcelain` | cool porcelain-white with faint blue veining and a pearlescent sheen |
| `ivory` | warm ivory-white, smooth as silk |
| `fair` | soft fair skin with a pearly blush |
| `warm peach` | warm peach, sun-kissed with a natural rosy glow |
| `light olive` | light warm olive, faintly golden at the shoulders and arms |
| `sand` | even, smooth warm sand |
| `warm tan` | lightly sun-warmed tan with a soft bronze blush at the shoulders and cheeks |
| `honey` | golden honey, glinting in sunlight |
| `light bronze` | light gleaming bronze — still a luminous light tone |
| `amber-gold` | amber-gold, glowing warm in candlelight |

* Khóa áp dụng cho **MỌI người xuất hiện trên lá**: nhân vật chính + nhân vật phụ (người tình, người đồng hành, đám đông, trẻ em, tu sĩ, người lữ khách…) — tất cả đều da sáng.
* **Kỹ thuật prompt**: nêu whitelist 10 tông trước, cấm tông sẫm sau — tránh để model "vẽ ra thứ được nhắc đến". Câu khóa chuẩn (đã nhúng sẵn trong từng prompt):

```text
Skin-tone lock (hard rule): every human figure on this card — the main figure and every
secondary or background figure (partners, companions, crowds, children) — is light-skinned
only, within these ten tones: porcelain, ivory, fair, warm peach, light olive, sand,
warm tan, honey, light bronze, amber-gold. No deep bronze, dark-brown or Black skin tones
appear anywhere on the card; lighting, shadow and candle glow must never darken skin
beyond these tones.
```

## 4. COUNT LOCK (đếm vật phẩm)

* Mỗi lá có số vật phẩm bắt buộc (kiếm/chén/gậy/đồng xu) khai báo trong `cards.json` (`count.n` = ràng buộc CỨNG, `count.layout` = cách xếp + cách đếm).
* Lá không có vật phẩm suit (`count = null`) → phát câu khóa *"no extra suit objects"*.
* Câu khóa được nhúng sẵn vào cuối mỗi prompt trong `03-PROMPTS-78-FULL.md`.

## 5. Cấu trúc 4 Lớp Chiều Sâu (4-Layer Depth)

* **Lớp 1 (Nền)**: giấy da cổ nhuốm sepia ấm.
* **Lớp 2 (Nội dung)**: phối cảnh tự nhiên thoáng đãng, ánh sáng ấm, chiều sâu lùi dần; nội dung **PHÓNG TO, tràn nhẹ xuống dưới mép trong của khung viền vàng**.
* **Lớp 3 (Khung viền)**: viền vàng Gothic mỏng lấy chuẩn từ The Moon; **hoa văn viền ĐÈ LÊN mép nội dung** (foreground ornament over background scene) — khung nổi phía trước, cảnh lùi ra sau.
* **Lớp 4 (Tên)**: ribbon banner đáy chứa tên lá; medallion tròn trên chứa emblem.

---

## 6. MASTER PROMPT TEMPLATE v3 (Chuẩn THE MOON)

Các slot: `{TITLE}` tên lá · `{EMBLEM}` huy hiệu · `{SCENE}` bối cảnh · `{CHARACTER_SPECIFICATION}` khối 8 thông số nhân vật · `{COUNT_LOCK}`.

```text
A single tarot card "{TITLE}" built inside the reference frame, matching the EXACT open window display, scale and lighting style of THE MOON (reference image): keep the intricate thin golden line-art border in vintage gothic style and the aged parchment background texture.

At the TOP, inside the small oval medallion: the emblem of this card — {EMBLEM} — drawn in fine antique gold line art.
At the BOTTOM, inside the ribbon banner: the title "{TITLE}" in clean antique gold lettering.

In the large open center panel — filling the entire inner window edge to edge, bleeding slightly beneath the golden border, open and natural, with no heavy inner arches and no added columns:
{SCENE}.

{CHARACTER_SPECIFICATION}

Skin-tone lock (hard rule): every human figure on this card — the main figure and every secondary or background figure (partners, companions, crowds, children) — is light-skinned only, within these ten tones: porcelain, ivory, fair, warm peach, light olive, sand, warm tan, honey, light bronze, amber-gold. No deep bronze, dark-brown or Black skin tones appear anywhere on the card; lighting, shadow and candle glow must never darken skin beyond these tones.

Anatomy lock (hard rule): each figure has exactly two arms, two legs, one head and one torso; every joint (shoulders, elbows, wrists, hips, knees, ankles) connects naturally to the body — no extra or fused limbs, no limbs sprouting from the torso, no stub arms, no malformed joints, no wrong finger counts. Prefer poses with both arms clearly separated from the torso. If any anatomy error appears, redraw it rather than accept it.

{COUNT_LOCK}

Depth layering: enlarge the scene so its edges extend slightly beneath the inner edge of the golden border, then paint the thin golden line-art border, corner flourishes, oval medallion and ribbon banner ON TOP of the scene edges — foreground ornament overlapping the background content for a strong layered sense of depth.

Sensual fine-art anatomy, painterly warm lighting against subtle shadows, rich atmospheric perspective and depth, symmetrical golden frame border, perfectly centered, portrait orientation 7:12 aspect ratio, vintage gothic fine-art illustration, high detail.
```

### 6.1 Định dạng khối `{CHARACTER_SPECIFICATION}` (8 trường)

```text
Main figure — {VAI DIỆN} — render exactly as specified: a {TUỔI}-year-old young woman.
Eyes: {MÀU MẮT}, {DÁNG MẮT} — {ÁNH NHÌN}.
Hair: {KIỂU TÓC + MÀU}.
Skin: {TÔNG DA} — {MÔ TẢ TÔNG DA}.
Build: {CẤP A/B/C/D} — {MÔ TẢ VÓC DÁNG}.
Signature detail: {NÉT RIÊNG}.
Aura: {KHÔNG KHÍ}.
```

* Lá nhiều nhân vật (Three of Cups, Five of Wands, Judgement…): nhân vật chính dùng khối trên, nhân vật phụ mô tả ngay trong `{SCENE}` — **tất cả đều da sáng**, mỗi người một khuôn mặt + vóc dáng riêng.
* 6 lá vật thể thuần không có khối nhân vật: `wands-ace`, `wands-08`, `cups-ace`, `swords-ace`, `swords-03`, `pentacles-ace`.

### 6.2 Định dạng `{COUNT_LOCK}`

* Có vật phẩm: `Count lock (hard rule): {count.layout từ cards.json}`
* Không vật phẩm: `Count lock: no extra suit objects — do not add any additional wands, cups, swords or pentacle coins anywhere on this card beyond those described above.`

---

## 7. Ví dụ hoàn chỉnh — THE MOON (lá anchor)

```text
A single tarot card "THE MOON" built inside the reference frame, matching the EXACT open window display, scale and lighting style of THE MOON (reference image): keep the intricate thin golden line-art border in vintage gothic style and the aged parchment background texture.

At the TOP, inside the small oval medallion: the emblem of this card — a crescent moon dripping dew — drawn in fine antique gold line art.
At the BOTTOM, inside the ribbon banner: the title "THE MOON" in clean antique gold lettering.

In the large open center panel — filling the entire inner window edge to edge, bleeding slightly beneath the golden border, open and natural, with no heavy inner arches and no added columns:
a pale moon with a serene face dropping dew, two towers and a winding path, a nude water nymph rising from the dark pool with water streaming over her bare shoulders, a wolf and a dog howling, a crayfish in the water.

Main figure — the water nymph — render exactly as specified: a 21-year-old young woman.
Eyes: heavy-lidded moonstone silver-violet eyes, dreamy.
Hair: ink-blue-black hair with cool silvery highlights, cascading like water to her hips.
Skin: porcelain — cool porcelain-white with faint blue veining and a pearlescent sheen.
Build: Level A — slender — slender as a fairy, soft waist, gently curved hips.
Signature detail: a small crescent scar on her left cheekbone.
Aura: mist, a dark lake, the sound of water.

Skin-tone lock (hard rule): every human figure on this card — the main figure and every secondary or background figure (partners, companions, crowds, children) — is light-skinned only, within these ten tones: porcelain, ivory, fair, warm peach, light olive, sand, warm tan, honey, light bronze, amber-gold. No deep bronze, dark-brown or Black skin tones appear anywhere on the card; lighting, shadow and candle glow must never darken skin beyond these tones.

Anatomy lock (hard rule): each figure has exactly two arms, two legs, one head and one torso; every joint (shoulders, elbows, wrists, hips, knees, ankles) connects naturally to the body — no extra or fused limbs, no limbs sprouting from the torso, no stub arms, no malformed joints, no wrong finger counts. Prefer poses with both arms clearly separated from the torso. If any anatomy error appears, redraw it rather than accept it.

Count lock: no extra suit objects — do not add any additional wands, cups, swords or pentacle coins anywhere on this card beyond those described above.

Depth layering: enlarge the scene so its edges extend slightly beneath the inner edge of the golden border, then paint the thin golden line-art border, corner flourishes, oval medallion and ribbon banner ON TOP of the scene edges — foreground ornament overlapping the background content for a strong layered sense of depth.

Sensual fine-art anatomy, painterly warm lighting against subtle shadows, rich atmospheric perspective and depth, symmetrical golden frame border, perfectly centered, portrait orientation 7:12 aspect ratio, vintage gothic fine-art illustration, high detail.
```

---

## 8. Nguồn dữ liệu & kiểm tra

| File | Vai trò |
|---|---|
| `cards.json` | Nguồn dữ liệu 78 lá (scene/emblem/count) — **v3 đã sửa sạch mô tả da sẫm** |
| `01-CARD-TABLE.md` | Bảng chuẩn 72 nhân vật (tuổi · mắt · tóc · da · vóc dáng · nét riêng · không khí) |
| `03-PROMPTS-78-FULL.md` | **78 prompt hoàn chỉnh, copy-paste được ngay** |
| `prompts-full.json` | Bản máy đọc được của 78 prompt |
| `card-blank.png` / `the moon.png` | 2 ảnh tham chiếu đính kèm khi tạo ảnh (vị trí 1 / vị trí 2) |

Checklist v3:
- [x] 78/78 prompt khép kín: khung THE MOON + emblem + scene chi tiết + 8 thông số nhân vật + 3 khóa (skin/anatomy/count)
- [x] 72/72 nhân vật nữ 18–25 có đủ: mắt (màu+dáng+ánh nhìn) · tóc · da · vóc dáng A–D · nét riêng · không khí
- [x] 0 nhân vật da đen/da sẫm — 10 tông sáng `porcelain → amber-gold`, khóa áp dụng cho cả nhân vật phụ & hậu cảnh
- [x] 0 nhân vật vượt trần "trung bình" (A 29 · B 30 · C 9 · D 4)
- [x] Mỗi nhân vật 1 tổ hợp mắt duy nhất + 1 nét riêng duy nhất
- [x] Count lock nhúng sẵn trong từng prompt (kể cả cảnh báo lỗi đếm của swords-07, swords-08)
