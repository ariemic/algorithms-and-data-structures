'''
Zadanie 1. (sciezka Hamiltona w DAGu) Sciezka Hamiltona to sciezka przechodzaca przez wszystkie
wierzchołki w grafie, przez kazdy dokładnie raz. W ogólnym grafie znalezienie sciezki Hamiltona jest problemem
NP-trudnym. Prosze podac algorytm, który stwierdzi czy istnieje sciezka Hamiltona w acyklicznym
grafie skierowanym.
'''

#1 sposób - Brute - sprawdzam rozpoczynając od każdego wierzchołka czy zaczanjąc od niego odwiedze wszystkie  pozosałe wierzchołki po przejściu jeden raz dfs'em
#NIE ZADZIAŁA BO nie chce żeby mój dfs się cofnął i poszedł w drugą stronę kiedy wracając zobaczy że jeszcze jakiś wierzchołek jest nie odwiedzony to się cofnnie i go odwiedzi co wypluwa złe
#rozwiązanie


#2 sposob DOBRY - Szukam wierzchołka który ma stopień 0 (WK) czyli żadna krawedz do niego nie wchodzi - jest źródłem, robie z niego sortownie topologiczne; idę w kolejności sortowania topologicznego
#i sprawdzam czy jest krawedz (v, v+1)



#jak znaleźć wierzchołek ze stopniem 0? Robie sortowanie topologiczne po nim wierzchołek bedzie na ideksie 0 zwróconej przez funkcji liście

from collections import deque

def addEdges(G, edges):
    for edge in edges:
        a = edge[0]
        b = edge[1]
        G[a].append(b)
    
def sort_topologycly(G):
    n = len(G)
    visited = [False]*n
    topo_sorted = deque()
    
    def dfs_visit(G, u):        
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                dfs_visit(G, v)
        topo_sorted.appendleft(u)
    
    for u in range(n):
        if not visited[u]:
            dfs_visit(G, u)
    
    return topo_sorted

def hamiltonian_path(G):
    sorted_topo = sort_topologycly(G)
    n = len(sorted_topo)
        
    for i in range(n-1):
        a, b = sorted_topo[i], sorted_topo[i+1]
        if b not in G[a]: #jeśli nie ma krawędzi do b pod indeksem a (reprezentacja przez listy sąsiedztwa) to dfs sortując topologicznie gdzieś się rozgałęził więc nie jesteśmy w stanie idąc tylko przed siebie odwiedzić każdego wierzchołka    
            return False
    return True
    
n = 6
G = [ [] for _ in range(n) ]
edges = [ (0,1), (1, 2), (2, 4), (2, 5), (1, 3) ]
addEdges(G, edges)
print( hamiltonian_path(G) )

edges = [ (0, 1), (1, 2), (2, 4), (2, 5), (1, 3), (2, 3), (3, 5), (5, 4) ]
n = 6
addEdges(G, edges)
print( hamiltonian_path(G) )