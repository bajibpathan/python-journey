# -------------------------------
# Day 01: Band Name Generator 🎶
# -------------------------------

# This is a fun beginner project from the "100 Days of Python" journey.
# The program generates a band name using the city where the user grew up
# and the name of their pet. It's a simple project to practice:
# - Printing messages
# - Taking user input
# - String concatenation

# Welcome message
print("Welcome to the Band Name Generator.")

# Ask the user for the city where they grew up
city_name = input("What's the name of the city you grew up in?\n")

# Ask the user for the name of their pet
pet_name = input("What's your pet's name?\n")

# Combine the two inputs to form a band name suggestion
print("Your band name could be " + city_name + " " + pet_name)