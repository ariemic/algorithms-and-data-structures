'''
tablica k-chaotyczna
znaleźć algo który sortuje tą tablice w czasie klog(k) - każdy element jest oddalony od swojego miejsca o conajwyżej k miejsc

https://www.geeksforgeeks.org/nearly-sorted-algorithm/

'''

def left(i):
    return 2*i + 1
def right(i):
    return 2*i + 2
def parent(i):
    return (i-1)//2

def heapify(A, i, n):
    '''
    naprawianie kopca od korzenia, i - indeks elementu który wskazuje na korzeń
    '''
    l = left(i)
    r = right(i)
    min_ind = i
    if l < n and A[l] < A[min_ind]: 
        min_ind = l
    if r < n and A[r] < A[min_ind]:
        min_ind = r
    if min_ind != i:#jesli indeks z najw wartoscią jest rózny od indeksu korzenia do wymien je
        A[i], A[min_ind] = A[min_ind], A[i] #aktualizacja listy przy korzeniu
        heapify(A, min_ind, n)
    return A
    
    
def buildheap(A):
    '''
    budujemy coraz wieksze kopce na podstawie elementów z naszej tablicy
    '''
    n = len(A)
    for i in range(parent(n-1), -1, -1):
        heapify(A, i, n)

def SortKChaotic(T, k):
    n = len(T)
    T_heap = T[0:k+1] #musze tworzyć kopiec o wielkość k+1
    buildheap(T_heap)
    for i in range(n):
        if i+k+1 < n:
            T[i] = T_heap[0]
            T_heap[0] = T[i+k+1] #dodaje kolejny element na góre na kopca
            heapify(T_heap, 0, k+1)#k+1 bo to jest wielkość kopca
        else:
            #wyszlismy poza tablice indeksem k+i
            T[i] = T_heap[0]
            T_heap[0], T_heap[-1] = T_heap[-1], T_heap[0]
            T_heap.pop()
            heapify(T_heap, 0, len(T_heap))            
    return T

T = [1,0,3,2,4,6,5]
print(SortKChaotic(T, 1))