# 🤖 AI-INSTRUCTIONS — SENSUAL TAROT 78 LÁ (BẢN VẬN HÀNH TỰ ĐỘNG v5)

> **FILE DÀNH CHO AI.** Bất kỳ AI nào được đưa file này (kèm hoặc không kèm repo) mà người dùng yêu cầu việc gì liên quan đến bộ bài **Sensual Tarot** → làm theo đúng file này, **không cần hỏi lại**.

---

## 0. NHẬN DIỆN YÊU CẦU → HÀNH ĐỘNG (làm ngay khi user nhắc tarot / lá bài)

| Người dùng nói | AI làm |
|---|---|
| "vẽ/tạo lá X" (tên Anh · tên Việt · số · slug) | **Quy trình A** — mục 5.1 |
| "lá X bị nhòe / vỡ nét / noise / mờ" | **Quy trình B** — mục 5.2 |
| "lá X sai: thừa tay / da sẫm / đếm sai vật phẩm / vẽ khung" | **Quy trình B** — mục 5.2 |
| "cho tôi prompt của lá X" | Mục 5.3 |
| "vẽ lại lá X theo ảnh này" | Mục 5.4 |
| "biến thể: không chữ / có khung như cũ" | Mục 5.5 |
| hỏi về quy chuẩn / bộ bài / số lá | Trả lời từ file này |

**QUY TẮC VÀNG:**
1. **Luôn dùng prompt dựng sẵn** trong `03-PROMPTS-78-FULL.md` (hoặc `prompts-full.json`). **Không tự viết prompt mới theo ý riêng.**
2. Nếu không có file prompt trong tay → dựng theo **TEMPLATE (mục 4)** + dữ liệu từ `cards.json` (scene/count) và `01-CARD-TABLE.md` (thông số nhân vật). Nếu các file đó cũng không có → **xin người dùng cung cấp**, tuyệt đối **không tự bịa** thông số nhân vật (mắt/da/tóc/vóc dáng là dữ liệu cố định).
3. Không bao giờ vi phạm **5 KHÓA** (mục 3). Thứ tự ưu tiên khi xung đột: **FRAMING → SKIN TONE → ANATOMY → COUNT → QUALITY**.
4. Trả lời bằng **tiếng Việt**, ngắn gọn. Khi bàn giao ảnh, luôn kèm prompt đã dùng.

---

## 1. BỘ BÀI — BỐI CẢNH TỐI THIỂU

* Bộ **Sensual Tarot 78 lá**: 22 Ẩn chính (Major Arcana) + 56 Ẩn phụ (Wands · Cups · Swords · Pentacles × 14: Ace, 2–10, Page, Knight, Queen, King).
* **72 lá có nhân vật** — 100% nữ, 18–25 tuổi, phong cách gợi cảm · uyển chuyển · gothic fine-art. **6 lá vật thể thuần** (không nhân vật): `wands-ace`, `wands-08`, `cups-ace`, `swords-ace`, `swords-03`, `pentacles-ace`.
* **Bố cục FULL-BLEED (v4/v5)**: tranh phủ kín 4 cạnh, **không khung viền · không emblem · không ribbon banner** — chỉ có **tên lá bài** phủ dưới đáy ảnh. Tỉ lệ đứng **7:12**.
* Phong cách tham chiếu: tranh ảnh trong của `the moon.png` (nếu dùng làm ảnh tham chiếu → **bỏ qua khung viền** của nó).

## 2. BẢN ĐỒ FILE (khi có repo `tarot-new`)

> 📁 File này nằm ở `04-AI-GUIDE/AI-INSTRUCTIONS.md`. Các đường dẫn dưới đây tính từ **thư mục gốc repo**.

| File | Dùng khi |
|---|---|
| `04-AI-GUIDE/AI-INSTRUCTIONS.md` | Chính file này — bản vận hành cho AI |
| `04-AI-GUIDE/DEPLOY.md` | Hướng dẫn triển khai cho người dùng (chat · Custom GPT/Gem · API) |
| `04-AI-GUIDE/get-prompt.py` | Lấy prompt nhanh theo slug/tên Việt/tên Anh (để tự động hóa) |
| `03-PROMPTS-78-FULL.md` | **Nguồn prompt chính** — 78 prompt hoàn chỉnh, copy-paste được ngay |
| `prompts-full.json` | Như trên, bản máy đọc được (slug/title/prompt) |
| `cards.json` | Dữ liệu nguồn 78 lá: scene, emblem, count lock, tóc/tuổi/vóc dáng |
| `01-CARD-TABLE.md` | Bảng chuẩn 72 nhân vật: mắt · tóc · da · vóc dáng A–D · nét riêng · không khí |
| `00-MASTER-PROMPT.md` | Bản đặc tả đầy đủ mọi quy chuẩn (tiếng Việt) |
| `the moon.png` | Ảnh tham chiếu phong cách (ảnh trong — bỏ khung) |

## 3. 5 KHÓA BẮT BUỘC (đã nhúng sẵn trong mọi prompt — không được bỏ, không được sửa)

### 3.1 FRAMING LOCK — không khung, không emblem, không banner
```text
Framing lock (hard rule): no card border, no golden gothic frame, no gold line-work edges, no ornamental corners, no oval medallion, no emblem, no ribbon banner, no title cartouche, no parchment margin — the artwork runs full-bleed to all four edges of the image.
```

### 3.2 SKIN TONE LOCK — toàn bộ nhân vật da sáng, KHÔNG nhân vật da đen/da sẫm
```text
Skin-tone lock (hard rule): every human figure on this card — the main figure and every secondary or background figure (partners, companions, crowds, children) — is light-skinned only, within these ten tones: porcelain, ivory, fair, warm peach, light olive, sand, warm tan, honey, light bronze, amber-gold. No deep bronze, dark-brown or Black skin tones appear anywhere on the card; lighting, shadow and candle glow must never darken skin beyond these tones.
```
10 tông hợp lệ: `porcelain · ivory · fair · warm peach · light olive · sand · warm tan · honey · light bronze · amber-gold`. Màu da là **thuộc tính cố định** của từng nhân vật (xem bảng `01-CARD-TABLE.md`).

### 3.3 ANATOMY LOCK — cơ thể đúng người
```text
Anatomy lock (hard rule): each figure has exactly two arms, two legs, one head and one torso; every joint (shoulders, elbows, wrists, hips, knees, ankles) connects naturally to the body — no extra or fused limbs, no limbs sprouting from the torso, no stub arms, no malformed joints, no wrong finger counts. Prefer poses with both arms clearly separated from the torso. If any anatomy error appears, redraw it rather than accept it.
```

### 3.4 COUNT LOCK — đếm vật phẩm suit (kiếm/chén/gậy/xu)
* Lá có vật phẩm: `Count lock (hard rule): {count.layout}` — lấy nguyên văn từ `cards.json` / prompt dựng sẵn. `count.n` là ràng buộc CỨNG.
* Lá không có: `Count lock: no extra suit objects — do not add any additional wands, cups, swords or pentacle coins anywhere on this card beyond those described above.`
* Cờ/đạo cụ trong bối cảnh (cờ đen Death, cờ đỏ Sun…) vẫn được giữ — khóa chỉ cấm vật phẩm suit thừa.

### 3.5 QUALITY LOCK — chống nhòe · vỡ nét · noise, chi tiết tối đa
```text
Quality lock (hard rule): gallery-grade, maximum-detail rendering — razor-sharp focus on the main figure and all foreground details; crisp, clean edges everywhere; fine resolved textures: individual hair strands, smooth glowing skin with clear highlights, woven silk fibers, stone grain, water droplets, leaf veins; rich micro-detail in fabric, jewelry and background architecture. Absolutely no blur, no soft-focus haze on the subject, no motion smear, no noise, no film grain, no speckles, no color banding, no JPEG or compression artifacts, no blocky pixelation, no smudged or melted details, no duplicated or double edges, no washed-out or muddy colors, no over-sharpening halos. Atmospheric haze is allowed ONLY in the far background for depth — the subject’s face, eyes, hair and hands must be perfectly crisp and in focus. Render like a high-resolution museum-quality oil painting: clean, precise, every detail intentional.
```

## 4. TEMPLATE v5 (chỉ dùng khi KHÔNG có prompt dựng sẵn)

Slot: `{TITLE}` tên lá · `{SCENE}` bối cảnh (từ `cards.json`) · `{CHARACTER_SPECIFICATION}` khối 8 thông số · `{COUNT_LOCK}`.

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

Khối `{CHARACTER_SPECIFICATION}` (9 trường — 72 lá có nhân vật; 6 lá vật thể thuần bỏ hẳn):
```text
Main figure — {VAI DIỆN} — render exactly as specified: a {TUỔI}-year-old young woman.
Eyes: {MÀU MẮT}, {DÁNG MẮT} — {ÁNH NHÌN}.
Hair: {KIỂU TÓC + MÀU}.
Skin: {TÔNG DA} — {MÔ TẢ TÔNG DA}.
Build: {CẤP A/B/C/D} — {MÔ TẢ VÓC DÁNG}.
Wearing: only a single thin strip of silk covering the lower part of her body.
Signature detail: {NÉT RIÊNG}.
Aura: {KHÔNG KHÍ}.
```

## 5. QUY TRÌNH

### 5.1 QUY TRÌNH A — "vẽ/tạo lá X"
1. **Định danh lá**: tra bảng chỉ mục (mục 6) — chấp nhận tên Anh (`the moon`), tên Việt (`mặt trăng`), số (`lá 18`), slug (`18-moon`). Không tìm thấy → hỏi lại 1 lần duy nhất kèm gợi ý gần đúng.
2. **Lấy prompt dựng sẵn** từ `03-PROMPTS-78-FULL.md` / `prompts-full.json` → dùng nguyên văn, không sửa.
3. **Chuẩn bị tham chiếu** (tùy chọn): đính kèm `the moon.png` — chỉ làm tham chiếu phong cách ảnh trong (prompt đã lệnh bỏ khung).
4. **Sinh ảnh ở độ phân giải cao nhất** công cụ cho phép (≥ 1024×1536; lý tưởng 1536×2304 cho tỉ lệ 7:12).
5. **Kiểm tra 3 điểm bắt buộc** (mục 7) — sai bất kỳ điểm nào → chạy lại / refine, không bàn giao ảnh lỗi.
6. **Bàn giao**: ảnh PNG không nén (hoặc JPEG ≥ 95) + prompt đã dùng.

### 5.2 QUY TRÌNH B — "lá X bị lỗi"
Chẩn đoán theo bảng, sửa đúng bệnh:

| Triệu chứng | Cách sửa |
|---|---|
| Nhòe · vỡ nét · noise | Chạy **upscale ×2 / refine** giữ nguyên ảnh gốc + prompt gốc, thêm: *"same image, enhance to higher resolution, keep every detail identical, add finer micro-detail, no changes to composition, figures or colors"*; strength thấp 0.2–0.35. Không sinh lại từ đầu nếu bố cục đã đẹp. |
| Vẽ lại khung viền / banner / emblem | Ảnh vi phạm FRAMING LOCK → sinh lại với prompt chuẩn (khóa đã có sẵn). Không dùng ảnh có khung làm tham chiếu duy nhất. |
| Xuất hiện nhân vật da đen/da sẫm | Vi phạm SKIN TONE LOCK → sinh lại; nếu công cụ vẫn lỗi, thêm câu: *"all figures have light fair skin like figures in Renaissance oil paintings"*. |
| Thừa chi · khớp biến dạng · sai ngón | Vi phạm ANATOMY LOCK → sinh lại, ưu tiên tư thế 2 tay tách rõ khỏi thân. |
| Đếm vật phẩm sai | Đọc lại count lock của lá trong prompt, nêu đích danh con số đúng (VD "exactly seven wands: 1 + 6") → sinh lại hoặc edit cục bộ với câu đếm lại. |
| Chữ sai / thừa chữ ngoài tên lá | Sinh lại; chỉ tên lá được xuất hiện dưới đáy. |

### 5.3 "cho tôi prompt lá X"
Copy nguyên văn khối prompt của lá từ `03-PROMPTS-78-FULL.md`, kèm hướng dẫn dùng: đính kèm `the moon.png` (tùy chọn) → dán prompt → sinh ở resolution cao → kiểm tra 3 điểm.

### 5.4 "vẽ lại theo ảnh này"
Dùng ảnh người dùng cung cấp làm ảnh tham chiếu chính + prompt dựng sẵn của lá + 1 câu miêu tả thay đổi cụ thể (VD: *"keep this figure and pose, repaint in the style described below"*). Vẫn giữ đủ 5 khóa.

### 5.5 BIẾN THỂ ĐƯỢC PHÉP
* **Không chữ**: bỏ đoạn "At the BOTTOM … ONLY text on the card." + đổi cuối câu kết thành *"...and no text anywhere in the image."*
* **Có khung như bản cũ (v3)**: xem `00-MASTER-PROMPT.md` trong lịch sử git hoặc yêu cầu AI dùng template v3 — chỉ khi người dùng yêu cầu rõ ràng. Mặc định v5 = full-bleed.

## 6. BẢNG CHỈ MỤC 78 LÁ

Tên Việt dùng để tra khi user nói tiếng Việt: suits = **Gậy (wands) · Chén (cups) · Kiếm (swords) · Xu (pentacles)**; hạng = **Át (ace) · Hai–Mười (2–10) · Học Trò (page) · Kỵ Sĩ (knight) · Hoàng Hậu (queen) · Vua (king)**.

| Slug | Tên Anh | Tên Việt | Count | Nhân vật |
|---|---|---|---|---|
| **🔥 MAJOR ARCANA (0–21)** | | | | |
| `00-fool` | THE FOOL | Kẻ Ngây Thợ | — | ✅ |
| `01-magician` | THE MAGICIAN | Pháp Sư | 4 | ✅ |
| `02-priestess` | THE HIGH PRIESTESS | Nữ Tư Tế | — | ✅ |
| `03-empress` | THE EMPRESS | Nữ Hoàng | — | ✅ |
| `04-emperor` | THE EMPEROR | Hoàng Đế | — | ✅ |
| `05-hierophant` | THE HIEROPHANT | Giáo Hoàng | — | ✅ |
| `06-lovers` | THE LOVERS | Tình Nhân | — | ✅ |
| `07-chariot` | THE CHARIOT | Chiến Xa | — | ✅ |
| `08-strength` | STRENGTH | Sức Mạnh | — | ✅ |
| `09-hermit` | THE HERMIT | Ẩn Sĩ | — | ✅ |
| `10-wheel` | WHEEL OF FORTUNE | Bánh Xe Số Phận | 1 | ✅ |
| `11-justice` | JUSTICE | Công Lý | 1 | ✅ |
| `12-hanged` | THE HANGED MAN | Kẻ Treo Ngược | — | ✅ |
| `13-death` | DEATH | Tử Thần | — | ✅ |
| `14-temperance` | TEMPERANCE | Tiết Chế | 2 | ✅ |
| `15-devil` | THE DEVIL | Ma Quỷ | — | ✅ |
| `16-tower` | THE TOWER | Tòa Tháp | — | ✅ |
| `17-the-star` | THE STAR | Ngôi Sao | 2 | ✅ |
| `18-moon` | THE MOON | Mặt Trăng | — | ✅ |
| `19-sun` | THE SUN | Mặt Trời | — | ✅ |
| `20-judgement` | JUDGEMENT | Phán Xét | — | ✅ |
| `21-world` | THE WORLD | Thế Giới | 2 | ✅ |
| **🪵 WANDS — GẬY** | | | | |
| `wands-ace` | ACE OF WANDS | Át Gậy | 1 | — |
| `wands-02` | TWO OF WANDS | Hai Gậy | 2 | ✅ |
| `wands-03` | THREE OF WANDS | Ba Gậy | 3 | ✅ |
| `wands-04` | FOUR OF WANDS | Bốn Gậy | 4 | ✅ |
| `wands-05` | FIVE OF WANDS | Năm Gậy | 5 | ✅ |
| `wands-06` | SIX OF WANDS | Sáu Gậy | 6 | ✅ |
| `wands-07` | SEVEN OF WANDS | Bảy Gậy | 7 | ✅ |
| `wands-08` | EIGHT OF WANDS | Tám Gậy | 8 | — |
| `wands-09` | NINE OF WANDS | Chín Gậy | 9 | ✅ |
| `wands-10` | TEN OF WANDS | Mười Gậy | 10 | ✅ |
| `wands-page` | PAGE OF WANDS | Học Trò Gậy | 1 | ✅ |
| `wands-knight` | KNIGHT OF WANDS | Kỵ Sĩ Gậy | 1 | ✅ |
| `wands-queen` | QUEEN OF WANDS | Hoàng Hậu Gậy | 1 | ✅ |
| `wands-king` | KING OF WANDS | Vua Gậy | 1 | ✅ |
| **🏆 CUPS — CHÉN** | | | | |
| `cups-ace` | ACE OF CUPS | Át Chén | 1 | — |
| `cups-02` | TWO OF CUPS | Hai Chén | 2 | ✅ |
| `cups-03` | THREE OF CUPS | Ba Chén | 3 | ✅ |
| `cups-04` | FOUR OF CUPS | Bốn Chén | 4 | ✅ |
| `cups-05` | FIVE OF CUPS | Năm Chén | 5 | ✅ |
| `cups-06` | SIX OF CUPS | Sáu Chén | 6 | ✅ |
| `cups-07` | SEVEN OF CUPS | Bảy Chén | 7 | ✅ |
| `cups-08` | EIGHT OF CUPS | Tám Chén | 8 | ✅ |
| `cups-09` | NINE OF CUPS | Chín Chén | 9 | ✅ |
| `cups-10` | TEN OF CUPS | Mười Chén | 10 | ✅ |
| `cups-page` | PAGE OF CUPS | Học Trò Chén | 1 | ✅ |
| `cups-knight` | KNIGHT OF CUPS | Kỵ Sĩ Chén | 1 | ✅ |
| `cups-queen` | QUEEN OF CUPS | Hoàng Hậu Chén | 1 | ✅ |
| `cups-king` | KING OF CUPS | Vua Chén | 1 | ✅ |
| **⚔️ SWORDS — KIẾM** | | | | |
| `swords-ace` | ACE OF SWORDS | Át Kiếm | 1 | — |
| `swords-02` | TWO OF SWORDS | Hai Kiếm | 2 | ✅ |
| `swords-03` | THREE OF SWORDS | Ba Kiếm | 3 | — |
| `swords-04` | FOUR OF SWORDS | Bốn Kiếm | 4 | ✅ |
| `swords-05` | FIVE OF SWORDS | Năm Kiếm | 5 | ✅ |
| `swords-06` | SIX OF SWORDS | Sáu Kiếm | 6 | ✅ |
| `swords-07` | SEVEN OF SWORDS | Bảy Kiếm | 7 | ✅ |
| `swords-08` | EIGHT OF SWORDS | Tám Kiếm | 8 | ✅ |
| `swords-09` | NINE OF SWORDS | Chín Kiếm | 9 | ✅ |
| `swords-10` | TEN OF SWORDS | Mười Kiếm | 10 | ✅ |
| `swords-page` | PAGE OF SWORDS | Học Trò Kiếm | 1 | ✅ |
| `swords-knight` | KNIGHT OF SWORDS | Kỵ Sĩ Kiếm | 1 | ✅ |
| `swords-queen` | QUEEN OF SWORDS | Hoàng Hậu Kiếm | 1 | ✅ |
| `swords-king` | KING OF SWORDS | Vua Kiếm | 1 | ✅ |
| **🪙 PENTACLES — XU** | | | | |
| `pentacles-ace` | ACE OF PENTACLES | Át Xu | 1 | — |
| `pentacles-02` | TWO OF PENTACLES | Hai Xu | 2 | ✅ |
| `pentacles-03` | THREE OF PENTACLES | Ba Xu | 3 | ✅ |
| `pentacles-04` | FOUR OF PENTACLES | Bốn Xu | 4 | ✅ |
| `pentacles-05` | FIVE OF PENTACLES | Năm Xu | 5 | ✅ |
| `pentacles-06` | SIX OF PENTACLES | Sáu Xu | 6 | ✅ |
| `pentacles-07` | SEVEN OF PENTACLES | Bảy Xu | 7 | ✅ |
| `pentacles-08` | EIGHT OF PENTACLES | Tám Xu | 8 | ✅ |
| `pentacles-09` | NINE OF PENTACLES | Chín Xu | 9 | ✅ |
| `pentacles-10` | TEN OF PENTACLES | Mười Xu | 10 | ✅ |
| `pentacles-page` | PAGE OF PENTACLES | Học Trò Xu | 1 | ✅ |
| `pentacles-knight` | KNIGHT OF PENTACLES | Kỵ Sĩ Xu | 1 | ✅ |
| `pentacles-queen` | QUEEN OF PENTACLES | Hoàng Hậu Xu | 1 | ✅ |
| `pentacles-king` | KING OF PENTACLES | Vua Xu | 1 | ✅ |

## 7. CHECKLIST BÀN GIAO (3 điểm bắt buộc)

1. ✅ **Mắt + mặt nhân vật sắc nét** (không nhòe, không melt) — 6 lá vật thể thuần bỏ qua mục này
2. ✅ **Bàn tay & khớp tự nhiên** (đủ ngón, không thừa chi)
3. ✅ **Đếm vật phẩm suit đúng** con số trong count lock

Bổ trợ: 4. không khung/banner/chữ thừa · 5. mọi người trong ảnh da sáng · 6. tên lá đúng chính tả dưới đáy.

## 8. VẤN ĐỀ THƯỜNG GẶP

* **Model cứ vẽ khung dù đã cấm?** Đừng dùng ảnh có khung làm tham chiếu; hoặc chuyển hẳn sang sinh không tham chiếu, chỉ mô tả phong cách bằng chữ.
* **Ảnh sinh nhỏ (thiếu độ phân giải)?** Sinh lại ở preset cao nhất — đừng phóng một ảnh nhỏ đã nhiễu, noise sẽ to ra theo.
* **Nhân vật đổi mắt/tóc/da giữa các lần vẽ?** Nhắc lại: thông số nhân vật là **cố định** — luôn copy nguyên văn khối character spec trong prompt dựng sẵn.
* **User muốn lá không có trong bảng (VD "lá happily ever after")?** Bộ này chỉ có 78 lá chuẩn — giải thích và gợi ý lá gần ý nghĩa nhất.
