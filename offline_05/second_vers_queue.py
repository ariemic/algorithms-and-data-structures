from zad5testy import runtests
from queue import PriorityQueue
            
            
def build_graph(E, singularities, s, n):
    #ładniejsze ale wolniejsze
    G = [[]for _ in range(n)]

    q = PriorityQueue()
    
    for i in range(len(E)):
        u, v, val = E[i]
        if singularities[u] and not singularities[v]:
            q.put((val, v)) 
            
        if not singularities[u] and singularities[v]:
            q.put((val, u))
            
        if not singularities[u] and not singularities[v]:
            G[u].append((v, val))
            G[v].append((u, val))
        
    visited = [False]*n        
    while not q.empty():
        val, u = q.get()
        if not visited[u]:
            G[u].append((s, val))
            G[s].append((u, val))
            visited[u] = True
        
    return G            


def relax(u, v, edge_weight, d, parent):
    if d[v] > d[u] + edge_weight:
        d[v] = d[u] + edge_weight
        parent[v] = u
        return True
    return False

def dijkstra(G, s):
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
    singularities = [False]*n
    for i in S:
        singularities[i] = True
        
    s = min(S)
    if singularities[a] and singularities[b]: return 0
    if singularities[a]: a = s
    if singularities[b]: b = s

    G = build_graph(E, singularities, s, n)
    # print(G)
    d = dijkstra(G, a)
    return d[b] if d[b] != float('inf') else None


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )






