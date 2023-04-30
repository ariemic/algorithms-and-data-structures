'''
Zadanie 7. (kosztowna szachownica) Dana jest szachownica o wymiarach n x n. Kazde pole (i, j)
ma koszt (liczbe ze zbioru {1, . . . , 5}) umieszczony w tablicy A (na polu A[j][i]). W lewym górnym rogu
szachownicy stoi król, którego zadaniem jest przejsc do prawego dolnego rogu, przechodzac po polach o
minmalnym sumarycznym koszcie. Prosze zaimplementowac funkcje kings path(A), która oblicza koszt
sciezki króla. Funkcja powinna byc mozliwie jak najszybsza

Robie implementacje dijkstry dla macierzy sąsiedztwa
'''

from queue import PriorityQueue

def relax(u, v, edge_weight, d, parent):
    if d[v] > d[u] + edge_weight:
        d[v] = d[u] + edge_weight
        parent[v] = u
        return True
    return False


        
   

def kings_path(A):
    pass
