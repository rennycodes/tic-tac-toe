# Creating the game board
board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']

# Displaying the game board
def display_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])

# Getting player input
current_player = "X"
def get_player_input(board):
    usr_inp = int(input("Choose a board space 1-9: "))
    if usr_inp >= 1 and usr_inp <= 9 and board[usr_inp-1] == "-":
        board[usr_inp-1] = current_player
    else:
        print("Oh noo, that spot is already taking(*_*)")

# Check for win or tie
def win_tie(board):
    if board[0] == board[1] == board[2] and board[0] != "-":
        print("the winner is f{board[0]}")


# A loop to make the game run continously
while True:
    display_board(board)
    get_player_input(board)
    win_tie(board)
    break



# switch the player

# check for win or tie