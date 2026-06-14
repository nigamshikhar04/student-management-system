import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Shikhar@0408",
    database="student_db"
)

cursor = connection.cursor()

def calculate_grade(marks):
    if marks>=90:
        return "A+"
    elif marks>=80:
        return "A"
    elif marks >=70:
        return "B"
    elif marks >=60:
        return "C"
    elif marks >=50:
        return "D"
    else:
        return "F"

def add_student():
    name=input("Enter student name: ")
    marks=int(input("Enter marks (0-100)"))
    grade = calculate_grade(marks)

    cursor.execute("""
           INSERT INTO students (name, marks, grade)
           VALUES (%s, %s, %s)
       """, (name, marks, grade))
    connection.commit()
    print(f"Student name {name} added with grade {grade}!")

def view_students():
    cursor.execute("Select * from students")
    students=cursor.fetchall()

    if len(students) == 0:
        print("No student Found")
    else:
        print("\n--- All Students ---")
        for student in students:
            print(f"ID: {student[0]} | Name: {student[1]} | Marks: {student[2]} | Grade: {student[3]}")

def search_student():
    name=input("Enter the name of the student: ")
    cursor.execute("""
           SELECT * FROM students 
           WHERE name LIKE %s
       """, (f"%{name}%",))
    results = cursor.fetchall()
    if len(results)==0:
        print("No student found with that name.")
    else:
        print("\n--- Search Results ---")
        for student in results:
            print(f"ID: {student[0]} | Name: {student[1]} | Marks: {student[2]} | Grade: {student[3]}")

def delete_student():
    view_students()
    student_id=int(input("\nEnter student ID to delete: "))
    cursor.execute("DELETE FROM students WHERE id = %s", (student_id,))
    connection.commit()
    print(f"Student with ID {student_id} deleted successfully!")
def main():
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student by name:")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter choice (1/2/3): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Try again.")


main()






