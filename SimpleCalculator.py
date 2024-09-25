# Simple Calculator in Python

# Function for addition
def add(x, y):
    return x + y

# Function for subtraction
def subtract(x, y):
    return x - y

# Function for multiplication
def multiply(x, y):
    return x * y

# Function for division
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Function to display the menu
def show_menu():
    print("Simple Calculator")
    print("-----------------")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    print()

# Main function to run the calculator
def calculator():
    while True:
        show_menu()
        
        try:
            choice = int(input("Enter your choice (1-5): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.\n")
            continue

        if choice == 5:
            print("Exiting the calculator. Goodbye!")
            break
        
        if choice in [1, 2, 3, 4]:
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
            except ValueError:
                print("Invalid input. Please enter a valid number.\n")
                continue

            if choice == 1:
                result = add(num1, num2)
                print(f"The result of {num1} + {num2} is: {result}\n")
            elif choice == 2:
                result = subtract(num1, num2)
                print(f"The result of {num1} - {num2} is: {result}\n")
            elif choice == 3:
                result = multiply(num1, num2)
                print(f"The result of {num1} * {num2} is: {result}\n")
            elif choice == 4:
                result = divide(num1, num2)
                print(f"The result of {num1} / {num2} is: {result}\n")
        else:
            print("Invalid choice. Please choose a valid option (1-5).\n")

# Start the calculator
if __name__ == "__main__":
    calculator()
