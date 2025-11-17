# 📈 Stock Price & News Alert System (Python)

This Python automation project tracks stock price movements using the **Alpha Vantage API** and automatically sends the top news articles related to the company using the **NewsAPI** and **Twilio SMS API**.

If the stock price moves significantly, you instantly receive an SMS alert with:
- 🔺 Price movement indicator  
- 📉 Percentage change  
- 📰 Latest news headlines  
- 📝 Short description of each article  

Great project for practicing:
- REST API integrations  
- JSON parsing  
- Environment variables  
- Twilio SMS automation  
- Financial data analysis  

---

## 🚀 Features

- Fetches daily stock prices  
- Identifies upward or downward stock price movement  
- Calculates percentage change  
- Retrieves relevant news articles  
- Sends SMS alerts automatically  
- Uses secure API key management  
- Works for any company or stock symbol  

---

## 🛠️ Tech Stack

- **Python 3**
- `requests` — HTTP API calls  
- `twilio` — SMS alerts  
- Alpha Vantage Stock API  
- NewsAPI for headlines  

---

## 📦 Installation

- Clone the repository:
- Install dependencies:
    - ``` pip install requests twilio ```

---

## 🔑 Environment Variables

Create a .env file or export variables:

```bash
export STOCK_API_KEY="your_alpha_vantage_api_key"
export NEWS_API_KEY="your_news_api_key"
export TWILIO_ACCOUNT_SID="your_twilio_sid"
export TWILIO_AUTH_TOKEN="your_twilio_auth_token"
```

Update sender & receiver phone numbers inside the script:

```bash
from_="your_twilio_phone_number"
to="your_verified_phone_number"
```

---

### ▶️ Running the Script

```bash python main.py ```


If the stock moves, you'll receive SMS alerts like:

```bash
TSLA: 🔺3.2%
Headline: Tesla hits new milestone.
Brief: Tesla announces new manufacturing plans...
```

---

## 📊 How Price Movement Detection Works

```bash
difference = yesterday - day_before_yesterday
percentage = (difference / yesterday) * 100
```

And for trend indication:

```bash
"🔺" if difference > 0 else "🔻"
```

You can modify the alert threshold:

```bash
if abs(diff_percent) > 5:
    # Only alert for movements above 5%
```

---

## 📁 Project Structure
```bash
stocknewsalert/
│
├── main.py          # Main program logic
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