class MoneyMachine:
    """Models the machine responsible for handling payments and tracking profit."""

    CURRENCY = "$"

    # Define coin values used in the machine
    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Prints the current total profit."""
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """
        Prompts the user to insert coins and calculates the total amount inserted.
        Returns the total monetary value received.
        """
        print("Please insert coins.")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
        return self.money_received

    def make_payment(self, cost):
        """
        Handles the transaction:
        - Checks if payment is sufficient
        - Provides change
        - Updates profit
        - Refunds if insufficient
        Returns True if the transaction is successful, False otherwise.
        """
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry, that's not enough money. Money refunded.")
            self.money_received = 0
            return False
