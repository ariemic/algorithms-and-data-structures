def partition(A, left, right):
    '''
    function returns pivot's index for current array
    '''
    i = left - 1
    for j in range(left, right):
        if A[j] <= A[right]:
            i += 1
            A[j], A[i] = A[i], A[j]
    i += 1
    A[i], A[right] = A[right], A[i]
    return i  


def quickSort(A):
    '''
    bez rekurencji ogonowej - ważny krok w ograniczeniu zużycia pamięci
    '''
    def rek(A, left=0, right=len(A)-1):
        '''
        Najpier rekurencyjnie posortuje lewą od pivota część tablicy, następnie mój left będzie indeksem na prawo od pivota, 
        czyli tak jak normalnie zachowywałaby się rekurencja dla prawej części tablicy. While kończy się w momencie kiedy left przyjmnie wartość
        ostatniego indeksu tablicy (left = len(A)-1).
        '''
        while left < right:
            pivot = partition(A, left, right)
            rek(A, left, pivot-1)
            left = pivot+1
        return A
    return rek(A)

print(quickSort([2, 4, 2, 1, 9, 10, 23, 21]))

def quickSortMemory(A, left, right):
    '''
    Make partiotion always for the smaller array, that will save memory space 
    '''
    n = len(A)
    while left < right:
        pivot = partition(A, left, right)
        if (pivot-1) - left > right - (pivot+1):
            quickSortMemory(A, pivot+1, right)
            right = pivot-1
        else:
            quickSortMemory(A, left, pivot-1)
            left = pivot+1       
    return A
print(quickSortMemory([3, 5, 1, 90, 34, 12, 6, 3], 0, 7))

