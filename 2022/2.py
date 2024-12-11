data = [
    'A Y',
    'B X',
    'C Z',
]

points = {'X': 1, 'Y': 2, 'Z': 3}


def play(hand):
    # Return our points based on this hand.
    his, mine = hand.strip().split()
    points = {'X': 1, 'Y': 2, 'Z': 3}[mine]
    if (his == 'A' and mine == 'Y'
            or his == 'B' and mine == 'Z'
            or his == 'C' and mine == 'X'):
        points += 6
    elif (his == 'A' and mine == 'X'
            or his == 'B' and mine == 'Y'
            or his == 'C' and mine == 'Z'):
        points += 3
    return points


def play2(hand):
    his, result = hand.strip().split()
    mine = None
    points_map = {'A': 1, 'B': 2, 'C': 3}
    points = 0
    if result == 'X':
        # need to lose
        mine = {'A': 'C', 'B': 'A', 'C': 'B'}[his]
    elif result == 'Y':
        # need to draw
        mine = his
        points += 3
    else:
        # need to win
        points += 6
        mine = {'A': 'B', 'B': 'C', 'C': 'A'}[his]
    points += points_map[mine]
    return points


if __name__ == '__main__':
    # for row in data:
    #     print(row, play2(row))

    with open('2.input') as f:
        points = 0
        for row in f:
            points += play2(row)
    print(points)