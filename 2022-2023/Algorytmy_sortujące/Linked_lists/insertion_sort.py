
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


def insertToSorted(h, curr):
    #takes head of the sorted array, and pointer for node to insert in good place
    if h == None or h.val > curr.val:
        curr.next = h
        return curr
    q = h
    while h.next != None and h.next.val < curr.val:
        h = h.next
    Next = h.next
    h.next = curr
    curr.next = Next
    return q

p = create_linked([2, 7, 12, 1, 7])
# wypisz(insertToSorted(p, Node(5)))

def insertion_sort(p):
    h = None #pointer for sorted array
    while p != None:
        curr = p
        p = p.next
        curr.next = None
        h = insertToSorted(h, curr)
    return h

wypisz(insertion_sort(p))