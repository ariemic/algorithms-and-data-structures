from queue import PriorityQueue

def prim(G):
  n = len(G)
  visited = [False]*n
  parents = [-1]*n
  weights = [float('inf')]*n

  q = PriorityQueue()
  q.put((0, 0)) #(val, u) -> trzeba w tej kolejności bo tak działa implementacja priority queue w pythonie 
  weights[0] = 0

  while not q.empty():
    _, u = q.get()
    if not visited[u]:
      visited[u] = True

      for v, edge_val in G[u]:

        if not visited[v] and edge_val < weights[v]:
          weights[v] = edge_val
          parents[v] = u
          q.put((edge_val, v))

  return parents, weights

def create_MST(G):
  n = len(G)
  parents, weights = prim(G)
  MST = [[]for _ in range(n)]

  for v in range(n):
    u = parents[v]
    if u != -1:
      MST[u].append((v, weights[v]))
      MST[v].append((u, weights[v]))
  return MST




def undirected_weighted_graph_list(E):
    # Find a number of vertices
    n = 0
    for e in E:
        n = max(n, e[0], e[1])
    n += 1
    # Create a graph
    G = [[] for _ in range(n)]
    for e in E:
        G[e[0]].append((e[1], e[2]))
        G[e[1]].append((e[0], e[2]))
    return G

G = undirected_weighted_graph_list([(0, 1, 1), (1, 2, 5), (2, 3, 3000), (0, 5, 12), (1, 5, 7),
(5, 2, 6), (5, 4, 8), (4, 2, 4), (4, 3, 9)])
  
print( prim(G) )
# print( create_MST(G) )