#3)Dany jest graf jako macierz sąsiedztwa. Czy istnieje cykl o długości 4?
#   a)O(v^4) -> sprawdzamy wszystkie czwórki wierchołków czy są połączone v 
#   b)O(v^3) -> 1) Rozważamy wszystkie pary wierzcholkow -> jesli x i y maja wspolnych dwoch sasiadow -> przechodzimy po macierzy sąsiedztwa/BFS dla każdego wierzchołka v

'''
Dany jest graf nieskierowany G zawierajacy n wierzchołków. Zaproponuj
algorytm, który stwierdza czy w G istnieje cykl składajacy sie z dokładnie 4 wierzchołków. Zakładamy, ze
graf reprezentowany jest przez macierz sasiedztwa A.


Cykl 4 istnieje jesli istnieją krawedzie pomiedzy 4 wierzchołkami takie ze majac wierzcholki [a, b, c, d]; 
a - b
|   |
c - d
zatem w macierzy szukam dwóch kolumn w ktorych dla sprawdzanych wierszy wystepuja 1-dynki (krawedzie)
'''
A = [[0, 1, 0, 0, 1], #G - graf nieskierowany z cyklem długości 4
     [1, 0, 1, 1, 1],
     [0, 1, 0, 1, 0], 
     [0, 1, 1, 0, 1],
     [1, 1, 0, 1, 0]]

def cykl_na4(G):
     n = len(G)
     for i in range(n-1):#row 1
          for j in range(i+1, n): #row 2
               cnt = 0
               for k in range(n): #columns
                    if G[i][k] == 1 and G[j][k] == 1:
                         cnt += 1
                    if cnt == 2: return True

