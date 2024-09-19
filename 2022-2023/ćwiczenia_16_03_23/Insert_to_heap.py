'''
Wstawianie do kopca binarnego
'''
class Heap:
    def __init__(self, n):
        self.T = [0]*n
        self.size = 0
    
def right(i):
    return 2*i+2

def left(i):
    return 2*i+1

def parent(i):
    return (i-1)//2

def heapify(A, i, n):
    l = left(i)
    r = right(i)
    max_ind = i
    if l < n and A[l] > A[max_ind]:
        max_ind = l
    if r < n and A[r] > A[max_ind]:
        max_ind = r
    if max_ind != i:
        A[i], A[max_ind] = A[max_ind], A[i]
        heapify(A, max_ind, n)
        
        
def insert(H, x):
    i = H.size
    p = parent(H.size)
    H.T[H.size] = x
    H.size += 1
    while p >= 0:
        if H.T[p] < H.T[i]:
            H.T[p], H.T[i] = H.T[i], H.T[p] 
        else:
            break
        i = p
        p = parent(p)