import networkx as nx
import matplotlib.pyplot as plt


def create_graph():
    graph = nx.Graph()

    graph.add_nodes_from(
        ["Kyiv", "Lviv", "Odesa", "Dnipro", "Donetsk", "Zaporizhia", "Kharkiv", "Chernihiv", "Ivano-Frankivsk"])

    edges_with_distances = [
        ("Kyiv", "Lviv", 540),
        ("Kyiv", "Odesa", 475),
        ("Kyiv", "Dnipro", 477),
        ("Kyiv", "Ivano-Frankivsk", 603),
        ("Lviv", "Odesa", 826),
        ("Lviv", "Ivano-Frankivsk", 134),
        ("Dnipro", "Donetsk", 217),
        ("Donetsk", "Zaporizhia", 247),
        ("Zaporizhia", "Kharkiv", 330),
        ("Kharkiv", "Chernihiv", 300),
        ("Chernihiv", "Kyiv", 150)
    ]

    graph.add_weighted_edges_from(edges_with_distances)

    return graph


def describe_graph(graph):
    print(f"Кількість вершин графа: {len(graph.nodes())}")
    print(f"Кількість ребер графа: {graph.edges()}")
    print(f"Ваги ребер графа: {nx.get_edge_attributes(graph, 'weight')}")

    degree_sequence = dict(graph.degree())
    print(f"Ступені вершин графа:")
    for node, degree in degree_sequence.items():
        print(f"{node}: {degree}")


def visualize_graph(graph):
    weights = nx.get_edge_attributes(graph, "weight")
    max_weight = max(weights.values())
    widths = [w/max_weight * 10 for w in weights.values()]

    pos = nx.circular_layout(graph)
    nx.draw(
        graph,
        pos,
        with_labels=True,
        font_weight="bold",
        node_size=700,
        node_color="skyblue",
        font_color="black",
        font_size=8,
        edge_color="gray",
        width=widths,
    )
    edge_labels = nx.get_edge_attributes(graph, "weight")
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)

    plt.show()


def bfs_recursive(graph, start, visited=None, queue=None):
    if visited is None:
        visited = []
    if queue is None:
        queue = [start]

    if not queue:
        return visited

    current_node = queue.pop(0)
    if current_node not in visited:
        visited.append(current_node)
        queue.extend(
            neighbor
            for neighbor in graph.neighbors(current_node)
            if neighbor not in visited
        )

    return bfs_recursive(graph, start, visited, queue)


def dfs_recursive(graph, vertex, visited=None):
    if visited is None:
        visited = []
    visited.append(vertex)
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

    return visited


def dijkstra(graph, start):
    distances = {node: float("inf") for node in graph.nodes()}
    distances[start] = 0

    visited = {node: False for node in graph.nodes()}

    while False in visited.values():
        current_node = min(
            [node for node in graph.nodes() if visited[node] is False],
            key=lambda node: distances[node],
        )
        visited[current_node] = True

        for neighbour, weight in graph[current_node].items():
            if distances[current_node] + weight["weight"] < distances[neighbour]:
                distances[neighbour] = distances[current_node] + weight["weight"]

    return distances


if __name__ == "__main__":
    print("------------------# Завдання 1------------------")
    G = create_graph()
    describe_graph(G)

    print("------------------# Завдання 2------------------")
    print("DFS-обхід:")
    print(" ".join(dfs_recursive(G, "Ivano-Frankivsk")))

    print("BFS-обхід:")
    print(" ".join(bfs_recursive(G, "Ivano-Frankivsk")))

    print("------------------# Завдання 3------------------")
    print("Найкоротші відстані від вершини Ivano-Frankivsk:")
    print(dijkstra(G, "Ivano-Frankivsk"))

    visualize_graph(G)
