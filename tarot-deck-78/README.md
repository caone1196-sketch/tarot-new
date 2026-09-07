# Sensual Tarot — bộ 78 lá

Thư mục này là bộ đầu ra riêng cho yêu cầu tạo bộ Tarot 78 lá hoàn chỉnh.

## Nguồn tham chiếu đã dùng

- `../17-the-star.png`: neo phong cách hình nhân vật, ánh sáng fine-art, chiều sâu không khí và chuẩn trình bày.
- `../the moon.png`: mẫu thứ hai để đối chiếu bố cục dọc, độ tương phản cảnh và cách đặt tên.
- `../card-blank.png`: khung giấy da và hoa văn viền vàng Gothic dùng làm lớp khung chung cho mọi lá.
- `../00-MASTER-PROMPT.md`: quy chuẩn cửa sổ hình, lớp chiều sâu, khung và tên lá.
- `../02-CHARACTER-SPECS.md`: tuổi, tóc, mắt, da, vóc dáng, nét riêng và aura của các nhân vật.
- `../cards.json`: danh sách 78 lá, cảnh và COUNT LOCK của từng lá.

## Cấu trúc

- `cards/*.jpg`: ảnh thành phẩm 78 lá, 784 × 1360 px, cùng tỉ lệ dọc 7:12.
- `manifest.json`: manifest nguyên bản của 78 lá lấy từ `cards.json`.
- `compose_deck.py`: script ghép art vào `card-blank.png`, sau đó đặt badge và ribbon tiêu đề đồng bộ.
- `_art/`: art trung gian chưa ghép (sẽ được dọn sau khi bộ hoàn thiện).
- `_cache/`: lớp khung/ribbon trung gian của script.

## Quy chuẩn ghép

Art trung tâm được tạo không có chữ/khung, mở tràn theo cửa sổ trong. Script giữ lớp hoa văn của `card-blank.png` ở phía trước, sau đó đặt một badge oval và ribbon giấy da viền vàng. Chữ dùng serif cổ điển màu vàng nâu, cùng hệ màu và họa tiết với hai lá mẫu. Mỗi prompt vẫn giữ COUNT LOCK trong `cards.json`; các lá vật thể không có nhân vật được xử lý riêng.

## Kiểm tra nhanh

Sau khi đủ ảnh, chạy:

```bash
python compose_deck.py
identify cards/*.jpg
```

Lệnh ghép có thể chạy lại an toàn cho từng slug hoặc toàn bộ bộ bài.
