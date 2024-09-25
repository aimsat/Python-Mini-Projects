import string

# Function to check if the input is a palindrome
def is_palindrome(input_text):
    # Remove spaces and punctuation, and convert to lowercase
    cleaned_text = ''.join(char.lower() for char in input_text if char.isalnum())
    
    # Check if the cleaned text is the same forwards and backwards
    return cleaned_text == cleaned_text[::-1]

# Function to display the user interface and handle input
def palindrome_checker():
    print("Welcome to the Palindrome Checker!")
    
    while True:
        input_text = input("Enter a word or phrase to check (or type 'exit' to quit): ").strip()

        if input_text.lower() == 'exit':
            print("Exiting the Palindrome Checker. Goodbye!")
            break
        
        if not input_text:
            print("Error: Empty input. Please enter a valid word or phrase.")
            continue
        
        if is_palindrome(input_text):
            print(f"'{input_text}' is a palindrome!")
        else:
            print(f"'{input_text}' is not a palindrome.")

# Start the palindrome checker
if __name__ == "__main__":
    palindrome_checker()
