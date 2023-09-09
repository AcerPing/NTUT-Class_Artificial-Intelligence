# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 11:36:02 2023

@author: Asus
"""

import numpy as np

ROWS = 6
COLUMNS = 6
CONNECT = 4

def create_board():
    return np.zeros((ROWS, COLUMNS))

def is_valid_move(board, row, col):
    return board[row][col] == 0

def make_move(board, row, col, mark):
    board[row][col] = mark

def check_win(board, row, col, mark):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
    for dr, dc in directions:
        count = 1
        for i in range(1, CONNECT):
            r, c = row + i * dr, col + i * dc
            if (
                0 <= r < ROWS and 0 <= c < COLUMNS
                and board[r][c] == mark
            ):
                count += 1
            else:
                break

        if count == CONNECT:
            return True
    return False

def play_game():
    board = create_board()
    game_over = False
    turn = 0

    while not game_over:
        print(board)
        row = int(input(f"Player {turn % 2 + 1}'s turn. Choose row (0-{ROWS - 1}): "))
        col = int(input(f"Player {turn % 2 + 1}'s turn. Choose column (0-{COLUMNS - 1}): "))

        if 0 <= row < ROWS and 0 <= col < COLUMNS and is_valid_move(board, row, col):
            make_move(board, row, col, turn % 2 + 1)
            game_over = check_win(board, row, col, turn % 2 + 1)

            if game_over:
                print(board)
                print(f"Player {turn % 2 + 1} wins!")
            else:
                turn += 1
        else:
            print("Invalid move. Try again.")

if __name__ == "__main__":
    play_game()
