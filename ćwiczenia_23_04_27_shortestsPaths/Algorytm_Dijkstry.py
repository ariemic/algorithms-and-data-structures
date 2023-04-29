'''
Algorytm Dijikstry - algorytm elementarny ale w każdym kroku skacze do najbliższego prawadziwego wierzchołka - oparty na bfs'ie

Złożoność dla list sąsiedztwa z kopcem binarnym - O(ElogV)
Dla reprezentacji macierzowej używanie kopca binarnego jest niewygodne, zamiast tego przeglądam liniowo wierzchołki i wybieram wierzcholek z najmniejsza wartością u.d
taki który nie został jeszcze przetworzony  - O(V^2) z liniową kolejką

Nie wymagamy wag naturalnych, ale muszą być nieujemne -> uwaga znalezienie najmniejszej ujemnej wartości i dodanie tej wartości do wszystkich
wag krawedzi powodując że bedziemy mieć tylko nieujemne wagi nie zadziała ponieważ jeżeli ścieżka będzie miec dużo wiecej krawedzi niż inna
ale początkowo o bardzo niskich wagach dodanie dużej wagi spowoduje ze ta sciezka nie bedzie mogła zostac uznana za najkrótsza

Notacja
G = (V, E)
w(u,v) - odległość z u do v
u.d - oszacowanie odległości ze źródła do u
u.parent - poprzednik na najkrótszej ścieżce ze źródła


Działanie: Start z s należacego do V
1. Umieść wszystkie wierzchołki w kolejce priorytetowej (typ minimimum)z oszcowaniem odległości inf - w praktyce realizowane inaczej - O(log(rozmiaru koleji))
2. Zmień odległość s na 0
3. Póki wierzchołki są w kolejce
    - wyjmij z kolejki wierzchołek u o minimalnej wartości u.d
    dla każdej krawędzi {u,v} [(u,v)-dla grafu skierowanego] wykonaj relaksacje
    
        def relax(u, v):
            if v.d > u.d + w(u, v):#odkrylismy ze oszacowanie v jest nie optymalne
                v.d = u.d + w(u,v)
                v.parent = u
                
    Każda krawędz jest relaksowana conajwyżej raz
    
Algorytm szuka najkrotszych sciezek z początkowego wierzchołka do wszystkich 

Dlaczego algorytm Dijkstry jest poprawny?
- bo ralizuje BFS z dodatnimi wierzchołkami (nie prawidłowy argument jeśli wagi nie są naturalne)
- dowód indukcyjny

Tw. Gdy algoryt Dijkstry wyciąga wierzchołek u z kolejki, to jego pole u.d zawiera długość najkrótszej ścieżki z s do u
Dowód. (przez indukcje)
Podstawa indukcji - dla s jest to oczywisty sposób prawda
Krok indykcyjny: 
    wierzchołki, które zostały wyjęte z kolejki -> ich pola d mają prawidłowe wartości (tak samo pola parent)
    wierzchołki w kolejce -> skoro każda inna ścieżka jest gorsza to nasza jest najlepsza
    
'''
from queue import PriorityQueue

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

def relax(u, v, edge_weight, d, parent):
    if d[v] > d[u] + edge_weight:
        d[v] = d[u] + edge_weight
        parent[v] = u
        return True
    return False

def dijkstra(Edges, s):
    #for adjency representation graph
    G = build_graph(Edges)
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
        visited[u] = True #zapewnia nas nie będziemy cofać się do tyłu w grafie
    return d, parent
    
    
Edges = [(0,1, 5),
(1,2,21),
(1,3, 1),
(2,4, 7),
(3,4,13),
(3,5,16),
(4,6, 4),
(5,6, 1)]

d, parent = dijkstra(Edges, 0)
print(d, parent)