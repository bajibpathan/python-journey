# ☕ Coffee Machine Project (Object-Oriented Programming in Python)

A Python project that simulates a real-world coffee vending machine using **Object-Oriented Programming (OOP)** principles.  
It allows users to order drinks, handle payments, check available resources, and manage transactions.

---

## 🧠 Project Overview

This project models a coffee machine using three core components:

- **Menu** – Holds available drinks and their recipes.
- **CoffeeMaker** – Manages ingredients and prepares coffee.
- **MoneyMachine** – Handles coin-based transactions and tracks profit.

All components interact in the `main.py` file to simulate a real coffee-making process.

---

## 🧩 Files Structure

```bash
coffee_machine_oop/
│
├── main.py # Main program to run the coffee machine
├── coffee_maker.py # Handles coffee making and resources
├── menu.py # Defines drinks and menu items
├── money_machine.py # Handles payments and profits
└── README.md # Documentation file
```

---

## ⚙️ Features

✅ Menu-driven user interface  
✅ Resource availability check before brewing  
✅ Coin-based payment system  
✅ Automatic change calculation  
✅ Reporting for profit and available ingredients  
✅ Modular design using OOP concepts

---

## 🧠 OOP Concepts Demonstrated

- **Classes & Objects** – Representing real-world entities (`Menu`, `CoffeeMaker`, `MoneyMachine`)
- **Encapsulation** – Keeping functionality separated into different modules
- **Abstraction** – Hiding internal details while exposing user-friendly methods
- **Interaction between Objects** – Collaboration between menu, coffee maker, and money system

---

## 🧾 Example Usage

```bash
What would you like (latte/espresso/cappuccino/): latte
Please insert coins.
How many quarters?: 10
How many dimes?: 0
How many nickles?: 0
How many pennies?: 0
Here is $0.0 in change.
Here is your latte ☕️. Enjoy!
```

---

## 🧰 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/bajibpathan/coffee-machine-oop.git
   ```
2. Navigate to the folder:

```bash
cd coffee-machine-oop
```

3. Run the main program:

```bash
python3 main.py
```

---

## 📚 Key Learnings

Through this project, I learned:

- How to structure Python code using Object-Oriented Programming
- How different classes interact to simulate real-world systems
- How to handle user input, calculations, and conditional logic
- The importance of code modularity and reusability

---

## 🙏 Credits

This project is inspired by the 100 Days of Python Bootcamp by Dr. Angela Yu on Udemy.
I completed and documented it as part of my Python OOP learning journey.

---

## 📜 License

This project is for educational purposes. Feel free to use or modify it for your own learning or projects.

---
