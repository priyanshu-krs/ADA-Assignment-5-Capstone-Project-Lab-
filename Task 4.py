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

# ---------------- DIJKSTRA ----------------
distances = nx.single_source_dijkstra_path_length(G, 0)
print("Dijkstra Distances:", distances)

# Show graph for Dijkstra
plt.figure()
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000)
nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))
plt.title("Task 5: Dijkstra Graph")
plt.show()

# ---------------- MST ----------------
mst = nx.minimum_spanning_tree(G)

total_weight = sum(d['weight'] for u, v, d in mst.edges(data=True))
print("MST Total Weight:", total_weight)

# Show MST graph
plt.figure()
nx.draw(mst, pos, with_labels=True, node_color='lightgreen', node_size=2000)
nx.draw_networkx_edge_labels(mst, pos, edge_labels=nx.get_edge_attributes(mst, 'weight'))
plt.title("Task 5: Minimum Spanning Tree")
plt.show()