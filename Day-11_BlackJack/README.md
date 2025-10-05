# 🃏 Blackjack Game — Python Capstone Project

This is a fun and interactive **Blackjack game** built using Python.  
It follows standard Blackjack rules and allows the player to compete against the computer dealer.

---

## 🚀 Features
- Play multiple rounds interactively.
- Handles **Blackjack (21)**, **Ace adjustment (11 → 1)**, and **bust scenarios**.
- Computer follows dealer rules: draws until score ≥ 17.
- Clean and modular code with functions for each key operation.
- Fun ASCII art logo to enhance the game experience.

---

## 🕹️ How to Play
1. Run the program.
2. You and the computer are each dealt two cards.
3. On your turn:
   - Type **'y'** to draw another card.
   - Type **'n'** to pass and let the dealer play.
4. The dealer draws cards until their score is **17 or higher**.
5. The winner is determined based on the closest score to **21** without going over.

---

## 📚 Rules Summary
| Card Type | Value |
|------------|--------|
| Number Cards | Face value |
| Jack, Queen, King | 10 |
| Ace | 11 (can become 1 if score exceeds 21) |

**Blackjack (Ace + 10-value card)** = automatic win (score shown as `0` in code).

---

## 📂 Project Structure
```
Blackjack/
│── art.py # Contains ASCII logo
│── main.py # Main game logic
│── README.md # Project documentation
```

---

## 🧑‍💻 Example Gameplay


Do you want to play a game of Blackjack? Type 'y' or 'n': y

Your cards: [10, 6], current score: 16
Computer's first card: 8
Type 'y' to get another card, type 'n' to pass: y
Your cards: [10, 6, 5], current score: 21
Computer's final hand: [8, 9, 4], final score: 21
Draw 🙃


---

## 🧠 What I Learned
- How to use **lists and functions** effectively for modular programming.
- Applying **loops** and **conditional logic** to handle game rules.
- Handling **randomization** using the `random` module.
- Writing **reusable functions** with clear responsibilities.
- Implementing **recursion** and **loops** for continuous play.

---

## 🙏 Credits
This project is part of the  
**Dr. Angela Yu’s 100 Days of Python Coding Bootcamp (Udemy Course)**.  

---

## 📜 License

This project is for educational purposes. Feel free to use or modify it for your own learning or projects.

---