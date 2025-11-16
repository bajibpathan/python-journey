# 🌧️ Rain Alert Notification System (Python)

A simple Python automation project that checks upcoming weather conditions using the **OpenWeatherMap API** and sends an SMS alert using **Twilio** if rain is expected. This is a great beginner-friendly project demonstrating:

- REST API consumption  
- JSON parsing  
- Environment variable handling  
- Basic weather condition analysis  
- SMS automation using Twilio  
- Error handling and clean coding practices  

---

## 🚀 Features

- Fetches the next **4 forecast intervals (3-hour blocks)** from OpenWeatherMap  
- Checks if rain or precipitation is expected using weather condition codes  
- Sends an SMS alert to your phone automatically  
- Uses secure environment variables for all API keys  
- Works anywhere in the world with customizable latitude & longitude  

---

## 🛠️ Tech Stack

- **Python 3**
- `requests` (for API calls)  
- `twilio` (for SMS messaging)  
- OpenWeatherMap API  
- Twilio SMS API  

---

## 📦 Installation

- Clone the repo
- Instakllk dependencies:
    ```pip install requests twilio```

---

## 🔑 Environment Variables

Create a .env file or export variables in your shell:

```bash
export OWM_API_KEY="your_openweathermap_api_key"
export TWILIO_ACCOUNT_SID="your_twilio_account_sid"
export TWILIO_AUTH_TOKEN="your_twilio_auth_token"
```

Replace the placeholder numbers in the script:

```bash
from_="your_twilio_number"
to="your_phone_number"
```

---


## ▶️ Usage

Run the script:

``` python main.py ```


If rain is expected, you will receive an SMS:

``` "It's going to rain today. Remember to bring ☔️"```

--- 

## 🌦️ How Rain Detection Works

OpenWeatherMap provides a weather condition ID.
This script checks:

```bash
if weather_id < 700:
    # Rain, drizzle, or snow conditions
```

Codes below 700 mean precipitation is expected.

--- 

## 📁 Project Structure
```
RainAlert/
│
├── main.py          # Main automation script
├── README.md        # Documentation
```

---

## 🙌 Credits

Project inspired by Python 100 Days of Code Bootcamp by Angela Yu.
Created as part of Python learning projects.

---

## 📜 License

This project is open for educational and learning purposes.
Feel free to fork and experiment.