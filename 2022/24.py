import pprint

raw = """
#.####################################################################################################
#>^<.v^^v>>^>vv..<><v.<^<^<v.^>>^<>>><><<>^v^>.^<>><<^vv><^<>>vv^v.<.^v><<<>.<v><<^v<v^<>.<vv<>vv<<v>#
#<v<vv><^>v<><.<<^^<>^>v<^vvvv^<<v<<^.^.^>.<><^><<^v<^><<v>vv<<>>>^.^<>>>^vvv^><^v^^>>><<vvv>><<><><.#
#>.vv^^^<^>v>vvv>^.<v<>...v^<>v<><<..vvv<^<<v>^>^<^v^>><^^v.v>>><^.^>vv^^v>v<^^.vv<v<v<>>^^>v>vvv^v><#
#.<v>^^<^v^^<^>>^>><v>^vv>^<v<v^^<>^v><v<^<>>.v^>^.v^><vvv^.^.>vvv^.v.>.>^<^.<^>><^><v<<v>^^>><><^^^<#
#<^<<v^vvv>>><>^^>>v.v.v^^>^<>><^>>^^><v>v<^.^.v<..>>>.>>.<^<^^^>.<>^^.v^>>>v>v>^^v>^><>><<.^.^>vv^^.#
#<^^>^v><..v^v<^.<vv^v<.<>.<>.^v^>^^>>v^^v.<.^><>^v.^^v>v<^^vv<<^^v<>><>^<v>>^<><v^.>>>>^v.>v.><.>v>>#
#<>.<<v.><^><<>>v><><>^..^v^<v>v<v.<>^<>>^v.^^>>.v^.<v>v>.v.v<>v.<.vv<<^<>^^^^>>.<vv<><<>vv>^>.v^<^>>#
#<.^<vv<><v^^<^v^.<><>v>>>.<<v<<v>>v^..v<<>^>^v>>.<>>v<^>^>^<vvv<><<<..v><<<v>><v<^v^<<^vvv>^>^<v<vv<#
#>^>^v>><<>>.^<>>^.^<v>^>>.<v^>v<<>vv><.v<.^^^>v<v>.v^v^.>>^^^vvvv<^<^<v>^.^<>v<^.^<>v>>vv<>>^^^>v>><#
#>><^<<v<>>^<^>v>v^v><v<v><^v>v>^>^<>>^v>vv^>^v<vv^v>.<^><.vv^^^<^><..<<<>^>^.^>>>^<>.^<^>^<>^^v>v<v>#
#><<><v><v^v>.v>^.<^><^^v><<<<<.^>>.^^<v>v>>^<^<>.^.>>>.>>.^v>v.<^^v^<^<>v<>^^<v^><<^^^<><v^>v>v<^.v<#
#<v>.v<<><vvv^<>^^^<<v<v^v^><v.><<.^^>vvv^>^v>v><><<.v>v<<<><..>>v>>v><^^>^^.^>v.v..>^><^.<>^<<^<<v<<#
#<vv<<vvv<vv>v><<.v<v<><.>^vv.^<<<<<<<v<^<^v^v>.v><vv<v^>^^^.^vv<<v>.<<><>>><^<^.^<>^>^<>v.v.v^><v<<.#
#.>^.>vv<v<><vv^v.^v<.^.v<><>^^>^.>v^<><v<<><vv<<^v>^>v<>^v>v>>v<>^<v.<v^^<<v><<.^<^>.vv.>>^.vv<><v><#
#>>v>>>.v<v<^^>><^^v^>>v>v^>>^<v^^^^.vv.^vv<vv><v^v<>^v<>>>>^^v>^<v<v^<>><>.v>>v..^>..<v<<>.v<<.<^>v<#
#<><^>>v^<^^vv>v<v.>.v.<^v.^>vvv<^>v><^>v><><.v>>.^^>><<>.v^<<^.<.^^.<v><v.^.v<^^^^<^<^>vv<v<.v<<v<^>#
#<<^^<<^vvv<<<<.^vv^.><<vv>v^><>..^.^^v>v>^^<<v>^v.v>^v><>>^v><<.v>v<>^v<v<>v<^v^.^<vv>>^>v>^><<v><.<#
#<<>v.v>...^^.<<^>>.<>^^^v>^<^><v<<<><<vv^.v^>.v^.>>^<v>>^<v^^<v>>vv<<>.>>.v^v><.^v.>^>^><^^v^^v<v>^<#
#<^vv^<><<<v^^<^>>v><^<<v^^v^>>^>v<>.<>>v>v<><v.>v<><<<<.<<.<<>>>><><vv><^v<<<^>v<^<^^<v^><^<..v>.vv>#
#><^>>>.^.>v<^^>>vv<v><^<<v.<.>^<^<^v>vv>v^^><.^.^>>.v.>v^.>>^<>^^^>vvv>..v^vv<^v>>v<><><<<^^<<v>^^<>#
#>^<vv>^v<<.<<v>^><><>>v.>.^<>^^vv<<>>>v^<>>><<v.v>>^<<vv<^vvv><><.v><.vv^v^.v.>vv^<><.v^>vv.<<<v<><<#
#>v<^>>.>>v>v>><^>^>^.^>^>vv>^<<><^v.<vvv<^.><>>v>v>^<>><^>^^<>v>v>.<^v^>>>v^>vvv.>.>^<><>.v^vv><>^>>#
#>><>v^>^>>^>^^>^>^<^>>vv>>>>>>vvv.v>.^v<v<vvv<<>.<^v.vv.v>^>>vv<<v^>^^^^>>^v.^v>>v<vvv<.<>^^<^v<<<.<#
#<>vv<^v>v^<v>>^<<>v^>vvvv>v^><^>^v<v^^^>><^><<.^>v^vv.v<<<>..v<^<.vv>.v>^>>>^^v^v^<^v^<^^<<vv>.>.>><#
#<<<v><>v.><v>><v^<^>><>^<vv><<.<<<<.v^v>v>v>.><>.<v><^.<^>^^><v>vv.<v>.v.>>.^>^>v<^vvvv>><>^^v<^>v>.#
#>.^>^>.<v.v<.<>vv<v<>^v<.>^>v<^v^>.>^<^..v<>>v.v>^.v<^>>^^^<v.<>v><v.^v^.>vv<<^<v^<.^^^.^>>.v>.vv.^.#
#<^v><>.<^v<v<^v<vv^^>.>v^^<v>^<.<^^<<.^>vv^^<^>v<v<^<v^^>vv^v>v^^>>..v^>.<v>v>v<v^<>^<^><.>^>>><<v.<#
#>>^<vv.<<>v.<>v.^>>^^vv^<^>vv<^>v.v>>.^.v^.v<v>^<>^.>><^>v>.>>v^<^>.>>^v<<v<<^^<vvvvv><^>^>v^^^^>^v>#
#<^.>^v>^<>>^.^<>.>..><>.<v^v^vv^>v^..v<<><>>^.^><^^<^^<^v<<^<^>.<><^.>^<^vv^>>>>^^>>><v<<<<^><.>^>.<#
#.v<>><^^vv^<<v^v><<<v<<<v><>><>>v^>v>^^^v<<<<<<>.^v<>.^<><<^vv<^>>v.^><v>v<^v>^v><v>>v<^^>vv.^<^>.>.#
#>^<.>v^^^><<v><>^.>vvv>v^<^>v><<<><><.^>>.>vv.^<<<<<^<^>^>v<^^<^<><v<.<>v<<><<v<^>>v>>>^<>>>.<<^<^<<#
#>^^>.vv^><.>v<vv>^><>v><^<v.<v^>.^><v<v>v^>^<v^v>v<<v^^<^>.^<v<vv<.>>v>v^v.<vv^^^^><v>^<>^v^>vv>>vv>#
#><>^<^^>^>v<^^<vv^<<^>v<>>v^>^v.v.v>^^><^<<<<>v>vv<v>^^<v>>.v<><<^><^^<<>>>>^>v>^>><><^>v><^^><v^^>>#
#><<<v<v><>^vv.^<>^>><v>vv^v^v<<v.v<v^>>vvvv^v<^<v^.><^^v><><v<^^<>><<>v^vv<^>v><>><<<^>>^^<^>><>v<v<#
#>^v><>v<>>^v>^<v^<vv><>^^>>>>v><v^v^>>>v<^<<<<<v<^<>>v><^<<^^^<^<>v<>^<v><^.>>><<^v.<>v^^.>>^^.^>^v<#
####################################################################################################.#
""".strip().split('\n')
# raw = """
# #.######
# #>>.<^<#
# #.<..<<#
# #>v.><>#
# #<^v^^>#
# ######.#
# """.strip().split('\n')
blizzards = set()
walls = set()
for y, line in enumerate(raw):
    for x, c in enumerate(line):
        if c == '#':
            walls.add((x, y))
        elif c != '.':
            blizzards.add((x, y, c))
start = (next(i for i, c in enumerate(raw[0]) if c != '#'), 0)
stop = (next(i for i, c in enumerate(raw[-1]) if c != '#'), len(raw) - 1)
original_start = start
original_stop = stop
min_x = 1
max_x = len(raw[0]) - 2
min_y = 1
max_y = len(raw) - 2
edges = {
    '<': min_x,
    '>': max_x,
    '^': min_y,
    'v': max_y,
}
print('mins/maxes:', min_x, max_x, min_y, max_y)
print('start/stop:', start, stop)
original_configuration = blizzards.copy()


def get_next_moves(blizzards):
    next_moves = set()
    for x, y, c in blizzards:
        if c == '<':
            x = x - 1
            if x == 0:
                next_moves.add((max_x, y, c))
            else:
                next_moves.add((x, y, c))
        elif c == '>':
            x = x + 1
            if x == edges[c] + 1:
                next_moves.add((1, y, c))
            else:
                next_moves.add((x, y, c))
        elif c == '^':
            y = y - 1
            if y == 0:
                next_moves.add((x, max_y, c))
            else:
                next_moves.add((x, y, c))
        elif c == 'v':
            y = y + 1
            if y == edges[c] + 1:
                next_moves.add((x, 1, c))
            else:
                next_moves.add((x, y, c))
    return next_moves


def to_str(blizzards, expedition=None):
    print(raw[0])
    for y in range(1, len(raw) - 1):
        print('#', end='')
        for x in range(1, len(raw[0]) - 1):
            cnt = 0
            if (x, y) == expedition:
                output = 'E'
            else:
                output = '.'
                for c in '<', '>', 'v', '^':
                    if (x, y, c) in blizzards:
                        output = c
                        cnt += 1
            if cnt > 1:
                print(cnt, end='')
            else:
                print(output, end='')
        print('#')
    print(raw[-1])


def get_valid_moves(position, blizzard_positions):
    pos = []
    x, y = position
    if (x + 1, y) not in blizzard_positions and min_x <= (x + 1) <= max_x and min_y <= y <= max_y:
        pos.append((x + 1, y))
    if (x - 1, y) not in blizzard_positions and min_x <= (x - 1) <= max_x and min_y <= y <= max_y:
        pos.append((x - 1, y))
    if (x, y + 1) not in blizzard_positions and min_y <= (y + 1) <= max_y and min_x <= x <= max_x or (x, y + 1) == stop:
        pos.append((x, y + 1))
    if (x, y - 1) not in blizzard_positions and min_y <= (y - 1) <= max_y and min_x <= x <= max_x or (x, y - 1) == start:
        pos.append((x, y - 1))
    if position not in blizzard_positions:
        pos.append(position)
    return pos


def get_free_nodes(blizzards):
    free_nodes = {start, stop}
    blizzard_positions = {(x, y) for x, y, c in blizzards}
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if (x, y) not in blizzard_positions and (x, y) not in walls:
                free_nodes.add((x, y))
    return free_nodes


# def get_edge_stream():
#     global blizzards
#     t = 0
#     while True:
#         free_nodes = get_free_nodes(blizzards)
#         # print('free nodes:', free_nodes)
#         blizzards = get_next_moves(blizzards)
#         blizzard_positions = {(x, y) for x, y, c in blizzards}
#         # to_str(blizzards)
#         for node in free_nodes:
#             # print('node:', node)
#             for move in get_valid_moves(node, blizzard_positions):
#                 # print(' valid move:', move)
#                 yield node, move, t, 1, blizzards
#         t += 1


# iterations = 0
# time_max = 500
# to_str(blizzards)
#
# times = {}
# for y in range(1, len(raw) - 1):
#     for x in range(1, len(raw[0]) - 1):
#         times[(x, y)] = 1_000_000
# times[start] = 0
# times[stop] = 1_000_000
# import collections
# paths = collections.defaultdict(list)
# paths[start] = []
# for n1, n2, t, delta, blizzards in get_edge_stream():
#     if (t + delta) <= time_max and t >= times[n1]:
#         if (t + delta) < times[n2]:
#             times[n2] = t + delta
#             # print('arriving at', n2, 'in time', t + delta)
#             # to_str(blizzards, n2)
#             paths[n2] = paths[n1] + [(n1, t + delta)]
#     elif t >= time_max:
#         break
#     elif times[stop] < 1_000_000:
#         break

# pprint.pprint(times)
# print(times[stop])
# for row in paths[stop]:
#     print(row)
# 231 för lågt?

# nytt försök med traditionell algo
import math
cycles = math.lcm(max_x, max_y)
v2_free_nodes = set()
# blizzards = original_configuration.copy()

# print('FREE NODES')
# pprint.pprint(v2_free_nodes)


def v2_get_next_moves(node):
    x, y, t = node
    next_nodes = set()
    if (x, y, t + 1) in v2_free_nodes:
        next_nodes.add((x, y, t + 1))
    if (x + 1, y, t + 1) in v2_free_nodes:
        next_nodes.add((x + 1, y, t + 1))
    if (x - 1, y, t + 1) in v2_free_nodes:
        next_nodes.add((x - 1, y, t + 1))
    if (x, y + 1, t + 1) in v2_free_nodes:
        next_nodes.add((x, y + 1, t + 1))
    if (x, y - 1, t + 1) in v2_free_nodes:
        next_nodes.add((x, y - 1, t + 1))
    return next_nodes


def dfs(start, stop):
    visited = {start}
    q = [start]
    while q:
        v = q.pop(0)
        # print('popping', v)
        x, y, t = v
        if (x, y) == stop:
            # print('finished!')
            return v
        for next_node in v2_get_next_moves(v):
            # print(' next node;', next_node)
            if next_node not in visited:
                visited.add(next_node)
                q.append(next_node)


for t in range(cycles * 2):
    for x, y in get_free_nodes(blizzards):
        v2_free_nodes.add((x, y, t))
    blizzards = get_next_moves(blizzards)
start = (1, 0, 0)
v2_free_nodes.add(start)


first_stop = dfs(start, stop)
print('first stop:', first_stop)
v2_free_nodes.remove(start)
start = first_stop
v2_free_nodes.add(start)
stop = original_start
second_stop = dfs(start, stop)
print('second stop:', second_stop)
v2_free_nodes.remove(start)
start = second_stop
v2_free_nodes.add(start)
stop = original_stop
third_stop = dfs(start, stop)
print('third stop:', third_stop)