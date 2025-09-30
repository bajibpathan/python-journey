# Caesar Cipher 🔐

A beginner-friendly Python project that implements the **Caesar Cipher**, one of the oldest and simplest encryption techniques.
This project allows you to encode (encrypt) and decode (decrypt) messages by shifting letters of the alphabet by a chosen number.

---

## 📌 Features

* Encrypts messages using Caesar Cipher shift.
* Decrypts messages back to plain text.
* Leaves non-alphabet characters (spaces, punctuation, numbers) unchanged.
* Handles large shift numbers by wrapping around using modulo.
* Interactive CLI program with option to repeat or exit.

---

## 🚀 How It Works

1. The user chooses to **encode** or **decode** a message.
2. They provide:

   * The text message.
   * A shift number (encryption key).
3. The program shifts each alphabet character by the given number.

   * Example: shifting `"abc"` by `2` → `"cde"`.
   * Decoding uses the reverse shift.
4. The program runs in a loop until the user decides to exit.

---

## 🖥️ Example Run

```text
Type 'encode' to encrypt, type 'decode' to decrypt:
encode
Type your message:
hello world
Type the shift number:
5
Here is the encoded result: mjqqt btwqi

Type 'yes' if you want to go again. Otherwise, type 'no'
no
Goodbye
```

---

## 📚 What I Learned

* **Functions in Python**

  * Writing reusable functions with multiple arguments.
* **Conditional Logic**

  * Handling encode/decode using `if-else`.
* **Loops**

  * Using a `while` loop to repeat until exit.
* **Lists and Indexing**

  * Finding positions of characters in the alphabet.
  * Wrapping around with modulo (`%`) operator.
* **String Handling**

  * Converting input to lowercase.
  * Preserving non-alphabet characters.

---

## ⚡ Credits

* Inspired by **Dr. Angela Yu’s 100 Days of Code: Python Bootcamp** (Udemy).
* ASCII logo is stored in a separate `art.py` file.

---

## 📂 Project Structure

```plaintext
├── art.py               # Contains ASCII logo
├── caesar_cipher.py     # Main program with Caesar Cipher logic
└── README.md            # Project documentation
```

---

## 🛠️ How to Run

1. Clone this repository or download the files.
2. Open a terminal in the project directory.
3. Run the program:

   ```bash
   python3 caesar_cipher.py
   ```
4. Follow the on-screen instructions to encode or decode messages.

---

## 📜 License

This project is for educational purposes. Feel free to use or modify it for your own learning or projects.

---
