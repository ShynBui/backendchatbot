from flask import Blueprint, request, jsonify
from data.connect import connect_to_database

information_blueprint = Blueprint('information', __name__)

# Thêm một thông tin mới
@information_blueprint.route('/information', methods=['POST'])
def add_information():
    connection = connect_to_database()
    if connection:
        data = request.json
        name = data['name']
        link = data['link']

        cursor = connection.cursor()
        sql = "INSERT INTO information (name, link) VALUES (%s, %s)"
        values = (name, link)
        cursor.execute(sql, values)
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"message": "Information added successfully"}), 201
    else:
        return jsonify({"error": "Failed to connect to database"}), 500

# Lấy thông tin tất cả information
@information_blueprint.route('/information', methods=['GET'])
def get_all_information():
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM information")
        information = cursor.fetchall()
        cursor.close()
        connection.close()
        return jsonify(information), 200
    else:
        return jsonify({"error": "Failed to connect to database"}), 500

# Lấy thông tin của một thông tin dựa trên in_id
@information_blueprint.route('/information/<int:in_id>', methods=['GET'])
def get_information(in_id):
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor(dictionary=True)
        sql = "SELECT * FROM information WHERE in_id = %s"
        cursor.execute(sql, (in_id,))
        info = cursor.fetchone()
        cursor.close()
        connection.close()
        if info:
            return jsonify(info), 200
        else:
            return jsonify({"error": "Information not found"}), 404
    else:
        return jsonify({"error": "Failed to connect to database"}), 500

# Cập nhật thông tin của một thông tin dựa trên in_id
@information_blueprint.route('/information/<int:in_id>', methods=['PUT'])
def update_information(in_id):
    connection = connect_to_database()
    if connection:
        data = request.json
        name = data.get('name', '')
        link = data.get('link', '')

        cursor = connection.cursor()
        sql = "UPDATE information SET name=%s, link=%s WHERE in_id=%s"
        values = (name, link, in_id)
        cursor.execute(sql, values)
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"message": "Information updated successfully"}), 200
    else:
        return jsonify({"error": "Failed to connect to database"}), 500

# Xóa một thông tin dựa trên in_id
@information_blueprint.route('/information/<int:in_id>', methods=['DELETE'])
def delete_information(in_id):
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        sql = "DELETE FROM information WHERE in_id=%s"
        values = (in_id,)
        cursor.execute(sql, values)
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"message": "Information deleted successfully"}), 200
    else:
        return jsonify({"error": "Failed to connect to database"}), 500
