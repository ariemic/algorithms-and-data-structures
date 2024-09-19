#1 Merge sort na listach 1 kierunkowych
#Scalanie - zwraca wskazanie na początek i koniec listy
#Odcinanie serii naturalnej - zwraca początek i koniec serii
#Połączenie w całość


class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
        
def wypisz(p):
    while p != None:
        print(p.val, end=" ")
        p = p.next

def create_link(tab):
    p = Node(tab[0])
    q = p
    for i in range(1, len(tab)):
        p.next = Node(tab[i])
        p = p.next
    return q


def merge(p, q):
    #function merge two sorted linked lists
    if p == None:
        return q
    if q == None:
        return p   
    r = Node(None)
    res = r
    while p != None and q != None:
        if p.val <= q.val:
            r.next = p
            p = p.next
            r.next.next = None
        else:
            r.next = q
            q = q.next
            r.next.next = None
        r = r.next
    if p == None:
        r.next = q
    if q == None:
        r.next = p
    return res.next

def split(p):
    if p.next == None:
        return p
    fast = slow = p
    while fast.next != None and fast.next.next != None:
        fast = fast.next.next
        slow = slow.next
    mid = slow.next #wskazanie na połowe listy
    slow.next = None
    return p, mid


def merge_sort(p):# WAŻNE
    if p.next is not None:
        head, tail = split(p)
        head = merge_sort(head)
        tail = merge_sort(tail)
        p = merge(head, tail)
    return p

a = create_link([1, 5, 6, 8])
b = create_link([3, 4, 7, 9, 9])
d = create_link([1, 6, 3, 2, 9, 1, 9])
wypisz(a)
print()
wypisz(b)
c = merge(a, b)
print()
wypisz(c)
print()
x, y = split(c)
print()
wypisz(x)
print()
wypisz(y)
print()
p = merge_sort(d)
wypisz(p)