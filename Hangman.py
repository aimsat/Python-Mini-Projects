import random

# List of words for the game
word_list = ['python', 'programming', 'hangman', 'challenge', 'developer', 'code', 'debugging']

# Function to select a random word
def get_random_word():
    return random.choice(word_list)

# Function to display the current progress of the word
def display_word_progress(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

# Function to display the current hangman status
def display_hangman(tries):
    stages = [
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        ---------
        """,
        """
           -----
           |   |
               |
               |
               |
               |
        ---------
        """
    ]
    return stages[tries]

# Main function to play the hangman game
def hangman_game():
    print("Welcome to the Hangman Game!")

    word = get_random_word()  # Get a random word
    guessed_letters = []  # To keep track of the guessed letters
    tries = 6  # Number of tries the player has

    print(f"The word has {len(word)} letters.")
    print(display_hangman(tries))
    print(display_word_progress(word, guessed_letters))
    
    while tries > 0:
        guess = input("Guess a letter: ").lower()
        
        # Input validation for non-alphabetic input
        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input. Please enter a single alphabetical character.")
            continue
        
        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try a different letter.")
            continue
        
        # Add the guessed letter to the list
        guessed_letters.append(guess)
        
        # Check if the guessed letter is in the word
        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            tries -= 1
        
        # Display the current state of the game
        print(display_hangman(tries))
        print(display_word_progress(word, guessed_letters))
        
        # Check if the player has guessed the word
        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! You've guessed the word: {word}")
            break
    else:
        print(f"You're out of tries! The word was: {word}. Better luck next time.")

# Start the game
if __name__ == "__main__":
    hangman_game()
