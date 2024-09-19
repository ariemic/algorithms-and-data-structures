# np. liczba liter - zwraca najdl. spojnego slowa bedacego palindromeme
# mamy dwóch biegaczy to znaczy: patrzymy na pierwszą litere w słowie i szukamy jej powtórzenia jeśli je znajdziemy do porównujemy wewętrzne litery czy są takie same do błedu, jesli to nie jest palidrom to szukamy kolejnego powtórzenia lietery i robimy tak samo aż to ostatniej litery słowie robimy tak dla każdej litery i zapisujemy max np. palidrom i porównujemy z nim jesli znajdziemy nowe rozwiązanie
# złożoność: O(n^2)
from zad1testy import runtests

def ceasar( s ):
  maxi = 0
  n = len(s)
  for i in range(n):
    for j in range(n-1, i, -1):
      start, end = i, j
      loc_max = 0
      
      while s[start] == s[end] and start < end:
          loc_max += 2
          start += 1
          end -= 1
      if( start == end): loc_max += 1
      if loc_max % 2 == 1:
         maxi = max(loc_max, maxi)
        #  we can exit here because the longest palindrome has been found starting at s[i]
         break
      
  return maxi
        
        
# s = "akontnoknonabcddcba"
# print(ceasar(s))

# # zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ceasar , all_tests = False )
