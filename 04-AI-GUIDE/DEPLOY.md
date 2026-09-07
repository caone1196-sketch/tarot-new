# 🚀 HƯỚNG DẪN TRIỂN KHAI — BIẾN REPO NÀY THÀNH "AI VẼ TAROT"

> Sau khi làm 1 trong các cách dưới đây, bạn chỉ cần nói **"vẽ lá mặt trăng"** / **"tạo Nine of Swords"** — AI tự đọc hướng dẫn, tự lấy prompt đúng, tự kiểm tra chất lượng.

---

## 0. BỘ FILE CẦN MANG THEO (tối thiểu)

| Ưu tiên | File | Bắt buộc? |
|---|---|---|
| 1 | `04-AI-GUIDE/AI-INSTRUCTIONS.md` | ✅ Bắt buộc — bộ não vận hành |
| 2 | `03-PROMPTS-78-FULL.md` *(hoặc `prompts-full.json`)* | ✅ Bắt buộc — nguồn 78 prompt |
| 3 | `the moon.png` | ⭕ Tùy chọn — tham chiếu phong cách |
| 4 | `01-CARD-TABLE.md` + `cards.json` | ❌ Chỉ cần khi AI phải tự dựng prompt từ dữ liệu |

---

## 1. CÁCH NHANH NHẤT — DÁN TRỰC TIẾP VÀO CHAT (0 phút setup)

Dùng cho: **ChatGPT · Claude · Gemini · bất kỳ AI chat nào** (miễn hỗ trợ đọc file/văn bản dài).

1. Mở chat mới với AI có khả năng **tạo ảnh**.
2. Đính kèm 2 file: `04-AI-GUIDE/AI-INSTRUCTIONS.md` + `03-PROMPTS-78-FULL.md` (nếu AI không đọc được file đính kèm → dán nội dung `AI-INSTRUCTIONS.md` vào tin nhắn đầu).
3. (Tùy chọn) đính kèm `the moon.png` làm ảnh tham chiếu phong cách.
4. Gõ: **"Hãy đọc file hướng dẫn rồi vẽ lá [tên lá]"** — xong.

✅ Ưu điểm: làm được ngay, không cần tài khoản trả phí.
❌ Nhược điểm: mỗi chat mới phải đính kèm lại.

---

## 2. TRIỂN KHAI LÂU DÀI — TẠO AI RIÊNG CỦA BẠN

### 2.1 ChatGPT — Custom GPT (cần Plus/Team)
1. Vào **chatgpt.com → Explore GPTs → Create**.
2. ô **Instructions**: dán toàn bộ nội dung `AI-INSTRUCTIONS.md` (thêm câu: *"Prompt nguồn nằm trong file Knowledge."*).
3. mục **Knowledge**: upload `03-PROMPTS-78-FULL.md` (hoặc `prompts-full.json`) + `the moon.png`.
4. Bật **Capabilities: Image Generation** (để DALL·E/GPT-image vẽ ngay trong GPT).
5. Save → từ giờ mở GPT này ra, gõ *"vẽ lá mặt trăng"* là chạy đúng quy trình A.

### 2.2 Claude — Projects (cần Pro/Max)
1. **claude.ai → Projects → New Project** (VD: "Tarot Deck").
2. **Project Instructions**: dán nội dung `AI-INSTRUCTIONS.md`.
3. **Project Knowledge**: upload `03-PROMPTS-78-FULL.md` + `the moon.png`.
4. Mỗi lần vẽ: mở project → gõ yêu cầu. Claude sẽ trích prompt đúng lá và có thể viết lệnh tạo ảnh / bàn giao prompt cho công cụ vẽ.

### 2.3 Gemini — Gems (cần tài khoản Google)
1. **gemini.google.com → Gems → New Gem**.
2. **Instructions**: dán `AI-INSTRUCTIONS.md` + ghi rõ "Prompt nguồn trong file đính kèm Knowledge".
3. **Upload files** (nếu gói hỗ trợ): `03-PROMPTS-78-FULL.md`, `the moon.png`.
4. Save Gem "Tarot Artist" → gọi khi cần.

### 2.4 Arena.ai Agent Mode (nơi bạn đang dùng repo này)
- Repo `tarot-new` đã nằm sẵn trong workspace → chỉ cần nói trực tiếp trong phiên: **"vẽ lá X theo repo"** — agent sẽ tự đọc `04-AI-GUIDE/` và làm đúng quy trình.

---

## 3. TRIỂN KHAI CHO AI LẬP TRÌNH / AGENT (Cursor · Copilot · API)

### 3.1 Để AI trong repo tự nhận hướng dẫn
- File đã ở trong repo → AI agent (Cursor, Copilot Workspace, Arena...) sẽ thấy khi được yêu cầu việc liên quan tarot.
- **Mẹo hiển thị ngay trang chủ GitHub / dễ thấy nhất**: copy `AI-INSTRUCTIONS.md` thành `README.md` ở thư mục gốc (giữ nguyên bản trong `04-AI-GUIDE/` cũng được).
- Nếu dùng **GitHub Copilot**: thêm file `.github/copilot-instructions.md` chứa nội dung rút gọn: *"Đọc 04-AI-GUIDE/AI-INSTRUCTIONS.md trước khi làm bất kỳ việc gì liên quan đến bộ bài tarot."*

### 3.2 Dùng qua API (tự động hóa hoàn toàn)
Cấu trúc chuẩn cho mọi API (OpenAI, Anthropic, Gemini...):

```python
# system prompt = nội dung AI-INSTRUCTIONS.md
system = open("04-AI-GUIDE/AI-INSTRUCTIONS.md", encoding="utf-8").read()
# prompt của lá cần vẽ — lấy từ prompts-full.json
import json
prompts = {p["slug"]: p["prompt"] for p in json.load(open("prompts-full.json"))["prompts"]}
user_message = "Vẽ lá 18-moon"
# → gắn prompts["18-moon"] vào pipeline tạo ảnh của bạn
```

Hoặc dùng script sẵn có trong thư mục này:
```bash
python 04-AI-GUIDE/get-prompt.py 18-moon          # theo slug
python 04-AI-GUIDE/get-prompt.py "mặt trăng"       # theo tên Việt
python 04-AI-GUIDE/get-prompt.py "nine of swords"  # theo tên Anh
```

---

## 4. SO SÁNH NHANH

| Cách | Setup | Dùng lại | Vẽ ảnh luôn | Phù hợp |
|---|---|---|---|---|
| 1. Dán vào chat | 0 phút | ❌ mỗi lần | Tùy AI | Thử nhanh |
| 2. Custom GPT / Gem / Project | 5–10 phút | ✅ vĩnh viễn | ✅ (GPT, Gemini) | **Khuyên dùng** |
| 3. Agent trong repo | 0 (sẵn sàng) | ✅ | Tùy nền tảng | Làm việc trên code/repo |
| 3.2 API + script | 15–30 phút | ✅ tự động | Tự tích hợp | Chạy loạt 78 lá |

💡 **Gợi ý lộ trình:** dùng Cách 1 thử vài lá cho ưng → rồi dựng Custom GPT/Project (Cách 2) làm "xưởng vẽ" cố định → nếu cần sinh cả bộ 78 lá loạt thì chuyển sang API (Cách 3.2).

---

## 5. LƯU Ý KHI TRIỂN KHAI

1. **Chỉnh sửa phải đổi ở nguồn**: sửa prompt → sửa `cards.json`/`03-PROMPTS-78-FULL.md` (hoặc yêu cầu AI agent trong repo sửa rồi tái sinh) — đừng sửa từng bản sao dán trong chat.
2. **Bản dán vào Custom GPT/Gem là bản chụp** — mỗi lần cập nhật repo phải dán lại.
3. **Kiểm tra sau khi setup**: nói thử *"vẽ lá mặt trăng"* — AI đúng quy trình sẽ: hỏi/lấy prompt `18-moon` nguyên văn → sinh full-bleed không khung → trả kèm checklist 3 điểm. Nếu AI tự bịa prompt → nó chưa đọc file hướng dẫn, kiểm tra lại Knowledge/Instructions.
4. **Ảnh tham chiếu**: chỉ dùng `the moon.png` khi công cụ hỗ trợ ảnh tham chiếu; prompt đã tự mô tả phong cách bằng chữ nên không bắt buộc.
