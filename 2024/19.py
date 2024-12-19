import functools

data = """
r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb
""".strip().split('\n\n')
data = open('data/19.dat').read().strip().split('\n\n')
towels = [t.strip() for t in data[0].split(',')]
designs = data[1].split('\n')

@functools.cache
def find(design):
    if len(design) == 0:
        return 1
    else:
        return sum(find(design.removeprefix(pattern)) for pattern in towels if design.startswith(pattern))

p1 = p2 = 0
for design in designs:
    if value := find(design):
        p1 += 1
        p2 += value

print('part 1:', p1)
print('part 2:', p2)