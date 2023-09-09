# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 15:51:46 2023

@author: Asus
"""

import numpy as np
import random

ROWS = 6
COLUMNS = 6
CONNECT = 4

def create_board():
    return np.zeros((ROWS, COLUMNS))

def is_valid_move(board, row, col):
    return board[row][col] == 0

def make_move(board, row, col, mark):
    board[row][col] = mark

def check_win(board, mark):
    for row in range(ROWS):
        for col in range(COLUMNS):
            if (
                col <= COLUMNS - CONNECT
                and len(set(board[row, col : col + CONNECT])) == 1
                and board[row, col] == mark
            ) or (
                row <= ROWS - CONNECT
                and len(set(board[row : row + CONNECT, col])) == 1
                and board[row, col] == mark
            ) or (
                row <= ROWS - CONNECT
                and col <= COLUMNS - CONNECT
                and len(set(board[range(row, row + CONNECT), range(col, col + CONNECT)])) == 1
                and board[row, col] == mark
            ) or (
                row >= CONNECT - 1
                and col <= COLUMNS - CONNECT
                and len(set(board[range(row, row - CONNECT, -1), range(col, col + CONNECT)])) == 1
                and board[row, col] == mark
            ):
                return True
    return False

def ai_move(board):
    while True:
        row = random.randint(0, ROWS - 1)
        col = random.randint(0, COLUMNS - 1)
        if is_valid_move(board, row, col):
            make_move(board, row, col, 2)
            return

def play_game():
    board = create_board()
    game_over = False

    while not game_over:
        print(board)

        row = int(input(f"Your turn. Choose row (0-{ROWS - 1}): "))
        col = int(input(f"Your turn. Choose column (0-{COLUMNS - 1}): "))

        if 0 <= row < ROWS and 0 <= col < COLUMNS and is_valid_move(board, row, col):
            make_move(board, row, col, 1)
            game_over = check_win(board, 1)

            if game_over:
                print(board)
                print("You win!")
            else:
                ai_move(board)
                game_over = check_win(board, 2)

                if game_over:
                    print(board)
                    print("AI wins!")
        else:
            print("Invalid move. Try again.")

if __name__ == "__main__":
    play_game()
