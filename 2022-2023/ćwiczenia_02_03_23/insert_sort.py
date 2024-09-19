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


def sortedInsert(h, curr):
    if h == None or h.val > curr.val:
        curr.next = h
        return curr
    else:
        tmp = h
        while tmp.next != None and tmp.next.val < curr.val:
            tmp = tmp.next
        
        curr.next = tmp.next
        tmp.next = curr
        return h


# p = create_linked([ 2, 5, 8])
# wypisz(sortedInsert(p, Node(10)))

def insertionSort(p):
    curr = p
    h = None
    while curr != None:
        currNext = curr.next
        h = sortedInsert(h, curr)
        curr = currNext
    return h

p = create_linked([1, 2, 8, 5])
wypisz(insertionSort(p))