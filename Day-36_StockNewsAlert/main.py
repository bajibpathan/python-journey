import requests
import os
from twilio.rest import Client

# -----------------------------
# Stock Price & News Alert Script
# -----------------------------
# This project monitors stock price changes for a given company.
# If the stock shows significant movement, the script automatically
# fetches the latest news articles and sends them as SMS alerts
# using the Twilio API.
# -----------------------------

STOCK = "TSLA"                 # Stock ticker symbol to monitor
COMPANY_NAME = "Tesla Inc"     # Company name for news search

# ------------ STOCK API SETUP ------------
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = os.environ.get("STOCK_API_KEY")  # Alpha Vantage API Key

# Parameters for stock price API request
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
    "outputsize": "compact"
}

# ------------ NEWS API SETUP ------------
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")  # News API Key

# Parameters for fetching latest company news
news_parameters = {
    "apiKey": NEWS_API_KEY,
    "q": COMPANY_NAME
}

# ------------ TWILIO API SETUP ------------
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")  # Twilio SID
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")     # Twilio Auth Token

# ------------ FETCH STOCK DATA ------------
stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
stock_response.raise_for_status()

# Extract daily stock data
data = stock_response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]

# Yesterday’s closing price
yesterday_data = data_list[0]
yesterday_closing_price = float(yesterday_data["4. close"])

# Day before yesterday’s closing price
day_before_yesterday = data_list[1]
day_before_yesterday_closing_price = float(day_before_yesterday["4. close"])

# Compute absolute price difference
difference = yesterday_closing_price - day_before_yesterday_closing_price
up_down = "🔺" if difference > 0 else "🔻"

# Compute price movement percentage
diff_percent = (difference / yesterday_closing_price) * 100

# ------------ TRIGGER NEWS ALERT ------------
# Check if the stock price moved significantly (non-zero here, but can be increased)
if abs(diff_percent) > 0:
    # Fetch related news articles
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    news_response.raise_for_status()
    articles = news_response.json()["articles"]

    # Get the top 3 articles
    three_articles = articles[:3]

    # Format articles into SMS-friendly messages
    formatted_articles = [
        f"{STOCK}: {up_down}{round(diff_percent,2)}%\nHeadline: {article['title']}.\nBrief: {article['description']}\n"
        for article in three_articles
    ]

    print(formatted_articles)  # Debugging output

    # Send each article via SMS using Twilio
    client = Client(account_sid, auth_token)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="from_telephone_number",  # Replace with valid Twilio number
            to="to_telephone_number"        # Replace with verified recipient number
        )
