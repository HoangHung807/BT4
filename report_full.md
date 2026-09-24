# Báo cáo hoàn chỉnh — TechReview (GEO)

## Tóm tắt dự án
Xây dựng website mẫu `TechReview` tối ưu theo chuẩn GEO (Generative Engine Optimization) tập trung vào "Điện thoại và tư vấn công nghệ". Mục tiêu: tạo nội dung, schema, và kế hoạch kiểm thử để nội dung dễ được AI Search hiểu và trích xuất.

## 1. Nghiên cứu từ khóa và FAQ

- Mục tiêu: xác định từ khóa có ý định tìm kiếm rõ ràng để hướng nội dung và FAQ.
- Đối tượng: người muốn mua điện thoại, sinh viên, game thủ, người quan tâm camera/pin.
- Danh sách từ khóa: `data/keyword-research.csv` (20 từ khóa với Search Intent và trang mục tiêu).
- FAQ: `data/faq-questions.csv` (20 câu, mỗi câu 50–100 từ).

Phần này đáp ứng Yêu cầu I: Nghiên cứu từ khóa và FAQ.

## 2. Xây dựng nội dung

- Trang chủ: `index.html` chứa giới thiệu, nhóm nội dung, bài nổi bật, FAQ ngắn.
- Bài viết chính: `article.html` với cấu trúc H1/H2/H3, trả lời nhanh, bảng so sánh, bullet points, FAQ, tác giả, ngày cập nhật, nguồn tham khảo.
- Trang FAQ đầy đủ: `faq.html` với 20 câu hỏi.

Nguyên tắc viết cho GEO:
- Trả lời trực tiếp, ngắn gọn ở đầu bài.
- Dùng heading, bullet, table để cấu trúc nội dung dễ trích xuất.
- Thêm metadata và JSON-LD cho mỗi trang.

Phần này đáp ứng Yêu cầu II: Xây dựng nội dung website.

## 3. Schema Markup

- `Organization` ở `index.html`.
- `Article` ở `article.html`.
- `FAQPage` ở `faq.html`.
- (Khuyến nghị) thêm `BreadcrumbList` và `WebSite` khi mở rộng.

Toàn bộ JSON-LD hiện có trong các file HTML tương ứng. (Xem `index.html`, `article.html`, `faq.html`).

Phần này đáp ứng Yêu cầu III: Schema Markup.

## 4. Tối ưu tốc độ và đa thiết bị

- Thiết kế mobile-first, CSS gọn (`css/style.css`), JS tối thiểu (`js/main.js`).
- Hình ảnh: dùng WebP/AVIF, kích thước phù hợp, lazy loading (nếu có ảnh lớn). Alt text phải có.
- HTML semantic, canonical, meta description, robots.txt, sitemap.xml đã có.
- Core Web Vitals: hướng dẫn tối ưu LCP/INP/CLS có trong README và phần tư vấn trong `report.md`.

Phần này đáp ứng Yêu cầu IV: Tối ưu website.

## 5. Kiểm tra AI Search

- Kế hoạch và danh sách câu truy vấn: `data/ai-queries.csv` và `data/ai-testing-plan.md`.
- Ghi chú: việc kiểm thử thực tế (thu thập trích dẫn từ Google AI/Gemini, Copilot/Bing, Perplexity) cần trang public hoặc truy cập Internet. Nếu chưa thực hiện, ghi "Chưa kiểm thử".

Phần này đáp ứng Yêu cầu V: Kiểm tra AI Search (kế hoạch và truy vấn).

## Nguồn tham khảo

- Google Search Central: https://developers.google.com/search
- Schema.org: https://schema.org
- Trang chính thức nhà sản xuất: (Apple, Samsung, Xiaomi official sites)

## Hạn chế & Ghi chú

- Nội dung đã viết không bao gồm dữ liệu benchmark thực nghiệm cụ thể cho từng model (không tạo số liệu giả). Các kết luận dựa trên nguyên tắc kỹ thuật và nguồn công khai.
- Kiểm thử AI Search chưa được thực hiện trong môi trường nếu hosting chưa public — báo cáo đánh dấu các bước cần làm thủ công.

## Kết luận

Đã hoàn thành: nội dung, schema, từ khóa, FAQ, sitemap, robots, README, và kế hoạch kiểm thử. Bước tiếp theo: deploy site public và thực hiện kiểm thử AI Search; thu thập citation rate và tối ưu theo kết quả.

---

Checklist:

[x] Yêu cầu 1 hoàn thành
[x] Yêu cầu 2 hoàn thành
[x] Yêu cầu 3 hoàn thành
[x] Yêu cầu 4 hoàn thành
[ ] Yêu cầu 5 hoàn thành (chưa kiểm thử thực tế — hướng dẫn đã sẵn sàng)
