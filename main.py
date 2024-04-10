# app.py
from flask import Flask, request,jsonify
from apiServer.user_api import user_blueprint
from apiServer.message_api import message_blueprint
from apiServer.session_api import session_blueprint
from apiServer.role_api import role_blueprint
from apiServer.information_api import information_blueprint
from apiServer.chat_emloyee_api import chat_blueprint
from apiServer.data_score_api import data_score_blueprint
from apiServer.faculty_api import faculty_blueprint

from flask_cors import CORS
# from apiServer.gpt_api import callGpt

#Tạo token 
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

from datetime import timedelta


app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'Welcome to backend botchat2024 Lê Văn Chiến!'

# @app.route('/gpt', methods=['POST'])
# def callgpt():
#     data = request.json
#     gpt = callGpt(data)
#     if gpt:
       
#         return jsonify(gpt), 200
#     else:
#         return jsonify({"error": "Failed to Gpt"}), 500

# Khai báo key bí mật cho việc tạo token
app.config['JWT_SECRET_KEY'] = 'your_secret_key'
# Cấu hình thời gian sống của token
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=1)  # Token truy cập hết hạn sau 30 ngày
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(days=1) # Token làm mới hết hạn sau 60 ngày

# Khởi tạo JWTManager với ứng dụng Flask của bạn
jwt = JWTManager(app)

# Đăng ký các blueprint
app.register_blueprint(user_blueprint)
app.register_blueprint(message_blueprint)
app.register_blueprint(session_blueprint)
app.register_blueprint(role_blueprint)
app.register_blueprint(information_blueprint)
app.register_blueprint(chat_blueprint)
app.register_blueprint(data_score_blueprint)
app.register_blueprint(faculty_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
    
