'''
Zadanie 4. (malejace krawedzie) Dany jest graf G = (V,E), gdzie kazda krawedz ma wage ze zbioru
{1, . . . , SES} (wagi krawedzi sa parami rózne). Prosze zaproponowac algorytm, który dla danych wierzchołków
x i y sprawdza, czy istnieje sciezka z x do y, w której przechodzimy po krawedziach o coraz mniejszych wagach.


Przeszukiwanie w glab

Dany jest graf gdzie kazda krawedz ma wage calkowita i wagi sa parami rozne ( 1 do n )
Algorytm, ktory dla danych wierzcholkow sprwadza, czy istnieje sciezka miedzy dwoma wierzcholkami
o kazdej krawedzi z waga coraz mniejsza. Czy mozna tak dojsc? 

Dodatkowy argument, ktory mowi o wadze ostatniej krawedzi.
Robimy przeszukanie dla wszystkich krawedzi, ktore maja wage mniejsza
Nie mamy visted, mozemy wchodzic do wierzcholkow kilka razy 
Nie zapetlimy sie, nie cofniemy sie, bo wchodzimy do krawedzi o MNIEJSZEJ wadze 
Wagi sa tez parami rozne 
'''
#7)Malejące krawędzie - G=(V,E) nieskierowany, koszty krawędzi {1...|E|} s->t po krawędziach o coraz mniejszych wagach -> DFS -> nie sprawdzamy visited, sprawdzamy czy koszt mniejszy

G = [[1, 0], [0, 1], [2, 0], [0, 2], [4, 0], [0, 4], [3, 2],  [2, 3], [6, 3], [3, 6], [3, 4], [4,3]]
wagi = [7, 7, 2, 2, 5, 5, 4, 4, 1, 1, 3, 3] #waga jest przypisane krawedzi pod tym samym indeksem

#zamiast dwóch tablic w tablicy z grafem G mogę przechowywać dane w postaci krotek (krawedz, waga)

G = [[1, 0], [0, 2], [0, 4], [2, 3], [3, 6], [4,3]] #skierowany
wagi = [7, 2, 5, 4, 1, 3] #waga jest przypisane krawedzi pod tym samym indeksem

def merge_G_wagi_together(G, wagi):
    pass

from collections import deque

def vertices_(G):
    #zwraca liczbe wiercholków w grafie (p.lista kraw)
    maxi =  0
    for arr in G:
        for i in arr:
            if i > maxi:
                maxi = i
    return maxi

def create_adjencList(G):
    #graf dany za pomocą listy krawedzi przeksztalca do reprezentacji przez liste sąsiedztwa
    m = vertices_(G)
    G_res = [[]for _ in range(m)]
    for arr in G:
        G_res[arr[0]].append[arr[1]]
        G_res[arr[1]].append[arr[0]]
    return G_res

def is_path(G, x, y):
    G_adj = create_adjencList(G)
    # n = len(G_adj)
    q = deque()
    q.append(x)
    while q:
        u = q.popleft()
        for v in G_adj[u]:
            #krawedz pomiedzy u - v musze ja znalezc w tablicy G i jej wage
            pass
                 
        