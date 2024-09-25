import random
import string

# Function to generate a random password
def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special_chars):
    # Create a pool of characters to choose from based on user preferences
    character_pool = ''
    
    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_lowercase:
        character_pool += string.ascii_lowercase
    if use_digits:
        character_pool += string.digits
    if use_special_chars:
        character_pool += string.punctuation
    
    # Ensure the character pool is not empty
    if not character_pool:
        raise ValueError("At least one type of character must be selected to generate a password.")
    
    # Generate a random password using the character pool
    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

# Function to get user input and generate the password
def password_generator():
    print("Welcome to the Password Generator!")
    
    # Get password length from the user
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length <= 0:
                print("Please enter a valid positive number.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    # Get customization options from the user
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'
    
    # Generate the password
    try:
        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special_chars)
        print(f"Generated password: {password}")
    except ValueError as e:
        print(e)

# Start the password generator
if __name__ == "__main__":
    password_generator()
