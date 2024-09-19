# Zastosowanie listy odsyłaczowej do implementacji
# tablicy rzadkiej. Proszę napisać trzy funkcje:
# – inicjalizującą tablicę,
# – zwracającą wartość elementu o indeksie n,
# – podstawiającą wartość value pod indeks n.

# Tablica rzadka to tablica, ktora nie w kazdym indeksie ma wartosc ( tam gdzie nie ma jest None)

class Node:
    def __init__(self, val=None, idx = -1):
        self.idx = idx
        self.val = val
        self.next = None
        
def initialize():
    a = Node()
    return a

def retrive_val(zb, id):
    while zb != None and zb.idx < id:
        zb = zb.next 
    if zb == None or zb.idx != id:
        return None
    else:
        return zb.val
    
def set_val(zb, val, id):
    while zb.next != None and zb.next.idx < id:
        zb = zb.next
    if zb.next != None and zb.next.idx == id:
        zb.next.val = val
        return
    p = Node(val, id)
    if zb.next == None:
        zb.next = p
    else:
        #zb.next.idx > el #wstwiam el na koncu listy
        p.next = zb.next
        zb.next = p
        
