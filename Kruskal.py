def weight(edge):
    return edge[2]


def kruskal(graph):
    edges = sorted(graph, key=weight)
    mst = []
    connected = set()
    for edge in edges:
        start, end, _ = edge
        if start not in connected or end not in connected:
            mst.append(edge)
            connected.update([start, end])
    return mst


# Ejemplo de uso
graph = [
    ("A", "B", 4),
    ("B", "C", 1),
    ("C", "D", 3),
    ("A", "D", 2),
    ("D", "E", 6),
    ("B", "E", 5),
]


mst = kruskal(graph)
print("MST:", mst)
