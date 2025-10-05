import random
from art import logo

# ------------------------------
# Function: deal_card()
# ------------------------------
def deal_card():
    """Returns a random card from the deck."""
    # In Blackjack, 11 represents Ace, and 10 represents 10, Jack, Queen, King
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


# ------------------------------
# Function: calculate_score()
# ------------------------------
def calculate_score(cards):
    """Takes a list of cards and returns the current score."""
    # Blackjack condition: If sum of two cards = 21, return 0 (used to represent Blackjack)
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    # If the hand has an Ace (value 11) and the total goes above 21, convert Ace to 1
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    # Return the total score of the hand
    return sum(cards)


# ------------------------------
# Function: compare()
# ------------------------------
def compare(u_score, c_score):
    """Compares user and computer scores and returns the game result message."""
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"


# ------------------------------
# Function: play_game()
# ------------------------------
def play_game():
    """Main function that controls the flow of a single Blackjack game."""
    print(logo)  # Display the ASCII game logo

    # Initialize user and computer hands
    user_cards = []
    computer_cards = []
    is_game_over = False

    # Deal initial two cards to both player and computer
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # Continue game until it's over
    while not is_game_over:
        # Calculate scores
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        # Display current hands
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        # Check for end-game conditions
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            # Ask if user wants another card
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # Computer draws cards until reaching 17 or higher (standard Blackjack rule)
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # Display final results
    print(f"\nYour final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


# ------------------------------
# Game Loop
# ------------------------------
# Keeps asking the user if they want to play again
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    # Clear the console (adds spacing for a cleaner look)
    print("\n" * 20)
    play_game()
