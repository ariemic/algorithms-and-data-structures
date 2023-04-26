#Proszę napisać funkcję usuwającą ostatni element listy. Do funkcji należy przekazać wskazanie na pierwszy element listy

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
        
def wypisz(zb):
    while zb != None:
        print(zb.val, end="")
        zb = zb.next

def usun_z_konca(p):
    if p == None:
        return None
    prev = None
    while p.next != None:
        prev = p #guardian przejume wskazanie na kolejny element    
        p = p.next
    prev.next = None # powoduje ze prev przestaje wskazywac na kolejne elementy listy p
    return prev
       
    
def remove_last(p):
    if p == None:
        return None
    else:
        prev = None
        while p.next != None:
            prev = p #przypisuje zmiennej prev cała liste p, NIE MOGE NAPISAC PREV.NEXT BO W TYM MOMENCIE PREV NIE BYLO WSKAZNIKIEM NA LISTE
            p = p.next
        prev.next = None #IMPORTANT
        return prev



p = Node(1)
p.next = Node(3)
p.next.next = Node(9)
p.next.next.next = Node(2)
remove_last(p)
wypisz(p)