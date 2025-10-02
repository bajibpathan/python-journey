# Import ASCII logo art from art.py for better UI/UX
from art import logo

# Function for addition
def add(n1, n2):
    return n1 + n2

# Function for subtraction
def subtract(n1, n2):
    return n1 - n2

# Function for multiplication
def multiply(n1, n2):
    return n1 * n2

# Function for division
def divide(n1, n2):
    return n1 / n2

# Main calculator function that handles user input and operations
def calculator():
    # Display calculator logo at start
    print(logo)
    
    # Control flag to decide whether to continue calculations
    should_accumulate = True
    
    # Ask for the first number from the user
    number1 = float(input("What's the first number?: "))

    # Loop until user chooses to stop
    while should_accumulate:

        # Display all available operation symbols (+, -, *, /)
        for symbol in operations:
            print(symbol)

        # Ask the user to choose an operation
        operation_symbol = input("Pick an operation: ")
        
        # Ask for the next number
        number2 = float(input("What's the next number?: "))

        # Perform the calculation using the chosen operation
        result = operations[operation_symbol](number1, number2)

        # Display the result of the calculation
        print(f"{number1} {operation_symbol} {number2} = {result}")

        # Ask user whether they want to continue, restart, or quit
        choice = input(
            f"Type 'y' to continue calculating with {result}, "
            f"or type 'n' to start a new calculation, "
            f"or 'q' to quit:  "
        ).lower()

        if choice == 'y':
            # Continue with the result as the new first number
            number1 = result
        elif choice == 'n':
            # Restart the calculator fresh
            should_accumulate = False
            print("\n" * 20)  # Clear screen effect
            calculator()      # Recursively call calculator
        elif choice == 'q':
            # Exit the program
            print("Good Bye")
            return

# Dictionary mapping operation symbols to their respective functions
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# Start the calculator program
calculator()
