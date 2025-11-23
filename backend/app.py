from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import random
import re
from datetime import datetime
import os

app = Flask(__name__)
CORS(app)  # Cho phép frontend gọi API

class RoRiChatbot:
    def __init__(self):
        self.load_data()
        self.conversation_history = []
    
    def load_data(self):
        """Load dữ liệu shop và sản phẩm"""
        self.shop_info = {
            "name": "Rô Ri Shop",
            "slogan": "In điều bạn muốn - Tặng điều bạn thương",
            "hotline": "0905 298 298",
            "email": "contact@rorishop.com",
            "facebook": "rorishop.official",
            "working_hours": "8:00 - 20:00 hàng ngày",
            "shipping": "Giao hàng toàn quốc 3-5 ngày",
            "free_shipping": "Miễn phí ship cho đơn từ 500k"
        }
        
        self.products = {
            "ly_su": {
                "name": "Ly Sứ In Hình Theo Yêu Cầu",
                "price": 120000,
                "description": "Ly sứ cao cấp, in hình sắc nét, bền màu",
                "category": "Ly & Cốc"
            },
            "binh_giu_nhiet": {
                "name": "Bình Giữ Nhiệt In Logo Công Ty", 
                "price": 250000,
                "description": "Bình giữ nhiệt inox 304, giữ nhiệt 12h",
                "category": "Bình Giữ Nhiệt"
            },
            "ao_thun": {
                "name": "Áo Thun In Hình Theo Thiết Kế",
                "price": 180000,
                "description": "Áo thun cotton 100%, in chuyển nhiệt cao cấp",
                "category": "Áo Thun"
            },
            "box_qua_tang": {
                "name": "Box Quà Tặng 20/11",
                "price": 299000,
                "description": "Set quà tặng đầy đủ, thiết kế theo yêu cầu",
                "category": "Set Quà Tặng"
            },
            "moc_khoa": {
                "name": "Móc Khóa In Hình Theo Yêu Cầu",
                "price": 30000,
                "description": "Móc khóa acrylic, in UV sắc nét",
                "category": "Móc Khóa"
            },
            "tui_tote": {
                "name": "Túi Tote In Hình/Logo",
                "price": 89000,
                "description": "Túi tote canvas bền đẹp, in silk cao cấp",
                "category": "Túi Tote"
            }
        }
        
        # Keywords để nhận diện ý định
        self.intent_keywords = {
            "greeting": ["xin chào", "hello", "chào", "hi", "hey"],
            "products": ["sản phẩm", "có gì", "bán gì", "items", "danh mục", "catalog"],
            "price": ["giá", "bao nhiều", "cost", "price", "tiền", "phí"],
            "shipping": ["giao hàng", "ship", "delivery", "nhận hàng", "vận chuyển"],
            "contact": ["liên hệ", "contact", "hotline", "phone", "gọi"],
            "order": ["đặt hàng", "order", "mua", "buy", "thanh toán"],
            "design": ["thiết kế", "design", "file", "in ấn", "tùy chỉnh"],
            "thanks": ["cảm ơn", "thank", "thanks", "cám ơn"],
            "bye": ["tạm biệt", "bye", "goodbye", "see you", "chào tạm biệt"]
        }

    def detect_intent(self, message):
        """Phát hiện ý định từ tin nhắn"""
        message_lower = message.lower()
        
        # Kiểm tra từng intent
        for intent, keywords in self.intent_keywords.items():
            for keyword in keywords:
                if keyword in message_lower:
                    return intent
        
        return "general"

    def format_price(self, price):
        """Format giá tiền"""
        return f"{price:,.0f}đ".replace(",", ".")

    def get_response(self, message, user_session=None):
        """Tạo phản hồi cho tin nhắn"""
        intent = self.detect_intent(message)
        
        responses = {
            "greeting": [
                "Xin chào! Tôi là RIO BOT, trợ lý của Rô Ri Shop! 😊 Tôi có thể giúp bạn tìm hiểu về sản phẩm, giá cả và dịch vụ của chúng tôi.",
                "Chào bạn! Chào mừng đến với Rô Ri Shop - nơi in điều bạn muốn, tặng điều bạn thương! 🎁 Tôi có thể hỗ trợ gì cho bạn?",
                "Hello! Tôi là RIO BOT của Rô Ri Shop! ✨ Bạn muốn tìm hiểu về sản phẩm nào không?"
            ],
            
            "products": [
                f"Rô Ri Shop chuyên về:\n📦 {', '.join([p['category'] for p in self.products.values()])}\n\nTất cả đều có thể in theo yêu cầu của bạn! Bạn muốn xem sản phẩm nào cụ thể?",
                "Chúng tôi có đầy đủ sản phẩm quà tặng cá nhân hóa:\n" + "\n".join([f"• {p['name']}" for p in self.products.values()]) + "\n\nBạn quan tâm sản phẩm nào nhất? 🎨"
            ],
            
            "price": [
                "Bảng giá sản phẩm Rô Ri Shop:\n" + "\n".join([f"• {p['name']}: {self.format_price(p['price'])}" for p in self.products.values()]) + f"\n\n💰 {self.shop_info['free_shipping']}!",
                f"Giá sản phẩm rất cạnh tranh! Ví dụ ly sứ chỉ {self.format_price(120000)}, áo thun {self.format_price(180000)}... \n\n📞 Gọi {self.shop_info['hotline']} để được tư vấn giá tốt nhất!"
            ],
            
            "shipping": [
                f"🚚 {self.shop_info['shipping']}\n💝 {self.shop_info['free_shipping']}\n📦 COD hoặc chuyển khoản đều được!\n\nBạn ở khu vực nào để tôi tư vấn thời gian giao hàng cụ thể?",
                f"Chúng tôi giao hàng toàn quốc! {self.shop_info['shipping']} và {self.shop_info['free_shipping']} nhé! 🎯"
            ],
            
            "contact": [
                f"📞 Hotline: {self.shop_info['hotline']}\n📧 Email: {self.shop_info['email']}\n📘 Facebook: {self.shop_info['facebook']}\n⏰ {self.shop_info['working_hours']}\n\nBạn có thể liên hệ bất cứ lúc nào! 😊",
                f"Liên hệ ngay với Rô Ri Shop:\n🔥 Hotline: {self.shop_info['hotline']} (zalo/call)\n💬 Messenger: facebook.com/{self.shop_info['facebook']}"
            ],
            
            "order": [
                "Để đặt hàng bạn có thể:\n1. 🛒 Thêm sản phẩm vào giỏ hàng trên website\n2. 📞 Gọi hotline 0905 298 298\n3. 💬 Nhắn tin qua Facebook\n\nBạn muốn đặt sản phẩm nào?",
                "Quy trình đặt hàng đơn giản:\n• Chọn sản phẩm\n• Gửi file thiết kế (nếu có)\n• Xác nhận đơn hàng\n• Thanh toán\n• Nhận hàng\n\nTôi có thể hỗ trợ bạn từng bước! 🎯"
            ],
            
            "design": [
                "Về thiết kế, Rô Ri Shop hỗ trợ:\n🎨 Thiết kế miễn phí theo yêu cầu\n📁 Nhận file có sẵn (AI, PSD, PNG, JPG)\n👀 In thử mẫu demo để xem trước\n✨ Tư vấn ý tưởng sáng tạo\n\nBạn đã có ý tưởng thiết kế chưa?",
                "Chúng tôi có team design chuyên nghiệp! Bạn có thể:\n• Gửi ý tưởng, chúng tôi thiết kế\n• Gửi file có sẵn để in\n• Tham khảo mẫu có sẵn\n\nFile thiết kế nào cũng ok! 🎭"
            ],
            
            "thanks": [
                "Không có gì! Rô Ri Shop luôn sẵn sàng hỗ trợ bạn! 😊 Còn gì cần tư vấn thêm không?",
                "Cảm ơn bạn đã tin tưởng Rô Ri Shop! 🙏 Hãy liên hệ bất cứ khi nào bạn cần nhé!"
            ],
            
            "bye": [
                "Tạm biệt bạn! Hẹn gặp lại sớm tại Rô Ri Shop! 👋 Đừng quên follow Facebook để cập nhật ưu đãi mới nhé!",
                "Bye bye! Cảm ơn bạn đã ghé thăm! 🌟 Liên hệ 0905 298 298 khi cần hỗ trợ nhé!"
            ],
            
            "general": [
                f"Tôi hiểu bạn đang quan tâm về {self.shop_info['name']}! 🎁 Bạn có thể hỏi tôi về:\n📦 Sản phẩm\n💰 Giá cả\n🚚 Giao hàng\n🎨 Thiết kế\n📞 Liên hệ\n\nBạn muốn biết gì nhất?",
                f"Tôi có thể hỗ trợ bạn về tất cả dịch vụ của {self.shop_info['name']}! Hãy hỏi cụ thể về sản phẩm, giá cả, hay quy trình đặt hàng nhé! 😊",
                f"Chào bạn! Tôi là trợ lý ảo của {self.shop_info['name']} - chuyên in quà tặng cá nhân hóa! 🎨 Bạn cần tư vấn gì?"
            ]
        }
        
        # Lưu lịch sử hội thoại
        self.conversation_history.append({
            "user": message,
            "intent": intent,
            "timestamp": datetime.now().isoformat()
        })
        
        return random.choice(responses[intent])

# Khởi tạo chatbot
chatbot = RoRiChatbot()

@app.route('/api/chat', methods=['POST'])
def chat():
    """API endpoint cho chatbot"""
    try:
        data = request.json
        message = data.get('message', '')
        user_session = data.get('session', 'anonymous')
        
        if not message.strip():
            return jsonify({
                'success': False,
                'error': 'Message không được để trống'
            }), 400
        
        # Tạo phản hồi
        response = chatbot.get_response(message, user_session)
        
        return jsonify({
            'success': True,
            'message': response,
            'timestamp': datetime.now().isoformat()
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/products', methods=['GET'])
def get_products():
    """API lấy danh sách sản phẩm"""
    try:
        return jsonify({
            'success': True,
            'products': chatbot.products
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/shop-info', methods=['GET'])
def get_shop_info():
    """API lấy thông tin shop"""
    try:
        return jsonify({
            'success': True,
            'shop_info': chatbot.shop_info
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat()
    })

if __name__ == '__main__':
    # Chạy với debug mode cho development
    app.run(debug=True, host='0.0.0.0', port=5000)
