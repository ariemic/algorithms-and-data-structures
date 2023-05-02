'''
Zadanie 6. (dwóch kierowców) Dana jest mapa kraju w postaci grafu G = (V,E), gdzie wierzchołki to
miasta a krawedzie to drogi łaczace miasta. Dla kazdej drogi znana jest jej długosc (wyrazona w kilometrach
1
jako liczba naturalna). Alicja i Bob prowadza (na zmiane) autobus z miasta x > V do miasta y > V , zamieniajac
sie za kierownica w kazdym kolejnym miescie. Alicja wybiera trase oraz decyduje, kto prowadzi pierwszy.
Prosze zapropnowac algorytm, który wskazuje taka trase (oraz osobe, która ma prowadzic pierwsza), zeby
Alicja przejechała jak najmniej kilometrów. Algorytm powinien byc jak najszybszy (ale przede wszystkim
poprawny).

Dla każdego miasta mamy dwie opcje: albo wyjedzie z niego Alice albo Bob;
rozmnażam wiercholki dla każdego miasta bede mieć 2, tak samo rozmnażam krawedzie z podziałem wag np mam kraw o wadze 57; przypisuje alice 
kraw z wag a 57 i bobowi kraw z wagą 0. Musi tak być, aby te krawedzie wystepowały na zmiane. Krawedzie powinny być skierowane.
Wyszukuje najkrotsza sciezke pomiedzy dwoma wierzchołkami lub 

Poprzez przeopbienie grafu na dizwne krawedzie jestsmy w stanie uzyc standardowego algorytmy wyszikwania najkrotszej sciezki.
np. dijkstra + w kolejce zapamieteju (liczba przejechanych km, wierzchołek, A) A - alice dojechała lub B - Bob dojechał
'''