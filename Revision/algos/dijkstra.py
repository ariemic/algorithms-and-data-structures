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