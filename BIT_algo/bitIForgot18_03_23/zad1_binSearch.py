'''
Dane sa dwa zbiory liczb, reprezentowane jako tablice rozmiarów m i n, 
gdzie m jest znacznie mniejsze od n. Zaproponuj algorytm, ktry sprawdzi, czy 
zbiory są rozłączne.
m < n
'''
from random import randint

def merge_sort(S):
    n = len(S)
    if n > 1:
        left = merge_sort(S[:n//2])
        right = merge_sort(S[n//2:])
        
        #merge
        nl, nr = len(left), len(right)
        i = j = k = 0
        while i < nl and j < nr:
            if left[i] <= right[j]:
                S[k] = left[i]
                i += 1
            else:
                S[k] = right[j]
                j += 1
            k +=1
        while i != nl:
            S[k] = left[i]
            i += 1
            k += 1;
        while j != nr:
            S[k] = right[j]
            j += 1
            k += 1
    return S


def binary_search(A, m, x):
    left = 0 
    right = m-1
    while right >= left:
        mid = (left+right)//2
        if A[mid] > x:
            right = mid-1
        elif A[mid] < x:
            left = mid+1
        else:
            return True
    return False

# print(binary_search(A, len(A), 25))

def are_dijointed_sets(A, B):
    m, n = len(A), len(B)
    A = merge_sort(A)
    for i in range(n):
        if binary_search(A, m, B[i]):
            return False
    return True

A = [15, 2, 24, 15, 12, 25]
B = [ 2, 4, 1, 1, 2, 9, 10, 21, 34]
print(are_dijointed_sets(A, B))