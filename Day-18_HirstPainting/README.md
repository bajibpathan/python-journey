# 🎨 Hirst Painting Project (Python Turtle Art)

This project recreates a **Hirst-style painting** — a grid of colorful dots — using Python's **Turtle Graphics** module.  
Inspired by the famous contemporary artist **Damien Hirst**, this project demonstrates how to use Python to create visual art through code.

---

## 🚀 Features

- 🐢 Uses the **Turtle Graphics** module for drawing.
- 🎨 Randomly selects colors to create a unique dot pattern each time.
- 🧮 Draws a **10x10 grid** of colored dots.
- ⚡ Optimized for fast rendering using `speed("fastest")`.
- 🧠 Demonstrates concepts like loops, lists, and RGB color manipulation.

---

## 🧩 Project Structure

```
HirstPainting/
│
├── main.py # Main Python file that generates the painting
└── README.md # Project documentation
```

---

## 🧠 How It Works

1. The program sets the Turtle module to use **RGB color mode**.
2. A list of colors (in RGB format) is predefined from real artwork.
3. The turtle draws 100 dots (10 rows x 10 columns).
4. After drawing each row, the turtle moves up and resets to the next line.
5. Each dot is randomly colored, giving a vibrant, unique look.

---

## 🧰 Requirements

- Python 3.x
- No external libraries needed (only uses the built-in `turtle` and `random` modules)

---

## ▶️ How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/bajibpathan/hirst-painting.git
   cd hirst-painting
   ```
2. Run the program:
   ```bash
   python main.py
   ```
3. A Turtle window will open displaying the dot painting.
   Click the window to close it when done.

---

## 🖌️ Example Output

Below is a representation of what the output might look like (actual colors vary each run):

● ● ● ● ● ● ● ● ● ●
● ● ● ● ● ● ● ● ● ●
● ● ● ● ● ● ● ● ● ●
● ● ● ● ● ● ● ● ● ●
● ● ● ● ● ● ● ● ● ●
● ● ● ● ● ● ● ● ● ●
● ● ● ● ● ● ● ● ● ●
● ● ● ● ● ● ● ● ● ●
● ● ● ● ● ● ● ● ● ●
● ● ● ● ● ● ● ● ● ●

---

## 💡 Concepts Learned

- Working with the Turtle Graphics module
- Controlling the turtle’s position and direction
- Generating random colors using RGB tuples
- Using loops to automate drawing patterns
- Building structured, repeatable art through procedural programming

---

## 🎓 Credits

This project was inspired by the Hirst Painting Project from the
100 Days of Code: The Complete Python Pro Bootcamp by Dr. Angela Yu.
I learned and implemented it independently for practice and creativity.

---

## 📜 License

This project is open for educational and learning purposes.
Feel free to fork and experiment with different color palettes or grid sizes!
