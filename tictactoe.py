# Tic Tac Toe Game in Python

# Create the board as a list
board = [' ' for _ in range(9)]

# Function to print the board
def print_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

# Function to check if any player has won
def check_winner(player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), # Rows
                      (0, 3, 6), (1, 4, 7), (2, 5, 8), # Columns
                      (0, 4, 8), (2, 4, 6)] # Diagonals
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# Function to check if the board is full
def check_full():
    return ' ' not in board

# Function to handle a player’s move
def make_move(player):
    while True:
        try:
            move = int(input(f"Player {player}, choose your move (1-9): ")) - 1
            if move < 0 or move > 8 or board[move] != ' ':
                print("Invalid move. Try again.")
            else:
                board[move] = player
                break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

# Main game loop
def play_game():
    current_player = 'X'  # Player X starts the game
    while True:
        print_board()
        make_move(current_player)
        
        if check_winner(current_player):
            print_board()
            print(f"Player {current_player} wins!")
            break
        elif check_full():
            print_board()
            print("It's a tie!")
            break
        
        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'

# Start the game
if __name__ == "__main__":
    play_game()
