#find the shortest path

from collections import deque

def shortestPath(G, s, k):
    n = len(G)
    q = deque()
    q.append(s)
    visited = [False]*n
    parent = [None]*n
    d = [-1]*n
    visited[s] = True
    d[s] = 0
    while q:
        u = q.popleft()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                d[v] = d[u]+1
                q.append(v)
            if v == k:
                q = deque()
                break
            
    res= [k]
    while parent[k] != None:
        res.append(parent[k])
        k = parent[k]
    return res


G=[[1],[0,5,6],[3,4,5],[6,5,2],[2],[1,2,3],[3,1]]
print(shortestPath(G, 3, 0))    