# 🌹 BẢNG THÔNG SỐ NHÂN VẬT — 72 NHÂN VẬT NỮ (PHONG CÁCH GỢI CẢM · GOTHIC FINE-ART)

> File **phát triển từ** `01-CARD-TABLE.md` (bảng chuẩn — nguồn gốc tuổi/tóc/vóc dáng/huy hiệu/tên)
> và `tarot prompt/cards.json`. Tuổi + kiểu tóc được **giữ nguyên 100%** so với bảng chuẩn.
> File này **bổ sung** 4 thuộc tính mới: **Đôi mắt · Màu da · Nét riêng (signature) · Không khí (aura)**,
> và **chuẩn hóa vóc dáng** vào dải **Thanh mảnh → Trung bình** (không vượt trần "trung bình").

---

## 0. THANG NHÂN VẬT — TỪ THONG THẢ → TRUNG BÌNH

```
THONG THẢ (thoáng, duyên, nhẹ)                                        TRUNG BÌNH (đủ, mềm, cân)
A ──────────────────── B ──────────────────── C ──────────────────── D
petite · willowy · mảnh            thon gọn · săn nhẹ · thanh        cân đối · mềm mại · cong tự nhiên
```

- **A (Thanh mảnh)** — dáng nhẹ như gió, eo nhỏ, ít đường nét nặng → "thong thả" nhất.
- **B (Thon gọn)** — dây chun săn nhẹ, vai gọn, dáng vận động → "thong thả có chuyển động".
- **C (Trung bình mềm)** — cân đối, cong tự nhiên vừa phải → ngưỡng "trung bình".
- **D (Trung bình đầy đặn)** — đầy đặn vừa đủ, cong nữ tính trong ngưỡng trung bình → trần của dải.
- **KHÔNG có cấp nào vượt quá D**: không béo, không plus-size, không phóng đại.
- Sự gợi cảm nằm ở **đường cong tự nhiên, làn da bóng, tư thế và ánh mắt** — không nằm ở kích cỡ.

---

## 1. QUY CHUẨN TỔNG (áp dụng cho cả 72 lá)

### 1.1 Màu da — TUYỆT ĐỐI KHÔNG DA ĐEN / DA SẪM MÀU
Toàn bộ 72 nhân vật chỉ dùng 10 tông da sáng → nâu vàng nhạt (không có tông sẫm, không nâu đen, không đen):

| Tông da | Mô tả |
|---|---|
| `porcelain` | trắng sứ, lạnh, gân xanh mờ, ánh ngọc trai |
| `ivory` | trắng ngà, ấm, mịn như lụa |
| `fair` | trắng hồng nhạt, bóng mờ như xà cừ (fair pearlescent) |
| `warm peach` | đào ấm, má hồng tự nhiên, bị nắng làm ửng vàng |
| `light olive` | ô-liu nhạt, ấm, mịn, hơi vàng ở vai và tay |
| `sand` | cát ấm, đều màu, mượt |
| `warm tan` | rám nắng nhẹ, ửng đồng ở vai và gò má |
| `honey` | mật ong vàng, óng ánh dưới nắng |
| `light bronze` | đồng nhạt, bóng gợn sáng (vẫn là tông sáng) |
| `amber-gold` | hổ phách-vàng, rực dưới ánh đèn nến |

> Màu da là **thuộc tính cố định** của từng nhân vật (không được đổi khi tạo hình lại lá).
> Không bao giờ pha bóng da thành tông nâu sẫm, nâu đen hay đen — kể cả dưới ánh sáng mạnh.

### 1.2 Vóc dáng — 4 CẤP, TRẦN LÀ "TRUNG BÌNH"
Dải chuẩn: **A (thanh mảnh) → B (thon gọn) → C (trung bình mềm) → D (trung bình đầy đặn)**.
Không có cấp nào vượt quá trung bình: **không plus-size, không béo, không nặng nề**.
Gợi cảm nằm ở **đường cong tự nhiên, làn da bóng, tư thế và ánh mắt** — không nằm ở kích cỡ phóng đại.

| Cấp | Tên | Đặc điểm |
|---|---|---|
| **A** | Thanh mảnh (Slender / Delicate) | petite, willowy, mảnh mai, eo nhỏ, dáng nhẹ như gió |
| **B** | Thon gọn (Lean / Toned) | dây chun săn nhẹ, eo thắt, vai gọn, cơ mềm tự nhiên, dáng vận động |
| **C** | Trung bình mềm (Average soft) | cân đối, cong tự nhiên vừa phải, bụng phẳng-mềm, dáng đứng thong thả |
| **D** | Trung bình đầy đặn (Average shapely) | đầy đặn vừa, hông và ngực cong nữ tính trong ngưỡng trung bình, không phình |

> Chuyển đổi từ bảng cũ: các mô tả `voluptuous / curvaceous / luxurious curves` cũ
> (Empress, Devil, Queen of Wands, Queen of Pentacles…) được **hạ xuống cấp D**
> — vẫn nữ tính, gợi cảm, nhưng **trong ngưỡng trung bình**, không còn phóng đại.

### 1.3 Đôi mắt — 10 dáng chuẩn + bảng màu
| Dáng mắt | Mô tả |
|---|---|
| `almond` | hạnh nhân, cân đối, cân bằng giữa sắc và dịu |
| `doe` | tròn to, ngây thơ, long lanh |
| `heavy-lidded` | mí nặng, khép hờ, quyến rũ |
| `hooded` | mí che, sâu thẳm, khó đọc |
| `upturned` | đuôi mắt hếch nhẹ, tinh nghịch / kiêu |
| `cat` | mắt mèo, sắc, đuôi vươn dài |
| `round` | tròn trong, ngạc nhiên / trong trẻo |
| `narrow` | hẹp dài, sắc bén, tập trung |
| `wide-set` | mắt cách xa nhau, thần thái thanh thoát |
| `dreamy` | mơ màng, khép hờ, chìm trong suy nghĩ |

Bảng màu dùng: honey-amber · pale violet · sea-green · topaz-amber · storm-grey ·
moss-green · chestnut-amber · steel-blue · amber-gold · silver-grey · golden-hazel ·
grey-green · teal · ice-blue · aquamarine · wine-plum · slate-grey · moonstone silver-violet ·
gold-green · emerald · auburn-brown · honey-brown · dark cherry-violet · hazel-green ·
golden-amber · dark chestnut · umber · hazel-grey · baby-blue · violet-grey · deep brown ·
amber-brown · walnut-brown · seal-brown · flint-grey · dark emerald · misty grey ·
dark brown · fear-bright hazel · grey-brown · honey-hazel · blazing grey-blue · jade ·
steel-grey · warm brown · icy-grey · deep umber · molten brown · earth-brown · …
**Mỗi nhân vật có tổ hợp MÀU + DÁNG + ÁNH NHÌN duy nhất** (không cặp nào trùng).

### 1.4 Nét riêng (Signature — mỗi nhân vật chỉ 1 chi tiết)
Mỗi nhân vật có **đúng một chi tiết không thể nhầm lẫn**: nốt ruồi, vết sẹo nhỏ,
mảng tàn nhang, hình xăm nhỏ, khuyên tai, lúm đồng tiền, vết bớt, khuyên mũi, dây chuyền…
Không nhân vật nào dùng chung nét riêng với nhân vật khác.

### 1.5 Phạm vi & độ tuổi
- 72 nhân vật nữ, **18–25 tuổi** (giữ nguyên bảng chuẩn), 100% nữ.
- 6 lá **không có nhân vật** (vật thể thuần): `wands-ace`, `wands-08`, `cups-ace`,
  `swords-ace`, `swords-03`, `pentacles-ace` — không nằm trong file này.

---

## 2. BẢNG PHÂN BỐ VÓC DÁNG (A → D) — 72 NHÂN VẬT

| Cấp | Số lá | Lá |
|---|---|---|
| **A** — Thanh mảnh | 29 | 00-fool, 02-priestess, 05-hierophant, 06-lovers, 09-hermit, 12-hanged, 13-death, 14-temperance, 17-the-star, 18-moon, 19-sun, wands-02, wands-07, wands-page, cups-02, cups-04, cups-05, cups-06, cups-07, cups-page, cups-queen, swords-04, swords-06, swords-07, swords-08, swords-09, pentacles-05, pentacles-08, pentacles-page |
| **B** — Thon gọn | 30 | 01-magician, 04-emperor, 07-chariot, 08-strength, 10-wheel, 11-justice, 16-tower, 20-judgement, 21-world, wands-03, wands-04, wands-05, wands-06, wands-09, wands-10, wands-knight, wands-king, cups-08, cups-knight, swords-02, swords-05, swords-10, swords-page, swords-knight, swords-queen, swords-king, pentacles-02, pentacles-03, pentacles-07, pentacles-knight |
| **C** — Trung bình mềm | 9 | cups-03, cups-09, cups-10, cups-king, pentacles-04, pentacles-06, pentacles-09, pentacles-10, pentacles-king |
| **D** — Trung bình đầy đặn | 4 | 03-empress, 15-devil, wands-queen, pentacles-queen |

---

## 3. BẢNG CHÍNH — MAJOR ARCANA · 22 NHÂN VẬT

| Lá | Tuổi | Đôi mắt | Kiểu tóc (chuẩn) | Vóc dáng | Màu da | Nét riêng | Không khí |
|---|---|---|---|---|---|---|---|
| **[A]** **THE FOOL** `00-fool` | 19 | honey-amber, doe, tròn long lanh, ngây thơ không phòng bị | loose wind-tossed honey-blonde waves down to her shoulder blades, sunlit and carefree | **A** petite & lithe, eo nhỏ, bước chân nhẹ như gió | warm peach | 3 tàn nhang vàng nhỏ dưới mắt trái | gió mai, mật ong, vực thẳm mời gọi |
| **[I]** **THE MAGICIAN** `01-magician` | 22 | pale violet, almond sắc, hooded, ánh nhìn xuyên thấu | jet-black straight hair falling past her waist like a sleek silk curtain, center-parted | **B** cao, dài, thanh thoát, tư thế chỉ huy | porcelain | sẹo bạc mảnh dọc ngón trỏ tay phải | tĩnh điện, mực đen, bạc lạnh |
| **[II]** **THE HIGH PRIESTESS** `02-priestess` | 23 | sea-green sâu, heavy-lidded, nửa khép hờ, huyền bí | deep auburn hair with soft natural waves, cascading beneath a sheer gossamer veil | **A** mảnh mai, cổ cao, dáng ngồi thẳng trầm tĩnh | ivory | bớt hình lưỡi liềm sau tai trái | ánh trăng, khói trầm, trang giấy cũ |
| **[III]** **THE EMPRESS** `03-empress` | 24 | topaz-amber, almond ấm, đuôi mắt hếch nhẹ, sà xuống gợi cảm | thick ripe-wheat golden blonde hair, spilling over both shoulders in soft ropey curls garlanded with flowers | **D** đầy đặn vừa, hông-vòng một cong mềm trong ngưỡng trung bình | honey | nốt ruồi nhỏ trên xương đòn trái | lúa chín, mật, hương hoa cam |
| **[IV]** **THE EMPEROR** `04-emperor` | 25 | storm-grey, hooded, lạnh lùng ra lệnh | sleek dark bronze-brown hair in a sharp warrior braid, crowned with a golden ram-horn circlet | **B** cao, vai rộng, săn chắc theo kiểu chiến binh, không thô | sand | sẹo nhỏ khía chân mày phải | đá granit, sắt, gió núi |
| **[V]** **THE HIEROPHANT** `05-hierophant` | 24 | moss-green, dreamy, ánh mắt biết tuốt, hơi cụp | thick espresso-brown waves falling over embroidered ceremonial vestments | **A** cao, thanh mảnh, dáng đứng giáo sĩ uy nghiêm | fair | khuyên vàng nhỏ ở tragus tai trái | chuông xa, da cừu, chữ cổ |
| **[VI]** **THE LOVERS** `06-lovers` | 21 | chestnut-amber, doe, liếc nghiêng say đắm về phía người kia | warm chestnut-brown hair gathered in a loose romantic knot with soft wisps framing her cheeks | **A** đồng hồ mảnh, eo mềm, uyển chuyển | warm peach | lúm đồng tiền má phải | hoa cam, gió hè, lời hứa |
| **[VII]** **THE CHARIOT** `07-chariot` | 22 | steel-blue, narrow, quyết đoán, không chớp | dark sable-brown hair tightly plaited in a single thick warrior braid over one shoulder | **B** săn chắc, vai tạc, eo thắt, dáng trụ vững | light olive | sẹo nhỏ hình tia chớp trên cẳng tay phải | bụi đường, vó ngựa, cờ |
| **[VIII]** **STRENGTH** `08-strength` | 23 | amber-gold như mắt sư tử, almond, rực và ôn hòa | burnished copper-red long wavy hair flowing down like a lion's mane | **B** mảnh mà khỏe, lưng cơ mềm, cong tự nhiên | warm tan | tàn nhang li ti khắp sống mũi và má | nắng chiều, lông sư tử, hơi thở ấm |
| **[IX]** **THE HERMIT** `09-hermit` | 23 | silver-grey gần như trong suốt, dreamy, an tĩnh | ethereal silver-ash long hair, veiled beneath sheer white cowl gauze | **A** mảnh, huyền bí, dáng ngồi thiền | porcelain | bớt hình mặt trăng trên cổ tay phải trong | tuyết rơi im lặng, nến |
| **[X]** **WHEEL OF FORTUNE** `10-wheel` | 22 | golden-hazel, upturned, nhìn xa như tiên tri | golden-amber braided hair crowned with mystic celestial laurels | **B** cao, thanh gọn, dáng thiên thần canh gác | warm tan | 3 khuyên vàng nhỏ xếp dọc vành tai trái | gió xoáy, tiếng bánh xe, sao |
| **[XI]** **JUSTICE** `11-justice` | 24 | grey-green, wide-set, nhìn thẳng không chớp | sleek raven-black hair drawn back sharply into a high polished half-ponytail | **B** cao, thanh thoát, xương đòn nổi, lưng thẳng | ivory | sẹo mảnh dọc hàm trái | cán cân, đá cẩm thạch, im lặng |
| **[XII]** **THE HANGED MAN** `12-hanged` | 21 | teal sâu, heavy-lidded, đảo ngược mà vẫn bình thản | golden-brown tousled locks cascading downward with gravity, glowing in ethereal light | **A** mảnh dẻo như vũ công, tư thế treo lơ lửng thanh thoát | light olive | hình xăm dây thường xuân quanh mắt cá trái | chạng vạng, rễ cây, nước |
| **[XIII]** **DEATH** `13-death` | 22 | ice-blue nhạt, hooded, không thể đọc | long bone-platinum hair flowing behind an ornate gothic helm | **A** cao, mảnh, bóng dáng kỵ sĩ lạnh | porcelain | xăm hoa hồng trắng trên xương bả vai phải | sương lạnh, bông hoa héo |
| **[XIV]** **TEMPERANCE** `14-temperance` | 22 | aquamarine, upturned nhẹ, sáng trong như nước | pale fine ash-blonde hair floating weightlessly in the air | **A** sẽ gầy mảnh, tay chân dài, lưng cong mềm | fair | sẹo bạc hình lưỡi liềm trên lòng bàn tay phải | nước chảy, ánh sáng xuyên, sự cân bằng |
| **[XV]** **THE DEVIL** `15-devil` | 21 | wine-plum, cat, heavy-lidded, đốt mắt | midnight-black wavy hair with deep wine-red undertones, wild and untamed | **D** cong đầy đặn vừa, hông mềm, lưng võng gợi cảm | sand | nốt ruồi đỏ thẫm ở khóe môi | khói ngọt, gỗ đàn hương, dây xích |
| **[XVI]** **THE TOWER** `16-tower` | 20 | slate-grey, round, mở to kinh ngạc giữa cú rơi | storm-dark chestnut hair blown dynamically backward by lightning winds | **B** săn, dẻo, thân hình nhào lộn | fair | sẹo trắng mảnh trên xương đòn trái | sấm, gió giật, đá vụn |
| **[XVII]** **THE STAR** `17-the-star` | 20 | starlight grey-blue, wide-set, long lanh như nước đêm | very long pale shimmering gold hair, wet and silky, cascading down past one bare shoulder | **A** mảnh, chân dài, thần thái nữ thần thanh khiết | ivory | chòm tàn nhang vàng trên hai vai | nước đêm, sao, làn da ướt |
| **[XVIII]** **THE MOON** `18-moon` | 21 | moonstone silver-violet, heavy-lidded, mơ màng | ink-blue-black hair with cool silvery highlights, cascading like water to her hips | **A** mảnh như tiên nữ, eo mềm, hông cong nhẹ | porcelain | sẹo lưỡi liềm nhỏ trên gò má trái | sương, hồ tối, tiếng nước |
| **[XIX]** **THE SUN** `19-sun` | 19 | gold-green (moss-gold), round, cười long lanh | radiant sunflower-blonde hair, bouncing loose curls garlanded in red blossoms | **A** trẻ trung, gầy nhẹ, cong mềm vui vẻ | honey | vệt tàn nhang vàng trên sống mũi | hoa hướng dương, mùa hè |
| **[XX]** **JUDGEMENT** `20-judgement` | 22 | amber với vệt vàng kim, upturned, mở to như vừa thức giấc | rich amber-honey hair in thick luminous waves catching golden rays | **B** cao thanh thoát, vòng tay mở, dáng tái sinh | warm peach | sẹo nhỏ hình lông phượng sau gáy | đồng vọng, kèn xa, rạng đông |
| **[XXI]** **THE WORLD** `21-world` | 22 | emerald sâu, wide-set, sáng và đầy đủ | dark chocolate-chestnut hair swirling freely with violet silk ribbons | **B** dáng vũ công hoàn mỹ, chân dài, eo thon | warm tan | khuyên vàng nhỏ ở cánh mũi phải | vũ điệu, gió bốn hướng, hoa dại |

---

## 4. BẢNG CHÍNH — WANDS · 12 NHÂN VẬT (trừ Ace & Eight)

| Lá | Tuổi | Đôi mắt | Kiểu tóc (chuẩn) | Vóc dáng | Màu da | Nét riêng | Không khí |
|---|---|---|---|---|---|---|---|
| **TWO OF WANDS** `wands-02` | 22 | auburn-brown, almond, nhìn xa trầm ngâm | deep auburn hair falling in long loose ringlets over one shoulder | **A** mảnh, dáng đứng thẳng trầm tư | fair | nốt ruồi nhỏ trên môi trên bên phải | gió biển, đá ấm, chân trời |
| **THREE OF WANDS** `wands-03` | 23 | honey-brown, almond, quyết tâm nhìn về khơi xa | warm caramel-brown hair loosely braided with golden cord | **B** cao, mảnh, lưng dài hướng về chân trời | warm tan | khuyên vàng nhỏ ở ngón cái tay phải | hoàng hôn, bến cảng, buồm |
| **FOUR OF WANDS** `wands-04` | 20 | dark cherry-violet, round, lấp lánh tinh nghịch | blue-black hair piled high in a floral-pinned braided updo | **B** mảnh dẻo, eo vũ công, tay nâng duyên dáng | light olive | chùm tàn nhang hình bông hoa trên vai trái | nến, vũ hội, cánh hoa |
| **FIVE OF WANDS** `wands-05` | 21 | hazel-green sắc, narrow, tập trung như so gươm | short tousled copper-brown hair damp with exertion | **B** săn gọn, cơ mềm, dáng đấu tập linh hoạt | sand | sẹo mảnh qua khớp ngón tay phải | bụi đấu trường, tiếng gậy |
| **SIX OF WANDS** `wands-06` | 22 | golden-amber, upturned, kiêu hãnh ngẩng cao | honey-gold hair billowing triumphantly in the wind | **B** cao, thanh, dáng cưỡi ngựa hiên ngang | warm tan | dãy khuyên vàng nhỏ dọc vành tai trái | reo hò, cờ, nắng thắng trận |
| **SEVEN OF WANDS** `wands-07` | 21 | dark chestnut, narrow, cảnh giác dưới lông mày thấp | dark espresso hair cropped close at sides with messy curls on top | **A** mảnh, dai, gân gọn, dáng phòng thủ | light olive | vết khía nhỏ ở chân mày trái | rìa rừng, đêm, lửa nhỏ |
| **NINE OF WANDS** `wands-09` | 24 | umber, hooded, canh chừng không chớp | dark brown hair pulled back with a simple leather tie | **B** vai rộng, săn bền, dáng canh gác | warm tan | dải sẹo nhỏ hình mào chim trên vai phải | lửa trại, đội canh, sương đêm |
| **TEN OF WANDS** `wands-10` | 23 | deep brown viền amber, heavy-lidded, mệt nhưng kiêu | damp chestnut hair clinging to brow from labor | **B** lưng khỏe, vai vững, cơ bắp làm việc | sand | vết sẹo bỏng nhỏ trên cẳng tay trái | mồ hôi, lúa, đất ấm |
| **PAGE OF WANDS** `wands-page` | 18 | ginger-amber, round, tò mò rực sáng | short tousled ginger-auburn hair cut in a playful textured bob | **A** nhỏ nhắn, nhanh nhẹn, dáng hăng hái | fair | tàn nhang li ti trên hai cẳng tay | nắng non, con đường, trống |
| **KNIGHT OF WANDS** `wands-knight` | 22 | gold-green, almond, cười rộng táo bạo | wind-whipped golden-brown curls peeking beneath a feathered diadem | **B** mảnh săn, cơ bụng gọn, dáng phi nước đại | light olive | dây chuyền vàng mảnh ở cổ tay phải | lửa, vó ngựa, lông vũ |
| **QUEEN OF WANDS** `wands-queen` | 24 | russet-amber, upturned, ấm mà thống trị | a magnificent mane of rich russet-red waves crowning her head | **D** đầy đặn vừa, cong nữ tính, dáng ngồi hỏa diệm | honey | khuyên vàng hình mặt trời trên chân mày trái | lửa ấm, da báo, gia vị |
| **KING OF WANDS** `wands-king` | 25 | bronze-gold, hooded, uy nghiêm | dark bronze hair swept back in an ornate crown braid with fiery orange ribbons | **B** cao, vai rộng, dáng quân chủ thanh thoát | light bronze | băng tay xăm hình ruy băng cam quanh cổ tay phải | rồng, hoàng kim, gió lửa |

---

## 5. BẢNG CHÍNH — CUPS · 13 NHÂN VẬT (trừ Ace)

| Lá | Tuổi | Đôi mắt | Kiểu tóc (chuẩn) | Vóc dáng | Màu da | Nét riêng | Không khí |
|---|---|---|---|---|---|---|---|
| **TWO OF CUPS** `cups-02` | 21 | hazel-green mềm, upturned, say mê nhìn người kia | soft ash-brown hair worn in a low intertwined romantic braid | **A** mảnh, dáng nghiêng giao hòa uyển chuyển | fair | lúm đồng tiền má trái | nước mưa, hứa hẹn, hoa táo |
| **THREE OF CUPS** `cups-03` | 20 | ba đôi mắt khác nhau: chocolate doe · amber almond · copper-green cat | rich chocolate-brown, golden-blonde, and copper hair among the three maidens | **C** ba dáng hài hòa: mảnh · trung bình mềm · tròn trịa mềm | warm peach · honey · fair | mỗi cô cài một bông: hồng · tím · cúc | tiếng cười, rượu nho, vườn mùa |
| **FOUR OF CUPS** `cups-04` | 22 | grey-blue mờ, downturned, chán lơ đãng | dark wavy hair falling over her shoulder in contemplative thought | **A** mảnh, dáng ngồi thả lỏng thờ ơ | fair | nốt ruồi nhỏ trên gò má phải | bóng cây, buồn nhẹ, dòng nước |
| **FIVE OF CUPS** `cups-05` | 22 | watery hazel, downturned, khóe mắt ướt | long mahogany hair unbound and draping over cloaked shoulders | **A** mảnh, dáng cúi cổ thanh mảnh buồn | porcelain | tàn nhang như hạt mưa trên mu bàn tay | mưa phùn, áo choàng ướt |
| **SIX OF CUPS** `cups-06` | 19 | baby-blue, doe, ngây thơ | pale golden hair styled in a delicate maiden crown knot | **A** nhỏ nhắn, mềm mại, dáng đứng dễ thương | warm peach | bớt màu tím nhạt hình cánh hoa trên vai phải | sân vườn, kẹo mật, ký ức |
| **SEVEN OF CUPS** `cups-07` | 21 | violet-grey, dreamy, nửa khép trong mê | dark raven curls drifting in mystical haze | **A** mảnh, dáng đứng mê hoặc, tay khẽ nâng | fair | khuyên bạc lưỡi liềm trên sụn tai phải | khói mộng, gương, ảo ảnh |
| **EIGHT OF CUPS** `cups-08` | 23 | deep brown, narrow, quyết tâm quay lưng | deep brown hair tucked under a travel cloak | **B** mảnh gọn, bóng dáng lữ khách dứt khoát | light olive | sẹo nhỏ hình la bàn trên lòng bàn tay trái | mưa, bước chân, núi xa |
| **NINE OF CUPS** `cups-09` | 24 | amber-brown, upturned, cười cong như trăng | warm honey-brown hair in a relaxed loose chignon | **C** mềm mại cân đối, cong tự nhiên trung bình | honey | khuyên vàng hình hoa hồng nhỏ ở dái tai phải | rượu ngọt, nến, ghế bành ấm |
| **TEN OF CUPS** `cups-10` | 22 | hazel mềm, warm, dịu dàng | warm hazel-brown hair cascading in silky ripples | **C** thanh-mềm, dáng mẹ trẻ đầy ân cần | warm peach | bớt hình trái tim mờ trên hông trái | tổ ấm, cầu vồng, tiếng trẻ |
| **PAGE OF CUPS** `cups-page` | 18 | smoky-blue, doe, ngạc nhiên đầy mộng mơ | dark glossy hair in a single side fishtail braid over the collarbone | **A** nhỏ nhắn, tay chân mảnh, dáng cầm chén | fair | khuyên bạc hình ngôi sao trên vành tai phải | giấc mơ, cá bạc, nước |
| **KNIGHT OF CUPS** `cups-knight` | 22 | sea-blue dịu, almond, lãng mạn | fair sandy-blonde hair falling in soft romantic waves across her brow | **B** mảnh cao, dáng hiệp sĩ thi ca | warm tan | sẹo mảnh hình lông vũ trên vai phải | sông thơ, hoa súng, trăng |
| **QUEEN OF CUPS** `cups-queen` | 23 | silver-platinum, heavy-lidded, huyền bí | long shimmering platinum-blonde hair falling straight like water to her thighs | **A** mảnh, eo nhỏ, vẻ đẹp nữ hoàng mộng mị | porcelain | bớt lưỡi liềm bạc nhỏ sau gáy | nước ngọc, ánh trăng, thì thầm |
| **KING OF CUPS** `cups-king` | 25 | ocean-blue sâu, hooded, vị vương giả bình thản | deep-wave dark espresso hair crowned in sea-gold and pearls | **C** cao, đầy và vững, dáng ngồi biển cả | light olive | nhẫn vàng trơn ở ngón giữa tay phải | biển lặng, thủy triều, ngọc trai |

---

## 6. BẢNG CHÍNH — SWORDS · 12 NHÂN VẬT (trừ Ace & Three)

| Lá | Tuổi | Đôi mắt | Kiểu tóc (chuẩn) | Vóc dáng | Màu da | Nét riêng | Không khí |
|---|---|---|---|---|---|---|---|
| **TWO OF SWORDS** `swords-02` | 21 | flint-grey, ẩn sau lụa, vẫn căng | jet-black hair drawn back into a sleek, flawless high knot | **B** mảnh cân, cơ bụng săn, dáng giữ thăng bằng | ivory | khóa vàng nhỏ ở thái dương phải (giữ lụa) | im lặng căng, nước đứng |
| **FOUR OF SWORDS** `swords-04` | 22 | nhắm — hàng mi dài xám nhạt, nghỉ ngơi | deep sable hair spread neatly around her resting head on stone | **A** mảnh, dáng nằm tạc tượng thanh tịnh | porcelain | sẹo bạc hình thánh giá nhỏ trên cổ tay trái | nhà nguyện, tro, gió chùa |
| **FIVE OF SWORDS** `swords-05` | 22 | dark emerald, almond, liếc xéo tự mãn | wind-blown dark brown hair with a subtle confident smirk | **B** mảnh nhanh, vai sắc, dáng xoay người gọn | light olive | sẹo mảnh xé đôi chân mày phải | gió thắng, lá khô, cười mỉa |
| **SIX OF SWORDS** `swords-06` | 21 | misty grey mềm, downturned, trầm | light ash-brown hair gathered softly in a misty veil | **A** mảnh, dáng ngồi thuyền lặng lẽ | fair | dây bạc nhỏ hình con thuyền ở mắt cá chân | sông sương, mái chèo, đi xa |
| **SEVEN OF SWORDS** `swords-07` | 20 | dark brown, cat, ánh mắt láu lỉnh lướt nhanh | mischievous tousled dark chestnut hair | **A** mảnh nhẹ, dáng rón rén của kẻ trộm | sand | sẹo trắng mảnh ngang lòng bàn tay phải | bóng tối, bước chân lén, bạc |
| **EIGHT OF SWORDS** `swords-08` | 20 | fear-bright hazel, doe, viền nước mắt | dark brown hair bound loosely with a crimson ribbon | **A** mảnh mong manh, dáng co lại | fair | vết bớt đỏ nhạt hình dải lụa trên mắt cá phải | hoàng hôn, dây thắt, lưỡi kiếm |
| **NINE OF SWORDS** `swords-09` | 22 | grey-brown buồn, downturned, ướt | long black hair falling in sorrowful waves over her weeping hands | **A** mảnh, dáng ngồi trong váy ngủ, gầy | porcelain | nốt ruồi hình giọt nước trên má phải | đêm trằn trọc, tiếng khóc, gió |
| **TEN OF SWORDS** `swords-10` | 23 | nhắm, hàng mi dài, bình yên dưới nắng | dark silky hair strewn across shoreline sand | **B** mảnh thanh thản, dáng nằm hòa vào bờ cát | warm peach | sẹo nhỏ hình ngôi sao trên khuỷu tay phải | bình minh sau bão, sóng, cỏ |
| **PAGE OF SWORDS** `swords-page` | 18 | honey-hazel sắc, almond, cảnh giác | windswept honey-brown hair cut in a sharp feathered pixie cut | **B** mảnh nhanh, dáng đứng trên đồi sẵn sàng | warm tan | sẹo nhỏ khía cằm | đồi đá, gió sắc, dấu chân |
| **KNIGHT OF SWORDS** `swords-knight` | 21 | blazing grey-blue, narrow, hung hãn | dark hair streaming wildly back from beneath an open winged helmet | **B** mảnh săn, dáng phi thẳng tấn công | sand | xăm nhỏ hình mũ giáp cánh trên vai trái | sấm vó, gió thét, thép |
| **QUEEN OF SWORDS** `swords-queen` | 24 | jade lạnh, hooded, sắc lẹm | deep mahogany-red hair in an intricate woven crown braid | **B** cao thanh thoát, xương đòn nổi, dáng ngồi thẳng | ivory | sẹo mảnh hình lưỡi kiếm trên xương đòn phải | sương giá, trí tuệ, con dao giải phẫu |
| **KING OF SWORDS** `swords-king` | 25 | steel-grey, narrow, xét xử | clean-cut raven hair crowned with sharp golden circlet | **B** cao, dáng thẩm phán uy nghi | light olive | sẹo trắng mảnh trên ngón cái phải | tòa án, ánh thép, công lý |

---

## 7. BẢNG CHÍNH — PENTACLES · 13 NHÂN VẬT (trừ Ace)

| Lá | Tuổi | Đôi mắt | Kiểu tóc (chuẩn) | Vóc dáng | Màu da | Nét riêng | Không khí |
|---|---|---|---|---|---|---|---|
| **TWO OF PENTACLES** `pentacles-02` | 19 | hazel-gold vui, round, lấp lánh | tousled sandy-gold curls bouncing with her dance | **B** mảnh dẻo, vũ công cân bằng | fair | bớt tròn như đồng xu sau tai phải | nhạc đường phố, gió, tiếng cười |
| **THREE OF PENTACLES** `pentacles-03` | 22 | walnut-brown, almond, tập trung hạ mí | dark auburn hair coiled in a practical braided crown | **B** vai nghệ nhân săn gọn, tay khéo | light olive | tàn nhang màu đất li ti trên hai bàn tay | đá, phấn, tiếng đục |
| **FOUR OF PENTACLES** `pentacles-04` | 24 | deep umber, heavy-lidded, phòng vệ | neatly combed dark brown hair holding gold close | **C** chắc cân đối, dáng ngồi vững vàng | warm tan | nhẫn vàng trơn ở ngón trỏ tay trái | két sắt, im lặng, đất |
| **FIVE OF PENTACLES** `pentacles-05` | 20 | icy-grey nhạt, doe, run rẩy mệt mỏi | long windswept dark-brown hair catching falling snow | **A** mảnh, dáng co mình dưới cửa sổ nhà thờ | porcelain | bớt trắng như sương trên cổ | tuyết, đói, cửa sổ sáng |
| **SIX OF PENTACLES** `pentacles-06` | 23 | warm hazel, almond, rộng lượng thẳng thắn | well-groomed golden-brown hair in merchant styling | **C** cân đối tử tế, dáng đứng phân phát | sand | khuyên vàng hình đồng xu ở dái tai trái | chợ, bánh mì, tiếng đồng xu |
| **SEVEN OF PENTACLES** `pentacles-07` | 22 | hazel-green mỏi mà hy vọng, heavy-lidded | sweat-touched warm chestnut hair resting on hoe handle | **B** săn nông dân, tay chắc, dáng tựa cuốc | warm tan | sẹo nhỏ hình chiếc lá trên xương bả vai phải | ruộng nắng, đất, mùa vụ |
| **EIGHT OF PENTACLES** `pentacles-08` | 21 | seal-brown, cúi mắt cực tập trung | chestnut hair bound in a neat, focused low chignon | **A** mảnh, tay tỉ mỉ, dáng cúi trên bàn | fair | xăm mực vàng hình đồng xu trên cổ tay trái | xưởng đá, tiếng khắc, dầu |
| **NINE OF PENTACLES** `pentacles-09` | 23 | deep espresso vệt xanh, almond, kiêu hãnh bình thản | long vine-dark espresso hair loosely curled with gold thread | **C** đồng hồ thanh lịch, cong mềm trung bình | honey | nhẫn vàng mảnh ở mắt cá phải | vườn nho, vàng, chim sẻ |
| **TEN OF PENTACLES** `pentacles-10` | 22 | warm brown, almond, ấm áp trưởng giả | warm honey-brown hair in a thick braided crown | **C** mềm mại, dáng mẫu hệ hiền | warm peach | bớt hình chiếc lá sau tai trái | gia tộc, bàn ăn, mùa gặt |
| **PAGE OF PENTACLES** `pentacles-page` | 18 | sunny hazel, round, chân thành | golden-blonde hair falling loose past shoulders, catching meadow sun | **A** nhỏ nhắn, dáng học trò nghiêm túc | fair | chòm tàn nhang nhỏ trên xương đòn phải | đồng cỏ, sách cũ, hoa |
| **KNIGHT OF PENTACLES** `pentacles-knight` | 23 | earth-brown, almond, điềm tĩnh bền bỉ | dark bronze hair braided under an oak-leaf crested helmet | **B** săn chắc, dáng kỵ sĩ nặng mà thong thả | warm tan | sẹo nhỏ hình lá sồi trên cẳng tay trái | đường đất, bụi, ngựa thở |
| **QUEEN OF PENTACLES** `pentacles-queen` | 24 | molten brown ấm, upturned, nữ hoàng bao dung | deep chocolate hair with a ruddy golden sheen, crowned in blooming vines | **D** đầy đặn vừa, cong mềm mẫu tính | honey | bớt hình hoa hồng trên vai trái | vườn trái, bơ, tiếng gà |
| **KING OF PENTACLES** `pentacles-king` | 25 | deep brown ánh amber, hooded, hào phóng | dark wavy hair woven with golden laurel leaves and ripe grapes | **C** vững chãi, đầy-ở-mức-trung-bình, dáng ngồi ung dung | sand | nhẫn vàng lá nguyệt quế ở ngón áp út phải | lâu đài, mùa nho, đồng tiền |

---

## 8. KIỂM TRA NHANH (CHECKLIST)

- [x] 72/72 nhân vật có đủ: tuổi · mắt · tóc (chuẩn) · vóc dáng (A–D) · da · nét riêng · không khí
- [x] 0 nhân vật da đen / da sẫm — chỉ 10 tông từ porcelain → amber-gold
- [x] 0 nhân vật vượt trần "trung bình" — không plus-size, không béo (A 29 · B 30 · C 9 · D 4)
- [x] Mỗi nhân vật 1 tổ hợp mắt (màu + dáng + ánh nhìn) duy nhất
- [x] Mỗi nhân vật 1 nét riêng duy nhất (không trùng)
- [x] Tuổi và kiểu tóc giữ nguyên 100% so với bảng chuẩn `01-CARD-TABLE.md`
- [x] 6 lá không nhân vật được loại trừ đúng: wands-ace, wands-08, cups-ace, swords-ace, swords-03, pentacles-ace
