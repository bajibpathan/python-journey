
# 🤖 Reeborg's World Maze Solver

This project provides a solution to the **Reeborg's World Maze Puzzle** using Python-style commands. It demonstrates the use of a **right-hand rule algorithm** to navigate mazes and reach the goal.

---

## 🚀 Features

- Uses a **helper function** (`turn_right`) to simplify code.
- Follows the **right-hand rule** to systematically solve the maze.
- Works in the **Reeborg’s World** online environment.
- Demonstrates a clean and logical approach to problem-solving.

---

## 📂 Project Structure

```

reeborg-maze-solver/
│── maze_solver.py   # Python-style solution with comments
│── README.md        # Project documentation

```

---

## ⚙️ How It Works

1. The program first moves forward until it encounters a wall.
2. Then, it follows these rules until reaching the goal:
   - If the right side is clear → turn right and move.
   - Else if the front is clear → move forward.
   - Else → turn left.
3. This process continues until the robot successfully reaches the goal.

This algorithm is a classic **right-hand wall-following maze solver**.

---

## ▶️ Usage

1. Open [Reeborg's World](https://reeborg.ca/reeborg.html).
2. Load a maze world (e.g., "Maze").
3. Copy and paste the code from `maze_solver.py` into the editor.
4. Run the program to watch Reeborg solve the maze.

---

## 📘 What I Learned

- **Programming Fundamentals**
  - Defining and reusing functions.
  - Loops and conditional logic.
- **Maze Solving Algorithms**
  - Right-hand rule technique for maze navigation.
- **Problem Solving**
  - Breaking down a problem into smaller, reusable parts.
  - Using helper functions (`turn_right`) to make code readable.

---

## 🙌 Credits

This project was inspired by the **100 Days of Code: Python Pro Bootcamp** by *Dr. Angela Yu* on Udemy, where solving Reeborg’s World puzzles is part of early programming exercises.

---

