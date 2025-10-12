import random
from art import logo, vs
from game_data import data

def format_data(account):
    """Format the account data into a printable and user-friendly string."""
    # Extracting individual details from the account dictionary
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    # Return a formatted string like: "Cristiano Ronaldo, a footballer, from Portugal"
    return f"{account_name}, a {account_desc}, from {account_country}"

def check_answer(user_guess, a_followers, b_followers):
    """Compare follower counts and check if user's guess is correct.

    Args:
        user_guess (str): The user's choice, 'a' or 'b'
        a_followers (int): Follower count for account A
        b_followers (int): Follower count for account B

    Returns:
        bool: True if the user's guess is correct, False otherwise.
    """
    # Determine which account has more followers
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

# Display the game logo from the art module
print(logo)

# Initialize score counter and game control variable
score = 0
game_should_continue = True

# Select a random account as the initial 'B' to start the game
account_b = random.choice(data)

# Main game loop
while game_should_continue:
    # Move previous 'B' to become the new 'A'
    account_a = account_b
    # Select a new 'B' ensuring it's different from 'A'
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    # Display the two accounts being compared
    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    # Get the player's guess input
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Clear screen effect by printing multiple new lines
    print("\n" * 20)
    print(logo)

    # Retrieve follower counts from both accounts
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    # Check if the guess was correct
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Provide feedback and update the score accordingly
    if is_correct:
        score += 1
        print(f"You're right! Current Score: {score}")
    else:
        print(f"Sorry, that's wrong. Final Score: {score}")
        # End the game when the user makes an incorrect guess
        game_should_continue = False
