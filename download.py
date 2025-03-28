from telethon.sync import TelegramClient
import os
from datetime import datetime
import asyncio

# Thông tin tài khoản Telegram
api_id = 123456  # Thay bằng API ID của bạn
api_hash = "abcdabcd1234abcd"  # Thay bằng API Hash của bạn
phone_number = "+84912345678"  # Số điện thoại của bạn (bao gồm mã quốc gia)
group_id  = -12345678  # ID hoặc @username của group

# Thư mục lưu file
download_dir = "Download_Files"
os.makedirs(download_dir, exist_ok=True)

# Kết nối Telegram
client = TelegramClient("session_name", api_id, api_hash)

# Tăng số lượng tin nhắn tải mỗi lần
BATCH_SIZE = 50  # Tăng từ mặc định (10) lên 50 tin nhắn mỗi lần
CONCURRENT_DOWNLOADS = 5  # Số file tải cùng lúc (tăng nếu mạng mạnh)

async def download_file(message):
    """Hàm tải file riêng biệt"""
    if message.file:
        month_folder = os.path.join(download_dir, message.date.strftime("%Y-%m"))
        os.makedirs(month_folder, exist_ok=True)

        file_path = os.path.join(month_folder, message.file.name or f"file_{message.id}")
        if os.path.exists(file_path):
            print(f"Đã có: {file_path}, bỏ qua.")
            return
        
        print(f"Đang tải: {file_path}")
        await client.download_media(message, file=file_path)
        print(f"Đã tải: {file_path}")

async def main():
    await client.start(phone_number)
    
    messages = client.iter_messages(group_id, limit=None)  # Duyệt toàn bộ tin nhắn
    tasks = []  # Danh sách task tải file

    async for message in messages:
        if message.file:
            tasks.append(download_file(message))
            if len(tasks) >= CONCURRENT_DOWNLOADS:  # Đủ số luồng chạy song song
                await asyncio.gather(*tasks)
                tasks = []  # Reset danh sách task

    if tasks:  # Xử lý nốt file còn lại
        await asyncio.gather(*tasks)

with client:
    client.loop.run_until_complete(main())
