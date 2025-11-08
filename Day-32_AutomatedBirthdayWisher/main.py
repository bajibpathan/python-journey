import datetime as dt
import pandas
import random
import smtplib

# ---------------------------- USER CONFIGURATION ------------------------------- #
MY_EMAIL = "<YOUR_EMAIL>"      # Your email address (e.g., Gmail)
MY_PASSWORD = "<YOUR_PASSWORD>"  # Your app password or email password (use app password for Gmail)

# ---------------------------- GET TODAY'S DATE ------------------------------- #
# Fetch the current date and extract month and day
today_month = dt.datetime.now().month
today_day = dt.datetime.now().day

# Store today’s month and day as a tuple for easy comparison
today_tuple = (today_month, today_day)

# ---------------------------- READ BIRTHDAY DATA ------------------------------- #
# Load the birthday list from a CSV file
# Expected columns: name, email, year, month, day
data = pandas.read_csv("birthdays.csv")

# Create a dictionary with (month, day) as key and full row data as value
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

# ---------------------------- CHECK AND SEND EMAIL ------------------------------- #
# If today's date matches any (month, day) in the dictionary, send a birthday email
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]

    # Randomly choose one of the three pre-written letter templates
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"

    # Read the selected letter template
    with open(file_path) as letter_file:
        contents = letter_file.read()

        # Personalize the letter by replacing the placeholder with the recipient's name
        birthday_letter = contents.replace("[NAME]", birthday_person["name"])

    # ---------------------------- SEND EMAIL ------------------------------- #
    # Establish a secure connection with the Gmail SMTP server
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()  # Secure the connection
        connection.login(MY_EMAIL, MY_PASSWORD)  # Log in using provided credentials

        # Send the birthday email
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject: Happy Birthday!\n\n{birthday_letter}"
        )

    print(f"🎉 Birthday email successfully sent to {birthday_person['name']} ({birthday_person['email']})!")

else:
    # If today doesn't match anyone’s birthday, no action is taken
    print("✅ No birthdays today.")
