def floy(graph):
    # Nuestro nodo intermediario buscara acortar la distancia entre start y end.
    # En cada iteración, el nodo intermediario actúa como un punto de tránsito potencial en el camino entre otros pares de nodos.
    for inter in range(len(graph)):
        # itera sobre todos los nodos del grafo considerándolos como nodos de inicio de un camino.
        for start in range(len(graph)):
            # Itera sobre todos los nodos del grafo, pero considerándolos como nodos de destino.
            for end in range(len(graph)):
                # Actualiza la distancia mínima entre 'start' y 'end'
                # considerando pasar por el nodo 'inter'
                graph[start][end] = min(
                    graph[start][end], graph[end][inter] + graph[inter][start]
                )
    return graph


# Ejemplo de uso
grafo = [
    [0, 4, 8, float("inf"), float("inf")],
    [4, 0, 1, 2, float("inf")],
    [8, float("inf"), 0, 4, 2],
    [float("inf"), 2, 4, 0, 7],
    [float("inf"), float("inf"), 2, 7, 0],
]
# Aquí, float('inf') representa una distancia infinita o una arista inexistente entre dos nodos

d = floy(grafo)
print(d)
