import requests
import os
from twilio.rest import Client

# -----------------------------
# Rain Alert Notification Script
# -----------------------------
# This project fetches weather forecast data from OpenWeatherMap 
# and sends an SMS alert using Twilio if rain is expected 
# in the next few forecast intervals (approx. next 12 hours).
# -----------------------------

OWMN_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

# API keys and credentials stored securely in environment variables
API_KEY = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

# Coordinates for the location to monitor
MY_LAT = 40.71     # Your latitude
MY_LNG = 74.00     # Your longitude

# Parameters sent to OpenWeatherMap API
parameters = {
    "lat": MY_LAT,
    "lon": MY_LNG,
    "cnt": 4,        # Number of forecast intervals to check (3-hour intervals)
    "appid": API_KEY
}

# Call OpenWeatherMap API
response = requests.get(url=OWMN_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()["list"]

# Flag to determine if rain is expected
will_rain = False

# Loop through each forecasted time interval
for hour_data in weather_data:
    # Weather condition codes: <700 generally indicates rain/snow/drizzle
    condition_code = int(hour_data["weather"][0]["id"])
    if condition_code < 700:
        will_rain = True

# If rain is expected, send SMS alert via Twilio
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring ☔️",
        from_="from_telephone_number",   # Replace with valid Twilio number
        to="to_telephone_number"         # Replace with verified recipient number
    )
    print(message.status)  # Print delivery status for debugging
