# 📚 Library Management System (Python)

## 📌 Description
This project is a **command-line based Library Management System** developed using Python.  
It allows users to manage books in a library by adding new books, viewing available books, issuing and returning books, and tracking issued books.  
All data is stored persistently using a JSON file, making the system suitable for learning real-world data management concepts.

## 🚀 Features
- Add new books with unique book IDs
- View all available books with details
- Issue books and reduce available copies
- Return books and update availability
- View issued books per title
- View total number of books issued
- Persistent storage using a JSON file
- Menu-driven user interface

## 🛠️ Technologies Used
- Python 3
- Built-in `json` module
- Built-in `os` module
- JSON file storage (`library.json`)

## 🐍 Python Concepts Used
- Dictionaries and nested dictionaries
- File handling with JSON (`json.load`, `json.dump`)
- `os.path.exists()` for file validation
- Exception handling (`try` / `except`)
- Functions and modular programming
- Loops (`while`, `for`)
- Conditional statements
- Arithmetic operations for tracking issued books
- Global variables
- `__main__` entry point

## 🧠 New Things Learned
- Designing a real-world management system using Python
- Handling structured data with multiple attributes
- Maintaining and updating application state
- Implementing business logic (issue/return constraints)
- Preventing invalid operations using condition checks
- Tracking derived data (issued books) dynamically
- Writing scalable menu-driven programs

## 🔮 Future Improvements
- Add user/member management
- Implement book search functionality
- Add due dates and fine calculation
- Improve input validation and error handling
- Convert the project to an OOP-based design
- Add role-based access (admin/user)
