from zad5testy import runtests

from queue import PriorityQueue

def relax(u, v, edge_weight, d, parent):
    if d[v] > d[u] + edge_weight:
        d[v] = d[u] + edge_weight
        parent[v] = u
        return True
    return False

def dijkstra(G, s, t):
  n = len(G)
  d = [float("inf")]*n
  parent = [None]*n
  visited = [False]*n
  q = PriorityQueue()
  d[s] = 0
  q.put((d[s], s))
  while not q.empty():
    d_u, u = q.get()
    for v, edge_weight in G[u]:
      if not visited[v] and relax(u, v, edge_weight, d, parent):
         q.put((d[v], v))
    visited[u] = True
    if u == t: return d[t]


def buid_adj_graph(E, S, n):
  G = [[]for _ in range(n)]
  for (u, v, edge) in E:
    G[u].append((v, edge))
    G[v].append((u, edge))
  
  m = len(S)
  for i in range(m-1):
    u = S[i]
    for j in range(i+1, m):
      v = S[j]
      # Jezeli byly juz takie krawedzie w grafie ale z jakąś wagą to bedziemy miec zduplikowane krawedzie pasowałoby zostawić tylko te zerowe a tamte usunąć
      G[u].append((v, 0))
      G[v].append((u, 0))
  
  return G
      


def spacetravel( n, E, S, a, b ):
    G = buid_adj_graph(E, S, n)
    return dijkstra(G, a, b)
    

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )