#znajdz k-ty co do wielkości element w liście
from random import randint

def partition(A, left, right):
    x = randint(left, right)
    i = left - 1
    A[x], A[right] = A[right], A[x]
    for j in range(left, right):
        if A[j] < A[right]:
            i += 1
            A[j], A[i] = A[i], A[j]
    A[i], A[right] = A[right], A[i]
    return i

def quickSelect(T, p, left, right):

    if right >= left:
        pivot = partition(T, left, right)
        if pivot == p: return pivot 
        elif pivot < p: return quickSelect(T, p, pivot + 1, right)
        else: return quickSelect(T, p, left, pivot - 1)

def find_Kth(A, k):
    n = len(A)
    quickSelect(A, k-1, 0, n-1)
    return A[k-1]

T = [2,4,1,3,5,7,9,6,8]
n = len(T)
print(find_Kth(T, 7))