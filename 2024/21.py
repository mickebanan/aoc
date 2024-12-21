import itertools
import pprint

data = """
029A
980A
179A
456A
379A
""".strip().splitlines()
# data = open('data/21.dat').read().strip().splitlines()

class Keypad:
    pos = None
    layout = ['789', '456', '123', 'X0A']
    dirs = {'^': (-1, 0), 'v': (1, 0), '>': (0, 1), '<': (0, -1)}
    forbidden = None

    def __init__(self):
        self.pos = 'A'
        self.ymax = len(self.layout) - 1
        self.xmax = len(self.layout[0]) - 1
        self.forbidden = next((y, x) for y, row in enumerate(self.layout) for x, c in enumerate(row) if c == 'X')

    def get_moves(self, to):
        pos = next((y, x) for y, row in enumerate(self.layout) for x, c in enumerate(row) if c == self.pos)
        visited = {self.forbidden}
        q = [(pos, '', visited)]
        dist = abs(pos[0] - to[0]) + abs(pos[1] - to[1])
        while q:
            (y, x), sequence, visited = q.pop(0)
            if (y, x) in visited or (y, x) == self.pos or len(sequence) > dist:
                continue
            if (y, x) == to:
                yield sequence
            if sequence:
                visited.add((y, x, sequence[-1]))
            for d, (dy, dx) in self.dirs.items():
                if 0 <= y + dy <= self.ymax and 0 <= x + dx <= self.xmax:
                    q.append(((y + dy, x + dx), sequence + d, visited))

    def move(self, to):
        # print('move from {} to {}'.format(self.pos, to))
        ny, nx = next((y, x) for y, row in enumerate(self.layout) for x, c in enumerate(row) if c == to)
        # print('(%s, %s), (%s, %s)' % (y, x, ny, nx))
        for path in self.get_moves((ny, nx)):
            yield path + 'A'
        self.pos = self.layout[ny][nx]

    def get_all_sequences(self, input):
        sequences = []
        # print('getting sequences for', input)
        for i, c in enumerate(input):
            # print('doing input', c)
            moves = []
            for m in self.move(c):
                # print(m)
                moves.append(m)
            if i == 0:
                sequences = moves
            else:
                s = []
                for seq in sequences:
                    for m in moves:
                        s.append(seq + m)
                sequences = s
        # print(len(sequences), sequences[:50])
        return sequences


class Robot(Keypad):
    layout = ['X^A', '<v>']

p1_keypads = [Keypad(), Robot(), Robot()]

p1 = 0
for seq in data:
    results = [seq]
    for kp in p1_keypads:
        results = list(itertools.chain.from_iterable(kp.get_all_sequences(r) for r in results))
    results.sort(key=len)
    print(seq, len(results[0]))
    p1 += len(results[0]) * int(seq.replace('A', ''))
print(p1)
