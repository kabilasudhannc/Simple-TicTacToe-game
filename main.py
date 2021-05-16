# importing required modules
import os

# ----global variables-----

# Initial Board data
board = [' ', ' ', ' ',
         ' ', ' ', ' ',
         ' ', ' ', ' ']

# Let us know if the game doesnt over yet
game_still_going = True

# Tell us who is the winner
winner = None

# Tells us who the current player
set_player = input('Choose between (X and O): ').upper()
current_player = set_player


# -------------Game Functions----------------
def play_game():
    # clear the initial screen
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    # Show the initial board
    print_board()

    # Loop until the game stops (winner or tie)
    while game_still_going:
        # Handle a turn
        handle_turn(current_player)

        # Check if the game is over
        check_if_game_over()

        # Flip to the other player
        flip_player()

    # Since the game over, Print the winner or tie
    if winner == 'X' or winner == 'O':
        print(f"{winner} won.")

    elif winner is None:
        print("Tie.")


def print_board():
    print('\n')
    print(f'{board[0]} | {board[1]} | {board[2]}\t1 | 2 | 3')
    print('- + - + -\t- + - + -')
    print(f'{board[3]} | {board[4]} | {board[5]}\t4 | 5 | 6')
    print('- + - + -\t- + - + -')
    print(f'{board[6]} | {board[7]} | {board[8]}\t7 | 8 | 9')
    print('\n')


def handle_turn(player):
    # Get who gonna play now
    print(f"{player}'s turn.")
    position = input('Choose a position from 1-9: ')

    # Whatever the user inputs, make sure it is a valid input, and the spot is open
    valid = False
    while not valid:

        # Make sure the input is valid
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input('Choose a position from 1-9: ')

        # Get correct index to change our board data through the player input
        position = int(position) - 1

        # Also make sure the player spot is available on the board
        if board[position] == ' ':
            valid = True
        else:
            print('You cant go there, Go again.')

    # Update the board data through the player position
    board[position] = player

    # Show the game board
    print_board()


def check_if_game_over():
    check_for_winner()
    check_for_tie()


def check_for_winner():
    # set the global variable
    global winner

    # Check for the winner any positions
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()

    # Get winner
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None


def check_rows():
    # Set global variable
    global game_still_going
    # check for the rows that have a same values
    row_1 = board[0] == board[1] == board[2] != ' '
    row_2 = board[3] == board[4] == board[5] != ' '
    row_3 = board[6] == board[7] == board[8] != ' '

    # Check for that any rows have the match, if does have flag that there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False

    # Return the winner
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    # if doesnt have any winner return None
    else:
        return None


def check_columns():
    # Set global variable
    global game_still_going
    # check for the columns that have a same values
    column_1 = board[0] == board[3] == board[6] != ' '
    column_2 = board[1] == board[4] == board[7] != ' '
    column_3 = board[2] == board[5] == board[8] != ' '

    # Check for any columns have a match, if does have flag there is a win
    if column_1 or column_2 or column_3:
        game_still_going = False

    # Return the winner
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    # if doesnt have any winner return None
    else:
        return None


def check_diagonals():
    # set global variable
    global game_still_going
    # check for the diagonals that have a same values
    diagonal_1 = board[0] == board[4] == board[8] != ' '
    diagonal_2 = board[6] == board[4] == board[2] != ' '

    # Check for any diagonal have a match, if does have a match flag there is a win
    if diagonal_1 or diagonal_2:
        game_still_going = False

    # Return the winner
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]
    # If doesnt have any win return None
    else:
        return None


def check_for_tie():
    # set global variable
    global game_still_going
    # if the board is full
    if ' ' not in board:
        game_still_going = False
        return True
    # Else there is no tie
    else:
        return False


def flip_player():
    # Set global variable
    global current_player
    # if the current player was X, Make it O
    if current_player == 'X':
        current_player = "O"
    # if the current player was O, Make it X
    elif current_player == 'O':
        current_player = 'X'


# ---------Execution Part------------
# play game data for Tic Tac Toe game
play_game()

# board
# Display board
# play game
# handle turn
# check win
# check rows
# check columns
# check diagonal
# check tie
# flip player
