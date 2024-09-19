from zad3testy import runtests
from math import floor

'''
BucketSort - co jest bejtem na to zadanie? Prawdopodobieństwo nie jest wgl potrzebne.
Mamy n-1 bucketów. ([1, 2) [2, 3), ... [n-1, n)]). Był maxa punktów za pominięcie prawdopodobieństwa.
Wkładamy liczby do jednego z bucketów i sortujemy bucketSortem. 
'''
# T = [6.1, 1.2, 1.5, 3.5, 4.5, 2.5, 3.9, 7.8]
# P = [(1,5, 0.75), (4, 8, 0.25)]

def InsertionSort(T):
    n = len(T)
    for i in range(1, n):
        for j in range(i):
            if T[i] < T[j]:
                T[i], T[j] = T[j], T[i]

 

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
        InsertionSort(bucket)
    i = 0
    for bucket in B:
        for x in bucket:
            T[i] = x
            i += 1
    return T

# def BucketSortStandard(T):
#     #w standarodowym bucket sorcie elementy są z przedziału [0, 1)
#     n = len(T)
#     buckets = [[]for _ in range(n)]
#     for i in range(n):
#         buck_idx = int(T[i]*n) #ze wzgl na standardowy przedział bucketSorta
#         buckets[buck_idx].append(T[i])
#     output = []
#     for i in range(n):
#         InsertionSort(buckets[i])
#         output.extend(buckets[i])
#     return output
    


def SortTab(T, P):
    #tablica P wgl nie jest potrzebna mogę wziąć standardowy zakres dla bucketSorta (0, 1) i będzie działać
    n = len(P)
    _from = P[0][0]
    _to = P[n-1][1]
    T = BucketSort(T, _from, _to) #jakikolwiek zakres wezme to działa -> wiec moge wziąc standardowy (0, 1]
    return T 

runtests( SortTab )