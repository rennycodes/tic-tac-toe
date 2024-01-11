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

while True:
    display_board(board)
    get_player_input(board)

# take player input

# check for win or tie

# switch the player

# check for win or tie