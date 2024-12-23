import networkx as nx

data = """
kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn
""".strip().splitlines()
data = open('data/23.dat').read().strip().splitlines()
g = nx.Graph(pair.split('-') for pair in data)
print('part 1:', sum(1 for nodes in nx.simple_cycles(g, 3) if any(1 for node in nodes if node.startswith('t'))))
print('part 2:', ','.join(sorted(list(c for c in nx.enumerate_all_cliques(g))[-1])))