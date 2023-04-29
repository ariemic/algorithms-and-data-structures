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

def DFS_mosty(G):
    n = len(G)
    visited = [False]*n
    d = [0]*n #zapisuje czas odwiedzenia danego wierzchołka pierwszy raz
    time = 0
    def dfsVisit(G, u):
        nonlocal time
        time += 1
        d[u]=time
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                dfsVisit(G, v)
        #nie potrzebuje czasu przetworzenia wierzchoła
    #end def
    low = [0]*n
    for u in range(n):
        if not visited[u]:
            dfsVisit(u)
    
    
        