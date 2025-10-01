from flask import Flask, request, jsonify
from pymongo import MongoClient
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

# MongoDB Atlas
MONGO_URI = os.getenv("MONGO_URI")
mongo_client = MongoClient(MONGO_URI)
mongo_db = mongo_client["student_management"]
mongo_students = mongo_db["students"]

# MySQL Connection
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASS = os.getenv("MYSQL_PASS")
MYSQL_DB = os.getenv("MYSQL_DB")

def get_mysql_conn():
    return mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASS,
        database=MYSQL_DB
    )

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

# Add student
@app.route("/student", methods=["POST"])
def add_student():
    data = request.json
    name = data.get("name")
    email = data.get("email")
    dept = data.get("department", "")
    year = data.get("year", 1)
    skills = data.get("skills", [])

    # Insert in MySQL
    conn = get_mysql_conn()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO students (name, email, department, year) VALUES (%s,%s,%s,%s)",
        (name, email, dept, year)
    )
    conn.commit()
    mysql_id = cursor.lastrowid
    cursor.close()
    conn.close()

    # Insert in MongoDB
    profile = {
        "mysql_id": mysql_id,
        "name": name,
        "email": email,
        "department": dept,
        "year": year,
        "skills": skills,
        "notes": []
    }
    mongo_students.insert_one(profile)

    return jsonify({"msg": "Student added", "mysql_id": mysql_id}), 201

# List all students
@app.route("/students", methods=["GET"])
def list_students():
    docs = list(mongo_students.find({}, {"_id": 0}))
    conn = get_mysql_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    sql_data = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify({"mongo": docs, "sql": sql_data})

# Add note to MongoDB student
@app.route("/student/<int:mysql_id>/note", methods=["POST"])
def add_note(mysql_id):
    data = request.json
    note = data.get("note", "")
    mongo_students.update_one({"mysql_id": mysql_id}, {"$push": {"notes": {"text": note}}})
    return jsonify({"msg": "Note added"}), 200

if __name__ == "__main__":
    app.run(debug=True)
