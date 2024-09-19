import math
# w tym zadaniu nie ma znaczenia czy od której strony wjedziemy (od wsochodu czy zachodu) bo śniag topi się równomiernie
# pierwszy podpunkt czyli przejeżdzaie śniegu jest dla picu, nigdy tego nie zrobimy bo po prostu nam sie to nie opłaca
# i teraz najwazniejsze jesli posortujemy tą tablice np. [56, 23, 12, 3, 3, 2] to jesli zaczniemy zbierać od najwiekszych wartosci to po 3 dniach od prawej strony bedą tylko 0 bo snieg 
# stopiniał a czy wezmeimy 56, 23, 12 czy 23, 12, 56 to nie ma znaczenie zawsze wjezdzamy od ktorej stronyi bierzemy maxa reszta sama stopnienieje zanim tam dojedziemy

from zad2testy import runtests

def left(i):
    return 2*i + 1

def right(i):
    return 2*i + 2

def parent(i):
    return math.floor((i-1)/2)

# repair max heap
def heapify(A, n, i):
    l = left(i)
    r = right(i)
    max_ind = i
    if l < n and A[l] > A[max_ind]:
        max_ind = l
    if r < n and A[r] > A[max_ind]:
        max_ind = r
    if max_ind != i:
        A[i], A[max_ind] = A[max_ind], A[i]
        heapify(A, n, max_ind)
    

def buildheap(A):
    n = len(A)
    for i in range(parent(n-1), -1, -1):
        heapify(A, n, i)

def snow( S ):
    n = len(S)
    buildheap(S)
    
        



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = False )
