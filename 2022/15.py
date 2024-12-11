raw = """
    Sensor at x=2, y=18: closest beacon is at x=-2, y=15
    Sensor at x=9, y=16: closest beacon is at x=10, y=16
    Sensor at x=13, y=2: closest beacon is at x=15, y=3
    Sensor at x=12, y=14: closest beacon is at x=10, y=16
    Sensor at x=10, y=20: closest beacon is at x=10, y=16
    Sensor at x=14, y=17: closest beacon is at x=10, y=16
    Sensor at x=8, y=7: closest beacon is at x=2, y=10
    Sensor at x=2, y=0: closest beacon is at x=2, y=10
    Sensor at x=0, y=11: closest beacon is at x=2, y=10
    Sensor at x=20, y=14: closest beacon is at x=25, y=17
    Sensor at x=17, y=20: closest beacon is at x=21, y=22
    Sensor at x=16, y=7: closest beacon is at x=15, y=3
    Sensor at x=14, y=3: closest beacon is at x=15, y=3
    Sensor at x=20, y=1: closest beacon is at x=15, y=3
""".strip().split('\n')
raw = """
Sensor at x=489739, y=1144461: closest beacon is at x=-46516, y=554951
Sensor at x=2543342, y=3938: closest beacon is at x=2646619, y=229757
Sensor at x=3182359, y=3999986: closest beacon is at x=3142235, y=3956791
Sensor at x=3828004, y=1282262: closest beacon is at x=3199543, y=2310713
Sensor at x=871967, y=3962966: closest beacon is at x=-323662, y=4519876
Sensor at x=1323641, y=2986163: closest beacon is at x=2428372, y=3303736
Sensor at x=2911492, y=2576579: closest beacon is at x=3022758, y=2461675
Sensor at x=3030965, y=2469848: closest beacon is at x=3022758, y=2461675
Sensor at x=3299037, y=3402462: closest beacon is at x=3142235, y=3956791
Sensor at x=1975203, y=1672969: closest beacon is at x=1785046, y=2000000
Sensor at x=3048950, y=2452864: closest beacon is at x=3022758, y=2461675
Sensor at x=336773, y=2518242: closest beacon is at x=1785046, y=2000000
Sensor at x=1513936, y=574443: closest beacon is at x=2646619, y=229757
Sensor at x=3222440, y=2801189: closest beacon is at x=3199543, y=2310713
Sensor at x=2838327, y=2122421: closest beacon is at x=2630338, y=2304286
Sensor at x=2291940, y=2502068: closest beacon is at x=2630338, y=2304286
Sensor at x=2743173, y=3608337: closest beacon is at x=2428372, y=3303736
Sensor at x=3031202, y=2452943: closest beacon is at x=3022758, y=2461675
Sensor at x=3120226, y=3998439: closest beacon is at x=3142235, y=3956791
Sensor at x=2234247, y=3996367: closest beacon is at x=2428372, y=3303736
Sensor at x=593197, y=548: closest beacon is at x=-46516, y=554951
Sensor at x=2612034, y=2832157: closest beacon is at x=2630338, y=2304286
Sensor at x=3088807, y=3929947: closest beacon is at x=3142235, y=3956791
Sensor at x=2022834, y=2212455: closest beacon is at x=1785046, y=2000000
Sensor at x=3129783, y=3975610: closest beacon is at x=3142235, y=3956791
Sensor at x=3150025, y=2333166: closest beacon is at x=3199543, y=2310713
Sensor at x=3118715, y=2376161: closest beacon is at x=3199543, y=2310713
Sensor at x=3951193, y=3181929: closest beacon is at x=4344952, y=3106256
Sensor at x=2807831, y=2401551: closest beacon is at x=2630338, y=2304286
Sensor at x=3683864, y=2906786: closest beacon is at x=4344952, y=3106256
Sensor at x=2723234, y=3206978: closest beacon is at x=2428372, y=3303736
Sensor at x=3047123, y=3891244: closest beacon is at x=3142235, y=3956791
Sensor at x=3621967, y=3793314: closest beacon is at x=3142235, y=3956791
Sensor at x=2384506, y=1814055: closest beacon is at x=2630338, y=2304286
Sensor at x=83227, y=330275: closest beacon is at x=-46516, y=554951
Sensor at x=3343176, y=75114: closest beacon is at x=2646619, y=229757
""".strip().split('\n')
sensors = set()
beacons = set()
for row in raw:
    s, b = row.split(':')
    s = s.strip().removeprefix('Sensor at')
    x, y = s.split(',')
    sensors.add((int(x.strip().removeprefix('x=')), int(y.strip().removeprefix('y='))))
    b = b.strip().removeprefix('closest beacon is at')
    x, y = b.split(',')
    beacons.add((int(x.strip().removeprefix('x=')), int(y.strip().removeprefix('y='))))
# print(sensors)
# print(beacons)
# search_space = [['.' for x in range(21)] for y in range(21)]
# for x, y in sensors:
#     try:
#         search_space[y][x] = 'S'
#     except IndexError:
#         pass
# for x, y in beacons:
#     try:
#         search_space[y][x] = 'B'
#     except IndexError:
#         pass


def get_distance(a, b):
    x1, y1 = a
    x2, y2 = b
    return abs(x1 - x2) + abs(y1 - y2)


distances = {}
for sensor in sensors:
    closest = None
    # print('checking', sensor)
    for beacon in beacons:
        d = get_distance(sensor, beacon)
        if not closest or d < closest:
            closest = d
    distances[sensor] = closest

min_x = min(x - d for (x, y), d in distances.items())
max_x = max(x + d for (x, y), d in distances.items())
min_y = min(y - d for (x, y), d in distances.items())
max_y = max(y + d for (x, y), d in distances.items())
print(min_x, max_x, min_y, max_y)

current_row = 0
limit = 4_000_001
# limit = 21
while current_row < limit:
    print('row:', current_row)
    row_contents = set()
    for sensor in sensors:
        x, y = sensor
        if y == current_row:
            row_contents.add((x, x))
        closest = distances[sensor]
        if y < current_row < y + closest:
            diff = y + closest - current_row
            # print(x, y, diff, 'intersecting from above')
            row_contents.add((x - diff, x + diff))
        elif y == current_row:
            diff = closest
            # print(x, y, diff, 'intersecting directly')
            row_contents.add((x - diff, x + diff))
        elif y > current_row > y - closest:
            diff = current_row - (y - closest)
            # print(x, y, diff, 'intersecting from below')
            row_contents.add((x - diff, x + diff))
        # make a map
        # i = 0
        # for yy in range(y - closest, y + closest + 1):
        #     for xx in range(x - i, x + i + 1):
        #         if (xx, yy) not in sensors and (xx, yy) not in beacons:
        #             try:
        #                 search_space[yy][xx] = '#'
        #             except IndexError:
        #                 pass
        #     if yy < y:
        #         i += 1
        #     else:
        #         i -= 1
        # end map
    for beacon in beacons:
        x, y = beacon
        if y == current_row:
            row_contents.add((x, x))
    row_contents = sorted(row_contents)
    # print('row contents', row_contents)
    stop = False
    last_x = None
    max_diff = 1
    for first, following in zip(row_contents, row_contents[1:]):
        x11, x12 = first
        # print(diff, max_diff)
        if not last_x or x12 > last_x:
            last_x = x12
        x21, x22 = following
        diff = x21 - x12
        # print(first, following, diff)
        if diff > 0:
            max_diff = max(max_diff, diff)
        if x21 > limit:
            break
        # calculate least overlapping area -> we can skip this far ahead
        # print(first, following, last_x)
        if x21 > last_x + 1 and 0 <= current_row < limit:
            print(first, following)
            stop = True
            print('row:', current_row, last_x + 1, max_diff)
            print('answer:', 4_000_000 * (last_x + 1) + current_row)
            break
        # for x1, x2 in available:
    current_row += max_diff
    # print('min diff:', max_diff)
    # current_row += 1
    if stop:
        break

# for line in search_space:
#     print(''.join(line))
# y 3041245, x 2949122 + 1 (min diff?! 52311)
