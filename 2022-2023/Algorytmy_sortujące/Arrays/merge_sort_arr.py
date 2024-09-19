
def merge_sort(S):
    n = len(S)
    if n > 1:
        left = merge_sort(S[:n//2])
        right = merge_sort(S[n//2:])
        
        #merge
        nl, nr = len(left), len(right)
        i = j = k = 0
        while i < nl and j < nr:
            if left[i] <= right[j]:
                S[k] = left[i]
                i += 1
            else:
                S[k] = right[j]
                j += 1
            k +=1
        while i != nl:
            S[k] = left[i]
            i += 1
            k += 1;
        while j != nr:
            S[k] = right[j]
            j += 1
            k += 1
    return S

print(merge_sort([2, 3, 9, 2, 1, 10, 4]))



def merge(L, R, A):
    #A - original array from elments come from
    nl, nr = len(L), len(R)
    i = j = k = 0
    while i < nl and j < nr:
        if L[i] < R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
    while i != nl:
        A[k] = L[i]
        i += 1
        k += 1        
    while j != nr:
        A[k] = R[j]
        j += 1
        k += 1
    
def mergeSort(T):
    n = len(T)
    if n > 1:
        left = mergeSort(T[:n//2])
        right = mergeSort(T[n//2:])
        merge(left, right, T)
    return T