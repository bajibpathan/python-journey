# 🔐 PyPassword Generator

A simple yet effective **Password Generator** built in Python. This project helps you create secure passwords with a mix of **letters**, **numbers**, and **symbols**, ensuring stronger protection for your accounts.

---

## 🚀 Features

- User-defined password strength:
  - Choose the number of letters
  - Choose the number of symbols
  - Choose the number of numbers
- Generates a **randomized strong password**.
- Option to view a simpler password sequence (non-shuffled).
- Lightweight and beginner-friendly.

---

## 📂 Project Structure

```

password-generator/
│── password_generator.py   # Main Python script with comments
│── README.md               # Project documentation

```

---

## ⚙️ How It Works

1. The program asks the user:
   - How many letters to include.
   - How many symbols to include.
   - How many numbers to include.
2. It randomly selects characters from each category.
3. The characters are shuffled to improve security.
4. A strong password is displayed.

---

## ▶️ Usage

Run the script using Python:


```bash
python password_generator.py

Example interaction:

Welcome to the PyPassword Generator!
How many letters would you like in your password?
5
How many symbols would you like?
3
How many numbers would you like?
2
Strong Password: aR5#y%N8$
```
---

## 📘 What I Learned

* **Python Basics**

  * Using `lists` and `strings`.
  * Taking **user input** with `input()`.
* **Random Module**

  * `random.choice()` for selecting random elements.
  * `random.shuffle()` for mixing the list.
* **Password Security**

  * Importance of mixing letters, numbers, and symbols.
  * Why shuffling increases password strength.
* **Project Skills**

  * Writing **clean, commented code**.
  * Structuring a small Python project with a README.

---

## 🙌 Credits

This project is part of the **100 Days of Code: Python Pro Bootcamp** by *Dr. Angela Yu* on Udemy.

Special thanks to the course for inspiring this project.



