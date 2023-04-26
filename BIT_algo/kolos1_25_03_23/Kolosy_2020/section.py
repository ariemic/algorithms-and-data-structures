
'''

quick select dla pivot = p, bez istotnosci kolejności po quick selectcie.
Oraz drugi quick select dla pivot = q, od początku do indeksu q tablicy czyli tylko < T[q].
Dostaniemy liczby z przedziału [p:q+1]. 
Quick Select - wywoływanie quicksorta tylko na połówce, która nas interesuje.
'''
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

# def quickSelect(A, i):
#     n = len(A)
#     left, right = 0, n-1
#     pivot = partition(A, left, right)
#     while pivot != i:
#         if pivot < i:
#             left = pivot+1
#         else:
#             right = pivot-1
#         pivot = partition(A, left, right)
        
def quickSelect(T, p, left, right):
    #
    if right >= left:
        pivot = partition(T, left, right)
        if pivot == p: return pivot 
        elif pivot < p: return quickSelect(T, p, pivot + 1, right)
        else: return quickSelect(T, p, left, pivot - 1)
        
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

# T = [43, 74, 53, 61, 97, 80, 61, 19, 61, 73, 89, 93, 42, 17, 89, 80]
# # T2 = [17, 19, 43, 42, 53, 61, 80, 61, 73, 74, 61, 80, 89, 89, 93, 97]
# T1 = [43, 53, 17, 19, 42, 61, 61, 61, 73, 74, 80, 93, 97, 80, 89, 89]
# n = len(T1)
# # T2 = [43, 17, 19, 42, 53, 61, 61, 61, 73, 74, 80, 80, 89, 93, 89, 97]
# quickSelect(T1, 7, 0, n-1)
# print(T1)
def section(T, p, q):
    n = len(T)
    #pivot indicates the index when T[p] will end up and divide array into group of elements  <= T[p] and elements > T[p] without sorting array

    # pivot = partition(T, 0, n-1)
    quickSelect(T, p, 0, n-1)
    quickSelect(T, q, p, n-1)
    #alternatywa
    # while pivot != p:
    #     if pivot < p:
    #         pivot = partition(T, pivot+1, n-1)
    #     else: pivot = partition(T, 0, pivot-1)
    # while pivot != q:
    #     if pivot < q:
    #         pivot = partition(T, pivot+1, n-1)
    #     else: pivot = partition(T, p, pivot-1)
    return T[p:q+1]

[95, 121, 144, 144, 156, 192]
T = [144,156,121,95,329,144,348294,192,65,49,79,69,213,731]

print(section(T, 4, 9))

    
        
        

        