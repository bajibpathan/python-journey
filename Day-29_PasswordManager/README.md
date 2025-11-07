# 🔐 Password Manager

A simple and secure **Password Manager** built using Python’s **Tkinter GUI**.  
This app helps you generate strong passwords and store your login credentials locally.

---

## 💡 Features

✅ Random password generator (letters, numbers, symbols)  
✅ Automatic copy of password to clipboard  
✅ Simple UI for entering and saving credentials  
✅ Data saved locally in `data.txt`  
✅ Input validation and confirmation before saving  

---

## 🧠 How It Works

1. Enter a **Website**, **Email/Username**, and optionally click **Generate Password**.
2. The generated password is automatically copied to your clipboard.
3. Click **Add** to save the details securely in `data.txt`.
4. Each entry is saved in the format:
    ```website | email | password```


---

## 🧱 Project Structure

```bash
PasswordManager/
│
├── main.py # Main Python script
├── logo.png # App logo displayed in UI
├── data.txt # Saved credentials file (auto-created)
└── README.md # Project documentation
```

---

## 🛠️ Requirements

- Python 3.x  
- Tkinter (comes pre-installed with Python)  
- pyperclip library for clipboard operations

Install pyperclip using:
```bash
pip install pyperclip
```
---

## ▶️ Run the App

Run the app:
``` python main.py ```

---

## ⚠️ Security Note

This app saves credentials in plain text (data.txt) for simplicity and learning purposes.
For production use:

- Consider encrypting the data file (e.g., using cryptography library).
- Avoid storing sensitive passwords without encryption.

---

## 📸 Example UI

```
+-------------------------------------------+
|          [Password Manager Logo]           |
| Website:  [_______________________]        |
| Email:    [abc@example.com________]        |
| Password: [______] [Generate Password]     |
|                                             |
|                 [Add]                      |
+-------------------------------------------+

```

---

## 🧩 Learning Highlights

- Tkinter layout and event handling
- Input validation and messagebox dialogs
- File operations (write, append, read)
- Clipboard integration using pyperclip
- Random password generation with Python’s random module

---

## 🙌 Credits

Project inspired by Python 100 Days of Code Bootcamp by Angela Yu.
Created as part of Python learning projects.

---

## 📜 License

This project is open for educational and learning purposes.
Feel free to fork and experiment.

