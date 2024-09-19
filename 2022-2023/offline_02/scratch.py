def right(i):
    return 2*i+2
def left(i):
    return 2*i + 1
def parent(i):
    return (i-1)//2

def heapify(S, i, n):
    l = left(i)
    r = right(i)
    max_ind = i
    if l < n and S[l] > S[max_ind]:
        max_ind = l
    if r < n and S[r] > S[max_ind]:
        max_ind = r
    if max_ind != i:
        S[i], S[max_ind] = S[max_ind], S[i]
        heapify(S, max_ind, n)
    return S

def buildheap(S):
    n = len(S)
    for i in range(parent(n-1), -1, -1):
        heapify(S, i, n)


def snow(S):
    '''
    szukam największej wartośi w liscie i wrzucam ją do wierzchołka heapa, nastepnie wrzucam tą wartość na koniec listy i odrazy sumeje, 
    robie swapa jak w heapsorcie z pierwszym elementem listy
    '''
    n = len(S)
    buildheap(S)
    suma = d = 0
    i = n - 1
    while i > 0 and S[0] - d > 0:
        S[0], S[i] = S[i], S[0]
        suma += (S[i] - d)
        d += 1
        heapify(S, 0, i)
        i -= 1
    return suma
        
        