import collections
import copy
import itertools

from helpers import timer

data = """
2333133121414131402
""".strip()
data = open('data/9.dat').read().strip()
files = collections.defaultdict(list)
filetype = itertools.cycle((1, 0))
free_space = []
file_id = pos = 0
for c in data:
    if next(filetype):
        files[file_id].extend(list(range(pos, pos + int(c))))
        file_id += 1
    else:
        free_space.extend(list(range(pos, pos + int(c))))
    pos += int(c)

def group_free_space(free_space):
    # Group contiguous free space.
    d = {}
    first = cont = 0
    prev = None
    for i, v in enumerate(free_space):
        if not prev:
            first = prev = v
            cont += 1
            continue
        if v == prev + 1:
            prev = v
            cont += 1
        else:
            d[first] = cont
            first = prev = v
            cont = 1
    d[first] = cont  # Don't forget the last element.
    return d

@timer
def sort(files, free_space, part=1):
    files = copy.deepcopy(files)
    free_space = copy.deepcopy(free_space)
    for f in range(max(files), -1, -1):
        segments = files[f]
        if part == 1:
            for i in range(len(segments)):
                if min(free_space) > segments[-1]:
                    break
                next_free_space = next(iter(sorted(free_space)))
                space = free_space.pop(next_free_space) - 1
                segments.pop(-1)
                segments = segments[:i] + [next_free_space] + segments[i:]
                if space:
                    free_space[next_free_space + 1] = space
            files[f] = segments
        else:
            for pos, length in sorted(free_space.items()):
                if pos > segments[0]:
                    break
                if length >= len(segments):
                    space = length - len(segments)
                    del free_space[pos]
                    files[f] = range(pos, pos + len(segments))
                    if space:
                        free_space[pos + len(segments)] = space
                    break
    return files

free_space = group_free_space(free_space)
print('part 1:', sum(file * pos for file, segments in sort(files, free_space).items() for pos in segments))
print('part 2:', sum(file * pos for file, segments in sort(files, free_space, part=2).items() for pos in segments))
