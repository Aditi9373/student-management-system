from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Change these to your RDS credentials
db = mysql.connector.connect(
    host="RDS-ENDPOINT",
    user="admin",
    password="password",
    database="studentdb"
)

# HOME – SHOW STUDENTS
@app.route("/")
def home():
    cursor = db.cursor()
    cursor.execute("SELECT id, name, email, course FROM students")
    students = cursor.fetchall()
    return render_template("index.html", students=students)

# ADD STUDENT
@app.route("/add", methods=["POST"])
def add():
    name = request.form["name"]
    email = request.form["email"]
    course = request.form["course"]

    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO students (name,email,course) VALUES (%s,%s,%s)",
        (name, email, course)
    )
    db.commit()
    return redirect("/")

# DELETE STUDENT
@app.route("/delete/<int:id>")
def delete(id):
    cursor = db.cursor()
    cursor.execute("DELETE FROM students WHERE id=%s", (id,))
    db.commit()
    return redirect("/")

# EDIT PAGE
@app.route("/edit/<int:id>")
def edit(id):
    cursor = db.cursor()
    cursor.execute("SELECT id,name,email,course FROM students WHERE id=%s", (id,))
    student = cursor.fetchone()
    return render_template("edit.html", student=student)

# UPDATE STUDENT
@app.route("/update", methods=["POST"])
def update():
    id = request.form["id"]
    name = request.form["name"]
    email = request.form["email"]
    course = request.form["course"]

    cursor = db.cursor()
    cursor.execute(
        "UPDATE students SET name=%s,email=%s,course=%s WHERE id=%s",
        (name, email, course, id)
    )
    db.commit()
    return redirect("/")

app.run(host="0.0.0.0", port=5000)
