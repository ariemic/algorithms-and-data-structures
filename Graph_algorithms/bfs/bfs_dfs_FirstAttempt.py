from collections import deque

def bfs(G, root):
    #d - distance - wave number - let us know on which level we are
    visited = [0]*len(G)
    q = deque()
    q.append((root, 0))
    while q:
        # print(q)
        v, d = q.popleft()
        for u in G[v]:
            if visited[u] == 0:#if not visited 
                q.append((u, d+1))
                visited[u] = d+1
    return visited
    
G = [[2, 6], [4, 3], [1], [], [], [1], [5]]

print(bfs(G, 0))

def dfs(G, s):
    n = len(G)
    visited = [0]*n
    def rek(G, s, cnt=0):
        nonlocal visited
        visited[s] = cnt
        for u in G[s]:
            if not visited[u]:
                rek(G, u, cnt+1)
    rek(G, s)
    return visited
    
print(dfs(G, 0))