from flask import Blueprint, request, jsonify
from data.connect import connect_to_database

chat_blueprint = Blueprint('chatEmloyee', __name__)

# Thêm một tin nhắn mới
@chat_blueprint.route('/chatEmloyees', methods=['POST'])
def add_message():
    connection = connect_to_database()
    if connection:
        data = request.json
        messenger = data['messenger']
        emloyee = data['emloyee']
        status = data['status']
        datetime = data['datetime']
        user_id = data['user_id']

        cursor = connection.cursor()
        sql = "INSERT INTO chat_with_emloyee (messenger, emloyee, status, datetime, user_id) VALUES (%s, %s, %s, %s, %s)"
        values = (messenger, emloyee, status, datetime, user_id)
        cursor.execute(sql, values)
        message_id = cursor.lastrowid
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"message": "Message added successfully", "message_id": message_id}), 201
    else:
        return jsonify({"error": "Failed to connect to database"}), 500

# Lấy tất cả các tin nhắn
@chat_blueprint.route('/chatEmloyees', methods=['GET'])
def get_all_messages():
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM chat_with_emloyee")
        messages = cursor.fetchall()
        cursor.close()
        connection.close()
        return jsonify(messages), 200
    else:
        return jsonify({"error": "Failed to connect to database"}), 500

# Lấy thông tin của một tin nhắn dựa trên message_id
@chat_blueprint.route('/chatEmloyees/<int:message_id>', methods=['GET'])
def get_message(message_id):
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor(dictionary=True)
        sql = "SELECT * FROM chat_with_emloyee WHERE id = %s"
        cursor.execute(sql, (message_id,))
        message = cursor.fetchone()
        cursor.close()
        connection.close()
        if message:
            return jsonify(message), 200
        else:
            return jsonify({"error": "Message not found"}), 404
    else:
        return jsonify({"error": "Failed to connect to database"}), 500

# Cập nhật thông tin của một tin nhắn dựa trên message_id
@chat_blueprint.route('/chatEmloyees/<int:message_id>', methods=['PUT'])
def update_message(message_id):
    connection = connect_to_database()
    if connection:
        data = request.json
        messenger = data.get('messenger', None)
        emloyee = data.get('emloyee', None)
        status = data.get('status', None)
        datetime = data.get('datetime', None)

        cursor = connection.cursor()
        sql = "UPDATE chat_with_emloyee SET messenger=%s, emloyee=%s, status=%s, datetime=%s WHERE id=%s"
        values = (messenger, emloyee, status, datetime, message_id)
        cursor.execute(sql, values)
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"message": "Message updated successfully"}), 200
    else:
        return jsonify({"error": "Failed to connect to database"}), 500

# Xóa một tin nhắn dựa trên message_id
@chat_blueprint.route('/chatEmloyees/<int:message_id>', methods=['DELETE'])
def delete_message(message_id):
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        sql = "DELETE FROM chat_with_emloyee WHERE id=%s"
        values = (message_id,)
        cursor.execute(sql, values)
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"message": "Message deleted successfully"}), 200
    else:
        return jsonify({"error": "Failed to connect to database"}), 500

# Lấy tất cả các tin nhắn của một user và sắp xếp theo datetime
@chat_blueprint.route('/chatEmloyees/user<int:user_id>', methods=['GET'])
def get_messages_by_user_id(user_id):
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor(dictionary=True)
        sql = "SELECT * FROM chat_with_emloyee WHERE user_id = %s ORDER BY datetime "
        cursor.execute(sql, (user_id,))
        messages = cursor.fetchall()
        cursor.close()
        connection.close()
        return jsonify(messages), 200
    else:
        return jsonify({"error": "Failed to connect to database"}), 500

