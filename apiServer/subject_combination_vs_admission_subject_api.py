from flask import Blueprint, request, jsonify
from data.connect import connect_to_database
import json

subject_combination_vs_admission_subject_blueprint = Blueprint('subject_combination_vs_admission_subject', __name__)

# Thêm một bản ghi mới vào bảng subject_combination_vs_admission_subject
@subject_combination_vs_admission_subject_blueprint.route('/subject_combination_vs_admission_subjects', methods=['POST'])
def add_subject_combination_vs_admission_subject():
    connection = connect_to_database()
    if connection:
        data = request.json
        id_combination = data['id_combination']
        id_subject = data['id_subject']

        cursor = connection.cursor()
        sql = "INSERT INTO subject_combination_vs_admission_subject (id_combination, id_subject) VALUES (%s, %s)"
        values = (id_combination, id_subject)
        cursor.execute(sql, values)
        id_record = cursor.lastrowid  # Lấy ID của bản ghi vừa được thêm
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"message": "Subject combination vs admission subject added successfully", "id_record": id_record}), 201
    else:
        return jsonify({"error": "Failed to connect to database"}), 500

# Lấy thông tin tất cả các bản ghi trong bảng subject_combination_vs_admission_subject
@subject_combination_vs_admission_subject_blueprint.route('/subject_combination_vs_admission_subjects', methods=['GET'])
def get_all_subject_combination_vs_admission_subjects():
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM subject_combination_vs_admission_subject")
        subject_combination_vs_admission_subjects = cursor.fetchall()
        cursor.close()
        connection.close()
        return jsonify(subject_combination_vs_admission_subjects), 200
    else:
        return jsonify({"error": "Failed to connect to database"}), 500

# Lấy thông tin của một bản ghi trong bảng subject_combination_vs_admission_subject dựa trên id_record
@subject_combination_vs_admission_subject_blueprint.route('/subject_combination_vs_admission_subjects/<int:id_record>', methods=['GET'])
def get_subject_combination_vs_admission_subject(id_record):
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor(dictionary=True)
        sql = "SELECT * FROM subject_combination_vs_admission_subject WHERE id=%s"
        cursor.execute(sql, (id_record,))
        subject_combination_vs_admission_subject = cursor.fetchone()
        cursor.close()
        connection.close()
        if subject_combination_vs_admission_subject:
            return jsonify(subject_combination_vs_admission_subject), 200
        else:
            return jsonify({"error": "Subject combination vs admission subject not found"}), 404
    else:
        return jsonify({"error": "Failed to connect to database"}), 500

# Cập nhật thông tin của một bản ghi trong bảng subject_combination_vs_admission_subject dựa trên id_record
@subject_combination_vs_admission_subject_blueprint.route('/subject_combination_vs_admission_subjects/<int:id_record>', methods=['PUT'])
def update_subject_combination_vs_admission_subject(id_record):
    connection = connect_to_database()
    if connection:
        data = request.json
        id_combination = data.get('id_combination', None)
        id_subject = data.get('id_subject', None)

        cursor = connection.cursor()
        sql = "UPDATE subject_combination_vs_admission_subject SET id_combination=%s, id_subject=%s WHERE id=%s"
        values = (id_combination, id_subject, id_record)
        cursor.execute(sql, values)
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"message": "Subject combination vs admission subject updated successfully"}), 200
    else:
        return jsonify({"error": "Failed to connect to database"}), 500

# Xóa một bản ghi trong bảng subject_combination_vs_admission_subject dựa trên id_record
@subject_combination_vs_admission_subject_blueprint.route('/subject_combination_vs_admission_subjects/<int:id_record>', methods=['DELETE'])
def delete_subject_combination_vs_admission_subject(id_record):
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        sql = "DELETE FROM subject_combination_vs_admission_subject WHERE id=%s"
        values = (id_record,)
        cursor.execute(sql, values)
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"message": "Subject combination vs admission subject deleted successfully"}), 200
    else:
        return jsonify({"error": "Failed to connect to database"}), 500
    
@subject_combination_vs_admission_subject_blueprint.route('/subject_combination_vs_admission_subjects_group', methods=['GET'])
def get_subject_combination_vs_admission_subjects_group():
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor(dictionary=True)
        sql = """
            SELECT sc.id_combination,
                   JSON_UNQUOTE(JSON_ARRAYAGG(JSON_OBJECT('id_subject', asub.id_subject, 'name', asub.name))) AS subjects
            FROM subject_combination_vs_admission_subject scvas
            JOIN admission_subject asub ON scvas.id_subject = asub.id_subject
            JOIN subject_combination sc ON scvas.id_combination = sc.id_combination
            GROUP BY sc.id_combination;
        """
        cursor.execute(sql)
        results = cursor.fetchall()
        cursor.close()
        connection.close()

        # Chuyển đổi chuỗi JSON thành danh sách Python
        for result in results:
            result['subjects'] = json.loads(result['subjects'])

        return jsonify(results), 200
    else:
        return jsonify({"error": "Failed to connect to database"}), 500