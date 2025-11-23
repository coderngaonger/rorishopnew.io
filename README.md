# 🎁 Rô Ri Shop - E-commerce Website với AI Chatbot

Website bán hàng hoàn chỉnh cho Rô Ri Shop với chatbot AI tích hợp.

## ✨ Tính năng

### 🛒 Frontend
- **Giao diện responsive** - Tương thích mọi thiết bị
- **Giỏ hàng** - Thêm, xóa, cập nhật sản phẩm
- **Upload file** - Drag & drop file thiết kế
- **Chatbot widget** - Chat realtime với AI
- **Smooth animations** - Hiệu ứng mượt mà

### 🤖 Backend API
- **Chatbot AI thông minh** - Hiểu ngữ cảnh, trả lời tự nhiên
- **RESTful API** - Chuẩn REST API
- **CORS enabled** - Hỗ trợ cross-origin
- **Error handling** - Xử lý lỗi robust
- **Session management** - Quản lý phiên chat

### 🎯 Chatbot Features
- **Intent Recognition** - Nhận diện ý định người dùng
- **Product Info** - Tư vấn sản phẩm, giá cả
- **Smart Responses** - Phản hồi thông minh theo ngữ cảnh
- **Conversation History** - Lưu lịch sử chat
- **Quick Actions** - Nút tác vụ nhanh

## 🚀 Cài đặt & Chạy

### 📋 Yêu cầu
- Python 3.8+
- Flask
- Modern web browser

### 🔧 Backend Setup

1. **Cài đặt dependencies:**
```bash
cd backend
pip install -r requirements.txt
```

2. **Chạy server:**
```bash
python app.py
```
Server sẽ chạy tại: `http://localhost:5000`

### 🌐 Frontend Setup

1. **Mở file HTML:**
```bash
cd frontend
# Mở index.html bằng web server hoặc live server
# Hoặc double-click vào index.html
```

2. **Hoặc sử dụng Python HTTP Server:**
```bash
cd frontend
python -m http.server 8080
```
Frontend sẽ chạy tại: `http://localhost:8080`

## 📁 Cấu trúc dự án

```
WEBRORI/
├── backend/
│   ├── app.py              # Flask API server
│   ├── requirements.txt    # Python dependencies
│   └── README.md
├── frontend/
│   ├── index.html         # Website chính
│   └── README.md
└── README.md              # File này
```

## 🔌 API Endpoints

### Chat API
```
POST /api/chat
Content-Type: application/json

{
  "message": "Có những sản phẩm nào?",
  "session": "user_123"
}

Response:
{
  "success": true,
  "message": "Rô Ri Shop chuyên về ly sứ, bình giữ nhiệt...",
  "timestamp": "2024-01-01T00:00:00"
}
```

### Products API
```
GET /api/products

Response:
{
  "success": true,
  "products": {
    "ly_su": {
      "name": "Ly Sứ In Hình Theo Yêu Cầu",
      "price": 120000,
      "category": "Ly & Cốc"
    }
  }
}
```

### Health Check
```
GET /health

Response:
{
  "status": "healthy",
  "timestamp": "2024-01-01T00:00:00"
}
```

## 🧠 Chatbot Intent Recognition

Chatbot có thể nhận diện các ý định:

- **greeting**: Chào hỏi
- **products**: Hỏi về sản phẩm
- **price**: Hỏi về giá cả
- **shipping**: Hỏi về giao hàng
- **contact**: Thông tin liên hệ
- **order**: Quy trình đặt hàng
- **design**: Thiết kế sản phẩm
- **thanks**: Cảm ơn
- **bye**: Tạm biệt

## 🎨 Customization

### Thay đổi sản phẩm
Sửa file `backend/app.py` trong class `RoRiChatbot.__init__()`:

```python
self.products = {
    "san_pham_moi": {
        "name": "Tên sản phẩm",
        "price": 100000,
        "description": "Mô tả sản phẩm",
        "category": "Danh mục"
    }
}
```

### Thay đổi phản hồi chatbot
Sửa `responses` dictionary trong `get_response()` method:

```python
responses = {
    "greeting": [
        "Phản hồi chào hỏi mới...",
    ]
}
```

## 🚀 Deploy lên Production

### 1. Heroku Deploy
```bash
# Tạo Procfile
echo "web: gunicorn app:app" > Procfile

# Deploy
git init
heroku create rorishop-api
git add .
git commit -m "Initial commit"
git push heroku main
```

### 2. VPS Deploy
```bash
# Sử dụng gunicorn
pip install gunicorn
gunicorn --bind 0.0.0.0:5000 app:app
```

### 3. Frontend Deploy
- Upload `frontend/index.html` lên hosting (Netlify, Vercel, GitHub Pages)
- Cập nhật `API_BASE_URL` trong file HTML về URL production

## 🔧 Troubleshooting

### Lỗi CORS
Nếu gặp lỗi CORS, kiểm tra:
```python
from flask_cors import CORS
CORS(app)  # Trong app.py
```

### Chatbot không phản hồi
1. Kiểm tra server backend có chạy không
2. Kiểm tra console browser có lỗi không
3. Kiểm tra endpoint `/health`

### Frontend không load sản phẩm
1. Kiểm tra API `/api/products`
2. Kiểm tra console có lỗi network không

## 📞 Liên hệ

- **Hotline**: 0905 298 298
- **Email**: contact@rorishop.com
- **Facebook**: /rorishop.official

## 📝 License

MIT License - Sử dụng tự do cho mục đích thương mại.
