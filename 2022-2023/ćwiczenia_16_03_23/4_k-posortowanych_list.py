'''
k - posortowanych linked list -> scalić w jedną
'''
class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
        
def wypisz(p):
    while p != None:
        print(p.val, end=" ")
        p = p.next

def create_linked(tab):
    p, n = Node(tab[0]), len(tab)
    q = p
    for i in range(1, n):
        p.next = Node(tab[i])
        p = p.next
    return q

def left(i):
    return 2*i+1
def right(i):
    return 2*i + 2
def parent(i):
    return (i-1)//2

def heapify(A, i, n, idx):
    '''
    KOPIEC MINIMUM dla linkedLists z tuplami
    naprawianie kopca od korzenia, i - indeks elementu który wskazuje na korzeń
    '''
    l = left(i)
    r = right(i)
    min_ind = i
    if l < n and A[l][idx].val < A[min_ind][idx].val: 
        min_ind = l
    if r < n and A[r][idx].val < A[min_ind][idx].val:
        min_ind = r
    if min_ind != i:#jesli indeks z najw wartoscią jest rózny od indeksu korzenia do wymien je
        A[i], A[min_ind] = A[min_ind], A[i] #aktualizacja listy przy korzeniu
        heapify(A, min_ind, n, idx)
    return A

    
def buildheap(A, idx):
    n = len(A)
    for i in range(parent(n-1), -1, -1):
        heapify(A, i, n, idx)
        

a = create_linked([1, 4, 5, 12])
b = create_linked([2, 10, 13, 14, 18])
c = create_linked([5, 17, 23, 42, 189])
d = create_linked([1, 1, 1, 1, 4, 5])
arr = [a, b, c, d]

def insert(arr, heap, idx):
    if arr[idx] != None:
        node = arr[idx]
        arr[idx] = arr[idx].next
        node.next = None
        heap[0] = (node, idx)
        heapify(heap, 0, len(heap), 0)
    else:
        #skracam kopiec o 1 node'a
        heap[0], heap[-1] = heap[-1], heap[0]
        heap.pop()
        heapify(heap, 0, len(heap), 0)
    return heap
    

def merge_K_sortedLL(arr, k):
    '''
    Tworze kopiec o wykości k w którym będę przechowywać pierwszed node'y z każdej linked listy, robie min heapify, usuwam najmniejszego node'a z kopca
    na jego miejsce wstawiam kolejnego node'a z linked listy z której node pochodził.
    k = len(arr)
    '''
    res = Node()
    p = res
    heap = []
    
    if k == 0:
        return res.next
    
    for i in range(k):
        node = arr[i]
        arr[i] = arr[i].next
        node.next = None
        heap.append((node, i)) #i wskazauje na nr linkedlisty z ktorej biore node'a
    if heap == 0:
        return res.next
    buildheap(heap, 0)
    
    while heap:
        #jesli jakaś lista się skonczy to moj kopiec będzie krótszy o 1 na stałe
        p.next = heap[0][0]
        idx = heap[0][1]
        heap = insert(arr, heap, idx)
        p = p.next
    return res.next
            
res = merge_K_sortedLL(arr, 4)
wypisz(res)
    
    
