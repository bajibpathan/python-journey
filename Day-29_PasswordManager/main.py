import tkinter
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- CONSTANTS ------------------------------- #
# Define character sets for generating random passwords
LETTERS = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
    'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
    'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    """Generates a strong random password using letters, numbers, and symbols."""
    password_letters = [choice(LETTERS) for _ in range(randint(8, 10))]
    password_symbols = [choice(SYMBOLS) for _ in range(randint(2, 4))]
    password_numbers = [choice(NUMBERS) for _ in range(randint(2, 4))]

    # Combine all characters and shuffle them for randomness
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    # Join list elements into a single string
    password = "".join(password_list)

    # Insert generated password into the entry box and copy it to clipboard
    password_entry.insert(0, password)
    pyperclip.copy(password)  # Automatically copies the password for convenience


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    """Validates user inputs and saves credentials securely to a text file."""
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # Input validation to ensure no field is empty
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty")
    else:
        # Ask for confirmation before saving the credentials
        is_ok = messagebox.askokcancel(
            title=website,
            message=f"These are the details entered: \nEmail: {email}\nPassword: {password}\nIs it okay to save?"
        )

        # Save credentials to a file if user confirms
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")

            # Clear input fields and reset focus
            website_entry.delete(0, tkinter.END)
            password_entry.delete(0, tkinter.END)
            website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Application logo
canvas = tkinter.Canvas(width=200, height=200)
logo_image = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# Labels for input fields
website_label = tkinter.Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = tkinter.Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = tkinter.Label(text="Password:")
password_label.grid(row=3, column=0)

# Input fields
website_entry = tkinter.Entry(width=34)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()  # Automatically focus cursor on website field

email_entry = tkinter.Entry(width=34)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "abc@example.com")  # Default email for convenience

password_entry = tkinter.Entry(width=17)
password_entry.grid(row=3, column=1)

# Buttons for generating and saving passwords
generate_password_button = tkinter.Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = tkinter.Button(text="Add", width=32, command=save_data)
add_button.grid(row=4, column=1, columnspan=2)

# Run the Tkinter main event loop
window.mainloop()
