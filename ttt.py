# ttt.py

import timeit

board = [["_" for _ in range(3)] for _ in range(3)]

def print_board_list(board):
    [print(row) for row in board]

def print_board_for(board):
    for row in board:
        print(row)

begin = timeit.default_timer()
print_board_list(board)
end = timeit.default_timer()
print(end - begin)

begin = timeit.default_timer()
print_board_for(board)
end = timeit.default_timer()
print(end - begin)
