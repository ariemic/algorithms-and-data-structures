# Proszę napisać funkcję, która otrzymując jako parametr wskazujący na początek listy jednokierunkowej, 
# usuwa z niej wszystkie elementy, w których wartość klucza w zapisie binarnym ma nieparzystą ilość jedynek

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


def is_odd_ones(n):
    cnt = 0
    while n != 0:
        if n%2 == 1: cnt +=1
        n //= 2
    return cnt%2 == 1 

#dla listy jednokierunkowej
def remove(head):
    prev = head
    curr = prev.next
    while curr != None:
        if not is_odd_ones(prev.val):
            prev.next = curr
            prev = prev.next
        else:
            prev.val = curr.val
        curr = curr.next     
    prev.next = None
    return head


def remove(head):
    prev = head
    curr = prev.next
    while curr != None:
        if is_odd_ones(prev.val) == False:
            prev.next = curr
            prev = prev.next
        else:
            prev.val = curr.val #usuwamy połączenie w liscie zmieniajac wartosc w prev
        curr = curr.next
    prev.next = None #usuwamy wszystko co zostało nie dołączone do listy
    return head
            




p = create_linked([1, 2, 3, 8, 9])#res ->3, 9
wypisz(p)
print()
q = remove(p)
wypisz(q)