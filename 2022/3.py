import itertools

data = [
    'vJrwpWtwJgWrhcsFMMfFFhFp',
    'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
    'PmmdzqPrVvPwwTWBwg',
    'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
    'ttgJtRGJQctTZtZT',
    'CrZsJsPPZsGzwwsLwLmpwMDw',
]


def prio(char):
    if char == char.lower():
        return ord(char) - 96
    return ord(char) - 38


def batched(iterable, n):
    "Batch data into lists of length n. The last batch may be shorter."
    # batched('ABCDEFG', 3) --> ABC DEF G
    it = iter(iterable)
    while batch := list(itertools.islice(it, n)):
        yield batch

# s = 0
# for row in batched(data, 3):
#     match = next(iter(set(row[0]).intersection(set(row[1]).intersection(set(row[2])))))
#     print(match, prio(match))


s = 0
with open('3.input') as f:
    for row in batched(f, 3):
        # middle = int(len(row) / 2)
        # first, second = row[:middle], row[middle:]
        # match = next(iter(set(first).intersection(set(second))))
        match = next(iter(set(row[0].strip()).intersection(set(row[1].strip()).intersection(set(row[2].strip())))))
        s += prio(match)
print(s)