def dfs(graph, node, visited=None):
    # Esto significa que si usáramos una lista mutable como valor predeterminado (por ejemplo, visited=[]),
    # esta misma lista se compartiría entre todas las llamadas a la función,
    # lo cual puede llevar a resultados inesperados y bugs
    # Para evitar este comportamiento, se utiliza None. Asegurara que cada fez que se llame dfs sin algun dato,
    # cree una nueva lista. De manera recursiva
    if visited == None:
        visited = []

    visited.append(node)  # Marcar el nodo actual como visitado

    # Iterar sobre cada vecino del nodo actual
    for neighbor in graph[node]:
        # Si el vecino no ha sido visitado
        if neighbor not in visited:
            # Llamada recursiva a dfs para el vecino
            dfs(graph, neighbor, visited)
    return visited


graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"], "D": [], "E": ["F"], "F": []}


print(dfs(graph, "A"))
