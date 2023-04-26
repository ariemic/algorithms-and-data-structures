from random import randint, choice

def partition(A, r, l):
    y = randint(l, r)    
    A[y], A[r] = A[r], A[y]
    x = A[r]
    i =  l - 1
    for j in range(l, r):#UWAGA NA RANGE
        if A[j] <= x:
            i += 1
            A[j], A[i] = A[i], A[j]
    i += 1
    A[i], A[r] = A[r], A[i]
    return i


def quick_sort(A, r, l):
       
    while l < r:#UWAGA
        pivot = partition(A, r, l)
        quick_sort(A,pivot - 1, l)
        # quick_sort(A,r,pivot + 1)
        l = pivot + 1
        
A = [randint(1, 120)for _ in range(20)]
print(A)
quick_sort(A, 19, 0)
print(A)
