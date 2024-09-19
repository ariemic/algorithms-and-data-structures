
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
    return (i-1)//2

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
    # repair all heaps from the bottom unitl it build one big heap
    for i in range(parent(n-1), -1, -1):
        heapify(A, n, i)

def heapsort(A):
    n = len(A)
    buildheap(A)
    for i in range(n-1, 0, -1):
        A[0], A[i] = A[i], A[0]
        # repair only main veretex of the heap
        heapify(A, i , 0)


def snow( S ):
    n = len(S)
    buildheap(S)
    suma = d = 0
    i = n - 1
    while i > 0 and S[0] - d > 0:
        suma = suma + S[0] - d
        d += 1
        S[0], S[i] = S[i], S[0]
        heapify(S, i, 0)
        i -= 1
    return suma


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = False )
