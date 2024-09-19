'''
Algorytm zlicza liczbę inwersji w tablicy
'''
global cnt 
cnt = 0

def merge(L, R, A):
    global cnt
    #merge two sorted arrays and count number of inversion in merged array
    i = j = k = 0
    nl, nr = len(L), len(R)
    while i < nl and j < nr:
        if L[i] > R[j]:
            A[k] = L[i]
            cnt += nr - j
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
    while i != nl:
        #tu już nie będzie żadnych inwersji
        A[k] = L[i]
        i += 1
        k += 1        
    while j != nr:
        A[k] = R[j]
        j += 1
        k += 1
    return cnt
    
    

    
def mergeSort(A):
    #sortuje malejąco
    global cnt
    n = len(A)
    if n > 1:
        left = mergeSort(A[:n//2])
        right = mergeSort(A[n//2:])
        merge(left, right, A) #return cnt
    return A

T = [8,4,2,1]
print(mergeSort(T))
print(cnt)