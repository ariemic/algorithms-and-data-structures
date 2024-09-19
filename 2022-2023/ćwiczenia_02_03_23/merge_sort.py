
A = [1, 8, 2, 5, 4, 3, 7, 9]

def merge_sorted(A, B):
    n, m = len(A), len(B)
    i, j, k = 0, 0, 0
    T = [0]*(n+m)
    while i < n and j < m:
        if A[i] < B[j]:
            T[k] = A[i]
            i += 1
        else:
            T[k] = B[j]
            j += 1
        k += 1
    while i < n:
        T[k] = A[i]
        i += 1
        k += 1
    while j < m:
        T[k] = B[j]
        j += 1
        k += 1
    return T

print(merge_sorted([1, 4, 5, 6], [3, 5, 10]))
def mergeSort(A):
    n = len(A)
    if n > 1: 
        mid = n // 2
        L = A[:mid]
        R = A[mid:]
        nl, nr = len(L), len(R)
        sort_L = mergeSort(L)
        sort_R = mergeSort(R)
        #idzie dalej jeżeli tablica ma 1 element
        i, j, k = 0, 0, 0 
        #i, j - wskaźniki na lewą i prawą stronę listy
        while i < nl and j < nr:
            if sort_L[i] <= sort_R[j]:
                A[k] = sort_L[i]
                i += 1
            else:
                A[k] = sort_R[j]
                j += 1
            k += 1
        while i < nl:
            A[k] = sort_L[i]
            i += 1
            k += 1
        while j < nr:
            A[k] = sort_R[j]
            j += 1
            k += 1
    return A

print(mergeSort(A))
            