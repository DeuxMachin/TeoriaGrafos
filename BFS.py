def bfs(graph, nodoinicial):
    
    visitado = []#Almacenaremos los nodos visitados
    cola = [nodoinicial]#Cola para los nodos pendientes de visitados
    while cola:
        nodos = cola.pop(0)#Borramos el primer nodo de la cola
        if nodos not in visitado: 
            visitado.append(nodos)#Lo marcaremos como visitado
            for neighbor e in graph[nodos]: #Visitara todos los nodos accesibles del nodo inciaal
                if neighbor  not in visitado:
                    cola.append(neighbor )
    return visitado


graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"], "D": [], "E": ["F"], "F": []}


print(bfs(graph, "A"))
