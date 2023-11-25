class TeoriaGrafos:
    def __init__(self):
        self.Opciones = 2
        self.CantidadNodos = 0
        self.Bidireccional = True
        self.Conexiones = []
        self.algoritmos = {
            "dfs": self.dfs,
            "bfs": self.bfs,
            "kruskal": self.kruskal,
            "prim": self.prim,
            "dijkstra": self.dijkstra,
            "floyd-warshall": self.floyd_warshall,
        }

    # ----------------------------------------------------------------

    def Menu(self):
        print(
            "Bienvenido. Tiene dos opciones: ",
            "\n",
            "1)Ingresar datos",
            "\n",
            "2)Seleccionar algoritmo de grafo.",
        )

        if self.Opciones == 1:
            pass
        elif self.Opciones == 2:
            self.seleccionarAlgoritmo()
        else:
            print("Opción no válida")

    # ----------------------------------------------------------------

    def seleccionarAlgoritmo(self):
        print("Seleccione un algoritmo de la lista: ")
        for algoritmo in self.algoritmos:
            print(
                algoritmo.upper()
            )  # Mostrar las opciones en mayúsculas para el usuario
        eleccion = input(
            "Escriba el nombre del algoritmo: "
        ).lower()  # Convertir a minúsculas
        if eleccion in self.algoritmos:
            self.algoritmos[eleccion]()
        else:
            print("Algoritmo no válido")

    # ----------------------------------------------------------------

    def dfs(graph, node, visited=None):
        if visited == None:
            visited = []

        visited.append(node)

        for i in graph[node]:
            if i not in visited:
                grafos.dfs(graph, i, visited)
        return visited

    # ----------------------------------------------------------------

    def bfs(graph, nodoInicial):
        visitados = []
        cola = [nodoInicial]
        while cola:
            vecinos = cola.pop(0)
            if vecinos not in visitados:
                visitados.append(vecinos)
                for i in graph[vecinos]:
                    if i not in visitados:
                        cola.append(i)
        return visitados

    # ----------------------------------------------------------------
    def weight(edge):
        return edge[2]

    def kruskal(graph):
        edges = sorted(graph, key=grafos.weight)
        mst = []
        connected = set()
        for edge in edges:
            start, end, _ = edge
            if start not in connected or end not in connected:
                mst.append(edge)
                connected.update([start, end])
        return mst

    # ----------------------------------------------------------------

    def prim(self):
        print("Ejecutando Prim...")
        # Aquí va la lógica para Prim

    # ----------------------------------------------------------------

    def dijkstra(self):
        print("Ejecutando Dijkstra...")
        # Aquí va la lógica para Dijkstra

    # ----------------------------------------------------------------

    def floy(graph):
        for inter in range(len(graph)):
            for start in range(len(graph)):
                for end in range(len(graph)):
                    graph[start][end] = min(
                        graph[start][end], graph[end][inter] + graph[inter][start]
                    )
        return graph

    # ----------------------------------------------------------------

    def MakeGraph(self):
        if self.Bidireccional:
            print("El grafo es bidireccional")
        else:
            print("El grafo no es bidireccional")

    # ----------------------------------------------------------------


# Crear una instancia de la clase y llamamos al método Menu
grafos = TeoriaGrafos()
grafos.Menu()
