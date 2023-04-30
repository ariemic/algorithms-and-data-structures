'''
Zadanie 5. (krawedzie 0/1) Dana jest mapa kraju w postaci grafu G = (V,E). Kierowca chce przejechac
z miasta (wierzchołka) s to miasta t. Niestety niektóre drogi (krawedzie) sa płatne. Kazda droga ma taka
1
sama jednostkowa opłate. Prosze podac algorytm, który znajduje trase wymagajaca jak najmniejszej liczby
opłat. W ogólnosci graf G jest skierowany, ale mozna najpierw wskazac algorytm dla grafu nieskierowanego

Włączam Dijkstre i szukam trasy o najniższym koszcie od s do t, skoro każda krawedz ma wage 0 lub 1 czyli w ogólnoście nieujemną
'''

from queue import PriorityQueue

def create_graph(Edges, n):
    G = [[]for _ in range(n)]
    for edge in Edges:
        u, v, val = edge[0], edge[1], edge[2]
        G[u].append((v, val))
    return G


def dijkstra(Edges, n, s, t):
    G = create_graph(Edges, n)
    visited = [False]*n
    parent = [None]*n
    d = [float('inf')]*n
    d[s] = 0
    q = PriorityQueue(s)
    q.put((0,s))
    while not q.empty():
        w_u, u = q.get()
        for v, w_v in G[u]:        
            if not visited[v]:
                #relax
                if d[v] > d[u] + w_v:
                    d[v] = d[u] + w_v
                    parent[v] = u
                    q.put((w_v, v))
                    
        visited[u] = True
        charge = d[t]
        if u == t:
            
            path = [t]
            while t != None:
                t = parent[t]
                path.append(t)
            print(path[::-1])
            return charge
    return None


Edges = [(0, 1, 1), (0, 3, 1), (0, 2, 0), (2, 3, 0), (3, 4, 1)]
n = 5

print(dijkstra(Edges, n, 0, 4))