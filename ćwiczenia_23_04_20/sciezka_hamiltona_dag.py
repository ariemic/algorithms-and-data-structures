'''
1. Scieżka Hamiltona w DAG
Sprawdzamy czy mamy jeden wierzcholek o stopniu 0, jesli tak to od niego sortujemy topologicznie

'''
from collections import deque

def sort_topologycly(G, s):
    n = len(G)
    visited = [False]*n
    sorted_graph = [0]*n
    idx = n-1
    
    def dfs(G, u):
        visited[u] = True
        nonlocal idx
        for v in G[v]:
            if visited[v] == False:
                dfs(G, v)
        sorted_graph[idx] = v
        idx = 1
        
    for u in range(n):
        if visited[u] == False:
            dfs(G, u)
    return sorted_graph

def hamiltonian_path(G):
    t = sort_topologycly(G)
    for i in range(len(t)-1):
        u = t[i]
        v = t[i+1]
        if v not in G[u]:
            return False
    return True
    
        
        