import networkx as nx
import matplotlib.pyplot as plt

graph = {
    0: {1: 10, 2: 15, 3: 20},
    1: {0: 10, 2: 35, 3: 25},
    2: {0: 15, 1: 35, 3: 30},
    3: {0: 20, 1: 25, 2: 30}
}

parcels = [
    {"id": 1, "value": 60, "weight": 10},
    {"id": 2, "value": 100, "weight": 20},
    {"id": 3, "value": 120, "weight": 30},
]

capacity = 50


def greedy_selection(parcels, capacity):
    parcels = sorted(parcels, key=lambda x: x["value"] / x["weight"], reverse=True)

    selected = []
    total_value = 0

    for p in parcels:
        if capacity >= p["weight"]:
            selected.append(p)
            capacity -= p["weight"]
            total_value += p["value"]

    return selected, total_value


selected, value = greedy_selection(parcels, capacity)

print("Selected Parcels:", selected)
print("Total Value:", value)


# GRAPH VISUALIZATION
G = nx.Graph()

for u in graph:
    for v in graph[u]:
        G.add_edge(u, v, weight=graph[u][v])

pos = nx.spring_layout(G)

nx.draw(G, pos, with_labels=True, node_color='lightgreen', node_size=2000)

labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.title("Task 4: Greedy Selection Graph")
plt.show()