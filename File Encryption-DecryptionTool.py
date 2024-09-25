import os

# Simple Caesar Cipher encryption function
def encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - shift + key) % 26 + shift)
        else:
            encrypted_text += char
    return encrypted_text

# Simple Caesar Cipher decryption function
def decrypt(text, key):
    return encrypt(text, -key)

# Function to read the content of a file
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return None

# Function to write the encrypted/decrypted content to a file
def write_file(filename, content):
    try:
        with open(filename, 'w') as file:
            file.write(content)
            print(f"Successfully written to '{filename}'")
    except IOError:
        print(f"Error: Unable to write to '{filename}'.")

# Main function to handle encryption/decryption
def file_encryption_tool():
    print("File Encryption/Decryption Tool")

    while True:
        operation = input("Would you like to (E)ncrypt or (D)ecrypt a file? (Enter 'E' or 'D', or 'Q' to quit): ").lower()

        if operation == 'e':
            input_filename = input("Enter the name of the file to encrypt: ")
            text = read_file(input_filename)
            if text is None:
                continue

            while True:
                try:
                    key = int(input("Enter the encryption key (a positive integer): "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")

            encrypted_text = encrypt(text, key)
            output_filename = input("Enter the name of the file to save the encrypted text: ")
            write_file(output_filename, encrypted_text)

        elif operation == 'd':
            input_filename = input("Enter the name of the file to decrypt: ")
            text = read_file(input_filename)
            if text is None:
                continue

            while True:
                try:
                    key = int(input("Enter the decryption key (the same integer used for encryption): "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")

            decrypted_text = decrypt(text, key)
            output_filename = input("Enter the name of the file to save the decrypted text: ")
            write_file(output_filename, decrypted_text)

        elif operation == 'q':
            print("Exiting the tool. Goodbye!")
            break
        else:
            print("Invalid option. Please enter 'E' to encrypt, 'D' to decrypt, or 'Q' to quit.")

# Start the tool
if __name__ == "__main__":
    file_encryption_tool()
