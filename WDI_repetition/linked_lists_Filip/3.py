# Proszę napisać funkcję scalającą dwie posortowane listy w jedną
# posortowaną listę. Do funkcji należy przekazać wskazania na pierwsze
# elementy obu list, funkcja powinna zwrócić wskazanie do scalonej listy.
# - funkcja iteracyjna,
# - funkcja rekurencyjna.



class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
#end class

def print_all(p):
    while p is not None:
        print(p.val)
        p = p.next
#end def



def add(p, new_val): #dodawanie rekurencyjne

    if p.next is None:
        q = Node(new_val)
        p.next = q
        return

    elif p.next is not None:

        if p.next.val >= new_val:
            q = Node(new_val)
            q.next = p.next 
            p.next = q
        else:
            add(p.next, new_val)
    #end if 
#end def


def merge(p,q):

    if p is None:
        return q 
    
    if q is None:
        return p
    
    else:
        if p.val <= q.val:
            p.next = merge(p.next, q)
            return p
        else:
            q.next = merge(p, q.next)
            return q