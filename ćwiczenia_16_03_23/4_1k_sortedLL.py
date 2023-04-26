'''
k - posortowanych linked list -> scalić w jedną

NIE DZIAŁĄ

Nie wyciananie node'ów jest łatwiejsze do zrobienia niż korzystanie z przekazywania całych linked lists
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

def heapify(A, i, n):
    '''
    KOPIEC MINIMUM dla linkedLists z tuplami
    naprawianie kopca od korzenia, i - indeks elementu który wskazuje na korzeń
    '''
    l = left(i)
    r = right(i)
    min_ind = i
    if l < n and A[l].val < A[min_ind].val: 
        min_ind = l
    if r < n and A[r].val < A[min_ind].val:
        min_ind = r
    if min_ind != i:#jesli indeks z najw wartoscią jest rózny od indeksu korzenia do wymien je
        A[i], A[min_ind] = A[min_ind], A[i] #aktualizacja listy przy korzeniu
        heapify(A, min_ind, n)
    return A

    
def buildheap(A):
    n = len(A)
    for i in range(parent(n-1), -1, -1):
        heapify(A, i, n)
        

a = create_linked([1, 4, 5, 12])
b = create_linked([2, 10, 13, 14, 18])
c = create_linked([5, 17, 23, 42, 189])
d = create_linked([1, 1, 1, 1, 4, 5])
arr = [a, b, c, d]

def insert(heap, p):
    if heap[0].next != None:
        node = heap[0]
        heap[0] = heap[0].next
        # node.next = None
        # p.next = node
    else:
        node = heap[0]
        heap[0], heap[-1] = heap[-1], heap[0]
        heap.pop()
    node.next = None
    p.next = node
    p = p.next
    return p
    

def merge_K_sortedLL(arr, k):
    '''
    Tworze kopiec o wykości k w którym będę przechowywać pierwszed node'y z każdej linked listy, robie min heapify, usuwam najmniejszego node'a z kopca
    na jego miejsce wstawiam kolejnego node'a z linked listy z której node pochodził.
    k = len(arr)
    '''
    res = Node()
    p = res
    heap = []
    
    for i in range(k):
        heap.append(arr[i]) 
    
    buildheap(heap)
    while heap:
        #jesli jakaś lista się skonczy to moj kopiec będzie krótszy o 1 na stałe
        p = insert(heap, p)
    return res.next
            
res = merge_K_sortedLL(arr, 4)
wypisz(res)