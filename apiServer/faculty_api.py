from flask import Blueprint, request, jsonify
from data.connect import connect_to_database

faculty_blueprint = Blueprint('faculty', __name__)

# Thêm một bản ghi mới vào bảng faculty
@faculty_blueprint.route('/faculties', methods=['POST'])
def add_faculty():
    connection = connect_to_database()
    if connection:
        data = request.json
        name = data['name']

        cursor = connection.cursor()
        sql = "INSERT INTO faculty (name) VALUES (%s)"
        values = (name,)
        cursor.execute(sql, values)
        id_faculty = cursor.lastrowid  # Lấy ID của bản ghi vừa được thêm
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"message": "Faculty added successfully", "id_faculty": id_faculty}), 201
    else:
        return jsonify({"error": "Failed to connect to database"}), 500

# Lấy thông tin tất cả các bản ghi trong bảng faculty
@faculty_blueprint.route('/faculties', methods=['GET'])
def get_all_faculties():
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM faculty")
        faculties = cursor.fetchall()
        cursor.close()
        connection.close()
        return jsonify(faculties), 200
    else:
        return jsonify({"error": "Failed to connect to database"}), 500

# Lấy thông tin của một bản ghi trong bảng faculty dựa trên id_faculty
@faculty_blueprint.route('/faculties/<int:id_faculty>', methods=['GET'])
def get_faculty(id_faculty):
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor(dictionary=True)
        sql = "SELECT * FROM faculty WHERE id_faculty = %s"
        cursor.execute(sql, (id_faculty,))
        faculty = cursor.fetchone()
        cursor.close()
        connection.close()
        if faculty:
            return jsonify(faculty), 200
        else:
            return jsonify({"error": "Faculty not found"}), 404
    else:
        return jsonify({"error": "Failed to connect to database"}), 500

# Cập nhật thông tin của một bản ghi trong bảng faculty dựa trên id_faculty
@faculty_blueprint.route('/faculties/<int:id_faculty>', methods=['PUT'])
def update_faculty(id_faculty):
    connection = connect_to_database()
    if connection:
        data = request.json
        name = data.get('name', None)

        cursor = connection.cursor()
        sql = "UPDATE faculty SET name=%s WHERE id_faculty=%s"
        values = (name, id_faculty)
        cursor.execute(sql, values)
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"message": "Faculty updated successfully"}), 200
    else:
        return jsonify({"error": "Failed to connect to database"}), 500

# Xóa một bản ghi trong bảng faculty dựa trên id_faculty
@faculty_blueprint.route('/faculties/<int:id_faculty>', methods=['DELETE'])
def delete_faculty(id_faculty):
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        sql = "DELETE FROM faculty WHERE id_faculty=%s"
        values = (id_faculty,)
        cursor.execute(sql, values)
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"message": "Faculty deleted successfully"}), 200
    else:
        return jsonify({"error": "Failed to connect to database"}), 500
