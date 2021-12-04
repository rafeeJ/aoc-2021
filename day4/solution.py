import numpy as np
from numpy.core.defchararray import array
f = open('input.txt', 'r')

l = [i for i in f]

bingo_line = [int(i) for i in l.pop(0).strip().split(',')]

boards = {}
c = 0

while len(l) != 0:
    board = []
    if l[0] == '\n':
        l.pop(0)
        for i in range(5):
            row = l.pop(0).strip().split(' ')
            board.append([int(i) for i in row if i])
    if len(board) == 0:
        break
    boards[c] = board
    c += 1

boards_two = boards.copy()

def remove_square(board, key):
    for i in board:
        for j,k in enumerate(i):
            if k == key:
                i[j] = 999
    return board

def check_board(board):
    bingo = False
    for row in board:
        if row == [999, 999, 999, 999, 999]:
            print('Bingo row!')
            bingo = True
    for column in np.transpose(board):
        if np.array_equal(column, [999, 999, 999, 999, 999]):
            print('Bingo column!')
            bingo = True
            break
    return bingo

def sum_board(board):
    count = 0
    for row in board:
        for num in row:
            if num != 999:
                count += num
    return count

## Solution one
for num in bingo_line:
    for j in boards.keys():
        boards[j] = remove_square(boards[j], num)

        if check_board(boards[j]):
            #print(boards[j])
            #print(sum_board(boards[j])*num)
            break

won = []
## Solution two
for num in bingo_line:
    for key in boards_two.keys():
        if key not in [i[0] for i in won]:
            boards_two[key] = remove_square(boards_two[key], num)
            if check_board(boards_two[key]):
                won.append((key, num))

sol = sum_board(boards_two[won[-1][0]]) * won[-1][1]
print(sol)