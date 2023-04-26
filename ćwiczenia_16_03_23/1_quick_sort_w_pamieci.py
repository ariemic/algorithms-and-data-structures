def partition(A, l, r):
    
    x = A[r]
    i =  l - 1
    for j in range(l, r):#UWAGA NA RANGE
        if A[j] <= x:
            i += 1
            A[j], A[i] = A[i], A[j]
    i += 1
    A[i], A[r] = A[r], A[i]
    return i

def quickSortMemory(A, left, right):
    '''
    Robie zawsze partycjie i sortowanie dla mniejszej tablicy, przez co jest mniej wywołań rekurencyjnych, przez co zużywa mniej pamięci.
    Make partition always for the smaller array, that will save memory space 
    '''
    n = len(A)
    while left < right:
        pivot = partition(A, left, right)
        if (pivot-1) - left > right - (pivot+1):
            quickSortMemory(A, pivot+1, right)
            right = pivot-1
        else:
            quickSortMemory(A, left, pivot-1)
            left = pivot+1       
    return A
print(quickSortMemory([3, 5, 1, 90, 34, 12, 6, 3], 0, 7))



