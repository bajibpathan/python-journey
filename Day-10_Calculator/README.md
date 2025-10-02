# 🧮 Calculator Project

A simple **console-based calculator** built in Python that supports continuous calculations.  
Users can add, subtract, multiply, divide, and even continue calculations using the result of the previous operation.

---

## 🚀 Features
- Supports **Addition (+)**, **Subtraction (-)**, **Multiplication (*)**, and **Division (/)**.
- Allows **chained calculations** (continue with previous result).
- Provides options to:
  - Continue with current result
  - Start a new calculation
  - Quit the program
- Uses an ASCII art logo for a better user experience.

---

## 🖥️ How It Works
1. The calculator displays available operations.
2. User selects an operation and enters numbers.
3. Result is displayed.
4. User chooses:
   - **'y'** → Continue calculating with result
   - **'n'** → Start a new calculation
   - **'q'** → Quit the calculator

---

## 📂 Project Structure
```
Calculator/
│── art.py # Contains ASCII logo
│── main.py # Main calculator logic
│── README.md # Documentation

```
---

## 🧑‍💻 Example Run
```
What's the first number?: 10
+
/
Pick an operation: +
What's the next number?: 5
10.0 + 5.0 = 15.0
Type 'y' to continue calculating with 15.0, or type 'n' to start a new calculation, or 'q' to quit: y
+

/
Pick an operation: *
What's the next number?: 3
15.0 * 3.0 = 45.0
Type 'y' to continue calculating with 45.0, or type 'n' to start a new calculation, or 'q' to quit: q
Good Bye

```
---

## 📚 What I Learned
- Creating and using **functions** for modular code.
- Using a **dictionary of operations** to map symbols to functions.
- Implementing **loops and recursion** for continuous calculations.
- Building an **interactive command-line program**.

---

## 🙏 Credits
This project is inspired by  
**Dr. Angela Yu’s 100 Days of Python Coding Bootcamp (Udemy Course)**.  

---
## 📜 License

This project is for educational purposes. Feel free to use or modify it for your own learning or projects.

---