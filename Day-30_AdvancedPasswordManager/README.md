# 🔐 Advanced Password Manager

A secure and user-friendly **Password Manager** built using **Python** and **Tkinter GUI**.  
This version improves upon the basic version with:
- **JSON-based data storage**
- **Error handling**
- **Search functionality** to find saved credentials easily.

---

## ✨ Features

✅ Generate secure, random passwords  
✅ Copy passwords automatically to clipboard  
✅ Save credentials (Website, Email, Password) in a JSON file  
✅ Retrieve existing credentials with a search feature  
✅ Handle missing files or incomplete inputs gracefully  

---

## 🧱 Project Structure

```
AdvancedPasswordManager/
│
├── main.py # Main application script
├── logo.png # App logo for UI
├── data.json # JSON file storing credentials (auto-created)
└── README.md # Documentation

```

---

## 🧠 How It Works

1. **Generate Password**  
   - Click the “Generate Password” button to create a secure random password.
   - The password is **auto-copied** to your clipboard.

2. **Save Credentials**  
   - Enter the Website, Email/Username, and Password.
   - Click “Add” to save.  
   - All data is stored in `data.json` in this format:
     ```json
     {
       "example.com": {
         "email": "user@example.com",
         "password": "My$tr0ngP@ss"
       }
     }
     ```

3. **Find Saved Passwords**  
   - Enter a website name and click “Search”.
   - If found, your credentials appear in a popup and are copied to your clipboard.

---

## 🛠️ Requirements

- Python 3.x  
- Tkinter (pre-installed with Python)  
- pyperclip library for clipboard operations  

Install dependencies using:
```bash
pip install pyperclip
```

---

## ▶️ Run the App

```python main.py```

---

## ⚙️ Error Handling

- If data.json does not exist, the program creates it automatically.
- If input fields are empty, an alert will remind the user to fill them.
- If a website entry doesn’t exist in the data file, an error message will appear.

---

## 🔒 Security Notes

⚠️ This project stores credentials in plain text (JSON) for educational purposes only.
For production-level security:
- Encrypt the data using the cryptography library.
- Use a master password for authentication.
- Store data securely (e.g., local database or cloud vault).

---

## 📸 Example UI
```
+----------------------------------------------------+
|                     [Logo]                         |
| Website: [__________] [Search]                     |
| Email:   [abc@example.com___________]              |
| Password:[______] [Generate Password]              |
|                                                    |
|                  [Add]                             |
+----------------------------------------------------+
```

---

## 🧩 Learning Highlights

- Tkinter GUI layouts and event handling
- File handling with JSON (read, write, update)
- Error handling using try-except-else-finally
- Clipboard integration with pyperclip
- Building simple desktop apps with Python

---

## 🙌 Credits

Project inspired by Python 100 Days of Code Bootcamp by Angela Yu.
Created as part of Python learning projects.

---

## 📜 License

This project is open for educational and learning purposes.
Feel free to fork and experiment.
