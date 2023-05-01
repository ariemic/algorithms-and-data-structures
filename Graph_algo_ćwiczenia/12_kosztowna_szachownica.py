'''
Zadanie 7. (kosztowna szachownica) Dana jest szachownica o wymiarach n x n. Kazde pole (i, j)
ma koszt (liczbe ze zbioru {1, . . . , 5}) umieszczony w tablicy A (na polu A[j][i]). W lewym górnym rogu
szachownicy stoi król, którego zadaniem jest przejsc do prawego dolnego rogu, przechodzac po polach o
minmalnym sumarycznym koszcie. Prosze zaimplementowac funkcje kings path(A), która oblicza koszt
sciezki króla. Funkcja powinna byc mozliwie jak najszybsza

Robie implementacje dijkstry dla macierzy sąsiedztwa
'''

from queue import PriorityQueue


def relax(u, v, edge_weight, parent, d):
    if d[v] > d[u]+edge_weight:
        d[v] = d[u] + edge_weight
        parent[v] = u
        return True
    return False

def kingsPath(G, s, t):
    n = len(G)
    q = PriorityQueue()
    d = [float('inf')]*n
    visited = [False]*n
    parent = [None]*n
    d[s[0]] = 0
    q.put((0, s[0]))
    
    while not q.empty():
        du, u = q.get()
        for v in range(n):
            if not visited[v] and G[u][v] != -1 and relax(u, v, G[u][v], parent, d):
                q.put((d[v], v))
        visited[u] = True 
        if t == (u,v):
            return d[u]

