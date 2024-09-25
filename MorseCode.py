# Dictionary to map text characters to Morse code
TEXT_TO_MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', 
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-', 
    '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', 
    '$': '...-..-', '@': '.--.-.', ' ': '/'
}

# Dictionary to map Morse code to text characters
MORSE_TO_TEXT = {value: key for key, value in TEXT_TO_MORSE.items()}

# Function to translate text to Morse code
def text_to_morse(text):
    text = text.upper()  # Convert the text to uppercase
    morse_code = []
    
    for char in text:
        if char in TEXT_TO_MORSE:
            morse_code.append(TEXT_TO_MORSE[char])
        else:
            morse_code.append('?')  # For unknown characters, append a placeholder
    
    return ' '.join(morse_code)

# Function to translate Morse code to text
def morse_to_text(morse):
    morse = morse.split(' ')  # Split the Morse code by spaces to get individual codes
    decoded_text = []
    
    for code in morse:
        if code in MORSE_TO_TEXT:
            decoded_text.append(MORSE_TO_TEXT[code])
        else:
            decoded_text.append('?')  # For unknown codes, append a placeholder
    
    return ''.join(decoded_text)

# Main program for user interaction
def morse_code_translator():
    print("Welcome to the Morse Code Translator!")
    
    while True:
        print("\nChoose an option:")
        print("1. Text to Morse Code")
        print("2. Morse Code to Text")
        print("3. Exit")
        
        try:
            choice = int(input("Enter your choice (1, 2, or 3): "))
            
            if choice == 1:
                text = input("Enter the text to convert to Morse code: ")
                morse_code = text_to_morse(text)
                print(f"Morse Code: {morse_code}")
            
            elif choice == 2:
                morse_code = input("Enter the Morse code to convert to text (use spaces to separate characters): ")
                text = morse_to_text(morse_code)
                print(f"Text: {text}")
            
            elif choice == 3:
                print("Exiting the Morse Code Translator. Goodbye!")
                break
            
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        
        except ValueError:
            print("Invalid input. Please enter a number.")

# Start the Morse code translator
if __name__ == "__main__":
    morse_code_translator()
