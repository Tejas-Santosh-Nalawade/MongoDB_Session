import mysql.connector
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

# Test MySQL
conn = mysql.connector.connect(
    host=os.getenv("MYSQL_HOST"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASS"),
    database=os.getenv("MYSQL_DB")
)
print("MySQL connected")
conn.close()

# Test MongoDB
mongo_client = MongoClient(os.getenv("MONGO_URI"))
mongo_db = mongo_client["student_management"]
mongo_students = mongo_db["students"]
print("MongoDB connected")
