# 🧠 Quiz Application (Python)

## 📌 Description
This project is a **command-line based Quiz Application** built using Python.  
It loads multiple-choice questions from a CSV dataset and allows users to attempt quizzes in different game modes such as timed quiz, fast challenge, sudden death, and progressive scoring mode.

The project focuses on handling datasets, implementing game logic, managing timers, and building interactive CLI applications.

## 🚀 Features
- Load quiz questions from CSV dataset
- Randomized question order
- Multiple quiz modes:
  - Simple Quiz Mode
  - Fast Challenge Mode (2-minute unlimited questions)
  - Timed Mode (30 questions / 30 minutes)
  - Sudden Death Mode (Game ends on first wrong answer)
  - Progressive Reward Mode (Increasing score for streaks)
- Score tracking for each mode
- Menu-driven interface
- Option to exit quiz anytime

## 🛠️ Technologies Used
- Python 3
- Built-in `csv` module
- Built-in `random` module
- Built-in `time` module
- Built-in `os` module

## 🐍 Python Concepts Used
- File handling using CSV
- Dictionaries and list of dictionaries
- Functions and modular programming
- Loops and conditional statements
- Randomization using `random.shuffle()`
- Time-based execution using `time.time()`
- Menu-driven program design
- Input validation and control flow
- Global variables
- Exception-safe dataset loading

## 🧠 New Things Learned
- How to read structured datasets using CSV
- Designing multiple game modes in one application
- Implementing timer-based logic in Python
- Managing scoring systems for different rules
- Creating reusable quiz engine logic
- Building interactive CLI-based game applications
- Handling real dataset formatting issues (encoding, delimiters)

## 🔮 Future Improvements
- Add leaderboard and score history
- Shuffle options along with questions
- Add difficulty levels
- Add GUI using Tkinter or Web version using Flask
- Add database storage instead of CSV
- Add question category filtering
