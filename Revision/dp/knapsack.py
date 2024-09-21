"""
I = {0,.., n-1} - przedmioty
w - wagi przedmitów
p - ceny przedmitów
B - maksymalna waga (którą jest w stanie unieść złodziej) 

f(i, b) - maksymalna suma cen przedmiotów ze zbioru {0..i} których waga nie przekracza b
Wynik: f(n-1, B)

1) nie bierzemy i-tego przedmiotu
2) bierzemy i-ty przedmiot (tylko jeśli jesteśmy w stanie go zmieśći b - w(i) >= 0)
                1)            2)  
f(i, b) = max(f(i-1, b), f(i-1, b - w(i)) + p(i) )

f(0, b) = {
  p(0), w(0) <= b
  0,    w(0) > b
}
"""


def knapsack(Weights, Prices, MaxCapacity):
  n = len(Weights)

  F = [[0 for c in range(MaxCapacity + 1)] for i in range(n)]

  for c in range(Weights[0], MaxCapacity + 1):
    F[0][c] = Prices[0] 

  for c in range(MaxCapacity + 1):
    for i in range(1, n):
      F[i][c] = F[i-1][c] #patrzymy rząd wyżej są to wyniki wczesniej zabranych lub nie przedmitóœ

      if c - Weights[i] >= 0:#pomiescimy do plecaka wage i-tego przedmiotu
        #porównujemy co opłaca się bardziej to samo co wczesniej czy wziecie w tym wierszu rozwazanego przedmiotu i dopakowanie wolnego miejsca tym czym wczesniej sie najbardziej opłacało
        F[i][c] = max(F[i][c], F[i-1][c-Weights[i]] + Prices[i]) 

  return F[n-1][MaxCapacity]
  