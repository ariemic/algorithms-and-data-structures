from random import random

def insertionSort(A):
    n = len(A)
    for i in range(1, n):
        for j in range(i):
            if A[i] < A[j]:
                A[i], A[j] = A[j], A[i]
    return A

def bubbleSort(A):
    n = len(A)
    for i in range(n-1):
        for j in range(i, n):
            if A[i] > A[j]:
                A[i], A[j] = A[j], A[i]
    return A
A = [23, 52, 121, 122, 11, 2, 12, 4]
# print(insertionSort(A))
print(bubbleSort(A))


def BucketSort(T):
    #dla liczb z przedziału od [0, 1)
    n = len(T)
    B = [[]for _ in range(n)] #create buckets for numbers 
    for i in range(n):
        buck_ind = int(n*T[i]) #int round down
        B[buck_ind].append(T[i]) #put number into suitable bucket
    i = 0
    for bucket in B:
        insertionSort(bucket)
        for x in bucket:
            T[i] = x
            i += 1
    

T = [random() for _ in range(20)]
print(T)
print(BucketSort(T))
        
def BucketSort(T,_from, _to):
    n = len(T)
    bucket_width = (_to - _from )/n #okresle szerokosc kosza - liczby z jakiego przedziału sie w nim zmieszcza
    #create buckets
    B = [[]for _ in range(n)]
    for x in T:
        buck_idx = min(n-1, floor(x / bucket_width))
        B[buck_idx].append(x)
    for bucket in B:
        #sort elements in the interior buckets
        insertionSort(bucket)
    i = 0
    for bucket in B:
        for x in bucket:
            T[i] = x
            i += 1
    return T
