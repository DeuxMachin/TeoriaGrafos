def dijkstra(graph, start):
    distances = {vertex: float("infinity") for vertex in graph}
    distances[start] = 0
    vertices = set(graph.keys())

    while vertices:
        current_vertex = min(vertices, key=lambda vertex: distances[vertex])
        vertices.remove(current_vertex)

        for neighbor, weight in graph[current_vertex].items():
            new_distance = distances[current_vertex] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance

    return distances


graph = {
    "A": {"B": 1, "C": 4},
    "B": {"A": 1, "C": 2, "D": 5},
    "C": {"A": 4, "B": 2, "D": 1},
    "D": {"B": 5, "C": 1},
}
start_vertex = "A"
shortest_paths = dijkstra(graph, start_vertex)
print(shortest_paths)
