import collections
import itertools
import re

data = [
    'NNCB',
    '',
    'CH -> B',
    'HH -> N',
    'CB -> H',
    'NH -> C',
    'HB -> C',
    'HC -> B',
    'HN -> C',
    'NN -> C',
    'BH -> H',
    'NC -> B',
    'NB -> B',
    'BN -> B',
    'BB -> N',
    'BC -> B',
    'CC -> N',
    'CN -> C',
]
with open('14.dat') as f:
    data = [row.strip() for row in f.readlines()]
template = list(data[0])
rules = {}
for row in data[2:]:
    m = re.match(r'(\w+) -> (\w+)', row)
    rules[m[1]] = m[2]
frequencies = collections.defaultdict(int)
for letter in template:
    frequencies[letter] += 1
t = collections.defaultdict(int)
for pair in itertools.pairwise(template):
    pair = ''.join(pair)
    t[pair] += 1
template = t

for step in range(40):
    if step == 10:
        order = sorted(frequencies.items(), key=lambda x: x[1])
        print('part 1:', order[-1][-1] - order[0][-1])
    t = collections.defaultdict(int)
    for pair, n in template.items():
        r = rules.get(pair)
        if r:
            frequencies[r] += n
            p1 = pair[0] + r
            p2 = r + pair[1]
            t[p1] += n
            t[p2] += n
    template = t
order = sorted(frequencies.items(), key=lambda x: x[1])
print('part 2:', order[-1][-1] - order[0][-1])
