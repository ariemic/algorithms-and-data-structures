#Znalezc najkrótszą sciezke z s do t
#Tworzymy sztuczne wierzchołki odpowiednio dzielące krawędzie -> dodawanie sztucznych wierzchołków
#implementacja: nie modyfikujemy grafu -> za duzo roboty
#kiedy widzimy ze krawedz ma wage 2 to wrzucamy go do kolejki z licznikim 1, nastepnym razem z licznikiem 0
#czyli wrzucamy do kolejki wierzchołki w krotce z licznikiem za każdym razem o 1 mniejszym niż akutalna długość krawędzi


from collections import deque

def max_vertex(E):
    n = len(E)
    return max(E[i][1] for i in range(n))+1


def build_graph(E):
    #tworzy graf nieskierowany
    #przeksztalcam graf w liste sasiedztwa z krotka reprezentujaca wage
    n = len(E)
    G = [[]for _ in range(max_vertex(E))] #create graph with proper size
    for tup in E:
        u, v = tup[0], tup[1]
        val = tup[2]
        G[u].append((v, val))
        G[v].append((u, val))
    return G
    

def bfs(Edges, s, t):
    #search for path with smallest sum up weights
    G = build_graph(Edges)
    n = len(G)
    visited = [False]*n
    parent = [None]*n
    path, cost = [], 0
    q = deque()
    q.append(s)
    while q:
        u, w_u = q.popleft()
        for v, w_v in G[u]:        
            if not visited[v]:
                q.append(v, w_v)
                visited[v] = True
                parent[v] = u
            
        
        
        
s = (0, 0)
Edges = [(0,1, 5),
(1,2,21),
(1,3, 1),
(2,4, 7),
(3,4,13),
(3,5,16),
(4,6, 4),
(5,6, 1)]

print(max_vertex(Edges))
print(build_graph(Edges))