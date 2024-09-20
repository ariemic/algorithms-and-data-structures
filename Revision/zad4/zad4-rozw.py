from zad4testy import runtests
from collections import deque

def bfs(G, s, t):
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
      if v == t: return d[t]
  



def longer( G, s, t ):
    base_dist = bfs(G, s, t)
    if base_dist == None: return None

    n = len(G)
    # usuwamy po kolei krawedzie i sprawdzamy czy dystans sie wytłużył
    for u in range(n):
      for v in G[u]:
        G[u].remove(v)
        G[v].remove(u)
        dist = bfs(G, s, t)
        if dist == None or dist > base_dist:
          return (u, v)
        G[u].append(v)
        G[v].append(u)
    
    


    

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )