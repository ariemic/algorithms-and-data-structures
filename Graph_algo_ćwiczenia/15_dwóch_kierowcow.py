'''
Zadanie 6. (dwóch kierowców) Dana jest mapa kraju w postaci grafu G = (V,E), gdzie wierzchołki to
miasta a krawedzie to drogi łaczace miasta. Dla kazdej drogi znana jest jej długosc (wyrazona w kilometrach
1
jako liczba naturalna). Alicja i Bob prowadza (na zmiane) autobus z miasta x > V do miasta y > V , zamieniajac
sie za kierownica w kazdym kolejnym miescie. Alicja wybiera trase oraz decyduje, kto prowadzi pierwszy.
Prosze zapropnowac algorytm, który wskazuje taka trase (oraz osobe, która ma prowadzic pierwsza), zeby
Alicja przejechała jak najmniej kilometrów. Algorytm powinien byc jak najszybszy (ale przede wszystkim
poprawny).

Mam dany wierzchołek początkowy, szukam najkrótszej ścieżki do przejechania dla Alice, drogi przejechane przez Boba mnie nie obchodzą muszę jedynie trzymać parametr kto ostatni prowadził jeśli ostatnio prowadziła Alice
oznacza to że teraz jedzie Bob a jako że szukam najkrótszej ścieżki dla Alice to te sąsiednie krawędzie zeruje bo nie interesują mnie ich wagi, traktuje je jakbym ich nie było bo to bob sie na nich meczy!

Rozważam dwa przypadki Alicja jedzie jako pierwsza lub Bob jedzie jako pierwszy. Z tych dwóch najkrótszych ścieżek wybieram krótszą.
'''
from queue import PriorityQueue

def relax(u, v, edge_weight, d, parent):
    if d[v] > d[u] + edge_weight:
        d[v] = d[u] + edge_weight
        parent[v] = u
        return True
    return False

def Dijkstra(G, s, t, driver):
    n = len(G)
    d = [float('inf')]*n
    parent = [None]*n
    visited = [False]*n
    q = PriorityQueue()
    d[s] = 0
    q.put((d[s],s, driver))
    while not q.empty():
        du, u, who_will_drive = q.get()    
        #teraz bedzie prowdzić Bob
        for v, edge_weight in G[u]:
            if not visited[v]:
                if who_will_drive == 'Bob':
                    d[v] = d[u]
                    parent[v] = u
                    q.put((d[v], v, 'Alice'))
                elif who_will_drive == 'Alice' and relax(u, v, edge_weight, d, parent):
                    q.put((d[v], v, 'Bob'))
        visited[u] = True
        if u == t:
            return parent, d[t]
    return [], float('inf')
            
def two_drivers(G, x, y):
    #algorytm zwraca trase przejechaną przez Alicje i osobę która prowadzi pierwsza
    res = []
    drivers = ['Alice', 'Bob']
    Alice_effort = float('inf')
    for driver in drivers:
        parent, effort = Dijkstra(G, x, y, driver)
        if effort < Alice_effort:
            Alice_effort = effort
            res = [driver, effort, parent]
    parent = res[2]
    path = [y]
    while y != None:
        y = parent[y]
        path.append(y) 
    res[2] = path[:-1][::-1]#bez None na początku i odwrócone
    return res


graph = [[(1, 4), (2, 1), (3, 5)],
         [(0, 1), (4, 2)],
         [(0, 1), (5, 8), (6, 7)],
         [(0, 5), (5, 7)],
         [(1, 2), (7, 10)],
         [(2, 8), (3, 7), (8, 3)],
         [(2, 7), (7, 6)],
         [(4, 10), (6, 6), (9, 11)],
         [(5, 3), (9, 9)],
         [(7, 11), (8, 9)]]
n = len(graph)-1

print(two_drivers(graph, 0, n))

            