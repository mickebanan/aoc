data = [
    '2-4,6-8',
    '2-3,4-5',
    '5-7,7-9',
    '2-8,3-7',
    '6-6,4-6',
    '2-6,4-8',
]


def generate(pair):
    a, b = pair.split('-')
    a = int(a)
    b = int(b)
    return set(range(a, b + 1))

cnt = 0
with open('4.input') as f:
    for row in f:
        first, second = row.split(',')
        first = generate(first)
        second = generate(second)
        if first.intersection(second):
        # if first.issubset(second) or second.issubset(first):
            cnt += 1
print(cnt)
