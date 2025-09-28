
import random
from hangman_words import word_list   # Import list of possible words
from hangman_art import stages, logo  # Import ASCII art for hangman and game logo

# Set the number of lives (incorrect guesses allowed)
lives = 6

# Display the game logo at the start
print(logo)

# Randomly choose a word from the word list
chosen_word = random.choice(word_list)
print(chosen_word)  # Debugging: shows the chosen word (can be hidden in actual gameplay)

# Create placeholders (underscores) for the chosen word
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

# Initialize game state variables
game_over = False
correct_letters = []  # Store correctly guessed letters

# Main game loop
while not game_over:

    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()  # Take input from user and convert to lowercase

    # Check if the player already guessed this letter
    if guess in correct_letters:
        print(f"You've already guessed {guess}")
        
    display = ""  # This will hold the updated word with correct guesses filled in

    # Build the display string by checking guessed letters against the chosen word
    for letter in chosen_word:
        if letter == guess:  
            display += letter
            correct_letters.append(guess)  # Add correct guess to the list
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    # If the guessed letter is not in the chosen word, reduce lives
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        # End game if no lives are left
        if lives == 0:
            game_over = True
            print(f"***********************IT WAS {chosen_word}. YOU LOSE**********************")

    # Check if the player has guessed all letters (no underscores left)
    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    # Print the corresponding hangman stage (visual representation)
    print(stages[lives])
