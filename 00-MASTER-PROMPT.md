# 🔮 SENSUAL TAROT 78 LÁ — MASTER PROMPT SPECIFICATION (v4 · FULL-BLEED)

Bản chuẩn hóa quy chuẩn tạo hình và bố cục toàn bộ 78 lá bài Tarot.

**Thay đổi chính của v4** (so với v3):

1. **BỎ KHUNG VIỀN — BỎ EMBLEM — BỎ RIBBON BANNER**: tranh phủ kín toàn bộ khung hình (*full-bleed* 4 cạnh như một bức hội họa cổ điển), **chỉ giữ lại TÊN LÁ BÀI** phủ nhẹ dưới đáy ảnh. Không còn khung vàng Gothic, medallion emblem, ribbon banner, nền giấy da, hay 4 lớp chiều sâu của v3.
2. Thêm **FRAMING LOCK** (hard rule) vào từng prompt để model không tự vẽ lại khung/banner theo thói quen từ ảnh tham chiếu.
3. Giữ nguyên từ v3: prompt đầy đủ 100% (scene + 8 thông số nhân vật), **SKIN TONE LOCK** (10 tông da sáng, loại bỏ nhân vật da đen/da sẫm), **ANATOMY LOCK**, **COUNT LOCK**.
4. `the moon.png` chỉ còn là **tham chiếu phong cách ảnh trong** (nét vẽ, ánh sáng) — nêu rõ trong prompt là *bỏ qua hoàn toàn khung viền* của ảnh tham chiếu; `card-blank.png` không cần dùng nữa.

---

## 1. Quy chuẩn bố cục (Full-Bleed Layout Standard — v4)

* Tranh **phủ kín 4 cạnh khung hình** — không viền, không khung, không hoa văn mép, không nền giấy da: bối cảnh vẽ tràn ra tận mép trên/dưới/trái/phải như một bức hội họa cổ điển hoàn chỉnh.
* **Chữ trên ảnh**: chỉ duy nhất **tên lá bài** (VD: "THE MOON") — kiểu chữ cổ điển thanh lịch, phủ nhẹ **dưới đáy ảnh**, có bóng mờ nhẹ để đọc được trên mọi nền. Không chữ nào khác xuất hiện.
* **Không có**: khung viền vàng Gothic · medallion emblem · ribbon banner · parchment · hoa văn góc · bất kỳ chi tiết trang trí "bộ bài" nào bao quanh tranh.
* **Cách dùng thực tế**: (tùy chọn) đính kèm `the moon.png` làm tham chiếu phong cách ảnh trong — prompt đã ghi rõ *ignore the reference image's outer border and frame*.

## 2. Quy chuẩn tạo hình nhân vật (Sensual Fine-Art Figure Standard — giữ nguyên từ v3)

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

## 3. SKIN TONE LOCK (HARD RULE) — loại bỏ nhân vật da đen / da sẫm (giữ nguyên từ v3)

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
* Kỹ thuật: nêu whitelist 10 tông trước, cấm tông sẫm sau. Câu khóa chuẩn (đã nhúng sẵn trong từng prompt):

```text
Skin-tone lock (hard rule): every human figure on this card — the main figure and every
secondary or background figure (partners, companions, crowds, children) — is light-skinned
only, within these ten tones: porcelain, ivory, fair, warm peach, light olive, sand,
warm tan, honey, light bronze, amber-gold. No deep bronze, dark-brown or Black skin tones
appear anywhere on the card; lighting, shadow and candle glow must never darken skin
beyond these tones.
```

## 4. COUNT LOCK (đếm vật phẩm — giữ nguyên từ v3)

* Mỗi lá có số vật phẩm suit (kiếm/chén/gậy/đồng xu) khai báo trong `cards.json` (`count.n` = ràng buộc CỨNG, `count.layout` = cách xếp + cách đếm).
* Lá không có vật phẩm suit (`count = null`) → phát câu khóa *"no extra suit objects"*.
* Lưu ý: **cờ/banner nằm trong bối cảnh** (cờ đen của Death, cờ đỏ của The Sun, cờ trắng của Judgement…) vẫn được giữ — FRAMING LOCK chỉ cấm banner/chữ trang trí *khung card*, không cấm đạo cụ trong tranh.

## 5. FRAMING LOCK (HARD RULE — mới của v4)

Câu khóa nhúng sẵn trong từng prompt:

```text
Framing lock (hard rule): no card border, no golden gothic frame, no gold line-work edges,
no ornamental corners, no oval medallion, no emblem, no ribbon banner, no title cartouche,
no parchment margin — the artwork runs full-bleed to all four edges of the image.
```

Và lặp lại ở câu kết: *"...the artwork runs full-bleed to all four edges of the image, and the only text anywhere in the image is the card title."*

---

## 6. MASTER PROMPT TEMPLATE v4 (Full-Bleed)

Các slot: `{TITLE}` tên lá · `{SCENE}` bối cảnh · `{CHARACTER_SPECIFICATION}` khối 8 thông số nhân vật · `{COUNT_LOCK}`.

```text
A full-bleed tarot card artwork "{TITLE}": the painted scene fills the ENTIRE image edge to edge like a classical fine-art painting, matching the painterly style, warm lighting and level of detail of the inner artwork of THE MOON reference image — but completely ignoring the reference image's outer border and frame.

Framing lock (hard rule): no card border, no golden gothic frame, no gold line-work edges, no ornamental corners, no oval medallion, no emblem, no ribbon banner, no title cartouche, no parchment margin — the artwork runs full-bleed to all four edges of the image.

At the BOTTOM of the image, elegantly overlaid on the artwork: the title "{TITLE}" in clean antique lettering with a soft shadow for legibility — this is the ONLY text on the card.

The scene:
{SCENE}.

{CHARACTER_SPECIFICATION}

Skin-tone lock (hard rule): every human figure on this card — the main figure and every secondary or background figure (partners, companions, crowds, children) — is light-skinned only, within these ten tones: porcelain, ivory, fair, warm peach, light olive, sand, warm tan, honey, light bronze, amber-gold. No deep bronze, dark-brown or Black skin tones appear anywhere on the card; lighting, shadow and candle glow must never darken skin beyond these tones.

Anatomy lock (hard rule): each figure has exactly two arms, two legs, one head and one torso; every joint (shoulders, elbows, wrists, hips, knees, ankles) connects naturally to the body — no extra or fused limbs, no limbs sprouting from the torso, no stub arms, no malformed joints, no wrong finger counts. Prefer poses with both arms clearly separated from the torso. If any anatomy error appears, redraw it rather than accept it.

{COUNT_LOCK}

Sensual fine-art anatomy, painterly warm lighting against subtle shadows, rich atmospheric perspective and depth, portrait orientation 7:12 aspect ratio, vintage gothic fine-art illustration, high detail. Absolutely no card border, no golden gothic frame, no gold ornamental line-work at the edges, no corner flourishes, no oval medallion, no emblem, no ribbon banner, no title cartouche, no parchment margin — the artwork runs full-bleed to all four edges of the image, and the only text anywhere in the image is the card title.
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

> 💡 Muốn ảnh **thuần tranh không chữ**? Bỏ đoạn "At the BOTTOM … ONLY text on the card." và đổi câu kết thành *"...and no text anywhere in the image."*

---

## 7. Ví dụ hoàn chỉnh — THE MOON (v4 full-bleed)

```text
A full-bleed tarot card artwork "THE MOON": the painted scene fills the ENTIRE image edge to edge like a classical fine-art painting, matching the painterly style, warm lighting and level of detail of the inner artwork of THE MOON reference image — but completely ignoring the reference image's outer border and frame.

Framing lock (hard rule): no card border, no golden gothic frame, no gold line-work edges, no ornamental corners, no oval medallion, no emblem, no ribbon banner, no title cartouche, no parchment margin — the artwork runs full-bleed to all four edges of the image.

At the BOTTOM of the image, elegantly overlaid on the artwork: the title "THE MOON" in clean antique lettering with a soft shadow for legibility — this is the ONLY text on the card.

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

Sensual fine-art anatomy, painterly warm lighting against subtle shadows, rich atmospheric perspective and depth, portrait orientation 7:12 aspect ratio, vintage gothic fine-art illustration, high detail. Absolutely no card border, no golden gothic frame, no gold ornamental line-work at the edges, no corner flourishes, no oval medallion, no emblem, no ribbon banner, no title cartouche, no parchment margin — the artwork runs full-bleed to all four edges of the image, and the only text anywhere in the image is the card title.
```

---

## 8. Nguồn dữ liệu & kiểm tra

| File | Vai trò |
|---|---|
| `cards.json` | Nguồn dữ liệu 78 lá (scene/count) — v4: không còn dùng emblem trong prompt |
| `01-CARD-TABLE.md` | Bảng chuẩn 72 nhân vật (tuổi · mắt · tóc · da · vóc dáng · nét riêng · không khí) |
| `03-PROMPTS-78-FULL.md` | **78 prompt hoàn chỉnh full-bleed, copy-paste được ngay** |
| `prompts-full.json` | Bản máy đọc được của 78 prompt |
| `the moon.png` | (Tùy chọn) tham chiếu phong cách ảnh trong — bỏ qua khung viền |

Checklist v4:
- [x] 78/78 prompt **full-bleed**: không khung, không emblem, không ribbon banner, không parchment — chỉ tên lá bài dưới đáy ảnh
- [x] FRAMING LOCK nhúng 2 đầu prompt (sau mở đầu + trong câu kết) chống model vẽ lại khung
- [x] 72/72 nhân vật nữ 18–25 đủ 8 thông số: mắt (màu+dáng+ánh nhìn) · tóc · da · vóc dáng A–D · nét riêng · không khí
- [x] 0 nhân vật da đen/da sẫm — 10 tông sáng `porcelain → amber-gold`, khóa áp cho cả nhân vật phụ & hậu cảnh
- [x] 0 nhân vật vượt trần "trung bình" (A 29 · B 30 · C 9 · D 4)
- [x] Count lock nhúng sẵn trong từng prompt; cờ/đạo cụ trong bối cảnh vẫn được giữ
- [x] Cờ/notification: `card-blank.png` không còn cần dùng
