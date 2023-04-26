#Proszę napisać funkcję wstawiającą na koniec listy nowy element. Do funkcji należy przekazać wskazanie na pierwszy element listy oraz wstawianą wartość

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
        
def wypisz(zb):
    while zb != None:
        print(zb.val, end="")
        zb = zb.next
    
def wstaw_na_koniec(p, val):
    
    while p.next != None:
        p = p.next
    p.next = Node(val)
    return p

p = Node(1)
p.next = Node(3)
p.next.next = Node(9)
wstaw_na_koniec(p, 8)
wypisz(p)