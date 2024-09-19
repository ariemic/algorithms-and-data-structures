'''
Sortowanie stabline - najlepiej mergeSort.
Tworze tablice tupli gdzie tupla to (liczba, początkowy indeks liczby). 
Następnie robie sorta stabilnego po pierwszym indeksie tupli.
Dalej ile wartość bezwlędną z indeksów początkowych i po posortowaniu z każdej tupli. Moje maximum będzie
równe k.

'''

def into_tuples(T):
    n = len(T)
    for i in range(n):
        T[i] = (T[i], i)
    return T
    
    
def merge(L, R, A, idx):
    #A - original array from elments come from
    nl, nr = len(L), len(R)
    i = j = k = 0
    while i < nl and j < nr:
        if L[i][idx] < R[j][idx]:
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
    
def mergeSort(T, idx):
    n = len(T)
    if n > 1:
        left = mergeSort(T[:n//2], idx)
        right = mergeSort(T[n//2:], idx)
        merge(left, right, T, idx)
    return T
        
# T = [23, 512 ,12, 11, 4, 1, 2, 67, 13, 12, 89]
# print(mergeSort(T))

def chaos_index(T):
    '''
    Funkcja zwraca współczynnik nieuporządkowania tablicy, na wejściu dostajemy nieuporządkowaną tablice mamy podać takie minimalne k przesunieć które uporządkuje tablice.
    Sortuje po 0 indeksie tupli.
    '''
    n = len(T)
    into_tuples(T)
    T_sorted = mergeSort(T, 0)
    maxi = 0
    for i in range(n):
        maxi = max(T_sorted[i][1], T[i][1])
    return maxi
    
    
T = [0, 2, 1.1, 2]
print(chaos_index(T))