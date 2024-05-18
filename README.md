# backendchatbot
Kích hoạt môi trường ảo bằng cách sử dụng lệnh sau:
Trên Windows:
Copy code
myenv\Scripts\activate




# Chatbot 2024 Project

## Giới thiệu
Project này bao gồm một chatbot sử dụng cơ sở dữ liệu MySQL để lưu trữ và xử lý dữ liệu.

## Cài đặt
Để chạy project này, bạn cần cài đặt MySQL và Python trên máy tính của bạn.

### Cài đặt Python và Thư viện
1. Tải và cài đặt Python từ trang chủ Python.
2. Cài đặt tất cả các thư viện cần thiết bằng cách chạy lệnh sau trong terminal hoặc command prompt:
```bash
   pip install -r requirements.txt
 ```

### Cài đặt MySQL
1. Tải và cài đặt MySQL từ trang chủ MySQL.
2. Tạo một cơ sở dữ liệu mới tên là `chatbot2024`.

## Chạy File model.py
File `model.py` sẽ kết nối với cơ sở dữ liệu MySQL và tạo các bảng cần thiết từ file SQL dump.

1. Đảm bảo rằng bạn đã tạo cơ sở dữ liệu `chatbot2024` trong MySQL.
2. Chạy file `model.py` bằng cách sử dụng lệnh sau:
```python   
python model.py
```

## Chạy Project bằng main.py
Sau khi đã chạy `model.py`, bạn có thể khởi chạy chatbot bằng cách sử dụng `main.py`.

1. Mở terminal hoặc command prompt.
2. Chạy lệnh sau:
```python   
python main.py
```
3. Lưu địa chỉ localhost 

## Lưu ý
Để chạy đầy đủ dự án bạn cần cài đặt các phần sau.
1. [FrontEnd (Next.js)](https://github.com/VanChien411/Academic-chatbot-of-Open-University.git)

2. BackEnd (Python)
    - [backendchatbot](https://github.com/VanChien411/backendchatbot.git)   <img src="image.png" alt="alt text" width="10" height="10">
    - [server-connect-apiModel](https://github.com/VanChien411/server-connect-apiModel.git)
    - [server-websocket](https://github.com/VanChien411/server-websocket.git)

3. Bạn có thể trải nghiệm trực tiếp qua
    - [Chatbot OU website](https://academic-chatbot-of-open-university.vercel.app/)
 
## Hỗ trợ
Nếu bạn gặp vấn đề trong quá trình cài đặt hoặc chạy project, hãy liên hệ với chúng tôi qua email phuthienchien3@gmail.com
hoặc zalo
0328089720

Chúc bạn thành công!
