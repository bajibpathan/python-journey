
# 🎮 Hangman Game (Python)

A classic **Hangman game** built in Python. The player tries to guess the hidden word one letter at a time while avoiding running out of lives. Each wrong guess draws another part of the hangman!

---

## 🚀 Features

- Randomly selects a word from a predefined word list.
- Visual **ASCII art hangman** stages to show progress.
- Tracks number of lives (6 attempts).
- Prevents duplicate guesses with user feedback.
- Win/lose conditions with clear messages.

---

## 📂 Project Structure

```

hangman/
│── hangman.py         # Main game logic with comments
│── hangman_words.py   # List of words for the game
│── hangman_art.py     # ASCII art for hangman and logo
│── README.md          # Project documentation

```

---

## ⚙️ How It Works

1. The game displays a logo and a series of underscores representing the word.
2. The player guesses letters one by one.
   - If correct → the letter fills the blank(s).
   - If incorrect → the player loses a life and a part of the hangman is drawn.
3. The game ends when:
   - The word is fully guessed (**YOU WIN 🎉**).
   - Lives reach 0 (**YOU LOSE 💀**).

---

## ▶️ Usage

Run the game using Python:

```bash
python hangman.py


Example interaction:

****************************6/6 LIVES LEFT****************************
Guess a letter: a
Word to guess: a__le
****************************5/6 LIVES LEFT****************************
Guess a letter: z
You guessed z, that's not in the word. You lose a life.
```


---

## 📘 What I Learned

* **Python Basics**

  * Loops, conditionals, and functions.
  * Importing modules and using external files.
* **Game Logic**

  * Tracking game state (`lives`, guessed letters, game over conditions).
  * Updating the display dynamically.
* **User Experience**

  * Using ASCII art to improve engagement.
  * Giving meaningful feedback on each guess.

---

## 🙌 Credits

This project is part of the **100 Days of Code: Python Pro Bootcamp** by *Dr. Angela Yu* on Udemy.

Special thanks to the course for inspiring this project.

---


