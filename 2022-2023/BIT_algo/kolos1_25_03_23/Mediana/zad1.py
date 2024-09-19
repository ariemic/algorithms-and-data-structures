from zad1testy import runtests
# T = [[2, 3, 5], [7, 13, 15], [17, 19,23]]

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
            

        
def quickSort(A, left, right):
    if left < right:
        pivot = partition(A, left, right)
        quickSort(A, left, pivot-1)
        quickSort(A, pivot+1, right)
    

def Median(T):
    n = len(T)
    A = [T[i][j] for i in range(n) for j in range(len(T[i]))]
    # print(A)
    p, q = (n**2 - n)//2, (n**2 + n)//2-1
    quickSelect(A, q, 0, len(A)-1)
    quickSelect(A, p, 0, q)
    i, j, k = 0, p, q+1
    print(i, j, k)
    output = [[0 for _ in range(n)] for _ in range(n)]
    for y in range(n):
        for x in range(n):
            if x < y:
                output[y][x] = A[i]
                i +=1
            elif y == x:
                output[y][x] = A[j]
                j += 1
            else:
                output[y][x] = A[k]
                k += 1
    for i in range(n):
        print(output[i])    
    return output
    #tworze tablice wewnetrze w które będę wkładać po n elementów
  
    
runtests( Median ) 
