'''
Znajdowanie cyklu Eulera w grafie nieskierowanym i spójnym
'''

def edges_number(G):
    #return number of edges for undirected connected graph
    cnt = 0
    for arr in G:
        cnt += len(arr)
    return int(cnt/2)

def eulerCycle(G, s=0):
    n = len(G)
    cycle = []
    visited = [False]*n
    edges = edges_number(G1)
    cnt = 0
    
    def dfsVisit(G, u):
        nonlocal cnt
        visited[u] = True
        for v in G[u]:
            # if not visited[v]: #nie sprawdzam czy odwiedzone bo do wierzchołka mogę wejść dowolną liczbe razy
            G[u].remove(v) #usuwam krawedz przez kt przeszedlem w Grafie G
            G[v].remove(u)
            cnt += 1
            dfsVisit(G, v)
        cycle.append(u) #dopisuje wierzchołek do cyklu
        return 
    
    dfsVisit(G, s)
    #Jeśli po wykonaniu dfs visit G będę puste znaczy że przeszliśmy po wszystkich krawędziach, czyli istnieje cykle Eulera jeśli liczba usuniętych krawedzi bedzie rowna
    #liczbie krawedzi w grafie
    if cnt == edges:
        print("Eulerian cycle exist!")
        return cycle[::-1]
    return None

# G = [[1,2,3], [0,3], [0], [0,1,5], [], [3]]
G1 = [[1, 3, 2], [0, 2], [1, 0], [0, 4], [3]]
#G2 - cykl z wykladu, dl 15 chyba dziła
G2 = [[1, 2], [0, 2, 3, 4, 5, 6], [0, 3, 5, 1, 6, 4], [1, 4, 5, 2], [1, 3, 2, 5], [2, 1, 3, 4], [2, 1]]

print(eulerCycle(G1))    
    