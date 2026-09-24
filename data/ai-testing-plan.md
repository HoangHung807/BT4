# Kế hoạch kiểm thử AI Search

Mục tiêu: Kiểm tra mức độ trích dẫn và hiển thị của nội dung website trên các công cụ AI Search: Google AI/Gemini, Microsoft Copilot/Bing, Perplexity.

Chuẩn bị:
- Đảm bảo website có thể truy cập public (hoặc dùng ngrok / deploy tạm thời) và sitemap đã submit.
- Kiểm tra Schema bằng Rich Results Test.

Thực hiện kiểm thử:
1. Dùng danh sách 20 truy vấn trong `data/ai-queries.csv`.
2. Với mỗi truy vấn, ghi nhận:
   - Kết quả trả về của AI có trích dẫn website hay không.
   - Nếu có, lưu trích dẫn (URL) và snippet trích.
3. Tổng hợp: tính Citation Rate = (số truy vấn có trích dẫn / tổng số truy vấn) * 100%.

Ghi chú: Nếu không thể truy cập AI search từ môi trường này, hãy thực hiện thủ công theo hướng dẫn trong README và ghi lại kết quả.
