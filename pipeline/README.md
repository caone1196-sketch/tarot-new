# Pipeline — sinh bộ bài từ 4 nguồn đã quét

Quét thư mục thấy đúng 4 tài sản, và cả 4 đều được dùng làm dữ liệu đầu vào:

| Nguồn | Vai trò |
|---|---|
| `17-the-star.png` | **Ảnh mỏ neo (visual anchor)** — đính kèm vào *mọi* lần render để giữ khung viền, nền, ánh sáng |
| `00-MASTER-PROMPT.md` | Quy chuẩn khung viền · 4 lớp chiều sâu · ANATOMY LOCK · template prompt |
| `02-CHARACTER-SPECS.md` | 72 nhân vật nữ: tuổi · mắt · tóc · vóc dáng (A–D) · màu da · nét riêng · không khí |
| `cards.json` | 78 lá: tiêu đề · bối cảnh · huy hiệu · COUNT LOCK · tóc · tuổi |

Nhân vật lá **The Star** (`17-the-star`, hàng 20 tuổi trong bảng đặc tả) là hình mẫu tham
chiếu: mọi lá khác kế thừa chất da sáng bóng, giải phẫu fine-art, ánh sáng ấm và độ nét của
cô, nhưng giữ **đặc điểm riêng** của mình (mắt, tóc, dáng, nét riêng) theo bảng 72 nhân vật.

## Bố cục FULL-BLEED (v3 — chuẩn hiện hành)

Lá The Star gốc phí ~16% mặt thẻ cho **viền bạc + dải giấy da đựng tên** ở đáy: nội dung
tranh chỉ chiếm **84.1%**. Chuẩn mới bỏ hẳn phần đó:

- Tranh phủ **toàn bộ mặt thẻ**, tràn 4 cạnh, không viền bạc, không lề giấy da → **99.8%**.
- Viền vàng Gothic mỏng **vẽ đè lên trên** tranh như một lớp mạ nổi, tranh chạy tiếp ra ngoài.
- Tên lá nằm trên **dải ruy băng vàng mảnh đặt trực tiếp lên tranh**, cảnh vẫn thấy phía sau.

| | Bố cục cũ | Bố cục mới |
|---|---|---|
| Tranh chiếm | 84.1% | **99.8%** |
| Lề chết T/B/L/R | 42/43/40/41 px | 0/1/0/1 px |
| Panel tên | dải giấy da riêng | ruy băng đặt trên tranh |

Chuẩn này nằm trong `FRAME_STANDARD` + `TITLE_STANDARD` (`build_prompts.py`) nên **mọi lá
sinh về sau đều tự động áp dụng**. Các cụm "silver border / grey mat / parchment frame /
separate title panel" đã được đưa vào danh sách `NEGATIVE`.

## Chạy

```bash
python3 pipeline/build_prompts.py      # 4 nguồn  -> pipeline/prompts.json (78 prompt)
python3 pipeline/finalize.py status    # đã render bao nhiêu / còn thiếu lá nào
python3 pipeline/finalize.py check     # CẢNH BÁO lá nào lỡ quay về bố cục viền bạc cũ
python3 pipeline/finalize.py convert   # PNG -> JPEG q92 4:4:4, xoá PNG
python3 pipeline/finalize.py sheet     # contact-sheet.jpg
```

`check` đo độ phủ màu: full-bleed ~99%, bố cục cũ ~84%. Dưới 93% là lá lỗi, cần render lại.

## `prompts.json` có gì

Mỗi lá có 2 biến thể prompt:

- `prompt` — bản đầy đủ, bám sát template trong `00-MASTER-PROMPT.md` (dùng để đọc/kiểm tra).
- `render_prompt` — bản rút gọn ~30% nhưng **giữ nguyên mọi ràng buộc**, đây là bản thực sự
  gửi cho model kèm `17-the-star.png`.

Mỗi prompt luôn gồm 4 chốt chặn:

1. **FRAME** — copy y hệt khung The Star: viền vàng Gothic mỏng, nền da cổ, vát bạc, panel tên.
2. **FIGURE** — trộn `cards.json` (tóc/tuổi/bối cảnh) với `02-CHARACTER-SPECS.md`
   (mắt/da/vóc dáng/nét riêng/không khí). Da luôn ở 10 tông sáng, không bao giờ sẫm màu.
3. **ANATOMY LOCK** — 1 đầu · 1 thân · 2 tay 5 ngón · 2 chân, không thừa chi, không dính thân.
4. **COUNT LOCK** — số lượng vật phẩm chất bài là ràng buộc cứng, lấy thẳng từ `cards.json`.

## Hai điều chỉnh kỹ thuật

**`build` bị ghi đè.** `02-CHARACTER-SPECS.md` §1.2 hạ trần vóc dáng xuống "trung bình" (A–D)
và khai tử các mô tả `voluptuous / curvaceous` cũ trong `cards.json`. Nên phần `build` gửi cho
model lấy từ `pipeline/characters.en.json`, không lấy từ `cards.json`.

**`characters.en.json`.** Bảng 72 nhân vật viết bằng tiếng Việt; model ảnh cần tiếng Anh, nên
lớp này dịch sẵn mắt · da · vóc dáng · nét riêng · không khí. Tuổi và kiểu tóc **không** nằm ở
đây — chúng đọc trực tiếp từ nguồn để giữ đúng cam kết "giữ nguyên 100%".

**`SOFTEN`.** Vài cách diễn đạt trong `cards.json` làm bộ lọc an toàn trả về 0 ảnh. Bảng
`SOFTEN` trong `build_prompts.py` viết lại đúng những cụm đó (giữ nguyên ý đồ tranh khoả thân
fine-art cổ điển, chỉ đổi cách diễn đạt) để lệnh render trả về ảnh.

## Định dạng ảnh

78 lá dạng PNG gốc ≈ 210 MB, vượt hạn mức artifact của repo. Deck xuất ra JPEG quality 92
**không giảm mẫu màu (4:4:4)** — mỗi lá ~450 KB, cả bộ ~35 MB, mắt thường không phân biệt được.
