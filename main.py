# app.py
from flask import Flask
from apiServer.user_api import user_blueprint
from apiServer.message_api import message_blueprint
from apiServer.session_api import session_blueprint
from apiServer.role_api import role_blueprint
from apiServer.information_api import information_blueprint
from flask_cors import CORS

#Tạo token 
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity



app = Flask(__name__)
CORS(app)

# Khai báo key bí mật cho việc tạo token
app.config['JWT_SECRET_KEY'] = 'your_secret_key'

# Khởi tạo JWTManager với ứng dụng Flask của bạn
jwt = JWTManager(app)

# Đăng ký các blueprint
app.register_blueprint(user_blueprint)
app.register_blueprint(message_blueprint)
app.register_blueprint(session_blueprint)
app.register_blueprint(role_blueprint)
app.register_blueprint(information_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
