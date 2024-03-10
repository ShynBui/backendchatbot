from data.connect import connect_to_database
# Đọc nội dung của file SQL dump

# Kết nối đến cơ sở dữ liệu
connection = connect_to_database()

mycursor = connection.cursor()

with open('dump.sql', 'r') as file:
    sql_script = file.read()

# Tạo bảng và dữ liệu từ file SQL dump
commands = sql_script.split(';')

for command in commands:
    try:
        mycursor.execute(command)
        connection.commit()
    except Exception as e:
        print("Error:", e)

print("Tables and data have been created successfully")