# ttt.py

board = [["_" for _ in range(3)] for _ in range(3)]

def print_board(board):
    for row in board:
        print(row)

print_board(board)

try:
    selection = int(input("Select a square: "))
    if selection > 9 or selection < 1:
        print("Sorry, please select a number 1-9.")
    else:
        print(selection)
except ValueError:
    print("Sorry, that's not a number!")
