# 🍅 Pomodoro Timer

A simple and elegant **Pomodoro Timer** built with Python’s **Tkinter GUI**.  
This productivity tool helps manage work sessions and breaks using the Pomodoro technique.

---

## ⏱️ What is the Pomodoro Technique?

The **Pomodoro Technique** is a time management method that breaks work into intervals:
- **25 minutes** of focused work
- **5-minute** short breaks
- After every **4 sessions**, take a **20-minute long break**

---

## 🚀 Features

✅ Automatic work/break switching  
✅ Long break after every 4 Pomodoros  
✅ Reset button to restart sessions anytime  
✅ Visual checkmarks for completed work sessions  
✅ Clean, minimal GUI using **Tkinter**

---

## 🧱 Project Structure

```
PomodoroTimer/
│
├── main.py # Core application file
├── tomato.png # Tomato image used in GUI
└── README.md # Project documentation
```


---

## 💡 How It Works

1. Click the **Start** button to begin the timer.
2. The app alternates between **Work** and **Break** sessions automatically.
3. Each completed work session adds a ✔ checkmark below the timer.
4. Click **Reset** to stop and restart the timer.

---

## 🖥️ Requirements

- Python 3.x  
- Tkinter (comes pre-installed with Python)  
- `tomato.png` image file in the same directory

---

## ▶️ Run the App

1. Run the script:
    ```bash
        python main.py
    ```

---

## 📸 Example Output

```bash
    Work Session → 25:00 countdown
    Break Session → 05:00 countdown
    ✔ ✔ (after each completed work cycle)
```

---

## 🧠 Learning Highlights

- Tkinter GUI layout and event handling
- Countdown logic with after() and recursion
- Dynamic label and canvas updates
- State management between multiple work/break sessions

---

## 🙌 Credits

Project inspired by Python 100 Days of Code Bootcamp by Angela Yu.
Created as part of Python learning projects.

---

## 📜 License

This project is open for educational and learning purposes.
Feel free to fork and experiment.

