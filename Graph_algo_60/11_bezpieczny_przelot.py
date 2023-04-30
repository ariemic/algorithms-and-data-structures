'''
Zadanie 6. (bezpieczny przelot) Dany jest graf G = (V,E), którego wierzchołki reprezentuja punkty
nawigacyjne nad Bajtocja, a krawedzie reprezentuja korytarze powietrzne miedzy tymi punktami. Kazdy
korytarz powietrzny ei > E powiazany jest z optymalnym pułapem przelotu pi > N (wyrazonym w metrach).
Przepisy dopuszczaja przelot danym korytarzem jesli pułap samolotu rózni sie od optymalnego najwyzej o t
metrów. Prosze zaproponowac algorytm (bez implementacji), który sprawdza czy istnieje mozliwosc przelotu
z zadanego punktu x > V do zadanego punktu y > V w taki sposób, zeby samolot nigdy nie zmieniał pułapu.
Algorytm powinien byc poprawny i mozliwie jak najszybszy. Prosze oszacowac jego złozonosc czasowa.
'''
E = [(0, 2, 5), (0, 1, 1), (1, 4, 1), (1, 2, 2), (2, 3, 6)]
n = 5

from queue import PriorityQueue

def create_graph(E, n):
    n = len(E)
    G = [[]for _ in range(n)] #create graph with proper size
    for edge in E:
        u, v, val = edge[0], edge[1], edge[2]
        G[u].append((v, val))
        G[v].append((u, val))
    return G

def relax(u, v, weight, d, parent):
    if d[v] > d[u] + weight:
        d[v] = d[u]+weight
        parent[v] = u
        return True
    return False

def is_tunnel_ok(edge_weight, p, t):
    for i in range(t+1):
        if edge_weight + i == p or edge_weight - i == p:
            return True
    return False

def safe_flight(Edges, n, p, t, x, y):
    
    G = create_graph(Edges, n)
    visited = [False]*n
    parent = [None]*n
    d = [float('inf')]*n
    d[x] = 0
    
    q = PriorityQueue(x)
    q.put((d[x], x))
    
    while not q.empty():
        d_u, u = q.get()
        for v, edge_weight in G[u]:        
            if not visited[v] and is_tunnel_ok(edge_weight, p, t):
                if relax(u, v, edge_weight, d, parent):
                    q.put((d[v], v))
        visited[u] = True
        if u == y: return True
    return False
   
   
print(safe_flight(E, n, 3, 2, 0, 4))
        


    
    
    
    
    

