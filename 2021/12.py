import collections

import helpers

data = [
    'start-A',
    'start-b',
    'A-c',
    'A-b',
    'b-d',
    'A-end',
    'b-end',
]
data = [
    'dc-end',
    'HN-start',
    'start-kj',
    'dc-start',
    'dc-HN',
    'LN-dc',
    'HN-end',
    'kj-sa',
    'kj-HN',
    'kj-dc',
]
data = [
    'fs-end',
    'he-DX',
    'fs-he',
    'start-DX',
    'pj-DX',
    'end-zg',
    'zg-sl',
    'zg-pj',
    'pj-he',
    'RW-he',
    'fs-DX',
    'pj-RW',
    'zg-RW',
    'start-pj',
    'he-WI',
    'zg-he',
    'pj-fs',
    'start-RW',
]
data = [
    'mx-IQ',
    'mx-HO',
    'xq-start',
    'start-HO',
    'IE-qc',
    'HO-end',
    'oz-xq',
    'HO-ni',
    'ni-oz',
    'ni-MU',
    'sa-IE',
    'IE-ni',
    'end-sa',
    'oz-sa',
    'MU-start',
    'MU-sa',
    'oz-IE',
    'HO-xq',
    'MU-xq',
    'IE-end',
    'MU-mx',
]
paths = collections.defaultdict(set)
small_rooms = {}
for row in data:
    a, b = row.split('-')
    paths[a].add(b)
    paths[b].add(a)
    if a.islower() and a not in ('start', 'end'):
        small_rooms[a] = 0
    if b.islower() and b not in ('start', 'end'):
        small_rooms[b] = 0


def visit1(visited, room, path=None):
    if not path:
        path = []
    path.append(room)
    visited.add(room)
    if room == 'end':
        yield path
    else:
        for next_room in paths[room]:
            if next_room.isupper() or next_room not in visited:
                yield from visit1(visited.copy(), next_room, path=path[:])


def visit2(small_rooms, room, path=None):
    if not path:
        path = []
    path.append(room)
    if room.islower() and room not in ('start', 'end'):
        small_rooms[room] += 1
    if room == 'end':
        yield path
    else:
        for next_room in paths[room]:
            if next_room == 'start':
                continue
            if (next_room.isupper()
                    or next_room == 'end'
                    or small_rooms[next_room] == 0
                    or not any(v for v in small_rooms.values() if v > 1)):
                yield from visit2(small_rooms.copy(), next_room, path=path[:])


def p1():
    s = 0
    for v in visit1(set(), 'start'):
        s += 1
    print('part 1:', s)


@helpers.timer
def p2():
    s = 0
    for v in visit2(small_rooms, 'start'):
        s += 1
    print('part 2:', s)


p1()
p2()
