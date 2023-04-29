'''
Znajdowanie cyklu Eulera w grafie
'''

def eulerCycle(G, s=0):
    n = len(G)
    time = 0
    cycle = []
    visited = [False]*n
    
    def dfsVisit(G, u):
        nonlocal time
        visited[u] = True
        for v in G[u]:
            # if not visited[v]: #nie sprawdzam czy odwiedzone bo do wierzchołka mogę wejść dowolną liczbe razy
            G[u].remove(v) #usuwam krawedz przez kt przeszedlem w Grafie G
            G[v].remove(u)
            time += 1 #czas odkrycia
            dfsVisit(G, v)
        time += 1 #czas przetworzenia
        cycle.append(u) #dopisuje wierzchołek do cyklu
    
    for u in range(n):
        if not visited[u]:
            dfsVisit(G, u)
    return cycle[::-1]

# G = [[1,2,3], [0,3], [0], [0,1,5], [], [3]]
G1 = [[1, 3, 2], [0, 2], [1, 0], [0, 4], [3]]
#G2 - cykl z wykladu, dl 15 chyba dziła
G2 = [[1, 2], [0, 2, 3, 4, 5, 6], [0, 3, 5, 1, 6, 4], [1, 4, 5, 2], [1, 3, 2, 5], [2, 1, 3, 4], [2, 1]]

print(eulerCycle(G2))    
    