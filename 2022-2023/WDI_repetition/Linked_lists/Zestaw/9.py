# Dana jest niepusta lista reprezentująca liczbę naturalną. Kolejne elementy listy przechowują kolejne cyfry. Proszę napisać funkcję zwiększającą taką liczbę o 1.
class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
        
def wypisz(zb):
    while zb != None:
        print(zb.val, end="")
        zb = zb.next

def reverse(p):
    if p.next == None:
        return p
    else:
        prev = reverse(p.next)
        q = prev
        while q.next != None:
            q = q.next
        q.next = p
        p.next = None
        return prev
        
def add_one(p):
    #dodaje 1 do odwroconej listy
    q = p
    while q != None:
        if q.val < 9:
            q.val += 1
            return p
        else:
            q = q.next
    #zeruje wszystkie elemnety p i dodaje jak pierwszy element 1, przypadek gdy wszystkie cyfry w liscie byly 9-takami
    q = Node(1)
    r = q
    q.next = p
    while q.next != None:
        q.next.val = 0
        q = q.next
    return r

def create_ll(tab):
    zb = Node(tab[0])
    q = zb
    for i in range(1,len(tab)):
        zb.next = Node(tab[i])
        zb = zb.next
    return q

a = create_ll([1, 3, 5])
b = create_ll([9, 9, 8])
c = create_ll([9,9,9])
wypisz(b)
print()
ra = reverse(a)
rb = reverse(b)
rc = reverse(c)
wypisz(add_one(rc))