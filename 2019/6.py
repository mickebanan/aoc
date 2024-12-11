import networkx as nx

data = """
COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN
""".strip().split('\n')
data = open('data/6.dat').read().strip().split('\n')
graph = nx.Graph()
for row in data:
    a, b = row.split(')')
    graph.add_edge(a, b)
print('part 1:', sum(v for k, v in nx.shortest_path_length(graph, source='COM').items()))
print('part 2:', nx.shortest_path_length(graph, source='YOU', target='SAN') - 2)