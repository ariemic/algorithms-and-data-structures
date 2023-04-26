'''
Dana jest tablica liczb rzeczywistych wielkości n reprezentująca kopiec minimum
(array-based-heap). Mając daną liczbę rzeczywistą x, sprawdz, czy k-ty
najmniejszy element jest większy lub równy x.
'''

def right(i):
    return 2*i+2
def left(i):
    return 2*i-1
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
        heapify(max_ind)
    return A

def buildheap(A):
    n = len(A)
    for i in range(parent(n-1), -1, -1):
        pass
    
