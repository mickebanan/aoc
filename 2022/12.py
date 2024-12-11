import copy

map = [
    'Sabqponm',
    'abcryxxl',
    'accszExk',
    'acctuvwj',
    'abdefghi',
]
map = [
    'abcccccccccaaaaaaaaaaccccccccccccaaaaaaaaccaaccccccccccccccccccccccccccccccccccccccccccccaaaaaa',
    'abccccccccccaaaaaaaaaccccccccccccaaaaaaaaaaaacccccccccccaacccacccccccccccccccccccccccccccaaaaaa',
    'abcccccccccccaaaaaaacccccccccccccaaaaaaaaaaaaaacccccccccaaacaacccccccccaaaccccccccccccccccaaaaa',
    'abccccccccccaaaaaaccccccccccccccaaaaaaaaaaaaaaaccccccccccaaaaaccccccccccaaacccccccccccccccccaaa',
    'abccccccccccaaaaaaaccccccccccccaaaaaaaaaaaaaacccccccccccaaaaaacccccccccaaaacccccccccccccccccaac',
    'abaaccaaccccaaccaaaccccccccaaaaaaaaaaaaaaacaaccccccccccaaaaaaaacccccccccaaalcccccccccccccccaaac',
    'abaaaaaacccccccccaaccccccccaaaaaacccaaaacccaaccccccccccaaaaaaaaccccccccalllllllcccccccccccccccc',
    'abaaaaaacccccccaaacccccccccaaaaccccccaaaccccaaaaacccccccccaacccccccaaaakllllllllcccccccaacccccc',
    'abaaaaaacccccccaaaacccccccccaacccccccaaaccccaaaaacccccccccaacccccccaakkklllpllllccccacaaacccccc',
    'abaaaaaaaccccccaaaaccccaaccccccccccccccccccaaaaaaccccccccccccccccccckkkkpppppplllcccaaaaaaacccc',
    'abaaaaaaacaaaccaaaaccaaaaaaccccccccccccccccaaaaaacccccccaaaccccckkkkkkkpppppppplllcddaaaaaacccc',
    'abcaaaacccaacccccccccaaaaaacccccaaaccccccccaaaaaacccccccaaaaccjkkkkkkkpppppuppplmmdddddaaaccccc',
    'abccaaaaaaaaaccccccccaaaaaaccccaaaaaacccccccaaacccccccccaaaajjjkkkkkrpppuuuuupppmmmdddddacccccc',
    'abccccaaaaaaaacccccccaaaaacccccaaaaaacccccccccccccccccccaaacjjjjrrrrrrppuuuuupqqmmmmmddddaccccc',
    'abccccaaaaaaaaacccccccaaaacccccaaaaaaccccccccccccccccccccccjjjrrrrrrrrpuuuxuvvqqqmmmmmddddccccc',
    'abccccaaaaaaaaacccccccccccccccccaaaaaccccaacccaccccccccaaccjjjrrrruuuuuuuxxyvvqqqqqmmmmmdddcccc',
    'abccccaaaaaaaacccccccccaaaccccccaacaaccccaaacaacccaaacaaaccjjjrrrtuuuuuuuxxyvvvqqqqqmmmmdddcccc',
    'abccaaaaaaaacccccccccccaaaaaccccccccccccccaaaaacccaaaaaaaccjjjrrttttxxxxxxyyvvvvvqqqqmmmmdeeccc',
    'abccaaaccaaaccccccccaacaaaaacccccccccccccaaaaaacccaaaaaacccjjjrrtttxxxxxxxyyvvvvvvvqqqmmmeeeccc',
    'abaaaaaaaaaacccaaaccaaaaaaaaaaaccaaaccccaaaaaaaacccaaaaaaaajjjqqrttxxxxxxxyyyyyyvvvqqqnnneeeccc',
    'SbaaaaaaaaccccaaaaccaaaaaaaaaaaaaaaaacccaaaaaaaaccaaaaaaaaacjjjqqtttxxxxEzzyyyyvvvvqqqnnneeeccc',
    'abcaaaaaacccccaaaaccccaaaaaaaccaaaaaaccccccaaccccaaaaaaaaaaciiiqqqtttxxxyyyyyyvvvvrrrnnneeecccc',
    'abcaaaaaacccccaaaacccaaaaaaaaccaaaaaaccccccaaccccaaacaaacccciiiqqqqttxxyyyyyywvvvrrrnnneeeecccc',
    'abcaaaaaaccccccccccccaaaaaaaaacaaaaacccccccccccccccccaaaccccciiiqqtttxxyyyyyywwrrrrnnnneeeccccc',
    'abcaaacaacccccaacccccaaaaaaaaacaaaaacccccccccccccccccaaaccccciiiqqttxxxywwyyywwrrrnnnneeecccccc',
    'abccccccccaaacaaccccccccccacccccccccccccccccccccccccccccccccciiqqqttxxwwwwwwywwrrrnnneeeccccccc',
    'abccaacccccaaaaaccccccccccccccccccccccccccccccccccccccccaacaaiiqqqttwwwwsswwwwwrrrnnfffeccccccc',
    'abaaaaccccccaaaaaacccccccccccccccccccccccccccccaaaccccccaaaaaiiqqqttssssssswwwwrrronfffaccccccc',
    'abaaaaaacccaaaaaaacccccccccccccccccccccccccccaaaaaacccccaaaaaiiqqqssssssssssswrrrooofffaaaacccc',
    'abaaaaaaccaaaaaacccccccccccccccccccccccccccccaaaaaacccccaaaaaiiqqqppssspppssssrrrooofffaaaacccc',
    'abaaaaaaccaacaaacccccccccccccccccccccccccccccaaaaaacccccaaaaaiihpppppppppppossrrooofffaaaaacccc',
    'abaaaaccccccccaacccccccccccccccccccccccccccccaaaaaccccccccaaahhhhppppppppppoooooooofffaaaaccccc',
    'abaaaaccccccccccaacccccccccccccccccaaacccccccaaaaacccccccccccchhhhhhhhhhggpoooooooffffaaaaccccc',
    'abccaacccccccacaaaccccccccccccccccaaaaacccccccccccccccccccccccchhhhhhhhhggggoooooffffaacaaacccc',
    'abccccccccccaaaaacaaccccccccccccccaaaaaccccccccccccccccccccccccchhhhhhhhggggggggggffcaacccccccc',
    'abccccccccccaaaaaaaaccccccccccccccaaaacccaacccccccccccaccccccccccccccaaaaaggggggggfcccccccccccc',
    'abccccccccccccaaaaaccccaacccccccccaaaacaaaaccccccccaaaaccccccccccccccaaaacaaagggggcccccccccaccc',
    'abcccccccccccaaaaacccccaacccccccccaaaaaaaaaccccccccaaaaaaccccccccccccaaaccaaaacccccccccccccaaac',
    'abcccccccccccaacaaccaaaaaaaacccaaaaaaaaaaaccccccccccaaaaccccccccccccccaccccaaacccccccccccccaaaa',
    'abccccccccccccccaaccaaaaaaaaccaaaaaaaaaaaccccccccccaaaaacccccccccccccccccccccacccccccccccccaaaa',
    'abccccccccccccccccccccaaaaacccaaaaaaaaaaaacccccccccaacaacccccccccccccccccccccccccccccccccaaaaaa',
]
start = end = None
starts = set()
max_x = len(map[0]) - 1
max_y = len(map) - 1
print('max x/y', max_x, max_y)
_unvisited = set()
_distances = {}
for i, row in enumerate(map):
    for j, column in enumerate(row):
        if column == 'S' or column == 'a':
            starts.add((i, j))
            start = (i, j)
        elif column == 'E':
            end = (i, j)
        _unvisited.add((i, j))
        _distances[(i, j)] = None


def get_node_value(location):
    y, x = location
    if location == start:
        elevation = 'a'
    elif location == end:
        elevation = 'z'
    else:
        elevation = map[y][x]
    return ord(elevation)


def get_neighbors(location):
    neighbors = set()
    y, x = location
    value = get_node_value(location) + 1
    if y < max_y and value >= get_node_value((y + 1, x)):
        neighbors.add((y + 1, x))  # one down
    if y > 0 and value >= get_node_value((y - 1, x)):
        neighbors.add((y - 1, x))  # one up
    if x < max_x and value >= get_node_value((y, x + 1)):
        neighbors.add((y, x + 1))  # one right
    if x > 0 and value >= get_node_value((y, x - 1)):
        neighbors.add((y, x - 1))  # one left
    return neighbors

# TODO: man borde istället hålla reda på en current shortest path och kolla för varje node ifall man
#  kommer in på den, isåfall vet man genast vad resten kommer att bli och kan sluta sökningen där
results = []
print('starting positions:', len(starts))
shortest = None
for start in starts:
    print('starting from', start)
    distances = copy.deepcopy(_distances)
    distances[start] = 0
    unvisited = copy.deepcopy(_unvisited)
    while unvisited:
        try:
            node = next(iter(sorted([k for k, v in distances.items() if v is not None and k in unvisited],
                                    key=lambda k: distances[k])))
        except StopIteration:
            break  # no possible path
        unvisited.remove(node)
        unvisited_neighbors = get_neighbors(node).intersection(unvisited)
        y, x = node
        if node == end:
            print('done!')
            break
        for n in unvisited_neighbors:
            alt = distances[node] + 1
            if shortest and alt > shortest:
                break
            if not distances[n] or alt < distances[n]:
                distances[n] = alt
    if distances[end]:
        shortest = min(shortest or distances[end], distances[end] or shortest)
        results.append(distances[end])
print(results, shortest)
