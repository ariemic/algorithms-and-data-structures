'''
Ruchoma ramka odczytu
Tworze kopie tablicy o potrzebnej długości p, sortuje ją quicksortem. Już więcej nie będę tworzyć kopii, podczas przesuwania okna odczytu (dl p), będę usuwać pierwszy element
nieposortowanaej tablicy korzystając z funkcji remove(value) na posortowanej kopii tablicy. Wstawiam do kopii kolejny element W ODPOWIEDNIE MIEJSCE z tablicy T tak aby 
długość okna pozostała p. Tym sposobem zawsze na k-1 tym indeksie mam k-ty element, którego wartość będę dodawać do sumy aż dojdę do ostatniego elementu tablicy T.
'''

from random import randint

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

def quickSort(T, left, right):
    if left < right:
        pivot = partition(T, left, right)
        quickSort(T, left, pivot-1)
        quickSort(T, pivot+1, right)

def findPlace(A, val):
    '''
    Korzystam z binary searcha aby znaleźć miejsce w które musze wstawić daną wartość
    Tablica jest uporządkowana malejąco
    
    nie dziala dla wstawiania elementu na koniec listy, najmniejszego
    '''
    left, right = 0, len(A)-1
    while left <= right:
        mid = (left+right)//2
        if A[mid] == val:
            return mid
        elif A[mid] > val: left = mid+1
        else: right = mid-1
    return mid
    
            
    

T = [11, 10, 5, 4, 3, 2, 1]
T.insert(findPlace(T, 0), 0)
print(T)

def ksum(T, k, p):
    T_copy = T[:p]
    quickSort(T_copy, 0, p-1)
    n = len(T)
    suma = 0
    for i in range(n-p+1):
        suma += T_copy[k-1]
        T_copy.remove(T[i])
        idx = findPlace(T_copy, T[i+p-1])
        T_copy.insert(idx, T[i+p-1])
        print(T_copy)
    return suma

# T =  [7, 9, 1, 5, 8, 6, 2, 12]
# k =  4
# p =  5
# print(ksum(T, k, p))