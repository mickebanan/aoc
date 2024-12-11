import collections

import helpers

data = [
    '32T3K 765',
    'T55J5 684',
    'KK677 28',
    'KTJJT 220',
    'QQQJA 483',
]
with open('input/7.dat') as f:
    data = [row.strip() for row in f.readlines()]


class Hand:
    bid = None
    hand = None
    type = None
    card_ranks = None

    def __init__(self, hand, bid, part_2=False):
        def get_type(counts):
            if self.hand == 'JJJJJ':
                self.type = 'five-of-a-kind'
            elif next((card for card, count in counts.items() if count == 5), None):
                self.type = 'five-of-a-kind'
            elif next((card for card, count in counts.items() if count == 4), None):
                self.type = 'four-of-a-kind'
            elif c1 := next((card for card, count in sorted(counts.items(), key=lambda k: self.card_ranks.index(k[0]))
                             if count == 3), None):
                if next((card for card, count in counts.items() if card != c1 and count == 2), None):
                    self.type = 'full-house'
                else:
                    self.type = 'three-of-a-kind'
            elif c1 := next((card for card, count in sorted(counts.items(), key=lambda k: self.card_ranks.index(k[0]))
                             if count == 2), None):
                if next((card for card, count in counts.items() if card != c1 and count == 2), None):
                    self.type = 'two-pairs'
                else:
                    self.type = 'pair'
            else:
                self.type = 'no-type'
        if part_2:
            self.card_ranks = ('J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A')
        else:
            self.card_ranks = ('2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A')
        self.hand = hand
        self.bid = int(bid)
        counts = collections.defaultdict(int)
        for card in hand:
            counts[card] += 1
        get_type(counts)
        if part_2:
            # Add the J value to whatever would yield the best results.
            j = counts.pop('J', 0)
            if c := next((card for card, val in counts.items() if val >= 3), None):
                counts[c] += j
            elif c1 := next((card for card, val in counts.items() if val == 2), None):
                if c2 := next((card for card, val in counts.items() if val == 2 and card != c1), None):
                    if self.card_ranks.index(c1) < self.card_ranks.index(c2):
                        counts[c2] += j
                    else:
                        counts[c1] += j
                else:
                    counts[c1] += j
            else:  # Nothing better available, just make a pair of the highest card we have.
                for r in reversed(self.card_ranks):
                    if r in counts:
                        counts[r] += j
                        break
            get_type(counts)  # Recalculate type based on the new counts with joker values added.

    def __lt__(self, other):
        order = ('no-type', 'pair', 'two-pairs', 'three-of-a-kind', 'full-house', 'four-of-a-kind', 'five-of-a-kind')
        t1 = self.type
        t2 = other.type
        if t1 == t2:
            for c1, c2 in zip(self.hand, other.hand):
                if c1 == c2:
                    continue
                return self.card_ranks.index(c1) < self.card_ranks.index(c2)
        else:
            return order.index(t1) < order.index(t2)

    def __str__(self):
        return '%s (%s)' % (self.hand, self.bid)


def p1():
    hands = []
    for row in data:
        hand, bid = row.split()
        h = Hand(hand, bid)
        hands.append(h)
    hands.sort()
    s = sum(i * h.bid for i, h in enumerate(hands, start=1))
    print('p1 total score:', s)


def p2():
    hands = []
    for row in data:
        hand, bid = row.split()
        h = Hand(hand, bid, part_2=True)
        hands.append(h)
    hands.sort()
    s = sum(i * h.bid for i, h in enumerate(hands, start=1))
    print('p2 total score:', s)


p1()
p2()
