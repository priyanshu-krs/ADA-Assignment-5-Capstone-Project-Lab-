import time
import networkx as nx
import matplotlib.pyplot as plt
import itertools

graph = {
    0: {1: 10, 2: 15, 3: 20},
    1: {0: 10, 2: 35, 3: 25},
    2: {0: 15, 1: 35, 3: 30},
    3: {0: 20, 1: 25, 2: 30}
}

# ---------------- TSP FUNCTION ----------------
def tsp_bruteforce():
    nodes = list(graph.keys())
    min_cost = float('inf')

    for perm in itertools.permutations(nodes[1:]):
        cost = graph[0][perm[0]]

        for i in range(len(perm)-1):
            cost += graph[perm[i]][perm[i+1]]

        cost += graph[perm[-1]][0]

        min_cost = min(min_cost, cost)

    return min_cost


# ---------------- TIME PROFILING ----------------
sizes = [2, 3, 4]
times = []

for n in sizes:
    start = time.time()
    tsp_bruteforce()
    end = time.time()
    times.append(end - start)

print("Execution Times:", times)


# ---------------- PERFORMANCE PLOT ----------------
plt.figure()
plt.plot(sizes, times, marker='o')
plt.xlabel("Number of Nodes")
plt.ylabel("Time (seconds)")
plt.title("Task 7: TSP Performance")
plt.show()


# ---------------- GRAPH VISUALIZATION ----------------
G = nx.Graph()

for u in graph:
    for v in graph[u]:
        G.add_edge(u, v, weight=graph[u][v])

pos = nx.spring_layout(G)

nx.draw(G, pos, with_labels=True)
nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))

plt.title("Task 7: Network Graph")
plt.show()