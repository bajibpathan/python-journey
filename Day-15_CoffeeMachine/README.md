# ☕ Coffee Machine Project — Python Simulation

A beginner-friendly Python project that **simulates a real-world coffee machine**.  
It handles orders, processes payments using coins, manages ingredient resources, and serves coffee with change.  

---

## 🎯 Project Overview

The Coffee Machine project allows users to:
- Select a drink (espresso, latte, or cappuccino)
- Insert coins for payment
- Receive their coffee if enough resources and funds are available

The machine:
- Tracks and reports remaining resources
- Calculates profit
- Provides change when applicable

---

## ⚙️ How It Works

### 1. **Menu Configuration**
The `MENU` dictionary defines each drink’s:
- Required **ingredients**
- Associated **cost**

### 2. **User Input**
Prompts the user to:
- Choose a drink type
- Insert coins
- Continue or turn off the machine

### 3. **Core Functionalities**
| Function | Purpose |
|-----------|----------|
| `is_resource_sufficient()` | Checks if there are enough ingredients for the selected drink |
| `process_coins()` | Collects and totals coin input from the user |
| `is_transaction_successful()` | Validates if payment is sufficient and calculates change |
| `make_coffee()` | Deducts resources and simulates serving the drink |

---

## 🧠 Example Game Flow
```
What would you like? (espresso/latte/cappuccino): latte
Please insert coins.
How many quarters?: 10
How many dimes?: 0
How many nickles?: 0
How many pennies?: 0
Here is $0.0 in change.
Here is your latte ☕️. Enjoy!
```

---
## 💰 Machine Reports

You can type `report` anytime to see remaining ingredients and profits:
```
Water: 200ml
Milk: 50ml
Coffee: 76g
Money: $4.0
```
Type `off` to stop the machine.

---

## 🧩 Concepts Practiced

- Functions and modular programming  
- Dictionaries and nested data structures  
- Global vs. local scope  
- Control flow (loops, conditionals)  
- Simulating real-world transactions  

---

## 🚀 How to Run the Project

1. Clone this repository:
   ```bash
   git clone https://github.com/<your-username>/coffee-machine.git
   ```
2. Navigate into the project directory:
    ```bash
    cd coffee-machine
    ```
3. Run the program:
    ```bash
    python main.py
    ```


---

## 🧰 Files Included
|File Name|	Description|
|--|--|
|main.py|	Main program logic|
|README.md|	Documentation file|

---
## 🧑‍💻 What I Learned

Through this project, I learned:
- How to manage resources dynamically
- How to simulate money transactions
- How to use nested dictionaries effectively
- The importance of function reusability and readability

--- 

## 🙏 Credits

This project is part of Dr. Angela Yu’s 100 Days of Python Coding Bootcamp (Udemy Course).
All educational credit goes to her amazing teaching approach.

---
## 📜 License

This project is for educational purposes. Feel free to use or modify it for your own learning or projects.

---