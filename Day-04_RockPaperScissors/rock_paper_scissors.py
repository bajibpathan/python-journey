# Rock Paper Scissors Game 🎮 
# # A simple implementation of the classic game where you play against the computer.

import random

# ASCII art for Rock, Paper, and Scissors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# Store game images in a list for easy access
game_images = [rock, paper, scissors]

# Ask the user to make a choice
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# Generate computer's random choice
computer_choice = random.randint(0, 2)

# Check if the user input is valid
if user_choice >= 0 and user_choice <=2:
    print("You chose:\n")
    print(game_images[user_choice])
else:
    print("Invalid Choice, Please try again!")

# Show computer's choice
print("\nComputer chose\n")
print(game_images[computer_choice])

# Determine the game outcome 
# Handling invalid inputs
if user_choice >= 3 and user_choice < 0:
    print("You typed an invalid number. You lose!")

# Rock beats Scissors
elif user_choice == 0 and computer_choice == 2:
    print("You wins!")

# Scissors loses to Rock
elif computer_choice == 0 and user_choice == 2:
    print("you lose!")

# If computer number is higher, computer wins (except special cases above)
elif computer_choice > user_choice:
    print("You lose!")

# If user number is higher, user wins (except special cases above)
elif user_choice > computer_choice:
    print("You win!")
    
# If both choices are the same, it's a draw
elif computer_choice == user_choice:
    print("It's a draw!")
