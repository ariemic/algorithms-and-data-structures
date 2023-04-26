'''
Ariel Michalik
Złożoność czasowa: O(N + nlogn)
Algorytm porównuje każde słowo z zadanej tablicy ze swoją odwrotnością, następnie wybiera mniejszy leksykograficznie odpowiednik (dzięki temu w tablicy napisy, które są równoważne będą wyglądać tak samo).
Następnie sortuje zmienioną tablce, według kolejności leksykograficznej napisów, używając quicksorta. Po tym zabiegu te same napisy będą obok siebie, zliczam ile jest takich samych napisów w tablicy,
jeżeli jakiś ma moc >= połowy pozostałych napisów to kończe szukanie i zwracam zmienną maxi, bo nie znajdę już nic większego. 
'''
from zad3testy import runtests
from random import randint
from math import floor

def partition(A, left, right):
    x = randint(left, right)
    A[x], A[right] = A[right], A[x]
    i = left - 1
    for j in range(left, right):
        if A[j] <= A[right]:
            i += 1
            A[j], A[i] = A[i], A[j]
    i += 1
    A[i], A[right] = A[right], A[i]
    return i

def quickSort(A, left, right):
    while left < right:
        pivot = partition(A, left, right)
        if (pivot-1) - left > right - (pivot+1):
            quickSort(A, pivot+1, right)
            right = pivot - 1
        else:
            quickSort(A, left, pivot-1)
            left = pivot + 1

def strong_string(T):
    n = len(T) 
    for i in range(n):
        if T[i] > T[i][::-1]:
            T[i] = T[i][::-1]
    quickSort(T, 0, n-1)  
    i = maxi =  0
    while i < n:
        j, cnt = i+1, 1 
        while j < n and T[i] == T[j]:
            cnt += 1
            j += 1
        maxi = max(cnt, maxi)
        if maxi >= n//2 + 1: return maxi
        i = j
    return maxi


# #2sposob    
# def merge_sort(S):
#     n = len(S)
#     if n > 1:
#         left = merge_sort(S[:n//2])
#         right = merge_sort(S[n//2:])
        
#         #merge
#         nl, nr = len(left), len(right)
#         i = j = k = 0
#         while i < nl and j < nr:
#             if left[i] <= right[j]:
#                 S[k] = left[i]
#                 i += 1
#             else:
#                 S[k] = right[j]
#                 j += 1
#             k +=1
#         while i != nl:
#             S[k] = left[i]
#             i += 1
#             k += 1;
#         while j != nr:
#             S[k] = right[j]
#             j += 1
#             k += 1
#     return S
    

# def Buckets(T):
#     #dla liczb z przedziału od [0, 1)
#     n = len(T)
#     B = [[]for _ in range(n)] #create buckets for numbers # tu jest problem jeśli chodzi o długość napisu
#     for i in range(n):
#         buck_ind = min(n-1, floor(len(T[i])/n)) #indeksem kosza będzie długość napisu
#         B[buck_ind].append(T[i]) #put number into suitable bucket
#     maxi = 0
#     for bucket in B:
#         merge_sort(bucket)
#         k = len(bucket)
#         i =  0
#         j = 1
#         while j < k:
#             cnt = 0
#             while j < k and bucket[i] == bucket[j]: 
#                 j += 1
#                 cnt += 1
#             maxi = max(cnt, maxi)
#             i = j
#             j += 1
#     return maxi+1
    
# def strong_string(T):
#     n = len(T)
#     for i in range(n):
#         if T[i] > T[i][::-1]:
#             T[i] = T[i][::-1]
#         #wypieram zawsze opcje mniejszą leksykograficznie
#     maxi = Buckets(T)
#     return maxi

# # zmien all_tests na True zeby uruchomic wszystkie testy
runtests( strong_string, all_tests=True )
