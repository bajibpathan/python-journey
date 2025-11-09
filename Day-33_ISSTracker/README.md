# 🛰️ International Space Station (ISS) Tracker

A Python automation project that tracks the **International Space Station (ISS)** in real-time and sends you an **email alert** when it’s visible in your night sky 🌌.

This project combines **API integration**, **email automation**, and **astronomical data** to create a simple yet powerful space-tracking tool.

---

## 🚀 Features

- 🌍 **Real-Time ISS Tracking** — Uses live ISS positional data from the Open Notify API.  
- 🌅 **Day/Night Detection** — Uses the Sunrise-Sunset API to determine if it’s currently dark at your location.  
- 📬 **Email Alerts** — Automatically sends an email when the ISS is overhead at night.  
- ⏱️ **Background Automation** — Runs continuously, checking every 60 seconds.

---

## 🧠 How It Works

1. Fetches **current ISS coordinates** via the [Open Notify API](http://api.open-notify.org/iss-now.json).  
2. Compares the ISS position with your latitude and longitude (±5° range).  
3. Uses [Sunrise-Sunset API](https://sunrise-sunset.org/api) to check if it’s currently night at your location.  
4. If the ISS is nearby **and** it’s dark, sends you an email notification to “look up.”  

---

## 🛠️ Tech Stack

- **Python 3**
- **requests** – For making API calls.
- **datetime** – For checking current time.
- **smtplib** – For sending email notifications.
- **time** – For scheduled checking.

---

## 📂 Project Structure

```
ISSTracker/
│
├── main.py # Main Python script
├── README.md # Project documentation
```


---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
### 2️⃣ Install Dependencies
```bash
pip install requests
```
### 3️⃣ Configure Your Location and Email

Edit the following values in main.py:
```
MY_LAT = 43.653225      # Your latitude
MY_LONG = -79.383186    # Your longitude
MY_EMAIL = "youremail@gmail.com"
MY_PASSWORD = "yourpassword"   # Use an app-specific password
```

💡 For Gmail, you must enable 2-Step Verification and use an App Password for security.

---

## 💌 Email Alert Example

```
Subject: Look Up! 👆

The ISS is above you in the night sky!
```

When this email arrives, step outside — the ISS should be visible!

---

## 🙌 Credits

- APIs Used:
    - Open Notify ISS API
    - Sunrise-Sunset API
- Project inspired by Python 100 Days of Code Bootcamp by Angela Yu.
- Created as part of Python learning projects.

---

## 📜 License

This project is open for educational and learning purposes.
Feel free to fork and experiment.
