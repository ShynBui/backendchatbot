from flask import Blueprint, request, jsonify
from data.connect import connect_to_database

subject_combination_blueprint = Blueprint('subject_combination', __name__)

# Thêm một bản ghi mới vào bảng subject_combination
@subject_combination_blueprint.route('/subject_combinations', methods=['POST'])
def add_subject_combination():
    connection = connect_to_database()
    if connection:
        data = request.json
        id_combination = data['id_combination']
        name = data.get('name', None)

        cursor = connection.cursor()
        sql = "INSERT INTO subject_combination (id_combination, name) VALUES (%s, %s)"
        values = (id_combination, name)
        cursor.execute(sql, values)
        id_record = cursor.lastrowid  # Lấy ID của bản ghi vừa được thêm
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"message": "Subject combination added successfully", "id_record": id_record}), 201
    else:
        return jsonify({"error": "Failed to connect to database"}), 500

# Lấy thông tin tất cả các bản ghi trong bảng subject_combination
@subject_combination_blueprint.route('/subject_combinations', methods=['GET'])
def get_all_subject_combinations():
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM subject_combination")
        subject_combinations = cursor.fetchall()
        cursor.close()
        connection.close()
        return jsonify(subject_combinations), 200
    else:
        return jsonify({"error": "Failed to connect to database"}), 500

# Lấy thông tin của một bản ghi trong bảng subject_combination dựa trên id_record
@subject_combination_blueprint.route('/subject_combinations/<int:id_record>', methods=['GET'])
def get_subject_combination(id_record):
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor(dictionary=True)
        sql = "SELECT * FROM subject_combination WHERE id=%s"
        cursor.execute(sql, (id_record,))
        subject_combination = cursor.fetchone()
        cursor.close()
        connection.close()
        if subject_combination:
            return jsonify(subject_combination), 200
        else:
            return jsonify({"error": "Subject combination not found"}), 404
    else:
        return jsonify({"error": "Failed to connect to database"}), 500

# Cập nhật thông tin của một bản ghi trong bảng subject_combination dựa trên id_record
@subject_combination_blueprint.route('/subject_combinations/<int:id_record>', methods=['PUT'])
def update_subject_combination(id_record):
    connection = connect_to_database()
    if connection:
        data = request.json
        id_combination = data.get('id_combination', None)
        name = data.get('name', None)

        cursor = connection.cursor()
        sql = "UPDATE subject_combination SET id_combination=%s, name=%s WHERE id=%s"
        values = (id_combination, name, id_record)
        cursor.execute(sql, values)
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"message": "Subject combination updated successfully"}), 200
    else:
        return jsonify({"error": "Failed to connect to database"}), 500

# Xóa một bản ghi trong bảng subject_combination dựa trên id_record
@subject_combination_blueprint.route('/subject_combinations/<int:id_record>', methods=['DELETE'])
def delete_subject_combination(id_record):
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        sql = "DELETE FROM subject_combination WHERE id=%s"
        values = (id_record,)
        cursor.execute(sql, values)
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"message": "Subject combination deleted successfully"}), 200
    else:
        return jsonify({"error": "Failed to connect to database"}), 500
