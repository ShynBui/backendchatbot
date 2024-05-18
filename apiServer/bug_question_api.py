from flask import Blueprint, request, jsonify
from data.connect import connect_to_database

bug_question_blueprint = Blueprint('bug_question', __name__)

# Thêm một bản ghi mới vào bảng bug_question
@bug_question_blueprint.route('/bug_questions', methods=['POST'])
def add_bug_question():
    connection = connect_to_database()
    if connection:
        data = request.json
        title = data['title']
        content = data['content']
        view = data.get('view', 0)
        user_id = data['user_id']

        cursor = connection.cursor()
        sql = "INSERT INTO bug_question (title, content, view, create_time, user_id) VALUES (%s, %s, %s, NOW(), %s)"
        values = (title, content, view, user_id)
        cursor.execute(sql, values)
        id_bug_question = cursor.lastrowid  # Lấy ID của bản ghi vừa được thêm
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"message": "Bug question added successfully", "id_bug_question": id_bug_question}), 201
    else:
        return jsonify({"error": "Failed to connect to database"}), 500

# Lấy thông tin tất cả các bản ghi trong bảng bug_question
@bug_question_blueprint.route('/bug_questions', methods=['GET'])
def get_all_bug_questions():
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("""
        SELECT bug_question.*, user.full_name AS user_name
FROM bug_question
INNER JOIN user ON bug_question.user_id = user.user_id
""")
        bug_questions = cursor.fetchall()
        cursor.close()
        connection.close()
        return jsonify(bug_questions), 200
    else:
        return jsonify({"error": "Failed to connect to database"}), 500

# Lấy thông tin của một bản ghi trong bảng bug_question dựa trên id_bug_question
@bug_question_blueprint.route('/bug_questions/<int:id_bug_question>', methods=['GET'])
def get_bug_question(id_bug_question):
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor(dictionary=True)
        sql = """
        SELECT bug_question.*, user.full_name AS user_name
FROM bug_question
INNER JOIN user ON bug_question.user_id = user.user_id
WHERE bug_question.id = %s
"""
        cursor.execute(sql, (id_bug_question,))
        bug_question = cursor.fetchone()
        cursor.close()
        connection.close()
        if bug_question:
            return jsonify(bug_question), 200
        else:
            return jsonify({"error": "Bug question not found"}), 404
    else:
        return jsonify({"error": "Failed to connect to database"}), 500

# Cập nhật thông tin của một bản ghi trong bảng bug_question dựa trên id_bug_question
@bug_question_blueprint.route('/bug_questions/<int:id_bug_question>', methods=['PUT'])
def update_bug_question(id_bug_question):
    connection = connect_to_database()
    if connection:
        data = request.json
        title = data.get('title', None)
        content = data.get('content', None)
        view = data.get('view', None)

        cursor = connection.cursor()
        sql = "UPDATE bug_question SET title=%s, content=%s, view=%s WHERE id=%s"
        values = (title, content, view, id_bug_question)
        cursor.execute(sql, values)
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"message": "Bug question updated successfully"}), 200
    else:
        return jsonify({"error": "Failed to connect to database"}), 500

# Xóa một bản ghi trong bảng bug_question dựa trên id_bug_question
@bug_question_blueprint.route('/bug_questions/<int:id_bug_question>', methods=['DELETE'])
def delete_bug_question(id_bug_question):
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        sql = "DELETE FROM bug_question WHERE id=%s"
        values = (id_bug_question,)
        cursor.execute(sql, values)
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"message": "Bug question deleted successfully"}), 200
    else:
        return jsonify({"error": "Failed to connect to database"}), 500
