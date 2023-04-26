from kol1testy import runtests
from random import randint
#ZALICZA 4 TESTY -> 3.5PKT

def partition(T, left, right):
    #przestawia elementy na wieksze za pivotem i mniejsze przed nim, nie sortuje
    #zwraca indeks na którym znajduje się pivot
    x = randint(left, right)
    T[right], T[x] = T[x], T[right]
    i = left-1
    for j in range(left, right):
        if T[j] >= T[right]:
            i += 1
            T[i], T[j] = T[j], T[i]
    i += 1
    T[right], T[i] = T[i], T[right]
    return i

            
def quickSelect(T, left, right, k):
    #ma zwrócić tablice z pivotem na k-1 indeksie, -1 ponieważ iterujemy od 0
    while left <= right:
        pivot = partition(T, left, right)
        if pivot == k: return T[pivot]
        elif pivot > k: right = pivot-1
        else: left = pivot+1


def ksum(T, k, p):
    n, suma = len(T), 0
    for i in range(n-p+1):
        #mamy przedział długości p w którym szukamy k-tego najwiekszego elementu; 
        copy_T = T[i:i+p] #przeszukujemy obszar o długości p, zatem slicing od 0 do p+i-1 włącznie aby sumowało się do p elementów
        nc = len(copy_T)
        suma += quickSelect(copy_T, 0, nc-1, k-1)
    return suma   

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=True)
