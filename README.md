# **Tic-Tac-Toe Game**

This is a simple command-line implementation of the classic Tic-Tac-Toe game written in Python.

## **Overview**
This Python script allows two players to play the classic Tic Tac Toe game. Player 'X' and Player 'O' take turns to make a move on the 3x3 game board. The game continues until one player wins, or there is a tie.

## **Usage**

1. ### Run the Game:

   ```bash
   python tic_tac_toe.py  
2. ### Game Board:
    The game board is displayed in the console, and players take turns choosing a position to place their symbol ('X' or 'O').  

    1 | 2 | 3  
    4 | 5 | 6  
    7 | 8 | 9  
3. ### Player Input:
    When prompted, enter a number between 1 and 9 to place your symbol in the corresponding position on the board.
4. ### Game Outcome:
    The game continues until one player wins by completing a row, column, or diagonal, or if the board is filled without a winner, resulting in a tie.

## **Gameplay**
+ Player 'X' starts the game.
+ Players take turns until there is a winner or a tie.
+ The game ends with a victory message or a tie message.

## **Implementation Details**
+ ### Game Logic:
  + The script checks for a winner after every move, considering rows, columns, and diagonals.
  + It detects a tie if the board is full without a winner.
+ ### Player Switching:
  + Players switch turns between 'X' and 'O' after each move.
+ ### Random Computer Player:
  + The script includes a simple random computer player ('O') for single-player mode.

## **Customization**
+ Modify the Script:
  + Feel free to modify the script to add more features or change the gameplay.
+ Single Player vs Multiplayer:
  + Change the `current_player` variable to determine whether it's a two-player game ('X' vs 'O') or a single-player game against the computer.