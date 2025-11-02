# 🗺️ U.S. States Guessing Game

A fun and interactive Python game that tests your knowledge of all **50 U.S. States**!  
Built using the **turtle** graphics library and **pandas**, this project displays a blank U.S. map and lets players guess state names — marking them directly on the map as they go.

---

## 🎯 Game Objective

Guess as many U.S. states as you can!  
For every correct answer, the state name appears at the correct location on the map.  
When you’re done, type **"Exit"** to see which states you missed — they’ll be saved to a `states_to_learn.csv` file for you to study later.

---

## 🧩 Features

✅ Interactive GUI built using **Turtle Graphics**  
✅ Data-driven using **Pandas**  
✅ Automatically tracks correct and missed states  
✅ Saves unguessed states for review  
✅ Educational, visual, and beginner-friendly  

---

## 🗂️ Project Structure

```
USStatesGame/
│
├── 50_states.csv # Data file containing state names and their map coordinates
├── blank_states_img.gif # Map image used as the game background
├── main.py # Main game logic script
├── states_to_learn.csv # (Auto-generated) List of states the user missed
└── README.md # Project documentation
```

---

## ⚙️ How to Run the Game

### 1️⃣ Prerequisites
Make sure you have Python 3 installed.  
You’ll also need the following Python libraries:
```bash
pip install pandas

(turtle comes pre-installed with Python.)

```

### 2️⃣ Run the Script
From your terminal or IDE, run:
```bash
python main.py
```

The game window will open showing a blank U.S. map.

### 3️⃣ Play the Game!

- Enter a U.S. state name in the pop-up box.
- Correct guesses appear on the map.
- Type Exit anytime to quit and save the remaining states to states_to_learn.csv.

---

## 🧠 Example Walkthrough

Prompt Example:

```
0/50 States Correct
What's another state's name?
```

You enter: Texas
→ “Texas” is displayed on the map at its correct location.
→ Title updates to 1/50 States Correct.

If you quit:
```
Exit
```

A new file states_to_learn.csv is created containing all unguessed states.

---

### 🗃️ Data File Format (50_states.csv)

|state|x|y|
|--|--|--|
|Alabama|139|-77|
|Alaska|-204|-170|
|Arizona|-200|-40|

The x and y values correspond to coordinates on the map where the state name will be displayed.

---

## 💡 Key Learnings

- 🐍 Using Pandas to load and manipulate CSV data
- 🖼️ Using Turtle Graphics for interactive GUIs
- 🔤 Handling user input dynamically
- 💾 Writing data to CSV for progress tracking

---

## 🙌 Credits

Inspired by Dr. Angela Yu’s Python Bootcamp Project (Day 25: U.S. States Game).
Recreated and learned by Baji Pathan to strengthen Python data handling and visualization skills.

---

## 📜 License

This project is open for educational and learning purposes.
Feel free to fork and experiment with different color palettes or grid sizes!
