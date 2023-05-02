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
    G = [[]*n]
    for edge in Edges:
        u, v, val = edge[0], edge[1], (-1)*edge[2] #robie ujemne wagi na krawedziach ->kopiec min w max
        G[u].append((v, val))
        G[v].append((u, val))
    return G
        

def relax(u, v, edge_weight, d, parent):
    if d[v] > d[u] + edge_weight:
        d[v] = d[u] + edge_weight
        parent[v] = (u, edge_weight)
        return True
    return False

def dijkstra(G, s, t):
    n = len(G)
    d = [float('inf')]*n
    parent = [None]*n #trzuma krotki (do, waga_krawedzi)
    visited = [False]*n
    q = PriorityQueue()
    d[s] = 0
    q.put((d[s],s))
    while not q.empty():
        d_u, u = q.get()
        for v, edge_weight in G[u]:
            if not visited[v] and relax(u, v, edge_weight, d, parent):
                #przy krawedziach wielokrotnych parent zapisze parenta dla najwiekszej wagi krawedzi
                q.put((d[v], v))
        visited[u] = True 
        if u == t:            
            return  parent
    return None

def guide_problem(Edges, A, B, K):
    #dijkstra z kopcem maximum; przy tym zapisuje najmniejsza wage na tej scieżce bo tyle osob z grupy moge wpakować tą trasą
    #po użyciu danych krawędzi usuwam je lub dworze macierz w kt zapisuje kt krawedzie zużyłem już
    G = create_grapth(Edges)
    group_cnt, paths = 0, []
    while K != 0:  
        parent= dijkstra(G, A, B)
        if parent != None:
            n = len(parent)
            vertices = [parent[i][0] for i in range(n)] #create path form it because parent array keeps tuples (vertex, edge_weight)
            group_size = min(parent[i][1] for i in range(n))*(-1)
            K -= group_size    
            edge_delete(G, vertices, A, B)


#Jeśli autobus jedzie od stacji 0 do 2 to tworze krawedz tylko miedzy tymi wierzchołkami bo autobus jedzie między dwoma miastami!

#mogą istnieć krawędzie wielokrotne pomiędzy wierzchołkami ponieważ mogą istnieć autobusy które mają ten sam plan podróży -> trzeba zmodyfikować dijkstre lub mądrze stworzyć graf

#czy dijkstra działa dla wielokrotnych krawedzi? W podstawowej implementacji nie działa, wynik zależałby od kolejności krawędzi w grafie
#https://stackoverflow.com/questions/37504390/dijkstra-with-parallel-edges-and-self-loop



def edge_delete(G,parent,start,end):
    x = parent[end]
    while x != start:
        i = x[0]
        x = parent[x]
        j = x[0]
        weight = j[1]
        Edges.remove(weight(i,j,weight))



Edges = [(0, 1, 20),(0, 1, 30), (1, 4, 25), (0, 4, 10), (0, 2, 30), (2, 3, 21)]