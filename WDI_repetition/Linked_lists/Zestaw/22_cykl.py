# Dana jestlista, który być może zakończona jest cyklem. Napisać funkcję, która sprawdza ten fakt.

class Node:
    def __init__(self, val=None, next=None):
        self.next = next
        self.val = val
    
def wypisz(p):
    while p != None:
        print(p.val, end="")
        p = p.next

def czy_cykl(p):
    slow = p
    fast = p
    if slow.next != None and fast.next.next != None:
        slow = slow.next
        fast = fast.next.next
        while slow.next != None and fast.next != None and fast.next.next != None:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
    return False

#JAK NAPISAĆ FUNKCJE KTÓRA TWORZY LINKED LISTE Z CYKLEM?

a = Node(1, None)
b = Node(2, a)
c = Node(3, b)
d = Node(4, c)
e = Node(5, d)
f = Node(6, e)
g = Node(7, f)

wypisz(g)