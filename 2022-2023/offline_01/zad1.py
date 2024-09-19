
'''
Ariel Michalik
Złożoność czasowa: O(n^2)

Algorytm sprawdza od najkrótszego wewnętrznego słowa zaczynając od takiego którego środkowa litera jest na indeksie 1 czy jest to palindrom, jeśli tak to inkrementuje r sprawdzając czy możliwe jest 
utworzenie palindromu z sprawdzonym wcześniej wewnątrz, jeżeli nie wychodzimy poza tablice z jednej lub drugiej strony to sprawdzamy czy litery z prawej i lewej strony naszego wewnętrznego palindromu
są takie same jeśli tak do dalej inkrementujemy r i szukamy jeszcze większego palindromu zewnętrznego, jeżeli nie to wychodzimy z pętli while i zaczynamy szukanie palindromu od kolejnego indeksu 
stanowiącego punkt centralny. Zmienna leng przetrzymuje długość znalezionego palindromu, korzystając z faktu jest to 2*r(promień słowa) + 1 przez co rozpatrujemy tylko palindromy o długości nieparzystej.
Funkcja zwraca znalezioną długość palindromu lub 0 jeżeli parament podany na wejściu jest pustym stringiem.
 
'''
from zad1testy import runtests

def ceasar(s):
    n = len(s)
    if n < 1: return 0
    maxi = 1
    for m in range(n):
        r = 1
        while m - r >= 0 and m + r < n:
            if s[m-r] != s[m+r]:
                break
            r += 1
        leng = 2*(r-1) + 1 
        maxi = max(maxi, leng)
    return maxi


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ceasar , all_tests = True )
