import random
from art import logo

# Constants for number of turns based on difficulty level
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# -------------------------------------------
# Function: check_answer()
# -------------------------------------------
def check_answer(user_guess, actual_answer, turns):
    """
    Compare the user's guess with the actual answer.
    
    Args:
        user_guess (int): The number guessed by the user.
        actual_answer (int): The actual randomly chosen number.
        turns (int): The number of remaining attempts.
    
    Returns:
        int: Updated number of turns left after evaluating the guess.
    """
    if user_guess > actual_answer:
        print("Too high.")
        print("Guess again!")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low.")
        print("Guess again!")
        return turns - 1
    else:
        print(f"🎉 You got it! The correct answer was {actual_answer}.")
        return 0


# -------------------------------------------
# Function: set_difficulty()
# -------------------------------------------
def set_difficulty():
    """
    Asks the player to choose a difficulty level and returns 
    the corresponding number of allowed turns.
    
    Returns:
        int: Number of turns based on chosen difficulty.
    """
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    elif level == "hard":
        return HARD_LEVEL_TURNS
    else:
        print("❌ Invalid input. Please type 'easy' or 'hard' only.")
        return set_difficulty()  # Ask again if invalid input is given


# -------------------------------------------
# Function: game()
# -------------------------------------------
def game():
    """
    Main function that runs the Number Guessing Game.
    
    The game randomly selects a number between 1 and 100, 
    and the player tries to guess it within a limited number of turns.
    """
    print(logo)
    print("🎯 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100...")

    # Randomly choose the number to guess
    answer = random.randint(1, 100)
    print(answer)  # 👀 Uncomment this line for debugging or testing

    # Set the difficulty level and get number of turns
    turns = set_difficulty()
    guess = 0

    # Game loop: continue until player guesses correctly or runs out of turns
    while guess != answer:
        print(f"\nYou have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        # Check guess and update remaining turns
        turns = check_answer(guess, answer, turns)

        # If no turns left, game over
        if turns == 0:
            print("💀 You've run out of guesses. You lose!")
            print(f"The correct answer was {answer}.")
            return


# -------------------------------------------
# Start the game
# -------------------------------------------
game()
