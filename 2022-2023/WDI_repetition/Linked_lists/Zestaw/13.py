# Proszę napisać funkcję, otrzymującą jako parametr wskaźnik na pierwszy element listy o wartościach typu int,
# usuwającą wszystkie elementy, których wartość jest mniejsza od wartości bezpośrednio poprzedzających je elementów.

class Node:
    def __init__(self, val=None, next=None):
        self.next = next
        self.val = val
    
def wypisz(p):
    while p != None:
        print(p.val, end="")
        p = p.next
        
def create_linked(tab):
    p = Node(tab[0])
    q = p
    for i in range(1, len(tab)):
        p.next = Node(tab[i])
        p = p.next
    return q

p = create_linked([1, 3, 2, 4, 3, 1])
wypisz(p)

def remove_smaller(p):
    prev = p
    curr = prev.next
    prev_val = prev.val
    while curr != None:
        if curr.val < prev_val:
            prev_val = curr.val
            curr = curr.next
            prev.next = curr 
            #nie ma tu dołączanie nieczego do listy, tylko przesuwanie wskaźnika
        else:
           prev_val = curr.val
           prev = prev.next
           curr = curr.next 
    return p



q = remove_smaller(p)
print()
wypisz(q)
        
            
            