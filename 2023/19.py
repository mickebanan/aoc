import collections
import math
import operator
import re
from functools import reduce

data = """px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}
"""
data = open('input/19.dat').read().strip()
instructions = collections.defaultdict(list)
parts = []
read_parts = False
ops = {'<': operator.lt, '>': operator.gt}


def get_part_values(part):
    values = {}
    for value in part:
        a, val = value.split('=')
        values[a] = int(val)
    return values


for row in data.split('\n'):
    if not row:
        read_parts = True
        continue
    if read_parts:
        parts.append(get_part_values(row.strip('{}').split(',')))
    else:
        i, rules = row.split('{')
        instructions[i] = rules.rstrip('}').split(',')


def parse_rule(rule):
    if ':' in rule:
        instr = op = value = None
        cond, target = rule.split(':')
        if '<' in cond:
            instr, value = cond.split('<')
            op = '<'
        elif '>' in cond:
            instr, value = cond.split('>')
            op = '>'
        return instr, op, int(value), target
    else:
        return rule


def parse(part, rule):
    if rule == 'A':
        return sum(part.values())
    elif rule == 'R':
        return 0
    for rr in instructions[rule]:
        instr = parse_rule(rr)
        if isinstance(instr, tuple):
            k, op, value, target = instr
            if reduce(ops[op], (part[k], value)):
                return parse(part, target)
        else:
            return parse(part, instr)


p1 = 0
for part in parts:
    p1 += parse(part, 'in')
print('part 1:', p1)


p2 = 0
d = {'x': range(1, 4001), 'm': range(1, 4001), 'a': range(1, 4001), 's': range(1, 4001)}
work = [('in', d)]
while work:
    rule, values = work.pop(0)
    if rule == 'A':
        p2 += math.prod(len(r) for r in values.values())
    else:
        for rr in instructions[rule]:
            instr = parse_rule(rr)
            if isinstance(instr, tuple):
                k, op, value, target = instr
                val = values[k]
                if op == '<':
                    start, mid, stop = (val.start, value, val.stop)
                    values[k] = range(start, mid)
                    work.append((target, values.copy()))
                    values[k] = range(mid, stop)
                else:
                    start, mid, stop = (val.start, value + 1, val.stop)
                    values[k] = range(mid, stop)
                    work.append((target, values.copy()))
                    values[k] = range(start, mid)
            elif instr != 'R':
                work.append((instr, values))
print('part 2:', p2)
