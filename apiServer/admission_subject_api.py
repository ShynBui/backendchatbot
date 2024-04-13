from flask import Blueprint, request, jsonify
from data.connect import connect_to_database

admission_subject_blueprint = Blueprint('admission_subject', __name__)

# Thêm một bản ghi mới vào bảng admission_subject
@admission_subject_blueprint.route('/admission_subjects', methods=['POST'])
def add_admission_subject():
    connection = connect_to_database()
    if connection:
        data = request.json
        id_subject = data['id_subject']
        name = data.get('name', None)

        cursor = connection.cursor()
        sql = "INSERT INTO admission_subject (id_subject, name) VALUES (%s, %s)"
        values = (id_subject, name)
        cursor.execute(sql, values)
        id_admission_subject = cursor.lastrowid  # Lấy ID của bản ghi vừa được thêm
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"message": "Admission subject added successfully", "id_admission_subject": id_admission_subject}), 201
    else:
        return jsonify({"error": "Failed to connect to database"}), 500

# Lấy thông tin tất cả các bản ghi trong bảng admission_subject
@admission_subject_blueprint.route('/admission_subjects', methods=['GET'])
def get_all_admission_subjects():
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM admission_subject")
        admission_subjects = cursor.fetchall()
        cursor.close()
        connection.close()
        return jsonify(admission_subjects), 200
    else:
        return jsonify({"error": "Failed to connect to database"}), 500

# Lấy thông tin của một bản ghi trong bảng admission_subject dựa trên id_admission_subject
@admission_subject_blueprint.route('/admission_subjects/<int:id_admission_subject>', methods=['GET'])
def get_admission_subject(id_admission_subject):
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor(dictionary=True)
        sql = "SELECT * FROM admission_subject WHERE id=%s"
        cursor.execute(sql, (id_admission_subject,))
        admission_subject = cursor.fetchone()
        cursor.close()
        connection.close()
        if admission_subject:
            return jsonify(admission_subject), 200
        else:
            return jsonify({"error": "Admission subject not found"}), 404
    else:
        return jsonify({"error": "Failed to connect to database"}), 500

# Cập nhật thông tin của một bản ghi trong bảng admission_subject dựa trên id_admission_subject
@admission_subject_blueprint.route('/admission_subjects/<int:id_admission_subject>', methods=['PUT'])
def update_admission_subject(id_admission_subject):
    connection = connect_to_database()
    if connection:
        data = request.json
        id_subject = data.get('id_subject', None)
        name = data.get('name', None)

        cursor = connection.cursor()
        sql = "UPDATE admission_subject SET id_subject=%s, name=%s WHERE id=%s"
        values = (id_subject, name, id_admission_subject)
        cursor.execute(sql, values)
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"message": "Admission subject updated successfully"}), 200
    else:
        return jsonify({"error": "Failed to connect to database"}), 500

# Xóa một bản ghi trong bảng admission_subject dựa trên id_admission_subject
@admission_subject_blueprint.route('/admission_subjects/<int:id_admission_subject>', methods=['DELETE'])
def delete_admission_subject(id_admission_subject):
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        sql = "DELETE FROM admission_subject WHERE id=%s"
        values = (id_admission_subject,)
        cursor.execute(sql, values)
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"message": "Admission subject deleted successfully"}), 200
    else:
        return jsonify({"error": "Failed to connect to database"}), 500
