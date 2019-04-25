# ttt.py

board = [["_" for _ in range(3)] for _ in range(3)]

def print_board(board):
    for row in board:
        print(row)

print_board(board)

try:
    selection = int(input("Select a square: "))
    if not 1 <= selection <= 9:
        raise ValueError
    print(selection)
except ValueError:
    print("Sorry, please select a number 1-9")
