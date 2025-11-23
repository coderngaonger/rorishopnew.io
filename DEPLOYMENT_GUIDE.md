# 🚀 HƯỚNG DẪN DEPLOY CHATBOT RÔ RI SHOP

## 📋 CHECKLIST CHUẨN BỊ

- [ ] Tài khoản GitHub
- [ ] Tài khoản Render.com (miễn phí)
- [ ] Git installed trên máy tính
- [ ] Python 3.9+ (để test local)

## 🔥 BƯỚC 1: TEST LOCAL (Tùy chọn)

```bash
# Clone hoặc download project
cd rorishop-chatbot/

# Chạy backend local
./run_local.sh

# Mở browser test tại:
# http://localhost:5000 - API
# test_chatbot.html - Test chatbot UI
```

## 🌐 BƯỚC 2: DEPLOY BACKEND (API)

### 2.1 Upload lên GitHub

```bash
# Tạo repository mới trên GitHub: rorishop-chatbot

# Upload code
git init
git add .
git commit -m "Initial chatbot setup"
git remote add origin https://github.com/YOURUSERNAME/rorishop-chatbot.git
git branch -M main
git push -u origin main
```

### 2.2 Deploy trên Render

1. **Đăng ký/đăng nhập tại [render.com](https://render.com)**

2. **Tạo Web Service:**
   - Click "New" → "Web Service"
   - Connect GitHub repository: `rorishop-chatbot`
   - Cấu hình:
     - **Name**: `rorishop-chatbot-api`
     - **Region**: Singapore (gần VN nhất)
     - **Branch**: `main`
     - **Root Directory**: `backend`
     - **Environment**: `Python 3`
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `gunicorn app:app`

3. **Deploy:**
   - Click "Create Web Service"
   - Chờ 3-5 phút để deploy
   - ✅ Success: Bạn sẽ có URL như `https://rorishop-chatbot-api.onrender.com`

### 2.3 Test API

```bash
# Test health check
curl https://rorishop-chatbot-api.onrender.com/health

# Test chat
curl -X POST https://rorishop-chatbot-api.onrender.com/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "xin chào"}'
```

## 🌟 BƯỚC 3: DEPLOY FRONTEND (Website)

### 3.1 Cập nhật API URL

Sửa file `frontend/index.html` dòng ~1180:

```javascript
// THAY ĐỔI URL NÀY
const CHATBOT_API_URL = 'https://rorishop-chatbot-api.onrender.com';
```

### 3.2 Commit thay đổi

```bash
git add frontend/index.html
git commit -m "Update API URL for production"
git push origin main
```

### 3.3 Deploy Frontend

**Option A: GitHub Pages (Miễn phí)**

1. Vào GitHub repository settings
2. Scroll xuống "Pages"
3. Source: "Deploy from a branch"
4. Branch: `main`
5. Folder: `/frontend`
6. Save
7. ✅ Website sẽ available tại: `https://YOURUSERNAME.github.io/rorishop-chatbot/`

**Option B: Netlify (Miễn phí)**

1. Vào [netlify.com](https://netlify.com)
2. "Add new site" → "Import from Git"
3. Connect GitHub repository
4. Publish directory: `frontend`
5. Deploy

**Option C: Vercel (Miễn phí)**

1. Vào [vercel.com](https://vercel.com)
2. "Import Project"
3. Connect GitHub repository  
4. Root Directory: `frontend`
5. Deploy

## ✅ BƯỚC 4: KIỂM TRA & TEST

### 4.1 Test Backend

- API Health: `https://your-api-url.onrender.com/health`
- Chat Test: Sử dụng `test_chatbot.html`

### 4.2 Test Frontend

- Mở website deployed
- Click vào chatbot widget
- Test các tin nhắn:
  - "xin chào"
  - "có sản phẩm gì"
  - "giá bao nhiều"
  - "giao hàng thế nào"

### 4.3 Debugging

**Nếu chatbot không hoạt động:**

1. **Check console browser (F12):**
   - Có lỗi CORS?
   - Có lỗi 404, 500?
   - API URL đúng chưa?

2. **Check API logs trên Render:**
   - Vào Render dashboard
   - Click vào service
   - Xem "Logs" tab

3. **Common Issues:**
   - ❌ API URL sai → Sửa trong frontend/index.html
   - ❌ CORS error → API should handle CORS automatically
   - ❌ 500 error → Check Python code, dependencies

## 🎯 BƯỚC 5: CUSTOMIZE

### 5.1 Sửa Thông Tin Shop

Edit `backend/app.py`:

```python
shop_info = {
    "name": "Your Shop Name",
    "hotline": "Your Phone",
    "email": "your@email.com",
    # ...
}
```

### 5.2 Thêm/Sửa Sản Phẩm

```python
products = [
    {
        "id": 7,
        "name": "New Product",
        "category": "Category",
        "price": 100000,
        "description": "Description",
        "tags": ["tag1", "tag2"]
    }
    # ...
]
```

### 5.3 Deploy Lại

```bash
git add .
git commit -m "Update shop info and products"
git push origin main
```

Render sẽ tự động redeploy!

## 🔧 TROUBLESHOOTING

### Backend Issues

| Problem | Solution |
|---------|----------|
| 500 Error | Check Python code, dependencies |
| Timeout | Render free tier sleeps after 15min idle |
| Build Failed | Check requirements.txt, Python version |

### Frontend Issues

| Problem | Solution |
|---------|----------|
| Chatbot not working | Check API URL in index.html |
| CORS Error | Should be handled by Flask-CORS |
| 404 Error | Check API endpoint paths |

### Performance Issues

| Problem | Solution |
|---------|----------|
| Slow first response | Render free tier cold start (~30s) |
| Chat timeout | Check network, API status |

## 📱 URLs CUỐI CÙNG

Sau khi deploy thành công:

- **🔗 Website**: `https://YOURUSERNAME.github.io/rorishop-chatbot/`
- **🔗 API**: `https://rorishop-chatbot-api.onrender.com`
- **🔗 Test Page**: `https://YOURUSERNAME.github.io/rorishop-chatbot/test_chatbot.html`

## 🎉 HOÀN THÀNH!

Chatbot của bạn đã sẵn sàng hoạt động 24/7!

### Next Steps:
- Monitor performance trên Render dashboard
- Thêm Google Analytics cho website
- Customize responses theo business
- Consider paid plan cho performance tốt hơn

### Support:
- GitHub Issues cho technical problems
- Render documentation cho deployment issues
- Stack Overflow cho coding questions

Happy coding! 🚀🤖
