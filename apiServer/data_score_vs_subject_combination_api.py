from flask import Blueprint, request, jsonify
from data.connect import connect_to_database
import json

data_score_vs_subject_combination_blueprint = Blueprint('data_score_vs_subject_combination', __name__)

@data_score_vs_subject_combination_blueprint.route('/data_score_vs_subject_combinations', methods=['POST'])
def add_data_score_vs_subject_combination():
    connection = connect_to_database()
    if connection:
        data = request.json
        id_score = data['id_score']
        id_combination = data.get('id_combination', None)
        formula = data.get('formula', None)

        cursor = connection.cursor()
        sql = "INSERT INTO data_score_vs_subject_combination (id_score, id_combination, formula) VALUES (%s, %s, %s)"
        values = (id_score, id_combination, formula)
        cursor.execute(sql, values)
        id_record = cursor.lastrowid  # Lấy ID của bản ghi vừa được thêm
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"message": "Data score vs subject combination added successfully", "id_record": id_record}), 201
    else:
        return jsonify({"error": "Failed to connect to database"}), 500

# Lấy thông tin tất cả các bản ghi trong bảng data_score_vs_subject_combination
@data_score_vs_subject_combination_blueprint.route('/data_score_vs_subject_combinations', methods=['GET'])
def get_all_data_score_vs_subject_combinations():
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM data_score_vs_subject_combination")
        data_score_vs_subject_combinations = cursor.fetchall()
        cursor.close()
        connection.close()
        return jsonify(data_score_vs_subject_combinations), 200
    else:
        return jsonify({"error": "Failed to connect to database"}), 500

# Lấy thông tin của một bản ghi trong bảng data_score_vs_subject_combination dựa trên id_record
@data_score_vs_subject_combination_blueprint.route('/data_score_vs_subject_combinations/<int:id_record>', methods=['GET'])
def get_data_score_vs_subject_combination(id_record):
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor(dictionary=True)
        sql = "SELECT * FROM data_score_vs_subject_combination WHERE id=%s"
        cursor.execute(sql, (id_record,))
        data_score_vs_subject_combination = cursor.fetchone()
        cursor.close()
        connection.close()
        if data_score_vs_subject_combination:
            return jsonify(data_score_vs_subject_combination), 200
        else:
            return jsonify({"error": "Data score vs subject combination not found"}), 404
    else:
        return jsonify({"error": "Failed to connect to database"}), 500

# Cập nhật thông tin của một bản ghi trong bảng data_score_vs_subject_combination dựa trên id_record
@data_score_vs_subject_combination_blueprint.route('/data_score_vs_subject_combinations/<int:id_record>', methods=['PUT'])
def update_data_score_vs_subject_combination(id_record):
    connection = connect_to_database()
    if connection:
        data = request.json
        id_score = data.get('id_score', None)
        id_combination = data.get('id_combination', None)
        formula = data.get('formula', None)

        cursor = connection.cursor()
        sql = "UPDATE data_score_vs_subject_combination SET id_score=%s, id_combination=%s, formula=%s WHERE id=%s"
        values = (id_score, id_combination, formula, id_record)
        cursor.execute(sql, values)
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"message": "Data score vs subject combination updated successfully"}), 200
    else:
        return jsonify({"error": "Failed to connect to database"}), 500

# Xóa một bản ghi trong bảng data_score_vs_subject_combination dựa trên id_record
@data_score_vs_subject_combination_blueprint.route('/data_score_vs_subject_combinations/<int:id_record>', methods=['DELETE'])
def delete_data_score_vs_subject_combination(id_record):
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        sql = "DELETE FROM data_score_vs_subject_combination WHERE id=%s"
        values = (id_record,)
        cursor.execute(sql, values)
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"message": "Data score vs subject combination deleted successfully"}), 200
    else:
        return jsonify({"error": "Failed to connect to database"}), 500



@data_score_vs_subject_combination_blueprint.route('/data_score_and_combination_by_year', methods=['GET'])
def get_data_score_and_combination_by_year():
    year = request.args.get('year', None)  # Lấy giá trị year từ tham số truy vấn

    connection = connect_to_database()
    if connection:
        cursor = connection.cursor(dictionary=True)

        # Truy vấn để lấy dữ liệu từ bảng data_score và mảng id_combination từ bảng data_score_vs_subject_combination
        sql = """
           SELECT ds.id_score, ds.id_career, ds.score, ds.name, ds.id_faculty, ds.year, ds.multiplier,
                    JSON_ARRAYAGG(dsvc.id_combination) AS id_combination
            FROM data_score ds
            LEFT JOIN data_score_vs_subject_combination dsvc ON ds.id_score = dsvc.id_score
            WHERE ds.year = %s
            GROUP BY ds.id_score
        """
        cursor.execute(sql, (year,))
        data = cursor.fetchall()

        cursor.close()
        connection.close()

        # Chuyển đổi chuỗi JSON thành mảng Python
        for item in data:
            item['id_combination'] = json.loads(item['id_combination'])

        return jsonify(data), 200
    else:
        return jsonify({"error": "Failed to connect to database"}), 500
