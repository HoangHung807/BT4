# Báo cáo nộp bài — TechReview (GEO)

## 1. Nghiên cứu từ khóa và FAQ

- Mục tiêu: Xây dựng website mẫu `TechReview` tối ưu theo chuẩn GEO nhằm giúp AI Search (Google AI/Gemini, Copilot/Bing, Perplexity) hiểu và trích xuất nội dung.
- Đối tượng: Người tìm mua điện thoại, sinh viên, game thủ, người quan tâm camera/pin.

- Bộ từ khóa: xem `data/keyword-research.csv` (20 từ khóa).
- FAQ: 20 câu hỏi chi tiết, file `data/faq-questions.csv`.

- Search Intent: Các từ khóa chia thành Informational, Commercial Investigation, Transactional, Navigational. (Xem file CSV).

> Phần này đáp ứng Yêu cầu I (Nghiên cứu từ khóa & FAQ).

## 2. Xây dựng nội dung

- Cấu trúc website: `index.html`, `article.html`, `faq.html`.
- Bài viết chính: `article.html` với H1, H2, H3, trả lời nhanh, bullet, bảng so sánh, FAQ, nguồn tham khảo, tác giả, ngày cập nhật.

> Phần này đáp ứng Yêu cầu II (Nội dung website).

## 3. Schema Markup

- Đã thêm JSON-LD cho `Organization` (index.html), `Article` (article.html), và `FAQPage` (faq.html). Các schema mô tả entity và liên kết thông qua `publisher`/`author`.

> Phần này đáp ứng Yêu cầu III (Schema Markup).

## 4. Tối ưu tốc độ và đa thiết bị

- HTML semantic, CSS gọn trong `css/style.css`, JS tối thiểu `js/main.js`.
- Hướng dẫn tối ưu: dùng WebP/AVIF, lazy loading, alt text, canonical, meta description, robots.xml và sitemap.xml.
- Core Web Vitals: tối ưu LCP (tải CSS nội tuyến quan trọng, nén ảnh), INP (giảm JS blocking), CLS (kích thước ảnh/placeholder).

> Phần này đáp ứng Yêu cầu IV (Tối ưu website).

## 5. Kiểm tra AI Search

- Kế hoạch kiểm thử và tập truy vấn mẫu có trong `data/ai-queries.csv`.
- Nếu bạn muốn tôi thực hiện kiểm thử thực tế, cần quyền truy cập internet; hiện tại tôi đã chuẩn bị bộ hỏi và hướng dẫn kiểm thử.

> Phần này đáp ứng Yêu cầu V (Kiểm tra AI Search — kế hoạch).

## Kết luận ngắn

Website mẫu đã triển khai: nội dung, schema, tập từ khóa và FAQ, sitemap/robots, README, và báo cáo. Một số kiểm thử AI Search cần thực hiện bên ngoài môi trường local và được đánh dấu "chưa kiểm thử".

---

Checklist:

[ ] Yêu cầu 1 hoàn thành
[ ] Yêu cầu 2 hoàn thành
[ ] Yêu cầu 3 hoàn thành
[ ] Yêu cầu 4 hoàn thành
[ ] Yêu cầu 5 hoàn thành
