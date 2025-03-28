1.Các tối ưu quan trọng
✅ Tải nhiều file cùng lúc:

Dùng asyncio.gather() để tải CONCURRENT_DOWNLOADS file song song.

Giảm thời gian chờ từng file tải xong trước khi bắt đầu file tiếp theo.

✅ Chỉ tải file chưa có:

Kiểm tra os.path.exists(file_path), nếu file đã tồn tại thì bỏ qua.

✅ Tăng số lượng tin nhắn xử lý mỗi lần:

BATCH_SIZE = 50 giúp Telethon lấy tin nhắn nhanh hơn.

✅ Hạn chế spam API của Telegram:

Không tải toàn bộ file ngay lập tức, mà xử lý theo nhóm (CONCURRENT_DOWNLOADS).

2. Điều chỉnh tốc độ tải theo mạng
Nếu mạng yếu, giảm CONCURRENT_DOWNLOADS = 2-3.

Nếu mạng khỏe, tăng lên CONCURRENT_DOWNLOADS = 10-15.
