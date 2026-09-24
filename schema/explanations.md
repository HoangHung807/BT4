# Giải thích Schema cho TechReview

1. Organization (index.html)
   - Mô tả: thông tin cơ bản về tổ chức/website.
   - Lý do: giúp search engine nhận diện thương hiệu và logo.

2. WebSite (tích hợp trong sitemap/metadata nếu cần)
   - Mô tả: mặt bằng site-level để hỗ trợ sitelinks và tìm kiếm trang.

3. Article (article.html)
   - Mô tả: đánh dấu bài viết chính, giúp AI trích xuất thông tin tác giả, ngày xuất bản, tóm tắt.

4. BreadcrumbList (nên thêm khi có cấu trúc nhiều tầng)
   - Mô tả: giúp hiển thị đường dẫn theo cấu trúc site trong kết quả tìm kiếm.

5. FAQPage (faq.html)
   - Mô tả: đánh dấu câu hỏi và câu trả lời để AI/Google hiểu các Q&A có cấu trúc.

Quan hệ giữa entity:
- `Article` có thuộc `publisher` là `Organization`.
- `FAQPage` chứa `Question`/`Answer` entities.
