import orca
import networkx as nx
import itertools
import random

def gnm_random_graph(N, M):
    G = nx.Graph()
    G.add_nodes_from(range(N))

    possible_edges = itertools.combinations(G.nodes, 2)
    edges_to_add = random.sample(list(possible_edges), M)
    G.add_edges_from(edges_to_add)

    return G

#G = gnm_random_graph(4, 3)
G = nx.Graph()
with open('graph.in') as graph:
    for no,line in enumerate(graph):
        if no == 0:
            pass
        else:
            x = line.split()
            G.add_edge(x[0], x[1])

# G.add_edge("A", "B")
# G.add_edge("B", "D")
# G.add_edge("A", "C")
# G.add_edge("C", "D")
#nx.draw(G)
print (f'graph: {G}')
counts = orca.orbit_counts("node", 5, G)
print(f'Number of nodes: {len(counts)}')
print(f'Number of graphlets: {len(counts[0])}')
print('Counts: ', counts)

with open('graph.out', 'w') as f:
    for line in counts:
        f.write(f"{line}\n")
