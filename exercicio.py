from collections import deque

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
