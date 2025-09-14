from collections import deque
import heapq

GRAPH = {
    "Pelotas": {"Camaquã": 150, "Rio Grande": 55, "Bagé": 180, "Santa Maria": 370},
    "Camaquã": {"Pelotas": 150, "Guaíba": 65, "Porto Alegre": 125},
    "Guaíba": {"Camaquã": 65, "Porto Alegre": 30},
    "Porto Alegre": {"Guaíba": 30, "Camaquã": 125, "Rio Grande": 320, "Bagé": 380, "Santa Maria": 290},
    "Rio Grande": {"Pelotas": 55, "Porto Alegre": 320},
    "Bagé": {"Pelotas": 180, "Porto Alegre": 380},
    "Santa Maria": {"Pelotas": 370, "Porto Alegre": 290},
}

def bfs(grafo, inicio, objetivo):
    fila = deque([(inicio, [inicio])])
    visitados = set()
    passos = 0

    while fila:
        atual, caminho = fila.popleft()
        passos += 1
        print(f"[BFS] Visitando: {atual} | Caminho até agora: {caminho}")

        if atual == objetivo:
            return caminho, passos

        if atual not in visitados:
            visitados.add(atual)
            for vizinho in grafo[atual]:
                if vizinho not in visitados:
                    fila.append((vizinho, caminho + [vizinho]))

    return None, passos



def dfs(grafo, inicio, objetivo):
    pilha = [(inicio, [inicio])]
    visitados = set()
    passos = 0

    while pilha:
        atual, caminho = pilha.pop()
        passos += 1
        print(f"[DFS] Visitando: {atual} | Caminho até agora: {caminho}")

        if atual == objetivo:
            return caminho, passos

        if atual not in visitados:
            visitados.add(atual)
            for vizinho in grafo[atual]:
                if vizinho not in visitados:
                    pilha.append((vizinho, caminho + [vizinho]))

    return None, passos

def dijkstra(grafo, inicio, objetivo):
    fila = [(0, inicio, [inicio])]  # (custo, nó atual, caminho)
    visitados = set()

    while fila:
        custo, atual, caminho = heapq.heappop(fila)
        print(f"[Dijkstra] Visitando: {atual} | Custo até agora: {custo} km | Caminho: {caminho}")

        if atual == objetivo:
            return caminho, custo

        if atual not in visitados:
            visitados.add(atual)
            for vizinho, peso in grafo[atual].items():
                if vizinho not in visitados:
                    heapq.heappush(fila, (custo + peso, vizinho, caminho + [vizinho]))
    return None, float("inf")


inicio = "Pelotas"
objetivo = "Porto Alegre"

print("\n==== BFS =====")
caminho_bfs, passos_bfs = bfs(GRAPH, inicio, objetivo)
print("Caminho final (BFS):", " -> ".join(caminho_bfs))
print("Passos BFS:", passos_bfs)

print("\n==== DFS =====")
caminho_dfs, passos_dfs = dfs(GRAPH, inicio, objetivo)
print("Caminho final (DFS):", " -> ".join(caminho_dfs))
print("Passos DFS:", passos_dfs)


print("\n==== Dijkstra =====")
caminho_dij, custo_dij = dijkstra(GRAPH, inicio, objetivo)
print("Caminho final (Dijkstra):", " -> ".join(caminho_dij))
print("Custo total:", custo_dij, "km")

print("\n===== Comparação Final =====")
print(f"BFS -> Caminho: {' -> '.join(caminho_bfs)}, Passos: {passos_bfs}")
print(f"DFS -> Caminho: {' -> '.join(caminho_dfs)}, Passos: {passos_dfs}")
print(f"Dijkstra -> Caminho: {' -> '.join(caminho_dij)}, Custo: {custo_dij} km")
