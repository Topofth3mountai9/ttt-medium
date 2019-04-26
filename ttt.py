# ttt.py

def convert_selection(selection):
    selection -= 1
    return (selection // 3, selection % 3)


def print_board(board):
    for row in board:
        print(row)


def select_square():
    selection = int(input("Select a square: "))
    if not 1 <= selection <= 9:
        raise ValueError
    return selection


board = [["_" for _ in range(3)] for _ in range(3)]
print_board(board)
try:
    selection = select_square()
    print(selection)
except ValueError:
    print("Sorry, please select a number 1-9")
