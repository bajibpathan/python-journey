# Import the ASCII logo from a separate file (art.py) for better UI/UX
from art import logo

# Display the logo at the start of the program
print(logo)

# Function to find the highest bidder from the dictionary of bids
def find_highest_bidder(bidding_dictionary):
    winner = ""       # Stores the name of the winner
    highest_bid = 0   # Stores the highest bid found so far

    # Loop through all bidders in the dictionary
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]  # Get the bid for this bidder
        # Check if this bid is higher than the current highest
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder   # Update the winner

    # Announce the winner and their bid
    print(f"The winner is {winner} and the bid ${highest_bid}")


# Variable to control the continuation of bidding process
continue_bidding = True

# Dictionary to store all bids { "name": bid_amount }
bids = {}

# Main auction loop
while continue_bidding:
    # Ask for user input (bidder name and bid value)
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bids[name] = bid   # Save the bid in the dictionary

    # Ask if there are more bidders
    should_continue = input("Are there any other bidders?  Type 'yes' or 'no'.\n").lower()

    if should_continue == 'no':
        # If no more bidders, end the auction and find the winner
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == 'yes':
        # Clear the screen by printing empty lines (creates fairness in bidding)
        print("\n" * 30)
