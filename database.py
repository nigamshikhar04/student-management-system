import mysql.connector

connection= mysql.connector.connect(
    host='localhost',
    user='root',
    password='Shikhar@0408',
    database='student_db'

)
cursor=connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        marks INT,
        grade VARCHAR(5)
    )
""")

connection.commit()





