'''
Dane sa dwa zbiory liczb, reprezentowane jako tablice rozmiarów m i n, 
gdzie m jest znacznie mniejsze od n. Zaproponuj algorytm, ktry sprawdzi, czy 
zbiory są rozłączne.
m < n
'''
def partition(A, left, right):
    x = A[right]
    i = left - 1
    for j in range(left, right):
        if A[j] <= x:
            i += 1
            A[j], A[i] = A[i], A[j]
    i += 1
    A[i], A[right] = A[right], A[i]
    return i

def quick_sort(A, left, right):
    if left < right:
        pivot = partition(A, left, right)
        quick_sort(A, left, pivot-1)
        quick_sort(A, pivot +1, right)
    return A

def czy_rozlaczne(A, B):
    m, n = len(A), len(B)
    A, B = quick_sort(A,0,m-1), quick_sort(B, 0, n-1)
    i = 0; j = 0
    while i < m and j < n:
        if A[i] < B[j]:
            i += 1
        elif A[i] > B[j]:
            j += 1
        else:
            return False
    return True

A = [1, 3, 5, 12, 122]    
B = [13, 4, 8, 8, 8, 8, 500]
print(czy_rozlaczne(A, B))