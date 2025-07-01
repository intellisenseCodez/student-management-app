# Student Management System 🎓

A Python CLI application for managing student records, built with SQLite.

## Features ✨
- ✅ Add new students  
- 🔍 View all students  
- 📝 Update student records  
- ❌ Delete students  
- 💾 Persistent database storage  

## Prerequisites
- Python 3.9+  
- Docker (optional, for containerized usage)

---

## Installation

### Method 1: Run directly with Python

```bash
# Clone the repository
git clone https://github.com/intellisenseCodez/student-management-app.git
cd student-management-app

# Run the application
python3 app/app.py
```

## Method 2: Run with Docker 🐳
- Build Docker Image

```bash
docker build -t student-cli-app .
```

- Run the CLI App in Interactive Mode
```bash
docker run -it --rm student-cli-app
```

Note: The `-it` flag enables interaction so you can use the `input()` prompts.

- To Persist the Database File (Optional)
```bash
docker run -it --rm -v $(pwd)/student.db:/src/app/student.db student-cli-app
```

This ensures your data is saved even after the container stops.


## For Class Purpose 👩‍🎓👨‍🎓
- Use this app to teach:
- Basic CRUD operations
- SQLite usage in Python
- Docker fundamentals

## Contributors
Oyekanmi Lekan

