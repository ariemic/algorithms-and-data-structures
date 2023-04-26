#c) Posortuj liste przez wybieranie - insertion sort

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


def insertion_sort(A):
    n = len(A)
    for i in range(1, n):
        for j in range(i):
            if A[j] > A[i]:
                A[j], A[i] = A[i], A[j]
            else:
                continue
    return A

# print(insertion_sort([3,5, 1, 2, 9, 10, 23, 2, 1]))
def sortedInsert(h, curr):
    '''
    function iterates through the start of sorted list unitl it finds an element greater than
    current node
    '''
    if h.next == None and h.val > curr.val:
        curr.next = h
        return curr
    q = Node()
    q.next = h
    while q.next != None:
        if q.next.val > curr.val:
            tmp = q.next
            q.next = curr
            curr.next = tmp
            q = q.next
            break
        else:
            q = q.next
    return h
p = create_linked([1, 3, 4, 6, 7])
wypisz(sortedInsert(p, Node(8)))


def insertion_sort_link(p):
    curr = p.next
    h = Node(p.val)
    while curr != None:
        node = curr
        curr = curr.next
        node.next = None
        h = sortedInsert(h, node)
        wypisz(h)
        
    return p
            
# p = create_linked([1, 2, 8, 5])
# wypisz(insertion_sort_link(p))
    
    











