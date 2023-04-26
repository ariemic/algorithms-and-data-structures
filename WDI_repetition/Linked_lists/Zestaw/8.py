# Dana jest niepusta lista, proszę napisać funkcję usuwającą co drugi element listy. Do funkcji należy przekazać wskazanie na pierwszy element listy.
class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
        
def wypisz(zb):
    while zb != None:
        print(zb.val, end="-")
        zb = zb.next
        
def create_linked(tab):
    p = Node(tab[0])
    q = p
    for i in range(1, len(tab)):
        p.next = Node(tab[i])
        p = p.next
    return q


def remove_every_second(p):
    q = p
    while p != None:
        if p.next != None:
            p.next = p.next.next
        p = p.next
    return q



p = create_linked([2, 8, 10, 3, 4, 5])
wypisz(p)
print()
q = remove_every_second(p)
wypisz(q)