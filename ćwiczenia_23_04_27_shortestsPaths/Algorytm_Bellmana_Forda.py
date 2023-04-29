'''
Algorytm Bellmana-Forda z def. graf musi być skierowany
Najkrótsze ścieżki gdy dopuszczamy ujemne wagi
Złożoność: O(V*E)

1. Inicjalizacja
    for v { V:
        v.d = inf
        v.parent = None
    s.d = 0
    
2. Relaksacje
    for i in range(|V|-1):
        for (u, v) { E:
            Relax(u,v)
            
3. Weryfikacja
    czy dla każdego (u, v) { E:
        v.d <= u.d + w(u, v)?
        jeśli nie zachodzi przynajmniej dla jednego wierzchołka to mamy gdzieś ujemny cykl
        
Czemu kroki 1 + 2 dają dobry wynik, jeśli nie ma cykli o ujemnej wadze?
Każda iteracji relaksuje co najmniej jedną dalej krawędź najkrótszej ścieżki

Czemu kork 3 wykrywa ujemne cykle wtedy suma[i=0, k-1](vi, v(i+1) ) < 0
Zał: weryfikacja nie wykryła ujemnego cyklu to dla każdego i:
    vi.d <= v(i-1).d + w(v(i-1), vi)
    Po zsumowaniu tych nierówności:
    suma[i=1, k](vi.d) <= suma[i=1, k]( v(i-1).d + w( v(i-1), vi) )
        x                       x                       < 0        sprzeczność
        
'''