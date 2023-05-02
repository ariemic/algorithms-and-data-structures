'''
Problem przewodnika turystycznego

visited na krawedz, robimy macierz sasiedztwa gdzie oznaczamy czy macierz zostala wykorzystana czy nie

1):
-bfs takie ze w kazdym wierz na biezaca trzymam info jaka jest minimalna waga kraw. na drodze do tego wierzcholka
-najelpiej miec macierz visited;  
-przechodzimy przez graf opytmalizujac sobie info tak zeby znalezc sciezke z minimalna wage na najoptymalniejszej sciezce - problem min(max)

2)
po kolei dodajemy do kolejki wierz w kolejności malejacych wag i w ktorym momencie m
Bierzemy wszystkie krawedzie i je sortujemy po pojemnosci autobusu na danej trasie, jedna po drugie dodawac kraw do do grafu dopoki
nie zacznie istniec ta sciezka (find union);

3) sprawdzamy czy istnieje krawedz z a do b;
Wyszukiwanie binarne:
-jesli mamy przewiezdz 100osob to zastanawiamy sie czy istnieje taka trasa zeby przewiezdz po 50 osob; wyrzucamy wszystkie trasy mniejsze niz 50;
dfs/bfs z dodatkowym if-em a wczesniej wyszukiwanie binarne -> zlozonosc O(logn*E)
'''

#70
#30 nie -> 15
#15 git
#10
#5


def max_vertex(Edges):
    return max(Edges[i][1] for i in range(len(Edges)))+1

def create_grapth(Edges):
    #w tym sposobie powstają parallel edges
    n = max_vertex(Edges)
    G = [[]*n]
    for edge in Edges:
        u, v, val = edge[0], edge[1], edge[2]
        G[u].append((v, val))
        G[v].append((u, val))
    return G

def guide_problem(Edges, A, B, K):
    pass



Edges = [(0, 1, 20),(0, 1, 30), (1, 4, 25), (0, 4, 10), (0, 2, 30), (2, 3, 21)]