'''
1. Sprawdzanie czy graf jest dwudzielny (czyli zauwazyc, ze to 2-kolorowanie i uzyc DFS lub BFS).

Bipartie graph doesn't need to be connected.
'''
from collections import deque

def bfs_is_bipartite(G, s=0):
    n = len(G)
    visited = [False]*n
    colors = [-1]*n
    q = deque()
    visited[s] = True
    colors[s] = 0
    q.append(s)
    while q:
        u = q.popleft()
        for v in G[u]:
            if not visited[v]:
                q.append(v)
                visited[v] = True
                colors[v] = (u+1)%2
            else:
                if colors[v] == colors[u]: 
                    return False
    return True


def dfs_is_bipartite(G, s=0):
    n = len(G)
    colors = [-1]*n
    colors[s]=0
    visited = [False]*n
    
    def dfs_visit(G, u):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                colors[v] = (u+1)%2
                dfs_visit(G, v)
            else:
                if colors[v] == colors[u]: return False    
        return True
        
    for u in range(n):
        if not dfs_is_bipartite(G, u): return False
    return True
    