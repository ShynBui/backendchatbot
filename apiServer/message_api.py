from flask import Blueprint, request, jsonify
from data.connect import connect_to_database

message_blueprint = Blueprint('messages', __name__)


# Thêm một tin nhắn mới
@message_blueprint.route('/messages', methods=['POST'])
def add_message():
    connection = connect_to_database()
    if connection:
        data = request.json
        session_id = data['session_id']
        question = data['question']
        answer = data['answer']
        question_time = data['question_time']
        answer_time = data['answer_time']
        comment = data.get('comment', '')

        cursor = connection.cursor()
        sql = "INSERT INTO message (session_id, question, answer, question_time, answer_time, comment) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (session_id, question, answer, question_time, answer_time, comment)
        cursor.execute(sql, values)
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"message": "Message added successfully"}), 201
    else:
        return jsonify({"error": "Failed to connect to database"}), 500

# Lấy thông tin tất cả các tin nhắn
@message_blueprint.route('/messages', methods=['GET'])
def get_all_messages():
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM message")
        messages = cursor.fetchall()
        cursor.close()
        connection.close()
        return jsonify(messages), 200
    else:
        return jsonify({"error": "Failed to connect to database"}), 500

@message_blueprint.route('/messages/<int:messages_id>', methods=['GET'])
def get_session(messages_id):
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor(dictionary=True)
        sql = "SELECT * FROM messages WHERE messages_id = %s"
        cursor.execute(sql, (messages_id,))
        messages = cursor.fetchone()
        cursor.close()
        connection.close()
        if messages:
            return jsonify(messages), 200
        else:
            return jsonify({"error": "messages not found"}), 404
    else:
        return jsonify({"error": "Failed to connect to database"}), 500

# Cập nhật thông tin của một tin nhắn
@message_blueprint.route('/messages/<int:qa_id>', methods=['PUT'])
def update_message(qa_id):
    connection = connect_to_database()
    if connection:
        data = request.json
        session_id = data['session_id']
        question = data['question']
        answer = data['answer']
        question_time = data['question_time']
        answer_time = data['answer_time']
        comment = data.get('comment', '')

        cursor = connection.cursor()
        sql = "UPDATE message SET session_id=%s, question=%s, answer=%s, question_time=%s, answer_time=%s, comment=%s WHERE qa_id=%s"
        values = (session_id, question, answer, question_time, answer_time, comment, qa_id)
        cursor.execute(sql, values)
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"message": "Message updated successfully"}), 200
    else:
        return jsonify({"error": "Failed to connect to database"}), 500

# Xóa một tin nhắn
@message_blueprint.route('/messages/<int:qa_id>', methods=['DELETE'])
def delete_message(qa_id):
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        sql = "DELETE FROM message WHERE qa_id=%s"
        values = (qa_id,)
        cursor.execute(sql, values)
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"message": "Message deleted successfully"}), 200
    else:
        return jsonify({"error": "Failed to connect to database"}), 500

