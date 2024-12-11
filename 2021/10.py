from bisect import insort
from collections import deque

data = [
    '[({(<(())[]>[[{[]{<()<>>',
    '[(()[<>])]({[<{<<[]>>(',
    '{([(<{}[<>[]}>{[]{[(<()>',
    '(((({<>}<{<{<>}{[]{[]{}',
    '[[<[([]))<([[{}[[()]]]',
    '[{[{({}]{}}([{[{{{}}([]',
    '{<[[]]>}<{[{[{[]{()[[[]',
    '[<(<(<(<{}))><([]([]()',
    '<{([([[(<>()){}]>(<<{{',
    '<{([{{}}[<[[[<>{}]]]>[]]',
]
with open('10.dat') as f:
    data = [row.strip() for row in f.readlines()]
charmap = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}


def work(part_1=True):
    corrupted = {c: 0 for c in charmap.values()}
    endings = []
    for line in data:
        q = deque()
        is_corrupt = False
        for char in line:
            if char in charmap:
                q.append(char)
            else:
                a = q.pop()
                if char != charmap[a]:
                    corrupted[char] += 1
                    is_corrupt = True
                    break
        if q and not is_corrupt:
            endings.append(''.join(charmap[c] for c in reversed(q)))
    if part_1:
        return corrupted
    else:
        return endings


def p1():
    points = {')': 3, ']': 57, '}': 1197, '>': 25137}
    corrupted = work()
    print('part 1:', sum(n * points[c] for c, n in corrupted.items()))


def p2():
    points = {')': 1, ']': 2, '}': 3, '>': 4}
    endings = work(part_1=False)
    scores = []
    for ending in endings:
        s = 0
        for char in ending:
            s *= 5
            s += points[char]
        insort(scores, s)
    print('part 2:', scores[len(scores) // 2])


p1()
p2()
