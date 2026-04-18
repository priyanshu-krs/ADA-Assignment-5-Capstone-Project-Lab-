import networkx as nx
import matplotlib.pyplot as plt

graph = {
    'A': {'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30}
}

G = nx.Graph()

for u in graph:
    for v in graph[u]:
        if not G.has_edge(u, v):
            G.add_edge(u, v, weight=graph[u][v])

pos = nx.spring_layout(G, seed=42)

nx.draw(G, pos, with_labels=True, node_color='orange', node_size=2000)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.title("Task 2: Input Graph")
plt.show()