from flask import Blueprint, request, jsonify
from data.connect import connect_to_database

bug_comment_blueprint = Blueprint('bug_comment', __name__)

# Thêm một bản ghi mới vào bảng bug_comment
@bug_comment_blueprint.route('/bug_comments', methods=['POST'])
def add_bug_comment():
    connection = connect_to_database()
    if connection:
        data = request.json
        bug_question_id = data['bug_question_id']
        content = data['content']
        user_id = data['user_id']
        user_id_last_comment = data['user_id_last_comment']

        cursor = connection.cursor()
        sql = "INSERT INTO bug_comment (bug_question_id, content, user_id, user_id_last_comment,create_time ) VALUES (%s, %s, %s, %s,NOW())"
        values = (bug_question_id, content, user_id, user_id_last_comment)
        cursor.execute(sql, values)
        id_bug_comment = cursor.lastrowid  # Lấy ID của bản ghi vừa được thêm
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"message": "Bug comment added successfully", "id_bug_comment": id_bug_comment}), 201
    else:
        return jsonify({"error": "Failed to connect to database"}), 500

# Lấy thông tin tất cả các bản ghi trong bảng bug_comment
@bug_comment_blueprint.route('/bug_comments', methods=['GET'])
def get_all_bug_comments():
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("""
    SELECT bug_comment.*,
           user.full_name AS user_name,
           user_last_comment.full_name AS user_name_last_comment
    FROM bug_comment
    INNER JOIN user ON bug_comment.user_id = user.user_id
    INNER JOIN user AS user_last_comment ON bug_comment.user_id_last_comment = user_last_comment.user_id
""")
        bug_comments = cursor.fetchall()
        cursor.close()
        connection.close()
        return jsonify(bug_comments), 200
    else:
        return jsonify({"error": "Failed to connect to database"}), 500

# Lấy thông tin của một bản ghi trong bảng bug_comment dựa trên id_bug_comment
@bug_comment_blueprint.route('/bug_comments/<int:id_bug_comment>', methods=['GET'])
def get_bug_comment(id_bug_comment):
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor(dictionary=True)
        sql = "SELECT * FROM bug_comment WHERE id = %s"
        cursor.execute(sql, (id_bug_comment,))
        bug_comment = cursor.fetchone()
        cursor.close()
        connection.close()
        if bug_comment:
            return jsonify(bug_comment), 200
        else:
            return jsonify({"error": "Bug comment not found"}), 404
    else:
        return jsonify({"error": "Failed to connect to database"}), 500

# Cập nhật thông tin của một bản ghi trong bảng bug_comment dựa trên id_bug_comment
@bug_comment_blueprint.route('/bug_comments/<int:id_bug_comment>', methods=['PUT'])
def update_bug_comment(id_bug_comment):
    connection = connect_to_database()
    if connection:
        data = request.json
        content = data.get('content', None)
        user_id_last_comment = data.get('user_id_last_comment', None)

        cursor = connection.cursor()
        sql = "UPDATE bug_comment SET content=%s, user_id_last_comment=%s WHERE id=%s"
        values = (content, user_id_last_comment, id_bug_comment)
        cursor.execute(sql, values)
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"message": "Bug comment updated successfully"}), 200
    else:
        return jsonify({"error": "Failed to connect to database"}), 500

# Xóa một bản ghi trong bảng bug_comment dựa trên id_bug_comment
@bug_comment_blueprint.route('/bug_comments/<int:id_bug_comment>', methods=['DELETE'])
def delete_bug_comment(id_bug_comment):
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        sql = "DELETE FROM bug_comment WHERE id=%s"
        values = (id_bug_comment,)
        cursor.execute(sql, values)
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"message": "Bug comment deleted successfully"}), 200
    else:
        return jsonify({"error": "Failed to connect to database"}), 500


@bug_comment_blueprint.route('/bug_comments/question/<int:id>', methods=['GET'])
def get_bug_comments_by_bug_question_id(id):
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("""
            SELECT bug_comment.*,
                   user.full_name AS user_name,
                   user_last_comment.full_name AS user_name_last_comment
            FROM bug_comment
            INNER JOIN user ON bug_comment.user_id = user.user_id
            INNER JOIN user AS user_last_comment ON bug_comment.user_id_last_comment = user_last_comment.user_id
            WHERE bug_comment.bug_question_id = %s
        """, (id,))
        bug_comments = cursor.fetchall()
        cursor.close()
        connection.close()
        return jsonify(bug_comments), 200
    else:
        return jsonify({"error": "Failed to connect to database"}), 500
