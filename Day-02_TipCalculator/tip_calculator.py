# -------------------------------
# Day 02: Tip Calculator 💵
# -------------------------------

# This program calculates how much each person should pay
# after splitting a bill, including a tip percentage.
# Concepts covered:
# - Variables
# - Data types (int, float)
# - User input
# - Arithmetic operations
# - Rounding numbers
# - f-strings for formatted output

# Welcome message
print("Welcome to the tip calculator!")

# Ask the user for the total bill amount and convert it to float
bill = float(input("What was the total bill? $"))

# Ask the user for the tip percentage they want to give (10, 12, or 15)
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))

# Ask the user how many people will split the bill
people = int(input("How many people to split the bill? "))

# Calculate the tip as a percentage (e.g., 12 -> 0.12)
tip_as_percent = tip / 100

# Calculate the total tip amount
total_tip_amount = bill * tip_as_percent

# Add the tip to the original bill to get the total
total_bill = bill + total_tip_amount

# Divide the total bill by the number of people
bill_per_person = total_bill / people

# Round the result to 2 decimal places (like a real bill amount)
final_amount = round(bill_per_person, 2)

# Display the amount each person should pay
print(f"Each person should pay: ${final_amount}")