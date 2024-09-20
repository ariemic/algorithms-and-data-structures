#* złożoność O(V + E) dla listowej

from collections import deque

def bfs(G, s=0):
  n = len(G)
  parent = [None]*n
  visited = [False]*n
  d = [-1]*n
  q = deque()
  q.append(s)
  visited[s], d[s] = True, 0
  while q:
    u = q.popleft()
    for v in G[u]:
      if not visited[v]:
        visited[v] = True
        d[v] = d[u] + 1
        parent[v] = u
        q.append(v)
  return parent, visited, d




G=[[1],[0,5,6],[3,4,5],[6,5,2],[2],[1,2,3],[3,1]]
# G = [[2, 6], [4, 3], [1], [], [], [1], [5]]         
parent, visited, d = bfs(G)
print(parent, visited, d)