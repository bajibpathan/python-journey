# -----------------------------
# Treasure Island Adventure Game
# -----------------------------
# A simple text-based adventure game where players make choices
# that determine whether they reach the treasure or meet their doom.
# Inspired by Dr. Angela Yu's "100 Days of Python" Udemy course.

# Display ASCII art map at the beginning of the game

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

# Game introduction
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# First choice - left or right
print("You're at a cross road. Where do you want to go?")
choice1 = input("\t Type \"left\" or \"right\"\n").lower()

if choice1 == "left":
    # Second choice - wait or swim
    print("You've come to a lake. There is an island in the middle of the lake.")
    choice2 = input('Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()

    if choice2 == "wait":
        # Third choice - pick a door
        choice3 = input("You arrive safely on the island. You see three doors: red, blue, and yellow. Which door?\n").lower()
        
        if choice3 == "red":
            print("Burned by fire. Game Over!")
        elif choice3 == "blue":
            print("Eaten by beasts. Game Over!")
        elif choice3 == "yellow":
            print("Congratulations! You found the treasure. You Win!")
        else:
            print("That door doesn’t exist. Game Over!")
    else:
        print("You were attacked by trout. Game Over!")

else:
    print("You fall into a hole. Game Over.")

