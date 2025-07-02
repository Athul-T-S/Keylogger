# Keylogger
just keylogger

# 🔐 Python Keylogger (Educational Project)

This is a simple Python-based keylogger designed for cybersecurity students to learn about keylogging techniques in a controlled, ethical, and legal environment. It captures all keyboard inputs and stores them in a local log file. The logger runs silently and exits when `Ctrl + Shift + Q` is pressed.

## ⚠️ DISCLAIMER

> This project is for **educational purposes only**. Do **not** run or distribute this on any system without **explicit permission**. Unauthorized use of keyloggers is illegal and unethical.

## 📦 Features

- Captures all keystrokes (characters + special keys)
- Runs silently in the background
- Logs are saved to a local file
- Safe exit using `Ctrl + Shift + Q`
- Easy to compile as a `.exe` for Windows

## 🔧 Requirements

- Python 3.x
- `pynput` module

Install dependencies with:

pip install pynput

## 🚀 How to Run

### ▶️ Run as Python Script

1. Save the script as `keylogger.py`
2. Run using:

   python keylogger.py

3. To stop it, press **Ctrl + Shift + Q**

### 🛠️ Compile to EXE (Windows)

Use PyInstaller to make a standalone executable:

pip install pyinstaller  
pyinstaller --noconsole --onefile keylogger.py

After build, the `.exe` file will be inside the `dist/` folder. Run it by double-clicking.

## 📂 Output

Logs are saved in:

keylogs/log.txt

Example output:

2025-07-02 15:20:33,211: h  
2025-07-02 15:20:33,410: i  
2025-07-02 15:21:10,001: [Key.enter]

## 🛑 Exit Key

To stop the keylogger, press:

Ctrl + Shift + Q

This will safely terminate the program and write `[CTRL+SHIFT+Q detected. Exiting.]` to the log file.

## 💡 Ideas for Improvement

- 🔐 Encrypt the log file
- ☁️ Send logs to Firebase or Gmail
- ⏲️ Auto-rotate logs daily/hourly
- 🧠 Add clipboard logger
- 👀 Capture active window titles
- 🎛️ Build GUI to visualize logs

## 👨‍💻 Author

Athul TS – Cybersecurity Student

## 📜 License

This project is licensed under the MIT License.
