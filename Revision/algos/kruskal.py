class Node:
  def __init__(self, value):
    self.val = value
    self.parent = self
    self.rank = 0


def find(x):
  # jeśli kompresja ścieżki się zakończy to zwrócimy reprezentata zbioru
  if x.parent != x:
    x.parent = find(x.parent)
  return x.parent

def union(x, y):
  x = find(x)
  y = find(y)
  if x == y: return
  if x.rank > y.rank:
    y.parent = x
  else:
    x.parent = y
    if x.rank == y.rank:
      y.rank += 1

def find_max_vertex(Edges):
  maxi = 0
  for u, v, _ in Edges:
    maxi = max(u, v, maxi)
  return maxi + 1


def kruskal(Edges):
  n = find_max_vertex(Edges)
  Edges.sort(key = lambda x: x[2])

  MST = []
  Vertices = [Node(v) for v in range(n)]
  for edge in Edges:
    u, v, _ = edge
    rootU, rootV = find(Vertices[u]), find(Vertices[v])
    if rootU != rootV:
      union(rootU, rootV)
      MST.append(edge)
  return MST

    

Edges = [(5, 0, 2), (0, 1, 3), (1, 2, 1), (5, 6, 1), (1, 6, 2), (5, 4, 6),(4, 3, 8), (3, 6, 5), (2, 3, 7)]
# [(1, 2, 1), (5, 6, 1), (5, 0, 2), (1, 6, 2), (3, 6, 5), (5, 4, 6)]
print(kruskal(Edges))