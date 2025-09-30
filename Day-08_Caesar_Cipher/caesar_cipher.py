
# Import the ASCII logo art from a separate file (art.py) for better UI/UX
from art import logo

# Display the logo when the program starts
print(logo)

# Define the alphabet that will be used for encryption and decryption
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Control variable for looping the program multiple times
should_continue = True

# Caesar cipher function: works for both encoding and decoding
def caesar(original_text, shift_amount, encode_or_decode):
    # Initialize an empty string to store the final result
    output_text = ""

    # If decoding, reverse the shift direction
    if encode_or_decode == "decode":
        shift_amount *= -1

    # Loop through each letter in the input text
    for letter in original_text:
        # If the character is not in the alphabet (e.g., space, numbers, punctuation),
        # keep it unchanged in the output
        if letter not in alphabet:
            output_text += letter
        else:
            # Find the new position of the letter after shifting
            shifted_position = alphabet.index(letter) + shift_amount

            # Use modulo to wrap around the alphabet (so it doesn’t go out of range)
            shifted_position %= len(alphabet)

            # Append the shifted letter to the output string
            output_text += alphabet[shifted_position]

    # Display the final encrypted or decrypted text
    print(f"Here is the {encode_or_decode}d result: {output_text}")


# Main program loop
while should_continue:
    # Ask user whether they want to encode or decode
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    # Get the message from the user
    text = input("Type your message:\n").lower()

    # Get the shift number (key) for the Caesar Cipher
    shift = int(input("Type the shift number:\n"))

    # Call the Caesar function with the user inputs
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    # Ask the user if they want to continue or exit
    choice = input("Type 'yes' if you want to go again. Otherwise, type 'no'\n").lower()
    if choice == "no":
        should_continue = False
        print("Goodbye")

