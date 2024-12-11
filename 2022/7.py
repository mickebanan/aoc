import collections

data = [
    '$ cd /',
    '$ ls',
    'dir a',
    '14848514 b.txt',
    '8504156 c.dat',
    'dir d',
    '$ cd a',
    '$ ls',
    'dir e',
    '29116 f',
    '2557 g',
    '62596 h.lst',
    '$ cd e',
    '$ ls',
    '584 i',
    '$ cd ..',
    '$ cd ..',
    '$ cd d',
    '$ ls',
    '4060174 j',
    '8033020 d.log',
    '5626152 d.ext',
    '7214296 k',
]

cd = '/'
is_listing = False
tree = collections.defaultdict(list)
with open('7.input') as f:
    for line in f:
        parts = line.split()
        if parts[0] == '$':
            is_listing = False
            cmd = parts[1]
            if len(parts) > 2:
                args = parts[2]
            else:
                args = None
            if cmd == 'cd':
                if args == '/':
                    cd = '/'
                elif args == '..':
                    cd = cd.split('/')
                    cd = '/'.join(cd[:-2]) + '/'
                else:
                    cd += args + '/'
            elif cmd == 'ls':
                is_listing = True
        elif is_listing:
            tree[cd].append(parts)

import pprint
pprint.pprint(tree)


def traverse(dir):
    for filetype, name in tree[dir]:
        if filetype == 'dir':
            yield from traverse(dir + name + '/')
        else:
            yield int(filetype)


maxsize = 70_000_000
needed = 30_000_000
used = sum(s for s in traverse('/'))
free = maxsize - used
totsize = 0
candidates = []
print('used size now:', used, 'free:', free)
for dir in tree:
    size = sum(s for s in traverse(dir))
    print(dir, size, free + size)
    if free + size > needed and dir != '/':
        candidates.append([dir, size])
    if size < 100_000:
        totsize += size
print(used, free, totsize)

print('candidates:')
pprint.pprint(candidates)
print('smallest:')
print(next(iter(sorted(candidates, key=lambda v: v[1]))))
