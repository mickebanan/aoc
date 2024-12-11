import collections

data = """125 17""".split()
data = open('data/11.dat').read().strip().split()

def count(n):
    d = collections.Counter(data)
    for i in range(n):
        g = collections.Counter()
        for k, v in d.items():
            if k == '0':
                g['1'] += v
            elif len(k) % 2 == 0:
                k1, k2 = k[:len(k)//2], k[len(k)//2:]
                g[str(int(k1))] += v
                g[str(int(k2))] += v
            else:
                g[str(int(k) * 2024)] += v
        d = g
    return sum(d.values())

print('part 1:', count(25))
print('part 2:', count(75))