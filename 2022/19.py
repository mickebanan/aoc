import collections
import pprint
import re
import sys

data = """
Blueprint 1: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 2 ore and 20 clay. Each geode robot costs 4 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 19 clay. Each geode robot costs 3 ore and 8 obsidian.
Blueprint 3: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 2 ore and 14 clay. Each geode robot costs 4 ore and 15 obsidian.
Blueprint 4: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 2 ore and 16 clay. Each geode robot costs 2 ore and 8 obsidian.
Blueprint 5: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 4 ore and 8 obsidian.
Blueprint 6: Each ore robot costs 4 ore. Each clay robot costs 3 ore. Each obsidian robot costs 2 ore and 7 clay. Each geode robot costs 3 ore and 8 obsidian.
Blueprint 7: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 8 clay. Each geode robot costs 2 ore and 18 obsidian.
Blueprint 8: Each ore robot costs 4 ore. Each clay robot costs 3 ore. Each obsidian robot costs 4 ore and 15 clay. Each geode robot costs 4 ore and 9 obsidian.
Blueprint 9: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 20 clay. Each geode robot costs 2 ore and 12 obsidian.
Blueprint 10: Each ore robot costs 3 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 20 clay. Each geode robot costs 2 ore and 12 obsidian.
Blueprint 11: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 3 ore and 8 obsidian.
Blueprint 12: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 2 ore and 16 clay. Each geode robot costs 2 ore and 9 obsidian.
Blueprint 13: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 15 clay. Each geode robot costs 3 ore and 20 obsidian.
Blueprint 14: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 17 clay. Each geode robot costs 4 ore and 16 obsidian.
Blueprint 15: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 16 clay. Each geode robot costs 3 ore and 15 obsidian.
Blueprint 16: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 18 clay. Each geode robot costs 3 ore and 8 obsidian.
Blueprint 17: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 11 clay. Each geode robot costs 3 ore and 8 obsidian.
Blueprint 18: Each ore robot costs 3 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 9 clay. Each geode robot costs 2 ore and 10 obsidian.
Blueprint 19: Each ore robot costs 2 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 19 clay. Each geode robot costs 4 ore and 12 obsidian.
Blueprint 20: Each ore robot costs 2 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 4 ore and 9 obsidian.
Blueprint 21: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 2 ore and 7 clay. Each geode robot costs 3 ore and 10 obsidian.
Blueprint 22: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 10 clay. Each geode robot costs 2 ore and 14 obsidian.
Blueprint 23: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 2 ore and 15 clay. Each geode robot costs 2 ore and 13 obsidian.
Blueprint 24: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 7 clay. Each geode robot costs 4 ore and 17 obsidian.
Blueprint 25: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 20 clay. Each geode robot costs 2 ore and 10 obsidian.
Blueprint 26: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 8 clay. Each geode robot costs 3 ore and 19 obsidian.
Blueprint 27: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 20 clay. Each geode robot costs 3 ore and 14 obsidian.
Blueprint 28: Each ore robot costs 4 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 15 clay. Each geode robot costs 2 ore and 13 obsidian.
Blueprint 29: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 2 ore and 17 clay. Each geode robot costs 3 ore and 19 obsidian.
Blueprint 30: Each ore robot costs 2 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 13 clay. Each geode robot costs 3 ore and 11 obsidian.
""".strip().split('\n')
data = """
Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian.
""".strip().split('\n')
blueprints = collections.defaultdict(dict)
for i, row in enumerate(data, 1):
    m = re.match(r'.*ore robot.*(\d+)'
                 r'.*clay robot.*(\d+)'
                 r'.*obsidian robot.*(\d+) ore and (\d+)'
                 r'.*geode robot.*(\d+) ore and (\d+).*', row)
    if m:
        blueprints[i]['ore'] = {'ore': int(m.group(1))}
        blueprints[i]['clay'] = {'ore': int(m.group(2))}
        blueprints[i]['obsidian'] = {'ore': int(m.group(3)), 'clay': int(m.group(4))}
        blueprints[i]['geode'] = {'ore': int(m.group(5)), 'obsidian': int(m.group(6))}
        blueprints[i]['max_usage'] = {
            'ore': (blueprints[i]['ore']['ore'] + blueprints[i]['clay']['ore'] +
                    blueprints[i]['obsidian']['ore'] + blueprints[i]['geode']['ore']),
            'clay': blueprints[i]['obsidian']['clay'],
            'obsidian': blueprints[i]['geode']['obsidian'],
        }


def build(bp, robot, resources, robots):
    needed = bp[robot]
    for r, amount in needed.items():
        resources[r] -= amount
    robots[robot] += 1
    return resources, robots


def has_resources(bp, robot, resources):
    needed = bp[robot]
    for r, amount in needed.items():
        if not resources[r] >= amount:
            return False
    return True


def get_robots(bp, resources, robots):
    r = {}
    for robot in 'geode', 'obsidian', 'clay', 'ore':
        res = resources.copy()
        rbts = robots.copy()
        if has_resources(bp, robot, res):
            res, rbts = build(bp, robot, res, rbts)
            r[robot] = (res, rbts)
    return r


resources = {
    'ore': 0,
    'clay': 0,
    'obsidian': 0,
    'geode': 0,
}
robots = {
    'ore': 1,
    'clay': 0,
    'obsidian': 0,
    'geode': 0
}
# how many combinations of robots can we build?
bp = blueprints[2]
print(bp)
print(robots)
print(resources)


def add_resources(robots, resources):
    res = resources.copy()
    for robot, cnt in robots.items():
        res[robot] += cnt
    return res


def max_geode_output(bp, time_remaining, robots, resources):
    geodes = 0
    robots = robots.copy()
    resources = resources.copy()
    for t in range(time_remaining):
        geodes += robots['geode']
        if has_resources(bp, 'geode', resources):
            resources, robots = build(bp, 'geode', resources, robots)
    return geodes


def walk(bp, time_remaining, robots, resources, instructions):
    global max_geodes
    # print('walking with time remaining', time_remaining, s)
    # print(robots, resources)
    if not time_remaining:
        yield robots, resources, instructions
    elif (time_remaining < 3
          and resources['geode'] + max_geode_output(bp, time_remaining, robots, resources) < max_geodes):
        yield robots, resources, instructions
    else:
        can_build_robots = get_robots(bp, resources, robots)
        if 'geode' in can_build_robots:
            # print(' herp derp ')
            res, rbts = can_build_robots['geode']
            # print(res, rbts)
            res = add_resources(robots, res)
            inst = instructions[:]
            inst.append([tuple((k, v)) for k, v in res.items()])
            inst.append('geode robot')
            yield from walk(bp, time_remaining - 1, rbts, res, inst)
        elif 'ore' in can_build_robots and len(can_build_robots) == 1 and robots['ore'] < bp['max_usage']['ore']:
            res, rbts = can_build_robots['ore']
            res = add_resources(robots, res)
            inst = instructions[:]
            inst.append([tuple((k, v)) for k, v in res.items()])
            inst.append('ore robot')
            yield from walk(bp, time_remaining - 1, rbts, res, inst)
        else:
            resources = resources.copy()
            res = add_resources(robots, resources)
            inst = instructions[:]
            inst.append([tuple((k, v)) for k, v in res.items()])
            yield from walk(bp, time_remaining - 1, robots, res, inst)
            if can_build_robots:
                if 'ore' in can_build_robots:
                    del can_build_robots['ore']
                for robot, (res, rbts) in can_build_robots.items():
                    if robots[robot] >= bp['max_usage'][robot]:
                        continue
                    if (robot == 'obsidian'
                            and robots['obsidian'] * time_remaining + sum(range(time_remaining))
                            < bp['geode']['obsidian']):
                        continue
                    _res = res.copy()
                    _res = add_resources(robots, _res)
                    inst = instructions[:]
                    inst.append([tuple((k, v)) for k, v in _res.items()])
                    inst.append(robot + ' robot')
                    yield from walk(bp, time_remaining - 1, rbts, _res, inst)

max_geodes = 0
import time
t = time.time()
for r1, r2, instructions in walk(bp, 24, robots, resources, []):
    # print(r1, r2)

    if r2['geode'] > max_geodes:
        # max_geodes = r2['geode']
        minute = 1
        i = 0
        while i < len(instructions):
            res = instructions[i]
            if i + 1 < len(instructions) and isinstance(instructions[i + 1], str):
                command = instructions[i + 1]
                i += 1
            else:
                command = ''
            print('Minute %s: resources: %s, instruction: %s' % (minute, res, command if command else '---'))
            minute += 1
            i += 1
        print(r1, r2, time.time() - t)
        max_geodes = max(r2['geode'], max_geodes)
print(max_geodes)
print(time.time() - t)
# 7 geodes 124 sek
# 9 geodes ok 177 sek

