""" 
Sortuje krawędzie, następnie przechodzę sliding windowem biorąc zawsze n - 1 krawędzi (jest to własność drzewa - zawsze ma taką wielkość) jeśli znalazłem drzewo MST to jest to najmniejsze możliwe więc je zracam.
"""

from kol2testy import runtests

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

def build_edges(G):
    n = len(G)
    Edges = []
    for u in range(n):
      for v, edge_val in G[u]:
        if u < v:
            Edges.append((u, v, edge_val ))
    return n, Edges

  
def kruskal(Edges, n):
  MST = []
  Vertices = [Node(v) for v in range(n)]
  for edge in Edges:
    u, v, _ = edge
    rootU, rootV = find(Vertices[u]), find(Vertices[v])
    if rootU != rootV:
      union(rootU, rootV)
      MST.append(edge)
  return MST



def beautree(G):
  # własności drzewa |V| = |E| + 1 => len(MST) = n - 1, n = |V|
  n, Edges = build_edges(G)  
  TREE_LEN = n - 1
  Edges.sort(key = lambda x: x[2])
  mini = float("inf")
  m = len(Edges)
  if m < TREE_LEN: return None
  for i in range(m - (TREE_LEN) + 1):
    # przesuwamy okno o długości TREE_LEN
    j = i+TREE_LEN
    MST = kruskal(Edges[i:j], n)
    # teraz tworzymy MST tylko na fragment grafu a musimy zawsze na cały graf stworzyć
    if MST != None and len(MST) == TREE_LEN:
      suma = 0
      for _,_, edge_val in MST:
        suma += edge_val
      mini = min(mini, suma)
      return mini #pierwsze drzewo które znajdziemy będzie mieć najmniejszą wagę ponieważ krawedzie są posorotwane nie malejąco i wielkość drzewa MST jest stała

  return None

  

#Musimy zawsze wziąć ciąg krawędzi bo jeżeli zostawimy luke to drzewo nie będzie piękne -> nie spełni warunków zadania
# G = [[(1, 3), (2, 1), (4, 2)], [(0, 3), (2, 5)], [(1, 5), (0, 1), (3, 6)], [(2, 6), (4, 4)], [(3, 4), (0, 2)]]
Edges = [(0, 2, 1), (0, 4, 2), (0, 1, 3), (3, 4, 4), (1, 2, 5), (2, 3, 6)] #posortowane
# beautree(G)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( beautree, all_tests = True )
