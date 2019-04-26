# ttt.py

def main():
    board = [["_" for _ in range(3)] for _ in range(3)]
    is_x = True
    while True:
        player = "X" if is_x else "O"
        print_board(board)
        try:
            selection = convert_selection(select_square())
            place_piece(selection, player, board)
        except ValueError:
            print("Sorry, please select a number 1-9")
        is_x = not is_x


def convert_selection(selection):
    selection -= 1
    return (selection // 3, selection % 3)


def place_piece(selection, player, board):
    board[selection[0]][selection[1]] = player


def print_board(board):
    for row in board:
        print(row)


def select_square():
    selection = int(input("Select a square: "))
    if not 1 <= selection <= 9:
        raise ValueError
    return selection


if __name__ == "__main__":
    main()
