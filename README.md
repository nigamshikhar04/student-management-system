Student Management System

Full-stack web app to manage student records with automatic grade calculation. Built with Python, Flask, and MySQL.

Features:
Add students with auto-calculated grades (A+ to F)
View all records in a styled table
Delete records with one click
Data persists in MySQL


Tech Stack:
Python · Flask · MySQL · HTML/CSS · Jinja2

Run Locally
bashgit clone https://github.com/nigamshikhar04/student-management-system.git
pip install flask mysql-connector-python
Create database student_db in MySQL, update credentials in app.py, then:
bashpython database.py
python app.py

Visit http://127.0.0.1:5000

Project Structure

├── app.py          # Flask routes
├── database.py     # DB setup
├── templates/
│   └── index.html
