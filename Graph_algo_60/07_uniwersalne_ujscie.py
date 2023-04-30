'''
Zadanie 2. (uniwersalne ujscie) Mówimy, ze wierzchołek t w grafie skierowanym jest uniwersalnym
ujsciem, jesli 
(a) z kazdego innego wierzchołka v istnieje krawedz z v do t, oraz 
(b) nie istnieje zadna krawedz wychodzaca z t.

1. Podac algorytm znajdujacy uniwersalne ujscie (jesli istnieje) przy reprezentacji macierzowej (O(n2)).
2. Pokazac, ze ten problem mozna rozwiazac w czasie O(n) w reprezentacji macierzowej.


Jedziemy przez macierz, mamy wspolrzedne i, j, zaczynamy od lewego gornego rogu. Idziemy w prawo dopoki
sa zera. Jesli doszlismy do 1, to wtedy idziemy w dol i sprwadzamy, czy mozemy znowu isc w prawo ( patrzymy 
czy sa zera ). Czyli schodzimy w dol dopoki nie ma zera po prawej stronie. JEsli jest to idziemy w prawo. Postepujem
tak dopoki nie dojdziemy do prawej sciany. Jak doszlismy do sciany sprawdzamy czy dany wiersz nie jest
tym czego szukamy. Sprawdzamy ten wiersz i kolumne (jesli doszlismy od scainy w 5 indeksie, to sprawdzamy
piaty wiersz i piate kolumne). Jesli pasuje to znalezlizmy, jesli nie, to znaczy
ze nie istnieje. Czy i dlaczego mozemy byc pewni, ze go nie przegapimy? 
Jest tak, bo jesi idizemy w dol to jest tylko jedna dziura, ktora przepusci nas w prawo do sciany,
jesli takiej nie znajdziemy, to nie ma takiego ujscia. 

'''
G = [[0, 0, 1, 1], #source - 3
     [1, 0, 0, 1], 
     [0, 0, 0, 1], 
     [0, 0, 0, 0]]


def find_source(G):
    #O(n^2)
    n = len(G)
    arr = [0]*n
    for i in range(n):
        if G[i] == arr: #dany wiersz ma same zera
            cnt = 0
            for j in range(n):
                if i != j and G[j][i] == 1:
                    cnt += 1
            if cnt == n-1: return i
    return None

def find_source_linear(G):
    #O(n) 
    n = len(G)
    i, j = 0, 1
    while j != n and i != n:
        if G[i][j] == 0:
            j += 1
        else:
            i += 1
    return i if G[i] == [0]*n else None

print(find_source(G))
            

