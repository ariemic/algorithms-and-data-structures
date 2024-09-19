'''
Alogrytm wyszukiwania wszystkich mostów w grafie
Most to krawędz od wierzchołka do jego rodzica, wiec początkowy wierzchołek mający low(v)=d(v) nie spełnia założeń mostu gdyż nie ma rodzica!

1. Wykonuj DFS, dla każdego v zpaisz jego czas odwiedzenia d(v) - NIE przetworzenia
2. Dla każdego wierzchołka v oblicz low(v) = min( d(v); min(d(u), gdzie z v jest krawedz wsteczna do u; min(low(w)),w to dziecko v w dfs))
low(v) = min{ d(v), min{d(u}, min{low(w)} }
3. Mosty to krawędzie {v, parent(v)} takie gdzie d(v)=low(v)

low(v)- identyfikator cyklu

Jeśli low(v) < d(v) to {p(v), v} nie jest mostem, bo wchodząc do v ustawiamy low(v) = d(v), idąc dalej
low(v) musiał zmaleć kiedy istniała jakaś rawędź wsteczna która spowodowała obniżenie stopnia jakiegoś wierzhołka
niżej w rekurencyjnym przechodzeniu dfs'a, dfs cofając się sprawdzał czy low danego wierzchołka jest niższy od 
swojego dziecka jeśli nie był to rodzic przejmował jego wartość low tym samym niszcząc równoważność
low(v)=d(v) na low(v) < d(v).

UWAGA! Jeśli podzielimy most na fragmenty to algorytm wykryje każdy z nich, gdyż każdy jest mostem.
'''
#Algorytm ma zwracać liczbę mostów w grafie oraz liste krotek z zapisanymi mostami 

def Bridges(G):
    #algorytm zwraca liczbe mostów w grafie oraz wierzchołki je tworzące w postaci listy krotek
    n = len(G)
    visited = [False]*n
    parent = [None]*n
    visit_time = [0]*n
    low = [float('inf')]*n
    bridges = []
    time = 0

    def dfs_visit(G, u):
        nonlocal time
        
        time += 1
        visited[u] = True
        visit_time[u], low[u] = time, time #1 krok
        
        for v in G[u]:
            if not visited[v]:
                parent[v] = u
                dfs_visit(G, v) #najpierw wchodzę rekurencją później przypisuje low, nie moge na odwrót
                low[u] = min(low[u], low[v]) #bierzemy paremetry low ponieważ visit_time nie ulega zmienie, interesuje nas tylko przy patrzeniu na krawedz wsteczna!
                
            elif v != parent[u]:#co znaczy ten warunek - nie za bardzo rozumiem
                low[u] = min(low[u], visit_time[v]) #patrze na krawedz wsteczną jeśli nie mogę wejść głębiej bo już wszystkie sąsiednie wierzchołki są odwiedzone
        
    
    for u in range(n):
        if not visited[u]:
            dfs_visit(G, u)
            
    for u in range(n):
        if visit_time[u] == low[u] and parent[u] != None:
            bridges.append((parent[u], u))
    return bridges




G = [[1, 4], [0, 2], [1, 3, 4], [2, 5, 6], [0, 2], [3, 6], [3, 5, 7], [6]]
bridges = Bridges(G)
print(bridges)
    
        