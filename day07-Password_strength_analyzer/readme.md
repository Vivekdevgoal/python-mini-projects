# 🔐 Password Strength Checker (Python)

## 📌 Description
This project is a **command-line based Password Strength Checker** built using Python.  
It analyzes a given password based on length, character variety, and common security patterns to determine its overall strength.  
The application also provides detailed feedback on weaknesses and suggestions to improve password security.

## 🚀 Features
- Password strength scoring system (0–100)
- Classification of passwords (Weak, Moderate, Strong, Very Strong)
- Length-based strength analysis
- Character variety checks (uppercase, lowercase, digits, special characters)
- Detection of weak patterns:
  - Sequential characters (abc, 123)
  - Repeated characters (aaa, 111)
  - Keyboard patterns (qwerty, asdf)
  - Common dictionary passwords
- Detailed issue reporting
- Actionable suggestions to improve password strength

## 🛠️ Technologies Used
- Python 3
- Standard Python libraries

## 🐍 Python Concepts Used
- Functions and modular programming
- Dictionaries for scoring and penalties
- String processing and pattern detection
- Conditional logic and loops
- Sets and frequency analysis
- Character encoding using `ord()`
- Algorithmic problem solving
- CLI-based user interaction
- Aggregation of multiple evaluation metrics

## 🧠 New Things Learned
- How real-world password strength systems work
- Designing weighted scoring mechanisms
- Detecting sequential and keyboard patterns
- Improving application security through validation
- Writing reusable and testable analysis functions
- Combining multiple evaluation strategies into one final score

## 🔮 Future Improvements
- Add entropy-based password analysis
- Support batch password testing from files
- Mask password input for security
- Add GUI or web-based interface
- Export password analysis report
