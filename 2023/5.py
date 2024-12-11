import helpers

data = [
    'seeds: 79 14 55 13',
    'seed-to-soil map:',
    '50 98 2',
    '52 50 48',
    'soil-to-fertilizer map:',
    '0 15 37',
    '37 52 2',
    '39 0 15',
    'fertilizer-to-water map:',
    '49 53 8',
    '0 11 42',
    '42 0 7',
    '57 7 4',
    'water-to-light map:',
    '88 18 7',
    '18 25 70',
    'light-to-temperature map:',
    '45 77 23',
    '81 45 19',
    '68 64 13',
    'temperature-to-humidity map:',
    '0 69 1',
    '1 0 69',
    'humidity-to-location map:',
    '60 56 37',
    '56 93 4',
]
with open('input/5.dat') as f:
    data = [row.strip() for row in f.readlines()]

seeds = []
mapping = {}
mapping_inverse = {}
m = rm = None
for row in data:
    if not row:
        continue
    if not seeds:
        seeds = [int(a) for a in row.removeprefix('seeds: ').split()]
    else:
        if row.endswith(' map:'):
            m = row.removesuffix(' map:')
            rm = '-'.join(reversed(m.split('-')))
            mapping[m] = {}
            mapping_inverse[rm] = {}
        else:
            dest, source, length = row.split()
            dest = int(dest)
            source = int(source)
            length = int(length)
            mapping[m][(source, source + length - 1)] = dest
            mapping_inverse[rm][(dest, dest + length - 1)] = source


@helpers.timer
def p1():
    # part 1
    min_loc = None
    for seed in seeds:
        a = seed
        for m in ('seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water', 'water-to-light', 'light-to-temperature',
                  'temperature-to-humidity', 'humidity-to-location'):
            match = next((_m for _m in mapping[m] if _m[0] <= a <= _m[1]), None)
            if match:
                match_map = mapping[m][match]
                a = match_map + a - match[0]
        min_loc = min(a or min_loc, min_loc or a)
    print('part 1:', min_loc)


@helpers.timer
def p2():
    # part 2
    # Very slow but calculates the right answer by going backwards from potential locations and checking if
    # there's a matching seed.
    seed_intervals = [(seed_start, seed_start + seed_length - 1)
                      for seed_start, seed_length in zip(seeds[::2], seeds[1::2])]
    found = False
    for a in range(100000000):
        if found:
            break
        initial = a
        for m in ('location-to-humidity', 'humidity-to-temperature', 'temperature-to-light', 'light-to-water',
                  'water-to-fertilizer', 'fertilizer-to-soil', 'soil-to-seed'):
            match = next((_m for _m in mapping_inverse[m] if _m[0] <= a <= _m[1]), None)
            if match:
                match_map = mapping_inverse[m][match]
                a = match_map + a - match[0]
        for start, end in seed_intervals:
            if start <= a <= end:
                print(' final match:', initial)
                found = True


p1()
p2()  # 357 seconds. Not pretty.
