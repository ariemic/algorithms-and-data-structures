'''
Zadanie 4. (malejace krawedzie) Dany jest graf G = (V,E), gdzie kazda krawedz ma wage ze zbioru
{1, . . . , SES} (wagi krawedzi sa parami rózne). Prosze zaproponowac algorytm, który dla danych wierzchołków
x i y sprawdza, czy istnieje sciezka z x do y, w której przechodzimy po krawedziach o coraz mniejszych wagach.

Nie powienienem tu oznaczać visited bo kilka razy mogę wejść do tego samego wierzchołka, nie zależy mi na najkrótszej ścieżce tylko nad taką która spełnia warunki zadania jeśli istnieje.
'''

from collections import deque

G = [[(1,2), (2,4)], [(0,2), (3, 5), (2, 6)], [(0, 4), (3, 3), (1, 6)], [(2,3), (1,5), (4, 1)], [(3, 1)]]
G1 = [[(1,2), (2,4), (4, 7)], [(0,2), (3, 5), (2, 6)], [(0, 4), (3, 3), (1, 6)], [(2,3), (1,5), (4, 1)], [(3, 1), (0, 7)]]

G_test = [[(1, 2), (2, 1)], [(0, 2), (2, 5)], [(0, 1), (1, 5)]]


def DFS(G, value, source, destination):
    for (neighbour, weight) in G[source]:
        
        if neighbour == destination and value > weight:
            return True 

        elif value > weight:
            if DFS(G, weight, neighbour, destination):
                return True

    return False 
print( DFS(G_test, float('inf'), 0, 4) )


def DFS_decreasing_edges(G, x, y):
    n = len(G)
    parent = [None]*n
    path = []
    def dfs_visit(G, x, y):
        u, u_w = x[0], x[1]    
        if u == y:
            return True
        
        for v, v_w in G[u]:
            if v_w < u_w: 
                if dfs_visit(G, (v, v_w), y): 
                    parent[v] = u
                    return True
        return False
              
    if dfs_visit(G, (x, float('inf')), y):
        path = [y]
        while y != x:
            y = parent[y]
            path.append(y)
    return path[::-1] if len(path) > 0 else None 
    


def BFS_decreasing_edges(G, x, y):
    n = len(G)
    visited = [False]*n
    visited[x] = True
    parent = [None]*n
    q = deque()
    q.append((x, float('inf')))
    while q:
        u, u_w = q.popleft()
        for v, v_w in G[u]:
            if not visited[v] and v_w < u_w:
                q.append((v, v_w))
                visited[v] = True
                parent[v] = u
        if u == y:
            return True
    return False
        
print(BFS_decreasing_edges(G_test, 0, 4))


print(DFS_decreasing_edges(G_test, 0, 4))
    