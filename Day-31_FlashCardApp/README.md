# 🧠 Flashcard Learning App (Python)

A simple **Flashcard Learning App** built with **Tkinter** and **Pandas**, designed to help users learn French words efficiently through spaced repetition.

---

## 🚀 Features

- 🎴 **Interactive Flashcards** – Learn French words with automatic card flipping.
- 🔄 **Smart Progress Tracking** – The app remembers which words you already know.
- 🧩 **Data Persistence** – Progress is saved automatically in a `words_to_learn.csv` file.
- ⏳ **Auto Flip Timer** – Cards flip automatically to show translations after 3 seconds.
- ✅ **Minimal & User-Friendly UI** – Clean design for distraction-free learning.

---

## 🛠️ Tech Stack

- **Python 3**
- **Tkinter** (for GUI)
- **Pandas** (for data handling)
- **Random** (for word shuffling)

---

## 📂 Project Structure

```
FlashcardApp/
│
├── data/
│ ├── french_words.csv # Original word dataset (French to English)
│ ├── words_to_learn.csv # User's progress (auto-generated)
│
├── images/
│ ├── card_front.png # Flashcard front design
│ ├── card_back.png # Flashcard back design
│ ├── right.png # "Known" button image
│ ├── wrong.png # "Unknown" button image
│
├── main.py # Application main script
└── README.md # Project documentation
```

---

## 🧩 How It Works

1. The app loads a list of French-English word pairs.
2. Displays one French word at a time.
3. After 3 seconds, flips the card to show the English translation.
4. Click ✅ if you know the word — it will be removed from your learning list.
5. Click ❌ if you want to keep practicing that word.
6. Progress is saved automatically in `data/words_to_learn.csv`.

---

## 💡 Example

| French  | English |
| :------ | :------ |
| Bonjour | Hello   |
| Chat    | Cat     |
| Maison  | House   |

---

## ⚙️ Installation & Setup

1. Install required dependencies:

   ```bash
   pip install pandas
   ```

2. Run the app:
   ```bash
   python main.py
   ```

---

## 🧠 Learning Logic

- Words you mark as known are removed from the list.
- Remaining words are saved to words_to_learn.csv.
- When you restart the app, it resumes where you left off.

---

## 🙌 Credits

Project inspired by Python 100 Days of Code Bootcamp by Angela Yu.
Created as part of Python learning projects.

---

## 📜 License

This project is open for educational and learning purposes.
Feel free to fork and experiment.
