# 🧩 Quizzler – Python Quiz App

A fun and interactive **True/False quiz application** built with **Python, Tkinter, and OOP principles**, fetching live trivia questions via the **Open Trivia DB API**.  

Test your knowledge on computer science and get instant feedback with a clean and responsive GUI.

---

## 🚀 Features

- 🧠 **Dynamic Questions** — Fetches random True/False questions via API.  
- 🧩 **Object-Oriented Design** — Uses classes to structure question data and quiz logic.  
- 🎨 **Graphical User Interface** — Built with Tkinter for an interactive experience.  
- ✅ **Instant Feedback** — Shows green/red screen feedback for correct/incorrect answers.  
- 📊 **Score Tracking** — Displays your running score throughout the quiz.

---

## 🧠 Tech Stack

- **Python 3**
- **Tkinter** — For GUI
- **Requests** — For API calls
- **OOP Concepts** — Encapsulation, modular classes, and data handling

---

## 📂 Project Structure

```bash
QuizzlerApp/
│
├── main.py # Entry point – connects all modules
├── data.py # Fetches questions from the API
├── question_model.py # Defines the Question class
├── quiz_brain.py # Manages quiz logic and score
├── ui.py # Builds and handles the Tkinter interface
├── images/ # Contains 'true.png' and 'false.png' buttons
└── README.md # Project documentation
```


---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

### 2️⃣ Install Dependencies
```pip install requests```

### 3️⃣ Run the Application
```python main.py```

---

## 🖼️ UI Overview

- 🧾 A question appears on the white card.
- 🔘 Two buttons for True and False responses.
- 💬 Immediate color feedback:
- 🟩 Green = Correct
- 🟥 Red = Incorrect
- 📈 Score displayed at the top.

---

## 🧩 Example API Data

Fetched from Open Trivia DB:
```json
{
  "category": "Science: Computers",
  "type": "boolean",
  "difficulty": "easy",
  "question": "Linus Torvalds created Linux and Git.",
  "correct_answer": "True"
}
```

---

## 🧱 Key Concepts Demonstrated
|Concept    |Description|
|--         |--         |
|OOP (Object-Oriented Programming)|	Classes: Question, QuizBrain, and QuizInterface|
|API Integration|	Fetches quiz data dynamically via requests|
|Tkinter GUI|	Canvas, labels, and buttons for interactive layout|
|Event Handling|	Button click events trigger real-time responses|
|Encapsulation|	Logic separated cleanly across different modules|

---

## 🙌 Credits

Project inspired by Python 100 Days of Code Bootcamp by Angela Yu.
Created as part of Python learning projects.

---

## 📜 License

This project is open for educational and learning purposes.
Feel free to fork and experiment.