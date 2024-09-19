'''
Sprawdz czy graf jest spójny przy pomocy DFS'a dla postaci listy sąsiedztwa i macierzowej

1. Puszczam raz dfs'a od wierzchołka zerowego, jeśli po tym jednym razie wejde w if'a to znaczy że istnieje nie odwiedzony wierzchołek zatem graf jest niespójny
'''

def DFS(G):
    #adjancency list
    n = len(G)
    visited = [False]*n
    
    def dfs_visit(G, u):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:

                dfs_visit(G, v)
    
    dfs_visit(G, 0)
    for u in range(1, n): 
        if not visited[u]:
            return False
    return True


def DFS(G):
    #adjancency matrix - działa dla grafu nieskierowanego -> jak napisać dla skierowanego?
    n = len(G)
    visited = [False]*n
    
    def dfs_visit(G, i, n):
        visited[i] = True
        for j in range(n):
            if not visited[j] and G[i][j] == 1:
                dfs_visit(G, j, n)
                
    dfs_visit(G, 0, n)
    print(visited)
    for i in range(1, n):
        if not visited[i]:
            return False
    return True

G = [[0, 0, 1, 1], 
    [1, 0, 0, 0], 
    [0, 1, 0, 0], 
    [1, 0, 0, 0]]

print(DFS(G))
    