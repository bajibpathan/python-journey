# 🔼 Higher or Lower Game — Python Project

A fun and interactive Python game where you guess which celebrity or public figure has **more followers on social media!**  
Each correct guess increases your score — but one wrong move, and the game ends.

---

## 🎮 Game Overview

In this game:
- You’ll be shown **two famous personalities**.
- You must guess who has **more followers**.
- If your guess is right, your score increases and you continue.
- If your guess is wrong, the game ends and your final score is displayed.

---

## 🧩 How the Game Works

1. The game starts by displaying the logo (`logo` from `art.py`).
2. Two random accounts are selected from `game_data.py`.
3. Player inputs their guess:  
   👉 `'A'` or `'B'`
4. The program compares their follower counts.
5. If the guess is correct:
   - The score increases.
   - The next round begins (previous ‘B’ becomes new ‘A’).
6. If incorrect:
   - The game ends.
   - Your final score is displayed.

---

## 🧠 Key Functions

### `format_data(account)`
Formats the data from `game_data.py` into a readable string:
```python
"Cristiano Ronaldo, a footballer, from Portugal"
```
### `check_answer(user_guess, a_followers, b_followers)`

Compares follower counts and returns whether the user’s guess is correct.

---

## 🧰 Project Files

|File Name|	Description|
|--|--|
|main.py|	Main game logic|
|art.py|	Contains ASCII logos and VS graphic|
|game_data.py|	List of dictionaries with celebrity data|
|README.md|	Project documentation (this file)|

### 📦 Example Game Flow
```python
Compare A: Ariana Grande, a pop singer, from USA
vs
Against B: Dwayne Johnson, an actor and former wrestler, from USA
Who has more followers? Type 'A' or 'B': A

You're right! Current Score: 1
```

---

## 💡 What I Learned

Through this project, I learned how to:

Work with lists and dictionaries

Use functions with parameters and return values

Generate random data selections

Implement loops and conditional logic

Manage game flow and state tracking

🧑‍💻 Technologies Used

Python 3

Random module

Basic ASCII art and text-based interface

## 🚀 How to Run the Game

Clone this repository:
```
git clone https://github.com/<your-username>/higher-lower-game.git
```

Navigate to the project folder:
```
cd higher-lower-game
```

Run the program:
```
python main.py
```

---

## 🙏 Credits

This project is part of
Dr. Angela Yu’s 100 Days of Python Coding Bootcamp (Udemy Course).
All learning credits go to her structured and fun teaching style.

---
## 📜 License

This project is for educational purposes. Feel free to use or modify it for your own learning or projects.

---
