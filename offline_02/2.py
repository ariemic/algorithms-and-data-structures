def merge_sort(S): #posortuj malejąco
    n = len(S)
    if n > 1:
        left = merge_sort(S[:n//2])
        right = merge_sort(S[n//2:])
        #merge
        nr, nl = len(right), len(left)
        i = j = k = 0
        while i < nl and j < nr:
            if left[i] >= right[j]:
                S[k] = left[i]
                i += 1 
            else:
                S[k] = right[j]
                j += 1
            k += 1
        while i < nl:
            S[k] = left[i]
            i += 1
            k += 1
        while j < nr:
            S[k] = right[j]
            j += 1
            k += 1
    return S
def snow( S ):
    S = merge_sort(S)
    #index w tablicy wskazuje na numer dnia zbierania
    d, suma = 0, 0
    while S[d] - d > 0:
        suma += (S[d] - d)
        d += 1
    return suma
