# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Function to display the menu and handle user input
def temperature_converter():
    print("Welcome to the Temperature Converter!")
    
    while True:
        try:
            # Display the menu options
            print("\nChoose a conversion option:")
            print("1. Celsius to Fahrenheit")
            print("2. Fahrenheit to Celsius")
            print("3. Exit")
            
            # Get user choice
            choice = int(input("Enter your choice (1-3): "))

            if choice == 1:
                # Celsius to Fahrenheit conversion
                celsius = float(input("Enter temperature in Celsius: "))
                fahrenheit = celsius_to_fahrenheit(celsius)
                print(f"{celsius}°C is equal to {fahrenheit:.2f}°F.")
            elif choice == 2:
                # Fahrenheit to Celsius conversion
                fahrenheit = float(input("Enter temperature in Fahrenheit: "))
                celsius = fahrenheit_to_celsius(fahrenheit)
                print(f"{fahrenheit}°F is equal to {celsius:.2f}°C.")
            elif choice == 3:
                # Exit the program
                print("Exiting the Temperature Converter. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")
        except ValueError:
            # Handle non-numeric inputs
            print("Invalid input. Please enter a valid number.")
        except Exception as e:
            # General error handling
            print(f"An error occurred: {e}")

# Start the temperature converter
if __name__ == "__main__":
    temperature_converter()
