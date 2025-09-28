import random

# List of letters (both lowercase and uppercase) to be used in the password
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
    'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
    'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

# List of numbers to be used in the password
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# List of special characters to make the password stronger
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

# Ask user how many letters, symbols, and numbers they want in their password
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Empty list to store password characters
password = []

# Add random letters to the password list
for letter in range(0, nr_letters):
    random_letter = random.choice(letters)
    password.append(random_letter)

# Add random symbols to the password list
for symbol in range(0, nr_symbols):
    random_symbol = random.choice(symbols)
    password.append(random_symbol)

# Add random numbers to the password list
for number in range(0, nr_numbers):
    random_number = random.choice(numbers)
    password.append(random_number)

# Uncomment the below lines if you want an "easy password" (not shuffled)
# easy_password = "".join(password)
# print(f"Easy Password: {easy_password}")

# Shuffle the characters in the password to make it more secure
random.shuffle(password)

# Join the characters into a final strong password string
strong_password = "".join(password)

# Display the generated strong password to the user
print(f"Strong Password: {strong_password}")
