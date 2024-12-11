import pprint
import re
import collections

data = """
Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II""".strip().split('\n')
data = """
Valve AW has flow rate=0; tunnels lead to valves DS, AA
Valve NT has flow rate=4; tunnels lead to valves AO, IT, AM, VZ
Valve FI has flow rate=0; tunnels lead to valves NK, RH
Valve NK has flow rate=13; tunnels lead to valves VZ, QE, FI
Valve ZB has flow rate=0; tunnels lead to valves IC, TX
Valve DS has flow rate=3; tunnels lead to valves ME, JY, OV, RA, AW
Valve JT has flow rate=0; tunnels lead to valves RA, OE
Valve OH has flow rate=0; tunnels lead to valves KT, AK
Valve OE has flow rate=9; tunnels lead to valves SH, MR, JT, QI
Valve CT has flow rate=0; tunnels lead to valves JH, NA
Valve CB has flow rate=0; tunnels lead to valves XC, JH
Valve EK has flow rate=0; tunnels lead to valves GB, ZZ
Valve NA has flow rate=0; tunnels lead to valves GL, CT
Valve JY has flow rate=0; tunnels lead to valves DS, IH
Valve RA has flow rate=0; tunnels lead to valves JT, DS
Valve QT has flow rate=0; tunnels lead to valves ZG, KM
Valve SM has flow rate=0; tunnels lead to valves AK, AM
Valve XC has flow rate=11; tunnel leads to valve CB
Valve BF has flow rate=10; tunnels lead to valves BU, MR
Valve OV has flow rate=0; tunnels lead to valves BV, DS
Valve GB has flow rate=25; tunnel leads to valve EK
Valve SD has flow rate=0; tunnels lead to valves JF, CN
Valve IH has flow rate=0; tunnels lead to valves JY, KM
Valve DF has flow rate=0; tunnels lead to valves ON, IC
Valve BV has flow rate=6; tunnels lead to valves OV, JN, ZG, UF
Valve PO has flow rate=0; tunnels lead to valves AK, QE
Valve JH has flow rate=12; tunnels lead to valves CB, MI, CT
Valve CN has flow rate=22; tunnel leads to valve SD
Valve JF has flow rate=0; tunnels lead to valves KM, SD
Valve QI has flow rate=0; tunnels lead to valves MI, OE
Valve JN has flow rate=0; tunnels lead to valves BV, BS
Valve TX has flow rate=0; tunnels lead to valves KM, ZB
Valve ME has flow rate=0; tunnels lead to valves VG, DS
Valve ON has flow rate=0; tunnels lead to valves DF, AA
Valve GL has flow rate=20; tunnel leads to valve NA
Valve AA has flow rate=0; tunnels lead to valves ON, UF, WR, ML, AW
Valve BS has flow rate=0; tunnels lead to valves JN, IC
Valve RH has flow rate=0; tunnels lead to valves FI, KT
Valve BU has flow rate=0; tunnels lead to valves BF, BG
Valve IT has flow rate=0; tunnels lead to valves NT, KT
Valve MR has flow rate=0; tunnels lead to valves OE, BF
Valve AO has flow rate=0; tunnels lead to valves ML, NT
Valve KM has flow rate=16; tunnels lead to valves WR, IH, QT, TX, JF
Valve ML has flow rate=0; tunnels lead to valves AO, AA
Valve VG has flow rate=0; tunnels lead to valves ME, IC
Valve MI has flow rate=0; tunnels lead to valves QI, JH
Valve AM has flow rate=0; tunnels lead to valves NT, SM
Valve KT has flow rate=23; tunnels lead to valves BG, OH, RH, SH, IT
Valve AK has flow rate=14; tunnels lead to valves SM, PO, OH
Valve BG has flow rate=0; tunnels lead to valves KT, BU
Valve QE has flow rate=0; tunnels lead to valves NK, PO
Valve IC has flow rate=17; tunnels lead to valves VG, ZZ, BS, ZB, DF
Valve UF has flow rate=0; tunnels lead to valves BV, AA
Valve SH has flow rate=0; tunnels lead to valves KT, OE
Valve WR has flow rate=0; tunnels lead to valves AA, KM
Valve ZZ has flow rate=0; tunnels lead to valves IC, EK
Valve ZG has flow rate=0; tunnels lead to valves BV, QT
Valve VZ has flow rate=0; tunnels lead to valves NK, NT
""".strip().split('\n')
_data = []
valves = {}
flow_rates = {}
for row in data:
    vs, cs = row.split(';')
    vs = vs.removeprefix('Valve').split()
    rate = vs[-1].split('=')[1]
    flow_rates[vs[0]] = int(rate)
    m = re.match(r'.*? to .*? ([A-Z, ]*)', cs)
    if m:
        valves[vs[0]] = {'connections': {c.strip() for c in m.group(1).split(',')},
                         'value': None,
                         'state': False}


def get_shortest_path(start, stop):
    distances = {valve: None for valve in valves}
    distances[start] = 0
    unvisited = {valve for valve in valves}
    while unvisited:
        node = next(iter(sorted([n for n, v in distances.items() if v is not None and n in unvisited],
                                key=lambda k: distances[k])))
        unvisited.remove(node)
        unvisited_neighbors = valves[node]['connections'] & unvisited
        for n in unvisited_neighbors:
            alt = distances[node] + 1
            if not distances[n] or alt < distances[n]:
                distances[n] = alt
        if node == stop:
            return distances[node]


relevant_valves = sorted([k for k, v in flow_rates.items() if v])
distances = collections.defaultdict(dict)
for n1 in valves:
    for n2 in [n for n in valves if n != n1]:
        d = get_shortest_path(n1, n2)
        distances[n1][n2] = d


def walk(node, valve_order, time_remaining, available_valves=None):
    if not available_valves:
        available_valves = relevant_valves
    for v in available_valves:
        if v not in valve_order and distances[node][v] <= time_remaining:
            yield from walk(v, valve_order + [v], time_remaining - distances[node][v] - 1,
                            available_valves=available_valves)
    if valve_order:
        yield valve_order[:]


def get_flow(order, time_remaining):
    node = 'AA'
    value = 0
    for v in order:
        time_remaining -= distances[node][v] + 1
        value += flow_rates[v] * time_remaining
        node = v
    return value


# part 1
# combinations = [get_flow(v, 26) for v in walk('AA', [], 26)]


import itertools
# min_len = len(relevant_valves) // 3
# max_len = 2 * len(relevant_valves) // 3
m = 0
for ln in range(7, 10):
    print('len:', ln)
    for a in itertools.permutations(relevant_valves, ln):
        rest = set(relevant_valves) - set(a)
        combinations1 = max([get_flow(v, 26) for v in walk('AA', [], 26, available_valves=a)])
        combinations2 = max([get_flow(v, 26) for v in walk('AA', [], 26, available_valves=rest)])
        # print(combinations1 + combinations2)
        m = max(m, combinations1 + combinations2)
        print(m)
    print(m)
print(m)

# mellan 2063 och 2350?!
