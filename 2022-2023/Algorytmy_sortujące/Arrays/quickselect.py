from random import randint
#sortujemy malejąco - interesują nas liczby w tablicy na pozycji od p do q włącznie
def partition(A, left, right):
    x = randint(left, right)
    i = left - 1
    A[x], A[right] = A[right], A[x]
    for j in range(left, right):
        if A[j] < A[right]:
            i += 1
            A[j], A[i] = A[i], A[j]
    i += 1
    A[i], A[right] = A[right], A[i]
    return i
    
    
def quickSelect(A, i, left, right):
    n = len(A)
    # left, right = 0, n-1
    pivot = partition(A, left, right)
    while pivot != i:
        if pivot < i:
            left = pivot+1
        else:
            right = pivot-1
        pivot = partition(A, left, right)
        
def quickSelect(T, p, left, right):
    #
    if right >= left:
        pivot = partition(T, left, right)
        if pivot == p: return pivot 
        elif pivot < p: return quickSelect(T, p, pivot + 1, right)
        else: return quickSelect(T, p, left, pivot - 1)

