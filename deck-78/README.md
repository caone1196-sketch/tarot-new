# 🔮 SENSUAL TAROT — Bộ bài 78 lá (deck-78)

Bộ bài được tạo từ toàn bộ nội dung repo:
`00-MASTER-PROMPT.md` · `01-CARD-TABLE.md` · `02-CHARACTER-SPECS.md` · `cards.json`

## Tham chiếu
| Vai trò | File |
|---|---|
| **Neo phong cách chính (nhân vật + khung + chữ)** | `../the moon.png` |
| Tham chiếu phụ (bố cục / ánh sáng) | `../17-the-star.png` |
| Khung trắng | `../card-blank.png` |

## Chuẩn đồng bộ (áp dụng cho cả 78 lá)
- Khung viền vàng Gothic mỏng + 4 hoa văn góc + đường kẻ vàng kép — copy nguyên từ `the moon.png`
- Kiểu chữ tên lá: blackletter mạ vàng, cùng size/gradient/đổ bóng như chữ "THE MOON"
- Nội dung tràn kín ô trong, không cổng vòm / cột đá
- Hoa văn vàng đè lên mép cảnh → phân lớp chiều sâu
- Tỉ lệ dọc 7:12
- ANATOMY LOCK + COUNT LOCK theo đúng `cards.json`

## Cấu trúc
```
deck-78/
├── index.json      # danh mục 78 lá (slug, title, prompt, ảnh)
├── prompts/        # 78 file prompt .txt sinh từ cards.json
├── cards/          # 78 ảnh lá bài .png
└── viewer.html     # xem toàn bộ bộ bài
```

## Sinh lại prompt
```bash
python3 tools/build_prompts.py
```

> **Lưu ý nội dung:** các nhân vật được thể hiện trong trang phục vải rủ kín đáo
> (fine-art cổ điển) thay vì khỏa thân; mọi yếu tố còn lại của prompt gốc
> (bối cảnh, nhân vật, tuổi, tóc, vóc dáng, count lock) được giữ nguyên.
