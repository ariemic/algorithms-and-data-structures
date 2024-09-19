def right(i):
    return 2*i+2

def left(i):
    return 2*i+1

def parent(i):
    return (i-1)//2

def heapify(A, i, n):
    l = left(i)
    r = right(i)
    max_ind = i
    if l < n and A[l] > A[max_ind]:
        max_ind = l
    if r < n and A[r] > A[max_ind]:
        max_ind = r
    if max_ind != i:
        A[max_ind], A[i] = A[i], A[max_ind]
        heapify(A, max_ind, n)
    return A

def buildheap(A):
    n = len(A)
    for i in range(parent(n-1), -1, -1): #i don't understand this line
        heapify(A, i, n)
        
#write heapsort
def heapsort(A):
    n = len(A)
    buildheap(A)
    for i in range(n-1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heapify(A, 0, i)#zawsze naprawiam kopiec od idx 0 z ktorego zamieniam element z ostatnim nieposortowanym
    return A
    
A = [ 2, 3, 23, 12, 11, 29, 10, 1, 1, 3]
print(heapsort(A))

    