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

def merge(p, q):
    if p == None:
        return q
    if q == None:
        return p
    res = Node()
    head = res
    cp, cq = p, q
    while cp != None and cq != None:
        if cp.val <= cq.val:
            res.next = cp
            cp = cp.next
        else:
            res.next = cq
            cq = cq.next
        res = res.next
    #one of the lists is empty, we need to join rest of the second list with the result list
    if cp != None:
        res.next = cp
    if cq != None:
        res.next = cq
    # tail = res.next
    return head.next

def split(p):
    #divide list by half and return indicator for the first element of both lists
    fast = slow = p
    while fast.next != None and fast.next.next != None:
        fast = fast.next.next
        slow = slow.next
    mid = slow.next
    slow.next = None
    return p, mid   

a = create_linked([1, 2, 8, 9])
b = create_linked([2, 5, 7, 9])
head, tail = split(a)
wypisz(head)
print()
wypisz(tail)
print()

def merge_sort(p):
    if p.next != None:
        h, t = split(p)
        mh = merge_sort(h)
        mt = merge_sort(t)
        p = merge(mh, mt)
    return p


def mergeRek(a, b, res):
    if a == None: return b
    if b == None: return a
    if a.val < b.val:
        res = a
        res.next = mergeRek(a.next, b, res.next) #przypisanie jest bardzo wazne 
        #inczaej sie wykrzaczy
    else:
        res = b
        res.next = mergeRek(a, b.next, res.next)
    return res

c = create_linked([1, 2, 8, 3, 5, 9, 9, 10, 2, 0])
wypisz(merge_sort(c))
        
        