import collections
import re

data = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
""".strip().split('\n')
data = open('data/5.dat').read().strip().split('\n')
rules = collections.defaultdict(list)
updates = []
for row in data:
    if not row:
        continue
    m = re.match(r'(\d+)\|(\d+)', row)
    if m:
        rules[m.group(1)].append(m.group(2))
    else:
        updates.append(row.split(','))

p1 = p2 = 0
for update in updates:
    error = False
    sort_key = {}
    for i, instruction in enumerate(update):
        rest = update[i+1:]
        others = update[:i] + rest
        sort_key[instruction] = len(set(others) - set(rules[instruction]))
        for r in rest:
            if r not in rules[instruction]:
                error = True
    if not error:
        p1 += int(update[len(update)//2])
    else:
        update.sort(key=lambda v: sort_key.get(v))
        p2 += int(update[len(update)//2])
print('part 1:', p1)
print('part 2:', p2)
