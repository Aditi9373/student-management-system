# student-management-system
Flask-based Student Management System with AWS RDS backend and modern UI for adding, editing, and deleting student records.

## Features
- Add students
- Edit students
- Delete students
- View student list in a table
- Attractive UI

## Tech Stack
- Python 3
- Flask
- MySQL (AWS RDS)
- HTML/CSS

## Steps Implemented
1. Launch an Ubuntu EC2 instance and connect to it.
2. Create a MySQL database and students table (using AWS RDS or MySQL).
3. Configure the database connection in app.py.
4. Build the Flask backend for CRUD operations (Add, Edit, Delete, View).
5. Design the UI using HTML and CSS inside the templates folder.
6. Run the Flask application using Python on the EC2 instance.
7. Access the application in a web browser using the EC2 public IP to manage student records.

## Files Included
student-management-system/
app.py
templates/
index.html
edit.html

## Usage
1. Configure RDS endpoint in app.py
2. Run app: python3 app.py
3. Open browser: http://EC2_PUBLIC_IP:5000


