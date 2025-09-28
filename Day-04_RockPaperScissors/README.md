# Rock Paper Scissors 🎮✊✋✌️

A simple Python implementation of the classic **Rock, Paper, Scissors** game where you play against the computer.

---
## 🎮 Gameplay 

- Choose **Rock (0)**, **Paper (1)**, or **Scissors (2)**. 
- The computer randomly makes a choice. 
- The game compares choices and prints whether you **win, lose, or draw**. 
- ASCII art is displayed to make the game more fun and interactive. 

**Rules:**
- Rock beats Scissors 
- Scissors beats Paper 
- Paper beats Rock

---
## 🚀 How to Run 

1. Clone this repository: 
```bash 
git clone https://github.com/your-username/rock-paper-scissors.git
```
2. Navigate into the project folder:
```cd rock-paper-scissors```

3. Run the Python script:
```python rock_paper_scissors.py```

Make sure you have Python 3.x installed on your system.

---
## 📂 Project Structure

rock-paper-scissors/ 
│── rock_paper_scissors.py # Main Python game file 
│── README.md # Project documentation

---
## ✨ Features
- Interactive text-based gameplay
- ASCII art for Rock, Paper, and Scissors
- Random computer choice for fairness
- Beginner-friendly Python project

## 📘 What I Learned

From this project, I practiced and understood:

- Conditional Statements
    - if conditions → checking player choices
    - if / else → handling win/lose/draw outcomes
- Nested Conditions
    - Used for special cases (e.g., Rock vs Scissors logic)
- Logical Operators
    - To validate input and compare multiple conditions
- Lists
    - Storing ASCII art for Rock, Paper, Scissors in a single list for easy access
    - Example:
        game_images = [rock, paper, scissors]

- Nested Lists (conceptual extension)
    - While this project uses a single list, I learned how nested lists can be used for:
    -   Storing win/lose conditions in a structured way
    - Example idea:
        outcomes = [
            ["Draw", "Lose", "Win"],   # Rock outcomes
            ["Win", "Draw", "Lose"],   # Paper outcomes
            ["Lose", "Win", "Draw"]    # Scissors outcomes
        ]
        print(outcomes[user_choice][computer_choice])

## 🙏 Credits

This project is part of Dr. Angela Yu’s 100 Days of Code: The Complete Python Pro Bootcamp on Udemy.
Thanks to Dr. Angela Yu for creating this beginner-friendly game project and making coding fun.

## 📜 License

This project is for educational purposes.
Feel free to modify and extend the game with new features, but please give credit if sharing publicly.