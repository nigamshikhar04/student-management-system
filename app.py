from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Shikhar@0408",
    database="student_db"
)

cursor = connection.cursor()

def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"

@app.route("/")
def home():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    return render_template("index.html", students=students)

@app.route("/add", methods=["POST"])
def add_student():
    name = request.form["name"]
    marks = int(request.form["marks"])
    grade = calculate_grade(marks)

    cursor.execute("""
        INSERT INTO students (name, marks, grade)
        VALUES (%s, %s, %s)
    """, (name, marks, grade))

    connection.commit()
    return redirect("/")

@app.route("/delete/<int:student_id>", methods=["POST"])
def delete_student(student_id):
    cursor.execute("DELETE FROM students WHERE id = %s", (student_id,))
    connection.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)