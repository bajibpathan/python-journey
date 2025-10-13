from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Create instances of the three main components of the coffee machine.
money_machine = MoneyMachine()  # Handles payments and profit tracking
coffee_maker = CoffeeMaker()    # Handles ingredient usage and coffee making
menu = Menu()                   # Provides available drink options

# Control flag for running the machine
is_on = True

# The main loop that keeps the coffee machine running until turned off
while is_on:
    # Display available drink options dynamically from the Menu
    options = menu.get_items()
    choice = input(f"What would you like ({options}): ").lower()

    # Allow user to turn off the coffee machine
    if choice == "off":
        is_on = False
    # Print a report of current resources and profit
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        # Find the drink object corresponding to the user's choice
        drink = menu.find_drink(choice)
        # Proceed only if the drink exists and resources are sufficient
        if coffee_maker.is_resource_sufficient(drink):
            # Process payment and make the coffee if payment succeeds
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
