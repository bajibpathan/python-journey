# 🎂 Automated Birthday Wisher (Python)

A simple and efficient **Automated Birthday Wisher** built in Python that automatically sends personalized birthday emails to your contacts.  

Using this project, you can surprise your friends, family, or team members with a heartfelt email — **without lifting a finger!**

---

## 🚀 Features

- 🗓️ **Automated Birthday Detection** – Checks today’s date and matches it against your birthday list.
- ✉️ **Personalized Messages** – Uses customizable templates with the recipient’s name.
- 🎨 **Random Template Selection** – Randomly selects one of three pre-written birthday letters.
- 🔐 **Secure Email Sending** – Uses encrypted SMTP connection (TLS) for safe email delivery.
- 📁 **Persistent Data Storage** – Birthday details stored in a simple CSV file.

---

## 🛠️ Tech Stack

- **Python 3**
- **Pandas** – For reading and handling birthday data.
- **smtplib** – For sending emails through Gmail’s SMTP server.
- **datetime** – For fetching today’s date.
- **random** – For selecting random birthday templates.

---

## 📂 Project Structure

```
AutomatedBirthdayWisher/
│
├── birthdays.csv # Contact list with birthdays
│
├── letter_templates/ # Folder containing pre-written email templates
│ ├── letter_1.txt
│ ├── letter_2.txt
│ └── letter_3.txt
│
├── main.py # Main Python script
└── README.md # Project documentation
```


---

## 📋 Example: `birthdays.csv`

| name    | email               | year | month | day |
|:--------|:--------------------|:-----|:------|:----|
| Alice   | alice@example.com   | 1992 | 10     | 5  |
| Bob     | bob@example.com     | 1989 | 11     | 20 |
| Charlie | charlie@example.com | 1990 | 12     | 15 |

---

## 💌 Example: `letter_1.txt`

```
Dear [NAME],

Wishing you a fantastic birthday filled with joy and success!
Have an amazing year ahead! 🎉

Best wishes,
[Your_name]


```

The placeholder `[NAME]` will be automatically replaced with the actual recipient’s name when sending the email.

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
### 2️⃣ Install Required Libraries
```bash
pip install pandas
```
### 3️⃣ Update Your Email Credentials
Edit main.py and replace:
```
MY_EMAIL = "<YOUR_EMAIL>"
MY_PASSWORD = "<YOUR_PASSWORD>"

```
💡 For Gmail, enable 2-Step Verification and generate an App Password instead of using your main password.
### 4️⃣ Run the Script
```bash
python main.py
```
The script will check today’s date and send birthday wishes if a match is found.

---
## 🔒 Security Tip

- Never hard-code your credentials in a public repository.
- Use environment variables or a config file to store your email and password securely:

```bash
import os
MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")
```
---

## 🧠 How It Works

- Reads birthdays.csv to get names, emails, and dates.
- Checks if today matches any birthday.
- Picks a random letter from the letter_templates folder.
- Replaces [NAME] in the letter with the recipient’s name.
- Sends the email automatically via Gmail’s SMTP server.

---

## 🙌 Credits

Project inspired by Python 100 Days of Code Bootcamp by Angela Yu.
Created as part of Python learning projects.

---

## 📜 License

This project is open for educational and learning purposes.
Feel free to fork and experiment.
