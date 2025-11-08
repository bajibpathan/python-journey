import tkinter
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- CONSTANTS ------------------------------- #
# Define lists of characters to build secure, random passwords
LETTERS = [chr(i) for i in range(97, 123)] + [chr(i).upper() for i in range(97, 123)]  # a-z and A-Z
NUMBERS = [str(i) for i in range(10)]  # 0-9
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    """
    Generates a strong random password consisting of letters, numbers, and symbols.
    The generated password is inserted into the password entry box and copied to clipboard.
    """
    password_letters = [choice(LETTERS) for _ in range(randint(8, 10))]
    password_symbols = [choice(SYMBOLS) for _ in range(randint(2, 4))]
    password_numbers = [choice(NUMBERS) for _ in range(randint(2, 4))]

    # Combine all selected characters and shuffle them for randomness
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    # Join into a single string and insert into the entry field
    password = "".join(password_list)
    password_entry.delete(0, tkinter.END)
    password_entry.insert(0, password)

    # Automatically copy generated password to clipboard
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    """
    Saves user credentials (website, email, password) into a JSON file.
    Includes error handling for missing files and empty input fields.
    """
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # New data structure to store in JSON
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    # Validate user input fields
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty.")
        return

    try:
        # Attempt to open and load existing JSON data
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        # If file not found, create a new JSON file
        with open("data.json", "w") as data_file:
            json.dump(new_data, data_file, indent=4)
    else:
        # Update existing data with new website entry
        data.update(new_data)

        # Write the updated data back to file
        with open("data.json", "w") as data_file:
            json.dump(data, data_file, indent=4)
    finally:
        # Clear the website and password fields after saving
        website_entry.delete(0, tkinter.END)
        password_entry.delete(0, tkinter.END)
        website_entry.focus()


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    """
    Searches for saved credentials based on website input.
    If found, displays email and password; otherwise, shows an error message.
    """
    website = website_entry.get()

    # Attempt to read existing data
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No data file found.")
        return

    # Lookup the website in stored data
    if website in data:
        email = data[website]["email"]
        password = data[website]["password"]
        messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        pyperclip.copy(password)  # Auto-copy found password to clipboard
        website_entry.delete(0, tkinter.END)
    else:
        messagebox.showerror(title="Error", message=f"No details found for '{website}'.")


# ---------------------------- UI SETUP ------------------------------- #
# Initialize main window
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Add app logo
canvas = tkinter.Canvas(width=200, height=200)
logo_image = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# Labels
website_label = tkinter.Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = tkinter.Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = tkinter.Label(text="Password:")
password_label.grid(row=3, column=0)

# Entry fields
website_entry = tkinter.Entry(width=16)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_entry = tkinter.Entry(width=34)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "abc@example.com")

password_entry = tkinter.Entry(width=17)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = tkinter.Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = tkinter.Button(text="Add", width=32, command=save_data)
add_button.grid(row=4, column=1, columnspan=2)

search_button = tkinter.Button(text="Search", width=8, command=find_password)
search_button.grid(row=1, column=2)

# Run the main GUI loop
window.mainloop()
