# Lista zawiera niepowtarzające się elementy. Proszę napisać funkcję do której przekazujemy wskaźnik na początek oraz wartość klucza. 
# Jeżeli element o takim kluczu występuje w liście należy go usunąć z listy.
# Jeżeli elementu o zadanym kluczu brak w liście należy element o takim kluczu wstawić do listy.

class Node:
    def __init__(self, val=None):
        self.next = None
        self.val = val

def wypisz(zb):
    while zb != None:
        print(zb.val, end=" ")
        zb = zb.next
        
def create_linked(tab):
    p = Node(tab[0])
    q = p
    for i in range(1, len(tab)):
        p.next = Node(tab[i])
        p = p.next
    return q

def remove_or_insert(head, val):
    p = head
    while p != None:
        if p.val == val:
            p.next = p.next.next
            # return head
        p = p.next
    #val nie ma w liscie
    

p = create_linked([1, 2, 3, 4, 5])
q = remove_or_insert(p, 2)
wypisz(q)