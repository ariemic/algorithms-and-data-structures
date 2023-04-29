from zad5testy import runtests
from queue import PriorityQueue


def build_graph(E, S, n):
    #tworzy graf nieskierowany
    G = [[]for _ in range(n)]
    for tup in E:
        u, v, val = tup[0], tup[1], tup[2]
        G[u].append((v, val))
        G[v].append((u, val))
        
    for i in range(len(S)-1):
        u, v = S[i], S[i+1]
        G[u].append((v, 0))
        G[v].append((u, 0))
        
    return G

def relax(u, v, edge_weight, d, parent):
    if d[v] > d[u] + edge_weight:
        d[v] = d[u] + edge_weight
        parent[v] = u
        return True
    return False

def dijkstra(G, s):
    #for adjency representation graph
    n = len(G)
    d = [float('inf')]*n
    parent = [None]*n
    visited = [False]*n
    q = PriorityQueue()
    d[s] = 0
    q.put((d[s],s))
    while not q.empty():
        d_u, u = q.get()
        for v, edge_weight in G[u]:
            if not visited[v] and relax(u, v, edge_weight, d, parent):
                q.put((d[v], v))
        visited[u] = True #zapewnia nas nie będziemy cofać się do tyłu w grafie
    return d


def spacetravel( n, E, S, a, b ):
    G = build_graph(E, S, n)
    d = dijkstra(G, a)
    return d[b] if d[b] != float('inf') else None
    
E = [(0,1, 5),
(1,2,21),
(1,3, 1),
(2,4, 7),
(3,4,13),
(3,5,16),
(4,6, 4),
(5,6, 1)]
S = [ 0, 2, 3 ]
a = 1
b = 5
n = 7
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = False )






