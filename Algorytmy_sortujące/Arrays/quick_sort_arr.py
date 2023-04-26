from random import randrange

def quickSort(A, left, right):
    while left < right:
        pivot = partition(A, left, right)
        if (pivot-1) - left > right - (pivot+1):
            #lewa tablica jest większa zatem sortuje prawą tablice
            quickSort(A, pivot+1, right)
            right = pivot - 1
        else:
            quickSort(A, left, pivot-1)
            left = pivot + 1
            
def quickSort(A, r, l):
    while l < r:#UWAGA
        pivot = partition(A, r, l)
        quickSort(A,pivot - 1, l)
        # quick_sort(A,r,pivot + 1)
        l = pivot + 1
        
def quicksort(A, left, right):
    if left < right:
        pivot = partition(A, left, right)
        quicksort(A, left, pivot-1)
        quicksort(A, pivot+1, right)
        
        
def partition(A, left, right):
    x = A[right]
    i = left - 1 #na początku i jest przed tablicą bo nie przetworzyliśmy jeszcze elementów <= x
    for j in range(left, right):
        if A[j] <= x:
            i += 1
            A[j], A[i] = A[i], A[j]
    i += 1
    A[i], A[right] = A[right], A[i]
    return i


T =  [7, 9, 1, 5, 8, 6, 2, 12]
k =  4
p =  5
n = len(T)
print(partition(T, 0, n-1))
print(T)
A = [randrange(0, 100) for _ in range(20)]
print(A)
quicksort(A, 0, 19)
print(A)