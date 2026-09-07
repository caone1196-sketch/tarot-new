# 🔮 SENSUAL TAROT 78 LÁ — MASTER PROMPT SPECIFICATION (v5 · FULL-BLEED + QUALITY)

Bản chuẩn hóa quy chuẩn tạo hình và bố cục toàn bộ 78 lá bài Tarot.

**Thay đổi chính của v5** (so với v4):

1. **Thêm QUALITY LOCK (HARD RULE)** — khóa chất lượng chống **nhòe · vỡ nét · noise** khi sinh ảnh, tối đa hóa chi tiết: nét sắc như dao cạo trên nhân vật & tiền cảnh, chất liệu được vẽ rõ (sợi tóc, làn da, sợi lụa, hạt đá, giọt nước), cấm toàn bộ blur/noise/grain/artifact/nét nhân bản/màu bệt. Xem mục 5.
2. Câu kết prompt nâng cấp: *"Masterpiece quality — ultra-detailed, razor-sharp, pristine high-fidelity rendering."*
3. Thêm mục 9 — **Kinh nghiệm sinh ảnh** (cài đặt ngoài prompt để lấy chất lượng cao nhất).

Giữ nguyên từ v4: bố cục **full-bleed** (bỏ khung · bỏ emblem · bỏ ribbon banner, chỉ giữ tên lá bài dưới đáy ảnh), FRAMING LOCK, 8 thông số nhân vật, SKIN TONE LOCK (10 tông da sáng — loại bỏ nhân vật da đen/da sẫm), ANATOMY LOCK, COUNT LOCK.

---

## 1. Quy chuẩn bố cục (Full-Bleed Layout Standard)

* Tranh **phủ kín 4 cạnh khung hình** — không viền, không khung, không hoa văn mép, không nền giấy da: bối cảnh vẽ tràn ra tận mép trên/dưới/trái/phải như một bức hội họa cổ điển hoàn chỉnh.
* **Chữ trên ảnh**: chỉ duy nhất **tên lá bài** (VD: "THE MOON") — kiểu chữ cổ điển thanh lịch, phủ nhẹ **dưới đáy ảnh**, có bóng mờ nhẹ để đọc được trên mọi nền. Không chữ nào khác xuất hiện.
* **Không có**: khung viền vàng Gothic · medallion emblem · ribbon banner · parchment · hoa văn góc · bất kỳ chi tiết trang trí "bộ bài" nào bao quanh tranh.
* **Cách dùng thực tế**: (tùy chọn) đính kèm `the moon.png` làm tham chiếu phong cách ảnh trong — prompt đã ghi rõ *ignore the reference image's outer border and frame*.

## 2. Quy chuẩn tạo hình nhân vật (Sensual Fine-Art Figure Standard)

* **100% nhân vật nữ**, độ tuổi **18–25**, gợi cảm · uyển chuyển · mê hoặc (không dùng ngôn ngữ chiến binh/cơ bắp/vai rộng).
* Vóc dáng 4 cấp, trần là "trung bình": **A** thanh mảnh (29 lá) · **B** thon gọn (30 lá) · **C** trung bình mềm (9 lá) · **D** trung bình đầy đặn (4 lá: 03-empress, 15-devil, wands-queen, pentacles-queen). Không plus-size, không phóng đại.
* **8 trường bắt buộc cho mỗi nhân vật** (tổ hợp không trùng lặp giữa 72 nhân vật):

| # | Trường | Nội dung |
|---|---|---|
| 1 | **Tuổi** | 18–25, cố định theo bảng chuẩn `01-CARD-TABLE.md` |
| 2 | **Đôi mắt** | Màu + dáng (almond, doe, heavy-lidded, hooded, upturned, cat, round, narrow, wide-set, dreamy) + ánh nhìn riêng |
| 3 | **Tóc** | Kiểu dáng + màu, giữ nguyên 100% so với bảng chuẩn |
| 4 | **Màu da** | 1 trong 10 tông sáng (mục 3) — thuộc tính CỐ ĐỊNH, không đổi khi vẽ lại |
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
* Câu khóa chuẩn (đã nhúng sẵn trong từng prompt):

```text
Skin-tone lock (hard rule): every human figure on this card — the main figure and every
secondary or background figure (partners, companions, crowds, children) — is light-skinned
only, within these ten tones: porcelain, ivory, fair, warm peach, light olive, sand,
warm tan, honey, light bronze, amber-gold. No deep bronze, dark-brown or Black skin tones
appear anywhere on the card; lighting, shadow and candle glow must never darken skin
beyond these tones.
```

## 4. COUNT LOCK (đếm vật phẩm)

* Mỗi lá có số vật phẩm suit (kiếm/chén/gậy/đồng xu) khai báo trong `cards.json` (`count.n` = ràng buộc CỨNG, `count.layout` = cách xếp + cách đếm).
* Lá không có vật phẩm suit (`count = null`) → phát câu khóa *"no extra suit objects"*.
* Cờ/đạo cụ **trong bối cảnh** (cờ đen của Death, cờ đỏ của The Sun…) vẫn được giữ — FRAMING LOCK chỉ cấm banner/chữ trang trí *khung card*.

## 5. QUALITY LOCK (HARD RULE — mới của v5, chống nhòe · vỡ nét · noise)

Câu khóa nhúng sẵn trong từng prompt, **sau COUNT LOCK, trước câu kết**:

```text
Quality lock (hard rule): gallery-grade, maximum-detail rendering — razor-sharp focus on
the main figure and all foreground details; crisp, clean edges everywhere; fine resolved
textures: individual hair strands, smooth glowing skin with clear highlights, woven silk
fibers, stone grain, water droplets, leaf veins; rich micro-detail in fabric, jewelry and
background architecture. Absolutely no blur, no soft-focus haze on the subject, no motion
smear, no noise, no film grain, no speckles, no color banding, no JPEG or compression
artifacts, no blocky pixelation, no smudged or melted details, no duplicated or double
edges, no washed-out or muddy colors, no over-sharpening halos. Atmospheric haze is
allowed ONLY in the far background for depth — the subject's face, eyes, hair and hands
must be perfectly crisp and in focus. Render like a high-resolution museum-quality oil
painting: clean, precise, every detail intentional.
```

Cấu trúc khóa = **4 lớp**:
1. **Nét buộc phải có** (positive trước, negative sau — model vẽ ra cái được nhắc đến): razor-sharp focus · crisp edges · chất liệu resolved (sợi tóc, da, lụa, đá, nước) · micro-detail
2. **Cấm dứt khoát**: blur · soft-focus trên chủ thể · motion smear · noise · film grain · speckles · banding · JPEG/compression artifacts · pixelation · nét bệt/chảy · nét nhân bản/đúp · màu bệt/ố · halo over-sharpen
3. **Ngoại lệ có kiểm soát**: haze khí quyển CHỈ ở viền xa để tạo chiều sâu — mặt, mắt, tóc, tay nhân vật phải sắc nét tuyệt đối
4. **Chuẩn tham chiếu**: như tranh sấn museum-quality độ phân giải cao — sạch, chính xác, từng chi tiết có chủ đích

Câu kết prompt cũng được nâng cấp: *"Masterpiece quality — ultra-detailed, razor-sharp, pristine high-fidelity rendering."*

## 6. FRAMING LOCK (HARD RULE — từ v4)

```text
Framing lock (hard rule): no card border, no golden gothic frame, no gold line-work edges,
no ornamental corners, no oval medallion, no emblem, no ribbon banner, no title cartouche,
no parchment margin — the artwork runs full-bleed to all four edges of the image.
```

Và lặp lại ở câu kết: *"...the artwork runs full-bleed to all four edges of the image, and the only text anywhere in the image is the card title."*

---

## 7. MASTER PROMPT TEMPLATE v5 (Full-Bleed + Quality)

Các slot: `{TITLE}` tên lá · `{SCENE}` bối cảnh · `{CHARACTER_SPECIFICATION}` khối 8 thông số nhân vật · `{COUNT_LOCK}`.

```text
A full-bleed tarot card artwork "{TITLE}": the painted scene fills the ENTIRE image edge to edge like a classical fine-art painting, matching the painterly style, warm lighting and level of detail of the inner artwork of THE MOON reference image — but completely ignoring the reference image’s outer border and frame.

Framing lock (hard rule): no card border, no golden gothic frame, no gold line-work edges, no ornamental corners, no oval medallion, no emblem, no ribbon banner, no title cartouche, no parchment margin — the artwork runs full-bleed to all four edges of the image.

At the BOTTOM of the image, elegantly overlaid on the artwork: the title "{TITLE}" in the deck's unified title lettering — elegant letter-spaced antique-gold serif capitals with a soft dark drop shadow for legibility, the identical font style, letter height and antique-gold color used on every card of this deck — this is the ONLY text on the card.

The scene:
{SCENE}.

{CHARACTER_SPECIFICATION}

Skin-tone lock (hard rule): every human figure on this card — the main figure and every secondary or background figure (partners, companions, crowds, children) — is light-skinned only, within these ten tones: porcelain, ivory, fair, warm peach, light olive, sand, warm tan, honey, light bronze, amber-gold. No deep bronze, dark-brown or Black skin tones appear anywhere on the card; lighting, shadow and candle glow must never darken skin beyond these tones.

Anatomy lock (hard rule): each figure has exactly two arms, two legs, one head and one torso; every joint (shoulders, elbows, wrists, hips, knees, ankles) connects naturally to the body — no extra or fused limbs, no limbs sprouting from the torso, no stub arms, no malformed joints, no wrong finger counts. Prefer poses with both arms clearly separated from the torso. If any anatomy error appears, redraw it rather than accept it.

{COUNT_LOCK}

Quality lock (hard rule): gallery-grade, maximum-detail rendering — razor-sharp focus on the main figure and all foreground details; crisp, clean edges everywhere; fine resolved textures: individual hair strands, smooth glowing skin with clear highlights, woven silk fibers, stone grain, water droplets, leaf veins; rich micro-detail in fabric, jewelry and background architecture. Absolutely no blur, no soft-focus haze on the subject, no motion smear, no noise, no film grain, no speckles, no color banding, no JPEG or compression artifacts, no blocky pixelation, no smudged or melted details, no duplicated or double edges, no washed-out or muddy colors, no over-sharpening halos. Atmospheric haze is allowed ONLY in the far background for depth — the subject’s face, eyes, hair and hands must be perfectly crisp and in focus. Render like a high-resolution museum-quality oil painting: clean, precise, every detail intentional.

Masterpiece quality — ultra-detailed, razor-sharp, pristine high-fidelity rendering. Sensual fine-art anatomy, painterly warm lighting against subtle shadows, rich atmospheric perspective and depth, portrait orientation 7:12 aspect ratio, vintage gothic fine-art illustration, high detail. Absolutely no card border, no golden gothic frame, no gold ornamental line-work at the edges, no corner flourishes, no oval medallion, no emblem, no ribbon banner, no title cartouche, no parchment margin — the artwork runs full-bleed to all four edges of the image, and the only text anywhere in the image is the card title.
```

### 7.1 Định dạng khối `{CHARACTER_SPECIFICATION}` (8 trường)

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

### 7.2 Định dạng `{COUNT_LOCK}`

* Có vật phẩm: `Count lock (hard rule): {count.layout từ cards.json}`
* Không vật phẩm: `Count lock: no extra suit objects — do not add any additional wands, cups, swords or pentacle coins anywhere on this card beyond those described above.`

> 💡 Muốn ảnh **thuần tranh không chữ**? Bỏ đoạn "At the BOTTOM … ONLY text on the card." và đổi câu kết thành *"...and no text anywhere in the image."*

---

## 8. Ví dụ hoàn chỉnh — THE MOON (v5)

```text
A full-bleed tarot card artwork "THE MOON": the painted scene fills the ENTIRE image edge to edge like a classical fine-art painting, matching the painterly style, warm lighting and level of detail of the inner artwork of THE MOON reference image — but completely ignoring the reference image’s outer border and frame.

Framing lock (hard rule): no card border, no golden gothic frame, no gold line-work edges, no ornamental corners, no oval medallion, no emblem, no ribbon banner, no title cartouche, no parchment margin — the artwork runs full-bleed to all four edges of the image.

At the BOTTOM of the image, elegantly overlaid on the artwork: the title "THE MOON" in the deck's unified title lettering — elegant letter-spaced antique-gold serif capitals with a soft dark drop shadow for legibility, the identical font style, letter height and antique-gold color used on every card of this deck — this is the ONLY text on the card.

The scene:
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

Quality lock (hard rule): gallery-grade, maximum-detail rendering — razor-sharp focus on the main figure and all foreground details; crisp, clean edges everywhere; fine resolved textures: individual hair strands, smooth glowing skin with clear highlights, woven silk fibers, stone grain, water droplets, leaf veins; rich micro-detail in fabric, jewelry and background architecture. Absolutely no blur, no soft-focus haze on the subject, no motion smear, no noise, no film grain, no speckles, no color banding, no JPEG or compression artifacts, no blocky pixelation, no smudged or melted details, no duplicated or double edges, no washed-out or muddy colors, no over-sharpening halos. Atmospheric haze is allowed ONLY in the far background for depth — the subject’s face, eyes, hair and hands must be perfectly crisp and in focus. Render like a high-resolution museum-quality oil painting: clean, precise, every detail intentional.

Masterpiece quality — ultra-detailed, razor-sharp, pristine high-fidelity rendering. Sensual fine-art anatomy, painterly warm lighting against subtle shadows, rich atmospheric perspective and depth, portrait orientation 7:12 aspect ratio, vintage gothic fine-art illustration, high detail. Absolutely no card border, no golden gothic frame, no gold ornamental line-work at the edges, no corner flourishes, no oval medallion, no emblem, no ribbon banner, no title cartouche, no parchment margin — the artwork runs full-bleed to all four edges of the image, and the only text anywhere in the image is the card title.
```

---

## 9. Kinh nghiệm sinh ảnh chất lượng cao (ngoài prompt)

Prompt chỉ là một phần — chất lượng cuối còn phụ thuộc cài đặt khi sinh:

1. **Chọn độ phân giải cao nhất** mà công cụ cho phép (≥ 1024×1536, lý tưởng 1536×2304 trở lên cho tỉ lệ 7:12). Ảnh sinh nhỏ rồi phóng to lên sẽ nhòe — sinh to ngay từ đầu.
2. **Khử nhiễu/nâng nét bằng pass thứ 2 (upscale/refine)**: sau khi có ảnh gốc, chạy qua bước upscale ×2 (hoặc "enhance/detail pass") — dùng chính prompt của lá, thêm câu: *"same image, enhance to higher resolution, keep every detail identical, add finer micro-detail, no changes to composition, figures or colors"*.
3. **Lưu PNG không nén** (hoặc JPEG quality ≥ 95) — tránh nén lại nhiều lần gây artifact.
4. **Không ghép ảnh qua nhiều bước chỉnh** — mỗi lần xuất/nhập lại là một lần mất nét. Chuỗi lý tưởng: sinh → upscale ×1 → dùng.
5. **Nếu công cụ có tham số**: ưu tiên chế độ chất lượng/highest quality, giảm strength của bước upscale tinh chỉnh (0.2–0.35) để không bịa thêm chi tiết mới phá khuôn mặt.
6. **Kiểm tra 3 điểm trước khi chốt**: (a) mắt + mặt sắc nét, (b) tay đủ 5 ngón/khớp tự nhiên, (c) đếm vật phẩm suit đúng số — sai bất kỳ điểm nào thì vẽ lại/chạy refine, không chấp nhận.

---

## 10. Nguồn dữ liệu & kiểm tra

| File | Vai trò |
|---|---|
| **`04-AI-GUIDE/AI-INSTRUCTIONS.md`** | **Bản vận hành tự động cho AI** — đưa file này cho AI là tự biết mọi quy trình (vẽ · sửa · xuất prompt) |
| `cards.json` | Nguồn dữ liệu 78 lá (scene/count) — v5: thêm quality lock |
| `01-CARD-TABLE.md` | Bảng chuẩn 72 nhân vật (tuổi · mắt · tóc · da · vóc dáng · nét riêng · không khí) |
| `03-PROMPTS-78-FULL.md` | **78 prompt hoàn chỉnh full-bleed + quality lock, copy-paste được ngay** |
| `prompts-full.json` | Bản máy đọc được của 78 prompt |
| `the moon.png` | (Tùy chọn) tham chiếu phong cách ảnh trong — bỏ qua khung viền |

Checklist v5:
- [x] 78/78 prompt **full-bleed**: không khung, không emblem, không ribbon banner — chỉ tên lá bài dưới đáy ảnh
- [x] 78/78 prompt có **QUALITY LOCK**: chống nhòe/vỡ nét/noise/artifact, nét sắc trên chủ thể, chi tiết tối đa
- [x] 72/72 nhân vật nữ 18–25 đủ 8 thông số: mắt (màu+dáng+ánh nhìn) · tóc · da · vóc dáng A–D · nét riêng · không khí
- [x] 0 nhân vật da đen/da sẫm — 10 tông sáng `porcelain → amber-gold`, khóa áp cho cả nhân vật phụ & hậu cảnh
- [x] 0 nhân vật vượt trần "trung bình" (A 29 · B 30 · C 9 · D 4)
- [x] Count lock nhúng sẵn; FRAMING LOCK nhúng 2 đầu; câu kết "Masterpiece quality"
