# 🛡️ Password Security & Generation Tool

A Python-based command-line tool for password strength analysis, entropy calculation, and secure password generation, developed following software quality practices including automated testing and code quality tools.


## 🚀 Features

- **Password Strength Analysis**  
  Evaluates the robustness of a password by checking multiple security criteria such as length, lowercase and uppercase letters, numbers, special characters, and  overall complexity. The tool also provides feedback on detected weaknesses and suggests which security requirements are missing.
- **Entropy Calculation**  
  Estimates password unpredictability by computing entropy in bits using the formula `E = L · log₂(R)`.
- **Common Password Detection**  
  Checks whether a password appears in a local database of commonly used or leaked passwords.
- **Secure Password Generation**  
  Generates cryptographically secure passwords using Python’s `secrets` module with configurable length and character sets.
- **Visual Strength Indicator**  
  Displays a graphical strength bar to give immediate feedback on password security.
- **JSON Report Generation**  
  Allows exporting the results of the password analysis into a structured JSON report.

# Struttura del progetto
## 📁 Project Structure

```text
project/
│
├── src/
│   └── checker.py              # Core password analysis and generation logic
│
├── tests/
│   └── test_checker.py         # Unit tests implemented with pytest
│
├── data/
│   └── common_passwords.txt    # List of common passwords used for security checks
│
├── main.py                     # Command-line interface of the application
│
├── requirements-dev.txt        # Development dependencies (testing, linting, formatting)
│
└── README.md                   # Project documentation
```

---

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Peppescx/password-strength-checker
   cd password-strength-checker

2. **Setup the environment:**
   
   This project uses only the Python Standard Library for its core logic, so no external production dependencies are required. Ensure you have Python 3.8+           installed. For development, testing and code quality checks, install:
   ```bash
   pip install -r requirements_dev.txt

4. **Run the program**
   Execute the main script:
    ```bash
   python main.py
    ```
    You will see the interactive menu:
    ```bash
    === Security Tool v2.0 ===
    1. Analyze a password
    2. Generate a secure password
    3. Exit

## 👨‍💻 Author

Progetto universitario sviluppato da Giuseppe Scrofano e Lorenzo La Rocca per il corso QD 2025/2026 — Università degli Studi di Catania.


