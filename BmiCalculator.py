# Function to calculate BMI
def calculate_bmi(weight, height):
    if height == 0:
        return "Error! Height cannot be zero."
    return weight / (height ** 2)

# Function to categorize the BMI result
def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

# Function to display the user interface and handle user input
def bmi_calculator():
    print("Welcome to the BMI Calculator!")
    
    while True:
        try:
            # Get the user's height in meters
            height = float(input("Enter your height in meters (e.g., 1.75): "))
            if height <= 0:
                print("Invalid input. Height must be greater than zero. Please try again.\n")
                continue

            # Get the user's weight in kilograms
            weight = float(input("Enter your weight in kilograms (e.g., 68.5): "))
            if weight <= 0:
                print("Invalid input. Weight must be greater than zero. Please try again.\n")
                continue

            # Calculate BMI
            bmi = calculate_bmi(weight, height)
            if isinstance(bmi, str):
                print(bmi)  # Handle the error message from the BMI calculation
            else:
                # Display the BMI and category
                print(f"\nYour BMI is: {bmi:.2f}")
                category = categorize_bmi(bmi)
                print(f"Category: {category}\n")
                
            # Ask the user if they want to calculate again
            again = input("Do you want to calculate again? (yes/no): ").lower()
            if again != 'yes':
                print("Goodbye!")
                break
        
        except ValueError:
            # Handle non-numeric input
            print("Invalid input. Please enter a valid number for height and weight.\n")

# Start the BMI Calculator
if __name__ == "__main__":
    bmi_calculator()
