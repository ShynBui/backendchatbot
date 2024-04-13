from flask import Blueprint, request, jsonify
from data.connect import connect_to_database

data_score_blueprint = Blueprint('data_score', __name__)

# Thêm một bản ghi mới vào bảng data_score
@data_score_blueprint.route('/data_scores', methods=['POST'])
def add_data_score():
    connection = connect_to_database()
    if connection:
        data = request.json
        id_career = data['id_career']
        score = data['score']
        name = data['name']
        id_faculty = data.get('id_faculty', None)
        year = data['year']
        multiplier = data.get('multiplier', None)  # Thêm đọc giá trị của cột multiplier nếu có

        cursor = connection.cursor()
        sql = "INSERT INTO data_score (id_career, score, name, id_faculty, year, multiplier) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (id_career, score, name, id_faculty, year, multiplier)  # Thêm giá trị của cột multiplier vào câu lệnh SQL
        cursor.execute(sql, values)
        id_score = cursor.lastrowid
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"message": "Data score added successfully", "id_score": id_score}), 201
    else:
        return jsonify({"error": "Failed to connect to database"}), 500

# Lấy thông tin tất cả các bản ghi trong bảng data_score
@data_score_blueprint.route('/data_scores', methods=['GET'])
def get_all_data_scores():
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM data_score")
        data_scores = cursor.fetchall()
        cursor.close()
        connection.close()
        return jsonify(data_scores), 200
    else:
        return jsonify({"error": "Failed to connect to database"}), 500

# Lấy thông tin của một bản ghi trong bảng data_score dựa trên id_score
@data_score_blueprint.route('/data_scores/<int:id_score>', methods=['GET'])
def get_data_score(id_score):
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor(dictionary=True)
        sql = "SELECT * FROM data_score WHERE id_score = %s"
        cursor.execute(sql, (id_score,))
        data_score = cursor.fetchone()
        cursor.close()
        connection.close()
        if data_score:
            return jsonify(data_score), 200
        else:
            return jsonify({"error": "Data score not found"}), 404
    else:
        return jsonify({"error": "Failed to connect to database"}), 500

# Cập nhật thông tin của một bản ghi trong bảng data_score dựa trên id_score
@data_score_blueprint.route('/data_scores/<int:id_score>', methods=['PUT'])
def update_data_score(id_score):
    connection = connect_to_database()
    if connection:
        data = request.json
        id_career = data.get('id_career', None)
        score = data.get('score', None)
        name = data.get('name', None)
        id_faculty = data.get('id_faculty', None)
        year = data.get('year', None)
        multiplier = data.get('multiplier', None)  # Thêm giá trị của cột multiplier nếu có

        cursor = connection.cursor()
        sql = "UPDATE data_score SET id_career=%s, score=%s, name=%s, id_faculty=%s, year=%s, multiplier=%s WHERE id_score=%s"
        values = (id_career, score, name, id_faculty, year, multiplier, id_score)  # Thêm giá trị của cột multiplier vào câu lệnh SQL
        cursor.execute(sql, values)
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"message": "Data score updated successfully"}), 200
    else:
        return jsonify({"error": "Failed to connect to database"}), 500

# Xóa một bản ghi trong bảng data_score dựa trên id_score
@data_score_blueprint.route('/data_scores/<int:id_score>', methods=['DELETE'])
def delete_data_score(id_score):
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        sql = "DELETE FROM data_score WHERE id_score=%s"
        values = (id_score,)
        cursor.execute(sql, values)
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"message": "Data score deleted successfully"}), 200
    else:
        return jsonify({"error": "Failed to connect to database"}), 500


# Endpoint để lấy danh sách các đối tượng theo năm
@data_score_blueprint.route('/objects_by_year', methods=['GET'])
def get_objects_by_year():
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM data_score ORDER BY year DESC")
        objects = cursor.fetchall()
        cursor.close()
        connection.close()

        objects_by_year = {}
        for obj in objects:
            year = obj['year']
            if year not in objects_by_year:
                objects_by_year[year] = []
            objects_by_year[year].append({
                'id_score': obj['id_score'],
                'id_career': obj['id_career'],
                'score': obj['score'],
                'name': obj['name'],
                'id_faculty': obj['id_faculty'],
                'year': year
            })

        result = [objects_by_year[year] for year in objects_by_year.keys()]

        return jsonify(result), 200
    else:
        return jsonify({"error": "Failed to connect to database"}), 500

# Hàm tính điểm trung bình mỗi năm từ danh sách các đối tượng
def calculate_average_score(objects_by_year):
    average_scores = {}
    for year, objects in objects_by_year.items():
        total_score = sum(obj['score'] for obj in objects)
        num_objects = len(objects)
        if num_objects > 0:
            average_score = total_score / num_objects
        else:
            average_score = 0
        average_scores[year] = average_score
    return average_scores

# Endpoint để lấy danh sách các đối tượng theo năm và tính điểm trung bình
@data_score_blueprint.route('/objects_and_average_score_by_year', methods=['GET'])
def get_objects_and_average_score_by_year():
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM data_score ORDER BY year")
        objects = cursor.fetchall()
        cursor.close()
        connection.close()

        objects_by_year = {}
        for obj in objects:
            year = obj['year']
            if year not in objects_by_year:
                objects_by_year[year] = []
            objects_by_year[year].append({
                'id_score': obj['id_score'],
                'id_career': obj['id_career'],
                'score': obj['score'],
                'name': obj['name'],
                'id_faculty': obj['id_faculty'],
                'year': year
            })

        average_scores = calculate_average_score(objects_by_year)

        result = []
        for year, objects in sorted(objects_by_year.items()):
            year_data = {'year': year, 'objects': objects}
            year_data['average_score'] = average_scores.get(year, 0)
            result.append(year_data)

        return jsonify(result), 200
    else:
        return jsonify({"error": "Failed to connect to database"}), 500
