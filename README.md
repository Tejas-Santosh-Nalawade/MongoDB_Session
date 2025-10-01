# 📚 Student Management System

A full-stack student management application built with Flask (backend), Streamlit (frontend), MongoDB Atlas (document storage), and MySQL (relational data). This system demonstrates hybrid database architecture for managing student information and profiles.

## 🏗️ System Architecture

- **Backend**: Flask REST API with dual database connectivity
- **Frontend**: Streamlit web application with interactive dashboard
- **Databases**: 
  - MongoDB Atlas (student profiles, skills, notes)
  - MySQL (structured student data, courses, enrollments)

## 📁 Project Structure

```
student-management-project/
├── backend/
│   ├── app.py                 # Flask API server
│   ├── connection.py          # Database connection utilities
│   ├── requirements.txt       # Backend dependencies
│   └── .env                   # Environment variables
├── frontend/
│   ├── streamlit_app.py       # Streamlit dashboard
│   └── requirements.txt       # Frontend dependencies
└── sql/
    └── create_sql_schema.sql   # MySQL database schema
```

## 🔧 Prerequisites

Before starting, ensure you have the following installed:

- **Python 3.8+** ([Download here](https://www.python.org/downloads/))
- **MySQL Server** ([Download here](https://dev.mysql.com/downloads/mysql/))
- **Git** (for cloning the repository)
- **MongoDB Atlas Account** (free tier available at [mongodb.com](https://www.mongodb.com/))

## 📦 Installation Steps

### 1. Clone the Repository

```powershell
git clone <repository-url>
cd student-management-project
```

### 2. Database Setup

#### MySQL Setup
1. **Install and start MySQL server**
2. **Create the database and tables**:
   ```powershell
   mysql -u root -p < sql/create_sql_schema.sql
   ```
   Or manually run the SQL commands in your MySQL client.

#### MongoDB Atlas Setup
1. **Create a free MongoDB Atlas account** at [mongodb.com](https://www.mongodb.com/)
2. **Create a new cluster**
3. **Get your connection string** from the "Connect" button
4. **Whitelist your IP address** in Network Access
5. **Create a database user** in Database Access

### 3. Environment Configuration

1. **Navigate to the backend directory**:
   ```powershell
   cd backend
   ```

2. **Create a `.env` file** with your database credentials:
   ```env
   MONGO_URI=mongodb+srv://username:password@cluster0.xxxxx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0
   MYSQL_HOST=localhost
   MYSQL_USER=root
   MYSQL_PASS=your_mysql_password
   MYSQL_DB=student_management
   ```

   > ⚠️ **Important**: Replace the placeholder values with your actual database credentials.

### 4. Backend Setup

1. **Create a Python virtual environment**:
   ```powershell
   python -m venv venv
   venv\Scripts\activate
   ```

2. **Install backend dependencies**:
   ```powershell
   pip install -r requirements.txt
   ```

### 5. Frontend Setup

1. **Open a new PowerShell terminal** and navigate to the frontend directory:
   ```powershell
   cd frontend
   ```

2. **Create and activate virtual environment** (if not using the same one):
   ```powershell
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install frontend dependencies**:
   ```powershell
   pip install -r requirements.txt
   ```

## 🚀 Running the Application

### Method 1: Using Separate Terminals

#### Terminal 1 - Backend API Server
```powershell
cd backend
venv\Scripts\activate  # If not already activated
python app.py
```
The backend API will start on `http://127.0.0.1:5000`

#### Terminal 2 - Frontend Dashboard
```powershell
cd frontend
venv\Scripts\activate  # If not already activated
streamlit run streamlit_app.py
```
The frontend will start on `http://localhost:8501`

### Method 2: Quick Start Script

Create a `start.ps1` file in the project root:

```powershell
# Start backend in background
Start-Process powershell -ArgumentList "-Command", "cd backend; venv\Scripts\activate; python app.py"

# Wait a moment for backend to start
Start-Sleep -Seconds 3

# Start frontend
cd frontend
venv\Scripts\activate
streamlit run streamlit_app.py
```

Then run:
```powershell
.\start.ps1
```

## 🌟 Features

### Current Features
- ✅ **Add Students**: Create student records with personal info and skills
- ✅ **List Students**: View all students from both databases
- ✅ **Add Notes**: Attach notes to student profiles in MongoDB
- ✅ **Dual Database**: Structured data in MySQL, flexible data in MongoDB

### API Endpoints
- `GET /health` - Health check
- `POST /student` - Add new student
- `GET /students` - List all students
- `POST /student/<id>/note` - Add note to student

## 🔍 Usage Guide

1. **Open your browser** and go to `http://localhost:8501`
2. **Use the sidebar menu** to navigate between features:
   - **Add Student**: Fill in student details and skills
   - **List Students**: View all students from both databases
   - **Add Note**: Add notes to existing students

## 🛠️ Troubleshooting

### Common Issues

#### Backend won't start
- ✅ Check if MySQL server is running
- ✅ Verify `.env` file has correct database credentials
- ✅ Ensure MongoDB Atlas IP whitelist includes your IP
- ✅ Check if port 5000 is already in use

#### Frontend can't connect to backend
- ✅ Ensure backend is running on `http://127.0.0.1:5000`
- ✅ Check firewall settings
- ✅ Verify API_BASE URL in `streamlit_app.py`

#### Database connection errors
- ✅ Test MySQL connection: `mysql -u root -p`
- ✅ Test MongoDB connection string in MongoDB Compass
- ✅ Check database names match in code and actual databases

### Testing Database Connections

#### Test MySQL:
```powershell
mysql -u root -p -e "SELECT 'MySQL Connection Successful';"
```

#### Test MongoDB:
Use MongoDB Compass or the connection string directly.

## 📝 Development Notes

- **Backend runs on port 5000** (Flask default)
- **Frontend runs on port 8501** (Streamlit default)
- **Environment variables** are loaded from `.env` file
- **CORS** is not configured (frontend and backend should run on same machine)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is for educational purposes and demonstration of hybrid database architecture.

---

**Need Help?** Check the troubleshooting section above or create an issue in the repository.
