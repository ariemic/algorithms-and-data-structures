from zad1testy import Node, runtests

class Node1:
    def __init__(self, val=None):
        self.val = val
        self.next = None

def parent(i):
    return (i-1)//2
def left(i):
    return 2*i+1
def right(i):
    return 2*i+2

def min_heapify(T, i, n):
    l = left(i)
    r = right(i)
    min_ind = i
    if l < n and T[l].val < T[min_ind].val:
        min_ind = l
    if r < n and T[r].val < T[min_ind].val:
        min_ind = r
    if min_ind != i:
        T[i], T[min_ind] = T[min_ind], T[i] 
        min_heapify(T, min_ind, n) #napraw popsute mniejsze drzewo, jeśli takie uległo uszkodzeniu

def buildheap(A):
    n = len(A)
    for i in range(parent(n-1), -1, -1):
        min_heapify(A, i, n)
    
def insert(heap):
    n = len(heap)
    i = n-1
    while i > 0 and heap[parent(i)].val > heap[i].val:
        heap[parent(i)], heap[i] = heap[i], heap[parent(i)] 
        i = parent(i)
        

def SortH(p, k):
    #k-chaotyczność - wysokość min-heapa
    q = Node1(None)
    cq = q
    heap = []
    for _ in range(k+1):#create first heap
        data = p
        p = p.next
        data.next = None
        heap.append(data)
        if p == None:
            break
    buildheap(heap)
    while heap:
        q.next = heap[0]
        q = q.next
        if p != None:
            data = p
            p = p.next
            data.next = None
            heap[0] = data
            min_heapify(heap, 0, len(heap))
        else:
            heap[0], heap[-1] = heap[-1], heap[-1]
            heap.pop(-1)
            min_heapify(heap, 0, len(heap))
    return cq.next
    
runtests( SortH ) 
