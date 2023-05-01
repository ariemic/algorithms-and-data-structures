'''
Zadanie 7. (problem stacji benzynowych na grafie) Pewien podróznik chce przebyc trase z punktu A
do punktu B. Niestety jego samochód spala dokładnie jeden litr paliwa na jeden kilometr trasy.Wbaku miesci
sie dokładnie D litrów paliwa. Trasa jest reprezentowana jako graf, gdzie wierzchołki to miasta a krawedzie to
łaczace je drogi. Kazda krawedz ma długosc w kilometrach (przedstawiona jako licza naturalna). W kazdym
wierzchołku jest stacja benzynowa, z dana cena za litr paliwa. Prosze podac algorytm znajdujacy trase z
punktu A do punktu B o najmniejszym koszcie. Prosze uzasadnic poprawnosc algorytmu.

Robie dijkstre z tym że mnoże krawędzie przez cene paliwa na stacji do ktorej mam dojechać - chyba jednak nie ma tak łatwo 
'''
from queue import PriorityQueue

def relax(u, v, edge_weight, d, parent):
    if d[v] > d[u] + edge_weight:
        d[v] = d[u] + edge_weight
        parent[v] = u
        return True
    return False

def Dijkstra(G, s, t):
    n = len(G)
    d = [float('inf')]*n
    parent = [None]*n
    visited = [False]*n
    q = PriorityQueue()
    d[s] = 0
    q.put((d[s],s))
    while not q.empty():
        d_u, u = q.get()
        for v, edge_weight in G[u]:
            if not visited[v] and relax(u, v, edge_weight, d, parent):
                q.put((d[v], v))
        visited[u] = True 
        if u == t:
            return d[t]
        
        


