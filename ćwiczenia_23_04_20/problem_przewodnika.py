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

sprawdzamy czy istnieje krawedz z a do b;
Wyszukiwanie binarne:
-jesli mamy przewiezdz 100osob to zastanawiamy sie czy istnieje taka trasa zeby przewiezdz po 50 osob; wyrzucamy wszystkie trasy mniejsze niz 50;
dfa/bfs z dodatkowym if-em a wczesniej wyszukiwanie binarne -> zlozonosc O(logn*E)
'''