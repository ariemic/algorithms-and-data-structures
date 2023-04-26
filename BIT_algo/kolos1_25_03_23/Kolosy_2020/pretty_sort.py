''''
Counting sort najepierw rosnąco po czasach wielokrotnych, potem malejąco pojednokorotnych.
Tworze tablice zawierającą krotki (liczba, wielokrotne, jednokrotne).

Poćwiczyć funkcje sortujące dla konkretnych indeksów. Wydrukować i wziąć na 
kolokwium przydatne funkcje na kolosa. 
Mam 3 krotki, chcę posortować po 2 indeksie krotek.

Stabilne sortowania: heapsort, mergesort, countsort
Niestabline: Quicksort
'''

def turn_into_tuples(T):
    n = len(T)
    for i in range(n):
        num = T[i]
        numm = num
        A = [0]*10
        while num != 0:
            A[num%10] += 1
            num = num//10
        wielo, jedno = 0, 0 
        for j in range(10):
            if A[j] > 1: 
                wielo += 1
            if A[j] == 1:
                jedno += 1
        T[i] = (numm, wielo, jedno)
    return T


def CountSortIdx(T, i, r):
    #narazie sortuje rosnąco
    n = len(T)
    A = [0]*n
    B = [0]*10
    for j in range(n):
        B[T[j][i]] += 1
    if r == True:#malejąco
        for j in range(8, -1, -1):
            B[j] = B[j+1] + B[j]
    else:#rosnaco
        for j in range(1,10):
            B[j] = B[j-1]+B[j]
    for j in range(n-1, -1, -1):
        A[B[T[j][i]]-1] = T[j] #zwraca tablice z tuplami żeby zwracało tablice z samymi wartościami to przypisz T[j][0]
        B[T[j][i]] -= 1 
    return A


def pretty_sort(T):
    n = len(T)
    T = turn_into_tuples(T)
    T = CountSortIdx(T, 1, False)
    T = CountSortIdx(T, 2, True)
    return T
    
T = [123, 445, 28, 22, 4456]
print(pretty_sort(T))