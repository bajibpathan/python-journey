# Coffee Machine Program
# ----------------------
# This program simulates a real-world coffee machine.
# It allows users to choose from three types of drinks:
# espresso, latte, or cappuccino. The machine checks for
# ingredient availability, processes coin payments,
# deducts used resources, and serves coffee with change.

# Coffee Menu with ingredients and prices
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# Global variables to track total profit and available resources
profit = 0
resources = {
    "water": 300,   # in milliliters
    "milk": 200,    # in milliliters
    "coffee": 100,  # in grams
}

def is_resource_sufficient(order_ingredients):
    """Checks if there are enough ingredients to make the chosen drink.

    Args:
        order_ingredients (dict): Ingredients required for the selected drink.

    Returns:
        bool: True if resources are sufficient, False otherwise.
    """
    for item in order_ingredients:
        # If required ingredient exceeds what's available, notify user
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def process_coins():
    """Prompts the user to insert coins and calculates the total amount.

    Returns:
        float: The total amount of money inserted by the user.
    """
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    """Validates if the inserted money covers the drink's cost.

    Args:
        money_received (float): Total money user inserted.
        drink_cost (float): Cost of the selected drink.

    Returns:
        bool: True if transaction successful, False otherwise.
    """
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost  # Add earnings to total profit
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    """Prepares the drink by deducting used ingredients from resources.

    Args:
        drink_name (str): Name of the coffee selected by the user.
        order_ingredients (dict): Ingredients needed for that coffee.
    """
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")

# Control variable for the main machine loop
is_on = True

# Main loop simulating the coffee machine operation
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    
    if choice == "off":
        # Turn off the coffee machine
        is_on = False
    elif choice == "report":
        # Display current resources and total profit
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        # Get the drink details from the MENU dictionary
        drink = MENU[choice]
        
        # Check for sufficient ingredients before proceeding
        if is_resource_sufficient(drink["ingredients"]):
            # Ask user to insert coins
            payment = process_coins()
            # Check if payment is successful before making the coffee
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
