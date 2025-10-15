# 🧠 Quiz Brain – Python Quiz Game

A fun and interactive **True/False quiz game** built in Python that tests your general knowledge of computer science facts.  
This project demonstrates **Object-Oriented Programming (OOP)** principles like encapsulation, modular design, and data-driven question loading.

---

## 🚀 Features

- ✅ Object-Oriented structure with reusable classes (`Question`, `QuizBrain`)
- 📚 Data-driven questions loaded from `data.py`
- 🧩 Interactive console interface
- 📈 Real-time score tracking
- 🧠 Simple True/False quiz format for easy learning

---

## 🗂️ Project Structure

```
QuizBrain/
│
├── main.py # Entry point – controls quiz flow
├── quiz_brain.py # Handles quiz logic and scoring
├── quiz_model.py # Defines the Question class
├── data.py # Contains quiz questions
└── README.md # Project documentation
```


---

## 🧩 How It Works

1. Each question is stored as a dictionary in `data.py`.
2. The `Question` class models each question with its text and correct answer.
3. The `QuizBrain` class manages:
   - Asking questions  
   - Checking answers  
   - Updating scores  
4. The `main.py` file ties everything together and runs the quiz loop until all questions are completed.

---

## 🧠 Example Run

```
Q.1: The Windows ME operating system was released in the year 2000. (True/False): true
✅ You got it right!
Your current score is: 1 / 1

Q.2: The programming language 'Python' is based off a modified version of 'JavaScript'. (True/False): false
✅ You got it right!
Your current score is: 2 / 2

```

---

## 💡 Concepts Learned

- Object-Oriented Programming (OOP)
  - Classes & Objects
  - Methods and Attributes
- Data Structures (Lists, Dictionaries)
- User Input & Validation
- Program Flow Control (loops and conditions)

---

## 🧭 How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/<your-username>/quiz-brain.git
   cd quiz-brain
   ```
2. Run the game:
    ```bash
    python main.py
    ```

---
## 🙏 Credits

This project was inspired and developed as part of the **"100 Days of Code – The Complete Python Pro Bootcamp"** by Dr. Angela Yu on Udemy.

---
## 📜 License

This project is for educational purposes. Feel free to use or modify it for your own learning or projects.

---