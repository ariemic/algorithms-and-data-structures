'''
Zadanie 2. (dobry poczatek) Wierzchołek v w grafie skierowanym nazywamy dobrym poczatkiem jesli
kazdy inny wierzchołek mozna osiagnac sciezka skierowana wychodzaca z v. Prosze podac algorytm, który
stwierdza czy dany graf zawiera dobry poczatek.


WK żadna krawędz nie może do niego wchodzić d(u)=0 dla krawedzi wchodzących -> robie sortowanie topologiczne aby taki znaleźć
Robie od podejrzanego wierzchołka dfs'a jeśli po jednym puszczeniu tablica visited zawiera tylko wartości True to istnieje dobry początek wpw nie istnieje
'''
from collections import deque

def dfs_visit(G, u, visited, arr=None):        
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                dfs_visit(G, v)
        if arr != None:
            arr.apendleft(u)
        
def sort_topologycly(G):
    n = len(G)
    visited = [False]*n
    topo_sorted = deque()
    
    for u in range(n):
        if not visited[u]:
            dfs_visit(G, u, visited, topo_sorted)
    return topo_sorted


def good_beginning(G):
    n = len(G)
    visited=[False]*n
    source = sort_topologycly(G)[0]
    dfs_visit(G, source, visited)
    if visited == [True]*n: return True
    return False