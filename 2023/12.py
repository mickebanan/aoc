import functools

data = [
    '???.### 1,1,3',
    '.??..??...?##. 1,1,3',
    '?#?#?#?#?#?#?#? 1,3,1,6',
    '????.#...#... 4,1,1',
    '????.######..#####. 1,6,5',
    '?###???????? 3,2,1',
    '???#.????#?? 1,1,1,1',
]
with open('input/12.dat') as f:
    data = [row.strip() for row in f.readlines()]


@functools.cache
def parse(s, checksum):
    if not checksum:
        return 1 if '#' not in s else 0
    elif not s:
        return 0
    ck = checksum[0]

    def hash():
        a = s[:ck].replace('?', '#')
        if a != '#' * ck:
            return 0
        if not s[len(a):].startswith('#'):
            return parse(s[len(a) + 1:], checksum[1:])
        else:
            return 0

    def dot():
        return parse(s[1:], checksum)

    for i, c in enumerate(s):
        if c == '.':
            return dot()
        elif c == '#':
            return hash()
        elif c == '?':
            return hash() + dot()


p1 = p2 = 0
for row in data:
    value, checksum = row.split()
    checksum = [int(a) for a in checksum.split(',')]
    p1 += parse(value, tuple(checksum))
    value = '?'.join([value] * 5)
    checksum = [checksum * 5][0]
    p2 += parse(value, tuple(checksum))
print('part 1:', p1)
print('part 2:', p2)

