# 💌 Mail Merge Automation using Python

This **Mail Merge Python Automation** project automatically generates personalized letters for multiple recipients using a single letter template and a list of names.  

It’s a great example of how Python can be used for **file handling, string manipulation, and workflow automation** — saving tons of manual effort!

---

## 🧩 Project Overview

Instead of manually typing or copying letters for each person, this script:
1. Reads all invitee names from a text file  
2. Reads a letter template with a placeholder like `[name]`  
3. Replaces the placeholder with each person’s name  
4. Writes out a new, ready-to-send personalized letter file for each recipient  

---

## 🗂️ Project Structure

```bash
MailMerge/
│
├── Input/
│ ├── Names/
│ │ └── invited_names.txt # List of people to generate letters for
│ ├── Letters/
│ │ └── starting_letter.txt # Template letter with placeholder [name]
│
├── Output/
│ └── ReadyToSend/ # Final personalized letters are saved here
│
├── main.py # Python script that performs the mail merge
└── README.md # Project documentation
```


---

## ⚙️ How It Works

1. The placeholder `[name]` in the letter template is identified using a variable.
2. Each name from the `invited_names.txt` file is read and cleaned up (to remove spaces or newline characters).
3. The template text is updated using the `.replace()` function to substitute `[name]` with the actual name.
4. A new letter file is written for each person inside the `Output/ReadyToSend/` directory.

---

## 🧠 Example

### **Input:**
**invited_names.txt**
```
Angela
Brian
Catherine
```

**starting_letter.txt**
```
Dear [name],

You are invited to our annual celebration event this weekend!
We look forward to seeing you there.

Warm regards,
The Event Team
```


---

### **Output Files:**

```
Output/ReadyToSend/letter_for_Angela.txt
Output/ReadyToSend/letter_for_Brian.txt
Output/ReadyToSend/letter_for_Catherine.txt
```

Each file contains:
```
Dear Angela,

You are invited to our annual celebration event this weekend!
We look forward to seeing you there.

Warm regards,
The Event Team

```

---

## 💡 Key Learnings

This project reinforces several Python concepts:

### 📂 File Handling
- Reading and writing files using `open()`, `.read()`, and `.write()`
- Handling multiple input and output files efficiently

### 🔤 String Manipulation
- Using `.replace()` to substitute dynamic text
- Stripping unwanted whitespace with `.strip()`

### ⚙️ Automation Logic
- Automating repetitive tasks (mass personalization)
- Organizing input/output files in clean directory structures

---

## 🚀 How to Run

1. Make sure you have **Python 3.x** installed.  
2. Place your files as shown in the folder structure above.  
3. Run the script:

   ```bash
   python main.py
   ```
4. Check the Output/ReadyToSend/ folder — your personalized letters will be ready there!

---

## 🧾 Notes

Make sure the placeholder [name] in your template exactly matches the one in your script.

You can easily adapt this for other bulk tasks — like sending personalized emails or certificates.

---

## 🙌 Credits

This project was inspired by Dr. Angela Yu’s 100 Days of Python Bootcamp on Udemy.
I learned and recreated it to practice Python automation and file-handling skills.

---

## 📜 License

This project is open for educational and learning purposes.
Feel free to fork and experiment with different color palettes or grid sizes!
