import random

# Function to roll the dice
def roll_dice():
    return random.randint(1, 6)

# Function to display the user interface and handle user input
def dice_rolling_simulator():
    print("Welcome to the Dice Rolling Simulator!")
    
    while True:
        try:
            # Ask the user if they want to roll the dice
            roll = input("Type 'roll' to roll the dice or 'exit' to quit: ").lower()

            if roll == 'roll':
                # Roll the dice and display the result
                result = roll_dice()
                print(f"The dice rolled: {result}")
            elif roll == 'exit':
                # Exit the simulator
                print("Thanks for playing! Goodbye!")
                break
            else:
                # Handle invalid input
                print("Invalid input. Please type 'roll' to roll the dice or 'exit' to quit.")
        except Exception as e:
            # General error handling
            print(f"An error occurred: {e}")

# Start the dice rolling simulator
if __name__ == "__main__":
    dice_rolling_simulator()
