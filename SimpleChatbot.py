# Define a dictionary of responses
responses = {
    "hello": "Hello! How can I assist you today?",
    "hi": "Hi there! What can I do for you?",
    "how are you": "I'm just a program, but thanks for asking! How can I help?",
    "what is your name": "I'm a simple chatbot created to assist you.",
    "bye": "Goodbye! Have a nice day!",
    "help": "Sure! I'm here to assist with basic questions. What do you need help with?",
    "what can you do": "I can respond to simple queries and have basic conversations. Try asking me something!"
}

# Function to process the user input and respond
def get_response(user_input):
    # Convert the input to lowercase to make the chatbot case-insensitive
    user_input = user_input.lower()
    
    # Check if the input matches any predefined responses
    for keyword in responses:
        if keyword in user_input:
            return responses[keyword]
    
    # Default response if no match is found
    return "I'm sorry, I don't understand that. Can you please rephrase?"

# Main chatbot loop
def chatbot():
    print("Welcome to the Simple Chatbot!")
    print("Type 'bye' to exit the chat.")
    
    while True:
        user_input = input("You: ")
        
        # Exit condition
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        # Get and display the chatbot's response
        response = get_response(user_input)
        print(f"Chatbot: {response}")

# Start the chatbot
if __name__ == "__main__":
    chatbot()
