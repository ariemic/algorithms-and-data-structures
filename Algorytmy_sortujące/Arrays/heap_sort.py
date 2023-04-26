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
    max_ind = i
    if l < n and A[l] > A[max_ind]: 
        max_ind = l
    if r < n and A[r] > A[max_ind]:
        max_ind = r
    if max_ind != i:#jesli indeks z najw wartoscią jest rózny od indeksu korzenia do wymien je
        A[i], A[max_ind] = A[max_ind], A[i] #aktualizacja listy przy korzeniu
        heapify(A, max_ind, n)
    return A
    
    
def buildheap(A):
    '''
    budujemy coraz wieksze kopce na podstawie elementów z naszej tablicy
    '''
    n = len(A)
    for i in range(parent(n-1), -1, -1):
        heapify(A, i, n)
        
def heapsort(A):
    n = len(A)
    buildheap(A)
    print(A)
    for i in range(n-1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heapify(A, 0, i)
    


A = [2, 2, 5, 6, 3, 10, 11, 1, 2, 17]
print(heapsort(A))