'''
Najkrótsze ścieżki w DAG -> sorotwanie topologiczne
O(V+E)
Alternatywa: Uruchomienie jednej iteracji Bellmana-Forda
'''

def sort_topologiczne(G, s=0):
    time = 0
    n = len(G)
    visited = [False]*n 
    res = []
    
    def dfsVisit(G, u):
        nonlocal time
        time += 1
        visited[u] = True 
        for v in G[u]:
            if not visited[v]:
                dfsVisit(G, v)
        time += 1
        res.append(u)
        
    for u in range(n):
        if not visited[u]:
            dfsVisit(G, u)
        
    return res[::-1]

def shortestsPathsDAG(G, s):
    n = len(G)
    topo_sorted = sort_topologiczne(G, s)
    d = [float('inf') for _ in range(n)]
    parent = [None for _ in range(n)]
    for i in range(topo_sorted.index(s)+1, n): #wystarczy jedna pętla bo nie ma krawedzi która nas cofa i poprawi nam ścieżke bo nie ma cyklu mamy graf acykliczny
        for p, weight in G[i]:
            #relax
            if d[p] > d[i] + weight:
                d[p] = d[i]+weight
                parent[p] = i  
            #end relax
    return d, parent


def print_path(start, u, parent):
    #przy pomocy rekurencji
    if start == u:
        print(u)
    else:
        print_path(start, parent[u], parent)
        
def print_path(start, u, parent):
    #przy pomocy staku
    path = [0]
    while u != start:
        u = parent[u]
        path.append(u)
    for i in range(len(path)-1, -1, -1):
        print(path[i], end=" ")
    
    
    
    
    
    
    
    