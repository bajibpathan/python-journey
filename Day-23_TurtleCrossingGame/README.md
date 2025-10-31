# 🐢 Turtle Crossing Game

A fun and challenging arcade-style **Turtle Crossing Game** built using Python’s `turtle` graphics module.  
The goal is simple help the turtle cross a busy road while avoiding colorful, fast-moving cars!

---

## 🎮 Game Objective

Move the turtle 🐢 from the bottom to the top of the screen without colliding with any cars.  
Each successful crossing increases the level and makes the cars move faster 🚗💨!

---

## 🧩 Features

- Player-controlled turtle using the **Up Arrow** key  
- Randomly generated colorful cars for variety  
- Increasing difficulty with each level  
- Simple yet addictive gameplay  
- Real-time level tracking and **Game Over** message on collision  

---

## 🕹️ Controls

| Action | Key |
|--------|-----|
| Move Up | ⬆️ Up Arrow |

---

## 🧠 Key Learnings

This project helped me understand and apply:
- **Object-Oriented Programming (OOP)** concepts in Python  
- **Class relationships** between `Player`, `CarManager`, and `Scoreboard`  
- **Collision detection** using distances between Turtle objects  
- **Game loop design** with controlled frame rates using `time.sleep()`  
- Managing **dynamic difficulty** by incrementing speed per level  

---

## 📂 Project Structure

```
TurtleCrossingGame/
│
├── main.py # Main game loop and screen setup
├── player.py # Player (turtle) movement logic
├── car_manager.py # Car generation, movement, and level speed logic
├── scoreboard.py # Level display and game-over logic
└── README.md # Project documentation

```

---

## 💡 How to Run

1. Make sure you have **Python 3.x** installed.  
2. Clone this repository or download the files.  
3. Run the game using:

   ```bash
   python main.py
   ```
4. Use the Up Arrow key to move your turtle forward.
5. Avoid cars, reach the top, and see how many levels you can complete!

---

## 🏁 Game Rules

- 🚗 If a car hits your turtle → Game Over!
- 🐢 Each time you cross successfully → You advance a level.
- ⚡ With every new level → Cars move faster!

---

## 🙌 Credits

This project was inspired by Dr. Angela Yu’s “100 Days of Python” Bootcamp on Udemy.
I learned, re-created, and enhanced it for practice and deeper understanding of OOP and game design.

---

## 📜 License

This project is open for educational and learning purposes.
Feel free to fork and experiment with different color palettes or grid sizes!
