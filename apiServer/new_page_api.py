from flask import Blueprint, request, jsonify
from datetime import datetime
from data.connect import connect_to_database

new_page_blueprint = Blueprint('page', __name__)

# Thêm một trang mới vào bảng new_page
@new_page_blueprint.route('/pages', methods=['POST'])
def add_page():
    connection = connect_to_database()
    if connection:
        data = request.json
        user_id = data.get('user_id',None)
        name = data.get('name')
        content = data.get('content')
        create_time = datetime.now()
        update_time = datetime.now()

        cursor = connection.cursor()
        sql = "INSERT INTO new_page (user_id, name, content, create_time, update_time) VALUES (%s, %s, %s, %s, %s)"
        values = (user_id, name, content, create_time, update_time)
        cursor.execute(sql, values)
        id_page = cursor.lastrowid  # Lấy ID của bản ghi vừa được thêm
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"message": "Page added successfully", "id_page": id_page}), 201
    else:
        return jsonify({"error": "Failed to connect to database"}), 500

# Lấy thông tin tất cả các trang từ bảng new_page
@new_page_blueprint.route('/pages', methods=['GET'])
def get_all_pages():
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM new_page ORDER BY create_time DESC")
        pages = cursor.fetchall()
        cursor.close()
        connection.close()
        return jsonify(pages), 200
    else:
        return jsonify({"error": "Failed to connect to database"}), 500

# Lấy thông tin của một trang từ bảng new_page dựa trên id_page
@new_page_blueprint.route('/pages/<int:id_page>', methods=['GET'])
def get_page(id_page):
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor(dictionary=True)
        sql = "SELECT * FROM new_page WHERE id = %s"
        cursor.execute(sql, (id_page,))
        page = cursor.fetchone()
        cursor.close()
        connection.close()
        if page:
            return jsonify(page), 200
        else:
            return jsonify({"error": "Page not found"}), 404
    else:
        return jsonify({"error": "Failed to connect to database"}), 500


@new_page_blueprint.route('/pages/user/<int:user_id>', methods=['GET'])
def get_pages_by_user_id(user_id):
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor(dictionary=True)
        sql = "SELECT * FROM new_page WHERE user_id = %s"
        cursor.execute(sql, (user_id,))
        pages = cursor.fetchall()
        cursor.close()
        connection.close()
        if pages:
            return jsonify(pages), 200
        else:
            return jsonify({"error": "Pages not found"}), 404
    else:
        return jsonify({"error": "Failed to connect to database"}), 500


# Cập nhật thông tin của một trang từ bảng new_page dựa trên id_page
@new_page_blueprint.route('/pages/<int:id_page>', methods=['PUT'])
def update_page(id_page):
    connection = connect_to_database()
    if connection:
        data = request.json
        name = data.get('name', None)
        content = data.get('content', None)
        update_time = datetime.now()

        cursor = connection.cursor()
        sql = "UPDATE new_page SET name=%s, content=%s, update_time=%s WHERE id=%s"
        values = (name, content, update_time, id_page)
        cursor.execute(sql, values)
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"message": "Page updated successfully"}), 200
    else:
        return jsonify({"error": "Failed to connect to database"}), 500

# Xóa một trang từ bảng new_page dựa trên id_page
@new_page_blueprint.route('/pages/<int:id_page>', methods=['DELETE'])
def delete_page(id_page):
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        sql = "DELETE FROM new_page WHERE id=%s"
        values = (id_page,)
        cursor.execute(sql, values)
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"message": "Page deleted successfully"}), 200
    else:
        return jsonify({"error": "Failed to connect to database"}), 500
