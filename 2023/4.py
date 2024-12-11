import collections
import re

data = [
    'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',
    'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',
    'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1',
    'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83',
    'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36',
    'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11',
]
with open('input/4.dat') as f:
    data = [line.strip() for line in f.readlines()]


def work():
    s = 0
    copies = collections.defaultdict(int)
    for row in data:
        m = re.match(r'Card\s+(\d+): ([\d ]+) \| ([\d ]+)', row)
        card, winning, hand = m.groups()
        card = int(card)
        winning = {w for w in winning.split()}
        hand = {h for h in hand.split()}
        matches = len(hand & winning)
        points = 0.5
        copies[card] += 1
        if matches:
            for next_card in range(card + 1, card + matches + 1):
                points *= 2
                copies[next_card] += copies[card]
            s += points
    return int(s), sum(copies.values())


s1, s2 = work()
print('part 1:', s1)
print('part 2:', s2)
