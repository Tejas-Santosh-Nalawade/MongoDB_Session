import streamlit as st
import requests

API_BASE = "http://127.0.0.1:5000"

st.title("📚 Student Management Dashboard")

menu = st.sidebar.selectbox("Menu", ["Add Student", "List Students", "Add Note"])

if menu == "Add Student":
    st.header("➕ Add Student")
    name = st.text_input("Name")
    email = st.text_input("Email")
    dept = st.text_input("Department")
    year = st.number_input("Year", min_value=1, max_value=5, value=3)
    skills = st.text_input("Skills (comma-separated)")

    if st.button("Add"):
        payload = {
            "name": name,
            "email": email,
            "department": dept,
            "year": year,
            "skills": [s.strip() for s in skills.split(",") if s.strip()]
        }
        res = requests.post(f"{API_BASE}/student", json=payload)
        if res.status_code == 201:
            st.success("Student added successfully!")
        else:
            st.error("Failed to add student.")

elif menu == "List Students":
    st.header("👀 Students")
    if st.button("Show All"):
        res = requests.get(f"{API_BASE}/students")
        if res.ok:
            data = res.json()
            st.subheader("MongoDB Data")
            st.json(data["mongo"])
            st.subheader("MySQL Data")
            st.json(data["sql"])
        else:
            st.error("Failed to fetch data.")

elif menu == "Add Note":
    st.header("📝 Add Note to Student")
    mysql_id = st.number_input("MySQL Student ID", min_value=1, step=1)
    note = st.text_area("Note")

    if st.button("Add Note"):
        res = requests.post(f"{API_BASE}/student/{mysql_id}/note", json={"note": note})
        if res.ok:
            st.success("Note added successfully!")
        else:
            st.error("Failed to add note.")
