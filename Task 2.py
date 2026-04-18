import networkx as nx
import matplotlib.pyplot as plt

# Graph data
graph = {
    'A': {'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30}
}

# Recursive cost function
def route_cost(path):
    if len(path) == 1:
        return 0
    return graph[path[0]][path[1]] + route_cost(path[1:])

# Example route
route = ['A', 'B', 'D', 'C', 'A']
cost = route_cost(route)

print("Route:", route)
print("Total Cost:", cost)

# ---------------- GRAPH PART ----------------
G = nx.Graph()

# Add edges
for u in graph:
    for v in graph[u]:
        if not G.has_edge(u, v):
            G.add_edge(u, v, weight=graph[u][v])

pos = nx.spring_layout(G, seed=42)

plt.figure(figsize=(6,6))

# Draw full graph
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000)

# Draw edge labels
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

# Highlight route edges in RED
route_edges = list(zip(route, route[1:]))
nx.draw_networkx_edges(G, pos, edgelist=route_edges, width=3)

plt.title("Task 3: Recursive Route Cost Graph")
plt.show()