import re

data = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
data = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
data = open('data/3.dat').read()

p1 = p2 = 0
do = True
for m in re.finditer(r'do\(\)|don\'t\(\)|mul\((\d+),(\d+)\)', data):
    if m.group(0).startswith('mul'):
        value = int(m.group(1)) * int(m.group(2))
        p1 += value
    else:
        do = False if m.group(0) == "don't()" else True
        continue
    if do:
        p2 += value
print('part 1:', p1)
print('part 2:', p2)
