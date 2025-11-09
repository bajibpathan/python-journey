import requests
from datetime import datetime
import smtplib
import time

# ---------------------------- USER CONFIGURATION ------------------------------- #
MY_LAT = 43.653225   # Your latitude (example: Toronto, Canada)
MY_LONG = -79.383186 # Your longitude (example: Toronto, Canada)
MY_EMAIL = "<YOUR_EMAIL>"      # Your email address
MY_PASSWORD = "<YOUR_PASSWORD>" # Your email password or app-specific password

# ---------------------------- CHECK IF ISS IS OVERHEAD ------------------------------- #
def is_iss_overhead():
    """
    Checks the current location of the International Space Station (ISS)
    using the Open Notify API and determines if it is currently within
    ±5 degrees of the user's location.
    """
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    # Extract ISS position
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Check if ISS is near the user's position (within 5-degree range)
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


# ---------------------------- CHECK IF IT'S NIGHTTIME ------------------------------- #
def is_night():
    """
    Determines whether it is currently nighttime at the user's location
    using the Sunrise-Sunset API.
    """
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,  # Use 24-hour ISO format for time values
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    # Extract sunrise and sunset times from API response
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    # Get the current hour
    time_now = datetime.now().hour

    # Returns True if it is dark (i.e., before sunrise or after sunset)
    if time_now >= sunset or time_now <= sunrise:
        return True


# ---------------------------- SEND EMAIL NOTIFICATION ------------------------------- #
def send_email():
    """
    Sends an email alert notifying the user that the ISS is currently
    overhead and visible in the night sky.
    """
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()  # Secure the email connection
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject: Look Up! 👆\n\nThe ISS is above you in the night sky!"
        )


# ---------------------------- MAIN LOOP ------------------------------- #
# Repeatedly check every 60 seconds whether the ISS is overhead during the night.
# If both conditions are met, an email alert is sent to the user.
while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        send_email()
