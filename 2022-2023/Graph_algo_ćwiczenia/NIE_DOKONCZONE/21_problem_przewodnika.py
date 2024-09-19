'''
Zadanie 5. (problem przewodnika turystycznego) Przewodnik chce przewiezc grupe K turystów z
miasta A do miasta B. Po drodze jest jednak wiele innych miast i miedzy róznymi miastami jezdza autobusy o
róznej pojemnosci. Mamy dana liste trójek postaci (x, y, c), gdzie x i y to miasta miedzy którymi bezposrednio
jezdzi autobus o pojemnosci c pasazerów.
Przewodnik musi wyznaczyc wspólna trase dla wszystkich tursytów i musi ich podzielic na grupki tak,
zeby kazda grupka mogła przebyc trase bez rodzielania sie. Prosze podac algorytm, który oblicza na ile
(najmniej) grupek przewodnik musi podzielic turystów (i jaka trasa powinni sie poruszac), zeby wszyscy
dostali sie z A do B.
'''
from queue import PriorityQueue
#Jeśli chce używać PriorityQueue jako kopca max to musze każdą wartość przemnożyć przez -1 -> dijkstra w


def max_vertex(Edges):
    return max(Edges[i][1] for i in range(len(Edges)))+1

def create_grapth(Edges):
    #w tym sposobie powstają parallel edges
    n = max_vertex(Edges)
    G = [[]for _ in range(n)]
    for edge in Edges:
        u, v, val = edge[0], edge[1], (-1)*edge[2] #robie ujemne wagi na krawedziach ->kopiec min w max
        G[u].append((v, val))
        G[v].append((u, val))
    return G
        

def relax(u, v, edge_weight, d, parent, edges_weights):
    if d[v] > d[u] + edge_weight:
        d[v] = d[u] + edge_weight
        parent[v] = u
        edges_weights[v] = edge_weight
        return True
    return False

def dijkstra(G, s, t):
    n = len(G)
    d = [float('inf')]*n
    parent = [None]*n 
    edges_weights = [float('-inf')]*n
    
    visited = [False]*n
    q = PriorityQueue()
    d[s] = 0
    q.put((d[s],s))
    while not q.empty():
        d_u, u = q.get()
        for v, edge_weight in G[u]:
            if not visited[v] and relax(u, v, edge_weight, d, parent, edges_weights):
                #przy krawedziach wielokrotnych parent zapisze parenta dla najwiekszej wagi krawedzi
                q.put((d[v], v))
        visited[u] = True 
        if u == t:            
            return parent, edges_weights
    return None, None

def guide_problem(Edges, A, B, K):
    #dijkstra z kopcem maximum; przy tym zapisuje najmniejsza wage na tej scieżce bo tyle osob z grupy moge wpakować tą trasą
    #po użyciu danych krawędzi usuwam je lub dworze macierz w kt zapisuje kt krawedzie zużyłem już
    G = create_grapth(Edges)
    group_cnt, paths = 0, []
    while K != 0:  
        parent, edges_weights = dijkstra(G, A, B)
        if parent != None:
            n = len(edges_weights)
            group_size = max(edges_weights[i] for i in range(n))*(-1)
            K -= group_size       
            group_cnt += 1 
            paths.append(create_path(G, parent, B))    
            delete_edges(G, parent, edges_weights, B)
        return False
            
    return paths, group_cnt


#Jeśli autobus jedzie od stacji 0 do 2 to tworze krawedz tylko miedzy tymi wierzchołkami bo autobus jedzie między dwoma miastami!

#mogą istnieć krawędzie wielokrotne pomiędzy wierzchołkami ponieważ mogą istnieć autobusy które mają ten sam plan podróży -> trzeba zmodyfikować dijkstre lub mądrze stworzyć graf

#czy dijkstra działa dla wielokrotnych krawedzi? W podstawowej implementacji nie działa, wynik zależałby od kolejności krawędzi w grafie
#https://stackoverflow.com/questions/37504390/dijkstra-with-parallel-edges-and-self-loop

def create_path(G, parent, t):
    path = [t]
    while t != None:
        t = parent[t]
        path.append(t)
    return path[::-1][1:]

def delete_edges(G, parent, edges_weights, t):
    while parent[t] != None:
        u, v, val = t, parent[t], edges_weights[t]
        G[u].remove((v, val))
        G[v].remove((u, val))
        t = parent[t]




edges = [(0, 1, 20),(0, 1, 30), (1, 4, 25), (0, 4, 10), (0, 2, 30), (2, 3, 21), (3, 4, 22)]

print(guide_problem(edges, 0, 4, 80))
# edges = [
#     (0, 1, 50),
#     (0, 3, 25),
#     (1, 2, 75),
#     (2, 3, 20),
#     (3, 5, 50),
#     (5, 6, 2),
#     (4, 6, 10),
#     (6, 7, 20),
#     (7, 8, 70),
#     (1, 5, 75),
#     (2, 5, 30),
#     (3, 4, 50)
# ]
# print(guide_problem(edges, 0, 8, 100))