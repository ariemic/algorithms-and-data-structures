def partition(A, left, right):
    '''
    function returns pivot's index for current array
    '''
    i = left - 1
    for j in range(left, right):
        if A[j] <= A[right]:
            i += 1
            A[i], A[j] = A[j], A[i]
    i += 1
    A[right], A[i] = A[i], A[right]
    return i    

def quickSort(A, left, right):
    if left < right: #works recursively so there is no need for while loop
        pivot = partition(A, left, right)
        quickSort(A, left, pivot-1)
        quickSort(A, pivot+1, right)
    return A

print(quickSort([2, 4, 2, 1, 9, 10, 23, 21], 0, 7))