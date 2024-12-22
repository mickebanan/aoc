data = """
1
2
3
2024
""".strip().splitlines()
data = open('data/22.dat').read().strip().splitlines()

cache = {}
patterns = set()
p1 = 0
for n in data:
    seed = n
    cache[seed] = {}
    n = int(n)
    prev = None
    pattern = ()
    for _ in range(2000):
        n ^= (n << 6) & 16777216 - 1
        n ^= (n >> 5) & 16777216 - 1
        n ^= (n << 11) & 16777216 - 1
        last = int(str(n)[-1])
        if prev is not None:
            diff = last - prev
        else:
            diff = last - int(seed[-1])
        if len(pattern) == 4:
            pattern = pattern[1:] + (diff,)
            if pattern not in cache[seed]:
                cache[seed][pattern] = last
                patterns.add(pattern)
        else:
            pattern = pattern + (diff,)
        prev = last
    p1 += n
print('part 1:', p1)

best = 0
for pattern in patterns:
    val = 0
    for v in cache.values():
        if pattern in v:
            val += v[pattern]
    if val > best:
        best = val
print('part 2:', best)