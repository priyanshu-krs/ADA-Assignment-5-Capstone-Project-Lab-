import itertools
import networkx as nx
import matplotlib.pyplot as plt

graph = {
    0: {1: 10, 2: 15, 3: 20},
    1: {0: 10, 2: 35, 3: 25},
    2: {0: 15, 1: 35, 3: 30},
    3: {0: 20, 1: 25, 2: 30}
}

G = nx.Graph()

for u in graph:
    for v in graph[u]:
        G.add_edge(u, v, weight=graph[u][v])

pos = nx.spring_layout(G)

# ---------------- TSP ----------------
def tsp_bruteforce():
    nodes = list(graph.keys())
    min_cost = float('inf')
    best_path = None

    for perm in itertools.permutations(nodes[1:]):
        cost = graph[0][perm[0]]

        for i in range(len(perm) - 1):
            cost += graph[perm[i]][perm[i + 1]]

        cost += graph[perm[-1]][0]

        if cost < min_cost:
            min_cost = cost
            best_path = (0,) + perm + (0,)

    return best_path, min_cost


path, cost = tsp_bruteforce()

print("Optimal Route:", path)
print("Total Distance:", cost)

# ---------------- GRAPH ----------------

# Normal graph
plt.figure()
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000)
nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))
plt.title("Task 6: Graph")
plt.show()

# Highlight optimal route
edges = [(path[i], path[i+1]) for i in range(len(path)-1)]

plt.figure()
nx.draw(G, pos, with_labels=True, node_color='lightgreen', node_size=2000)
nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='red', width=3)
nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))
plt.title("Task 6: Optimal Route (TSP)")
plt.show()