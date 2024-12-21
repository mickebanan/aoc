import functools

data = """
029A
980A
179A
456A
379A
""".strip().splitlines()
data = open('data/21.dat').read().strip().splitlines()
dirs = {'>': (0, 1), '<': (0, -1), '^': (-1, 0), 'v': (1, 0)}


class Keypad:
    layout = ['789', '456', '123', 'X0A']
    forbidden = (3, 0)


class Robot:
    layout = ['X^A', '<v>']
    forbidden = (0, 0)


def get_moves(start, end):
    keypad = Keypad if start.isdigit() or end.isdigit() else Robot
    pos = next((y, x) for y, row in enumerate(keypad.layout) for x, c in enumerate(row) if c == start)
    ny, nx = next((y, x) for y, row in enumerate(keypad.layout) for x, c in enumerate(row) if c == end)
    ymax = len(keypad.layout) - 1
    xmax = len(keypad.layout[0]) - 1
    visited = {keypad.forbidden}
    q = [(pos, '')]
    dist = abs(pos[0] - ny) + abs(pos[1] - nx)
    res = []
    while q:
        (y, x), sequence = q.pop(0)
        if (y, x) in visited or len(sequence) > dist:
            continue
        if (y, x) == (ny, nx):
            res.append(sequence + 'A')
        if sequence:
            visited.add((y, x, sequence[-1]))
        for d, (dy, dx) in dirs.items():
            if 0 <= y + dy <= ymax and 0 <= x + dx <= xmax:
                q.append(((y + dy, x + dx), sequence + d))
    return res


@functools.cache
def get_length(sequence, level):
    total = 0
    for i in range(len(sequence)):
        curr = 'A' if i == 0 else sequence[i - 1]
        following = sequence[i]
        moves = get_moves(curr, following)
        if level == 0:
            total += min(len(s) for s in moves)
            continue
        lengths = set()
        for move in moves:
            lengths.add(get_length(move, level - 1))
        total += min(lengths)
    return total


def run(levels):
    return sum(get_length(seq, levels) * int(seq.replace('A', '')) for seq in data)

print('part 1:', run(2))
print('part 2:', run(25))