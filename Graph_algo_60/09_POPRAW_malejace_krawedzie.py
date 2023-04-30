'''
Zadanie 4. (malejace krawedzie) Dany jest graf G = (V,E), gdzie kazda krawedz ma wage ze zbioru
{1, . . . , SES} (wagi krawedzi sa parami rózne). Prosze zaproponowac algorytm, który dla danych wierzchołków
x i y sprawdza, czy istnieje sciezka z x do y, w której przechodzimy po krawedziach o coraz mniejszych wagach.

Nie powienienem tu oznaczać visited bo kilka razy mogę wejść do tego samego wierzchołka, nie zależy mi na najkrótszej ścieżce tylko nad taką która spełnia warunki zadania jeśli istnieje.
'''
from collections import deque

G = [[(1,2), (2,4)], [(0,2), (3, 5), (2, 6)], [(0, 4), (3, 3), (1, 6)], [(2,3), (1,5), (4, 1)], [(3, 1)]]
G1 = [[(1,2), (2,4), (4, 7)], [(0,2), (3, 5), (2, 6)], [(0, 4), (3, 3), (1, 6)], [(2,3), (1,5), (4, 1)], [(3, 1), (0, 7)]]


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
            path = []
            while u != x: 
                if parent[u] != None:
                    path.append(u)
                    u = parent[u]
                else:
                    return None
            path.append(x)
            #edge case jedna krawedz prowadząca z x do y nie spełania warunków zadania - algorytm się na tym wywala
            return path[::-1]
                
print(BFS_decreasing_edges(G, 0, 4))


def DFS_decreasing_edges(G, x, y):
    n = len(G)
    visited = [False]*n
    path = []
    
    def dfs_visit(G, u):    
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
              
                dfs_visit(G, v)

    for u in range(n):
        if not visited[u]:
            dfs_visit(G, u)
            
            

            
    