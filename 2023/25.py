import networkx as nx

data = """
jqt: rhn xhk nvd
rsh: frs pzl lsr
xhk: hfx
cmg: qnr nvd lhk bvb
rhn: xhk bvb hfx
bvb: xhk hfx
pzl: lsr hfx nvd
qnr: nvd
ntq: jqt hfx bvb xhk
nvd: lhk
lsr: lhk
rzs: qnr cmg lsr rsh
frs: qnr lhk lsr
"""
data = open('input/25.dat').read()
graph = nx.Graph()
for row in data.strip().splitlines():
    a, bs = row.split(':')
    for b in bs.strip().split():
        graph.add_edge(a, b)

# https://en.wikipedia.org/wiki/Graph_partition#Spectral_partitioning_and_spectral_bisection
g1, g2 = nx.spectral_bisection(graph)
print('part 1:', len(g1) * len(g2))
