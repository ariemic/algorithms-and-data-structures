#1 Merge sort na listach 1 kierunkowych
#Scalanie
#Odcinanie serii naturalnej - zwraca początek i koniec serii
#Połączenie w całość

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
        
def wypisz(p):
    while p != None:
        print(p.val, end=" ")
        p = p.next

def create_link(tab):
    p = Node(tab[0])
    q = p
    for i in range(1, len(tab)):
        p.next = Node(tab[i])
        p = p.next
    return q
        
def cut(p):
    #z wartownikiem
    q = p
    p = p.next
    if p == None:
        return None, None
    while p.next != None and p.val <= p.next.val:
        p = p.next
    w = q.next #wskaznik na poczatek serii
    q.next = p.next
    p.next = None
    #p - wskaznik na koniec serii
    return w, p
    
def merge(p1, p2):
    #bez wartownika
    t = head = Node(None)
    while p1 and p1:
        if p1.val <= p2.val:
            t.next = p1
            p1 = p1.next
        else:
            t.next = p2
            p2 = p2.next
    t = t.next        
    while p1:
        t.next = p1
        p1 = p1.next
        t = t.next
    while p2:
        t.next = p2
        p2 = p2.next
        t = t.next
    return head.next

def merge_sort(head):
    t = head
    while t.next != None:#t bedzie wskazaniem na koniec listy
        t = t.next
    while True:
        left_head, left_tail = cut(head)
        right_head, right_tail = cut(head)
        if right_head == None:
            head.next = left_head
            return 
        if t == right_tail: 
            t = head
        merged_head, merged_tail = merge(left_head, right_head)
        t.next = merged_head
        t = merged_tail
    
    

a = create_link([1, 5, 6, 8])
b = create_link([3, 4, 7, 9, 9])
wypisz(a)
print()
wypisz(b)
c = merge(a, b)
print()
wypisz(c)   
    
    
    
    
    
    
    
    
    