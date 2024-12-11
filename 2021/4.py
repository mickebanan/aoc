import copy

import helpers

data = [
    '7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1',
    '',
    '22 13 17 11  0',
    ' 8  2 23  4 24',
    '21  9 14 16  7',
    ' 6 10  3 18  5',
    ' 1 12 20 15 19',
    '',
    ' 3 15  0  2 22',
    ' 9 18 13 17  5',
    '19  8  7 25 23',
    '20 11 10 24  4',
    '14 21 16 12  6',
    '',
    '14 21 17 24  4',
    '10 16 15  9 19',
    '18  8 23 26 20',
    '22 11 13  6  5',
    ' 2  0 12  3  7',
]
with open('4.dat') as f:
    data = [row.strip() for row in f.readlines()]
draws = [int(a) for a in data[0].split(',')]
boards = []
board = []
for row in data[1:]:
    if not row:
        if board:
            boards.append(board)
            board = []
        continue
    row = [(int(a), False) for a in row.split()]
    board.append(row)
boards.append(board)


def check_row(row):
    if all(marked for value, marked in row):
        return True


def transpose(board):
    return list(zip(*board))


def unmarked_sum(board):
    return sum(value for row in board for value, marked in row if not marked)


@helpers.timer
def play(boards, part_2=False):
    boards_left = [i for i in range(len(boards))]
    for draw in draws:
        for i, board in enumerate(boards):
            for row in board:
                for x, (value, marked) in enumerate(row):
                    if value == draw:
                        row[x] = (value, True)
                        if check_row(row) or check_row(transpose(board)[x]):
                            if not part_2:
                                return i, value
                            try:
                                boards_left.remove(i)
                            except ValueError:
                                pass
                            if not boards_left:
                                return i, value


def p1():
    bc = copy.deepcopy(boards)
    b, draw = play(bc)
    unmarked = unmarked_sum(bc[b])
    print('winning board:', b)
    print('result:', unmarked * draw)


def p2():
    bc = copy.deepcopy(boards)
    b, draw = play(bc, part_2=True)
    unmarked = unmarked_sum(bc[b])
    print('winning board:', b)
    print('result:', unmarked * draw)


p1()
p2()
